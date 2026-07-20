---
type: business_node
id: NODE-0002
name: 商品供给
status: demo
updated_at: 2026-07-18
---

# NODE-0002 商品供给

## 节点定义

企业通过采购、类目、SKU、价格、库存和区域仓组织可销售商品供给。

## 关键问题

- 在售商品是否丰富且真实有货。
- 商品价格与采购成本是否支持合理利润。
- 补货、仓容和供应商事件是否限制可交易机会。

## 绑定资产

- 指标: [在售SKU数](../metrics/IND-0023-active-sku-count.md)、[有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)、[有货率](../metrics/IND-0025-in-stock-rate.md)、[销售件数](../metrics/IND-0027-units-sold.md)、[平均销售单价](../metrics/IND-0030-average-selling-price.md)、[商品成本](../metrics/IND-0004-cogs.md)
- 维度: [一级品类](../dimensions/DIM-0006-category-l1.md)、[二级类目](../dimensions/DIM-0007-category-l2.md)、[SKU](../dimensions/DIM-0008-sku.md)、[仓库](../dimensions/DIM-0011-warehouse.md)
- 层级: [一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)、[区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)
- 事实: [东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)、[小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)、[小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)、[小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)
