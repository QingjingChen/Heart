---
name: Add a benchmark to the meta-review
about: Propose a new benchmark for inclusion in the HEART workbook
title: "[ADD] <benchmark name>"
labels: benchmark-addition
assignees: ''
---

## Benchmark identification

- **Name:**
- **Primary citation (with link):**
- **Code / data repository:**
- **Year of release:**
- **Primary ethical dimension** (choose one):
  - [ ] Human-Centered
  - [ ] Fairness & Inclusiveness
  - [ ] Safety & Reliability
  - [ ] Trustworthiness & Controllability
  - [ ] Privacy Protection

## What it claims to measure

One sentence in the construct → task → metric form. See
[`docs/04_workbox_six_tools.md` § Tool 1](../docs/04_workbox_six_tools.md).

## What it actually measures (your read)

Use the 14 rubrics in
[`docs/03_fourteen_rubrics.md`](../docs/03_fourteen_rubrics.md). For each
rubric, mark ✅ / ◐ / ✗ / — and briefly cite the textual evidence (page,
section, dataset card).

## Why it should be added

What new dimension coverage, normative source, scenario type, metric, or
governance practice does this benchmark add that the current 103-paper set
does not already cover?

## Review checklist (for maintainers)

- [ ] Cross-checked by ≥ 1 external rubric-trained reviewer
- [ ] Added to `workbook/heart_toolkit.xlsx` (`Tool来源分布表` sheet)
- [ ] CSV exports regenerated
- [ ] Score distribution in `rubrics_14_anchors.csv` updated
- [ ] Added to `datasets/README.md` under the right dimension
