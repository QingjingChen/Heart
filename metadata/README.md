# Metadata and Provenance Schema

This folder defines the machine-readable metadata expected for HEART resource
records.

## What "metadata schema" Means

A metadata schema is a stable list of fields that each resource record should
contain. For HEART, it tells users and scripts what fields to expect for:

- benchmark entries;
- rubric records;
- repair-tool records;
- mini-case records;
- anonymized expert-validation votes.

The JSON Schema is stored in:

- [`heart_metadata_schema.json`](heart_metadata_schema.json)

## What "provenance" Means

Provenance records where a claim or annotation came from. For HEART, provenance
fields include:

- `source_bib_key`: the BibTeX key in `survey/literature/tech_ethics_survey.bib`;
- `source_file_path`: where the evidence appears in this repository;
- `source_url`: paper, code, dataset, or dataset-card URL;
- `evidence_quote_or_summary`: short evidence note supporting the annotation;
- `last_verified`: most recent verification date;
- `annotator_role`: expert, senior reviewer, script, or maintainer;
- `review_status`: draft, expert-reviewed, adjudicated, or needs-update.

These fields make the resource easier to audit, update, and reproduce. They
also separate HEART from an automatic scoring benchmark: an LLM can parse the
schema and draft evidence retrieval, but human experts remain responsible for
final interpretation and calibration.

## Current Machine-readable Locations

| Record type | Current file |
|---|---|
| Benchmark corpus | `codebook/benchmarks.csv` |
| Rubric codebook | `codebook/rubrics.csv`, `docs/interactive/data/rubrics_full.json` |
| Repair tools | `codebook/tools.csv`, `docs/interactive/data/t_tools.json` |
| Specific sub-tools | `codebook/sub_tools.csv` |
| Mini cases | `docs/interactive/data/mini_cases.json`, `codebook/mini_cases.csv` |
| Expert validation | `survey/results/expert_votes_anonymized_long.csv` |
| Literature index | `survey/literature/tech_ethics_survey.bib` |
