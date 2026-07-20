# Feedback Workflow

## 1. Feedback Card

Use this card whenever the user says a result is wrong, incomplete, hard to read, overfitted, missing evidence, or should be written back.

```markdown
## Hs Feedback Card

- Trigger source:
- Original task:
- Expected behavior:
- Actual behavior:
- User evidence:
- Problem type:
- Affected Hs ability:
- Affected business graph:
- Target source of truth:
- Risk level:
- Recommended action:
- Requires confirmation:
- Owner skill:
- Status:
```

## 2. Target Source Of Truth

Choose only one primary target:

| target | when to choose |
|---|---|
| business_graph | missing or wrong metrics, dimensions, hierarchy, source, fact, binding, index, or manifest |
| hs-entry | wrong routing, missing construction graph, weak clarification, wrong task strength |
| hs-onboarding | first business map logic, C/B/matching frame, initial graph generation |
| hs-graph | asset CRUD rules, index sync, manifest/registry maintenance |
| hs-analysis | metric audit, table blueprint, calculation mode, evidence structure |
| hs-research | external sample plan, source quality, benchmark mapping |
| hs-output | report/table/chart/readability format |
| docs | install, quickstart, architecture, user-facing explanation |
| no_change | rule already exists; issue is one-off execution or user input changed |

## 3. Action Types

| action | meaning |
|---|---|
| record_only | record the issue; no file change now |
| route_to_graph | ask or invoke `hs-graph` to update business graph assets |
| propose_skill_change | produce a change plan for skill rules |
| patch_skill | directly edit a low/medium-risk skill issue |
| patch_output_contract | update output format rules |
| patch_docs | update human-facing docs |
| ask_confirmation | stop and ask before high-risk changes |

## 4. Completion Output

After handling feedback, output:

```markdown
## Feedback Result

- Classification:
- Decision:
- Files changed:
- Files not changed:
- Follow-up:
- Same issue prevention:
```

If the issue is not fixed, say why and what is needed next.
