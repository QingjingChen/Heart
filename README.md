<div align="center">

# 💚 HEART
### Human-centric Ethical Assessment & Revision Toolkit for Benchmarks

[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue.svg)](LICENSE-code)
[![Status](https://img.shields.io/badge/Status-Pre--release-orange.svg)](docs/06_resource_availability.md)
[![Interactive Site](https://img.shields.io/badge/Live-Interactive%20Site-2C5282.svg)](https://qingjingchen.github.io/Heart/interactive/)

**A policy-grounded resource for revising AI-ethics benchmarks — not another leaderboard.**

[🌐 Live site](https://qingjingchen.github.io/Heart/interactive/) ·
[📖 Docs](#-documentation-stack) ·
[📊 Workbook](workbook/) ·
[📚 Bench corpus](datasets/sources.md) ·
[🤝 Contribute](.github/ISSUE_TEMPLATE/)

</div>

---

## 🧭 Navigate this repo

| 🎯 [**Diagnostic rubrics**](docs/03_fourteen_rubrics.md) | 🛠 [**Repair tools**](docs/04_workbox_six_tools.md) | 📚 [**Bench corpus**](datasets/sources.md) | 🌐 [**Interactive site**](docs/interactive/) |
|:---:|:---:|:---:|:---:|
| 14 audit rubrics in 3 layers | 14 generic tools + 103 specific sub-tools | 103 audited benchmarks across 5 dimensions | Click-through audit + repair workflow |

---

## What HEART is

HEART treats each existing AI-ethics benchmark as a **bundle of reusable tools**
(dataset patterns, task formats, metrics, evaluator protocols, governance practices)
rather than as a competing "gold standard." It bundles together:

- 📑 a meta-review of **103 benchmarks + 18 policy/governance sources** along **5 policy-grounded dimensions**
- 🩺 a **14-rubric** diagnostic codebook with v2 calibrated anchors, expert-validated across all 103 benchmarks
- 🧰 a **two-layer workbox** of repair tools: 14 **generic** tools (the canonical workbox) + 103 **specific** sub-tools (one per audited bench)
- 📖 a 4-step **audit → diagnosis → tool prescription → revision** guidebook
- 🌐 an **interactive site** that walks through the full workflow in the browser

> Goal: help benchmark authors and reviewers move from "this benchmark scored X" to **"this benchmark fails rubric R*y* on item I, use repair tool T*x* to fix it."**

---

## 🚀 Quick start

| Want to … | Go to |
|:---|:---|
| 🌐 Click through the audit workflow in your browser | [`Live interactive site`](https://qingjingchen.github.io/Heart/interactive/) |
| 🩺 Audit one benchmark by hand | [`docs/05_guidebook_workflow.md`](docs/05_guidebook_workflow.md) (4-step workflow) |
| 📊 Get the raw data | [`workbook/exports/benchmarks_103_tool_distribution.csv`](workbook/exports/) |
| 🔗 Look up a benchmark's paper / code / dataset mirror | [`datasets/sources.md`](datasets/sources.md) |
| 📚 Cite HEART | [`CITATION.cff`](CITATION.cff) (placeholder; DOI at release) |

---

## 📚 Documentation stack

The 6-doc stack reads top-down: problem → constructs → diagnosis → repair → workflow → release.

| 📄 Doc | What it covers |
|:---|:---|
| 🧩 [`01_problem.md`](docs/01_problem.md) | Why benchmark-as-leaderboard fails for ethics |
| 🌐 [`02_five_dimensions.md`](docs/02_five_dimensions.md) | Policy → 5 ethical dimensions mapping (UNESCO, OECD, EU AI Act, NIST RMF, GDPR, PIPL, …) |
| 🩺 [`03_fourteen_rubrics.md`](docs/03_fourteen_rubrics.md) | 14 audit rubrics × 3 layers (content / evaluation / governance), 0–5 anchors, 103-paper score distributions |
| 🧰 [`04_workbox_six_tools.md`](docs/04_workbox_six_tools.md) | The HEART Workbox: 6 paper-level tool families → 14 canonical web tools |
| 🛠 [`05_guidebook_workflow.md`](docs/05_guidebook_workflow.md) | 4-step `diagnose → prescribe → repair → re-claim` workflow |
| 📦 [`06_resource_availability.md`](docs/06_resource_availability.md) | FAIR statement, mirror locations, license, citation |

---

## 🎯 The 5 ethical dimensions

| Dimension | Benchmarkable scope |
|:---|:---|
| 👤 **Human-Centered** | Moral reasoning, empathy, well-being, professional boundaries, human agency |
| ⚖️ **Fairness & Inclusiveness** | Stereotyping, disparate treatment, representational harm, cultural coverage |
| 🛡️ **Safety & Reliability** | Dangerous assistance, jailbreak resistance, over-refusal, misuse, recovery |
| ⚙️ **Trustworthiness & Controllability** | Factuality, evidence support, sycophancy, temporal validity, rule-constrained reasoning |
| 🔒 **Privacy Protection** | Memorization, PII leakage, inferential disclosure, contextual integrity |

Cross-walked to 18 policy/governance sources in [`docs/02_five_dimensions.md`](docs/02_five_dimensions.md).

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
├── README.md                    ← you are here
├── CITATION.cff                 ← citation metadata
├── LICENSE                      ← CC-BY-4.0 (docs + workbook + rubrics)
├── LICENSE-code                 ← MIT (scripts, exporters)
│
├── docs/                        📖 6-doc reading stack
│   ├── 01_problem.md            ← motivation
│   ├── 02_five_dimensions.md    ← policy → 5 dimensions
│   ├── 03_fourteen_rubrics.md   ← 14 audit rubrics
│   ├── 04_workbox_six_tools.md  ← repair toolbox
│   ├── 05_guidebook_workflow.md ← 4-step workflow
│   ├── 06_resource_availability.md
│   └── interactive/             🌐 GitHub-Pages-served interactive site (mirror)
│
├── workbook/                    📊 master workbook (7 sheets)
│   ├── heart_toolkit.xlsx
│   └── exports/                 ← CSV / JSON exports
│
├── datasets/                    📚 bench corpus
│   ├── README.md                ← catalogue of 103 benches by dimension
│   └── sources.md               ← per-bench paper / code / Drive URLs
│
└── paper/                       📝 companion paper (added at release time)
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

Made with 💚 — pre-release; expect minor breakage as the workbook stabilises.

</div>
