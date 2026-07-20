---
type: manifest
id: demo-omnichannel-retail
name: 全渠道自营电商零售 Demo
status: task_ready
updated_at: 2026-07-18
---

# 全渠道自营电商零售 Demo

## 基本信息

- graph_id: `demo-omnichannel-retail`
- 业务名称: 全渠道自营电商零售
- 别名: retail demo, omnichannel retail
- 状态: task_ready
- 最近更新时间: 2026-07-18
- 业务负责人/维护人: Hs public demo

## 业务定义

- 服务对象: 购买家居生活商品的消费者。
- 付费方: 消费者。
- 交付价值: 通过可用商品、合理价格、顺畅交易与稳定履约满足消费需求。
- 核心交易: 用户访问后完成商品浏览、加购、下单、支付与收货。
- 核心经营目标: 在保持供给、履约和用户体验的前提下，实现贡献利润的可持续增长。

## 适用范围

- 适用业务: 自营库存、自担履约责任的多渠道电商零售。
- 不适用业务: 平台商家入驻、线下门店、会员订阅和纯佣金撮合。
- 主要使用场景: 指标树演示、经营诊断、目标测算、图谱维护、数据契约与错误阻断。
- 安全边界: 全部业务名称、城市、SKU、数据和事实均为虚构合成，不映射任何真实企业。

## 入口文件

- 设计说明: [design/](design/)
- 业务节点: [business_nodes/](business_nodes/)
- 指标: [metrics/](metrics/)
- 维度: [dimensions/](dimensions/)
- 层级关系: [hierarchies/](hierarchies/)
- 数据源: [sources/README.md](sources/README.md)
- 数据契约: [design/data-contract.md](design/data-contract.md)
- 数据生成器: [generator/generate_demo_data.py](generator/generate_demo_data.py)
- 数据审计: [datasets/audit/data_generation_audit.md](datasets/audit/data_generation_audit.md)
- 发布回归: [datasets/audit/full_demo_regression.md](datasets/audit/full_demo_regression.md)
- 业务事实: [facts/](facts/)
- 绑定关系: [bindings/BINDINGS.md](bindings/BINDINGS.md)
- 资产索引: [indexes/ASSET_INDEX.md](indexes/ASSET_INDEX.md)
- 指标索引: [indexes/METRIC_INDEX.md](indexes/METRIC_INDEX.md)
- 业务认知地图: [maps/README.md](maps/README.md)
- 演示任务: [tasks/README.md](tasks/README.md)
- 自动证据: [tasks/evidence/task_evidence.md](tasks/evidence/task_evidence.md)

## 资产规模

- 业务节点: 5
- 指标: 35
- 维度: 11
- 层级关系: 3
- 数据源: 8 个已落地 Source 卡
- 业务事实: 9
- 数据文件: 8 份正常 CSV、1 份隔离坏样本、2 份审计与回归报告
- 演示任务: 5
- 标准答案: 5

## 启动规则

- 用户明确提出使用公开零售 Demo 时，直接选择本图谱。
- 分析前必须读取 [指标索引](indexes/METRIC_INDEX.md)，再回到命中的原始指标、维度、层级、事实和 Source 文件。
- 只能通过 `sources/SRC-*.md` 定位数据；[数据设计稿](design/data-design.md) 和 [数据契约](design/data-contract.md) 用于解释生成机制，不能代替 Source 卡。
- 每次重新生成数据后，必须运行 [独立审计器](generator/validate_demo_data.py)，并确认审计报告中的 `release_ready: yes`。
- 每次调整生成逻辑、图谱或任务后，必须重新运行 [任务证据生成器](generator/build_demo_task_evidence.py)，并确认五份标准答案仍由证据支持。
- 比率、客单价、利润率、获客成本等派生指标必须从基础分子分母重算，不能独立生成、直接相加或平均。
