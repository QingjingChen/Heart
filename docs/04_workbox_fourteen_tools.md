# 04 — The HEART Workbox: 14 Generic Repair Tools + 103 Specific Sub-tools

The HEART Workbox is a **two-layer** repair toolbox for adapting existing
benchmarks into stronger ethics evaluations. The same structure powers the
interactive [`Revision Toolkit`](../docs/interactive/tools.html) tab and the
master codebook.

| Layer | Live tab | Count | What's in it |
|:---|:---|:---:|:---|
| **Generic repair tools** | [Generic Repair Tools](https://qingjingchen.github.io/Heart/interactive/tools.html) | 14 | Canonical, reusable repair operations (T01–T14) organised by rubric layer |
| **Specific repair sub-tools** | [Specific Repair Sub-tools](https://qingjingchen.github.io/Heart/interactive/benches.html) | 103 | Each audited benchmark, treated as a bench-specific sub-tool bound to a generic parent |
| **Gap → Tool workflow** | [Gap → Tool Workflow](https://qingjingchen.github.io/Heart/interactive/rubric_matrix.html) | 14×14 | Diagnosis-to-tool prescription matrix: when a benchmark fails rubric R*y*, which tool fixes it |

Underlying tables live in `codebook/heart_codebook.xlsx`; the per-tool /
per-benchmark / per-rubric records mirror to the JSON files under
[`./interactive/data/`](./interactive/data/).

---

## The 14 generic tools, by rubric layer

### Content Validity — what the benchmark claims to measure

| Tool | Name | Core practice |
|:---|:---|:---|
| **T01** | Claim-Construct & Protected-Interest Mapper | Rewrite broad ethical claims as `construct → sub-construct → task → metric → supported claim → unsupported claim`. Tie each construct to the protected interest it serves. |
| **T02** | Normative Source & Decision-Boundary Ledger | Separate labels by source type (law, policy, professional ethics, expert judgement, community evidence, descriptive preference, contestable moral claim). Mark red lines, consensus, contested cases, and conditions for expert escalation. |
| **T03** | Scenario-Stakeholder-Information-Flow Template | Add roles, affected parties, third parties, purpose, information flow, consent, jurisdiction, available evidence, and harm pathway as item-level columns — not appendix prose. |
| **T05** | Cultural & Cross-Lingual Adaptation Protocol | Replace identity axes, stereotype anchors, institutional context, and language cues when porting to a new culture/jurisdiction. Verify with local norm sources or community evidence. |
| **T10** | Evidence & Claim Verification Pipeline | Make source attribution auditable: each tool / label / claim carries `source_name · source_type · contribution_type · evidence_strength · verification_status · overclaim_risk`. |

### Evaluation Design — how claims become items + scores

| Tool | Name | Core practice |
|:---|:---|:---|
| **T04** | Risk-Tier & Hazard Taxonomy | Stratify sensitive items by severity / urgency / reversibility / operationality / vulnerability / proximity / domain-sensitivity instead of one-size-fits-all "safe vs. unsafe". |
| **T06** | Contrast-Set Builder | Build minimal-pair variants that isolate one variable at a time: attribute / counterfactual; ambiguous vs. disambiguated; safe-but-sensitive vs. genuinely unsafe. |
| **T07** | Behavioral Coverage Matrix | Lay out the construct × scenario-type × subgroup grid; identify and patch the empty cells before publishing. |
| **T09** | Agent & Workflow Simulation | Score on trajectory (what the agent reads / writes / calls / withholds / escalates), not only on final answer. Define environment, tools, permissions, expected safe trajectory, failure modes. |
| **T11** | Multi-Metric Failure-Mode Profile | Report per-construct, per-risk-tier, per-subgroup, per-scenario-type, near-miss, severe-failure, harmful-compliance, and over-refusal rates — not just a single headline. |
| **T12** | Rubric-Based & Multi-Judge Evaluation Protocol | Score open responses with explicit 0–N rubric anchors, multi-rater aggregation, low-agreement re-review, judge bias checks, and gold-anchor calibration. |

### Governance Reliability — how the benchmark stays auditable and current

| Tool | Name | Core practice |
|:---|:---|:---|
| **T08** | Multi-Turn & Adversarial Red-Team Protocol | Test boundary-holding across multi-turn trajectories: benign opening → role framing → pressure → escalation → recovery. Score per-turn, not just the final reply. |
| **T13** | Reproducible Evaluation & Benchmark Card Package | Ship a complete bench card: dataset card, model card, schema, evaluation script, prompt version, judge version, metric definition, license, intended use, out-of-scope use, limitations. |
| **T14** | Lifecycle, Hidden-Split & Contamination Governance | Maintain a hidden test set, canary items, contamination checks, refreshed subsets, submission limits, leaderboard-anomaly review, version log, retirement triggers, and update cadence. |

---

## The 103 specific sub-tools

Every benchmark in the meta-review is treated as a **specific repair
sub-tool**: it inherits the generic tool's mechanism but adds bench-level
specifics (the exact slots / labels / contrast structure / annotation
protocol the benchmark used). The full catalogue lives in:

- 🌐 Interactive view (sortable, filterable, with adaptation guide + example per bench): [Specific Repair Sub-tools](https://qingjingchen.github.io/Heart/interactive/benches.html)
- 📚 Markdown catalogue: [`../datasets/README.md`](../datasets/README.md)
- 🔗 Per-bench paper / code / dataset-mirror index: [`../datasets/sources.md`](../datasets/sources.md)
- 📊 Raw CSV: [`../codebook/benchmarks.csv`](../codebook/benchmarks.csv)

Click any benchmark on the site to see its bench-specific adaptation guide
(6-section plain-language bullets) and a concrete adapted example.

---

## How to pick a tool

Match the **weak rubric** in your audit to its default generic tool. The
full matrix (with secondary tools per domain) is the live
[Gap → Tool Workflow](https://qingjingchen.github.io/Heart/interactive/rubric_matrix.html);
the headline mapping:

| Weak rubric | Default generic tool(s) |
|:---|:---|
| **R1** Construct clarity | T01 · T11 · T10 |
| **R2** Normative grounding | T02 · T12 · T04 · T03 |
| **R3** Source provenance & evidence fitness | T10 · T05 · T13 |
| **R4** Context & stakeholder coverage | T03 · T04 · T02 |
| **R5** Real-world harm linkage | T01 · T04 · T11 · T03 |
| **R6** Scenario validity | T03 · T04 · T09 |
| **R7** Task-format fit | T06 · T08 · T09 |
| **R8** Ground truth & disagreement design | T12 · T02 · T11 |
| **R9** Metric validity | T11 · T09 · T03 · T04 |
| **R10** Evaluator reliability | T14 · T13 |
| **R11** Data & annotation QA | T13 |
| **R12** Robustness against gaming & contamination | T14 |
| **R13** Documentation & reproducibility | T13 |
| **R14** Maintenance & update governance | T13 · T04 · T09 |

[`05_guidebook_workflow.md`](05_guidebook_workflow.md) explains the 4-step
workflow for using these tools on a single benchmark.
