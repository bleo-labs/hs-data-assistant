---
id: SRC-0005
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0005 财务结果月表

## 数据源定义

- 文件或表名: `financial_results_monthly.csv`
- 存放位置: [datasets/raw/financial_results_monthly.csv](../datasets/raw/financial_results_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 销售渠道 × 一级品类。
- 唯一键: `month`、`city`、`sales_channel`、`category_l1`。
- 基础字段: `gmv`、`refund_amount`、`cogs`、`marketing_expense`、`fulfillment_expense`、`channel_fee`。
- 派生字段: `net_sales`、`gross_profit`、`contribution_profit`，均由基础金额逐分回算。

## 支持的指标

- [GMV](../metrics/IND-0001-gmv.md)、[退款金额](../metrics/IND-0002-refund-amount.md)、[净销售额](../metrics/IND-0003-net-sales.md)
- [商品成本](../metrics/IND-0004-cogs.md)、[毛利润](../metrics/IND-0005-gross-profit.md)、[毛利率](../metrics/IND-0006-gross-margin.md)
- [营销费用](../metrics/IND-0007-marketing-expense.md)、[履约费用](../metrics/IND-0008-fulfillment-expense.md)、[渠道费用](../metrics/IND-0009-channel-fee.md)
- [贡献利润](../metrics/IND-0010-contribution-profit.md)、[贡献利润率](../metrics/IND-0011-contribution-margin.md)、[退款率](../metrics/IND-0031-refund-rate.md)

## 支持的维度

- 月份、城市、销售渠道、一级品类；区域需通过 [SRC-0008](SRC-0008-dimension-mappings.md) 映射。

## 口径限制

- 利润、成本和费用以本表为权威。
- GMV 与退款金额必须和 [SRC-0003](SRC-0003-order-transactions.md) 在共同粒度逐分闭合。
- 比率只能在目标粒度聚合分子分母后重算，不能平均明细比率。
