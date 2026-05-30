# SOCKET (2023)

**Dimension**: Human centered  **Source / path**: `Paper: Choi et al. - 2023 - Do LLMs understand social knowledge? Evaluating the sociability of large language models with SocKET  
Issue: Construct clarity  
Score: 3  
— Lineage —  
• The paper introduces SocKET, a benchmark for evaluating the sociability of LLMs.  
• It defines “sociability” as the ability to understand and reason about social knowledge—including norms, roles, relationships, and intentions—in contextually appropriate ways.  
• The construct is operationalized via multiple-choice questions grounded in real-world social scenarios, drawing on theories from social psychology (e.g., theory of mind, social scripts, normative expectations).  
• However, the paper does not explicitly distinguish sociability from related constructs such as theory of mind, pragmatic reasoning, or moral judgment—leaving conceptual boundaries ambiguous.  
• While the test items are validated through expert annotation and pilot testing, no formal factor analysis or convergent/discriminant validity evidence is reported to confirm that SocKET isolates a distinct latent construct.`

## Representative tool

Social forum-derived scenario scaffolding with implicit norm inference tasks

## Tool explanation (full)

This tool crawls naturally occurring interaction posts from real social forums such as Reddit (e.g., the r/AskReddit thread “What’s the most socially awkward faux pas you’ve ever committed?”), preserving original contextual cues—including poster identity, comment-level disagreement, timestamps, and voting tendencies—and designs a three-stage task: 1) identifying implicit social roles and relational constraints; 2) inferring unstated normative expectations (e.g., “Why was this behavior mocked?”); and 3) generating responses aligned with majority consensus while retaining space for reasonable disagreement. Its core innovation lies in leveraging the inherent ambiguity and negotiability of authentic social expression—replacing hand-crafted, idealized moral dilemmas.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: Social knowledge / social situation understanding benchmark; comprehensively surveyed and classified under natural forum / social expression sources. Strength: Closeness to real-world social interaction; Weakness: Sources of social norms and cultural boundaries require explicit disclosure.” In strong_rubric_evidence, Scenario validity scores 4/5, with the note explicitly stating “closer to authentic social expression than abstract surveys,” confirming that its representative methodology is scenario construction grounded in natural forums.

## What it improves vs. baseline

Compared with traditional philosophical thought experiments (e.g., the trolley problem) or manually constructed normative judgment questions, this tool significantly enhances scenario authenticity and cultural embeddedness, requiring models to handle ambiguity, trade-offs, and group dynamics inherent in everyday social cognition—not merely apply preset principles.

## Adaptation example

In the adolescent-oriented campus social AI assistant dataset, posts such as “How to respond after being publicly called by the wrong name?” are extracted from authentic campus forums (e.g., the Education section of ChinaZhihu), preserving the original poster’s grade level, divergent comments from teachers and peers, and upvote distributions. The model is required not only to judge whether correction is warranted, but also to generate three feasible responses tailored to distinct role relationships (teacher–student vs. peer–peer) and cultural scripts (collectivist modesty vs. individual assertion), each annotated with the implicit norm it activates (e.g., “right to correct one’s name” vs. “maintenance of classroom order”).

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool crawls naturally occurring interaction posts from real-world social forums such as Reddit (e.g., the post “What’s the most socially awkward faux pas you’ve ever committed?” from r/AskReddit), preserving original contextual cues—including poster identity, comment-level disagreement, timestamps, and voting tendencies—and implements a three-stage task: (1) identifying implicit social roles and relational constraints; (2) inferring unstated normative expectations (e.g., “Why was this behavior mocked?”); and (3) generating responses aligned with majority consensus while retaining space for reasonable disagreement.
- **Normative grounding**: Its core lies in leveraging the ambiguity and negotiability of real-world social expressions to replace artificially constructed idealized moral dilemmas. Compared with traditional approaches based on philosophical thought experiments (e.g., the trolley problem) or manually crafted normative judgment items, this tool significantly enhances scenario authenticity and cultural embeddedness, requiring models to handle ambiguity, trade-offs, and group dynamics inherent in everyday social cognition rather than applying preset principles.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: This tool crawls naturally occurring interaction posts from real-world social forums such as Reddit (e.g., the post “What’s the most socially awkward faux pas you’ve ever committed?” from r/AskReddit), preserving original contextual cues—including poster identity, comment-level disagreement, timestamps, and voting tendencies—and implements a three-stage task: (1) identifying implicit social roles and relational constraints; (2) inferring unstated normative expectations (e.g., “Why was this behavior mocked?”); and (3) generating responses aligned with majority consensus while retaining space for reasonable disagreement.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool crawls naturally occurring interaction posts from real social forums such as Reddit (e.g., r/AskReddit’s “What’s the most socially awkward faux pas you’ve ever committed?”), preserving original contextual cues—including poster identity, comment-level disagreement, timestamps, and voting tendencies—and designs a three-stage task: 1) identifying implicit social roles and relational constraints; 2) inferring unstated normative expectations (e.g., “Why was this behavior mocked?”); and 3) generating responses aligned with majority consensus while retaining space for reasonable disagreement. Compared to traditional normative judgment tasks based on philosophical thought experiments (e.g., the trolley problem) or artificially constructed scenarios, this tool significantly enhances situational authenticity and cultural embeddedness, requiring models to handle ambiguity, trade-offs, and group dynamics inherent in everyday social cognition—not merely apply preset principles.  
— Survey —  
• from real examples collected in online forums (e.g., SOCKET), thereby combining standardized assessments with naturally occurring emotional expressions.
- **Task-format fit**: and design a three-stage task: 1) identifying implicit social roles and relational constraints; 2) inferring unstated normative expectations (e.g., “Why is this behavior mocked?”); and 3) generating responses that align with majority consensus while preserving space for reasonable disagreement.
- **Ground truth and disagreement design**: 3) Generate responses that align with the majority consensus while preserving space for reasonable disagreement.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• from real examples collected in online forums (e.g., SOCKET), thereby combining standardized assessments with naturally occurring emotional expressions. — Survey

## Synthesis

The review states that SOCKET collects real-world examples from online forums, combining standardized evaluation with natural emotional expression.
