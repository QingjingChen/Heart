# HEART Workbook CSV Exports

This folder mirrors the canonical xlsx workbook (`workbook/heart_toolkit.xlsx`)
as four English CSV exports. Each CSV is regenerated whenever the master
workbook is rev'd; rubric anchors are calibrated against the surveys and
benchmarks listed at the bottom of this file.

## Files

| File | Rows | Columns | Source sheet |
|---|---|---|---|
| `benchmark_diagnosis.csv` | 137 | 17 | Workbook sheet "Benchmark诊断" — per-benchmark per-rubric scoring with paper / issue / score evidence and survey cross-checks. |
| `benchmarks_104_tool_distribution.csv` | 105 | 27 | Workbook sheet "Tool来源分布表" — one row per benchmark, with the 14-rubric scoring, representative tool, lineage critiques, adaptation example, and survey cross-views. |
| `rubrics_14_anchors.csv` | 15 | 11 | Workbook sheet "诊断rubrics说明" — calibrated 4-bucket anchors (0 / 1-2 / 3-4 / 5) for each of the 14 rubrics, with score distribution and calibration sources. |
| `toolbox_48_tools.csv` | 48 | 9 | Workbook sheet "Toolbox整合说明" — 48 repair tools, aligned with the 104-benchmark master table. 12 of the 48 tools have at least one representative benchmark instance in the master; 30 are expert-recommended (gap-driven) — i.e., the diagnosis identifies a repeatable failure mode but the master corpus does not yet contain a benchmark that uses the corresponding repair tool. |

## Methodology

### How each benchmark row was scored (`benchmark_diagnosis.csv`)

Each `(benchmark × rubric)` cell follows a three-part structure:

1. **Paper:** what the original benchmark paper claims to do for this rubric (extracted verbatim from the paper text).
2. **Issue:** the limitation. We use two complementary sources:
   - the paper's own *Limitations* section (authors' self-acknowledged
     limits), and
   - later sibling papers' *Related work* critiques (e.g., **CBBQ** critiques
     **BBQ** for not exposing Chinese-context bias categories; **NaVAB**
     critiques **MoralStories** for relying on US Reddit norms). Sibling
     papers are usually more candid about a benchmark's blind spots than the
     authors themselves.
3. **Score:** 0--5 according to the rubric's calibrated anchor. We focus the
   write-up on the **weakest** dimensions; for the remaining dimensions we
   record a brief evaluation rather than a full three-part argument.

### Global calibration pass

After all benchmark rows were independently scored, a global comparison pass
was applied across the 103 benchmark corpus to:

- align scores on similar benchmarks (so that, e.g., **CrowS-Pairs** and
  **StereoSet** receive comparable Construct-clarity scores when their gaps
  are of similar severity),
- calibrate each rubric's anchors against the actual score distribution
  observed in the corpus (anchors that produced no 5-score instances were
  rewritten so that the 5-score requirement is achievable but discriminating),
- back-fill the calibrated anchors into `rubrics_14_anchors.csv`.

### Rubric calibration log (`rubrics_14_anchors.csv`)

The published rubric anchors are the **v2 calibrated** version. Each row's
**Calibration source** column lists the surveys and benchmarks used to
calibrate that rubric. Calibration combined:

- the original 0 / 1-2 / 3-4 / 5 anchors,
- a *Calibrated threshold* column with concrete benchmark anchors (e.g.,
  *"0 = Kleinberg; 2 = StereoSet/CrowS-Pairs/Winogender; 4 =
  CBBQ/KoBBQ/HolisticBias/WinoQueer"*),
- *Revision suggestions* identifying gaps in the original anchors (typically
  missing 5-score conditions or vague 3-4 boundaries),
- *Rubric v2 standards* drafted against the survey corpus and folded back
  in.

These four columns are now collapsed into the four anchor cells; the
calibration audit trail is summarised in the *Calibration source* column.

### Toolbox alignment (`toolbox_48_tools.csv`)

Each of the 48 repair tools was cross-checked against the 104-benchmark
master table by tokenised match on the master's *Representative tool*
column. Two outcomes:

- **12 matched tools** — at least one benchmark in the master corpus
  implements the tool; the master's `Adaptation example` is filled into the
  tool's *Mini case* column, and the matched benchmark name(s) appear in the
  *Representative source* column under `Master instances:`.
- **30 expert-recommended (gap-driven) tools** — no benchmark in the
  master corpus implements the tool, but expert review of the diagnosis
  identifies a recurring weakness that the tool would repair. These tools
  are tagged `Expert-recommended (gap-driven; no benchmark instance in
  master corpus)` in the *Representative source* column.

## Reproducing the calibration

The translation and calibration scripts live in this repository under
`workbook/scripts/` (added as a separate commit). They re-read the source
xlsx, regenerate the four CSVs, and require a DashScope (Qwen) key in
`~/.dashscope_key`.

## Provenance

- Master xlsx: `workbook/heart_toolkit.xlsx`
- Survey foundation: `datasets/sources.md` *(Survey papers consulted)*
- Per-benchmark URLs: `datasets/sources.md` *(104-entry index)*
