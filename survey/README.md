# HEART · A/B Preference Survey

A binary-comparison questionnaire that asks reviewers to judge **5 mini
cases × 14 audit rubrics** = **70 short A/B comparisons** between the
**original** AI-ethics benchmark item and the **HEART-revised** version.

For each rubric, the reviewer chooses one of:

> **A is clearly better · B is clearly better · About the same · Can't tell from this item**

The survey is delivered as a **Google Form**. This folder ships the
generator script — you run it once and it builds the Form for you.

---

## 🚀 One-time setup (≈ 2 minutes)

1. Open **[script.google.com](https://script.google.com)** and sign in.
2. Click **New project**.
3. Open the file [`HEART_Survey_Form_Generator.gs`](HEART_Survey_Form_Generator.gs)
   in this folder, **select all → copy**, and paste it over the default
   `Code.gs` content.
4. Press **Ctrl/Cmd + S** to save the project. Name it `HEART Survey`.
5. In the function-picker (next to the ▶ Run button), choose
   **`createHeartSurveyForm`** and click **Run**.
6. The first time, Apps Script asks you to **authorise** the script's
   one-off `forms` and `drive` permissions — accept.
7. After ~5 seconds, open **View → Logs** (or **Execution log** in the
   bottom panel). You will see two URLs:
   - `Form edit URL: https://docs.google.com/forms/d/.../edit`  ← only you
   - `Form fill URL: https://docs.google.com/forms/d/e/.../viewform`  ← share this with reviewers

That's it. The Form is now live and responses will auto-collect into a
Sheet (in the Form's **Responses** tab → click the green Sheets icon).

---

## 🧱 What the Form contains

| Section | Items |
|:---|:---|
| **Reviewer background** | role / familiarity (both optional) |
| **Case 1 · BBQ Age** (Fairness & Inclusiveness) | A vs. B item display + 14 rubric questions + 1 free-text |
| **Case 2 · XSTest** (Safety & Reliability) | … |
| **Case 3 · FreshQA** (Trustworthiness & Controllability) | … |
| **Case 4 · PrivacyLens** (Privacy Protection) | … |
| **Case 5 · CounselBench-Adv** (Human-Centered) | … |
| **Thank you** | submit |

Per-case the reviewer sees:

1. The **original item** (Version A) — fielded display: context, question, options, gold label, etc.
2. The **HEART-revised item** (Version B) — same field layout.
3. 14 rubric questions — title in English, sub-title (help text) in Chinese.
4. 1 optional free-text comment.

---

## 🛠 Editing / re-running

- **Tweak title or intro**: edit `SURVEY_TITLE` / `SURVEY_DESCRIPTION`
  near the top of the `.gs` file, save, and re-run `createHeartSurveyForm`.
  Each run produces a **new** Form — delete the old one from your Drive
  if you do not want duplicates.
- **Add or remove rubric questions**: edit the `RUBRICS` array.
- **Update case content**: edit `CASES`. The script regenerates the
  content from `docs/interactive/data/mini_cases.json` in the repo — if
  you change a case there, re-run this generator script (see below).

### Regenerate the `.gs` after editing mini cases

The `.gs` file embeds the case content inline (under the `CASES = [...]`
array). If you change a case in
[`docs/interactive/data/mini_cases.json`](../docs/interactive/data/mini_cases.json),
edit the corresponding object inside `CASES` to keep them in sync, then
re-run `createHeartSurveyForm` to publish a new Form.

---

## 📊 Analysing the responses

The Form auto-creates a linked Google Sheet (under the **Responses** tab
in the Form editor). Each row is one reviewer; each column is one
question. For per-rubric agreement / preference analysis you can:

- Pivot in Sheets (rows = rubric, columns = response category).
- Or download as CSV and run any standard inter-rater-agreement script
  (Krippendorff's α, Cohen's κ for paired reviewers, etc.).

---

## ❓ Why a Google Form (and not an in-site widget)?

- **Zero backend** on the GitHub Pages site.
- **Reviewers don't need a GitHub account** — they just need a browser.
- **Responses auto-aggregate** in Sheets, ready for IRR analysis.
- **Easy to fork**: anyone can re-run this script on their own Google
  account and host their own copy.

If you later want an embedded version on the interactive site, you can
copy the Form's `embed` URL into an `<iframe>` on any page.
