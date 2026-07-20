---
id: SRC-0002
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0002 商品行为漏斗月表

## 数据源定义

- 文件或表名: `product_behavior_funnel_monthly.csv`
- 存放位置: [datasets/raw/product_behavior_funnel_monthly.csv](../datasets/raw/product_behavior_funnel_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 销售渠道 × 一级品类 × 客户类型。
- 唯一键: `month`、`city`、`sales_channel`、`category_l1`、`customer_type`。
- 基础字段: `product_detail_users`、`add_to_cart_users`、`order_submit_users`、`paying_customers`。
- 闭合关系: 详情用户 ≥ 加购用户 ≥ 提交订单用户 ≥ 支付客户。

## 支持的指标

- [商品详情用户数](../metrics/IND-0013-product-detail-users.md)
- [加购用户数](../metrics/IND-0014-add-to-cart-users.md)
- [提交订单用户数](../metrics/IND-0015-order-submit-users.md)
- [支付客户数](../metrics/IND-0016-paying-customers.md)
- [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)
- [加购提交转化率](../metrics/IND-0019-cart-to-submit-rate.md)
- [提交支付转化率](../metrics/IND-0020-submit-to-pay-rate.md)

## 支持的维度

- 月份、城市、销售渠道、一级品类、客户类型；区域需通过 [SRC-0008](SRC-0008-dimension-mappings.md) 映射。

## 口径限制

- 不包含访问用户，不能计算按品类拆分的访问详情转化率。
- 每位月度用户只归入一个主浏览品类，确保品类基础量可闭合至渠道漏斗。
- 支付客户必须与 [SRC-0001](SRC-0001-channel-traffic-funnel.md) 和 [SRC-0003](SRC-0003-order-transactions.md) 在共同粒度闭合。
