# `heart_index.json` — schema reference

`heart_index.json` is the compiled, machine-readable view of the HEART
workbook. It is generated from the same `workbook/exports/*.csv` files
that live in this folder, plus a small Qwen-Plus enrichment pass for
fields that the CSVs don't carry directly (rubric `weak_triggers`, tool
`output_fields`, and domain templates).

The demo backend (`heart_web_demo_pub/heart_backend.py`) loads this
file once at startup and uses it as a **retrieval-and-constraint
index**: API calls extract benchmark profiles from the user upload, and
the index supplies the diagnosis rules, the recommended tools, the
output-field schema, and the domain templates that the LLM is allowed
to fill. Every recommendation produced by the demo carries a
`source: heart_index.<path>` pointer back into this file.

## Top-level structure

```jsonc
{
  "version": "1.0",
  "generated_at": "YYYY-MM-DD",
  "source": "Heart/workbook/exports/* (regenerated from workbook/heart_toolkit.xlsx)",
  "description": "...",

  "rubrics": { /* 14 rubric definitions + calibrated anchors + weak triggers */ },
  "tools":   { /* 20 consolidated repair tools + output-field schemas */ },

  "indices": {
    "rubric_to_tools":     { /* rubric_id -> [tool_id, ...] */ },
    "dimension_to_tools":  { /* dimension -> [tool_id, ...] */ },
    "trigger_to_rubric":   { /* lowercased trigger pattern -> [{rubric_id, score, rationale}] */ }
  },

  "domain_templates": { /* 3 target-domain templates */ },
  "metrics":          { /* 6 LLM-free quality metrics */ },
  "diagnosis_rules":  [ /* derived rule list for the rule-based scorer */ ]
}
```

## `rubrics[<rubric_id>]`

| Field | Type | Source | Description |
|---|---|---|---|
| `id` | snake_case | derived | Stable id; e.g., `construct_clarity`. |
| `name` | string | `rubrics_14_anchors.csv` col 0 | Human-readable name. |
| `definition` | string | col 1 | One-line definition. |
| `old_mapping` | string | col 2 | v1 rubric this descends from. |
| `key_question` | string | col 3 | The diagnostic question. |
| `calibrated_anchors` | object | cols 4–7 | `{0, 1_2, 3_4, 5}` — v2-calibrated anchor with benchmark examples. |
| `score_distribution` | string | col 8 | Score distribution across the 104 master benchmarks. |
| `good_vs_bad_bench_types` | string | col 9 | Survey-based examples of good and bad benchmarks. |
| `calibration_source` | string | col 10 | Surveys/benches used to set the anchors. |
| `weak_triggers` | list | **Qwen Plus** | 3–5 short patterns that flag the benchmark as low on this rubric without an LLM call. |

### `weak_triggers[]`

| Field | Type | Description |
|---|---|---|
| `pattern` | string (1–6 words) | Literal or regex-like phrase to match in a parsed benchmark profile. |
| `matches_score` | `"0"` or `"1-2"` | Which low-bucket the pattern indicates. |
| `rationale` | string | One-sentence justification. |

## `tools[<tool_id>]`

| Field | Type | Source | Description |
|---|---|---|---|
| `id` | snake_case | derived | Stable id; e.g., `normative_source_ledger`. |
| `name` | string | `toolbox_master.csv` col 0 | Display name. |
| `canonical_name` | string | col 1 | Canonical short name. |
| `core_practice` | string | col 2 | What the tool actually does. |
| `problem_fixed` | string | col 3 | The diagnostic problem repaired. |
| `bench_instances` | string | col 4 | Master-table benchmark instances with one-line evidence. |
| `survey_refs` | string | col 5 | Methodology surveys grounding the tool. |
| `mini_case` | string | col 6 | One short adaptation example. |
| `rubrics_improved` | list | `tools_by_rubric.csv` | Per-rubric entries: `{rubric_id, rubric_name, how, bench_ref, survey_ref}`. |
| `dimensions_applicable` | list | `tools_by_dimension.csv` | Per-dimension entries: `{dimension, why, bench_ref, survey_ref}`. |
| `output_fields` | list | **Qwen Plus** | Machine-friendly fields a revised item should carry after the tool is applied (see below). |

