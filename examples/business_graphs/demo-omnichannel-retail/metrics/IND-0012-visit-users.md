---
type: metric
id: IND-0012
name: 访问用户数
status: demo
updated_at: 2026-07-18
---

# IND-0012 访问用户数

## 节点定位

- 用途: C端需求漏斗基数，用于观察渠道流量规模。
- 计算属性: 去重用户基础量；在约定主渠道和主来源口径内可加，跨其他切片不可直接相加。

## 定义或计算公式

统计月内进入任一销售渠道的去重用户数。

## 可拆解为

### 结构拆解

- 可按区域、城市、销售渠道、流量来源和客户类型拆分。
- 本 Demo 每位月度用户只归入一个主渠道和主流量来源。

### 公式拆解

- 这是基础量，不从转化率反推生成。

### 条件性拆解

- 不按商品品类拆分，因此不能计算品类访问详情转化率。

## 适用范围

适用于渠道入口流量；不代表商品意向或购买客户。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 渠道漏斗为总量权威；投放表只提供可归因访问子集。

## 业务事实

- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 真实业务可能跨渠道重复，本 Demo 的可加规则是合成数据契约。
- 不得与商品详情、加购等用户数相加。
