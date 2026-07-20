---
type: metric
id: IND-0001
name: GMV
status: demo
updated_at: 2026-07-18
---

# IND-0001 GMV

## 节点定位

- 用途: 经营规模结果，用于观察支付成功但退款前的商品成交金额。
- 计算属性: 金额结果；由支付订单、销售件数和当期商品成交价逐级形成，相同口径下可加。

## 定义或计算公式

支付成功订单的商品成交金额，退款前口径，单位为元。

## 可拆解为

### 结构拆解

- 按互斥完整口径可拆为区域、渠道、一级品类、二级类目、客户类型或促销类型的组成。
- 每一种拆法独立成立，不得把不同维度的拆解项混加。

### 公式拆解

- [支付订单数](IND-0026-paid-orders.md) × [客单价](IND-0029-aov.md)
- [销售件数](IND-0027-units-sold.md) × [平均销售单价](IND-0030-average-selling-price.md)

### 条件性拆解

- 两条公式必须在同一粒度和口径下分别闭合。
- 退款不在 GMV 中扣除，应通过 [净销售额](IND-0003-net-sales.md) 观察。

## 适用范围

适用于全部支付成功交易；不等于收入、净销售额或利润。

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
- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 交易表为明细权威；财务表用于聚合一致性校验。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 不得独立随机生成 GMV、订单数、客单价和销售件数后再强行对齐。
- 数据生成时先生成支付订单数、每单件数、SKU 成交价和销售件数，再汇总商品成交金额形成 GMV；客单价与平均销售单价随后由分子分母计算。
