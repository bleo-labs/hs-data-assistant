---
type: dimension
id: DIM-0009
name: 客户类型
status: demo
updated_at: 2026-07-18
---

# DIM-0009 客户类型

## 维度定义

按客户在统计月前是否有成功支付记录区分新老客户。

## 可取值或取值来源

- 新客户: 首次支付发生在统计月。
- 老客户: 统计月前已有支付，本月再次支付。

## 适用指标

适用于用户漏斗、订单、客户结构与交易结果，重点包括 [支付客户数](../metrics/IND-0016-paying-customers.md)、[新支付客户数](../metrics/IND-0021-new-paying-customers.md)、[老支付客户数](../metrics/IND-0022-returning-paying-customers.md)、[购买频次](../metrics/IND-0028-purchase-frequency.md) 和 [老客占比](../metrics/IND-0035-returning-customer-share.md)。

## 数据源字段

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 字段名为 `customer_type`。

## 相关 hierarchy

- 不需要单独 hierarchy。

## 注意事项

- 新老客户定义依赖 30 个月观察窗口；窗口前已有历史支付但不可见的客户会形成左截断限制。
- 支付客户数按渠道或品类拆分后不可直接跨维度相加去重。
