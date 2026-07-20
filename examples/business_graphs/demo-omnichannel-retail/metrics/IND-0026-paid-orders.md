---
type: metric
id: IND-0026
name: 支付订单数
status: demo
updated_at: 2026-07-18
---

# IND-0026 支付订单数

## 节点定位

- 用途: 交易规模基础量，连接客户规模、购买频次与 GMV。
- 计算属性: 订单数量基础量；相同互斥交易口径下可加。

## 定义或计算公式

统计期内完成支付的订单数量。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型拆分。

### 公式拆解

- [支付客户数](IND-0016-paying-customers.md) × [购买频次](IND-0028-purchase-frequency.md)
- [GMV](IND-0001-gmv.md) / [客单价](IND-0029-aov.md)

### 条件性拆解

- 公式要求分子分母处于同一粒度。

## 适用范围

只包含支付成功订单；取消未支付订单不进入。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0007 二级类目](../dimensions/DIM-0007-category-l2.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)
- [DIM-0010 促销类型](../dimensions/DIM-0010-promotion-type.md)

## 数据源

- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- 取数规则: 交易表为权威；履约表的完成与取消订单用于闭合校验。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 支付订单数是基础量，购买频次和客单价由它计算。
- 不得独立随机生成订单数、频次与客单价。
