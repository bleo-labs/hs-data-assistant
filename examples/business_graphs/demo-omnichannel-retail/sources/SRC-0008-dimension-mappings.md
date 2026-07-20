---
id: SRC-0008
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0008 维度映射表

## 数据源定义

- 文件或表名: `dimension_mappings.csv`
- 存放位置: [datasets/raw/dimension_mappings.csv](../datasets/raw/dimension_mappings.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 单条时间有效映射关系。
- 唯一键: `mapping_type`、`parent_value`、`child_value`、`effective_start`、`effective_end`。
- 字段: `mapping_type`、`parent_value`、`child_value`、`effective_start`、`effective_end`。
- 映射范围: 区域-城市、城市-仓库、一级品类-二级类目、二级类目-SKU、渠道-流量来源。

## 支持的层级关系

- [区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)
- [一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)
- [渠道-流量来源适用关系](../hierarchies/HIER-0003-channel-traffic-source.md)

## 支持的维度

- 区域、城市、仓库、一级品类、二级类目、SKU、销售渠道、流量来源。

## 口径限制

- 跨期比较必须使用当月有效映射。
- `AP-LIFE-08` 在 2026-01 发生二级类目归属变化，不能用当前映射覆盖历史。
- 映射缺失或同一时点命中多条有效记录时，相关分析必须阻断。
