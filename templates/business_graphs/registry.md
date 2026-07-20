# Business Graph Registry

这里登记所有可被 Hs 系列 Skill 调用的业务指标树。

## 使用规则

- 如果用户的问题没有明确业务，而本目录存在多棵业务树，必须先询问用户使用哪一棵。
- 不同业务树之间不能混用指标口径；同名指标也必须回到各自业务树解释。
- 通用模板可以复用，具体指标、维度、数据源、业务事实必须落到某一棵业务树。
- `hs-onboarding` 负责生成第一版业务认知地图和指标树骨架。
- `hs-graph` 负责维护业务树资产、绑定关系、索引、总览和多业务入口。
- `hs-analysis` 负责在选定业务树后完成分析交付。

## 已登记业务树

| graph_id | 业务名称 | 别名 | 状态 | 入口 |
|---|---|---|---|---|
| `demo_business` | 示例业务 | demo | draft | `business_graphs/demo_business/manifest.md` |
