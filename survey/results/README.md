# HEART Expert Blind A/B Results (Anonymized)

This folder contains anonymized pilot expert-quality-assessment results for the five HEART mini cases. The raw Google Form export is not committed because it contains respondent initials. Experts are represented as `E01`--`E04` in response order.

## Files

| File | Purpose |
|---|---|
| `blind_key.csv / blind_key.json` | Researcher-side A/B decoding key for the five mini cases. |
| `expert_votes_anonymized_long.csv` | Per-expert, per-case, per-rubric votes decoded to HEART/original/tie. |
| `overall_acceptance_anonymized.csv` | Per-expert whole-case preference and acceptability decisions. |
| `expert_quality_table.csv` | Case-level H/O/T counts, ERS, whole-case preference, and acceptability. |
| `rubric_case_summary.csv` | Detailed 14-rubric by 5-case statistics used for the heatmap. |
| `layer_summary.csv` | Aggregated results by the three HEART rubric layers. |
| `agreement_by_case_rubric.csv` | Pairwise observed agreement inputs for consistency checks. |
| `expert_quality_overall.csv` | Overall ERS, vote totals, observed agreement, and Fleiss kappa. |
| `qualitative_comments_anonymized.csv` | Optional expert reasons with anonymized expert IDs. |
| `figures/rubric_case_heatmap_net_advantage.png` | Detailed rubric-by-case heatmap. |
| `figures/expert_quality_table.png` | Compact table figure for paper/slides. |

## Primary metric

ERS = (HEART votes + 0.5 × ties) / total rubric-level votes.

Latest pilot: n=4 experts, 280 rubric-level votes, H/O/T=244/8/28, ERS=0.921.