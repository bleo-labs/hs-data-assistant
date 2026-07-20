#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
TARGET="$CODEX_HOME/skills"
BACKUP_ROOT="$TARGET/.hs-sync-backups/$(date +%Y%m%d-%H%M%S)"

mkdir -p "$TARGET"

for skill_dir in "$PACKAGE_ROOT"/skills/hs-*; do
  skill_name="$(basename "$skill_dir")"
  if [ -e "$TARGET/$skill_name" ]; then
    mkdir -p "$BACKUP_ROOT"
    mv "$TARGET/$skill_name" "$BACKUP_ROOT/$skill_name"
  fi
  cp -R "$skill_dir" "$TARGET/$skill_name"
  find "$TARGET/$skill_name" -name ".DS_Store" -delete
  echo "Synced $skill_name"
done

echo "Hs skills synced to $TARGET"
if [ -d "$BACKUP_ROOT" ]; then
  echo "Previous Hs skills backed up to $BACKUP_ROOT"
fi
