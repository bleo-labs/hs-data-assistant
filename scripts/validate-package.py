#!/usr/bin/env python3
from pathlib import Path
import csv
from datetime import date
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_PRIVATE_PATTERNS = [
    r"/Users/[^/]+/",
    r"file:///",
    r"[A-Za-z]:\\Users\\[^\\]+\\",
    r"(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{12,}",
    r"(?<![A-Za-z0-9])(?:gh[pousr]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})",
]

ALLOW_PRIVATE_IN = {
    "scripts/validate-package.py",
    "scripts/validate-public-demo-workspace.py",
}


def load_private_patterns() -> list[str]:
    patterns = list(DEFAULT_PRIVATE_PATTERNS)
    configured = os.environ.get("HS_PRIVATE_TERMS_FILE")
    local_file = Path(configured).expanduser() if configured else ROOT / "private" / "private-terms.txt"
    if local_file.exists():
        for line in local_file.read_text(encoding="utf-8").splitlines():
            term = line.strip()
            if term and not term.startswith("#"):
                patterns.append(re.escape(term))
        print(f"OK: loaded local private-term denylist from {local_file}")
    return patterns


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def check_skill_frontmatter() -> None:
    skill_files = sorted((ROOT / "skills").glob("hs-*/SKILL.md"))
    if not skill_files:
        fail("no hs skills found")
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---") or "\n---" not in text[3:]:
            fail(f"invalid frontmatter: {path.relative_to(ROOT)}")
        header = text.split("---", 2)[1]
        if "name:" not in header or "description:" not in header:
            fail(f"missing name or description: {path.relative_to(ROOT)}")
    print(f"OK: {len(skill_files)} skill frontmatter files")


def check_skill_interface_metadata() -> None:
    skill_dirs = sorted((ROOT / "skills").glob("hs-*"))
    for skill_dir in skill_dirs:
        metadata_path = skill_dir / "agents" / "openai.yaml"
        if not metadata_path.exists():
            fail(f"missing UI metadata: {metadata_path.relative_to(ROOT)}")
        text = metadata_path.read_text(encoding="utf-8")
        required = ("interface:", "display_name:", "short_description:", "default_prompt:", "policy:")
        if not all(field in text for field in required):
            fail(f"incomplete UI metadata: {metadata_path.relative_to(ROOT)}")
        if f"${skill_dir.name}" not in text:
            fail(f"default prompt does not name skill: {metadata_path.relative_to(ROOT)}")
    print(f"OK: {len(skill_dirs)} skill UI metadata files")


def check_private_terms() -> None:
    regex = re.compile("|".join(load_private_patterns()), re.IGNORECASE)
    hits = []

    def scan_text(path: Path, text: str) -> None:
        for i, line in enumerate(text.splitlines(), 1):
            if regex.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{i}: {line.strip()}")

    def scan_csv(path: Path) -> None:
        with path.open(encoding="utf-8", errors="ignore", newline="") as handle:
            for row_number, row in enumerate(csv.reader(handle), 1):
                for value in row:
                    value = value.strip()
                    if not value or re.fullmatch(r"-?\d+(?:\.\d+)?", value):
                        continue
                    if regex.search(value):
                        hits.append(f"{path.relative_to(ROOT)}:{row_number}: {value}")

    def scan_json(path: Path) -> None:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            scan_text(path, path.read_text(encoding="utf-8", errors="ignore"))
            return

        def walk(value: object) -> None:
            if isinstance(value, str) and regex.search(value):
                hits.append(f"{path.relative_to(ROOT)}: {value}")
            elif isinstance(value, dict):
                for key, item in value.items():
                    walk(str(key))
                    walk(item)
            elif isinstance(value, list):
                for item in value:
                    walk(item)

        walk(payload)

    def scan_xlsx(path: Path) -> None:
        try:
            with zipfile.ZipFile(path) as workbook:
                for member in workbook.namelist():
                    if member == "xl/sharedStrings.xml" or member.startswith("xl/comments"):
                        text = workbook.read(member).decode("utf-8", errors="ignore")
                        if regex.search(text):
                            hits.append(f"{path.relative_to(ROOT)}:{member}: matched private term")
        except zipfile.BadZipFile:
            hits.append(f"{path.relative_to(ROOT)}: invalid xlsx archive")

    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in {".git", ".obsidian", "outputs", "private"}:
            continue
        if str(rel) in ALLOW_PRIVATE_IN:
            continue
        if path.suffix in {".md", ".yaml", ".yml", ".py", ".sh", ".html"}:
            scan_text(path, path.read_text(encoding="utf-8", errors="ignore"))
        elif path.suffix == ".csv":
            scan_csv(path)
        elif path.suffix == ".json":
            scan_json(path)
        elif path.suffix == ".xlsx":
            scan_xlsx(path)
    if hits:
        print("\n".join(hits))
        fail("private or concrete-business terms found")
    print("OK: no private terms, local paths, or credential patterns found")


