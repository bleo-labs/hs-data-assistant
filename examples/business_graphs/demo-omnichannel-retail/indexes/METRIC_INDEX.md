# Metric Index

> 每次分析先用本表完成指标审计，再打开所有命中指标的原始文件。Source 状态为 pending 时不得开始取数。

| id | name | status | 一句话用途 | source_status | path |
|---|---|---|---|---|---|
| `IND-0001` | GMV | demo | 退款前经营规模 | data_ready | [IND-0001-gmv.md](../metrics/IND-0001-gmv.md) |
| `IND-0002` | 退款金额 | demo | 还原真实销售的退款基础量 | data_ready | [IND-0002-refund-amount.md](../metrics/IND-0002-refund-amount.md) |
| `IND-0003` | 净销售额 | demo | 扣除退款后的核心销售结果 | data_ready | [IND-0003-net-sales.md](../metrics/IND-0003-net-sales.md) |
| `IND-0004` | 商品成本 | demo | 已售商品采购成本 | data_ready | [IND-0004-cogs.md](../metrics/IND-0004-cogs.md) |
| `IND-0005` | 毛利润 | demo | 净销售额扣除商品成本 | data_ready | [IND-0005-gross-profit.md](../metrics/IND-0005-gross-profit.md) |
| `IND-0006` | 毛利率 | demo | 商品盈利质量 | data_ready | [IND-0006-gross-margin.md](../metrics/IND-0006-gross-margin.md) |
| `IND-0007` | 营销费用 | demo | 获客与营销支出 | data_ready | [IND-0007-marketing-expense.md](../metrics/IND-0007-marketing-expense.md) |
| `IND-0008` | 履约费用 | demo | 仓储打包配送费用 | data_ready | [IND-0008-fulfillment-expense.md](../metrics/IND-0008-fulfillment-expense.md) |
| `IND-0009` | 渠道费用 | demo | 渠道佣金与技术服务费 | data_ready | [IND-0009-channel-fee.md](../metrics/IND-0009-channel-fee.md) |
| `IND-0010` | 贡献利润 | demo | 第一版最终经营目标 | data_ready | [IND-0010-contribution-profit.md](../metrics/IND-0010-contribution-profit.md) |
| `IND-0011` | 贡献利润率 | demo | 跨规模经营质量 | data_ready | [IND-0011-contribution-margin.md](../metrics/IND-0011-contribution-margin.md) |
| `IND-0012` | 访问用户数 | demo | 渠道流量漏斗基数 | data_ready | [IND-0012-visit-users.md](../metrics/IND-0012-visit-users.md) |
| `IND-0013` | 商品详情用户数 | demo | 具体商品兴趣用户 | data_ready | [IND-0013-product-detail-users.md](../metrics/IND-0013-product-detail-users.md) |
| `IND-0014` | 加购用户数 | demo | 商品兴趣过程量 | data_ready | [IND-0014-add-to-cart-users.md](../metrics/IND-0014-add-to-cart-users.md) |
| `IND-0015` | 提交订单用户数 | demo | 下单意向过程量 | data_ready | [IND-0015-order-submit-users.md](../metrics/IND-0015-order-submit-users.md) |
| `IND-0016` | 支付客户数 | demo | 成交客户规模 | data_ready | [IND-0016-paying-customers.md](../metrics/IND-0016-paying-customers.md) |
| `IND-0017` | 访问详情转化率 | demo | 流量到商品兴趣效率 | data_ready | [IND-0017-visit-to-detail-rate.md](../metrics/IND-0017-visit-to-detail-rate.md) |
| `IND-0018` | 详情加购转化率 | demo | 商品吸引力与供给效率 | data_ready | [IND-0018-detail-to-cart-rate.md](../metrics/IND-0018-detail-to-cart-rate.md) |
| `IND-0019` | 加购提交转化率 | demo | 购物车到下单效率 | data_ready | [IND-0019-cart-to-submit-rate.md](../metrics/IND-0019-cart-to-submit-rate.md) |
| `IND-0020` | 提交支付转化率 | demo | 下单到支付效率 | data_ready | [IND-0020-submit-to-pay-rate.md](../metrics/IND-0020-submit-to-pay-rate.md) |
| `IND-0021` | 新支付客户数 | demo | 首次成交客户规模 | data_ready | [IND-0021-new-paying-customers.md](../metrics/IND-0021-new-paying-customers.md) |
| `IND-0022` | 老支付客户数 | demo | 复购客户规模 | data_ready | [IND-0022-returning-paying-customers.md](../metrics/IND-0022-returning-paying-customers.md) |
| `IND-0023` | 在售SKU数 | demo | 商品丰富度 | data_ready | [IND-0023-active-sku-count.md](../metrics/IND-0023-active-sku-count.md) |
| `IND-0024` | 有货SKU数 | demo | 可交易供给 | data_ready | [IND-0024-in-stock-sku-count.md](../metrics/IND-0024-in-stock-sku-count.md) |
| `IND-0025` | 有货率 | demo | 供给可用性 | data_ready | [IND-0025-in-stock-rate.md](../metrics/IND-0025-in-stock-rate.md) |
| `IND-0026` | 支付订单数 | demo | 支付成功订单规模 | data_ready | [IND-0026-paid-orders.md](../metrics/IND-0026-paid-orders.md) |
| `IND-0027` | 销售件数 | demo | 支付商品件数 | data_ready | [IND-0027-units-sold.md](../metrics/IND-0027-units-sold.md) |
| `IND-0028` | 购买频次 | demo | 单客订单深度 | data_ready | [IND-0028-purchase-frequency.md](../metrics/IND-0028-purchase-frequency.md) |
| `IND-0029` | 客单价 | demo | 单订单成交价值 | data_ready | [IND-0029-aov.md](../metrics/IND-0029-aov.md) |
| `IND-0030` | 平均销售单价 | demo | 单件商品成交价格 | data_ready | [IND-0030-average-selling-price.md](../metrics/IND-0030-average-selling-price.md) |
| `IND-0031` | 退款率 | demo | 成交质量 | data_ready | [IND-0031-refund-rate.md](../metrics/IND-0031-refund-rate.md) |
| `IND-0032` | 准时履约率 | demo | 履约质量 | data_ready | [IND-0032-on-time-fulfillment-rate.md](../metrics/IND-0032-on-time-fulfillment-rate.md) |
| `IND-0033` | 新客获客成本 | demo | 可归因付费获客效率 | data_ready | [IND-0033-new-customer-acquisition-cost.md](../metrics/IND-0033-new-customer-acquisition-cost.md) |
| `IND-0034` | 付费投放产出比 | demo | 可归因净销售额与费用之比 | data_ready | [IND-0034-paid-media-output-ratio.md](../metrics/IND-0034-paid-media-output-ratio.md) |
| `IND-0035` | 老客占比 | demo | 支付客户结构 | data_ready | [IND-0035-returning-customer-share.md](../metrics/IND-0035-returning-customer-share.md) |
