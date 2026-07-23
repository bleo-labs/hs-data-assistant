# Feedback Taxonomy

## Common Problem Types

| type | symptom | usual owner |
|---|---|---|
| routing_error | user asked for one thing, entry sent to the wrong path | hs-entry |
| missing_construction_graph | standard/heavy task started without confirmed graph | hs-entry |
| scope_drift | result covered a narrower or different scope than promised | hs-entry / hs-analysis / hs-research |
| metric_miss | relevant metric was not included or read | hs-analysis / hs-graph |
| dimension_miss | dimension or hierarchy was missing or misunderstood | hs-graph |
| source_miss | required data source was missing, stale, or not linked | hs-graph |
| formula_or_grain_error | formula, aggregation grain, or calculation path was wrong | hs-analysis / hs-graph |
| evidence_gap | conclusion stronger than evidence supports | hs-analysis / hs-research |
| sample_gap | external research did not sample enough or used weak sources | hs-research |
| output_readability | report/table/chart was hard to read or not fit for recipient | hs-output |
| overfitting_private_case | reusable skill absorbed a concrete private case | affected skill |
| stale_index_or_link | index, registry, manifest, or cross-link drifted | hs-graph |
| user_input_gap | user did not provide enough information | no_change / hs-entry |

## Root-Cause Layers

先找首次偏离的层级，不要只修最后暴露问题的文件：

| layer | 判断标准 | 默认处理 |
|---|---|---|
| business_truth | 缺失或错误的是某个业务专属指标、维度、层级、事实、Source 或关系 | 回写对应 business graph |
| data_boundary | 来源、粒度、口径、时间、映射或空值语义没有冻结 | hs-data-contract / hs-graph |
| reusable_method | 通用工作流缺步骤、门槛或校验规则 | 对应 Hs Skill 修改候选 |
| output_contract | 分析正确但交付格式让用户误读或无法使用 | hs-output |
| execution_only | 规则已经存在，本轮偶发没有执行 | 记录、重跑，不急着改 Skill |
| user_preference | 只是特定用户或特定任务的偏好 | 用户配置或本次产物，不写通用规则 |

## How To Decide Whether To Change A Skill

Change a Skill only when at least one is true:

- the same class of failure appeared repeatedly
- the rule was explicitly agreed as reusable
- the failure creates high risk in future tasks
- the fix is a low-cost guardrail that does not overfit a concrete case

通用 Skill 修改还必须满足：能够写出一个不含私有业务信息的回归样本，并有明确通过标准。

Do not change a Skill when:

- the original rule already covered the issue
- the user changed the task midstream
- the failure came from missing private data
- the proposed rule only makes sense for one business

## Business Graph Writeback

Use business graph writeback when the issue is about business-specific truth:

- new metric
- new dimension
- new hierarchy
- new data source
- new business fact
- wrong scope
- wrong relation
- stale index

Route through `hs-graph`; do not write graph assets through `hs-feedback` unless the user explicitly asks and risk is low.

## Skill Rule Writeback

Use skill rule writeback when the issue is about reusable behavior:

- a step is missing from workflow
- routing is consistently wrong
- output contract is unclear
- validation is insufficient
- a required checkpoint is missing

Before patching, state why the rule is transferable and not a private-case overfit.

修改后必须按 `regression-workflow.md` 重跑验证；未验证的修改只能标记为 `fixed_unverified`，不能标记为已解决。
