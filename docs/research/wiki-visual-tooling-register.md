# Wiki Visual Tooling Register

This page records visual and knowledge-map tools that could be added when the research needs them. The intent is not to install every tool immediately. The intent is to keep a practical register so new information can be matched to the right visual form.

## Current baseline

The wiki currently uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with [PyMdown SuperFences](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#superfences) configured for Mermaid diagrams.

Mermaid is already suitable for:

- decision trees;
- governance flowcharts;
- sequence diagrams;
- state diagrams;
- entity-relationship diagrams;
- simple journey maps.

It should remain the default for diagrams that are small enough to read directly in Markdown and where source control readability matters.

## Tool register

| Tool | What it adds | Use when | Current posture |
| --- | --- | --- | --- |
| [Mermaid in Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/diagrams/) | Text-based flowcharts, sequence diagrams, ER diagrams, state diagrams, and related diagram types. | A process or decision can be expressed clearly as code in a Markdown fence. | Enabled. Default first choice. |
| [mkdocs-drawio](https://tuunit.github.io/mkdocs-drawio/) | Embeds `.drawio` / diagrams.net files as normal Markdown images. Supports multi-page diagrams, hosted diagrams, print/edit buttons, dark mode, and Material compatibility. | A board-facing or operational diagram is too visual or layout-heavy for Mermaid. | Strong candidate to enable first. |
| Static SVG, PNG, or WebP assets | Stable image assets copied through the MkDocs static build. | A diagram is final, brand/presentation-focused, or should not depend on runtime JavaScript. | Already available through ordinary Markdown image links. |
| [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox) | Click-to-zoom image lightbox for diagrams and screenshots. | Diagrams, screenshots, or evidence maps are too wide to read inline. | Strong candidate alongside draw.io. |
| [mkdocs-caption](https://pypi.org/project/mkdocs-caption/) | Figure and table captions, numbering, and cross-reference text. | The wiki needs report-style figures, board pack references, or formal numbered exhibits. | Candidate once visuals become board/report outputs. |
| [mkdocs-charts-plugin](https://github.com/timvink/mkdocs-charts-plugin) / [Vega-Lite](https://vega.github.io/vega-lite/docs/) | Declarative charts from JSON/data using Vega-Lite. | We have structured evidence, maturity, risk, validation, or inspection-readiness data to visualize. | Candidate after data structure stabilises. |
| [mkdocs-plotly-plugin](https://haoda-li.github.io/mkdocs-plotly-plugin/) | Interactive charts from Plotly JSON. | We need richer interactive charts than Vega-Lite, such as drillable dashboards or complex hover detail. | Later candidate; heavier than Vega-Lite. |
| [mkdocs-table-reader-plugin](https://timvink.github.io/mkdocs-table-reader-plugin/) | Inserts tables from CSV, JSON, Excel, YAML, TSV, and related files. | Evidence maps, RFL clause registers, vendor comparisons, or maturity tables should become data files rather than hand-written Markdown tables. | Candidate when tables become large or repeated. |
| [mkdocs-markmap](https://github.com/markmap/mkdocs_markmap) / [Markmap](https://markmap.js.org/docs/markmap) | Interactive mind maps from Markdown hierarchy. | A research topic needs a browsable concept map rather than a strict process diagram. | Candidate for research scoping and topic maps. |
| [mkdocs-kroki-plugin](https://pypi.org/project/mkdocs-kroki-plugin/) / [Kroki](https://kroki.io/) | One route to many diagram languages, including PlantUML, C4, GraphViz, D2, BPMN, Excalidraw, Vega, Vega-Lite, WaveDrom, and more. | Mermaid and draw.io are not enough, or a specialist notation is needed. | Powerful but heavier; consider privacy and hosting before enabling. |
| [mkdocs-network-graph-plugin](https://pypi.org/project/mkdocs-network-graph-plugin/) | Interactive knowledge network graph for Material for MkDocs, with full-site and local page connections. | The wiki needs an Obsidian-like site map showing how research pages connect. | Best MkDocs-native knowledge-map candidate. |
| [mkdocs-obsidian-interactive-graph-plugin](https://github.com/daxcore/mkdocs-obsidian-interactive-graph-plugin) | Obsidian-like interactive graph for Material for MkDocs using ECharts and wikilinks. | The wiki moves toward Obsidian-style wikilinks and wants a closer Obsidian visual pattern. | Secondary knowledge-map candidate; more moving parts than network graph. |
| [mkdocstrings/autorefs](https://github.com/mkdocstrings/autorefs) | Cross-page references, anchors, and backlink recording for other plugins or hooks. | Backlinks, referenced-by sections, or richer cross-reference behavior become important. | Infrastructure candidate, not a visual graph by itself. |
| [Foam graph visualization](https://djplaner.github.io/foam-with-material-for-mkdocs/user/features/graph-visualization/) | VS Code knowledge graph for Markdown notes, including files, tags, links, filters, and hover/click navigation. | Editors want a local authoring graph while writing the wiki. | Authoring-side option, not a published MkDocs site feature. |

## Obsidian-like knowledge map finding

Yes. The closest published-wiki options are:

1. **mkdocs-network-graph-plugin**: best fit for this site if we want a public, Material-compatible knowledge graph. It is described as an interactive knowledge network graph for Material for MkDocs and supports both full-site overview and local page connections.
2. **mkdocs-obsidian-interactive-graph-plugin**: closest in intent to Obsidian, but it currently relies on wikilinks, JavaScript assets, jQuery, and ECharts. It may be useful if the wiki adopts Obsidian-style `[[wikilinks]]`, but it is a less conservative first choice.
3. **Foam graph visualization**: useful for local authoring in VS Code, but not a native published-site graph.
4. **autorefs backlinks**: useful if the site needs backlink sections or graph data, but it does not itself render an Obsidian-style graph.

The recommended first experiment is **mkdocs-network-graph-plugin** on a branch, because it is designed for Material for MkDocs, has simple `plugins: - graph` setup, and avoids changing the wiki writing style to wikilinks.

## Use triggers

| New information type | Prefer |
| --- | --- |
| CQC scope decision pathway | Mermaid first; draw.io if board-facing. |
| Board assurance journey | draw.io, then static SVG export if stable. |
| Evidence pack structure | Mermaid or markmap. |
| RFL clause maturity dashboard | Vega-Lite or Plotly once data-backed. |
| Large RFL/vendor/evidence tables | table-reader from CSV or YAML. |
| Knowledge relationships across pages | mkdocs-network-graph-plugin. |
| Research concept map | markmap. |
| Formal board/report exhibit | caption plus glightbox. |
| Architecture/product modules | Mermaid, draw.io, or Kroki C4/PlantUML. |
| BPMN-style workflow | Kroki BPMN or draw.io. |
| Hand-drawn workshop sketch style | Kroki Excalidraw or draw.io. |

## Adoption order

1. **Shortlist now**: Mermaid, draw.io, static SVG/PNG, glightbox, caption, markmap, table-reader, Vega-Lite, Plotly, Kroki, network graph, Obsidian interactive graph, autorefs, Foam.
2. **Install only when needed**: do not add plugins without an immediate page or research output that will use them.
3. **First likely install**: `mkdocs-drawio` and `mkdocs-glightbox`, because they directly improve board-facing diagrams and large evidence maps.
4. **First knowledge-map experiment**: `mkdocs-network-graph-plugin` on a branch.
5. **Data-visualisation install**: add table-reader and Vega-Lite/charts only after evidence registers are converted to structured data.
6. **Kroki decision**: use only if we need specialist diagram languages and have decided whether to use hosted Kroki or a self-hosted service.

## Guardrails

- Prefer text-based diagrams where the source should be reviewable in Git.
- Prefer draw.io for diagrams that need manual layout, board polish, or iterative discussion.
- Prefer static SVG exports for visuals that should remain stable in LLM exports, printed material, or board packs.
- Avoid adding JavaScript-heavy interactive visuals unless they answer a real research question.
- Check whether a plugin changes Markdown syntax, page loading, search, or GitHub Pages compatibility before enabling it.
- Check privacy and dependency implications before using hosted rendering services such as Kroki.
- Keep LLM wiki usability in mind: every important visual should also have a short textual explanation nearby.

## Related pages

- [Product Research Roadmap](product-research-roadmap.md)
- [Platform Opportunity](platform-opportunity-tool-landscape.md)
- [Platform Tool Landscape](platform-tool-landscape.md)
- [Product Blueprint](platform-product-blueprint.md)
- [Source Map](source-map.md)
