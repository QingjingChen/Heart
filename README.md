# HEART: Human-centric Ethical Assessment & Revision Toolkit for Benchmarks

> A policy-grounded **resource** for revising AI-ethics benchmarks — not another leaderboard.

HEART treats each existing AI-ethics benchmark as a **bundle of reusable tools**
(dataset patterns, task formats, metrics, evaluator protocols, governance practices)
rather than as a competing "gold standard." It bundles together:

- a meta-review of **103 survey & benchmark papers** along **5 policy-grounded dimensions**
- a **14-rubric** diagnostic workbook with 0–5 anchors, expert-validated across all 103 papers
- a **48-entry tool-indexed workbox** of repair operations (the **HEART Workbox**)
- an index of **~72 source datasets** organised by the 5 dimensions
- a companion **Web Demo** that walks a user through diagnosis → tool selection → revision plan

---

## What's in this repository

| Path | What it is |
|---|---|
| [`docs/01_problem.md`](docs/01_problem.md) | Problem statement: why benchmark-as-leaderboard fails for ethics |
| [`docs/02_five_dimensions.md`](docs/02_five_dimensions.md) | Policy → 5 ethical dimensions mapping (UNESCO, OECD, EU AI Act, NIST AI RMF, GDPR, PIPL, internal tech-ethics files) |
| [`docs/03_fourteen_rubrics.md`](docs/03_fourteen_rubrics.md) | The 14 audit rubrics (content validity / evaluation design / governance reliability) with 0–5 anchors and current 103-paper score distributions |
| [`docs/04_workbox_six_tools.md`](docs/04_workbox_six_tools.md) | The 6 repair tools that form the HEART Workbox |
| [`docs/05_guidebook_workflow.md`](docs/05_guidebook_workflow.md) | 4-step guidebook for adapting a benchmark using the workbox |
| [`docs/06_resource_availability.md`](docs/06_resource_availability.md) | FAIR statement, mirror locations, citation, license |
| [`workbook/heart_toolkit.xlsx`](workbook/heart_toolkit.xlsx) | Master workbook (7 sheets) — the source of truth |
| [`workbook/exports/`](workbook/exports/) | CSV exports of every workbook sheet for tool-agnostic access |
| [`datasets/README.md`](datasets/README.md) | Full catalogue of 103 benchmarks (per-dimension tables) with representative tool, why-it-improves rationale, adaptation example, and limits |
| [`datasets/sources.md`](datasets/sources.md) | Per-benchmark **paper / code / Drive dataset** URL index (one row per benchmark) |
| [`demo/README.md`](demo/README.md) | Pointer to the [Web Demo source repository](https://github.com/QingjingChen/heart_web_demo_pub) and run instructions |
| [`paper/README.md`](paper/README.md) | Companion paper (PDF + bibtex) — added at release time |

## The 5 dimensions, at a glance

| Dimension | Benchmarkable scope |
|---|---|
| **Human-Centered** | Moral reasoning, empathy, well-being, professional boundaries, human agency |
| **Fairness & Inclusiveness** | Stereotyping, disparate treatment, representational harm, cultural coverage |
| **Safety & Reliability** | Dangerous assistance, jailbreak resistance, over-refusal, misuse, recovery |
| **Trustworthiness & Controllability** | Factuality, evidence support, sycophancy, temporal validity, rule-constrained reasoning |
| **Privacy Protection** | Memorization, PII leakage, inferential disclosure, contextual integrity |

Full policy-to-dimension proof in [`docs/02_five_dimensions.md`](docs/02_five_dimensions.md).

## The 6 repair tools, at a glance

| Tool | Problem repaired |
|---|---|
| **Claim–Construct Mapper** | Broad claims (`ethical`/`safe`/`trustworthy`) exceed the task |
| **Normative Source Ledger** | Labels rely on crowd agreement without clear normative authority |
| **Scenario & Stakeholder Expander** | Items mention an ethical topic but omit the situation that makes judgment valid |
| **Disagreement & Ground-Truth Protocol** | Contested ethical cases forced into a single answer key |
| **Metric & Failure-Mode Reporter** | Accuracy / refusal-rate / ASR becomes a proxy for the whole ethical claim |
| **Lifecycle & Contamination Guard** | Static public sets become stale, memorized, or easy to game |

Full descriptions in [`docs/04_workbox_six_tools.md`](docs/04_workbox_six_tools.md).

## Quick start

**Just want to audit one benchmark?** Open [`docs/05_guidebook_workflow.md`](docs/05_guidebook_workflow.md)
and follow the 4-step workflow. The Web Demo at
[`demo/`](demo/) automates the same flow.

**Want the raw data?** Every benchmark in the meta-review is a row in
[`workbook/exports/benchmarks_104_tool_distribution.csv`](workbook/exports/benchmarks_104_tool_distribution.csv).
Source datasets are indexed in [`datasets/README.md`](datasets/README.md).

## How to cite

A companion paper is in preparation; bibtex and DOI will be added at release time.
See [`CITATION.cff`](CITATION.cff) for the placeholder metadata.

## License

- **Code** (scripts, demo backend, exporters): [MIT](LICENSE-code)
- **Workbook, documentation, dataset index, rubric anchors**: [CC-BY-4.0](LICENSE)

Source datasets indexed in [`datasets/`](datasets/) are governed by their original
licenses — see each upstream repository.

## Contact

Open a GitHub issue for questions or contributions; see
[`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/).
