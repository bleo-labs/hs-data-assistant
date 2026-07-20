---
type: metric
id: IND-0004
name: 商品成本
status: demo
updated_at: 2026-07-18
---

# IND-0004 商品成本

## 节点定位

- 用途: 利润计算基础，用于反映已售商品对应的采购成本。
- 计算属性: 金额基础量；相同口径下可加。

## 定义或计算公式

统计期内已售商品对应的采购成本，单位为元。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道和一级品类拆分。
- 不同品类成本可在同一销售口径下相加。

### 公式拆解

- 第一版作为财务基础量生成，不用毛利率倒推。

### 条件性拆解

- 只确认与本期净销售额对应的已售商品成本，不包含期末库存价值。

## 适用范围

适用于已售商品；不含营销、履约和渠道费用。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 商品成本以财务结果月表为权威。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)

## 关系备注

- 商品成本与库存采购额不是同一口径。
- 不得用行业平均毛利率反推替代。
