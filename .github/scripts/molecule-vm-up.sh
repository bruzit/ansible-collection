#!/bin/bash
# Boots an Ubuntu cloud-image VM for molecule's delegated driver.
# QEMU user-mode networking + hostfwd -> fixed localhost port. No libvirt.
set -euo pipefail

WORK=/tmp/molecule-vm
mkdir -p "$WORK"; cd "$WORK"

[ -f key ] || ssh-keygen -t ed25519 -N '' -f key
PUBKEY=$(cat key.pub)

cat > user-data <<EOF
#cloud-config
ssh_authorized_keys:
  - $PUBKEY
package_update: false
EOF

declare -A IMAGES=( [ubuntu-24]=24.04 [ubuntu-26]=26.04 )
declare -A PORTS=(  [ubuntu-24]=2404  [ubuntu-26]=2604  )

for vm in "${!IMAGES[@]}"; do
  ver=${IMAGES[$vm]}; port=${PORTS[$vm]}

  # Cached by actions/cache; only download and verify on miss.
  if [ ! -f "$vm.img" ]; then
    curl -fL --retry 3 -o "$vm.img" \
      "https://cloud-images.ubuntu.com/releases/$ver/release/ubuntu-$ver-server-cloudimg-amd64.img"
    curl -fL --retry 3 -o "$vm.sums" \
      "https://cloud-images.ubuntu.com/releases/$ver/release/SHA256SUMS"
    sha=$(awk -v f="ubuntu-$ver-server-cloudimg-amd64.img" '$2 == f || $2 == "*" f {print $1}' "$vm.sums")
    [ -n "$sha" ] || { echo "ERROR: no checksum for $vm.img in SHA256SUMS" >&2; exit 1; }
    echo "$sha  $vm.img" | sha256sum -c -
  fi

  printf 'instance-id: %s\nlocal-hostname: %s\n' "$vm" "$vm" > meta-data
  cloud-localds "$vm-seed.iso" user-data meta-data

  # Writable overlay so the base image stays clean across re-runs.
  rm -f "$vm-overlay.qcow2"
  qemu-img create -f qcow2 -F qcow2 -b "$WORK/$vm.img" "$vm-overlay.qcow2" 10G

  qemu-system-x86_64 \
    -enable-kvm -cpu host -smp 2 -m 2048 \
    -drive "file=$vm-overlay.qcow2,format=qcow2,if=virtio" \
    -drive "file=$vm-seed.iso,format=raw,if=virtio" \
    -netdev "user,id=net0,hostfwd=tcp::$port-:22" \
    -device "virtio-net-pci,netdev=net0" \
    -display none -serial "file:$vm.serial.log" -daemonize -pidfile "$vm.pid"
done

# Wait for SSH on each VM (can take ~30-90s).
for vm in "${!PORTS[@]}"; do
  port=${PORTS[$vm]}
  for i in $(seq 1 120); do
    if ssh -i key -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
         -o ConnectTimeout=5 -p "$port" ubuntu@127.0.0.1 'true' 2>/dev/null; then
      echo "$vm ready (after ${i}x5s)"; break
    fi
    [ "$i" -eq 120 ] && { echo "ERROR: $vm not up within 10m" >&2; exit 1; }
    sleep 5
  done
done
