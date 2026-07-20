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

## How To Decide Whether To Change A Skill

Change a Skill only when at least one is true:

- the same class of failure appeared repeatedly
- the rule was explicitly agreed as reusable
- the failure creates high risk in future tasks
- the fix is a low-cost guardrail that does not overfit a concrete case

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
