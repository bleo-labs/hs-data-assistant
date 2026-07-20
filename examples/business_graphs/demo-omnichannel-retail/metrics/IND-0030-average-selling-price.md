---
type: metric
id: IND-0030
name: 平均销售单价
status: demo
updated_at: 2026-07-18
---

# IND-0030 平均销售单价

## 节点定位

- 用途: 商品价格结构效率指标，用于区分 GMV 变化中的件数和单价因素。
- 计算属性: 单均派生指标；不可加、不可直接平均。

## 定义或计算公式

[GMV](IND-0001-gmv.md) / [销售件数](IND-0027-units-sold.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型观察。

### 公式拆解

- [GMV](IND-0001-gmv.md) / [销售件数](IND-0027-units-sold.md)

### 条件性拆解

- 分母为 0 时不可计算。

## 适用范围

每件支付成功商品的平均成交金额，退款前口径。

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
- 取数规则: 由 GMV 与销售件数计算。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)

## 关系备注

- 汇总时从基础分子分母重算。
- 平均销售单价上升可能来自提价或品类结构变化。
