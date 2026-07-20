# Business Graph Maintenance Rules

## 1. Multi-Business Overview

`business_graphs/registry.md` is the top-level selector for all Hs skills.

Maintain it when:

- a new business graph is created
- aliases change
- a graph status changes
- a graph is archived or replaced
- a user may ask about multiple businesses, competitors, or industries

Minimum fields:

| graph_id | business name | aliases | status | entry |
|---|---|---|---|---|

If multiple graphs exist and the user did not specify one, Hs skills must ask which graph to use.

## 2. Single-Business Overview

Each `business_graphs/{business_id}/manifest.md` is the overview for one business tree.

Maintain it when:

- business definition changes
- aliases change
- applicable scope changes
- key entry files change
- asset counts change
- startup rules change

Minimum sections:

- basic info
- business definition
- applicable scope
- entry files
- asset counts
- startup rules

The manifest is not a metric definition file. Do not duplicate full metric logic there.

## 3. Indexes

`indexes/ASSET_INDEX.md` lists all assets.

`indexes/METRIC_INDEX.md` lists all metric-like nodes and helps analysis avoid missing relevant nodes.

After adding, deprecating, renaming, or deleting assets:

- update both indexes when affected
- preserve the rule that indexes do not replace original asset files
- keep paths clickable and relative to the business graph root when possible
- if an index and an asset file conflict, the asset file wins and the index needs repair

## 4. Bindings And Maps

Bindings connect assets to business nodes. The business cognition map should be rendered from these bindings or equivalent asset metadata, not manually maintained separately.

When assets change:

- update `bindings/BINDINGS.md` if present
- update business node files if they list assets
- update map data or regenerate exported HTML only when needed
- for day-to-day work, prefer conversation map output over HTML

Do not use map labels such as "complete", "partial", or "missing". Show asset counts and lists.

## 5. Link Consistency

Common links:

- metric -> dimensions / hierarchies / sources / facts
- dimension -> applicable metrics / source fields / hierarchy
- hierarchy -> participating dimensions / source / affected metrics
- fact -> affected metrics, dimensions, hierarchies, or sources
- source -> supported metrics and dimensions
- business node -> bound assets

If a link target does not exist:

- write `待补`
- explain what is missing
- create a follow-up item

Do not invent source files or facts that the user did not provide or confirm.

## 6. Asset Counts

When asset counts appear in manifest, bindings, or maps, update them after changes.

Counts should reflect actual files or active assets, depending on the local convention. If deprecated assets are included, mark that convention explicitly.

## 7. Safe Defaults

- Add new uncertain assets as `status: draft`.
- Mark user-supplied but unverified facts as hypothesis, user_claim, or pending verification.
- Deprecate before delete.
- Prefer linking existing assets before creating duplicates.
- For a business-specific detail, write it into the selected business graph, not into a reusable Skill.
