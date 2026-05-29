# 06 — Resource Availability & FAIR Statement

This document records the **availability, licensing, and FAIR-principle
status** of the HEART resource. It is the canonical reference for downstream
users.

---

## Components and where they live

| Component | Primary location | Mirror / DOI |
|---|---|---|
| Master workbook (xlsx) | [`workbook/heart_toolkit.xlsx`](../workbook/heart_toolkit.xlsx) | Zenodo (TBD, at release) |
| Workbook CSV exports | [`workbook/exports/`](../workbook/exports/) | Zenodo (TBD) |
| 14-rubric definitions & anchors | [`docs/03_fourteen_rubrics.md`](03_fourteen_rubrics.md) + [`workbook/exports/rubrics_14_anchors.csv`](../workbook/exports/rubrics_14_anchors.csv) | Zenodo (TBD) |
| Workbox (6 tools / 48 entries) | [`docs/04_workbox_six_tools.md`](04_workbox_six_tools.md) + [`workbook/exports/toolbox_48_tools.csv`](../workbook/exports/toolbox_48_tools.csv) | Zenodo (TBD) |
| Full benchmark catalogue (104 entries) | [`datasets/README.md`](../datasets/README.md) | Zenodo (TBD) |
| Per-benchmark paper / code / Drive URL index | [`datasets/sources.md`](../datasets/sources.md) + Google Drive | Zenodo (TBD) |
| Web Demo source | [github.com/QingjingChen/heart_web_demo_pub](https://github.com/QingjingChen/heart_web_demo_pub) | — |
| Companion paper PDF | [`paper/README.md`](../paper/README.md) (added at release time) | — |

A permanent **Zenodo DOI** will be minted at release time and back-filled
into this table.

---

## FAIR principles

### Findable

- This repository is **public** at <https://github.com/QingjingChen/Heart>.
- A persistent **Zenodo DOI** will be issued at release time.
- The repository has a `CITATION.cff` with bibliographic metadata (final
  author / venue fields added at release time), so GitHub's "Cite this
  repository" feature works out-of-the-box.
- Top-level keywords (AI ethics, benchmark, fairness, safety, privacy,
  trustworthiness, human-centered) are in the README and `CITATION.cff`.

### Accessible

- All documentation is plain markdown; no proprietary viewer required.
- The workbook is provided both as **xlsx** (with formatting and notes) and
  as **5 CSV exports** (tool-agnostic).
- No login or registration required. The Google Drive folder linked from
  [`datasets/README.md`](../datasets/README.md) is set to public read access.

### Interoperable

- CSV exports use UTF-8 encoding and the standard CSV escaping convention.
- The dataset index points to **upstream Hugging Face / GitHub** locations
  wherever the original authors made them available, so existing dataset
  tooling works unchanged.
- Bibliographic metadata is exposed in `CITATION.cff` (CFF format) and will
  be added in BibTeX form at release time.

### Reusable

- Two licenses, both standard:
  - **CC-BY-4.0** for the workbook, documentation, rubric anchors, and
    dataset index. See [`LICENSE`](../LICENSE).
  - **MIT** for any code (exporter scripts, demo backend). See
    [`LICENSE-code`](../LICENSE-code).
- Upstream dataset licenses are **not overridden** by this repository — each
  upstream dataset remains under its original license; this repository only
  publishes an index and rubric annotations.
- Every workbook row records its source (`Source file/path` column) so
  provenance is traceable.

---

## How to verify the resource

1. **Clone or download** this repository.
2. Open [`workbook/heart_toolkit.xlsx`](../workbook/heart_toolkit.xlsx) — it
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

- Releases follow **semantic versioning** (e.g., `1.0.0`).
- A `CHANGELOG.md` is appended on every release.
- The current snapshot corresponds to **v1.0.0**.
- Bug-fix and rubric-clarification updates go to `1.0.x`. New benchmark
  additions to the workbook trigger a `1.x.0` release.

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
