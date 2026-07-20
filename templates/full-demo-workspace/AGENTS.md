# Hs Public Demo Workspace

本工作区只用于 Hs 公开演示。所有业务、数据、事实和答案均为虚构合成，不代表任何真实企业。

## 任务入口

- Hs Skills 快照：`.agents/skills/`
- 业务图谱入口：`business_graphs/demo-omnichannel-retail/manifest.md`
- 指标索引：`business_graphs/demo-omnichannel-retail/indexes/METRIC_INDEX.md`
- 演示任务：`business_graphs/demo-omnichannel-retail/tasks/README.md`
- Source 卡：`business_graphs/demo-omnichannel-retail/sources/`
- 合成数据：`business_graphs/demo-omnichannel-retail/datasets/raw/`

## 执行规则

1. 用户提出命题后，先使用 `hs-entry` 判断任务强度与交付目标。
2. 施工图生成前，必须读取业务 manifest、指标索引、命中资产与 Source 卡。
3. 施工图必须交给用户确认，确认后才能计算或生成交付物。
4. 标准和重型数据任务必须先由 `hs-data-contract` 冻结口径。
5. 分析结果必须经过 `hs-metric-audit`；表格和报告分别交给 `hs-table-builder` 与 `hs-output`。
6. 发现图谱、数据、流程或输出问题时，交给 `hs-feedback`，不得静默修补。
7. 工作产物写入 `outputs/`；实验过程写入 `demo_projects/`；不得直接覆盖公开真源快照。

## 安全边界

- 不接入真实企业数据、客户信息、内部路径或私有业务图谱。
- 不把缺失值自动补成 0，不用兜底公式掩盖数据契约错误。
- 所有对外输出必须注明“虚构数据，仅用于演示”。
