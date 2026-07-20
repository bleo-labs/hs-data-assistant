---
type: metric
id: IND-0027
name: 销售件数
status: demo
updated_at: 2026-07-18
---

# IND-0027 销售件数

## 节点定位

- 用途: 商品销售规模基础量，连接数量与平均销售单价。
- 计算属性: 商品件数基础量；相同互斥交易口径下可加。

## 定义或计算公式

支付成功订单中包含的商品总件数。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、品类、客户类型和促销类型拆分。

### 公式拆解

- [GMV](IND-0001-gmv.md) / [平均销售单价](IND-0030-average-selling-price.md)

### 条件性拆解

- 与库存表的销售件数必须在城市、SKU 和月份口径上可校验。

## 适用范围

支付成功商品件数，不扣除后续退款件数。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0007 二级类目](../dimensions/DIM-0007-category-l2.md)
- [DIM-0008 SKU](../dimensions/DIM-0008-sku.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)
- [DIM-0010 促销类型](../dimensions/DIM-0010-promotion-type.md)

## 数据源

- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- 取数规则: 交易类目汇总与库存 SKU 底数必须通过有效映射闭合。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 不得在订单表和库存表分别随机生成后再强行解释差异。
- 数据生成必须从同一销售件数基础量映射到两张 Source。
