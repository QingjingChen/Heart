# HEART Resource Card

## Resource Identity

- **Name:** HEART: Human-centric Ethical Audit and Revision Toolkit for Benchmarks
- **Version:** v0.1.0
- **Repository:** <https://github.com/QingjingChen/Heart>
- **Interactive site:** <https://qingjingchen.github.io/Heart/interactive/>
- **DOI:** Pending Zenodo archival release. The repository includes `.zenodo.json`; a DOI will be minted for the indexed v0.1.0 release and back-filled into `CITATION.cff`.
- **License:** CC-BY-4.0 for data, documentation, codebook, rubric anchors, and resource metadata; MIT for scripts and site code.

## What Is Included

| Component | Format | Location | Machine-readable? |
|---|---|---|---|
| 103 benchmark corpus | CSV, XLSX, Markdown, JSON-backed website | `codebook/benchmarks.csv`, `codebook/heart_codebook.xlsx`, `datasets/README.md`, `docs/interactive/data/bench_map.json` | Yes |
| Source links for 103 benchmarks | Markdown | `datasets/sources.md` | Partially |
| Literature index pool | BibTeX | `survey/literature/tech_ethics_survey.bib` | Yes |
| 14 diagnostic rubrics | CSV, XLSX, Markdown, JSON | `codebook/rubrics.csv`, `docs/03_fourteen_rubrics.md`, `docs/interactive/data/rubrics_full.json` | Yes |
| 14 generic repair tools | CSV, XLSX, Markdown, JSON | `codebook/tools.csv`, `docs/04_workbox_fourteen_tools.md`, `docs/interactive/data/t_tools.json` | Yes |
| 103 benchmark-specific repair sub-tools | CSV, XLSX | `codebook/sub_tools.csv`, `codebook/heart_codebook.xlsx` | Yes |
| Five worked mini cases | CSV, JSON, website cards | `codebook/mini_cases.csv`, `docs/interactive/data/mini_cases.json`, `docs/interactive/mini_cases.html` | Yes |
| Blind expert A/B validation | anonymized CSV, PNG/PDF figures | `survey/results/` | Yes |
| Metadata and provenance schema | JSON Schema, Markdown | `metadata/heart_metadata_schema.json`, `metadata/README.md` | Yes |

## Machine-readable Codebook

Here, "machine-readable" means that the resource is exposed as structured files
that scripts or LLM-assisted workflows can parse without manually reading the
website: CSV, JSON, BibTeX, and XLSX tables with stable column names. The 14
rubrics can therefore be used by an LLM or a script to draft a score, retrieve
anchors, or recommend repair tools. However, HEART does **not** treat these
scores as a benchmark-of-benchmarks. Rubric scoring is calibrated by human
experts through close reading of the benchmark paper, repository, related
surveys, later related-work discussions, and author-stated limitations.

## Corpus Boundary

A resource is counted as a benchmark-related dataset only when it provides:

1. a task definition;
2. concrete test instances, prompts, examples, or a dataset; and
3. an evaluation protocol, metric, annotation schema, or scoring rule.

Purely conceptual papers, policy-only documents, and general capability
benchmarks without explicit ethical-risk claims are excluded from the 103-entry
benchmark corpus, though they may appear in the literature index or normative
source list.

## Expert Validation Package

The mini cases contain original items and HEART-revised items in
`docs/interactive/data/mini_cases.json`. The blind A/B key is stored in
`survey/results/blind_key.csv` and `survey/results/blind_key.json`. Expert votes
are stored in anonymized form in `survey/results/expert_votes_anonymized_long.csv`.
The raw Google Form export is not committed because it contains respondent
initials. The pilot validation uses four experts and reports Expert Revision
Success (ERS), whole-case preference, acceptability, and observed agreement.

## Installation and Reproduction

No package installation is required to read the resource. To regenerate the
derived codebook files:

```bash
python3 codebook/build_codebook.py
python3 scripts/validate_codebook.py
```

To inspect the interactive resource locally, open:

```text
docs/interactive/index.html
```

To reproduce the expert-result tables and figures, inspect the anonymized CSVs
in `survey/results/`. The committed figures were generated from
`survey/results/expert_votes_anonymized_long.csv`.

## Known Limitations

- The DOI is pending until the v0.1.0 archival release is deposited on Zenodo or
  another indexed dataset-sharing service.
- The 103-entry corpus is curated, not an exhaustive systematic review of all AI
  ethics literature.
- Expert rubric scores are evidence-guided human judgments; they should not be
  interpreted as automatic ground truth.
- Upstream benchmark licenses remain controlled by the original authors. HEART
  publishes an index, annotations, and repair guidance, not redistributed copies
  of all upstream datasets.
