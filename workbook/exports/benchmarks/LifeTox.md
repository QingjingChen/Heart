# LifeTox (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13235.txt`

## Representative tool

Implicit Toxicity Classification Template with Real-World Advice Context

## Tool explanation (full)

This tool structures real-life advice posts from Reddit (featuring long contexts, personal narratives, and implicit legal/social norm assumptions) into a binary classification task: determining whether AI-generated advice is implicitly toxic (e.g., superficially neutral but inducing illegal behavior, evading responsibility, or reinforcing biases). It does not rely on explicit profanity dictionaries; instead, “unsafe advice” boundaries are defined via human annotation combined with community rule consensus, and models are required to perform fine-grained trade-offs between authentic user intent (e.g., rights-protection requests) and potential harms (e.g., incitement to property damage).

Extraction rationale: Primarily based on the Benchmark diagnostic table notes: “Type: Implicit Toxicity Advice Classification Set”, “87,510 instances sourced from Reddit subreddits LPT and ULPT”, “Examples show hazardous advice embedded within real rental disputes”; the source_excerpt provides only titles and fragments and does not describe methodological details, so this template is synthesized from the notes’ emphasis on “implicit toxicity” and “life-advice context”.

## What it improves vs. baseline

Compared with benchmarks such as ToxicChat—which rely on explicit toxicity lexicons or synthetic prompts—this benchmark improves the detection capability for implicit, context-dependent toxicity (e.g., pseudo-legitimization of violence, institutional neglect) and avoids misclassifying genuine rights-assertion requests as toxic, thereby enhancing scenario authenticity and ethical sensitivity.

## Adaptation example

In the LegalBench legal consultation dataset, user queries (e.g., “My landlord changed the lock without permission; can I break in to retrieve my belongings?”) are paired with advice from lawyers or non-professionals. This template labels whether the advice implicitly encourages self-help remedies, thereby constructing a sub-dataset for implicit violation advice detection targeting judicial AI systems.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool structures real-life advice posts from Reddit (featuring long contexts, personal narratives, and implicit legal/social norm premises) into a binary classification task: determining whether AI-generated advice is implicitly toxic (e.g., superficially neutral but encouraging illegal behavior, evading responsibility, or reinforcing biases). It does not rely on explicit profanity dictionaries; instead, the boundary of “unsafe advice” is defined through human annotation combined with community rule consensus.  
— Lineage —  
• single-axis (life advice) limits coverage. — SALAD-bench (2024)  
— External perspective (Survey) —  
• LifeTox [Kim et al., 2024] is a dataset that uncovers implicit toxicity in life-advice scenarios, built from more than 87,000 real Reddit posts from LPT and ULPT communities. It focuses on long-form Q&A with rich context.
- **Normative grounding**: The boundary of “unsafe advice” is defined through human annotation combined with community-established rule consensus, and models are required to perform fine-grained trade-offs between genuine user intent (e.g., rights-protection requests) and potential harm (e.g., incitement to property damage).
- **Source provenance and evidence fitness**: 87,510 instances sourced from the Reddit subreddits LPT and ULPT.  
— Lineage —  
• Reddit ≠ chat conversation distribution. — ToxicChat-style critique  
• English-only Reddit does not address non-English implicit toxicity. — Wang Chinese 2024 critique  
— External perspective (Survey) —  
• LifeTox [Kim et al., 2024] is a dataset that uncovers implicit toxicity in life-advice scenarios, built from more than 87,000 real Reddit posts from the LPT and ULPT communities. It focuses on long-form Q&A with rich context.
- **Context and stakeholder coverage**: This tool structures real-life advice posts from Reddit (featuring long contexts, personal narratives, and implicit legal/social norm premises) into a binary classification task.  
— Lineage —  
• Single-axis (life advice) limits coverage. — SALAD-bench (2024)  
— External Perspective (Survey) —  
• LifeTox [Kim et al., 2024] is a dataset that uncovers implicit toxicity in life-advice scenarios, built from more than 87,000 real Reddit posts from LPT and ULPT communities. It focuses on long-form Q&A with rich context.
- **Real-world harm linkage**: Assess whether AI-generated recommendations are implicitly harmful—such as appearing neutral on the surface while subtly encouraging illegal behavior, evading accountability, or reinforcing biases.


### Evaluation design (5 rubrics)
- **Scenario validity**: Example shows embedded hazardous advice within real rental disputes.  
— Lineage —  
• Reddit ≠ chat conversation distribution. — ToxicChat-style critique  
— External perspective (Survey) —  
• LifeTox [Kim et al., 2024] is a dataset that uncovers implicit toxicity in life-advice scenarios, built from more than 87,000 real Reddit posts from LPT and ULPT communities. It focuses on long-form Q&A with rich context.
- **Task-format fit**: Structured as a binary classification task: determining whether AI-generated advice is implicitly toxic.
- **Ground truth and disagreement design**: By combining human annotation with community-established rule consensus to define the boundary of “unsafe advice.”
- **Metric validity**: Compared with benchmarks such as ToxicChat—which rely on explicit toxicity lexicons or synthetic prompts—this benchmark improves the detection capability for implicit, context-dependent toxicity (e.g., pseudo-legitimization of violence, institutional neglect) and avoids misclassifying genuine rights-assertion requests as toxic, thereby enhancing scenario authenticity and ethical sensitivity.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: By combining human annotation with community-established rule consensus to define the boundary of “unsafe advice.”
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• single-axis (life advice) limits coverage. — SALAD-bench (2024)
• Reddit ≠ chat conversation distribution. — ToxicChat-style critique
• English-only Reddit doesn't address non-English implicit toxicity. — Wang Chinese 2024 critique

## Self-acknowledged limits

Authors flag Reddit demographic skew (young Western males); English only; implicit-toxicity ground truth labor-intensive.

## External views (survey)

• LifeTox[Kim et al., 2024] is a dataset that uncovers implicit toxicity in life-advice scenarios, built from more than 87,000 real Reddit posts from LPT and ULPT communities. It focuses on long-form Q&A with rich context.

## Synthesis

The survey notes that LifeTox uncovers implicit toxicity in life-advice scenarios from over 87,000 authentic Reddit posts. Subsequent work criticizes it for focusing solely on the single axis of life advice, thereby limiting coverage; for the mismatch between Reddit data distribution and real-world chat dialogue distribution; and for using only English Reddit data, thus failing to address non-English implicit toxicity. The authors acknowledge data bias toward young Western males, exclusive use of English, and the labor-intensive nature of obtaining ground-truth labels.
