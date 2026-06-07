# HEART Expert Blind A/B Preference Survey

This folder contains the blind expert A/B survey used for the five HEART mini
cases. Experts compare two anonymized versions of each case (A vs. B) against
the 14 HEART diagnostic rubrics and may provide a short optional reason.

The survey does not reveal which version is the original benchmark item and
which version is the HEART-guided revision. A/B side assignment is fixed in
`BLIND_KEY` and should be kept by the researchers only.

For each rubric, experts choose one of:

> **Version A is better · Version B is better · No improvement for this rubric**

Each rubric item is followed by an optional free-text reason box.

Note: Google Forms cannot combine a radio-choice item and a free-text reason in
one question without forcing the respondent to choose an "Other" option.
Therefore, the decision and the reason are implemented as adjacent items.

---

## One-Time Setup (About 2 Minutes)

1. Open **[script.google.com](https://script.google.com)** and create a new
   Apps Script project.
2. Copy all content from
   [`HEART_Survey_Form_Generator.gs`](HEART_Survey_Form_Generator.gs) into
   `Code.gs`, replacing the default file content.
3. Save with **Ctrl/Cmd-S**.
4. Select **`createHeartBlindSurveyForm`** in the function selector and click
   **Run**.
5. Accept the one-time OAuth authorization prompt.
6. Open **View → Logs** or the execution log. The script prints:
   - `Form edit URL`: for researchers to edit the form;
   - `Form response URL`: the link to send to experts;
   - `BLIND_KEY` JSON: researcher-side decoding key. Do **not** send it to
     experts.

Responses are collected in the Google Form **Responses** tab and can be exported
to Google Sheets.

---

## Design Details

### Blind Assignment (A vs. B)

| Case | dim | A | B |
|:---:|:---|:---|:---|
| 1 | Fairness and Inclusion · BBQ Age | HEART revision | Original |
| 2 | Safety and Reliability · XSTest | Original | HEART revision |
| 3 | Trustworthiness and Controllability · FreshQA | HEART revision | Original |
| 4 | Privacy Protection · PrivacyLens | Original | HEART revision |
| 5 | Human-Centeredness · CounselBench-Adv | Original | HEART revision |

Three of the five cases place the original on side A, and two place the HEART
revision on side A. This counterbalancing reduces side-position guessing. The
table is researcher-only.

### Instructions Shown on the Form

The form points experts to
[`https://qingjingchen.github.io/Heart/interactive/`](https://qingjingchen.github.io/Heart/interactive/)
and asks them to focus on **B. Diagnostic Rubrics** and **C. Revision Toolkit**.
Experts should not inspect **D. Revision Examples** during the blind survey,
because that page may reveal which items are revised.

### Size and Estimated Time

| Item | Count |
|:---|:---:|
| Expert metadata (initials + field) | 2 |
| Case title / version display blocks | 3 × 5 = 15 |
| Rubric questions per case (MC + optional reason) × 14 | 28 × 5 = 140 |
| Overall case judgments | 4 × 5 = 20 |
| Closing page | 1 |
| **Total** | about 180 |

Estimated completion time: 25–30 minutes.

---

## Editing the Survey

- To edit the landing text, case titles, or rubric descriptions, edit the
  constants at the top of the `.gs` file.
- To change A/B assignment, edit `BLIND_KEY` and swap the corresponding `A` and
  `B` fields for that case before re-running the script.
- Each run creates a new Google Form. Delete older forms from Google Drive if
  you do not want duplicates.

---

## Result Analysis

The response table is a standard Google Sheet. Suggested analyses:

- **Per-rubric A preference rate**: `Version A is better` divided by valid
  responses.
- **Per-case A preference rate** across the 14 rubrics.
- Decode A/B with `BLIND_KEY` and compute the HEART revision success rate.
- **Per-rubric inter-rater agreement**, such as Krippendorff's alpha or pairwise
  kappa.
- The optional reasons can be thematically coded against the 14 rubrics.

### Committed Anonymized Results

The repository includes the latest anonymized pilot results in
[`results/`](results/):

- [`results/blind_key.csv`](results/blind_key.csv): researcher-side A/B
  decoding key;
- [`results/expert_votes_anonymized_long.csv`](results/expert_votes_anonymized_long.csv):
  anonymized expert × case × rubric votes;
- [`results/expert_quality_table.csv`](results/expert_quality_table.csv): H/O/T
  counts, ERS, overall preference, and acceptability;
- [`results/rubric_case_summary.csv`](results/rubric_case_summary.csv):
  detailed statistics for 14 rubrics × 5 cases;
- [`results/figures/rubric_case_heatmap_net_advantage.png`](results/figures/rubric_case_heatmap_net_advantage.png):
  rubric-level heatmap.

The raw Google Form export is not committed because it contains respondent
initials. Expert identifiers in the repository are normalized as `E01`--`E04`;
only anonymized votes and auditable reason text are retained.

---

## Why Google Forms Instead of a Website Widget?

- No backend is required; the GitHub Pages site remains fully static.
- Experts do not need GitHub accounts.
- Responses automatically land in Sheets, which simplifies IRR analysis.
- Anyone can fork the repository and regenerate the form under their own Google
  account.
