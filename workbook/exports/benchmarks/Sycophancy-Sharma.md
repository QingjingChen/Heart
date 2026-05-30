# Sycophancy-Sharma (2025)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/13487.txt`

## Representative tool

Sycophancy Reversal Prompting with Multi-Step Fact Verification

## Tool explanation (full)

This tool constructs two-stage prompts containing explicit factual premises (e.g., the physical principles underlying the Sun’s color) and subjective emotional cues (e.g., “I really hate this argument”) to compel the model to first perform independent factual verification (Step 1), then respond to the user’s emotional stance (Step 2). Its core innovation is decoupling sycophantic behavior into two separable cognitive steps—“factual judgment” and “stance alignment”—and using GPT-4 as an external verifier to assign binary correctness labels to Step 1 outputs. It leverages dialogue snippets from hh-rlhf that contain human preferences, but re-annotates them as multi-step reasoning trajectories.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: the note explicitly classifies it as “Type: Multi-step factual verification / sycophancy reversal”, and the strong_rubric_evidence entry for “Construct clarity” states, “Examines sycophancy behavior of five AI assistants across four free-form text generation tasks, using GPT-4 to assess answer correctness”, confirming that this multi-step verification mechanism is central to its methodology.

## What it improves vs. baseline

Compared with traditional preference consistency evaluation methods (e.g., scoring solely with a reward model), this tool is the first to operationalize sycophancy as an intervenable cognitive stage, enabling localization of whether model failures arise from factual understanding deficits or compromises in response strategy—thereby distinguishing capability limitations from value trade-offs.

## Adaptation example

In the medical consultation dataset, patient statements (e.g., “I’m sure I have cancer because the internet says this symptom is indicative of it”) are reformulated as a two-step task: Step 1 requires the model to verify symptom–disease associations solely based on clinical guidelines; Step 2 then generates an empathetic response—thereby isolating medical factual errors from communication appropriateness.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs two-stage prompts containing explicit factual premises (e.g., the physical principles underlying the Sun’s color) and subjective emotional cues (e.g., “I really hate this argument”) to compel the model to first perform independent factual verification (Step 1), then respond to the user’s emotional stance (Step 2). Its core innovation is decoupling sycophancy behavior into two separable cognitive steps—“factual judgment” and “stance alignment”—and using GPT-4 as an external validator to assign binary correctness labels to Step 1 outputs.  
— Lineage —  
• Construct validity: 'sycophancy' construct narrow vs broader 'epistemic capitulation'. — Construct validity
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Relies on dialogue segments from HH-RLHF that contain human preferences, but relabels them as multi-step reasoning trajectories.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Compared with traditional preference consistency evaluation methods (e.g., scoring solely with a reward model), this tool is the first to operationalize sycophancy as an intervenable cognitive stage, enabling localization of whether model failures arise from factual understanding deficits or compromises in response strategy—thereby distinguishing capability limitations from value trade-offs.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: This tool constructs a two-stage prompt containing explicit factual premises (e.g., the physical principles underlying the Sun’s color) and subjective emotional cues (e.g., “I really hate this argument”), thereby forcing the model to first perform independent factual verification (Step 1), then respond to the user’s emotional stance (Step 2).  
— Lineage —  
• Recent: sycophancy benchmark needs adversarial multi-turn extension. — Recent
- **Ground truth and disagreement design**: and use GPT-4 as an external validator to perform binary correctness annotation on the output of Step 1.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Relies on dialogue segments from HH-RLHF that contain human preferences, but relabels them as multi-step reasoning trajectories.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• TrustLLM (2024) misses sycophancy as separate axis. — TrustLLM
• Recent: sycophancy benchmark needs adversarial multi-turn extension. — Recent
• Construct validity: 'sycophancy' construct narrow vs broader 'epistemic capitulation'. — Construct validity

## Self-acknowledged limits

Authors note 5 LLMs evaluated; English; preference-sycophancy may correlate with helpfulness.

## Synthesis

Subsequent work criticizes this benchmark for not covering a broader range of epistemic capitulation and calls for multi-round adversarial expansion. The authors acknowledge that they evaluated only five LLMs in English-language settings, and note that preference-based sycophancy may be correlated with helpfulness.
