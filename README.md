<div align="center">

# ❤️ HEART
### Human-centric Ethical Audit & Revision Toolkit for Benchmarks

[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue.svg)](LICENSE-code)
[![Status](https://img.shields.io/badge/Status-Pre--release-orange.svg)](docs/06_resource_availability.md)
[![Interactive Site](https://img.shields.io/badge/Live-Interactive%20Site-2C5282.svg)](https://qingjingchen.github.io/Heart/interactive/)

**An interactive audit-and-repair toolkit for existing AI-ethics benchmarks.**

[🌐 Live site](https://qingjingchen.github.io/Heart/interactive/) ·
[📖 Docs](#-documentation-stack) ·
[📊 Workbook](workbook/) ·
[📚 Bench corpus](datasets/sources.md) ·
[🤝 Contribute](.github/ISSUE_TEMPLATE/)

</div>

---

## 🧭 Navigate this repo

| 🎯 [**Diagnostic rubrics**](docs/03_fourteen_rubrics.md) | 🛠 [**Repair tools**](docs/04_workbox_fourteen_tools.md) | 📚 [**Bench corpus**](datasets/sources.md) | 🌐 [**Interactive site**](docs/interactive/) |
|:---:|:---:|:---:|:---:|
| 14 audit rubrics in 3 layers | 14 generic tools + 103 specific sub-tools | 103 audited benchmarks across 5 dimensions | Click-through audit + repair workflow |

---

## What HEART is

HEART treats each existing AI-ethics benchmark as a **bundle of reusable tools**
(dataset patterns, task formats, metrics, evaluator protocols, governance practices)
that can be picked apart and re-applied. It bundles together:

- 📑 a meta-review of **103 benchmarks + 16 policy/governance sources** along **5 ethical dimensions**
- 🩺 a **14-rubric** diagnostic codebook with v2 calibrated anchors, expert-validated across all 103 benchmarks
- 🧰 a **two-layer workbox** of repair tools: 14 **generic** tools (the canonical workbox) + 103 **specific** sub-tools (one per audited bench)
- 📖 a 4-step **audit → diagnosis → tool prescription → revision** guidebook
- 🌐 an **interactive site** that walks through the full workflow in the browser

> Goal: help benchmark authors and reviewers move from "this benchmark scored X" to **"this benchmark fails rubric R*y* on item I, use repair tool T*x* to fix it."**

---

## 🚀 Quick start

| Want to … | Go to |
|:---|:---|
| 🌐 Click through the audit workflow in your browser | [Live interactive site](https://qingjingchen.github.io/Heart/interactive/) |
| 🩺 Audit one benchmark by hand | [`docs/05_guidebook_workflow.md`](docs/05_guidebook_workflow.md) (4-step workflow) |
| 📊 Get the raw data | [`workbook/exports/benchmarks_103_tool_distribution.csv`](workbook/exports/) |
| 🔗 Look up a benchmark's paper / code / dataset mirror | [`datasets/sources.md`](datasets/sources.md) |
| 📚 Cite HEART | [`CITATION.cff`](CITATION.cff) (placeholder; DOI at release) |

---

## 📖 Documentation stack

Each doc mirrors one tab (or stage) of the interactive site, so the workbook
and the site stay in lock-step.

| 📄 Doc | 🌐 Site tab | What it covers |
|:---|:---|:---|
| 🧩 [`01_problem.md`](docs/01_problem.md) | — | Motivation: why benchmark-as-leaderboard fails for ethics |
| 🌐 [`02_five_dimensions.md`](docs/02_five_dimensions.md) | **A.** [Policy & Corpus](https://qingjingchen.github.io/Heart/interactive/dimensions.html) | 5 ethical dimensions × 16 policy/governance sources |
| 📚 [`datasets/sources.md`](datasets/sources.md) + [`datasets/README.md`](datasets/README.md) | **A. (sub)** [103 Audited Benches](https://qingjingchen.github.io/Heart/interactive/benches.html) | Per-bench paper / code / dataset-mirror catalogue |
| 🩺 [`03_fourteen_rubrics.md`](docs/03_fourteen_rubrics.md) | **B.** [Diagnostic Rubrics](https://qingjingchen.github.io/Heart/interactive/rubrics.html) | 14 audit rubrics × 3 layers, 0–5 anchors, 103-bench score distributions |
| 🛠 [`04_workbox_fourteen_tools.md`](docs/04_workbox_fourteen_tools.md) | **C.** [Revision Toolkit](https://qingjingchen.github.io/Heart/interactive/tools.html) | 14 generic repair tools + 103 specific sub-tools + Gap → Tool workflow |
| 📖 [`05_guidebook_workflow.md`](docs/05_guidebook_workflow.md) | **D.** [Revision Examples](https://qingjingchen.github.io/Heart/interactive/mini_cases.html) | 4-step `diagnose → prescribe → repair → re-claim` workflow + worked cases |
| 📦 [`06_resource_availability.md`](docs/06_resource_availability.md) | — | FAIR statement, mirror locations, license, citation |

---

## 🎯 The 5 ethical dimensions

| Dimension | Benchmarkable scope |
|:---|:---|
| 👤 **Human-Centered** | Moral reasoning, empathy, well-being, professional boundaries, human agency |
| ⚖️ **Fairness & Inclusiveness** | Stereotyping, disparate treatment, representational harm, cultural coverage |
| 🛡️ **Safety & Reliability** | Dangerous assistance, jailbreak resistance, over-refusal, misuse, recovery |
| ⚙️ **Trustworthiness & Controllability** | Factuality, evidence support, sycophancy, temporal validity, rule-constrained reasoning |
| 🔒 **Privacy Protection** | Memorization, PII leakage, inferential disclosure, contextual integrity |

Cross-walked to 16 policy/governance sources in [`docs/02_five_dimensions.md`](docs/02_five_dimensions.md).

---

## 🛠 The two-layer repair workbox

### 14 generic repair tools (the public canonical)

| Layer | Generic tools (T01–T14) |
|:---|:---|
| **Content Validity** | T01 Claim-Construct Mapper · T02 Normative Source Ledger · T03 Scenario-Stakeholder-Info-Flow · T05 Cultural & Cross-Lingual · T10 Evidence & Claim Verification |
| **Evaluation Design** | T04 Risk-Tier & Hazard · T06 Contrast-Set Builder · T07 Behavioral Coverage Matrix · T09 Agent & Workflow Sim · T11 Multi-Metric Failure-Mode · T12 Rubric-Based & Multi-Judge |
| **Governance Reliability** | T08 Multi-Turn & Adversarial Red-Team · T13 Reproducible Eval & Card · T14 Lifecycle, Hidden-Split & Contamination |

### 103 specific sub-tools (one per audited bench)

Each audited benchmark is treated as a **specific repair sub-tool** bound to one or more generic tools. Browse the catalogue in [`datasets/sources.md`](datasets/sources.md) or open the interactive [`Specific Repair Sub-tools`](https://qingjingchen.github.io/Heart/interactive/benches.html) tab.

---

## 📂 Repository structure

```
.
├── README.md                            ← you are here
├── CITATION.cff                         ← citation metadata
├── LICENSE                              ← CC-BY-4.0 (docs + workbook + rubrics)
├── LICENSE-code                         ← MIT (scripts, exporters)
│
├── docs/                                📖 documentation stack
│   ├── 01_problem.md                    ← motivation
│   ├── 02_five_dimensions.md            ← 5 dimensions  (↔ site tab A)
│   ├── 03_fourteen_rubrics.md           ← 14 rubrics    (↔ site tab B)
│   ├── 04_workbox_fourteen_tools.md     ← 14 + 103 tools (↔ site tab C)
│   ├── 05_guidebook_workflow.md         ← workflow     (↔ site tab D)
│   ├── 06_resource_availability.md      ← release statement
│   └── interactive/                     🌐 GitHub-Pages-served interactive site
│
├── workbook/                            📊 master workbook (7 sheets)
│   ├── heart_toolkit.xlsx
│   └── exports/                         ← CSV / JSON exports
│
├── datasets/                            📚 bench corpus  (↔ site tab A sub-page)
│   ├── README.md                        ← catalogue of 103 benches by dimension
│   └── sources.md                       ← per-bench paper / code / Drive URLs
│
└── paper/                               📝 companion paper (added at release time)
```

---

## 📜 License

- 📐 **Code** (scripts, exporters, interactive-site JS/CSS): [MIT](LICENSE-code)
- 📖 **Workbook, documentation, dataset index, rubric anchors, interactive-site copy**: [CC-BY-4.0](LICENSE)

Source datasets indexed in [`datasets/`](datasets/) are governed by their original
licenses — see each upstream repository / paper.

---

## 🤝 Contributing & contact

Open a GitHub issue for questions, corrections, or new benchmark suggestions. See [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) for templates.

---

<div align="center">

Made with ❤️ — pre-release; expect minor breakage as the workbook stabilises.

</div>
