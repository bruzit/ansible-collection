#!/usr/bin/env python3
import argparse
import concurrent.futures
import ipaddress
import json
import os
import re
import socket
import subprocess
import sys
import threading
import time

SPEC = "/etc/molecule-traffic.json"
TIMEOUT = 3
# Below the 1 s initial RTO: one SYN, so one log token, per dropped TCP probe
CONNECT_TIMEOUT = 0.8


def load():
    with open(SPEC, encoding="utf-8") as spec:
        return json.load(spec)


def target(probe):
    return probe.get("to") or {"out": "peer", "in": "host", "lo": "lo"}[probe["direction"]]


def source(probe):
    return "host" if probe["direction"] in ("out", "lo") else probe.get("from", "peer")


def tcp_server(sock):
    while True:
        sock.accept()[0].close()


def udp_server(sock):
    while True:
        data, peer = sock.recvfrom(512)
        sock.sendto(data, peer)


def serve(name):
    spec = load()
    threads = []
    ports = {
        (p["proto"], p["port"])
        for p in spec["probes"]
        if target(p) == name and p["proto"] in ("tcp", "udp") and p["expect"] != "refused"
    }
    for proto, port in sorted(ports):
        sock = socket.socket(
            socket.AF_INET6, socket.SOCK_STREAM if proto == "tcp" else socket.SOCK_DGRAM
        )
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if "dev" in spec["targets"][name]:
            sock.setsockopt(
                socket.SOL_SOCKET, socket.SO_BINDTODEVICE, spec["targets"][name]["dev"].encode()
            )
        try:
            sock.bind(("::", port))
        except OSError as err:
            # A real daemon such as sshd already listens
            print(f"{proto}/{port}: {err}", file=sys.stderr)
            continue
        if proto == "tcp":
            sock.listen()
        threads.append(
            threading.Thread(target=tcp_server if proto == "tcp" else udp_server, args=(sock,))
        )
    for thread in threads:
        thread.start()
    if os.environ.get("NOTIFY_SOCKET"):
        with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as notify:
            notify.sendto(b"READY=1", os.environ["NOTIFY_SOCKET"])
    for thread in threads:
        thread.join()


def attempt(probe):
    if probe["proto"] == "icmp":
        ping = subprocess.run(
            ["ping", "-c", "1", "-W", str(TIMEOUT), probe["addr"]], capture_output=True, check=False
        )
        return "pass" if ping.returncode == 0 else "drop"
    family = socket.AF_INET6 if ":" in probe["addr"] else socket.AF_INET
    kind = socket.SOCK_STREAM if probe["proto"] == "tcp" else socket.SOCK_DGRAM
    with socket.socket(family, kind) as sock:
        sock.settimeout(CONNECT_TIMEOUT if kind == socket.SOCK_STREAM else TIMEOUT)
        if "sport" in probe:
            # Shared with the listener on the same port; the connected probe socket gets the reply
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("", probe["sport"]))
        try:
            sock.connect((probe["addr"], probe["port"]))
            if kind == socket.SOCK_DGRAM:
                sock.send(b"probe")
                sock.recv(512)
        # EPERM: dropped by the local output hook
        except (TimeoutError, PermissionError):
            return "drop"
        except ConnectionRefusedError:
            return "refused"
    return "pass"


def attempt_all(probes):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(probes) or 1) as pool:
        return list(pool.map(attempt, probes))


def journal(*args):
    return subprocess.run(
        ["journalctl", "-k", "-q", "--no-pager", "-o", "cat", *args],
        capture_output=True, text=True, check=True,
    ).stdout


def reset(targets):
    # Each round starts with fresh neighbour discovery and no conntrack entries left by an earlier one
    for t in targets.values():
        if "netns" not in t:
            continue
        subprocess.run(["ip", "-n", t["netns"], "neigh", "flush", "dev", "eth0"], check=True)
        subprocess.run(["ip", "neigh", "flush", "dev", t["link"]], check=True)
        for family in t.keys() & {"ipv4", "ipv6"}:
            for match in ("-s", "-d"):
                # Exits non-zero when nothing matched
                subprocess.run(["conntrack", "-D", "-f", family, match, t[family]], capture_output=True, check=False)


def probe(mode, without):
    spec = load()
    targets = spec["targets"]
    probes = []
    for p in spec["probes"]:
        if without and p.get("rules") != without or not {source(p), target(p)} <= targets.keys():
            continue
        blocked = p["expect"] == "drop" or without is not None
        expect = p["expect"]
        if blocked:
            expect = "pass" if mode == "audit" else "drop"
        addr = targets[target(p)][p["family"]]
        probes.append(dict(
            p,
            addr=addr,
            label=f"{p['direction']} {p['proto']}/{p.get('port', '-')} {p['family']} {source(p)}>{target(p)}"
            + (f" sport {p['sport']}" if "sport" in p else ""),
            expect=expect,
            log=blocked and mode != "quiet",
            pattern=(
                f"bruzit-drop-{p['direction']}: .* DST={ipaddress.ip_address(addr).exploded} .*"
                f"PROTO={p['proto'].upper()} SPT={p.get('sport', '[0-9]+')} DPT={p.get('port')} "
            ),
        ))
    groups = {}
    for p in probes:
        groups.setdefault(source(p), []).append(p)

    reset(targets)
    cursor = journal("-n", "1", "--show-cursor").rsplit("-- cursor: ", 1)[1].strip()
    children = {
        name: subprocess.Popen(
            ["ip", "netns", "exec", targets[name]["netns"], sys.executable, __file__, "attempt", json.dumps(batch)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        for name, batch in groups.items()
        if name != "host"
    }
    results = {"host": attempt_all(groups.get("host", []))}
    for name, child in children.items():
        out, err = child.communicate()
        if child.returncode:
            sys.exit(f"probes from {name} failed with rc {child.returncode}: {err}")
        results[name] = json.loads(out)
    for name, batch in groups.items():
        for p, result in zip(batch, results[name]):
            p["result"] = result

    deadline = time.monotonic() + 10
    while True:
        # Kernel log lines lag behind the packets, also when none are expected
        time.sleep(1)
        log = journal("--after-cursor", cursor)
        for p in probes:
            p["logged"] = re.search(p["pattern"], log) is not None
        if all(p["logged"] or not p["log"] for p in probes) or time.monotonic() > deadline:
            break

    json.dump([{k: v for k, v in p.items() if k not in ("addr", "pattern")} for p in probes], sys.stdout)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("serve").add_argument("name")
    sub.add_parser("attempt").add_argument("probes")
    run = sub.add_parser("probe")
    run.add_argument("--mode", required=True)
    run.add_argument("--without")
    args = parser.parse_args()
    if args.command == "serve":
        serve(args.name)
    elif args.command == "attempt":
        json.dump(attempt_all(json.loads(args.probes)), sys.stdout)
    else:
        probe(args.mode, args.without)


if __name__ == "__main__":
    main()
