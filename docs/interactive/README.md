# HEART · Interactive Workbox & Rubric Index

Static HTML/JS companion to the HEART resource paper. Five pages, no build
step, no server-side code — everything loads JSON files at runtime so
GitHub Pages can serve it as-is.

## Pages

| Page | Purpose |
|---|---|
| `index.html` | Landing page with the 5 tool categories + quick links. |
| `rubric_matrix.html` | Plotly heatmap of **14 audit rubrics × 14 canonical tools**. Click any cell to open a card showing the repair mechanism, the strongest benchmark evidence (with deep links to the original paper), and the adaptation prompt the demo backend would use. |
| `tools.html` | One card per tool (T01–T14): canonical name, core practice, boundary, generic adaptation skeleton, source-row prompt examples, polished examples, auto-vs-human gating, member benches with paper URLs, and represented sub-tools. |
| `benches.html` | Searchable 103-benchmark lookup (DataTables). Each row shows the primary and secondary canonical tools, sub-tool, improved rubrics; click `+` for the full adaptation prompt and example. |
| `vignettes.html` | The 5 dimension vignettes (Human-Centered / Fairness / Safety / Trustworthy / Privacy), plus the BBQ → Chinese customer-service mini case from the paper §5.3 with colour-highlighted diffs. |

## Data sources

All driving data lives under `data/`:

| File | Source sheet |
|---|---|
| `t_tools.json` | `交付物4_Toolbox整合说明_压缩` (14 T-tools full definition) |
| `bench_map.json` | `Bench→整合工具映射` (103 benches → T-tools mapping with sub-tools, prompts, examples) |
| `rubric_index.json` | `Tool→Rubric索引_可解释` (37 explainable cells per T × rubric) |
| `matrix.json` | `Tool×Rubric矩阵_压缩` (14×14 numeric evidence-weight matrix) |
| `prompts.json` | `细分工具→Prompt示例` (206 sub-tool prompt rows) |
| `manual_labels.json` | `人工标签→压缩工具映射` (85 manual labels → T-tools) |
| `cqj.json` | `Tool来源分布表-cqj` (103-bench source with manual labels) |
| `bench_urls.json` | parsed from `datasets/sources.md` (102 paper URLs) |
| `vignettes.json` | from the `Vignettes 五维案例` sheet (5 baseline-gap → tool → revised vignettes) |

Source workbook: `HEART_Excel_含原始与修订_整合压缩.xlsx`.

## Tech stack

- Plotly.js (CDN) — interactive heatmap
- DataTables (CDN) — searchable bench table
- vanilla CSS — single `assets/main.css`
- no build step, no bundler

## Local preview

```bash
cd docs/interactive
python3 -m http.server 8000
# open http://127.0.0.1:8000/
```

## GitHub Pages

This folder is served by GitHub Pages from the `main` branch's `docs/` path.
Live URL (after Pages is enabled): `https://qingjingchen.github.io/Heart/interactive/`.

To regenerate after the workbook is updated, re-export the 9 JSON files
under `data/` from the source xlsx with `openpyxl` (any script that
mirrors the `dump_sheet_as_dicts` pattern works); the HTML files do not
need to be touched.
