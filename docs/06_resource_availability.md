# 06 — Resource Availability & FAIR Statement

This document records the **availability, licensing, and FAIR-principle
status** of the HEART resource. It is the canonical reference for downstream
users.

---

## Components and where they live

| Component | Primary location | Mirror / DOI |
|---|---|---|
| Master codebook (xlsx) | [`codebook/heart_codebook.xlsx`](../codebook/heart_codebook.xlsx) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Codebook CSV exports | [`codebook/`](../codebook/) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| 14-rubric definitions & anchors | [`docs/03_fourteen_rubrics.md`](03_fourteen_rubrics.md) + [`codebook/rubrics.csv`](../codebook/rubrics.csv) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Workbox (14 generic tools + 103 specific sub-tools) | [`docs/04_workbox_fourteen_tools.md`](04_workbox_fourteen_tools.md) + [`codebook/tools.csv`](../codebook/tools.csv) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Full benchmark catalogue (103 entries) | [`datasets/README.md`](../datasets/README.md) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Per-benchmark paper / code / Drive URL index | [`datasets/sources.md`](../datasets/sources.md) + Google Drive | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Literature index pool | [`survey/literature/tech_ethics_survey.bib`](../survey/literature/tech_ethics_survey.bib) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Expert blind A/B validation results | [`survey/results/`](../survey/results/) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Resource card | [`RESOURCE_CARD.md`](../RESOURCE_CARD.md) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Datasheet | [`DATASHEET.md`](../DATASHEET.md) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Metadata / provenance schema | [`metadata/heart_metadata_schema.json`](../metadata/heart_metadata_schema.json) | [Zenodo DOI: 10.5281/zenodo.20578201](https://doi.org/10.5281/zenodo.20578201) |
| Interactive site | [`docs/interactive/`](interactive/) (live at [qingjingchen.github.io/Heart/interactive/](https://qingjingchen.github.io/Heart/interactive/)) | GitHub Pages |
| Companion paper PDF | [`paper/README.md`](../paper/README.md) (added at release time) | — |

The reviewed v0.1.0 artifact is archived at Zenodo:
<https://doi.org/10.5281/zenodo.20578201>.

---

## FAIR principles

### Findable

- This repository is **public** at <https://github.com/QingjingChen/Heart>.
- The archival v0.1.0 release has a persistent **Zenodo DOI**:
  <https://doi.org/10.5281/zenodo.20578201>.
- The repository has a `CITATION.cff` with bibliographic metadata (final
  author / venue fields added at release time), so GitHub's "Cite this
  repository" feature works out-of-the-box.
- Top-level keywords (AI ethics, benchmark, fairness, safety, privacy,
  trustworthiness, human-centered) are in the README and `CITATION.cff`.

### Accessible

- All documentation is plain markdown; no proprietary viewer required.
- The codebook is provided both as **xlsx** (with formatting and notes) and
  as **9 CSV exports** (tool-agnostic).
- No login or registration required. The Google Drive folder linked from
  [`datasets/README.md`](../datasets/README.md) is set to public read access.

### Interoperable

- CSV exports use UTF-8 encoding and the standard CSV escaping convention.
- The dataset index points to **upstream Hugging Face / GitHub** locations
  wherever the original authors made them available, so existing dataset
  tooling works unchanged.
- Bibliographic metadata is exposed in `CITATION.cff` (CFF format), the
  technology-ethics literature pool is provided as BibTeX in
  `survey/literature/tech_ethics_survey.bib`, and per-record metadata /
  provenance expectations are defined in `metadata/heart_metadata_schema.json`.

### Reusable

- Two licenses, both standard:
  - **CC-BY-4.0** for the codebook, documentation, rubric anchors, and
    dataset index. See [`LICENSE`](../LICENSE).
  - **MIT** for any code (exporter scripts, demo backend). See
    [`LICENSE-code`](../LICENSE-code).
- Upstream dataset licenses are **not overridden** by this repository — each
  upstream dataset remains under its original license; this repository only
  publishes an index and rubric annotations.
- Every codebook row records its source (`Source file/path` column) so
  provenance is traceable.

---

## How to verify the resource

1. **Clone or download** this repository.
2. Open [`codebook/heart_codebook.xlsx`](../codebook/heart_codebook.xlsx) — it
   should contain seven sheets: `Tool来源分布表`, `Toolbox整合说明`,
   `Benchmark诊断`, `诊断rubrics说明`, `引用核验`, plus two legacy
   "评价体系（旧）" sheets retained for reproducibility of the rubric
   re-derivation.
3. Spot-check any benchmark row in `Tool来源分布表` — every row should have
   a `Source file/path` and a non-empty `Tool explanation (原文，全文)`.
4. Run the Web Demo per [`demo/README.md`](../demo/README.md) and confirm
   the rubric → tool recommendation flow.

---

## Versioning policy

- Releases follow **semantic versioning** (e.g., `v0.1.0`).
- A `CHANGELOG.md` is appended on every release.
- The current snapshot corresponds to **v0.1.0**.
- Bug-fix and rubric-clarification updates go to `v0.1.x`. New benchmark
  additions to the codebook trigger a `v0.x.0` release; DOI-backed archival
  snapshots are created for reviewed releases.

---

## How to contribute

- Open a GitHub issue using one of the templates in
  [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/).
- For **adding a new benchmark to the meta-review**, use the
  `benchmark-addition` template. Contributions are reviewed by at least one
  HEART maintainer plus one external rubric-trained reviewer.

---

## Contact

Open a GitHub issue for questions or contributions.
