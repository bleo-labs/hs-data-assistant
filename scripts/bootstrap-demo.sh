#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="${1:-$PWD}"
TARGET_ROOT="$WORKSPACE_ROOT/business_graphs"
DEMO_ID="demo-two-sided-market"
SOURCE_ROOT="$PACKAGE_ROOT/examples/business_graphs"

if [ -e "$TARGET_ROOT/$DEMO_ID" ]; then
  echo "Demo already exists: $TARGET_ROOT/$DEMO_ID"
  echo "Nothing was changed. Remove or rename that directory before bootstrapping again."
  exit 1
fi

mkdir -p "$TARGET_ROOT"
cp -R "$SOURCE_ROOT/$DEMO_ID" "$TARGET_ROOT/$DEMO_ID"

REGISTRY="$TARGET_ROOT/registry.md"
if [ ! -f "$REGISTRY" ]; then
  cp "$SOURCE_ROOT/registry.md" "$REGISTRY"
elif ! grep -q "\`$DEMO_ID\`" "$REGISTRY"; then
  printf '\n| `%s` | 双边撮合示例业务 | demo marketplace | demo | `%s/manifest.md` |\n' "$DEMO_ID" "$DEMO_ID" >> "$REGISTRY"
fi

echo "Demo business graph created at: $TARGET_ROOT/$DEMO_ID"
echo "Registry updated at: $REGISTRY"
echo 'Next: connect the copied demo graph to your AI workspace, then start with hs-entry and a demo analysis question.'
