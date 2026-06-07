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
[📊 Codebook](codebook/) ·
[📚 Bench corpus](datasets/sources.md) ·
[📦 Resource card](RESOURCE_CARD.md) ·
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
| 📊 Get the raw data | [`codebook/benchmarks.csv`](codebook/) |
| 🔗 Look up a benchmark's paper / code / dataset mirror | [`datasets/sources.md`](datasets/sources.md) |
| 🔬 Inspect anonymized expert validation results | [`survey/results/`](survey/results/) |
| 📦 Review FAIR / resource-track metadata | [`RESOURCE_CARD.md`](RESOURCE_CARD.md), [`DATASHEET.md`](DATASHEET.md), [`metadata/`](metadata/) |
| 📚 Cite HEART | [`CITATION.cff`](CITATION.cff) (resource DOI: [`10.5281/zenodo.20578201`](https://doi.org/10.5281/zenodo.20578201)) |
| ✅ Sanity-check the codebook is internally consistent | `python3 scripts/validate_codebook.py` |
| ✅ Sanity-check the interactive site has no copy / vocab drift | `python3 scripts/site_consistency_check.py` |

---

## 📊 Data manifest

The codebook is the single source of truth. Every CSV is regenerated from
`docs/interactive/data/*.json` (the same files that power the live site)
by `codebook/build_codebook.py`. Sanity is enforced by
`scripts/validate_codebook.py`.

| File | Rows | Purpose | Key columns |
|---|---:|---|---|
| [`codebook/benchmarks.csv`](codebook/benchmarks.csv) | 103 | One row per `(benchmark × primary_dimension)` audit entry. A benchmark scored under two dimensions appears twice with a `[HC]` / `[F]` / `[S]` / `[T]` / `[P]` suffix. | `benchmark`, `dimension_en/_zh`, `paper_url`, `code_url`, `primary_tool_id`, `secondary_tool_id`, `rubrics_improved`, `adaptation_prompt_en/_zh`, `adaptation_example_en/_zh` |
| [`codebook/tools.csv`](codebook/tools.csv) | 14 | The 14 generic repair tools (T01–T14). | `tool_id`, `name_en/_zh`, `layer`, `core_practice_en/_zh`, `problem_fixed`, `core_rubrics_lifted`, `boundary_vs_neighbors`, `automatable`, `needs_human` |
| [`codebook/sub_tools.csv`](codebook/sub_tools.csv) | 206 | Primary + secondary specific sub-tools (one per benchmark per role); some secondary slots are empty. | `role`, `benchmark`, `parent_tool_id`, `subtool_name_en/_zh` |
| [`codebook/rubrics.csv`](codebook/rubrics.csv) | 14 | 14 diagnostic rubrics with v2 calibrated anchors. | `code`, `layer`, `name_en/_zh`, `key_question`, `anchor_0/1_2/3_4/5`, `score_distribution`, `mean` |
| [`codebook/policies.csv`](codebook/policies.csv) | 16 | Policy + governance corpus. | `source`, `type`, `url`, `support_<dimension>` |
| [`codebook/mini_cases.csv`](codebook/mini_cases.csv) | 5 | Worked before/after revision examples. | `id`, `dimension`, `title`, `source_dataset`, `rubrics_lifted`, `tools_applied` |
| [`codebook/rubric_tool_matrix.csv`](codebook/rubric_tool_matrix.csv) | 14×14 | Evidence-score matrix used by the site's `Gap → Tool Workflow` heatmap. | `rubric`, `T01`…`T14` |
| [`codebook/gap_detection.csv`](codebook/gap_detection.csv) | 14 | Per-rubric symptoms / red flags / evidence-to-inspect. | `code`, `typical_symptoms_en/_zh`, `red_flags`, `diagnostic_questions`, `domain_symptoms` |
| [`codebook/heart_codebook.xlsx`](codebook/heart_codebook.xlsx) | — | All eight CSVs bundled as one workbook (one sheet each). | — |
| [`survey/literature/tech_ethics_survey.bib`](survey/literature/tech_ethics_survey.bib) | 982 | Technology-ethics literature index used as the retrieval pool for corpus construction. | BibTeX keys, titles, authors, venues, years, URLs / DOIs |
| [`survey/results/expert_votes_anonymized_long.csv`](survey/results/expert_votes_anonymized_long.csv) | 280 | Anonymized expert A/B votes for five mini cases × 14 rubrics × 4 experts. | `expert_id`, `case_id`, `rubric`, `blind_choice`, `decoded_preference`, `score_for_ERS` |
| [`survey/results/rubric_case_summary.csv`](survey/results/rubric_case_summary.csv) | 70 | Detailed rubric-by-case validation statistics. | `case_id`, `rubric`, `heart_votes`, `original_votes`, `tie_votes`, `ERS`, `net_advantage` |
| [`metadata/heart_metadata_schema.json`](metadata/heart_metadata_schema.json) | — | JSON Schema for benchmark, rubric, tool, mini-case, and expert-vote records. | provenance fields, source URLs, review status, expert-vote schema |

The 103 benchmark corpus is therefore available as **CSV** (`codebook/benchmarks.csv`),
**XLSX** (`codebook/heart_codebook.xlsx`), **Markdown** (`datasets/README.md` and
`datasets/sources.md`), and **JSON-backed website data** under
`docs/interactive/data/`.

The 14-rubric codebook has a machine-readable version in
`codebook/rubrics.csv` and `docs/interactive/data/rubrics_full.json`. Here,
"machine-readable" means stable structured fields that a script or LLM-assisted
workflow can parse (rubric IDs, layers, anchor text, score distributions,
calibration notes). LLMs may assist evidence retrieval or draft scoring, but
final rubric calibration is performed by human experts through paper,
repository, related-work, survey, and limitation review.

### Manifest numbers

> **103** audited benchmark entries · **16** policy/governance sources · **5** dimensions · **14** diagnostic rubrics · **14** generic repair tools · **103** benchmark-specific sub-tools.

These numbers are the only ones that should appear anywhere in the repo,
the website, the README badges, or the paper. The validator hard-codes
them so any drift fails CI.

### Reproducing the site from the codebook

```bash
# edit JSON under docs/interactive/data/, then:
python3 codebook/build_codebook.py        # → codebook/*.csv + heart_codebook.xlsx
python3 scripts/validate_codebook.py      # PASS = 103/16/14/14
```

The website is statically served from `docs/interactive/`; opening
[`docs/interactive/index.html`](docs/interactive/) locally already works
without a build step. Do not hand-edit the CSVs — they are derived
artefacts.

---

## 📖 Documentation stack

Each doc mirrors one tab (or stage) of the interactive site, so the codebook
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
├── LICENSE                              ← CC-BY-4.0 (docs + codebook + rubrics)
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
├── codebook/                            📊 site-derived codebook (8 CSVs + xlsx bundle)
│   ├── heart_codebook.xlsx              ← multi-sheet bundle of all CSVs
│   ├── benchmarks.csv · tools.csv · sub_tools.csv · rubrics.csv
│   ├── policies.csv · mini_cases.csv · rubric_tool_matrix.csv · gap_detection.csv
│   └── build_codebook.py                ← regenerates everything from docs/interactive/data/
│
├── datasets/                            📚 bench corpus  (↔ site tab A sub-page)
│   ├── README.md                        ← catalogue of 103 benches by dimension
│   └── sources.md                       ← per-bench paper / code / Drive URLs
│
├── survey/                              🔬 expert validation + literature index
│   ├── literature/tech_ethics_survey.bib ← 982-entry retrieval/literature pool
│   └── results/                         ← anonymized A/B expert votes + figures
│
├── metadata/                            🧾 machine-readable schema + provenance fields
│   ├── README.md
│   └── heart_metadata_schema.json
│
└── paper/                               📝 companion paper (added at release time)
```

Resource-track support files:

- [`RESOURCE_CARD.md`](RESOURCE_CARD.md) — component manifest, formats, DOI
  status, reproduction instructions, limitations.
- [`DATASHEET.md`](DATASHEET.md) — motivation, composition, collection,
  inclusion criteria, intended / non-intended uses, maintenance.
- [`VERSION`](VERSION) — current release label (`v0.1.0`).
- [`.zenodo.json`](.zenodo.json) — metadata used for the DOI-backed Zenodo
  archival release: [`10.5281/zenodo.20578201`](https://doi.org/10.5281/zenodo.20578201).

---

## 📜 License

- 📐 **Code** (scripts, exporters, interactive-site JS/CSS): [MIT](LICENSE-code)
- 📖 **Codebook, documentation, dataset index, rubric anchors, interactive-site copy**: [CC-BY-4.0](LICENSE)

Source datasets indexed in [`datasets/`](datasets/) are governed by their original
licenses — see each upstream repository / paper.

---

## 🤝 Contributing & contact

Open a GitHub issue for questions, corrections, or new benchmark suggestions. See [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) for templates.

---

<div align="center">

Made with ❤️ — pre-release; expect minor breakage as the codebook stabilises.

</div>
