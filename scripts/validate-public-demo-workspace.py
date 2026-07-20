#!/usr/bin/env python3
from pathlib import Path
import csv
import json
import re
import subprocess
import sys


PRIVATE_PATTERNS = [
    r"/Users/[^/]+/",
    r"file:///",
    r"[A-Za-z]:\\Users\\[^\\]+\\",
    r"(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{12,}",
    r"(?<![A-Za-z0-9])(?:gh[pousr]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate-public-demo-workspace.py <workspace>")

    root = Path(sys.argv[1]).expanduser().resolve()
    graph = root / "business_graphs" / "demo-omnichannel-retail"
    required = [
        root / ".hs-public-demo-workspace",
        root / "AGENTS.md",
        root / "README.md",
        root / "business_graphs" / "registry.md",
        graph / "manifest.md",
        graph / "indexes" / "METRIC_INDEX.md",
        graph / "tasks" / "README.md",
        graph / "datasets" / "audit" / "data_generation_audit.md",
    ]
    for path in required:
        if not path.exists():
            fail(f"missing workspace asset: {path.relative_to(root)}")

    skills = sorted((root / ".agents" / "skills").glob("hs-*/SKILL.md"))
    if len(skills) != 10:
        fail(f"expected 10 Hs skills, found {len(skills)}")

    if any(path.is_symlink() for path in root.rglob("*")):
        fail("workspace contains symlinks and is not isolated")

    regex = re.compile("|".join(PRIVATE_PATTERNS), re.IGNORECASE)

    def check_value(path: Path, value: str) -> None:
        if regex.search(value):
            fail(f"private term found in {path.relative_to(root)}")
        if "/Users/" in value or "file:///" in value:
            fail(f"absolute local path found in {path.relative_to(root)}")

    def check_json(path: Path) -> None:
        payload = json.loads(path.read_text(encoding="utf-8"))

        def walk(value: object) -> None:
            if isinstance(value, str):
                check_value(path, value)
            elif isinstance(value, dict):
                for key, item in value.items():
                    walk(str(key))
                    walk(item)
            elif isinstance(value, list):
                for item in value:
                    walk(item)

        walk(payload)

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".py", ".sh", ".json", ".csv"}:
            continue
        if path.suffix == ".csv":
            with path.open(encoding="utf-8", errors="ignore", newline="") as handle:
                for row in csv.reader(handle):
                    for value in row:
                        value = value.strip()
                        if value and not re.fullmatch(r"-?\d+(?:\.\d+)?", value):
                            check_value(path, value)
        elif path.suffix == ".json":
            check_json(path)
        else:
            check_value(path, path.read_text(encoding="utf-8", errors="ignore"))

    audit = subprocess.run(
        [sys.executable, str(graph / "generator" / "validate_demo_data.py")],
        cwd=graph,
        capture_output=True,
        text=True,
        check=False,
    )
    if audit.returncode != 0:
        print(audit.stdout)
        print(audit.stderr)
        fail("copied demo data audit failed")

    evidence = subprocess.run(
        [sys.executable, str(graph / "generator" / "build_demo_task_evidence.py")],
        cwd=graph,
        capture_output=True,
        text=True,
        check=False,
    )
    if evidence.returncode != 0:
        print(evidence.stdout)
        print(evidence.stderr)
        fail("copied demo task evidence build failed")

    if "release_ready: yes" not in (graph / "datasets" / "audit" / "data_generation_audit.md").read_text(encoding="utf-8"):
        fail("copied demo data is not release-ready")

    print(f"PASS: isolated public demo workspace at {root}")


if __name__ == "__main__":
    main()
