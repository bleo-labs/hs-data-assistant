---
type: dimension
id: DIM-0005
name: 流量来源
status: demo
updated_at: 2026-07-18
---

# DIM-0005 流量来源

## 维度定义

用户进入销售渠道前的主要获客来源。

## 可取值或取值来源

- 自然流量
- 付费投放
- 私域触达
- 内容合作

## 适用指标

- [访问用户数](../metrics/IND-0012-visit-users.md)
- [商品详情用户数](../metrics/IND-0013-product-detail-users.md)
- [支付客户数](../metrics/IND-0016-paying-customers.md)
- [访问详情转化率](../metrics/IND-0017-visit-to-detail-rate.md)
- [新支付客户数](../metrics/IND-0021-new-paying-customers.md)
- [新客获客成本](../metrics/IND-0033-new-customer-acquisition-cost.md)
- [付费投放产出比](../metrics/IND-0034-paid-media-output-ratio.md)

## 数据源字段

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 事实表字段为 `traffic_source`，适用组合由映射表冻结。

## 相关 hierarchy

- [HIER-0003 渠道-流量来源](../hierarchies/HIER-0003-channel-traffic-source.md)

## 注意事项

- 只有具有明确费用和归因口径的流量才能进入获客成本与投放产出计算。
- 不适用的渠道来源组合不得生成记录。
