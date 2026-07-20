---
type: metric
id: IND-0005
name: 毛利润
status: demo
updated_at: 2026-07-18
---

# IND-0005 毛利润

## 节点定位

- 用途: 商品经营质量结果，用于判断净销售额扣除商品成本后的盈利空间。
- 计算属性: 金额派生结果；由基础金额计算。

## 定义或计算公式

[净销售额](IND-0003-net-sales.md) - [商品成本](IND-0004-cogs.md)。

## 可拆解为

### 结构拆解

- 可按区域、渠道和一级品类拆分。

### 公式拆解

- [净销售额](IND-0003-net-sales.md) - [商品成本](IND-0004-cogs.md)

### 条件性拆解

- 只有收入与成本确认口径一致时成立。

## 适用范围

不扣除营销、履约与渠道费用，因此不是最终经营利润。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 由净销售额与商品成本逐分回算。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 不得独立生成毛利润。
- 区域或品类毛利润可加，但 [毛利率](IND-0006-gross-margin.md) 必须重算。
