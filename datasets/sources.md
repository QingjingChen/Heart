# Benchmark Source Index

For each of the 104 benchmarks in the HEART meta-review, this page lists:

- **Paper** — link to the original paper (arXiv / ACL Anthology / DOI)
- **Code / data upstream** — the original authors' GitHub or Hugging Face repository
- **Local dataset mirror** — the corresponding subfolder in the project's Google Drive
  ([root folder](https://drive.google.com/drive/folders/1imN8G7mQ-RgBCkT7-7tBiVF0RPvYJZtK))

Cells marked `—` indicate the URL could not be located. For very recent benchmarks
or survey-only-mentioned clusters (e.g. `TrustMH-Bench`, `PsycoLLM` cluster,
`Chinese-Safeguard`, `WebArena-Privacy`, `Phare`), URLs will be added as the
upstream resources become discoverable. Contributions welcome via the
`benchmark-addition` issue template.

## Human-Centered

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **MoralMachine (2018)** | <https://doi.org/10.1038/s41586-018-0637-6> | <https://www.moralmachine.net/> | — |
| 2 | **MoralStories (2021)** | <https://aclanthology.org/2021.emnlp-main.54/> | <https://github.com/demelin/moral_stories> | [Moral_stories_HC](https://drive.google.com/drive/folders/1taIab9ExlFU4SoCpbgw3GxB1vP7pNlGr) |
| 3 | **SCRUPLES (2021)** | <https://ojs.aaai.org/index.php/AAAI/article/view/17589> | <https://github.com/allenai/scruples> | [scruples_HC](https://drive.google.com/drive/folders/1xo7iehjQ_vozoalvAnP37FYyjEe3OvoX) |
| 4 | **ETHICS (2023)** | <https://arxiv.org/abs/2008.02275> | <https://github.com/hendrycks/ethics> | [Ethics_HC](https://drive.google.com/drive/folders/1MwM1tAeGqHy_7uDLRZkahzlSnKcfnruM) |
| 5 | **MFQ-2 (2023)** | <https://doi.org/10.1037/pspp0000470> | <https://moralfoundations.org/> | — |
| 6 | **MoralChoice (2023)** | <https://arxiv.org/abs/2307.14324> | <https://github.com/ninodimontalcino/moralchoice> | [Moral_choice_HC](https://drive.google.com/drive/folders/1fPqsa3njy9cGTGpC1KQls0rBw4lVxTAr) |
| 7 | **CMoralEval (2024)** | <https://arxiv.org/abs/2408.09819> | <https://github.com/tjunlp-lab/CMoralEval> | — |
| 8 | **CPsyExam (2024)** | <https://arxiv.org/abs/2405.18743> | <https://github.com/CAS-SIAT-XinHai/CPsyExam> | [CPsyExam_data](https://drive.google.com/drive/folders/1zO7imfVcKEl_vHUahrrJHibXCVoFicA3) |
| 9 | **EmotionBench (2024)** | <https://arxiv.org/abs/2308.03656> | <https://github.com/CUHK-ARISE/EmotionBench> | [EmotionBench_data](https://drive.google.com/drive/folders/1-V-pSA6dlRd86yw9u0uoVPRj_6NE0fSm) |
| 10 | **SMILE (2024)** | <https://arxiv.org/abs/2305.00450> | <https://github.com/qiuhuachuan/smile> | [smile_data](https://drive.google.com/drive/folders/1COAYS-qrA3nmZ1LUCQcZw-Te17yb8y6N) |
| 11 | **Educator-LLM (2025)** | <https://arxiv.org/abs/2508.15250> | <https://github.com/Yifan-EDU/Educator-LLM> | — |
| 12 | **HeartBench (2025)** | <https://arxiv.org/abs/2512.21849> | <https://github.com/HeartBench/HeartBench> | [HeartBench_data](https://drive.google.com/drive/folders/19i6t4bNkTZr1SjNRYwJ4q7N8rBIANu8q) |
| 13 | **HumaniBench (2025)** | <https://arxiv.org/abs/2505.11454> | <https://huggingface.co/datasets/aiana94/HumaniBench> | [HumaniBench_HC](https://drive.google.com/drive/folders/1auLDZ7ZrNTPRtE4oYx8i0HbpyaDkJ2rE) |
| 14 | **MoReBench (2025)** | <https://arxiv.org/abs/2510.16380> | <https://github.com/yuzhaouoe/MoReBench> | [Morebench_HC](https://drive.google.com/drive/folders/1CCGm51Wyqwlpb5p-o2q2kyAmu_Yv4E3I) |
| 15 | **NaVAB (2025)** | <https://arxiv.org/abs/2504.12911> | <https://github.com/Stmoonshine/NaVAB> | [NaVAB_HC](https://drive.google.com/drive/folders/1k-GWLK5ylDqjAIFtIOawgFtq7lKOeTiQ) |
| 16 | **VITAL (2025)** | <https://arxiv.org/abs/2502.13775> | <https://github.com/anudeex/VITAL> | [VITAL_HC](https://drive.google.com/drive/folders/1rs59eN1gQRkJlHSWZus5rVICuNSLTQW0) |
| 17 | **TrustMH-Bench (2026)** | <https://arxiv.org/abs/2603.03047> | <https://github.com/Qiyuan0130/TrustMH_Bench> | — |
| 18 | **WVS / World Values Survey (2012)** | <https://www.worldvaluessurvey.org/> | <https://www.worldvaluessurvey.org/> | [Wvs_HC](https://drive.google.com/drive/folders/1cf8Q5-27h5vhcYWB_Zmjrbc2AK1xYb0w) |
| 19 | **PsycoLLM / Psychometrics / PsychCounsel / ValueBench (survey-mentioned psychology/value benchmarks)** | <https://arxiv.org/abs/2310.01386>; <https://arxiv.org/abs/2406.04214> | <https://github.com/LingyueYan-NLP/PsycoLLM>; <https://github.com/Psychim/PsychoBench>; <https://github.com/GOODDASH/ValueBench> | — |
| 20 | **SOCKET (2023)** | <https://aclanthology.org/2023.findings-emnlp.969/> | <https://github.com/minjechoi/SOCKET> | — |
| 21 | **SOCIAL-CHEM-101 (2020)** | <https://aclanthology.org/2020.emnlp-main.48/> | <https://maxwellforbes.com/social-chemistry/> | — |
| 22 | **EtiCor (2023)** | <https://aclanthology.org/2023.emnlp-main.747/> | <https://github.com/Reddy-Lab-Code-Research/EtiCor> | — |
| 23 | **MoralBench / MIC (survey-mentioned value benchmarks)** | <https://arxiv.org/abs/2406.04428> | <https://github.com/agiresearch/MoralBench> | — |
| 24 | **MFTCXplain (survey-mentioned)** | <https://arxiv.org/abs/2506.19073> | <https://github.com/MeMoLab-NLP/MFTCXplain> | — |

## Fairness & Inclusiveness

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **Kleinberg-FairTradeoffs (2016)** | <https://arxiv.org/abs/1609.05807> | <https://arxiv.org/abs/1609.05807> | — |
| 2 | **GAP (2018)** | <https://aclanthology.org/Q18-1042/> | <https://github.com/google-research-datasets/gap-coreference> | [GAP](https://drive.google.com/drive/folders/1UJcXHuSXGGojsCh0XHxftCXN5rIVQq07) |
| 3 | **WinoBias (2018)** | <https://aclanthology.org/N18-2003/> | <https://github.com/uclanlp/corefBias> | [winoBias](https://drive.google.com/drive/folders/1jBhbTfJn1_2atfNlMZOz9StaDMfYmcY5) |
| 4 | **Winogender (2018)** | <https://aclanthology.org/N18-2002/> | <https://github.com/rudinger/winogender-schemas> | [winogender](https://drive.google.com/drive/folders/1qWqt7QoYxxOVYPsY4jFFukWwpj4SBPgY) |
| 5 | **BEC-pro (2020)** | <https://aclanthology.org/2020.gebnlp-1.1/> | <https://github.com/marionbartl/gender-bias-BERT> | [BEC-Pro](https://drive.google.com/drive/folders/1yNOouQOLjoF83E9HFaKTy7sENvKuBObp) |
| 6 | **CrowS-Pairs (2020)** | <https://aclanthology.org/2020.emnlp-main.154/> | <https://github.com/nyu-mll/crows-pairs> | [CrowS-Pairs](https://drive.google.com/drive/folders/1bKWlqkqlHkEFoojXETmCxJwzks6H4R2m) |
| 7 | **Dev-WordEmbed (2020)** | <https://aclanthology.org/2020.acl-main.487/> | <https://github.com/sunipa/On-Measuring-and-Mitigating-Biased-Inferences-of-Word-Embeddings> | — |
| 8 | **UnQover (2020)** | <https://aclanthology.org/2020.findings-emnlp.311/> | <https://github.com/allenai/unqover> | [UnQover](https://drive.google.com/drive/folders/1JQLmeM_Ogo3oSp3E3SW6pVACI2FpJ92q) |
| 9 | **WikiGenderBias (2020)** | <https://aclanthology.org/2020.findings-emnlp.106/> | <https://github.com/uclanlp/reducingbias> | [Wikigender](https://drive.google.com/drive/folders/14cmybbLYE2AQNdNb5raG4l5fr0BdD_zE) |
| 10 | **BOLD (2021)** | <https://dl.acm.org/doi/10.1145/3442188.3445924> | <https://github.com/amazon-science/bold> | [BOLD](https://drive.google.com/drive/folders/19vZBkiKE6NDazrRpui9lnA4lfax1vpEi) |
| 11 | **BUG (2021)** | <https://aclanthology.org/2021.emnlp-main.211/> | <https://github.com/SLAB-NLP/BUG> | [BUG](https://drive.google.com/drive/folders/1WIkQXrnSSZhWDAsZUylkZTgJ2mDTIhwF) |
| 12 | **HONEST (2021)** | <https://aclanthology.org/2021.naacl-main.191/> | <https://github.com/MilaNLProc/honest> | [HONEST](https://drive.google.com/drive/folders/11fvUPnsf8X3p3TU2wQgL4ofm5baBnLjA) |
| 13 | **NeuTral-WinoBiasPlus (2021)** | <https://aclanthology.org/2021.eacl-main.163/> | <https://github.com/uclanlp/corefBias> | [winoBias](https://drive.google.com/drive/folders/1jBhbTfJn1_2atfNlMZOz9StaDMfYmcY5) |
| 14 | **RedditBias (2021)** | <https://aclanthology.org/2021.acl-long.151/> | <https://github.com/umanlp/RedditBias> | [RedditBias](https://drive.google.com/drive/folders/1Ml2a87IqvTit8HCUvZ_NUino8M1n7m7Y) |
| 15 | **StereoSet (2021)** | <https://aclanthology.org/2021.acl-long.416/> | <https://github.com/moinnadeem/StereoSet> | [StereoSet](https://drive.google.com/drive/folders/1KlLJOuYzWq-6UNiLDC6gw6bHYy9aKJ4s) |
| 16 | **BBQ (2022)** | <https://aclanthology.org/2022.findings-acl.165/> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 17 | **HolisticBias (2022)** | <https://aclanthology.org/2022.emnlp-main.625/> | <https://github.com/facebookresearch/ResponsibleNLP> | [HolisticBias](https://drive.google.com/drive/folders/1rNaTZB-GI4KQYIes7CDk5xpkQICw6aJk) |
| 18 | **Panda (2022)** | <https://arxiv.org/abs/2205.12586> | <https://github.com/facebookresearch/ResponsibleNLP/tree/main/PANDA> | [PANDA](https://drive.google.com/drive/folders/1U8nND1y63TpUFZK7QW7BXLbrsfX0mJ7c) |
| 19 | **Grep-BiasIR (2023)** | <https://arxiv.org/abs/2201.07754> | <https://github.com/KlaraKrieg/GrepBiasIR> | [Grep-BiasIR](https://drive.google.com/drive/folders/1oUFe-Nm-1Q_P4xkzGFbj8CRpWepWlKfo) |
| 20 | **MoralChoice (2023)** | <https://arxiv.org/abs/2307.14324> | <https://github.com/ninodimontalcino/moralchoice> | [Moral_choice_HC](https://drive.google.com/drive/folders/1fPqsa3njy9cGTGpC1KQls0rBw4lVxTAr) |
| 21 | **TrustGPT (2023)** | <https://arxiv.org/abs/2306.11507> | <https://github.com/HowieHwong/TrustGPT> | [TrustGPT](https://drive.google.com/drive/folders/1W-5-49BkspcyXJjvgDxs6U_kjKRPPPH6) |
| 22 | **WinoQueer (2023)** | <https://aclanthology.org/2023.acl-long.507/> | <https://github.com/katyfelkner/winoqueer> | [winoqueer](https://drive.google.com/drive/folders/19HRqUE5EzHd0xyWaXytVux54byOD8b1U) |
| 23 | **CBBQ (2024)** | <https://arxiv.org/abs/2306.16244> | <https://github.com/YFHuangxxxx/CBBQ> | [CBBQ](https://drive.google.com/drive/folders/11SidpflggcB1CBTE4GhCiIFhSMxS0eIO) |
| 24 | **KoBBQ (2024)** | <https://aclanthology.org/2024.tacl-1.28/> | <https://github.com/naver-ai/KoBBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 25 | **FLEX (2025)** | <https://aclanthology.org/2025.findings-naacl.201/> | <https://github.com/anna-shin/FLEX> | — |
| 26 | **Phare (2025)** | <https://arxiv.org/abs/2505.11365> | <https://github.com/Giskard-AI/phare> | — |
| 27 | **BharatBBQ (2024/2025)** | <https://arxiv.org/abs/2508.07090> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 28 | **JBBQ (2024/2025)** | <https://arxiv.org/abs/2506.12327> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |

## Safety & Reliability

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **RealToxicityPrompts (2020)** | <https://aclanthology.org/2020.findings-emnlp.301/> | <https://github.com/allenai/real-toxicity-prompts> | [RealToxicityPrompts](https://drive.google.com/drive/folders/1ww3kW4ZjzU9j6KX8j8fIZfvbB-4rGTj6) |
| 2 | **HateCheck (2021)** | <https://aclanthology.org/2021.acl-long.4/> | <https://github.com/paul-rottger/hatecheck-data> | [hatecheck](https://drive.google.com/drive/folders/1tef9nBTgdbuzoVh9C7DaqYhVdQ8dlu81) |
| 3 | **ToxiGen (2022)** | <https://aclanthology.org/2022.acl-long.234/> | <https://github.com/microsoft/ToxiGen> | [toxigen](https://drive.google.com/drive/folders/1UmE-AqjuTRaPwLkX3UgC5EVd8Jy3i8qU) |
| 4 | **ToxicChat (2023)** | <https://arxiv.org/abs/2310.17389> | <https://huggingface.co/datasets/lmsys/toxic-chat> | [toxic-chat](https://drive.google.com/drive/folders/1Nnp5CcnTpGZHXz-qM8SWfWRDY0t0gq3r) |
| 5 | **Chinese-Safeguard (2024)** | <https://aclanthology.org/2024.findings-acl.184/> | <[https://huggingface.co/datasets/Libr-AI/do-not-answer/tree/main/files/cdna](https://github.com/Libr-AI/do-not-answer/tree/main/cdna)> | — |
| 6 | **Do-not-answer (2024)** | <https://arxiv.org/abs/2403.01244> | <https://github.com/Libr-AI/do-not-answer> | [Do not answer](https://drive.google.com/drive/folders/130aFvSdUJ7ecgul3DnbyhthwsQlD0MRM) |
| 7 | **FFT (2024)** | <https://arxiv.org/abs/2311.18580> | <https://github.com/cuishiyao96/FFT> | [FFT](https://drive.google.com/drive/folders/1mfWAfiBjhCqwoIgxFcFdNCT7HWrRsYfv) |
| 8 | **HarmBench (2024)** | <https://arxiv.org/abs/2402.04249> | <https://github.com/centerforaisafety/HarmBench> | [HarmBench](https://drive.google.com/drive/folders/1qV4Apl2VxNYcnGYbuy0n4S__6pNFxq4N) |
| 9 | **JailBreakV (2024)** | <https://arxiv.org/abs/2404.03027> | <https://github.com/EddyLuo1232/JailBreakV_28K> | [JailBreakV_28K](https://drive.google.com/drive/folders/13RQ0kav6pBAOBk6c0KovCuYs1t4lC3l8) |
| 10 | **LifeTox (2024)** | <https://aclanthology.org/2024.naacl-short.59/> | <https://github.com/mbzuai-nlp/LifeTox> | [LifeTox](https://drive.google.com/drive/folders/1baFmEIQlSVA1VTt6jIEW3Q-oJJgcE2tQ) |
| 11 | **MM-SafetyBench (2024)** | <https://arxiv.org/abs/2311.17600> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1i0eM) |
| 12 | **SALAD-bench (2024)** | <https://aclanthology.org/2024.findings-acl.235/> | <https://github.com/OpenSafetyLab/SALAD-BENCH> | [SALAD-bench](https://drive.google.com/drive/folders/1qrYJ5ooiUAaI6pNf0M7VnVshA4I5t6yJ) |
| 13 | **SafetyBench (2024)** | <https://arxiv.org/abs/2311.17600> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1i0eM) |
| 14 | **XSTest (2024)** | <https://aclanthology.org/2024.naacl-long.301/> | <https://github.com/paul-rottger/exaggerated-safety> | [xstest](https://drive.google.com/drive/folders/1C5Zipc6iQGDHHoUVD0z4lAyt9Z0C6fU2) |
| 15 | **Agent-SafetyBench (2025)** | <https://arxiv.org/abs/2412.14470> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1i0eM) |
| 16 | **SafeInfer (2025)** | <https://arxiv.org/abs/2406.12274> | <https://github.com/SomnathBanerjee/SafeInfer> | — |
| 17 | **SaFeRDialogues (2022)** | <https://aclanthology.org/2022.acl-long.447/> | <https://parl.ai/projects/saferdialogues/> | [saferdialogues_dataset](https://drive.google.com/drive/folders/1VM4j5N9oxLIVP0aV4s1Ec7xjD7vI2l5T) |
| 18 | **BAD / Bot-Adversarial Dialogue (2021)** | <https://aclanthology.org/2021.naacl-main.235/> | <https://parl.ai/projects/safety_recipes/> | — |
| 19 | **HarmEval (2025)** | <https://arxiv.org/abs/2402.15302> | <https://github.com/SomnathBanerjee/HarmEval> | [HarmEval](https://drive.google.com/drive/folders/1B4iPpDasT-Tl3pMxB7mkKMXamM1ZnXQW) |
| 20 | **HH-RLHF / Anthropic H&H (2022)** | <https://arxiv.org/abs/2204.05862> | <https://github.com/anthropics/hh-rlhf> | [H&H](https://drive.google.com/drive/folders/1nSWsGjxw-nAO16t7fqsR9d-IxBqzU4f3) |
| 21 | **AdvBench (2023)** | <https://arxiv.org/abs/2307.15043> | <https://github.com/llm-attacks/llm-attacks> | — |
| 22 | **Red-Eval (2024)** | <https://arxiv.org/abs/2308.09662> | <https://github.com/declare-lab/red-instruct> | — |
| 23 | **LatentJailbreak (2024)** | <https://arxiv.org/abs/2307.08487> | <https://github.com/qiuhuachuan/latent-jailbreak> | — |
| 24 | **CyberSec.Eval (2024)** | <https://arxiv.org/abs/2312.04724> | <https://github.com/meta-llama/PurpleLlama> | — |
| 25 | **C-Do-not-answer (2024)** | <https://arxiv.org/abs/2403.01244> | <https://github.com/Libr-AI/do-not-answer> | [C-Do-not-answer](https://drive.google.com/drive/folders/1Da5wlPwg3t811fcWedaJ9E0YrqJY2Lxk) |

## Trustworthiness & Controllability

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **FEVER (2018)** | <https://aclanthology.org/N18-1074/> | <https://github.com/awslabs/fever> | — |
| 2 | **HotpotQA (2018)** | <https://aclanthology.org/D18-1259/> | <https://hotpotqa.github.io/> | — |
| 3 | **TruthfulQA (2022)** | <https://aclanthology.org/2022.acl-long.229/> | <https://github.com/sylinrl/TruthfulQA> | [TruthfulQA](https://drive.google.com/drive/folders/1hs4RwS_DXsN4B2umx3zzpu5B0LIRdVyo) |
| 4 | **LegalBench (2023)** | <https://arxiv.org/abs/2308.11462> | <https://github.com/HazyResearch/legalbench> | — |
| 5 | **TrustGPT (2023)** | <https://arxiv.org/abs/2306.11507> | <https://github.com/HowieHwong/TrustGPT> | [TrustGPT](https://drive.google.com/drive/folders/1W-5-49BkspcyXJjvgDxs6U_kjKRPPPH6) |
| 6 | **HallusionBench (2024)** | <https://arxiv.org/abs/2310.14566> | <https://github.com/tianyi-lab/HallusionBench> | — |
| 7 | **LawBench (2024)** | <https://arxiv.org/abs/2309.16289> | <https://github.com/open-compass/LawBench> | — |
| 8 | **PatentEval (2024)** | <https://aclanthology.org/2024.findings-naacl.142/> | <https://github.com/ZoeYou/PatentEval> | — |
| 9 | **TrustLLM (2024)** | <https://arxiv.org/abs/2401.05561> | <https://github.com/HowieHwong/TrustLLM> | [TrustLLM](https://drive.google.com/drive/folders/1f9xq6WWgThKm4_Jf3OXGanZX7Ysg5l5J) |
| 10 | **Sycophancy-Sharma (2025)** | <https://arxiv.org/abs/2310.13548> | <https://github.com/meg-tong/sycophancy-eval> | — |
| 11 | **HaluEval (2023)** | <https://aclanthology.org/2023.emnlp-main.397/> | <https://github.com/RUCAIBox/HaluEval> | [HaluEval](https://drive.google.com/drive/folders/1ZB8S82cty7l_CJC9NeAgRfbOAUaWk0K9) |
| 12 | **FActScore (2023)** | <https://aclanthology.org/2023.emnlp-main.741/> | <https://github.com/shmsw25/FActScore> | — |
| 13 | **FreshQA / FreshLLMs (2024)** | <https://arxiv.org/abs/2310.03214> | <https://github.com/freshllms/freshqa> | — |
| 14 | **SycophancyBench / Model-Written Evaluations (2022)** | <https://arxiv.org/abs/2212.09251> | <https://github.com/anthropics/evals> | — |
| 15 | **DecodingTrust (2023)** | <https://arxiv.org/abs/2306.11698> | <https://github.com/AI-secure/DecodingTrust> | [Decoding trust](https://drive.google.com/drive/folders/16c6hPtRXdl7UxWoyOIO_36jR3i7QfWgP) |

## Privacy Protection

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **ConVerse (Findings of EACL 2026)** | <https://arxiv.org/abs/2511.05359> | <https://github.com/amrgomaaelhady/ConVerse> | [Converse](https://drive.google.com/drive/folders/117OloShfJJfokRK08YTRSmlMJJQEc8Yr) |
| 2 | **EAPrivacy (ICLR 2026)** | <https://arxiv.org/abs/2510.02356> | <https://github.com/xinjie-shen/EAPrivacy> | [eai_bench](https://drive.google.com/drive/folders/1qGGsHxd8DDrSAS8o_itdRViccfjZmXoD) |
| 3 | **GoldCoin (2024)** | <https://arxiv.org/abs/2406.11149> | <https://github.com/HKUST-KnowComp/GoldCoin> | [GoldCoin](https://drive.google.com/drive/folders/1wfHwJnFsOqSG7WsOKf9AZrxISgOOj9Ff) |
| 4 | **PrivacyLens (2024)** | <https://arxiv.org/abs/2409.00138> | <https://github.com/SALT-NLP/PrivacyLens> | [PrivacyLens](https://drive.google.com/drive/folders/140TkRL08Dv6D0oPiQcW5ElYGn9e-EvhW) |
| 5 | **AgentDAM (2025)** | <https://arxiv.org/abs/2503.09780> | <https://github.com/facebookresearch/ai-agent-privacy> | [wa_format](https://drive.google.com/drive/folders/12EDOGC-Md8UA8RLUIKvgB76bq3F4cI1Z) |
| 6 | **PrivaCI-Bench (2025)** | <https://arxiv.org/abs/2503.04340> | <https://github.com/HKUST-KnowComp/PrivaCI-Bench> | — |
| 7 | **Carlini Extraction / Training Data Extraction (2021)** | <https://arxiv.org/abs/2012.07805> | <https://github.com/ftramer/LM_Memorization> | — |
| 8 | **DecodingTrust-Privacy (2023)** | <https://arxiv.org/abs/2306.11698> | <https://github.com/AI-secure/DecodingTrust> | [Decoding trust](https://drive.google.com/drive/folders/16c6hPtRXdl7UxWoyOIO_36jR3i7QfWgP) |
| 9 | **ProPILE (2023)** | <https://arxiv.org/abs/2307.01881> | <https://github.com/SongHwangbo/ProPILE> | — |
| 10 | **ConfAIde (2023)** | <https://arxiv.org/abs/2310.17884> | <https://github.com/skywalker023/confAIde> | — |
| 11 | **LLM-PBE (2024)** | <https://arxiv.org/abs/2408.12787> | <https://github.com/QinbinLi/LLM-PBE> | — |
| 12 | **MPCI-Bench (2026)** | <https://arxiv.org/abs/2601.08235> | <https://github.com/shoujuw/MPCI-Bench> | [MPCI-Bench](https://drive.google.com/drive/folders/1Yk-FdwqiuuzyhsGhxw-WcXVD_2fAJXSb) |

## Survey papers consulted

The meta-review draws on the following surveys for the benchmark inventory,
rubric calibration, normative grounding, and cross-comparison of evidence
across bias / safety / privacy / trustworthiness / human-centered dimensions.
All entries are also recorded in the citation-verification sheet of
[`workbook/heart_toolkit.xlsx`](../workbook/heart_toolkit.xlsx).

| # | Survey | Authors | Year | Venue | URL |
|---|---|---|---|---|---|
| 2 | **Is ETHICS about ethics? Evaluating ETHICS dataset** | Hancox-Li & Blili-Hamelin | 2024 | NeurIPS EvalEval Workshop | <https://arxiv.org/abs/2410.13009> |
| 3 | **LLM Ethics Benchmark: A Three-Dimensional Assessment System** | Jiao et al. | 2025 | Scientific Reports | <https://doi.org/10.1038/s41598-025-18489-7> |
| 4 | **Computational Machine Ethics: A Survey** | Zhong et al. | 2025 | JAIR | <https://doi.org/10.1613/jair.1.16836> |
| 5 | **Bias and Fairness in Large Language Models: A Survey** | Gallegos et al. | 2024 | Computational Linguistics | <https://arxiv.org/abs/2309.00770> |
| 6 | **A Survey on LLM-as-a-Judge** | Gu et al. | 2025 | arXiv preprint | <https://arxiv.org/abs/2411.15594> |
| 7 | **Aligning Large Language Models with Human: A Survey** | Wang et al. | 2023 | arXiv preprint | <https://arxiv.org/abs/2307.12966> |
| 8 | **Survey on AI Ethics: A Socio-technical Perspective** | Mbiazi et al. | 2025 | Computational Intelligence | <https://doi.org/10.1111/coin.70149> |
| 9 | **A Survey on Privacy Risks and Protection in Large Language Models** | Chen et al. | 2025 | AI Review | <https://doi.org/10.1007/s44443-025-00177-1> |
| 10 | **A Survey on Large Language Model (LLM) Security and Privacy: The Good, the Bad, and the Ugly** | Yao et al. | 2024 | arXiv preprint | <https://arxiv.org/abs/2312.02003> |
| 11 | **A Survey of Privacy Attacks in Machine Learning** | Rigaki & Garcia | 2023 | ACM Computing Surveys | <https://doi.org/10.1145/3624010> |
| 12 | **Security and Privacy Challenges of Large Language Models: A Survey** | Das et al. | 2024 | arXiv preprint | <https://arxiv.org/abs/2402.00888> |
| 13 | **On Protecting the Data Privacy of Large Language Models (LLMs): A Survey** | Yan et al. | 2024 | arXiv preprint | <https://arxiv.org/abs/2403.05156> |
| 14 | **Privacy and Security Concerns in Generative AI: A Comprehensive Survey** | Golda et al. | 2024 | IEEE Access | <https://ieeexplore.ieee.org/document/10565250> |
| 15 | **The Ethics of AI Ethics: An Evaluation of Guidelines** | Hagendorff | 2020 | Minds and Machines | <https://doi.org/10.1007/s11023-020-09517-8> |
| 16 | **Everything is Connected: Inseparable Algorithmic Bias from Algorithmic Performance** | Raji et al. | 2021 | NeurIPS Datasets and Benchmarks | <https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/084b6fbb10729ed4da8c3d3f5a3ae7c9-Abstract-round2.html> |
| 17 | **A Survey on Evaluation of Large Language Models** | Chang et al. | 2024 | ACM TIST | <https://arxiv.org/abs/2307.03109> |
| 18 | **Trust in AI: Progress, Challenges, and Future Directions** | Eriksson et al. | 2025 | Humanities and Social Sciences Communications | <https://doi.org/10.1057/s41599-025-04746-7> |
| 19 | **BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices** | Reuel et al. | 2024 | NeurIPS | <https://arxiv.org/abs/2411.12990> |
| 20 | **Worldwide AI Ethics: A Review of 200+ Guidelines and Recommendations** | Correa et al. | 2023 | Patterns | <https://doi.org/10.1016/j.patter.2023.100857> |
| 21 | **Measuring Massive Multitask Language Understanding** | Hendrycks et al. | 2021 | ICLR | <https://arxiv.org/abs/2009.03300> |

---

## Coverage statistics

- Benchmarks with a paper URL: **104 / 104** (100%)
- Benchmarks with a curated upstream code/data URL: **104 / 104** (100%)
- Benchmarks with a corresponding Google Drive mirror: **67 / 104** (64%)

Paper URLs were assembled from `custom.bib`, a manual override map verified
against the arXiv title search and the local PDF library, and author-confirmed
upstream-repo pointers.
