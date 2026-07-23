# 架构

Hs Data Assistant 有三层长期资产。

## Skill 协作总览

```mermaid
flowchart LR
  ENTRY["hs-entry\n任务识别与施工图"]
  ONBOARD["hs-onboarding\n第一版业务框架"]
  GRAPH["hs-graph\n长期业务资产"]
  CONTRACT["hs-data-contract\n数据边界"]
  ANALYSIS["hs-analysis\n内部推理与测算"]
  RESEARCH["hs-research\n外部证据与对标"]
  AUDIT["hs-metric-audit\n独立校验"]
  TABLE["hs-table-builder\n三层表格"]
  OUTPUT["hs-output\n可交付表达"]
  RECORD["project_graph + run_record\n计划与实际执行证据"]
  FEEDBACK["hs-feedback\n问题归因与回写"]

  ENTRY --> RECORD
  RECORD --> ONBOARD
  RECORD --> GRAPH
  ONBOARD --> GRAPH
  GRAPH --> CONTRACT
  GRAPH --> ANALYSIS
  GRAPH --> RESEARCH
  CONTRACT --> ANALYSIS
  ANALYSIS --> AUDIT --> TABLE --> OUTPUT
  RESEARCH --> OUTPUT
  OUTPUT --> FEEDBACK
  RECORD -.关键事件.-> FEEDBACK
  FEEDBACK --> ENTRY
  FEEDBACK --> GRAPH
  FEEDBACK --> ANALYSIS
  FEEDBACK --> OUTPUT
```

这不是一条每次都必须走完的流水线：

- 没有业务图谱时，先走 `hs-onboarding -> hs-graph`。
- 外部研究命题以 `hs-research` 为主，不强行经过数据契约和建表。
- 标准或重型内部数据任务必须经过 `hs-data-contract -> hs-analysis -> hs-metric-audit -> hs-table-builder`。
- 任何任务出现漏读、口径冲突、结论不可用或用户纠正时，都通过 `hs-feedback` 回写到真正需要修正的模块。
- 标准或重型任务使用同一组 `node_id` 对齐 `project_graph` 与 `run_record`：前者是施工计划，后者只记录关键执行事件。

## 1. 技能层：工作方法

Skills 定义 Agent 应该如何工作。

```text
hs-entry -> hs-onboarding / hs-graph / hs-research
          \-> Graph Scan -> 用户确认施工图
              \-> hs-data-contract -> hs-analysis -> hs-metric-audit
                  -> hs-table-builder -> hs-output
                                   \-> hs-feedback
```

这些技能是可复用方法，不能写入具体私有业务规则。

对需要内部数据读取、计算或表格交付的标准/重型任务，施工图必须先读取真实业务图谱、指标索引和 Source 卡，再进入数据契约。数据契约只能使用 Graph Scan 已确认的路径；审计未放行的中间结果不得进入最终表或报告。

## 2. 业务图谱层：业务专属资产

业务图谱用于存放某个具体业务的专属资产：

```text
business_graphs/
  registry.md
  {business_id}/
    manifest.md
    business_nodes/
    metrics/
    dimensions/
    hierarchies/
    facts/
    sources/
    bindings/
    indexes/
    maps/
```

`registry.md` 是多业务入口，用来选择当前要使用哪棵业务树。每个 `manifest.md` 是单棵业务图谱的总览。

## 3. 交付产出层：任务结果

Outputs 是具体任务产生的交付物，例如报告、表格、图表、施工图、回写卡和交接包。

输出物可能暴露业务图谱哪里不完整，但输出物不能替代业务图谱。需要长期保留的变化，应该通过 `hs-graph` 写回。

## 4. 运行记录：计划与实际对齐

标准和重型任务在用户确认施工图后初始化 `run_record.md`。它不保存完整思维链或每次工具调用，只在以下节点追加事件：任务启动、节点完成、节点阻塞、用户纠正、修改提案、回归验证和任务收口。

这样做的目的不是增加项目管理负担，而是让 Feedback 能回答两个问题：

- 问题第一次在哪个施工节点发生。
- 失败来自业务知识、数据边界、通用方法、输出契约，还是一次偶发未执行。

详细字段见 `skills/hs-entry/references/run-record-contract.md`。

## 5. 反馈回路：受控自我修正

Feedback 记录系统在哪里失败，并判断应该修改哪一个真源：

- 业务图谱资产问题 -> `hs-graph`
- 路由或施工图问题 -> `hs-entry`
- 分析方法问题 -> `hs-analysis`
- 数据源、口径、粒度、映射或空值语义问题 -> `hs-data-contract`
- 父子闭环、可比性、分子分母、Join、排名或异常问题 -> `hs-metric-audit`
- 最终表复杂计算、输入结果混淆或公式隐藏错误 -> `hs-table-builder`
- 研究方法问题 -> `hs-research`
- 输出可读性问题 -> `hs-output`
- 第一版业务地图逻辑问题 -> `hs-onboarding`

Feedback 应该先停止当前任务，读取运行证据并定位首次偏离，再决定是否修改系统，避免把一次偶发失败偷偷固化成永久规则。

标准闭环：

```text
真实任务 -> 运行记录 -> 用户纠正或校验失败 -> 根因分类
        -> 修改提案 -> 用户确认 -> 目标能力回写
        -> 从最早受影响节点重跑 -> 回归验证
```

Hs 不允许自由改写自己：

- 私有业务缺口回写 business graph，不进入通用 Skill。
- 规则已经存在但本轮没有执行，先记录和重跑，不急着加规则。
- 通用 Skill 修改必须经用户确认，并绑定至少一个可复现回归样本。
- 未通过回归验证，不宣称问题已经解决。

## 核心规则

`hs-onboarding` 和 `hs-graph` 使用同一套业务图谱文件契约。Onboarding 负责创建第一版，Graph 负责长期维护。
