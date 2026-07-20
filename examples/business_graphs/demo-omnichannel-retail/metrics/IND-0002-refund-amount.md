---
type: metric
id: IND-0002
name: 退款金额
status: demo
updated_at: 2026-07-18
---

# IND-0002 退款金额

## 节点定位

- 用途: 成交质量与真实收入校准，用于把 GMV 还原为净销售额。
- 计算属性: 金额基础量；相同口径下可加。

## 定义或计算公式

统计期内确认退款的商品金额，单位为元。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型拆分。
- 只有互斥完整口径可以汇总回总退款金额。

### 公式拆解

- 这是退款事实基础量，不用退款率反推生成。
- [退款率](IND-0031-refund-rate.md) = 退款金额 / [GMV](IND-0001-gmv.md)。

### 条件性拆解

- 退款确认月与原支付月可能不同；第一版按退款确认月统计。

## 适用范围

适用于已确认退款的支付交易；未完成售后申请不进入。

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
- 取数规则: 交易表为明细权威；财务表必须逐分闭合。

## 业务事实

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0006 东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)

## 关系备注

- 缺失退款金额时，[净销售额](IND-0003-net-sales.md)、[退款率](IND-0031-refund-rate.md) 和利润链全部阻断。
- 不得把空值或缺失字段当作 0。
