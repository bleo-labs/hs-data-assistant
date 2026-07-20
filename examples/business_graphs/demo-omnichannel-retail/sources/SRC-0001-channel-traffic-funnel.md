---
id: SRC-0001
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0001 渠道流量漏斗月表

## 数据源定义

- 文件或表名: `channel_traffic_funnel_monthly.csv`
- 存放位置: [datasets/raw/channel_traffic_funnel_monthly.csv](../datasets/raw/channel_traffic_funnel_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 销售渠道 × 流量来源 × 客户类型。
- 唯一键: `month`、`city`、`sales_channel`、`traffic_source`、`customer_type`。
- 基础字段: `visit_users`、`product_detail_users`、`paying_customers`。
- 生成规则: 每位月度用户只归入一个主渠道和主流量来源，基础量可向上加总。

## 支持的指标

- [访问用户数](../metrics/IND-0012-visit-users.md)
- [商品详情用户数](../metrics/IND-0013-product-detail-users.md)
- [支付客户数](../metrics/IND-0016-paying-customers.md)
- [访问详情转化率](../metrics/IND-0017-visit-to-detail-rate.md)
- [新支付客户数](../metrics/IND-0021-new-paying-customers.md)
- [老支付客户数](../metrics/IND-0022-returning-paying-customers.md)
- [老客占比](../metrics/IND-0035-returning-customer-share.md)

## 支持的维度

- 月份、城市、销售渠道、流量来源、客户类型；区域需通过 [SRC-0008](SRC-0008-dimension-mappings.md) 映射。

## 口径限制

- 不按品类拆分，品类漏斗使用 [SRC-0002](SRC-0002-product-behavior-funnel.md)。
- 不适用的渠道与流量来源组合不生成记录。
- 跨渠道用户未做真实身份去重，只能按本 Demo 的“主渠道”合成口径加总。
