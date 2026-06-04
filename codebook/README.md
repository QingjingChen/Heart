# Codebook

The HEART codebook is the **flat, version-controlled mirror** of the data that
powers the [interactive website](../docs/interactive/). Every CSV here is
regenerated from `docs/interactive/data/*.json`, so the codebook and the
website never drift apart.

If you only want to consume the data, take the CSVs. If you want a single
Excel file, take `heart_codebook.xlsx` (one sheet per CSV). If you are
editing the data, edit the JSON under `docs/interactive/data/` and re-run the
build script.

## Files

| File | What it is | Rows |
|---|---|---|
| `benchmarks.csv` | One row per audited benchmark with dimension, expert tag, paper / code URLs, primary + secondary tool assignments, sub-tool names (EN/ZH), rubrics-improved tags, and adaptation prompt + example. | 103 |
| `tools.csv` | One row per generic repair tool (T01–T14) with EN/ZH name, layer, core practice, problem fixed, applicable scope, boundary vs. nearby tools, automatable vs. needs-human parts, limitations, and evidence counts. | 14 |
| `sub_tools.csv` | One row per (benchmark × role) pair giving the specific repair sub-tool's name (EN/ZH) and its parent tool. | 206 |
| `rubrics.csv` | One row per calibrated audit rubric (R1–R14): name, key question, full 0/1–2/3–4/5 anchors, calibration anchors with bench examples, revision notes, current score distribution + mean — all bilingual. | 14 |
| `policies.csv` | One row per policy / governance source with source name, type, URL, and per-dimension support code (D1/D2/D3). | 16 |
| `mini_cases.csv` | One row per mini case: id, dimension, title, source dataset + entry, rubrics lifted, tools applied, why-improved narrative. | 5 |
| `rubric_tool_matrix.csv` | 14 rubrics × 14 tools evidence-score matrix used for the rubric-matrix heatmap on the website. | 14 |
| `gap_detection.csv` | One row per rubric: typical symptoms, red flags, evidence to inspect, diagnostic questions, per-ethics-domain symptoms (JSON), common misdiagnosis — all bilingual. | 14 |
| `heart_codebook.xlsx` | All eight CSVs as one workbook (one sheet each). Convenience bundle for analysts who prefer Excel. | — |

## Regenerating from website data

```bash
# from repo root
python3 codebook/build_codebook.py
```

The script (`codebook/build_codebook.py`) reads from
`docs/interactive/data/`:

- `bench_map.json` → `benchmarks.csv`, `sub_tools.csv` (parts)
- `t_tools.json` → `tools.csv`
- `rubrics_full.json` → `rubrics.csv`
- `dimensions.json` → `policies.csv`
- `mini_cases.json` → `mini_cases.csv`
- `matrix.json` → `rubric_tool_matrix.csv`
- `gap_detection.json` → `gap_detection.csv`
- `bench_urls.json` → paper/code URLs in `benchmarks.csv`

Run it after any data edit so the codebook tracks the website 1:1.
Requires `openpyxl` for the xlsx bundle (CSV generation works without it).

## Canonical 14 rubrics

The rubric columns and order are kept in sync with
[`../docs/03_fourteen_rubrics.md`](../docs/03_fourteen_rubrics.md):

| Code | EN | ZH |
|---|---|---|
| R1 | Construct clarity | 构念清晰度 |
| R2 | Normative grounding | 规范根据 |
| R3 | Source provenance and evidence fitness | 来源可追溯与证据适配 |
| R4 | Context and stakeholder coverage | 情境与利益相关方覆盖 |
| R5 | Real-world harm linkage | 与现实危害的关联 |
| R6 | Scenario validity | 场景真实性 |
| R7 | Task-format fit | 任务形式适配 |
| R8 | Ground truth and disagreement design | 答案与分歧设计 |
| R9 | Metric validity | 指标有效性 |
| R10 | Evaluator reliability | 评分者可靠性 |
| R11 | Data and annotation QA | 数据与标注质保 |
| R12 | Robustness against gaming and contamination | 对抗博弈与污染稳健性 |
| R13 | Documentation and reproducibility | 文档与可复现 |
| R14 | Maintenance and update governance | 维护与更新治理 |

## What was here before

The previous artefact was a hand-curated 7-sheet Excel master
(`heart_toolkit.xlsx`) plus CSV exports under `exports/`. Those have been
replaced by this site-derived codebook because the website now carries the
canonical labels, sub-tool names, EN/ZH translations, and revised
benchmark count (103, not 104). To inspect the pre-rebuild artefact, see
the repo history before commit that introduced this README.
