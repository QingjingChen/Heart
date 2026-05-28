# Workbook

This folder contains the **master HEART workbook** and its CSV exports.

## Files

| File | What it is |
|---|---|
| `heart_toolkit.xlsx` | The master workbook (7 sheets). Contains formatting, notes, and cell comments not preserved in CSV. |
| `exports/benchmarks_104_tool_distribution.csv` | One row per benchmark (n = 103 + header). Each row has its primary dimension, representative tool, 14-rubric annotations, adaptation example, lineage critiques, self-acknowledged limits, external survey views, and a Chinese synthesis. |
| `exports/toolbox_48_tools.csv` | The tool-indexed toolbox: 48 entries with `English name / Chinese name / core practice / problem repaired / rubric improved / applicable ethics scenarios / source paper / limitations / mini-case`. |
| `exports/benchmark_diagnosis_140rows.csv` | The 14-rubric diagnostic main table — one row per (benchmark × rubric-layer) cell. |
| `exports/rubrics_14_anchors.csv` | The 14 rubrics with 0–5 anchors, calibration examples, and the current score distribution across the 103 reviewed papers. |
| `exports/citation_verification.csv` | Citation-by-citation verification status for the most-cited works. |

## Sheet-by-sheet description (xlsx)

| Sheet | Rows × Cols | Purpose |
|---|---|---|
| `Tool来源分布表` (Tool Source Distribution) | 104 × 27 | One row per benchmark, with full rubric annotations |
| `Toolbox整合说明` (Toolbox Integration) | 48 × 9 | The 48-entry tool-indexed toolbox |
| `Benchmark诊断` (Benchmark Diagnosis) | 140 × 17 | 14-rubric main diagnostic table |
| `诊断rubrics说明` (Rubric Anchors) | 21 × 14 | 0–5 anchors + score distributions |
| `引用核验` (Citation Verification) | 20 × 4 | Source verification log |
| `评价体系（旧）` (Legacy scoring v1) | 25 × 13 | Retained for reproducibility of rubric re-derivation |
| `评价体系解释（旧）` (Legacy scoring v1, anchors) | 20 × 5 | Retained for reproducibility |

## How the CSV exports were produced

```python
import openpyxl, csv
wb = openpyxl.load_workbook('heart_toolkit.xlsx', data_only=True)
for sheet_name, out_name in {
    'Tool来源分布表':       'exports/benchmarks_104_tool_distribution.csv',
    'Toolbox整合说明':      'exports/toolbox_48_tools.csv',
    'Benchmark诊断':        'exports/benchmark_diagnosis_140rows.csv',
    '诊断rubrics说明':       'exports/rubrics_14_anchors.csv',
    '引用核验':             'exports/citation_verification.csv',
}.items():
    ws = wb[sheet_name]
    with open(out_name, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            w.writerow(['' if c is None else c for c in row])
```

The xlsx is the source of truth. Re-run this snippet after any edit to keep
the CSVs in sync.

## Notes on column semantics

The 14 rubric columns in `benchmarks_104_tool_distribution.csv` follow the
order documented in [`../docs/03_fourteen_rubrics.md`](../docs/03_fourteen_rubrics.md):

1. Construct clarity (构念清晰度)
2. Normative grounding (规范基础)
3. Source provenance and evidence fitness (来源可追溯)
4. Context and stakeholder coverage (语境与主体覆盖)
5. Real-world harm linkage (现实伤害连接)
6. Scenario validity (场景真实性)
7. Task-format fit (任务形式适配)
8. Ground truth and disagreement design (答案与分歧设计)
9. Metric validity (指标有效性)
10. Evaluator reliability (评分器可靠性)
11. Data and annotation QA (数据与标注质保)
12. Robustness against gaming and contamination (防污染与防刷榜)
13. Documentation and reproducibility (文档与可复现)
14. Maintenance and update governance (时效性与动态演进)

Each cell records the **textual evidence** supporting that rubric for the
given benchmark, not a numeric score. The numeric distribution per rubric is
in `rubrics_14_anchors.csv`.
