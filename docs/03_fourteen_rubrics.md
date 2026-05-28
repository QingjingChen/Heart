# 03 — The 14 Audit Rubrics

The HEART meta-review applies the same **14 rubrics** to every one of the
103 surveyed papers. Each rubric has a 0–5 anchor scale; each anchor is
described by **observable evidence in the benchmark paper or dataset
documentation** (not a subjective impression). At least four experts
cross-check every score and resolve disagreements by returning to traceable
textual evidence.

The 14 rubrics are organised in three layers.

## Layer 1 — Content validity (5 rubrics)

| # | Rubric | What it asks |
|---|---|---|
| 1 | **Construct clarity** | What exactly does this benchmark claim to measure, and are its boundaries / sub-dimensions / exclusions stated? |
| 2 | **Normative grounding** | Where does the ethical authority come from — law, policy, ethics theory, professional norms, community evidence, or crowd intuition? |
| 3 | **Source provenance & evidence fitness** | Are sources traceable? Are biases and gaps disclosed? Does the source actually fit the construct being tested? |
| 4 | **Context & stakeholder coverage** | Are roles, jurisdictions, affected parties, purpose, and information flow specified? |
| 5 | **Real-world harm linkage** | Does the benchmark connect its items to actual harm pathways, or only to topic labels? |

## Layer 2 — Evaluation design (5 rubrics)

| # | Rubric | What it asks |
|---|---|---|
| 6 | **Scenario validity** | Are scenarios situated and realistic enough that judgement is non-trivial? |
| 7 | **Task-format fit** | Does the task format (MCQ, open generation, multi-turn, tool use) match the construct? |
| 8 | **Ground truth & disagreement design** | Are contested cases forced to a single answer, or do labels accommodate legitimate disagreement / insufficient evidence? |
| 9 | **Metric validity** | Does the metric (accuracy, ASR, refusal rate, factuality) actually support the ethical claim, or is it a proxy? |
| 10 | **Evaluator reliability** | Is the evaluator (human, classifier, LLM-as-judge) calibrated and audited? |

## Layer 3 — Governance reliability (4 rubrics)

| #  | Rubric | What it asks |
|---|---|---|
| 11 | **Data & annotation QA** | What annotation protocols, IAA reporting, and quality controls were used? |
| 12 | **Robustness against gaming & contamination** | Hidden / refreshed subsets? Canaries? Contamination checks? |
| 13 | **Documentation & reproducibility** | Datasheet / benchmark card? Versioning? Reproducible scoring? |
| 14 | **Maintenance & update governance** | Is there a refresh cadence, retirement trigger, or change log? |

## 0–5 anchor example (Construct clarity)

| Score | Anchor |
|---|---|
| 0 | No construct stated, only broad labels (`ethics` / `safety` / `fairness`) |
| 1–2 | Topic label or rough definition only; no sub-dimensions; no task linkage |
| 3 | Construct + some sub-dimensions defined and mapped to data / task / metric |
| 4 | Construct + sub-dimensions + partial exclusion scope + known limits |
| 5 | Construct + boundaries + sub-dimensions + exclusion scope + complete task / metric / claim chain |

Full anchor tables for **all 14 rubrics** are in
[`../workbook/exports/rubrics_14_anchors.csv`](../workbook/exports/rubrics_14_anchors.csv).
The same file records, for each rubric, the **current score distribution
across the 103 reviewed papers** — for example:

> Construct clarity: 1 pt × 3 papers; 2 pt × 16; 3 pt × 39; 4 pt × 39; 5 pt × 6 (n = 103)

This distribution is what lets HEART avoid certifying any individual
benchmark as "good enough." Even on the most generous rubric, only a single-digit
number of the 103 reviewed papers reach a 5; that is the signal that the
borrowing-and-repair stance — not the leaderboard stance — is the right one.

## How the rubrics interact with the workbox

A **missing or weak** rubric is what triggers a specific repair tool in the
[`HEART Workbox`](04_workbox_six_tools.md):

| If this rubric is weak | Use this tool |
|---|---|
| Construct clarity / Normative grounding | Claim–Construct Mapper; Normative Source Ledger |
| Source provenance / Context & stakeholder | Scenario & Stakeholder Expander |
| Ground truth & disagreement | Disagreement & Ground-Truth Protocol |
| Metric validity / Evaluator reliability | Metric & Failure-Mode Reporter |
| Robustness / Documentation / Maintenance | Lifecycle & Contamination Guard |
