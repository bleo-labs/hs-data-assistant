---
type: metric
id: IND-0029
name: 客单价
status: demo
updated_at: 2026-07-18
---

# IND-0029 客单价

## 节点定位

- 用途: 单订单价值效率指标，用于解释 GMV 的订单价值变化。
- 计算属性: 单均派生指标；不可加、不可直接平均。

## 定义或计算公式

[GMV](IND-0001-gmv.md) / [支付订单数](IND-0026-paid-orders.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型观察。

### 公式拆解

- [GMV](IND-0001-gmv.md) / [支付订单数](IND-0026-paid-orders.md)

### 条件性拆解

- 分母为 0 时不可计算。

## 适用范围

每笔支付订单的平均成交金额，退款前口径。

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
- 取数规则: 由 GMV 与支付订单数计算。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)

## 关系备注

- 汇总时先汇总 GMV 和订单数再相除。
- 客单价变化可能来自价格、件单量或品类结构，不能直接等同于提价。
