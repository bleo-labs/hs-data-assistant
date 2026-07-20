---
type: metric
id: IND-0023
name: 在售SKU数
status: demo
updated_at: 2026-07-18
---

# IND-0023 在售SKU数

## 节点定位

- 用途: 商品丰富度资源指标，用于衡量可被销售的商品范围。
- 计算属性: 状态计数基础量；按唯一 SKU 和当期类目映射去重后可加。

## 定义或计算公式

统计月内至少一天处于可售状态的唯一 SKU 数量。

## 可拆解为

### 结构拆解

- 可按区域、城市、仓库、一级品类和二级类目拆分。

### 公式拆解

- 这是 SKU 状态基础量，是 [有货率](IND-0025-in-stock-rate.md) 的分母。

### 条件性拆解

- 同一 SKU 在多个城市仓出现时，跨仓汇总必须按分析目的决定是否去重。

## 适用范围

衡量商品可售范围，不代表实际有库存。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0011 仓库](../dimensions/DIM-0011-warehouse.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0007 二级类目](../dimensions/DIM-0007-category-l2.md)
- [DIM-0008 SKU](../dimensions/DIM-0008-sku.md)

## 数据源

- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 库存表提供状态；类目归属使用当期有效映射。

## 业务事实

- [FACT-0002 东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)
- [FACT-0005 品类口径调整](../facts/FACT-0005-category-reclassification.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 有货率按 SKU 状态计算，不按库存件数。
- 跨期类目比较须使用当期有效映射。
