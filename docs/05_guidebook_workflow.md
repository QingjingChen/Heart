# 05 — The Guidebook Workflow (4 steps)

The HEART Guidebook applies the [14 rubrics](03_fourteen_rubrics.md) and the
[6 workbox tools](04_workbox_six_tools.md) to a **single benchmark you want
to adapt**. The same workflow is automated end-to-end in the
[Web Demo](../demo/README.md).

---

## Step 1 — State the claim

Write down the **exact ethical claim** the benchmark currently makes, in one
sentence. Replace any of the following words: `ethical`, `safe`,
`trustworthy`, `fair`, `aligned`. They are too broad to support.

| ❌ Broad claim | ✅ Specific claim |
|---|---|
| "tests fairness" | "tests stereotype reliance under linguistic ambiguity in occupational reasoning" |
| "tests safety" | "tests over-refusal on benign requests phrased to surface-resemble disallowed ones" |
| "tests privacy" | "tests recognition of contextual-integrity violations in agentic email drafting" |

---

## Step 2 — Diagnose with the 14 rubrics

For each of the [14 rubrics](03_fourteen_rubrics.md), pick the 0–5 anchor
that best fits the benchmark you are auditing. Mark each rubric as one of:

- ✅ addressed
- ◐ partially addressed
- ✗ missing or unclear
- — not applicable

The result is a rubric profile. **The ✗ and ◐ rubrics are your revision targets.**

---

## Step 3 — Select tools from the workbox

Match each weak rubric to its repair tool from the
[HEART Workbox](04_workbox_six_tools.md):

| If this rubric came up ✗ or ◐ | Use this tool |
|---|---|
| Construct clarity | Tool 1 — Claim–Construct Mapper |
| Normative grounding / Source provenance | Tool 2 — Normative Source Ledger |
| Context & stakeholder / Scenario validity / Harm linkage | Tool 3 — Scenario & Stakeholder Expander |
| Ground truth & disagreement | Tool 4 — Disagreement & Ground-Truth Protocol |
| Metric validity / Evaluator reliability | Tool 5 — Metric & Failure-Mode Reporter |
| Robustness / Documentation / Maintenance | Tool 6 — Lifecycle & Contamination Guard |

---

## Step 4 — Revise and limit claims

Apply the selected tools. The revised benchmark must document **what it can
and cannot support**. Examples of acceptable scoped claims:

- "Supports: stereotype reliance in single-turn ambiguous occupational
  reasoning, English, US/UK demographics. Does **not** support: real-world
  hiring fairness, multilingual settings, or non-binary identity cases (see
  WinoQueer for the latter)."
- "Supports: contextual-integrity violation rate in agentic Gmail/Slack/Notion
  scenarios under 5 named information-flow norms. Does **not** support:
  jurisdiction-specific GDPR / PIPL compliance."

---

## A worked example

**Benchmark being adapted:** TruthfulQA (Lin et al., 2022).

| Rubric | Anchor | Status |
|---|---|---|
| Construct clarity | 3 — defines "truthfulness" but conflates *not lying* with *not generating false content* | ◐ |
| Normative grounding | 2 — labels are authors' adjudication; no policy / professional standard | ✗ |
| Context & stakeholder coverage | 2 — single-turn QA; no purpose, no audience | ✗ |
| Metric validity | 3 — multiple-choice and generative variants; generative scoring proxied via a separate classifier | ◐ |
| Maintenance governance | 1 — static set since 2022; contamination unaddressed | ✗ |

**Workbox tools applied:**

- **Tool 1** rewrites the construct from "truthful" to "**non-deceptive
  generation on questions where a confidently-stated common misconception
  exists**."
- **Tool 2** adds a **normative source ledger**: misconception classification
  sourced from cited debunking literature, not authors' intuition.
- **Tool 3** adds **purpose** (medical-advice / legal-advice / general-trivia)
  as a scenario axis.
- **Tool 5** replaces the single accuracy headline with: precision on red-line
  misconceptions, abstention rate when authoritative source disagreement is
  present, and over-correction rate on true-but-counter-intuitive claims.
- **Tool 6** introduces a hidden 2026 refresh set canary-tagged for
  contamination tracking.

The output is a **TruthfulQA-style tool** that supports a narrower but
defensible claim — exactly the unit HEART is designed to produce.
