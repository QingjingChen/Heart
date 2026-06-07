# Datasheet for HEART

## Motivation

HEART is designed to help researchers and reviewers audit and revise existing
AI-ethics benchmarks. Rather than treating benchmark scores as leaderboard
endpoints, HEART treats benchmarks as reusable design resources: task formats,
annotation schemes, metrics, contrast sets, evaluator protocols, and governance
practices can be extracted and re-applied to new evaluation needs.

## Composition

The resource contains:

- 103 audited benchmark entries across five ethical dimensions;
- 16 policy and governance sources used for normative grounding;
- 14 diagnostic rubrics organized into three audit layers;
- 14 generic repair tools;
- 103 benchmark-specific repair sub-tools;
- five mini cases with original items, HEART-revised items, gap tables, tool
  prescriptions, repair execution notes, and limitations;
- anonymized expert A/B pilot validation results.

The benchmark corpus is available as CSV and XLSX tables in `codebook/`, as a
human-readable catalogue in `datasets/`, and as JSON-backed interactive pages in
`docs/interactive/`.

## Collection Process

The literature pool follows the project technology-ethics survey index
(`survey/literature/tech_ethics_survey.bib`). Candidate benchmarks were
identified through academic databases, major AI/HCI venues, upstream dataset
repositories, survey papers, backward/forward citation tracking, and
policy-keyword searches aligned with the five HEART dimensions.

The final 103-entry corpus was curated by law, ethics, and AI-governance experts
over iterative screening and annotation. Selection prioritized representative,
highly cited, historically meaningful, or tool-reusable benchmarks, including
resources that critique or extend earlier benchmarks.

## Inclusion Criteria

A resource is included as a benchmark entry if it has:

1. a task definition;
2. concrete test instances, prompts, examples, or dataset artifacts;
3. an evaluation protocol, metric, annotation schema, or scoring rule; and
4. a clear connection to at least one HEART ethical dimension.

Purely conceptual frameworks, policy-only documents, and general capability
benchmarks without explicit ethical-risk claims are excluded from the benchmark
corpus.

## Annotation

Each benchmark entry is mapped to a primary ethical dimension, scored against
the 14 HEART rubrics, and associated with one or more repair tools. Rubric
scoring is not fully automated. LLMs can help retrieve evidence or draft
candidate scores from the machine-readable codebook, but final calibration is
based on human expert reading of the benchmark paper, repository, related
survey literature, later related-work discussions, and author-stated
limitations.

## Recommended Uses

- Audit an existing benchmark for construct validity, evaluation design, and
  governance reliability.
- Identify which HEART repair tools are relevant to a diagnosed benchmark gap.
- Build revised benchmark items for a specific domain while keeping provenance
  and limitations visible.
- Use the five mini cases as worked examples of the audit-to-repair workflow.

## Non-Recommended Uses

- Do not treat HEART rubric scores as automatic truth labels.
- Do not use HEART to rank all ethics benchmarks as a leaderboard.
- Do not assume upstream benchmark datasets can be redistributed under HEART's
  license; upstream licenses still apply.

## Distribution and DOI

This GitHub repository is the working release. The reviewed archival release is
v0.1.0 with Zenodo DOI: <https://doi.org/10.5281/zenodo.20578201>. DOI metadata
is recorded in `.zenodo.json`.

## Maintenance

The current release version is recorded in `VERSION`. New benchmarks, revised
rubric anchors, and updated expert validation results should be released with a
version bump and a regenerated codebook via:

```bash
python3 codebook/build_codebook.py
python3 scripts/validate_codebook.py
```
