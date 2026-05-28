# 04 — The HEART Workbox: Six Repair Tools

The HEART Workbox is a set of **six repair operations** for adapting existing
benchmark components into a more defensible ethics evaluation. The full
48-entry tool index (with `core practice / problem repaired / rubric
improved / applicable ethics scenarios / source paper / limitations /
mini-case`) lives in
[`../workbook/exports/toolbox_48_tools.csv`](../workbook/exports/toolbox_48_tools.csv).

The six tools below are the **clustered output** of that 48-entry index —
each tool groups together related practices that target one family of
benchmark weakness.

---

## Tool 1 — Claim–Construct Mapper

**Problem repaired.** Broad claims such as "ethical," "safe," or
"trustworthy" exceed what a single task can support.

**Revision operation.** Rewrite the claim as a **construct → task → metric**
chain. State the boundaries, exclusions, required evidence, and out-of-scope
uses.

**Reference practices.** FActScore (atomic factual decomposition);
XSTest (over-refusal as a separate construct from refusal); PrivaCI-Bench
(claim scoped to contextual-integrity satisfaction).

---

## Tool 2 — Normative Source Ledger

**Problem repaired.** Labels rely on crowd agreement, value keywords, or
platform data without a clear normative authority.

**Revision operation.** Separate the label sources into: **law, policy,
expert judgement, community evidence, descriptive preference,** and
**contestable moral claims**. Mark red lines, consensus, uncertain cases, and
locally varying cases. Annotate conflicts between sources rather than
collapsing them.

**Reference practices.** Hancox-Li & Blili-Hamelin's critique of ETHICS;
LegalBench (law as the source); ConfAIde / PrivaCI-Bench (contextual
integrity as the source).

---

## Tool 3 — Scenario & Stakeholder Expander

**Problem repaired.** Items mention an ethical topic but omit the situation
that makes ethical judgement non-trivial. The model "answers" without ever
being placed in a position where the answer is decidable.

**Revision operation.** Add **roles, affected parties, jurisdiction,
purpose, information flow, available evidence, interaction history, and
harm pathway**. Each addition is a column in the dataset, not a comment in
the appendix.

**Reference practices.** BBQ / CBBQ (ambiguous vs. disambiguated scenario
contrast); WinoQueer (community-in-the-loop harm definition);
ConfAIde (five-tuple contextual-integrity scenario).

---

## Tool 4 — Disagreement & Ground-Truth Protocol

**Problem repaired.** Contested ethical cases are forced into a single
answer key, suppressing legitimate moral disagreement.

**Revision operation.** Split labels into: **prohibited behaviour,
expected behaviour, acceptable disagreement, insufficient evidence,** and
**expert-escalation cases**. The benchmark then reports per-category
performance instead of a single accuracy.

**Reference practices.** Moral-dilemma benchmarks (MoralStories, SCRUPLES,
MoReBench); professional-advice benchmarks where law and ethics diverge.

---

## Tool 5 — Metric & Failure-Mode Reporter

**Problem repaired.** Accuracy, refusal rate, attack success rate (ASR),
toxicity score, or factuality score gets cited as a proxy for the entire
ethical claim.

**Revision operation.** Match each metric to the **specific construct** it
can support. Add **subgroup, scenario-type, uncertainty, over-refusal,
near-miss,** and **failure-mode** reporting. Publish the per-failure-mode
table; do not collapse to a single headline number.

**Reference practices.** FActScore (atomic precision/recall);
HarmBench (per-category breakdown); DecodingTrust (perspective-conditioned
reporting).

---

## Tool 6 — Lifecycle & Contamination Guard

**Problem repaired.** Static public sets become stale, memorised, or easy
to game once they have been indexed by training pipelines.

**Revision operation.** Add **hidden or refreshed subsets, canaries,
contamination checks, version logs, update cadence, retirement triggers,**
and **benchmark-card documentation**. Publish the test set's age and
contamination status alongside any score.

**Reference practices.** FreshQA (temporal refresh); adversarial safety
benchmarks with hidden splits; benchmark cards (Gebru et al.; Hutchinson et al.).

---

## How to pick a tool

Match the workbox tool to the **weak rubric** in your audit:

| Weak rubric | Tool |
|---|---|
| Construct clarity | Tool 1 |
| Normative grounding; Source provenance & evidence fitness | Tool 2 |
| Context & stakeholder coverage; Scenario validity; Real-world harm linkage | Tool 3 |
| Ground truth & disagreement design | Tool 4 |
| Metric validity; Evaluator reliability | Tool 5 |
| Robustness; Documentation; Maintenance | Tool 6 |

[`05_guidebook_workflow.md`](05_guidebook_workflow.md) explains the 4-step
workflow for using these tools on a single benchmark.
