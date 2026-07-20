---
type: business_node
id: NODE-0003
name: 匹配与交易
status: demo
updated_at: 2026-07-18
---

# NODE-0003 匹配与交易

## 节点定义

销售渠道把用户需求与可售商品连接起来，完成详情浏览、加购、下单和支付。

## 关键问题

- 转化下降发生在漏斗哪一层。
- 商品、渠道、客户类型与促销结构如何共同影响交易。
- 订单增长是否能被客户数、频次、客单价和件单价闭合解释。

## 绑定资产

- 指标: [加购用户数](../metrics/IND-0014-add-to-cart-users.md)、[提交订单用户数](../metrics/IND-0015-order-submit-users.md)、[支付客户数](../metrics/IND-0016-paying-customers.md)、[详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)、[加购提交转化率](../metrics/IND-0019-cart-to-submit-rate.md)、[提交支付转化率](../metrics/IND-0020-submit-to-pay-rate.md)、[支付订单数](../metrics/IND-0026-paid-orders.md)、[购买频次](../metrics/IND-0028-purchase-frequency.md)、[客单价](../metrics/IND-0029-aov.md)
- 维度: [销售渠道](../dimensions/DIM-0004-sales-channel.md)、[一级品类](../dimensions/DIM-0006-category-l1.md)、[二级类目](../dimensions/DIM-0007-category-l2.md)、[客户类型](../dimensions/DIM-0009-customer-type.md)、[促销类型](../dimensions/DIM-0010-promotion-type.md)
- 层级: [一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)、[渠道-流量来源](../hierarchies/HIER-0003-channel-traffic-source.md)
- 事实: [小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)、[全渠道大促](../facts/FACT-0004-omnichannel-sale.md)、[小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
