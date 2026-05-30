# HaluEval (2023)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Multi-Source Hallucination Annotation Protocol with Cross-Model Disagreement Filtering

## Tool explanation (full)

This tool employs a three-stage hallucination annotation process: (1) multiple LLMs (e.g., Llama-3, Claude-3, GPT-4) independently generate responses to the same prompt; (2) human annotators label each sentence in every response as “supported,” “refuted,” or “unsupported” based on trusted sources such as Wikipedia and authoritative textbooks; (3) only samples exhibiting substantive disagreement across at least two model outputs (e.g., one model asserts A while another denies A), and for which human annotation confirms hallucination in at least one output, are retained—forming a high-confidence hallucination test set. The approach relies on publicly accessible knowledge sources and inter-model cognitive divergence.

Evidence extraction: Primarily drawn from the Benchmark diagnostic table notes: the note explicitly states, “Comprehensive surveys consider it a diagnostic tool that uses generated and human-annotated hallucination samples to assess models’ ability to detect textual hallucinations.” Combined with the strong_rubric_evidence, where all three criteria receive a score of 4 and all point to “diagnosing whether models can identify hallucinatory content in text,” it follows that the core innovation lies in the construction and filtering mechanism for hallucination samples—not merely in the evaluation framework itself.

## What it improves vs. baseline

Compared with earlier protocols that rely on single-model generation followed by human binary judgment (e.g., TruthfulQA), this protocol significantly increases the discrimination difficulty and diagnostic specificity for hallucinated samples through cross-model disagreement filtering, thereby avoiding mislabeling “unknown but reasonable inferences” as hallucinations and enabling evaluation to focus more precisely on clear factual violations.

## Adaptation example

In the legal consultation dataset, multiple legal large language models are invoked to generate responses to the same legal question (e.g., “Is it illegal for a landlord to refuse to return a rental deposit?”). Human annotators label the factual accuracy of each sentence according to provisions of the Civil Code. Only samples are retained in which the models directly contradict each other on key statutory provisions—such as the time limit for deposit refunds or the upper limit on liquidated damages—and where such contradictions are explicitly refuted by statutory text; this yields the Judicial Hallucination Specialized Test Set.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool employs a three-stage hallucination annotation pipeline: (1) multiple LLMs (e.g., Llama-3, Claude-3, GPT-4) independently generate responses to the same prompt; (2) human annotators label each sentence in every response as “supported,” “refuted,” or “unsupported” based on trusted sources such as Wikipedia and authoritative textbooks; (3) only samples exhibiting substantive disagreement across at least two model outputs (e.g., one asserts A while another denies A), and for which human annotation confirms at least one output as hallucinated, are retained—forming a high-confidence hallucination test set.  
— Survey —  
• HaluEval [Li and others, 2023] provides generated and human-annotated hallucinated samples for diagnosing whether models can recognize hallucinations in text.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Human annotators labeled each sentence of every response as “support,” “refute,” or “no evidence” based on trusted sources such as Wikipedia and authoritative textbooks.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Compared with earlier protocols that rely on single-model generation followed by human binary judgment (e.g., TruthfulQA), this protocol significantly increases the discrimination difficulty and diagnostic specificity for hallucinated samples through cross-model disagreement filtering, thereby avoiding mislabeling “unknown but reasonable inferences” as hallucinations and enabling evaluation to focus more precisely on clear factual violations.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: This tool employs a three-stage hallucination annotation pipeline: (1) multiple LLMs (e.g., Llama-3, Claude-3, GPT-4) independently generate responses to the same prompt; (2) human annotators label each sentence in every response as “supported,” “refuted,” or “unsupported” based on trusted sources such as Wikipedia and authoritative textbooks; (3) only samples exhibiting substantive disagreement across at least two model outputs (e.g., one asserts A while another denies A), and for which human annotation confirms at least one output as hallucinated, are retained—forming a high-confidence hallucination test set.  
— Survey —  
• HaluEval [Li and others, 2023] provides generated and human-annotated hallucinated samples for diagnosing whether models can recognize hallucinations in text.
- **Ground truth and disagreement design**: Only samples where at least two models generate substantively divergent outputs (e.g., one model asserts A while another denies A) and where human annotation confirms that one of the outputs is a hallucination are retained, forming a high-confidence hallucination test set.
- **Metric validity**: —
- **Evaluator reliability**: Human annotators labeled each sentence of every response as “support,” “refute,” or “no evidence” based on trusted sources such as Wikipedia and authoritative textbooks.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Human annotators labeled each sentence of every response as “support,” “refute,” or “no evidence” based on trusted sources such as Wikipedia and authoritative textbooks.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• HaluEval [Li and others, 2023] provides generated and human-annotated hallucinated samples for diagnosing whether models can recognize hallucinations in text. — Survey

## Synthesis

The survey states that HaluEval provides both generated and human-annotated hallucination samples to diagnose whether models can identify hallucinated content in text.