def check_package_contract() -> None:
    required = [
        "README.md",
        "LICENSE",
        "AGENTS.md",
        "private-terms.example",
        "docs/install.md",
        "docs/quickstart.md",
        "docs/architecture.md",
        "docs/full-demo-walkthrough.md",
        "docs/release-checklist.md",
        "scripts/bootstrap-full-demo.sh",
        "scripts/reset-full-demo.sh",
        "scripts/validate-public-demo-workspace.py",
        "templates/business_graphs/registry.md",
        "templates/business_graphs/_template/manifest.md",
        "templates/full-demo-workspace/AGENTS.md",
        "templates/full-demo-workspace/README.md",
        "templates/full-demo-workspace/business_graphs/registry.md",
        "examples/business_graphs/registry.md",
        "templates/feedback/feedback_card.md",
        "templates/feedback/regression_case.md",
        "templates/run/run_record.md",
        "skills/hs-entry/references/run-record-contract.md",
        "skills/hs-feedback/references/regression-workflow.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"missing required file: {rel}")
    print("OK: package contract files exist")


def check_local_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    failures = []

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for target in link_pattern.findall(text):
            target = target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if not local_target:
                continue
            destination = (path.parent / local_target).resolve()
            if not destination.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {target}")

    if failures:
        print("\n".join(failures))
        fail("broken local markdown links found")
    print("OK: local markdown links resolve")


def check_feedback_loop_contract() -> None:
    skill_files = sorted((ROOT / "skills").glob("hs-*/SKILL.md"))
    missing_run_record = []
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if "run_record" not in text or "run-record-contract.md" not in text:
            missing_run_record.append(str(path.relative_to(ROOT)))

    if missing_run_record:
        fail(f"skills missing run-record contract: {', '.join(missing_run_record)}")

    feedback = (ROOT / "skills" / "hs-feedback" / "SKILL.md").read_text(encoding="utf-8")
    required_feedback_rules = (
        "首次偏离",
        "形成修改提案并等待确认",
        "回写并回归验证",
        "regression-workflow.md",
    )
    if not all(rule in feedback for rule in required_feedback_rules):
        fail("hs-feedback is missing controlled writeback or regression rules")

    print(f"OK: {len(skill_files)} skills share the run-record and controlled-feedback contract")


def check_demo_contract() -> None:
    demo_root = ROOT / "examples" / "business_graphs" / "demo-two-sided-market"
    registry = ROOT / "examples" / "business_graphs" / "registry.md"
    source_card = demo_root / "sources" / "SRC-0001-demo-monthly-metrics.md"
    data_file = demo_root / "datasets" / "raw" / "demo_monthly_metrics.csv"
    required_fields = {
        "month",
        "supply_type",
        "c_intent_users",
        "b_active_supply",
        "effective_matches",
        "single_match_revenue",
        "revenue",
    }

    for path in (demo_root / "manifest.md", registry, source_card, data_file):
        if not path.exists():
            fail(f"missing demo asset: {path.relative_to(ROOT)}")

    registry_text = registry.read_text(encoding="utf-8")
    if "`demo-two-sided-market`" not in registry_text or "`demo-two-sided-market/manifest.md`" not in registry_text:
        fail("demo registry entry does not point to the demo manifest")

    source_text = source_card.read_text(encoding="utf-8")
    if "`datasets/raw/demo_monthly_metrics.csv`" not in source_text:
        fail("demo source card does not point to the demo data file")

    with data_file.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
        headers = set(rows[0].keys()) if rows else set()

    if not rows or not required_fields.issubset(headers):
        fail("demo data file is empty or missing required fields")
    print("OK: demo graph, source card, and data file are runnable")


def check_retail_demo_contract() -> None:
    demo_root = ROOT / "examples" / "business_graphs" / "demo-omnichannel-retail"
    sources = {
        "SRC-0001-channel-traffic-funnel.md": "channel_traffic_funnel_monthly.csv",
        "SRC-0002-product-behavior-funnel.md": "product_behavior_funnel_monthly.csv",
        "SRC-0003-order-transactions.md": "order_transactions_monthly.csv",
        "SRC-0004-product-inventory.md": "product_inventory_monthly.csv",
        "SRC-0005-financial-results.md": "financial_results_monthly.csv",
        "SRC-0006-marketing-campaigns.md": "marketing_campaigns_monthly.csv",
        "SRC-0007-fulfillment.md": "fulfillment_monthly.csv",
        "SRC-0008-dimension-mappings.md": "dimension_mappings.csv",
    }

    for source_name, data_name in sources.items():
        source_path = demo_root / "sources" / source_name
        data_path = demo_root / "datasets" / "raw" / data_name
        for path in (source_path, data_path):
            if not path.exists():
                fail(f"missing retail demo asset: {path.relative_to(ROOT)}")
        source_text = source_path.read_text(encoding="utf-8")
        if f"datasets/raw/{data_name}" not in source_text:
            fail(f"retail Source card does not bind its data file: {source_path.relative_to(ROOT)}")

    bindings = (demo_root / "bindings" / "BINDINGS.md").read_text(encoding="utf-8")
    for source_name in sources:
        source_id = source_name.split("-", 2)[:2]
        source_id = "-".join(source_id)
        if f"`{source_id}`" not in bindings:
            fail(f"retail Source is absent from node bindings: {source_id}")

    audit_script = demo_root / "generator" / "validate_demo_data.py"
    result = subprocess.run(
        [sys.executable, str(audit_script)],
        cwd=demo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        fail("retail demo independent data audit failed")

    audit_report = demo_root / "datasets" / "audit" / "data_generation_audit.md"
    if "release_ready: yes" not in audit_report.read_text(encoding="utf-8"):
        fail("retail demo audit report is not release-ready")

    normal_path = demo_root / "datasets" / "raw" / "order_transactions_monthly.csv"
    bad_path = demo_root / "datasets" / "bad_samples" / "order_transactions_missing_refund_amount.csv"
    if not bad_path.exists():
        fail("retail demo isolated bad sample is missing")
    with normal_path.open(encoding="utf-8", newline="") as handle:
        normal_fields = set(next(csv.reader(handle)))
    with bad_path.open(encoding="utf-8", newline="") as handle:
        bad_fields = set(next(csv.reader(handle)))
    if "refund_amount" not in normal_fields or "refund_amount" in bad_fields:
        fail("retail demo bad sample is not isolated from the normal Source contract")

    print("OK: retail demo has 8 bound Sources and passes the independent data audit")


def check_retail_demo_tasks() -> None:
    demo_root = ROOT / "examples" / "business_graphs" / "demo-omnichannel-retail"
    task_root = demo_root / "tasks"
    task_files = [
        "TASK-0001-may-decline.md",
        "TASK-0002-region-performance.md",
        "TASK-0003-target-pressure.md",
        "TASK-0004-new-category.md",
        "TASK-0005-source-error.md",
    ]
    answer_files = [
        "ANSWER-0001-may-decline.md",
        "ANSWER-0002-region-performance.md",
        "ANSWER-0003-target-pressure.md",
        "ANSWER-0004-new-category.md",
        "ANSWER-0005-source-error.md",
    ]
    for filename in task_files:
        if not (task_root / filename).exists():
            fail(f"missing retail demo task: {filename}")
    for filename in answer_files:
        if not (task_root / "expected_answers" / filename).exists():
            fail(f"missing retail demo answer: {filename}")

    task_text = "\n".join((task_root / filename).read_text(encoding="utf-8") for filename in task_files)
    for intensity in ("轻量", "标准", "重型"):
        if f"强度：{intensity}" not in task_text:
            fail(f"retail demo has no {intensity} task")

    evidence_script = demo_root / "generator" / "build_demo_task_evidence.py"
    result = subprocess.run(
        [sys.executable, str(evidence_script)],
        cwd=demo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        fail("retail demo evidence build failed")

    evidence_path = task_root / "evidence" / "task_evidence.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    case_01 = evidence["case_01"]
    case_02 = evidence["case_02"]["regions"]
    case_03 = evidence["case_03"]
    if not (
        case_01["net_sales"]["delta"] < 0
        and abs(case_01["east_small_appliance"]["delta"]) > abs(case_01["net_sales"]["delta"])
        and case_01["paid_app_traffic"]["2026-05"]["visit_users"]
        > case_01["paid_app_traffic"]["2026-04"]["visit_users"]
        and case_01["paid_app_traffic"]["2026-05"]["visit_to_detail_rate"]
        < case_01["paid_app_traffic"]["2026-04"]["visit_to_detail_rate"]
    ):
        fail("retail TASK-0001 evidence no longer supports its standard answer")
    if not (
        case_02["东区"]["net_sales_2025_to_2026_06"]
        == max(item["net_sales_2025_to_2026_06"] for item in case_02.values())
        and case_02["南区"]["h1_net_sales_growth"]
        == max(item["h1_net_sales_growth"] for item in case_02.values())
        and case_02["南区"]["contribution_margin"]
        == max(item["contribution_margin"] for item in case_02.values())
    ):
        fail("retail TASK-0002 evidence no longer supports its standard answer")
    if not (
        case_03["target_net_sales"] > case_03["baseline_net_sales"]
        and 0.119 <= case_03["balanced_path"]["combined_uplift"] <= 0.121
        and case_03["single_lever_pressure"]["repeat_only_uplift"] > 0.20
    ):
        fail("retail TASK-0003 pressure model no longer supports its standard answer")

    print("OK: 5 retail demo tasks, construction graphs, and standard answers are runnable")


def check_full_demo_workspace() -> None:
    bootstrap = ROOT / "scripts" / "bootstrap-full-demo.sh"

    def digest_tree(root: Path) -> str:
        digest = hashlib.sha256()
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            digest.update(str(path.relative_to(root)).encode("utf-8"))
            digest.update(path.read_bytes())
        return digest.hexdigest()

    with tempfile.TemporaryDirectory(prefix="hs-full-demo-a-") as first_temp, tempfile.TemporaryDirectory(
        prefix="hs-full-demo-b-"
    ) as second_temp:
        targets = [Path(first_temp) / "workspace", Path(second_temp) / "workspace"]
        for target in targets:
            result = subprocess.run(
                ["bash", str(bootstrap), str(target)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                print(result.stdout)
                print(result.stderr)
                fail("full demo workspace bootstrap failed")

        if digest_tree(targets[0]) != digest_tree(targets[1]):
            fail("full demo workspace bootstrap is not deterministic")

    print("OK: full demo workspace bootstraps from empty directories deterministically")


def write_retail_demo_regression_report() -> None:
    report_path = (
        ROOT
        / "examples"
        / "business_graphs"
        / "demo-omnichannel-retail"
        / "datasets"
        / "audit"
        / "full_demo_regression.md"
    )
    report_path.write_text(
        f"""# 完整 Demo 发布回归

> 本报告由 `scripts/validate-package.py` 在全部检查通过后生成。演示业务和数据均为虚构合成。

- validation_date: {date.today().isoformat()}
- release_ready: yes
- Skill frontmatter 与界面元数据: pass
- 产品包文件契约: pass
- 本地 Markdown 链接: pass
- 运行记录与受控反馈闭环: pass
- 私有名称、路径与具体业务词扫描: pass
- 8 份 Source 卡与数据文件绑定: pass
- 固定种子数据独立审计: 40 pass / 0 fail
- 正常 Source 与缺字段坏样本隔离: pass
- 5 个任务卡与 5 个标准答案: pass
- 轻量、标准、重型任务覆盖: pass
- 三组自动证据方向与标准答案一致: pass
- 独立工作区空目录初始化与隔离校验: pass
- 两次独立初始化文件内容一致: pass

任何图谱、生成逻辑、Source 契约、任务卡或标准答案发生变化后，都必须重新运行产品包校验并更新本报告。
""",
        encoding="utf-8",
    )


def main() -> None:
    check_skill_frontmatter()
    check_skill_interface_metadata()
    check_private_terms()
    check_package_contract()
    check_local_markdown_links()
    check_feedback_loop_contract()
    check_demo_contract()
    check_retail_demo_contract()
    check_retail_demo_tasks()
    check_full_demo_workspace()
    write_retail_demo_regression_report()
    print("PASS: hs-data-assistant package validation")


if __name__ == "__main__":
    main()
