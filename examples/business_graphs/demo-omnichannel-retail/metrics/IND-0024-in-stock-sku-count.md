---
type: metric
id: IND-0024
name: 有货SKU数
status: demo
updated_at: 2026-07-18
---

# IND-0024 有货SKU数

## 节点定位

- 用途: 可交易供给资源指标，用于衡量在售商品中真实可售的 SKU 数。
- 计算属性: 状态计数基础量；按唯一 SKU 与仓库口径去重后可加。

## 定义或计算公式

统计月内在售且可用库存大于 0 的唯一 SKU 数量。

## 可拆解为

### 结构拆解

- 可按区域、城市、仓库、一级品类和二级类目拆分。

### 公式拆解

- 这是基础量，是 [有货率](IND-0025-in-stock-rate.md) 的分子。

### 条件性拆解

- 必须小于或等于同粒度 [在售SKU数](IND-0023-active-sku-count.md)。

## 适用范围

表示供给可用性，不代表库存件数充足或无断货天数。

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
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 数据生成必须满足有货 SKU 数 <= 在售 SKU 数。
- 城市仓关系需使用当月有效映射。
