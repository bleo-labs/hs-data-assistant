# Hs Graph Workflow

## 1. Operation Types

### Add Asset

Use when the user wants to add a metric, dimension, hierarchy, fact, source, business node, or business tree.

Required steps:

1. Choose the target business graph.
2. Check whether a similar asset already exists.
3. Assign a stable id using the local sequence style.
4. Create the asset under the correct folder.
5. Link it to related assets.
6. Bind it to at least one business node or explain why it is temporarily unbound.
7. Update indexes, manifest asset counts, and map/binding views.

### Modify Asset

Use when the user says a definition, formula, scope, source, dimension, or business fact is wrong or incomplete.

Required steps:

1. Read the original asset file.
2. Identify the exact section to change.
3. List affected linked assets.
4. Classify risk.
5. For high-risk changes, ask for confirmation before writing.
6. Update the asset and any reverse links or summaries.

### Link Assets

Use when existing assets are correct but disconnected.

Typical cases:

- A metric needs a source link.
- A dimension should point to a hierarchy.
- A fact affects a metric but is not linked.
- A source supports a metric but the metric does not link back.
- A business node should include an existing metric or fact.

Linking is usually medium risk unless it changes interpretation.

### Deprecate Or Delete

Default to deprecating, not deleting.

Deprecation steps:

1. Set `status: deprecated`.
2. Add replacement asset if one exists.
3. Add reason and date.
4. Update indexes and references.

Deletion is high risk. Before deleting, output an impact list:

- inbound links
- outbound links
- indexes
- binding rows
- map references
- analysis tasks that may depend on it if known

### Update Registry Or Manifest

Use when adding a new business tree, changing aliases, changing business scope, or updating asset counts.

Rules:

- `registry.md` is the multi-business entry.
- `manifest.md` is the single-business overview.
- A business graph cannot be used reliably if either file is stale.
- For users who study multiple businesses, aliases and status in `registry.md` are not optional.

### Audit And Repair

Use when the user asks whether the graph is healthy, or after a batch change.

Check:

- assets missing YAML frontmatter
- broken Markdown links
- orphan metrics not bound to business nodes
- metrics without source links
- sources without supported metric links
- dimensions that should point to hierarchy but do not
- hierarchy files with missing participating dimensions
- asset counts in manifest inconsistent with folders
- `METRIC_INDEX.md` or `ASSET_INDEX.md` missing current assets

## 2. Confirmation Rules

Only read and audit without confirmation.

Ask before writing when:

- changing formulas
- changing applicable scope
- changing ids or filenames
- deprecating or deleting
- changing registry aliases or active business status
- changing hierarchy mappings
- applying a feedback/writeback card that may alter future analysis behavior

For simple new draft assets or links, one concise change plan is enough. If the user has already explicitly asked to apply the specific change, proceed and report what changed.

## 3. Writeback Card Intake

When input comes from feedback, analysis, research, or user correction, convert it into a graph writeback card before changing files.

```markdown
## Graph Writeback Card

- Trigger source:
- Found issue:
- Why it matters:
- Suggested change:
- Affected graph:
- Affected assets:
- Risk level:
- Requires confirmation:
```

Do not treat a writeback card as final truth until it is either confirmed by the user or supported by existing source files.

## 4. Output After Execution

After any write operation, output:

| item | result |
|---|---|
| Target graph |  |
| Changed files |  |
| Updated indexes |  |
| Updated registry/manifest |  |
| Remaining gaps |  |
| Risk notes |  |
