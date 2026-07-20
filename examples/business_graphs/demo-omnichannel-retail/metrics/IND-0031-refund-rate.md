---
type: metric
id: IND-0031
name: 退款率
status: demo
updated_at: 2026-07-18
---

# IND-0031 退款率

## 节点定位

- 用途: 成交质量校准指标，用于判断 GMV 能否转化为净销售额。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[退款金额](IND-0002-refund-amount.md) / [GMV](IND-0001-gmv.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型观察。

### 公式拆解

- [退款金额](IND-0002-refund-amount.md) / [GMV](IND-0001-gmv.md)

### 条件性拆解

- 分母为 0 时不可计算。
- 第一版按退款确认月与当月 GMV 形成经营观察口径，不用于订单级严格 cohort。

## 适用范围

用于经营质量趋势，不等同于按原支付订单追踪的最终退款率。

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
- 取数规则: 退款金额与 GMV 先聚合再计算，交易与财务必须闭合。

## 业务事实

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0006 东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)

## 关系备注

- 汇总时先汇总退款金额和 GMV 再相除。
- 缺少退款金额时必须阻断利润链。
