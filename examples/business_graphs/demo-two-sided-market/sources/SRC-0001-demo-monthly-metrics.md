---
id: SRC-0001
type: source
status: demo
---

# SRC-0001-demo-monthly-metrics

## 数据源定义

- 文件或表名: demo_monthly_metrics.csv
- 存放位置: `datasets/raw/demo_monthly_metrics.csv`
- 数据截止时间: 2026-06-30
- 更新频率: 示例静态数据，不更新

## 数据粒度与字段

- 粒度: 月份 × 供给类型
- 关键字段: `month`、`supply_type`、`c_intent_users`、`b_active_supply`、`effective_matches`、`single_match_revenue`、`revenue`
- 限制: 仅用于验证 Hs 工作流和演示计算，不代表任何真实行业。

## 支持的指标

- [IND-0001-收入](../metrics/IND-0001-revenue.md)
- [IND-0002-C端意向用户数](../metrics/IND-0002-c-intent-users.md)
- [IND-0003-B端有效供给数](../metrics/IND-0003-b-active-supply.md)
