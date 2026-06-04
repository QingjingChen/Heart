# HEART Demo

The interactive HEART demo now lives **inside this repository** as a static
GitHub-Pages site — no separate backend or repo needed.

## 🌐 Try it

**Live**: [https://qingjingchen.github.io/Heart/interactive/](https://qingjingchen.github.io/Heart/interactive/)

**Source**: [`docs/interactive/`](../docs/interactive/) — vanilla HTML + JS + JSON,
no build step. To run locally:

```bash
cd docs/interactive
python3 -m http.server 8000
# then visit http://localhost:8000
```

## 🗺 What you get

The site walks you through HEART end to end:

| Stage | Page | What it shows |
|:---|:---|:---|
| **Overview** | `index.html` | Architecture: bench corpus → diagnosis → repair → examples |
| **A · Scope** | `dimensions.html` | 5 ethical dimensions × 18 policy sources; coverage matrix |
| **B · Diagnose** | `rubrics.html` | 14 calibrated rubrics with v2 anchors + bench examples per score |
| **C · Repair** | `tools.html` / `benches.html` / `rubric_matrix.html` | 14 generic tools, 103 specific sub-tools, Gap → Tool workflow |
| **D · Apply** | `mini_cases.html` | 5 worked before/after revision examples |

## 📦 Where the data comes from

All data on the site is loaded from JSON files under `docs/interactive/data/`,
themselves derived from the master workbook `workbook/heart_toolkit.xlsx`.
Nothing is generated at runtime.

| Workbook source | Site JSON |
|:---|:---|
| `workbook/exports/benchmarks_103_tool_distribution.csv` | `data/bench_map.json` |
| `workbook/exports/rubrics_14_anchors.csv` | `data/rubrics_full.json` |
| `workbook/exports/toolbox_master.csv` | `data/t_tools.json` |
| `datasets/sources.md` | `data/bench_urls.json` (paper / code / mirror links) |

If you change the workbook, regenerate the JSONs and commit both — the site
is intentionally static.
