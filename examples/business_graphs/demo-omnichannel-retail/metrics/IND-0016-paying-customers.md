---
type: metric
id: IND-0016
name: 支付客户数
status: demo
updated_at: 2026-07-18
---

# IND-0016 支付客户数

## 节点定位

- 用途: 成交客户规模，是客户、订单与销售结果之间的关键连接指标。
- 计算属性: 去重客户基础量；只在明确去重与主归属口径内可加。

## 定义或计算公式

统计月内至少完成一笔支付的去重客户数。

## 可拆解为

### 结构拆解

- [新支付客户数](IND-0021-new-paying-customers.md) + [老支付客户数](IND-0022-returning-paying-customers.md)
- 可按区域、城市、渠道、主品类和客户类型拆分。

### 公式拆解

- [支付订单数](IND-0026-paid-orders.md) / [购买频次](IND-0028-purchase-frequency.md)
- 公式用于校验，不作为基础量生成方法。

### 条件性拆解

- 跨渠道、品类和促销的客户数在真实业务不可直接相加；本 Demo 仅在主归属契约下闭合。

## 适用范围

适用于支付成功客户，不包括仅提交订单的用户。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0007 二级类目](../dimensions/DIM-0007-category-l2.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)
- [DIM-0010 促销类型](../dimensions/DIM-0010-promotion-type.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 渠道总量、主品类切片和交易归因必须逐层闭合。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 支付客户数必须等于新客与老客之和。
- 不得把按品类或促销重复出现的客户数直接汇总为全局客户数。
