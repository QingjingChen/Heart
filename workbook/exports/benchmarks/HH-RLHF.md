# HH-RLHF / Anthropic H&H (2022)

**Dimension**: Safety  **Source / path**: `Paper: Bai et al. - 2022 - Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback  
Issue: Construct clarity  
Score: 3  
— Lineage —  
• The paper explicitly defines “helpful” as “providing accurate, relevant, and comprehensive responses to user queries” and “harmless” as “avoiding outputs that are illegal, unethical, dangerous, or otherwise harmful”.  
• These definitions are grounded in widely accepted principles of AI safety and ethics (e.g., Asilomar AI Principles, IEEE Ethically Aligned Design).  
• However, the operationalization relies heavily on human annotator judgments without reporting inter-annotator agreement metrics or detailed annotation guidelines, limiting transparency and reproducibility.  
• The reward modeling step aggregates diverse human preferences into scalar rewards without disentangling potentially conflicting values (e.g., truthfulness vs. politeness), raising concerns about value pluralism and trade-off visibility.`

## Representative tool

Human preference-based helpful-harmless pairwise ranking template

## Tool explanation (full)

This tool adopts a pairwise ranking template: given the same prompt, human annotators are asked to select the response that is more “helpful” and more “harmless” between two model outputs; the annotation results constitute preference signals used to train reward models or directly assess model alignment. It does not rely on predefined rules or lexicons, but instead models safety boundaries as the collective human judgment—elicited in open-domain dialogue—on the trade-off between helpfulness and harmlessness.

Extraction basis: Primarily drawn from the “Type: helpful-harmless preference / red-team data” note in the Benchmark diagnostic table, and the consensus survey assessment stating “it shifts from static SFT to human preferences and red-teaming iteration,” supplemented by strong_rubric_evidence stating “open-domain dialogue and red-team preference data for training/evaluating the helpful-harmless balance,” confirming its core contribution as a preference-driven pairwise ranking paradigm.

## What it improves vs. baseline

Compared with earlier rule-based or keyword-matching safety evaluations (e.g., Toxicity Score), this tool is the first to embed safety assessment within real-world interactive objectives (helpful AND harmless), explicitly modeling value trade-offs via preference learning, thereby aligning evaluation more closely with users’ actual acceptance in deployment scenarios.

## Adaptation example

In the Legal Consultation Assistant dataset, this template can be reused to construct paired samples of “the same legal question + two different responses”; practicing lawyers are invited to jointly annotate preferences for “legal accuracy” and “risk avoidance,” thereby training a domain-specific reward model calibrated to safety boundaries in the legal domain.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool employs a pairwise ranking template: given the same prompt, human annotators are asked to select the response that is more “helpful” and more “harmless” between two model outputs; the annotation results constitute preference signals used either to train reward models or to directly evaluate model alignment.
- **Normative grounding**: It does not rely on predefined rules or lexicons; instead, it models safety boundaries as the collective human judgment—elicited in open-domain dialogues—regarding the trade-off between helpfulness and harmlessness.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Compared with earlier rule-based or keyword-matching safety evaluations (e.g., Toxicity Score), this tool is the first to embed safety assessment within real-world interactive objectives (helpful AND harmless), explicitly modeling value trade-offs via preference learning, thereby aligning evaluation more closely with users’ actual acceptance in deployment scenarios.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: This tool employs a pairwise ranking template: given the same prompt, human annotators are asked to select the response that is both more “helpful” and more “harmless” between two model outputs.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Synthesis

The survey does not mention this benchmark, and no subsequent work criticizes it.