### `output_fields[]`

| Field | Type | Description |
|---|---|---|
| `field` | snake_case | Field name (e.g., `expected_action`, `failure_mode`, `normative_anchor`). |
| `type` | enum | `string` / `enum` / `list` / `number` / `bool`. |
| `required` | bool | Whether the field is required for the tool's repair to count as applied. |
| `description` | string | What the field captures. |
| `example_values` | list | Concrete examples (used by the demo to populate dropdowns). |

## `indices.*`

| Index | Key | Value | Purpose |
|---|---|---|---|
| `rubric_to_tools` | `rubric_id` | `[tool_id, …]` | Given a low rubric score, list candidate repair tools (preserves the ordering used in `tools_by_rubric.csv`). |
| `dimension_to_tools` | dimension name | `[tool_id, …]` | Given the user's target dimension, list candidate tools. |
| `trigger_to_rubric` | lowercased pattern | `[{rubric_id, matches_score, rationale}, …]` | Used by the rule-based scorer for keyword-grep diagnosis without LLM calls. |

## `domain_templates[<domain_id>]`

Authored from master adaptation examples in the corresponding domain. The 3 shipped templates are `medical`, `finance`, `education`.

| Field | Type | Description |
|---|---|---|
| `domain_id` | snake_case | Stable id. |
| `name` | string | Human-readable name. |
| `purpose` | string | One-sentence statement of when to pick this template. |
| `required_fields` | list | Per-field entries: `{field, type, required, values, description}`. |
| `normative_anchors` | list | Per-anchor entries: `{id, citation, scope}`. |
| `failure_modes` | list | Per-mode entries: `{id, description}`. |
| `action_labels` | list | Valid values for the revised item's `expected_action` field. |
| `grounding_bench_refs` | list | Benchmark names from the master corpus that grounded the template. |

## `metrics[<metric_id>]`

Six LLM-free quality metrics that the backend can compute on a list of revised items + a domain template. Used by `POST /api/metrics`.

| Metric | Formula |
|---|---|
| `context_variable_coverage` | filled required fields ÷ total required fields |
| `normative_anchor_coverage` | items with a cited anchor ÷ total items |
| `action_label_diversity` | count of distinct `expected_action` values |
| `counterfactual_pair_coverage` | complete `pair_id` pairs ÷ target pairs |
| `failure_mode_coverage` | exercised `failure_mode` values ÷ template `failure_modes` |
| `traceability_coverage` | items carrying a `source` pointer ÷ total items |

## `diagnosis_rules[]`

Each entry is a derived `(rubric, trigger pattern) → recommended tools` rule. The demo uses these for the **rule-based** diagnosis pass; the LLM is only invoked afterwards to *fill* the recommended tool's `output_fields` for each per-sample case.

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable id of the form `rule_<rubric>_<pattern_slug>`. |
| `rubric_id` | string | The rubric this rule scores. |
| `trigger_pattern` | string | The literal pattern (see `weak_triggers.pattern`). |
| `expected_score` | `"0"` or `"1-2"` | The score this pattern triggers. |
| `rationale` | string | One-sentence justification. |
| `recommended_tools` | list of `tool_id` | Top-5 candidate repair tools (from `rubric_to_tools`). |

## Provenance contract

Every record the demo backend emits MUST carry a `source` pointer with one of these shapes:

```json
{"source": "heart_index.rubrics.metric_validity"}
{"source": "heart_index.tools.metric_failure_mode_reporter"}
{"source": "heart_index.diagnosis_rules.rule_metric_validity_rta_only"}
{"source": "heart_index.domain_templates.medical"}
```

The frontend can then deep-link the user back to the corresponding workbook row.

## Regeneration

To rebuild `heart_index.json` after the master xlsx is updated:

1. Regenerate the 4 CSVs and the calibrated rubric anchors via the translation/calibration pipeline.
2. Run the Qwen-Plus enrichment for `weak_triggers`, `output_fields`, and any new `domain_templates` (≈ 3 minutes of API time).
3. Run the assembly script.

The scripts are deliberately not committed; they require a DashScope (Qwen) key in `~/.dashscope_key`.
