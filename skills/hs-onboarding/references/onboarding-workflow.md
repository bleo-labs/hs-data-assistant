# Hs Onboarding Workflow

## 1. Purpose

Hs Onboarding turns an incomplete business description into a usable first map.

It does not promise a correct final metric tree. It creates a lightweight business cognition map that makes the user want to add assets. The default map is shown in the AI conversation; HTML is an optional export, not the first output.

## 2. Question Set

Use the smallest useful set of questions:

1. Who is the C side? What do they provide, and what do they want?
2. Who is the B side? What do they provide, buy, or consume?
3. Who pays? What exactly do they pay for?
4. How does B meet C? What is the matching or delivery action?
5. What is the root business result currently discussed by the organization?
6. Which part of this whole system can the user actually see or influence?

Ask follow-ups only when a missing answer blocks the first map.

## 3. Business Framework Rules

Treat the initial framework as editable.

Do not label a node as right or wrong. Show it as a hypothesis-backed business node generated from:

- user description
- uploaded reports or tables
- existing metric tree
- system inference

If the user says a node is wrong, revise the framework and keep moving.

## 4. Asset Binding Rules

Each business node can bind four asset types:

- metrics
- dimensions
- data sources
- business facts

Do not infer asset coverage quality. Only count and list assets.

Bad:

- "This node is already covered."
- "This node is partially covered."

Good:

- "This node has 8 metrics, 1 dimension, 2 data sources, and 0 business facts."

The user decides whether that is enough.

## 5. Supplement Prompts

Prompt the user to add assets when:

- a node has no metrics
- a node has metrics but no dimensions
- a node has metrics but no data sources
- a node has no business facts and may be misused
- the user can gain higher-level self-description by filling an upstream or downstream node

Use concrete prompts:

- "你这里有业绩指标，但缺雇主行业维度，要不要补上？"
- "你这里有 C 端意向UV，但还没有简历创建、职位点击、投递相关指标。"
- "这个节点目前只有业务事实，没有指标，是否要先建一个最低可用指标？"

## 6. Handoff To Hs Analysis

Use `hs-analysis` after onboarding when the user asks:

- why a KPI changed
- which driver contributed most
- whether a target is reasonable
- how to write a review or report
- how to build a calculation table or dashboard

Hs Onboarding prepares the map. Hs Analysis uses the map to solve concrete business questions.

## 7. Default Map Display

After the first business framework and asset binding are ready, show the map in this order:

1. Mermaid framework graph in the conversation.
2. Node asset summary table.
3. File jump list for metrics, dimensions, sources, and facts.
4. Supplement prompts.

Do not generate HTML by default. Generate HTML only when the user asks for a shareable, browsable, or stage-summary map.

The conversation map must stay lightweight:

- show node relationships and asset counts
- link to source asset files
- avoid full metric definitions
- avoid completeness labels such as "covered", "partial", or "missing"
