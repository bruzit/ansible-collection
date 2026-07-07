#!/bin/bash
# Tears down VMs booted by molecule-vm-up.sh.
set -uxo pipefail

WORK=/tmp/molecule-vm
for pid in "$WORK"/*.pid; do
  [ -f "$pid" ] || continue
  kill "$(cat "$pid")" 2>/dev/null || true
done
exit 0
