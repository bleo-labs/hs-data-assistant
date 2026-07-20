---
type: business_node
id: NODE-0004
name: 履约与售后
status: demo
updated_at: 2026-07-18
---

# NODE-0004 履约与售后

## 节点定义

支付订单进入仓储、出库和配送环节，并通过准时完成、取消和退款反映交付质量。

## 关键问题

- 履约是否准时，异常来自城市、仓库还是品类。
- 退款是否由促销、商品质量、缺货或履约问题推动。
- 系统事件与业务趋势是否被正确区分。

## 绑定资产

- 指标: [退款金额](../metrics/IND-0002-refund-amount.md)、[履约费用](../metrics/IND-0008-fulfillment-expense.md)、[退款率](../metrics/IND-0031-refund-rate.md)、[准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)
- 维度: [区域](../dimensions/DIM-0002-region.md)、[城市](../dimensions/DIM-0003-city.md)、[一级品类](../dimensions/DIM-0006-category-l1.md)、[仓库](../dimensions/DIM-0011-warehouse.md)
- 层级: [区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)
- 事实: [东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)、[全渠道大促](../facts/FACT-0004-omnichannel-sale.md)、[东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)
