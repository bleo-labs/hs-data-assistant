---
id: SRC-0003
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0003 订单交易月表

## 数据源定义

- 文件或表名: `order_transactions_monthly.csv`
- 存放位置: [datasets/raw/order_transactions_monthly.csv](../datasets/raw/order_transactions_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 销售渠道 × 一级品类 × 二级类目 × 客户类型 × 促销类型。
- 唯一键: `month`、`city`、`sales_channel`、`category_l1`、`category_l2`、`customer_type`、`promotion_type`。
- 基础字段: `paying_customers`、`paid_orders`、`units_sold`、`gmv`、`refund_amount`。
- 生成顺序: 支付客户 → 支付订单 → 销售件数 → SKU 成交金额 → GMV。

## 支持的指标

- [GMV](../metrics/IND-0001-gmv.md)
- [退款金额](../metrics/IND-0002-refund-amount.md)
- [支付客户数](../metrics/IND-0016-paying-customers.md)
- [新支付客户数](../metrics/IND-0021-new-paying-customers.md)
- [老支付客户数](../metrics/IND-0022-returning-paying-customers.md)
- [支付订单数](../metrics/IND-0026-paid-orders.md)
- [销售件数](../metrics/IND-0027-units-sold.md)
- [购买频次](../metrics/IND-0028-purchase-frequency.md)
- [客单价](../metrics/IND-0029-aov.md)
- [平均销售单价](../metrics/IND-0030-average-selling-price.md)
- [退款率](../metrics/IND-0031-refund-rate.md)

## 支持的维度

- 月份、城市、销售渠道、一级品类、二级类目、客户类型、促销类型。

## 口径限制

- 支付客户按一个主品类和一个主促销归因，可在本 Demo 内闭合；真实业务未必具备该可加性。
- 财务口径的净销售额、成本和费用以 [SRC-0005](SRC-0005-financial-results.md) 为准。
- 缺失 `refund_amount` 时，净销售额、退款率和利润计算必须阻断；隔离坏样本不属于本 Source。
