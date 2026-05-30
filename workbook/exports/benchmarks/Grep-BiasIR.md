# Grep-BiasIR (2023)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13461.txt`

## Representative tool

Controlled Query-Document Pair Template with Gender-Aware Document Variants

## Tool explanation (full)

This tool constructs a structured information retrieval evaluation framework: for each original query (e.g., “how to become ceo”), six semantically equivalent document variants—explicitly annotated by gender attribute (male/female/neutral × relevant/irrelevant)—are manually generated, forming a controlled query-document pair set. The construction relies on author-curated manual creation combined with cleaning of Google search results, anchored to seven gender stereotype dimensions (e.g., Career, DomesticWork) grounded in social role theory, ensuring systematic activation of specific bias representations while preserving thematic consistency across documents.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: explicitly identifying its type as an IR query-document pair framework; specifying six document versions per query (orthogonally crossed by gender and relevance); and covering seven sub-dimensions corresponding to social-role-theory-driven stereotypes. In strong_rubric_evidence, both Scenario validity and Task-format fit received scores of 4, corroborating the effectiveness of this template design.

## What it improves vs. baseline

Moving beyond the limitations of traditional information retrieval (IR) evaluation—which focuses solely on relevance ranking—this work is the first to model gender representation bias as a systematic semantic deviation at the document level, enabling fine-grained attribution (e.g., identifying the implicit male leadership assumption embedded in descriptions of “CEO”) rather than relying solely on aggregate ranking metrics such as NDCG.

## Adaptation example

In the job resume screening dataset, the original job query (e.g., “senior software engineer”) is expanded into three document variants—resumes of equally qualified candidates described using masculine-coded language, feminine-coded language, and gender-neutral language—to detect whether the model systematically downranks qualified candidates whose resumes use feminine-coded language in ranking tasks.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs a structured information retrieval evaluation framework: for each original query (e.g., “how to become ceo”), six semantically equivalent document variants—explicitly annotated by gender attribute (male/female/neutral × relevant/irrelevant)—are manually generated, forming a controlled query-document pair set. The construction relies on author-curated manual creation combined with cleaning of Google search results, anchored to seven gender-stereotype dimensions (e.g., Career, DomesticWork) grounded in social role theory, ensuring that documents systematically activate specific bias representations while maintaining thematic consistency in content.  
— Lineage —  
• HolisticBias / WinoQueer perspective: binary gender only; small (118). — HolisticBias/WinoQueer
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Relies on manual construction by the authors combined with cleaning of Google search results.
- **Context and stakeholder coverage**: — Lineage —  
• IR community: relevance judgments are coarse; no LGBTQ+ extension. — IR community
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool constructs a structured information retrieval evaluation framework: for each original query (e.g., “how to become ceo”), six semantically equivalent document variants are manually generated, each explicitly annotated with gender attributes (male/female/neutral × relevant/irrelevant), yielding a controlled query–document pair set.
- **Task-format fit**: This tool constructs a structured information retrieval evaluation framework: for each original query (e.g., “how to become ceo”), six semantically equivalent document variants are manually generated, each explicitly annotated with gender attributes (male/female/neutral × relevant/irrelevant), yielding a controlled query–document pair set.
- **Ground truth and disagreement design**: — Lineage —  
• IR community: relevance judgments are coarse; no LGBTQ+ extension. — IR community
- **Metric validity**: Moving beyond the limitations of traditional information retrieval (IR) evaluation—which focuses solely on relevance ranking—this work is the first to model gender representation bias as a systematic semantic deviation at the document level, enabling fine-grained attribution (e.g., identifying the implicit male leadership assumption embedded in descriptions of “CEO”) rather than relying solely on aggregate ranking metrics such as NDCG.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Relies on manual construction by the authors combined with cleaning of Google search results.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• HolisticBias / WinoQueer perspective: binary gender only; small (118). — HolisticBias/WinoQueer
• IR community: relevance judgments are coarse; no LGBTQ+ extension. — IR community

## Self-acknowledged limits

Authors flag small scale (118 queries) and binary gender.

## Synthesis

Subsequent work criticizes it for considering only binary gender and having a small scale (118 queries), coarse relevance judgments, and failure to extend to LGBTQ+ populations. The authors themselves acknowledge limitations in scale and the binary gender setup.
