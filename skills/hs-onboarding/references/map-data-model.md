# Business Cognition Map Data Model

这份文件只定义“业务认知地图”如何组织和渲染。它不是业务图谱资产文件的完整写作规范。

- 资产文件本身怎么写、每类文件必须包含什么、如何跨文件链接，见 `business-graph-file-contract.md`。
- 本文件只说明地图视图如何读取这些资产，并把它们展示成业务节点、资产数量和跳转清单。
- 地图默认先在 AI 对话内展示；HTML 页面只是可选导出形式。
- 如果本文件和 `business-graph-file-contract.md` 对同一资产字段的定义发生冲突，以 `business-graph-file-contract.md` 为准；本文件只保留地图展示所需的抽取字段。

## Core Objects

### Business Node

Represents one block in the business framework.

Fields:

- `id`: stable node id
- `title`: user-facing node name
- `summary`: what this node means in the business
- `lane`: optional grouping such as C side, B side, matching, revenue, organization
- `assets`: bound metrics, dimensions, data sources, and facts

### Map Asset Reference

Represents an asset item rendered under a business node. The complete file contract for each asset type lives in `business-graph-file-contract.md`; the map only needs the fields below.

Fields:

- `id`
- `asset_type`: one of `metric`, `dimension`, `hierarchy`, `source`, `fact`
- `name`
- `summary`: short display text extracted from the source asset file
- `source_path`
- `linked_nodes`: business node ids where this asset should appear
- `detail_anchor`: optional anchor for jumping to this item in the detail list

Map-specific guidance:

- Do not duplicate full metric definitions, source field lists, hierarchy mappings, or fact evidence in the map data.
- Use `summary` only as a compact display excerpt.
- The click-through should send the user back to the source asset file or detail list generated from that file.

## Rendering Rules

The default rendering is a conversation map, not an HTML page.

### Conversation Map

Render these blocks:

1. Mermaid graph: node title, node summary if short enough, and compact asset counts.
2. Asset summary table: one row per business node.
3. File jump list: grouped links to metric, dimension, hierarchy, source, and fact files.
4. Supplement prompts.

For each business node, render:

- node title
- node summary
- asset counts:
  - metrics count
  - dimensions count
  - hierarchies count
  - data sources count
  - facts count
- anchor links to detail lists

Do not render "complete", "partial", or "missing" as judgment labels.

Mermaid should stay readable. If the business has too many nodes, render the main framework first and move detailed asset lists into tables and file links.

### HTML Map

Generate HTML only when the user asks for browsing, sharing, or stage-summary output.

HTML can use the same data model as the conversation map, but may add:

- clickable asset counts
- collapsible detail lists
- visual lanes for C side, B side, matching, revenue, organization, and feedback
- export-friendly layout

## Update Rules

The map is a view of the asset system.

- Add metric -> node metric count increases and detail list updates.
- Delete metric -> node metric count decreases and detail list updates.
- Rename metric -> detail list updates.
- Add dimension -> node dimension count increases.
- Add hierarchy -> node hierarchy count increases.
- Add data source -> node data source count increases.
- Add business fact -> node fact count increases.
- Move asset to another node -> both node counts update.

The map should not be manually maintained separately from the metric asset system.
