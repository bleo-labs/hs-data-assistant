# 完整 Demo 演练

这份演练用于验证 Hs 在一套完全虚构的全渠道自营电商业务上，能否从业务图谱一路走到可校验结论。所有业务、数据和事实均为合成内容，不代表任何真实企业。

## 1. 进入演示真源

业务入口位于：

```text
examples/business_graphs/demo-omnichannel-retail/manifest.md
```

开始任务前依次读取：

1. `manifest.md`，确认业务边界和启动规则。
2. `indexes/METRIC_INDEX.md`，审查全量指标是否纳入或排除。
3. 命中指标的原始文件，以及相连的维度、层级、事实和 Source 卡。
4. Source 卡指向的 `datasets/raw/` 数据文件。

不能从任务描述直接跳到数据计算，也不能把设计稿当作数据源。

## 2. 选择演示任务

五个任务覆盖不同工作模式：

| 任务 | 主要能力 | 强度 |
|---|---|---|
| [5 月净销售额下滑](../examples/business_graphs/demo-omnichannel-retail/tasks/TASK-0001-may-decline.md) | 指标异动诊断 | 标准 |
| [区域综合表现](../examples/business_graphs/demo-omnichannel-retail/tasks/TASK-0002-region-performance.md) | 多指标综合判断 | 标准 |
| [下一季度目标压力](../examples/business_graphs/demo-omnichannel-retail/tasks/TASK-0003-target-pressure.md) | 关系型测算 | 重型 |
| [新增品类](../examples/business_graphs/demo-omnichannel-retail/tasks/TASK-0004-new-category.md) | 图谱增改与绑定 | 标准 |
| [Source 契约错误](../examples/business_graphs/demo-omnichannel-retail/tasks/TASK-0005-source-error.md) | 阻断、审计与反馈 | 标准 |

先把任务卡中的用户命题交给 `hs-entry`。Hs 应在读完图谱后给出施工图和范围门，并等待确认，再进入后续 Skill。

## 3. 对照证据与答案

- 自动计算证据：[task_evidence.md](../examples/business_graphs/demo-omnichannel-retail/tasks/evidence/task_evidence.md)
- 标准答案目录：[expected_answers/](../examples/business_graphs/demo-omnichannel-retail/tasks/expected_answers/)

标准答案不是要求措辞完全一致，而是检查：

- 是否覆盖任务要求的指标链和分析范围。
- 结论是否由 Source 数据和中间计算支持。
- 是否区分主因、次因、事实、推断和不可下结论项。
- 发生数据契约错误时，是否停止计算而不是静默补零。

## 4. 重建数据与回归

在演示业务目录中依次运行：

```bash
python3 generator/generate_demo_data.py
python3 generator/validate_demo_data.py
python3 generator/build_demo_task_evidence.py
```

然后在产品包根目录运行：

```bash
python3 scripts/validate-package.py
```

只有数据审计、任务证据、Source 绑定、本地链接、Skill 契约和隐私扫描全部通过，演示资产才可发布。

## 5. 独立演示工作区

当前目录是 GitHub 公开真源。日常录屏、截图、试验输出和临时图谱修改应在独立演示工作区进行。

在产品包根目录运行：

```bash
./scripts/bootstrap-full-demo.sh ~/HS_Public_Demo_Workspace
```

脚本会复制 Hs Skills 快照、完整图谱、合成数据、任务与答案，并执行隔离校验。目标目录必须为空。

需要恢复干净环境时，先检查并导出演示产物，再显式确认重置：

```bash
./scripts/reset-full-demo.sh ~/HS_Public_Demo_Workspace --yes
```

重置脚本会先把 `outputs/`、`exports/` 和 `recordings/` 备份到同级时间戳目录，再重新初始化。工作区中的改动不会自动覆盖 GitHub 真源。
