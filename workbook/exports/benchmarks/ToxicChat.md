# ToxicChat (2023)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13279.txt`

## Representative tool

Real-world user-AI prompt injection template with toxicity-labeled continuation pairs

## Tool explanation (full)

This tool captures real first-turn user prompts from the Vicuna online demo and manually or semi-automatically labels whether the subsequent AI response is toxic. It is structured as a ternary tuple: input (user prompt) → output (model response) → binary toxicity label, emphasizing implicit jailbreaking and instruction-induced toxicity triggers within authentic interaction contexts.  
Extraction rationale: Primarily based on the “Type: Toxic Prompt Continuation Set” and “Strength: Real user-AI interaction” entries in the Benchmark diagnostic table’s notes; the source_excerpt explicitly states that “few efforts have been made towards real-world user-AI conversations” and highlights that “users posing questions or giving instructions” constitute a key challenge source.

## What it improves vs. baseline

In contrast to conventional evaluations based on social media texts (e.g., Twitter, Reddit) or manually synthesized toxic content, this work is the first to systematically focus on real users’ active adversarial queries toward open-domain dialogue models, thereby exposing the models’ blind spots in toxicity identification under non-adversarially annotated yet highly intention-ambiguous scenarios.

## Adaptation example

In a customer service dialogue dataset, extract real user complaints from the first-turn queries (e.g., “Your customer service is just for show—get lost!”), retain the original context, and annotate whether the customer service model’s response triggers secondary toxicity (e.g., emotional counterattack, user denigration), thereby constructing a toxicity propagation chain evaluation subset tailored to service scenarios.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Construct as a ternary structure of input (user prompt) → output (model response) → binary toxicity label, emphasizing implicit jailbreaks and instruction-induced toxicity triggers in authentic interaction contexts.  
— Lineage —  
• TOXICCHAT [Lin et al., 2023] is the first toxicity detection benchmark constructed from real-world user-AI interactions (via Vicuna), comprising 10,166 high-quality annotated examples. The dataset highlights nuanced phenomena unique
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This tool captures real first-turn user prompts (prompt) from the Vicuna online demo and manually or semi-automatically labels whether subsequent AI responses constitute toxicity (toxic).  
— Lineage —  
• OpenAI Moderation API agreement with ToxicChat is low — moderator API biased.  
— External perspective (Survey) —  
• TOXICCHAT [Lin et al., 2023] is the first toxicity detection benchmark constructed from real-world user-AI interactions (via Vicuna), comprising 10,166 high-quality annotated examples. The dataset highlights nuanced phenomena unique
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Compared with traditional evaluations based on social media texts (e.g., Twitter, Reddit) or artificially synthesized toxic content, this work is the first to systematically focus on real users’ active adversarial questioning of open-domain dialogue models, exposing the models’ blind spots in toxicity identification under non-adversarially labeled yet highly intention-ambiguous scenarios.  
— Lineage —  
• conversation-only; lacks systematic red-teaming attacks.  
— External Perspective (Survey) —  
• TOXICCHAT [Lin et al., 2023] is the first toxicity detection benchmark constructed from real-world user-AI interactions (via Vicuna), comprising 10,166 high-quality annotated examples. The dataset highlights nuanced phenomena unique
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: and manually or semi-automatically annotate whether the subsequent AI responses are toxic.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• OpenAI Moderation API agreement with ToxicChat is low — moderator API biased.
• conversation-only; lacks systematic red-teaming attacks.
• English-only, no multimodal.

## Self-acknowledged limits

Authors flag that Vicuna-only data may not generalize to other LLMs; English-only; user demographics unknown.

## External views (survey)

• TOXICCHAT [Lin et al., 2023] is the first toxicity detection benchmark constructed from real-world user-AI interactions (via Vicuna), comprising 10,166 high-quality annotated examples. The dataset highlights nuanced phenomena unique

## Synthesis

The survey states that ToxicChat is the first toxicity detection benchmark based on real user–AI interactions, containing 10,166 high-quality annotated instances. Subsequent work criticizes it for being limited to dialogues, lacking systematic red-teaming attacks, supporting only English, and lacking multimodality. The authors acknowledge limitations including data sourced exclusively from Vicuna (potentially limiting generalizability), English-only support, and unknown user demographics.
