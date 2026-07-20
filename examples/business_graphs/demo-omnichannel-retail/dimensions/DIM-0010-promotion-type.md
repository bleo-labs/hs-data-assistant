---
type: dimension
id: DIM-0010
name: 促销类型
status: demo
updated_at: 2026-07-18
---

# DIM-0010 促销类型

## 维度定义

订单主要使用的促销机制。

## 可取值或取值来源

- 无促销
- 优惠券
- 平台大促
- 会员优惠

## 适用指标

适用于 [GMV](../metrics/IND-0001-gmv.md)、[退款金额](../metrics/IND-0002-refund-amount.md)、[支付订单数](../metrics/IND-0026-paid-orders.md)、[销售件数](../metrics/IND-0027-units-sold.md)、[客单价](../metrics/IND-0029-aov.md) 和 [退款率](../metrics/IND-0031-refund-rate.md)。

## 数据源字段

- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 字段名为 `promotion_type`。

## 相关 hierarchy

- 不需要单独 hierarchy。

## 注意事项

- 每笔合成订单只归入一个主促销类型，避免重复计算。
- 促销与结果的同步变化不自动构成因果结论。
