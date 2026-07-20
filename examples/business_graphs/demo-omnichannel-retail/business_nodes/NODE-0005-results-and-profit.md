---
type: business_node
id: NODE-0005
name: 经营结果与利润
status: demo
updated_at: 2026-07-18
---

# NODE-0005 经营结果与利润

## 节点定义

将交易规模、退款、商品成本、营销、履约和渠道费用还原为净销售额、毛利润与贡献利润。

## 关键问题

- 规模增长是否转化为净销售额和利润。
- 利润变化来自收入、商品成本还是经营费用。
- 区域、渠道、品类和客户结构变化是否改善经营质量。

## 绑定资产

- 指标: [GMV](../metrics/IND-0001-gmv.md)、[净销售额](../metrics/IND-0003-net-sales.md)、[毛利润](../metrics/IND-0005-gross-profit.md)、[毛利率](../metrics/IND-0006-gross-margin.md)、[营销费用](../metrics/IND-0007-marketing-expense.md)、[渠道费用](../metrics/IND-0009-channel-fee.md)、[贡献利润](../metrics/IND-0010-contribution-profit.md)、[贡献利润率](../metrics/IND-0011-contribution-margin.md)、[老客占比](../metrics/IND-0035-returning-customer-share.md)
- 维度: [月份](../dimensions/DIM-0001-month.md)、[区域](../dimensions/DIM-0002-region.md)、[城市](../dimensions/DIM-0003-city.md)、[销售渠道](../dimensions/DIM-0004-sales-channel.md)、[一级品类](../dimensions/DIM-0006-category-l1.md)、[客户类型](../dimensions/DIM-0009-customer-type.md)、[促销类型](../dimensions/DIM-0010-promotion-type.md)
- 事实: [南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)、[小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)、[全渠道大促](../facts/FACT-0004-omnichannel-sale.md)、[小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)、[小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)
