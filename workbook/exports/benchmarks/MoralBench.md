# MoralBench / MIC (survey-mentioned value benchmarks)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Value-aligned preference scoring framework with orthogonal moral dimension weights

## Tool explanation (full)

MoralBench implements a structured preference elicitation protocol where LLM responses to moral dilemmas are scored not only on binary correctness but along orthogonal moral dimensions (e.g., Autonomy, Fairness, Care, Loyalty, Authority, Sanctity), each weighted per item based on philosophical grounding and empirical salience. Responses are ranked via pairwise comparisons between model outputs and human reference answers, then aggregated into dimension-specific scores using Bradley-Terry modeling. The framework explicitly decouples value conflicts (e.g., fairness vs. care trade-offs) rather than collapsing them into a single “moral score”.

Paper: MoralBench  
Issue: Construct clarity, Normative grounding, Source provenance  
Score: 3  
— Lineage —  
• MoralBench decomposes moral evaluation into distinct, philosophically grounded dimensions (Autonomy, Fairness, Care, Loyalty, Authority, Sanctity).  
• Scoring weights each dimension per item according to both philosophical justification and empirical relevance.  
• Preference rankings are derived from pairwise comparisons against human reference answers and modeled via Bradley-Terry to yield dimension-specific scores.  
• The framework avoids conflating competing values (e.g., fairness versus care) into a unitary metric.

## What it improves vs. baseline

Replaces flat pass/fail or single-score moral evaluation (e.g., early ETHICS) with fine-grained, theory-informed dimensional profiling—enabling diagnosis of *which* values an LLM over- or under-prioritizes, especially in contested cases.

## Adaptation example

In the medical AI consultation dataset, adapt MoralBench’s dimensional scoring to triage chat logs: for each patient query (e.g., “Should I disclose my HIV status to my employer?”), score model responses separately on Autonomy (respecting patient self-determination), Justice (fair access to employment), and Care (emotional safety)—then flag models that consistently suppress Autonomy scores while inflating Care, revealing hidden paternalism.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: MoralBench implements a structured preference elicitation protocol where LLM responses to moral dilemmas are scored not only on binary correctness but along orthogonal moral dimensions (e.g., Autonomy, Fairness, Care, Loyalty, Authority, Sanctity), each weighted per item based on philosophical grounding and empirical salience. The framework explicitly decouples value conflicts (e.g., fairness vs. care trade-offs) rather than collapsing them into a single ‘moral score’.
- **Normative grounding**: MoralBench implements a structured preference elicitation protocol where LLM responses to moral dilemmas are scored not only on binary correctness but along orthogonal moral dimensions (e.g., Autonomy, Fairness, Care, Loyalty, Authority, Sanctity), each weighted per item based on philosophical grounding and empirical salience. The framework explicitly decouples value conflicts (e.g., fairness vs. care trade-offs) rather than collapsing them into a single ‘moral score’.
- **Source provenance and evidence fitness**: MoralBench implements a structured preference elicitation protocol where LLM responses to moral dilemmas are scored not only on binary correctness but along orthogonal moral dimensions (e.g., Autonomy, Fairness, Care, Loyalty, Authority, Sanctity), each weighted per item based on philosophical grounding and empirical salience. The framework explicitly decouples value conflicts (e.g., fairness vs. care trade-offs) rather than collapsing them into a single ‘moral score’.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: Responses are ranked via pairwise comparisons between model outputs and human reference answers, then aggregated into dimension-specific scores using Bradley-Terry modeling.
- **Metric validity**: Replaces flat pass/fail or single-score moral evaluation (e.g., early ETHICS) with fine-grained, theory-informed dimensional profiling—enabling diagnosis of *which* values an LLM over- or under-prioritizes, especially in contested cases.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Yet these values remain fragmented and imbalanced: for instance, MIC reports that informational–utility values dominate (over 66%), while socio-democratic values such as justice and human rights are underrepresented. — Survey

## Synthesis

The review notes that these values are fragmented and unbalanced: for example, information-utilitarian values dominate (over 66%), whereas sociodemocratic values such as justice and human rights are underrepresented.
