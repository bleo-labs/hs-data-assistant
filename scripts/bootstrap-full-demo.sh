#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET="${1:-$HOME/HS_Public_Demo_Workspace}"
TEMPLATE_ROOT="$PACKAGE_ROOT/templates/full-demo-workspace"
GRAPH_SOURCE="$PACKAGE_ROOT/examples/business_graphs/demo-omnichannel-retail"

if [ -e "$TARGET" ] && [ -n "$(find "$TARGET" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
  echo "Target is not empty: $TARGET"
  echo "Nothing was changed. Choose an empty directory or use reset-full-demo.sh explicitly."
  exit 1
fi

mkdir -p "$TARGET"
cp -R "$TEMPLATE_ROOT"/. "$TARGET"/
mkdir -p \
  "$TARGET/.agents/skills" \
  "$TARGET/business_graphs/demo-omnichannel-retail" \
  "$TARGET/demo_projects/active" \
  "$TARGET/demo_projects/completed" \
  "$TARGET/outputs/reports" \
  "$TARGET/outputs/spreadsheets" \
  "$TARGET/outputs/charts" \
  "$TARGET/outputs/feedback" \
  "$TARGET/exports" \
  "$TARGET/recordings" \
  "$TARGET/temp"

for skill_dir in "$PACKAGE_ROOT"/skills/hs-*; do
  skill_name="$(basename "$skill_dir")"
  cp -R "$skill_dir" "$TARGET/.agents/skills/$skill_name"
done

(
  cd "$GRAPH_SOURCE"
  tar --exclude='.DS_Store' --exclude='.obsidian' --exclude='__pycache__' -cf - .
) | (
  cd "$TARGET/business_graphs/demo-omnichannel-retail"
  tar -xf -
)

find "$TARGET" -name '.DS_Store' -delete
find "$TARGET" -type d -name '__pycache__' -prune -exec rm -rf {} +
printf '%s\n' 'hs-public-demo-workspace-v1' > "$TARGET/.hs-public-demo-workspace"

python3 "$PACKAGE_ROOT/scripts/validate-public-demo-workspace.py" "$TARGET"

echo "Hs public demo workspace created at: $TARGET"
echo "Start from: $TARGET/business_graphs/demo-omnichannel-retail/tasks/README.md"
