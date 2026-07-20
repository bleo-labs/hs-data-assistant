---
id: SRC-0007
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0007 履约月表

## 数据源定义

- 文件或表名: `fulfillment_monthly.csv`
- 存放位置: [datasets/raw/fulfillment_monthly.csv](../datasets/raw/fulfillment_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 仓库 × 一级品类。
- 唯一键: `month`、`city`、`warehouse`、`category_l1`。
- 基础字段: `completed_orders`、`on_time_completed_orders`、`canceled_orders`、`average_fulfillment_hours`。
- 闭合关系: 支付订单 = 已完成订单 + 取消订单；准时完成订单 ≤ 已完成订单。

## 支持的指标

- [准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)

## 支持的维度

- 月份、城市、仓库、一级品类；区域需通过 [SRC-0008](SRC-0008-dimension-mappings.md) 映射。

## 口径限制

- 取消订单不进入准时履约率分母。
- 支付订单必须与 [SRC-0003](SRC-0003-order-transactions.md) 聚合闭合。
- 履约费用不在本表，财务费用使用 [SRC-0005](SRC-0005-financial-results.md)。
