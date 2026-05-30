# HEART Workbook CSV Exports

This folder mirrors the canonical xlsx workbook (`workbook/heart_toolkit.xlsx`)
as English exports. Each artefact is regenerated whenever the master workbook
is rev'd; rubric anchors are calibrated against the surveys and benchmarks
listed in `rubrics_14_anchors.csv` → *Calibration source*.

## Files

| File | Rows | Purpose |
|---|---|---|
| `benchmark_diagnosis.csv` | 137 | Per-benchmark per-rubric scoring with paper / issue / score evidence and survey cross-checks. |
| `benchmarks_104_tool_distribution.csv` | 105 | One row per benchmark × 27 columns: 14-rubric scoring, representative tool, lineage critiques, adaptation example, and survey cross-views. |
| `benchmarks_104_tool_distribution.xlsx` | 105 | xlsx version of the same table with frozen header, wrapped cells, and column widths tuned for human review. |
| [`benchmarks/`](benchmarks/index.md) | 104 cards | One markdown card per benchmark, sectioned by 14 rubrics + lineage critiques + self-acknowledged limits + survey views + synthesis. Easier to read than the wide CSV; deep-linkable on GitHub. |
| `rubrics_14_anchors.csv` | 15 | Calibrated 4-bucket anchors (0 / 1–2 / 3–4 / 5) for each of the 14 rubrics, with score distribution and per-rubric calibration sources. |
| `toolbox_master.csv` | 20 | Consolidated repair-tool list with canonical name, core practice, problem fixed, **benchmark instances** in the 104-master, survey/methodology refs, and mini case. Replaces the previous 48-row toolbox sheet. |
| `tools_by_dimension.csv` | 48 | Long-format mapping `Dimension × Tool` for each of the 5 dimensions (Human-Centered / Fairness / Safety / Trustworthiness / Privacy). Records *why* the tool repairs problems in that dimension and the benchmark/survey reference. |
| `tools_by_rubric.csv` | 50 | Long-format mapping `Rubric × Tool` for each of the 14 rubrics. Records *how* the tool lifts the score on that rubric and the benchmark/survey reference. |

## Three views of the toolbox

The toolbox is published as **three tables that share the same `Tool` primary key**:

- `toolbox_master.csv` — **what each tool is** (definition + concrete benchmark instances).
- `tools_by_dimension.csv` — **which 5-dimension problem each tool repairs** (long format; one row per `(Dimension, Tool)`). This is the *applicability* view: for a benchmark in a given dimension, which tools should you reach for?
- `tools_by_rubric.csv` — **how each tool lifts each of the 14 rubric scores** (long format; one row per `(Rubric, Tool)`). This is the *scoring* view: for a low rubric score, which tools should you apply to raise it?

Dimension and rubric views are *not duplicates* — they answer different questions:

- `rubrics_14_anchors.csv` defines **what each rubric measures** and how to score it.
- `tools_by_rubric.csv` defines **which repair tools lift the score on that rubric** (and on which benchmarks they have a real-world instance).

## Methodology

### How each benchmark row was scored (`benchmark_diagnosis.csv`)

Each `(benchmark × rubric)` cell follows a three-part structure:

1. **Paper:** what the original benchmark paper claims to do for this rubric (extracted verbatim from the paper text).
2. **Issue:** the limitation. We use two complementary sources:
   - the paper's own *Limitations* section (authors' self-acknowledged limits), and
   - later sibling papers' *Related work* critiques (e.g., **CBBQ** critiques **BBQ** for not exposing Chinese-context bias categories; **NaVAB** critiques **MoralStories** for relying on US Reddit norms). Sibling papers are usually more candid about a benchmark's blind spots than the authors themselves.
3. **Score:** 0–5 according to the rubric's calibrated anchor. We focus the write-up on the **weakest** dimensions; for the remaining dimensions we record a brief evaluation rather than a full three-part argument.

### Global calibration pass

After all benchmark rows were independently scored, a global comparison pass was applied across the 103-benchmark corpus to:

- align scores on similar benchmarks (so that, e.g., **CrowS-Pairs** and **StereoSet** receive comparable Construct-clarity scores when their gaps are of similar severity),
- calibrate each rubric's anchors against the actual score distribution observed in the corpus (anchors that produced no 5-score instances were rewritten so that the 5-score requirement is achievable but discriminating),
- back-fill the calibrated anchors into `rubrics_14_anchors.csv`.

### Rubric calibration log (`rubrics_14_anchors.csv`)

The published rubric anchors are the **v2 calibrated** version. Each row's **Calibration source** column lists the surveys and benchmarks used to calibrate that rubric. Calibration combined the original 0 / 1–2 / 3–4 / 5 anchors with the *Calibrated threshold* column (concrete benchmark anchors), the *Revision suggestions* column (gap-finding for the original anchors), and the *Rubric v2 standards* drafted against the survey corpus. These four sources are now collapsed into the four anchor cells; the calibration audit trail is summarised in the *Calibration source* column.

### Toolbox consolidation (`toolbox_master.csv` + dimension / rubric views)

The previous 48-row toolbox sheet was a mixture of (a) real repair tools and (b) problem-type section headers. After consolidation, **20 canonical tools** remain. Each was passed through Qwen Max with the full 104-benchmark master as context to:

1. Identify which benchmarks in the master corpus **actually embody this tool** (not just token-match the name), with an evidence quote;
2. Map the tool to the subset of the 5 policy-grounded dimensions in which it repairs a recurring failure;
3. Map the tool to the subset of the 14 rubrics on which it lifts the score.

When no master benchmark embodies a tool, the survey-and-methodology reference (BetterBench, AI RMF, Model Cards, Datasheets, CheckList, HELM, etc.) is recorded instead, and the entry is flagged as "no master instance — see survey refs". This preserves the gap-driven character of the workbox while making the master-table grounding explicit.

## Reproducing the artefacts

The translation, calibration, and enrichment scripts are intentionally **not** committed to this repository — they require a DashScope (Qwen) key and produce stable outputs that are already version-controlled here. If you need to regenerate after the master xlsx is updated, the procedure is:

1. translate Chinese cells (Qwen Plus, ~5 minutes for the whole workbook),
2. calibrate the rubric anchors (Qwen Plus, 14 rubrics × ~10 seconds each),
3. enrich the 20 tools with bench / dim / rubric mappings (Qwen Max, ~7 minutes),
4. regenerate the xlsx and 104 markdown cards from the resulting CSVs.

## Provenance

- Master xlsx: `workbook/heart_toolkit.xlsx`
- Survey foundation: `datasets/sources.md` *(Survey papers consulted)*
- Per-benchmark URLs: `datasets/sources.md` *(104-entry index)*
- Per-benchmark cards: [`benchmarks/index.md`](benchmarks/index.md)
