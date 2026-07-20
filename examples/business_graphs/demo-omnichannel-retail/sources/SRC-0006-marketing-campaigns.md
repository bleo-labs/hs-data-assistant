---
id: SRC-0006
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0006 营销投放月表

## 数据源定义

- 文件或表名: `marketing_campaigns_monthly.csv`
- 存放位置: [datasets/raw/marketing_campaigns_monthly.csv](../datasets/raw/marketing_campaigns_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 销售渠道 × 流量来源 × 活动。
- 唯一键: `month`、`city`、`sales_channel`、`traffic_source`、`campaign`。
- 基础字段: `marketing_expense`、`attributable_visit_users`、`attributable_new_paying_customers`、`attributable_net_sales`。

## 支持的指标

- [营销费用](../metrics/IND-0007-marketing-expense.md)
- [访问用户数](../metrics/IND-0012-visit-users.md)
- [新支付客户数](../metrics/IND-0021-new-paying-customers.md)
- [新客获客成本](../metrics/IND-0033-new-customer-acquisition-cost.md)
- [付费投放产出比](../metrics/IND-0034-paid-media-output-ratio.md)

## 支持的维度

- 月份、城市、销售渠道、流量来源、活动；区域需通过 [SRC-0008](SRC-0008-dimension-mappings.md) 映射。

## 口径限制

- 仅包含可归因付费投放，不代表全渠道营销投入和全部新客。
- 投放费用不得超过 [SRC-0005](SRC-0005-financial-results.md) 的总营销费用。
- 不得用全渠道净销售额除以投放费用计算投放产出比。
