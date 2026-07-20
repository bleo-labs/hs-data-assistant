#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-$HOME/HS_Public_Demo_Workspace}"
CONFIRM="${2:-}"

if [ ! -f "$TARGET/.hs-public-demo-workspace" ]; then
  echo "Refusing to reset an unrecognized directory: $TARGET"
  exit 1
fi

if [ "$CONFIRM" != "--yes" ]; then
  echo "Reset is destructive. Run again with --yes after checking your outputs, exports, and recordings."
  exit 1
fi

BACKUP="${TARGET%/}-outputs-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP"
for name in outputs exports recordings; do
  if [ -d "$TARGET/$name" ]; then
    cp -R "$TARGET/$name" "$BACKUP/$name"
  fi
done

rm -rf "$TARGET"
"$SCRIPT_DIR/bootstrap-full-demo.sh" "$TARGET"

echo "Previous public outputs were backed up to: $BACKUP"
