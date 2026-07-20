---
type: metric
id: IND-0025
name: 有货率
status: demo
updated_at: 2026-07-18
---

# IND-0025 有货率

## 节点定位

- 用途: 供给可用性效率指标，用于识别库存对交易机会的约束。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[有货SKU数](IND-0024-in-stock-sku-count.md) / [在售SKU数](IND-0023-active-sku-count.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、仓库、一级品类和二级类目观察。

### 公式拆解

- [有货SKU数](IND-0024-in-stock-sku-count.md) / [在售SKU数](IND-0023-active-sku-count.md)

### 条件性拆解

- 分母为 0 时不可计算。
- 需要按唯一 SKU 状态去重。

## 适用范围

反映 SKU 可用比例，不反映每个 SKU 的库存深度。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0011 仓库](../dimensions/DIM-0011-warehouse.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0007 二级类目](../dimensions/DIM-0007-category-l2.md)

## 数据源

- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 聚合有货 SKU 与在售 SKU 后重算，类目归属使用当期映射。

## 业务事实

- [FACT-0002 东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 汇总时先按目标层级去重计数分子分母，再相除。
- 不得平均城市或品类有货率。
