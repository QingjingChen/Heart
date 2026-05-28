# Benchmark Source Index

For each of the 103 benchmarks in the HEART meta-review, this page lists:

- **Paper** — link to the original paper (arXiv / ACL Anthology / DOI)
- **Code / data upstream** — the original authors' GitHub or Hugging Face repository
- **Local dataset mirror** — the corresponding subfolder in the project's Google Drive
  ([root folder](https://drive.google.com/drive/folders/1imN8G7mQ-RgBCkT7-7tBiVF0RPvYJZtK))

Cells marked `—` indicate the URL could not be located. For very recent (2026)
or survey-only-mentioned benchmarks (e.g. `TrustMH-Bench`, `PsycoLLM` cluster,
`Chinese-Safeguard`, `WebArena-Privacy`, `Phare`), URLs will be added as the
upstream resources become discoverable. Contributions welcome via the
`benchmark-addition` issue template.

## Human-Centered

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **MoralMachine (2018)** | <https://doi.org/10.1038/s41586-018-0637-6> | <https://www.moralmachine.net/> | — |
| 2 | **MoralStories (2021)** | <https://aclanthology.org/2021.emnlp-main.54/> | <https://github.com/demelin/moral_stories> | [Moral_stories_HC](https://drive.google.com/drive/folders/1taIab9ExlFUID2yIplUc0CDKmHhCBH1P) |
| 3 | **SCRUPLES (2021)** | <https://ojs.aaai.org/index.php/AAAI/article/view/17589> | <https://github.com/allenai/scruples> | [scruples_HC](https://drive.google.com/drive/folders/1xo7iehjQ_vozoalCacrui4wWcRC3gwJs) |
| 4 | **ETHICS (2023)** | <https://arxiv.org/abs/2008.02275> | <https://github.com/hendrycks/ethics> | [Ethics_HC](https://drive.google.com/drive/folders/1MwM1tAeGqHy_7uDLRZkahzlSnKcfnruM) |
| 5 | **MFQ-2 (2023)** | <https://doi.org/10.1037/pspp0000470> | <https://moralfoundations.org/> | — |
| 6 | **MoralChoice (2023)** | <https://arxiv.org/abs/2307.14324> | <https://github.com/ninodimontalcino/moralchoice> | [Moral_choice_HC](https://drive.google.com/drive/folders/1fPqsa3njy9cGTGpC1Kdq8PsjqIIDl88P) |
| 7 | **CMoralEval (2024)** | <https://arxiv.org/abs/2408.09819> | <https://github.com/tjunlp-lab/CMoralEval> | — |
| 8 | **CPsyExam (2024)** | <https://arxiv.org/abs/2405.18743> | <https://github.com/CAS-SIAT-XinHai/CPsyExam> | [CPsyExam_data](https://drive.google.com/drive/folders/1zO7imfVcKEl_vHUahrrJHibXCVo42oIV) |
| 9 | **EmotionBench (2024)** | <https://arxiv.org/abs/2308.03656> | <https://github.com/CUHK-ARISE/EmotionBench> | [EmotionBench_data](https://drive.google.com/drive/folders/1-V-pSA6dlRd86yw9u0uo1qpQaTFCak3g) |
| 10 | **SMILE (2024)** | <https://arxiv.org/abs/2305.00450> | <https://github.com/qiuhuachuan/smile> | [smile_data](https://drive.google.com/drive/folders/1COAYS-qrA3nmZ1LUCQcZw-Te17yb8y6N) |
| 11 | **Educator-LLM (2025)** | <https://arxiv.org/abs/2508.15250> | — | — |
| 12 | **HeartBench (2025)** | <https://arxiv.org/abs/2512.21849> | — | [HeartBench_data](https://drive.google.com/drive/folders/19i6t4bNkTZr1SjNRYwJ4q7N8r0AHWvkC) |
| 13 | **HumaniBench (2025)** | <https://arxiv.org/abs/2505.11454> | <https://huggingface.co/datasets/aiana94/HumaniBench> | [HumaniBench_HC](https://drive.google.com/drive/folders/1auLDZ7ZrNTPRtEktev1otRBCa57fh1cf) |
| 14 | **MoReBench (2025)** | <https://arxiv.org/abs/2510.16380> | — | [Morebench_HC](https://drive.google.com/drive/folders/1CCGm51Wyqwlpb5p-o2q2kyAmu_Yv4E3L) |
| 15 | **NaVAB (2025)** | <https://arxiv.org/abs/2504.12911> | — | [NaVAB_HC](https://drive.google.com/drive/folders/1k-GWLK5ylDqjAIFtIOawgFtq7lKOeTiQ) |
| 16 | **VITAL (2025)** | <https://arxiv.org/abs/2502.13775> | — | [VITAL_HC](https://drive.google.com/drive/folders/1rs59eN1gQRkJlHSWZus5rVICuNSLTQW0) |
| 17 | **TrustMH-Bench (2026)** | — | — | — |
| 18 | **WVS / World Values Survey (2012)** | <https://www.worldvaluessurvey.org/> | <https://www.worldvaluessurvey.org/> | [Wvs_HC](https://drive.google.com/drive/folders/1cf8Q5-27h5vhcYWB_ZmjrbcZOsNCG8UX) |
| 19 | **PsycoLLM / Psychometrics / PsychCounsel / ValueBench (survey-mentioned psychology/value benchmarks)** | — | — | — |
| 20 | **SOCKET (2023)** | <https://aclanthology.org/2023.findings-emnlp.969/> | <https://github.com/minjechoi/SOCKET> | — |
| 21 | **SOCIAL-CHEM-101 (2020)** | <https://aclanthology.org/2020.emnlp-main.48/> | — | — |
| 22 | **EtiCor (2023)** | <https://aclanthology.org/2023.emnlp-main.747/> | <https://github.com/Reddy-Lab-Code-Research/EtiCor> | — |
| 23 | **MoralBench / MIC (survey-mentioned value benchmarks)** | <https://arxiv.org/abs/2406.04428> | <https://github.com/agiresearch/MoralBench> | — |
| 24 | **MFTCXplain (survey-mentioned)** | <https://arxiv.org/abs/2506.19073> | — | — |

## Fairness & Inclusiveness

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **Kleinberg-FairTradeoffs (2016)** | <https://arxiv.org/abs/1609.05807> | — | — |
| 2 | **GAP (2018)** | <https://aclanthology.org/Q18-1042/> | <https://github.com/google-research-datasets/gap-coreference> | [GAP](https://drive.google.com/drive/folders/1UJcXHuSXGGojsCh0XHxftCXNfxngwAFj) |
| 3 | **WinoBias (2018)** | <https://aclanthology.org/N18-2003/> | <https://github.com/uclanlp/corefBias> | [winoBias](https://drive.google.com/drive/folders/1jBhbTfJn1_2atfNlMZOz9StaDMfYmcY5) |
| 4 | **Winogender (2018)** | <https://aclanthology.org/N18-2002/> | <https://github.com/rudinger/winogender-schemas> | [winogender](https://drive.google.com/drive/folders/1qWqt7QoYxxOVYPsY4jFFukWUbK4CJJPh) |
| 5 | **BEC-pro (2020)** | <https://aclanthology.org/2020.gebnlp-1.1/> | — | [BEC-Pro](https://drive.google.com/drive/folders/1yNOouQOLjoF83E9HFaKTyT3swRa6dzM2) |
| 6 | **CrowS-Pairs (2020)** | <https://aclanthology.org/2020.emnlp-main.154/> | — | [CrowS-Pairs](https://drive.google.com/drive/folders/1bKWlqkqlHkEFoojXETnzqi7WmB411fKH) |
| 7 | **Dev-WordEmbed (2020)** | <https://aclanthology.org/2020.acl-main.487/> | — | — |
| 8 | **UnQover (2020)** | <https://aclanthology.org/2020.findings-emnlp.311/> | <https://github.com/allenai/unqover> | [UnQover](https://drive.google.com/drive/folders/1JQLmeM_Ogo3oSp3E3SW6pVACI2tlTGYR) |
| 9 | **WikiGenderBias (2020)** | <https://aclanthology.org/2020.findings-emnlp.106/> | <https://github.com/uclanlp/reducingbias> | [Wikigender](https://drive.google.com/drive/folders/14cmybbLYE2AV4VFebnsznVLILFrvcCj7) |
| 10 | **BOLD (2021)** | <https://dl.acm.org/doi/10.1145/3442188.3445924> | <https://github.com/amazon-science/bold> | [BOLD](https://drive.google.com/drive/folders/19vZBkiKE6NDazrRpui9lnA4lfax1vpbF) |
| 11 | **BUG (2021)** | <https://aclanthology.org/2021.emnlp-main.211/> | <https://github.com/SLAB-NLP/BUG> | [BUG](https://drive.google.com/drive/folders/1WIkQXrnSSZhWDAsZUylkZTgJ2mDTIhwF) |
| 12 | **HONEST (2021)** | <https://aclanthology.org/2021.naacl-main.191/> | <https://github.com/MilaNLProc/honest> | [HONEST](https://drive.google.com/drive/folders/11fvUPnsf8X3p3TU2wQgL4ofm5baBn4GP) |
| 13 | **NeuTral-WinoBiasPlus (2021)** | <https://aclanthology.org/2021.eacl-main.163/> | <https://github.com/uclanlp/corefBias> | [winoBias](https://drive.google.com/drive/folders/1jBhbTfJn1_2atfNlMZOz9StaDMfYmcY5) |
| 14 | **RedditBias (2021)** | <https://aclanthology.org/2021.acl-long.151/> | <https://github.com/umanlp/RedditBias> | [RedditBias](https://drive.google.com/drive/folders/1Ml2a87IqvTit8HCUvZ_NUin594pk69Ml) |
| 15 | **StereoSet (2021)** | <https://aclanthology.org/2021.acl-long.416/> | <https://github.com/moinnadeem/StereoSet> | [StereoSet](https://drive.google.com/drive/folders/1KlLJOuYzWq-6UNiLDC6gw6fcGTqL8Irg) |
| 16 | **BBQ (2022)** | <https://aclanthology.org/2022.findings-acl.165/> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 17 | **HolisticBias (2022)** | <https://aclanthology.org/2022.emnlp-main.625/> | <https://github.com/facebookresearch/ResponsibleNLP> | [HolisticBias](https://drive.google.com/drive/folders/1rNa2S65FbDtV6DcyTI4YIkYTG3LG3snh) |
| 18 | **Panda (2022)** | <https://arxiv.org/abs/2205.12586> | <https://github.com/facebookresearch/ResponsibleNLP/tree/main/PANDA> | [PANDA](https://drive.google.com/drive/folders/1U8nND1y63TpUFZ8Iw7MUSN8_GgozZc-K) |
| 19 | **Grep-BiasIR (2023)** | <https://arxiv.org/abs/2201.07754> | — | [Grep-BiasIR](https://drive.google.com/drive/folders/1oUFe-Nm-1Q_P4xkzGFbj8CRpWepWs2qQ) |
| 20 | **MoralChoice (2023)** | <https://arxiv.org/abs/2307.14324> | <https://github.com/ninodimontalcino/moralchoice> | [Moral_choice_HC](https://drive.google.com/drive/folders/1fPqsa3njy9cGTGpC1Kdq8PsjqIIDl88P) |
| 21 | **TrustGPT (2023)** | <https://arxiv.org/abs/2306.11507> | <https://github.com/HowieHwong/TrustGPT> | [TrustGPT](https://drive.google.com/drive/folders/1W-5-49BkspcyXJjvgDxs6U_kjKRPPPH6) |
| 22 | **WinoQueer (2023)** | <https://aclanthology.org/2023.acl-long.507/> | <https://github.com/katyfelkner/winoqueer> | [winoqueer](https://drive.google.com/drive/folders/19HRqUE5EzHd0xyWaXytVulNgbDFKqz6q) |
| 23 | **CBBQ (2024)** | <https://arxiv.org/abs/2306.16244> | <https://github.com/YFHuangxxxx/CBBQ> | [CBBQ](https://drive.google.com/drive/folders/11SidpflggcB1CBTE4GhCiIFhSMxS0eIO) |
| 24 | **KoBBQ (2024)** | <https://aclanthology.org/2024.tacl-1.28/> | <https://github.com/naver-ai/KoBBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 25 | **FLEX (2025)** | <https://aclanthology.org/2025.findings-naacl.201/> | — | — |
| 26 | **Phare (2025)** | — | <https://github.com/Giskard-AI/phare> | — |
| 27 | **BharatBBQ (2024/2025)** | <https://arxiv.org/abs/2508.07090> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |
| 28 | **JBBQ (2024/2025)** | <https://arxiv.org/abs/2506.12327> | <https://github.com/nyu-mll/BBQ> | [BBQ](https://drive.google.com/drive/folders/1caP795gTBJtp8UqhFNMBFyAnzVOw46l_) |

## Safety & Reliability

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **RealToxicityPrompts (2020)** | <https://aclanthology.org/2020.findings-emnlp.301/> | <https://github.com/allenai/real-toxicity-prompts> | [RealToxicityPrompts](https://drive.google.com/drive/folders/1kkitIpTlplknMKNnLGqKx2VI5BLHqpdI) |
| 2 | **HateCheck (2021)** | <https://aclanthology.org/2021.acl-long.4/> | <https://github.com/paul-rottger/hatecheck-data> | [hatecheck](https://drive.google.com/drive/folders/1tef9nBTgdbuzoVh9C7eeanpRknywJ20W) |
| 3 | **ToxiGen (2022)** | <https://aclanthology.org/2022.acl-long.234/> | <https://github.com/microsoft/ToxiGen> | [toxigen](https://drive.google.com/drive/folders/1UmE-AqjuTRaPwLkX3UgC5EVd8Jy3i8n0) |
| 4 | **ToxicChat (2023)** | <https://arxiv.org/abs/2310.17389> | <https://huggingface.co/datasets/lmsys/toxic-chat> | [toxic-chat](https://drive.google.com/drive/folders/1Nnp5CcnTpGZHXz-qM8SWfWRD-UnYwPWa) |
| 5 | **Chinese-Safeguard (2024)** | — | — | — |
| 6 | **Do-not-answer (2024)** | <https://arxiv.org/abs/2403.01244> | — | [Do not answer](https://drive.google.com/drive/folders/130aFvSdUJ7ecgul3DnbyhthwsvIUgTPe) |
| 7 | **FFT (2024)** | <https://arxiv.org/abs/2311.18580> | <https://github.com/cuishiyao96/FFT> | [FFT](https://drive.google.com/drive/folders/1mfWAfiBjhCqwoIgxFcFdNCT7HWrRsYfv) |
| 8 | **HarmBench (2024)** | <https://arxiv.org/abs/2402.04249> | <https://github.com/centerforaisafety/HarmBench> | [HarmBench](https://drive.google.com/drive/folders/1qV4Apl2VxNYcnGYbuy0n4S__6pN60PP0) |
| 9 | **JailBreakV (2024)** | <https://arxiv.org/abs/2404.03027> | <https://github.com/EddyLuo1232/JailBreakV_28K> | [JailBreakV_28K](https://drive.google.com/drive/folders/13RQ0kav6pBAOBk6c0KovCuxLBuXLM_EF) |
| 10 | **LifeTox (2024)** | <https://aclanthology.org/2024.naacl-short.59/> | <https://github.com/mbzuai-nlp/LifeTox> | [LifeTox](https://drive.google.com/drive/folders/1baFmEIQlSVA1VTt6jIEW3Q-oJJ5kNLM_) |
| 11 | **MM-SafetyBench (2024)** | <https://arxiv.org/abs/2311.17600> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1iUet) |
| 12 | **SALAD-bench (2024)** | <https://aclanthology.org/2024.findings-acl.235/> | — | [SALAD-bench](https://drive.google.com/drive/folders/1qrYJ5ooiU7XIISBcRZP1gbuXUBkTFfgm) |
| 13 | **SafetyBench (2024)** | <https://arxiv.org/abs/2311.17600> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1iUet) |
| 14 | **XSTest (2024)** | <https://aclanthology.org/2024.naacl-long.301/> | <https://github.com/paul-rottger/exaggerated-safety> | [xstest](https://drive.google.com/drive/folders/1C5Zipc6iQGDHHoUoPZRAry47aJXu64d_) |
| 15 | **Agent-SafetyBench (2025)** | <https://arxiv.org/abs/2412.14470> | <https://github.com/thu-coai/SafetyBench> | [SafetyBench](https://drive.google.com/drive/folders/19Km-8VzvIT9N4exB2zV13QV5Lgf1iUet) |
| 16 | **SafeInfer (2025)** | <https://arxiv.org/abs/2406.12274> | — | — |
| 17 | **SaFeRDialogues (2022)** | <https://aclanthology.org/2022.acl-long.447/> | <https://parl.ai/projects/saferdialogues/> | [saferdialogues_dataset](https://drive.google.com/drive/folders/1VM403gioB-oyJes-eJT__QS3znNgJvti) |
| 18 | **BAD / Bot-Adversarial Dialogue (2021)** | <https://aclanthology.org/2021.naacl-main.235/> | <https://parl.ai/projects/safety_recipes/> | — |
| 19 | **HarmEval (2025)** | <https://arxiv.org/abs/2402.15302> | — | [HarmEval](https://drive.google.com/drive/folders/1B4iPpDasT-Tl3pMxB7mkKMXamM1ZnXey) |
| 20 | **HH-RLHF / Anthropic H&H (2022)** | <https://arxiv.org/abs/2204.05862> | — | [H&H](https://drive.google.com/drive/folders/1nSWsGjxw-nAO16t7fqsR9d-IxBqOYqWr) |
| 21 | **AdvBench (2023)** | <https://arxiv.org/abs/2307.15043> | <https://github.com/llm-attacks/llm-attacks> | — |
| 22 | **Red-Eval (2024)** | <https://arxiv.org/abs/2308.09662> | — | — |
| 23 | **LatentJailbreak (2024)** | <https://arxiv.org/abs/2307.08487> | <https://github.com/qiuhuachuan/latent-jailbreak> | — |
| 24 | **CyberSec.Eval (2024)** | <https://arxiv.org/abs/2312.04724> | — | — |
| 25 | **C-Do-not-answer (2024)** | <https://arxiv.org/abs/2403.01244> | — | [C-Do-not-answer](https://drive.google.com/drive/folders/1Da5wlPwg3t811fcWedapescnTL8XE_Vn) |

## Trustworthiness & Controllability

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **FEVER (2018)** | <https://aclanthology.org/N18-1074/> | <https://github.com/awslabs/fever> | — |
| 2 | **HotpotQA (2018)** | <https://aclanthology.org/D18-1259/> | <https://hotpotqa.github.io/> | — |
| 3 | **TruthfulQA (2022)** | <https://aclanthology.org/2022.acl-long.229/> | <https://github.com/sylinrl/TruthfulQA> | [TruthfulQA](https://drive.google.com/drive/folders/1hs4RwS_DXsN4B2umx3zzpuu2lA0ymigo) |
| 4 | **LegalBench (2023)** | <https://arxiv.org/abs/2308.11462> | <https://github.com/HazyResearch/legalbench> | — |
| 5 | **TrustGPT (2023)** | <https://arxiv.org/abs/2306.11507> | <https://github.com/HowieHwong/TrustGPT> | [TrustGPT](https://drive.google.com/drive/folders/1W-5-49BkspcyXJjvgDxs6U_kjKRPPPH6) |
| 6 | **HallusionBench (2024)** | <https://arxiv.org/abs/2310.14566> | <https://github.com/tianyi-lab/HallusionBench> | — |
| 7 | **LawBench (2024)** | <https://arxiv.org/abs/2309.16289> | <https://github.com/open-compass/LawBench> | — |
| 8 | **PatentEval (2024)** | <https://aclanthology.org/2024.findings-naacl.142/> | — | — |
| 9 | **TrustLLM (2024)** | <https://arxiv.org/abs/2401.05561> | <https://github.com/HowieHwong/TrustLLM> | [TrustLLM](https://drive.google.com/drive/folders/1f9xq6WWgThKm4_Jf3OXGanZX7Ysg5l5J) |
| 10 | **Sycophancy-Sharma (2025)** | <https://arxiv.org/abs/2310.13548> | — | — |
| 11 | **HaluEval (2023)** | <https://aclanthology.org/2023.emnlp-main.397/> | <https://github.com/RUCAIBox/HaluEval> | [HaluEval](https://drive.google.com/drive/folders/1ZB8S82cty7l_CJC9NeAgRfbO26uUnsKP) |
| 12 | **FActScore (2023)** | <https://aclanthology.org/2023.emnlp-main.741/> | <https://github.com/shmsw25/FActScore> | — |
| 13 | **FreshQA / FreshLLMs (2024)** | <https://arxiv.org/abs/2310.03214> | <https://github.com/freshllms/freshqa> | — |
| 14 | **SycophancyBench / Model-Written Evaluations (2022)** | <https://arxiv.org/abs/2212.09251> | <https://github.com/anthropics/evals> | — |
| 15 | **DecodingTrust (2023)** | <https://arxiv.org/abs/2306.11698> | <https://github.com/AI-secure/DecodingTrust> | [Decoding trust](https://drive.google.com/drive/folders/16c6hPtRXdl7UxWoyOIO_kNKgIVvvvAac) |

## Privacy Protection

| # | Benchmark | Paper | Code / data upstream | Local dataset mirror |
|---|---|---|---|---|
| 1 | **Converse (2024)** | <https://arxiv.org/abs/2511.05359> | <https://github.com/skywalker023/confAIde> | [Converse](https://drive.google.com/drive/folders/117OloShfJJfokRK1mQer_s5DfMe-1Ktd) |
| 2 | **EAI-Bench (2024)** | <https://arxiv.org/abs/2510.02356> | — | [eai_bench](https://drive.google.com/drive/folders/1qGGsHxd8DDrSAS8o_itdRViccfjvWvox) |
| 3 | **GoldCoin (2024)** | <https://arxiv.org/abs/2406.11149> | <https://github.com/HKUST-KnowComp/GoldCoin> | [GoldCoin](https://drive.google.com/drive/folders/1wfHwJnFsOqSG7WsOKf9AZrxISgOOj9Ff) |
| 4 | **PrivacyLens (2024)** | <https://arxiv.org/abs/2409.00138> | <https://github.com/SALT-NLP/PrivacyLens> | [PrivacyLens](https://drive.google.com/drive/folders/140TkRL08Dv6D0oPiQcW5ElYGn9e-EMf-) |
| 5 | **WebArena-Privacy (2024)** | — | — | — |
| 6 | **PrivaCI-Bench (2025)** | <https://arxiv.org/abs/2503.04340> | — | — |
| 7 | **Carlini Extraction / Training Data Extraction (2021)** | <https://arxiv.org/abs/2012.07805> | <https://github.com/ftramer/LM_Memorization> | — |
| 8 | **DecodingTrust-Privacy (2023)** | <https://arxiv.org/abs/2306.11698> | <https://github.com/AI-secure/DecodingTrust> | [Decoding trust](https://drive.google.com/drive/folders/16c6hPtRXdl7UxWoyOIO_kNKgIVvvvAac) |
| 9 | **ProPILE (2023)** | <https://arxiv.org/abs/2307.01881> | <https://github.com/SongHwangbo/ProPILE> | — |
| 10 | **ConfAIde (2023)** | <https://arxiv.org/abs/2310.17884> | <https://github.com/skywalker023/confAIde> | — |
| 11 | **LLM-PBE (2024)** | <https://www.vldb.org/pvldb/vol17/p3201-li.pdf> | — | — |

---

## Coverage statistics

- Benchmarks with a paper URL: - Benchmarks with a curated upstream code/data URL: - Benchmarks with a corresponding Google Drive mirror: 
Paper URLs were assembled from three sources:

1. **`custom.bib`** (78 entries) — for benchmarks present in the manuscript bibliography
2. **Manual override map** — for benchmarks not in the bib but verifiable via the arXiv title search or our local PDF library (`Tool来源分布表` annotations)
3. **Author-confirmed GitHub README pointers** — where the upstream repo links to the paper
