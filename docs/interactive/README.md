# HEART · Interactive Workbox & Rubric Index

Static HTML/JS companion to the HEART resource paper. 6 pages, no build
step. GitHub Pages serves it as-is.

## Pages

| Page | Purpose |
|---|---|
| `index.html` | Landing + 3 rubric layers overview + tool category table. |
| `rubric_matrix.html` | Plotly 14×14 heatmap. Click any cell to open explainable card with repair mechanism, strongest benchmark evidence (with deep paper link), and adaptation prompt. |
| `tools.html` | 14 tools as a toolbox UI grouped by the **3 rubric layers** (Content Validity / Evaluation Design / Governance Reliability). Click any card to open a modal with collapsible accordion sections. |
| `benches.html` | DataTables-searchable 103-bench lookup. Column 3 is **专家标签** (expert label — all 103 are filled; the 18 originally blank ones were extracted via Qwen Plus from each bench's tool explanation + adaptation example). Click `+` for the full primary/secondary mapping with sub-tool, prompt, example. |
| `vignettes.html` | 5 paper-level vignettes (one per policy dimension), 150–220 words each. |
| `mini_cases.html` | **5 real-data adaptation examples** (BBQ Age / XSTest / FreshQA / PrivacyLens / CounselBench-Adv). Each shows the original item verbatim (with entry ID), the HEART-revised item, and which T-tools + operations were applied, the lifted rubrics, and a why-improved note. |

## Tool layering (rubric layer)

Each tool is sorted into the rubric layer matching its primary improved rubric:

| Layer | Tools |
|---|---|
| **内容有效性 Content Validity** (R1–R5) | T01 · T02 · T03 · T05 · T10 |
| **评测设计 Evaluation Design** (R6–R10) | T04 · T06 · T07 · T09 · T11 · T12 |
| **治理可靠性 Governance Reliability** (R11–R14) | T08 · T13 · T14 |

## Data sources

All data lives under `data/` and is exported once from
`HEART_Excel_含原始与修订_整合压缩.xlsx`:

| File | Source sheet |
|---|---|
| `t_tools.json` | `交付物4_Toolbox整合说明_压缩` (14 T-tools + rubric_layer field added) |
| `bench_map.json` | `Bench→整合工具映射` (103 benches; column renamed: 人工核对标签 → 专家标签; blanks filled) |
| `rubric_index.json` | `Tool→Rubric索引_可解释` (37 explainable cells) |
| `matrix.json` | `Tool×Rubric矩阵_压缩` (14×14 numeric) |
| `prompts.json` | `细分工具→Prompt示例` (206 sub-tool prompts) |
| `manual_labels.json` | `人工标签→压缩工具映射` (85 expert labels) |
| `cqj.json` | `Tool来源分布表-cqj` (103-bench source) |
| `bench_urls.json` | parsed from `datasets/sources.md` (102 paper URLs) |
| `vignettes.json` | dimension vignettes |
| `mini_cases.json` | 5 real-data mini cases (BBQ / XSTest / FreshQA / PrivacyLens / CounselBench-Adv) |
| `filled_labels.json` | the 18 expert labels filled via Qwen for originally-blank rows |

## Tech stack

- Plotly.js (CDN) for the heatmap
- DataTables (CDN) for the searchable bench table
- vanilla CSS in `assets/main.css`
- no build step

## Local preview

```bash
cd docs/interactive
python3 -m http.server 8000
# open http://127.0.0.1:8000/
```

## GitHub Pages

Served from `docs/interactive/` on the `main` branch.
Live: `https://qingjingchen.github.io/Heart/interactive/`
