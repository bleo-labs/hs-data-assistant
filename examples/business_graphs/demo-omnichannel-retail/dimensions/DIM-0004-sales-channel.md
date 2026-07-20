---
type: dimension
id: DIM-0004
name: 销售渠道
status: demo
updated_at: 2026-07-18
---

# DIM-0004 销售渠道

## 维度定义

消费者完成浏览和交易的销售入口。

## 可取值或取值来源

- 自营App
- 自营小程序
- 第三方平台

## 适用指标

- 经营结果: [GMV](../metrics/IND-0001-gmv.md)、[净销售额](../metrics/IND-0003-net-sales.md)、[贡献利润](../metrics/IND-0010-contribution-profit.md)
- 流量转化: [访问用户数](../metrics/IND-0012-visit-users.md) 至 [提交支付转化率](../metrics/IND-0020-submit-to-pay-rate.md)
- 交易与营销: [支付订单数](../metrics/IND-0026-paid-orders.md)、[客单价](../metrics/IND-0029-aov.md)、[新客获客成本](../metrics/IND-0033-new-customer-acquisition-cost.md)、[付费投放产出比](../metrics/IND-0034-paid-media-output-ratio.md)

## 数据源字段

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 字段名为 `sales_channel`。

## 相关 hierarchy

- [HIER-0003 渠道-流量来源](../hierarchies/HIER-0003-channel-traffic-source.md)

## 注意事项

- 第三方平台仍是自营销售渠道，不代表平台商家入驻模式。
- 渠道费用的适用范围不同，详见 [渠道费用](../metrics/IND-0009-channel-fee.md)。
