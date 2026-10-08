# MQR 4.91 — Two Newly Acquired Original-Paper Rival Courts and Literature Intake

Date: 2026-10-08. Same continuous MQR 4.91 research version. **Not** a new Lab, Notion version page, or new stage.

## Source identity, Drive normalization and duplicate audit

Both papers were uploaded by the user to the existing shared `00_INTAKE — Literature Radar` and identified by opening original PDF content, not by guessing names. Their DOI, author order and title were directly checked on the opening PDF page. Exact files **renamed and moved with the original Drive IDs** into shared `10_PAPERS` (folder `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP`) without deletion or copying:

1. **Grimmett, Whitsed & Horta (2020)**, *Presence-only species distribution models are sensitive to sample prevalence: Evaluating models using spatial prediction stability and accuracy metrics*. `Ecological Modelling` 431, 109194. DOI `10.1016/j.ecolmodel.2020.109194`. Original PDF file ID `1X5oYSlVVcCwR1xkUI0ld16PUt6JYjYoA`, 4,466,527 bytes. Original `grimmett2020.pdf`. Canonical name `Grimmett, Whitsed & Horta (2020) — Presence-Only Species Distribution Models Are Sensitive to Sample Prevalence - Evaluating Models Using Spatial Prediction Stability and Accuracy Metrics — DOI 10.1016-j.ecolmodel.2020.109194.pdf`.
2. **Lee, Correa & Bareinboim (2020)**, *General Transportability – Synthesizing Observations and Experiments from Heterogeneous Domains*. `AAAI-20`. DOI `10.1609/aaai.v34i06.6582`. Original PDF file ID `1kfiCHsh6ZERktdK309y7GShaNRUU9YS4`, 588,232 bytes. Original `jrevak,+AAAI_LeeS-6006.pdf`. Canonical name `Lee, Correa & Bareinboim (2020) — General Transportability - Synthesizing Observations and Experiments from Heterogeneous Domains — AAAI DOI 10.1609-aaai.v34i06.6582.pdf`.

Before mutation, Drive metadata-name duplicate searches for distinctive author/title/DOI strings found only the two uploaded PDFs; corresponding canonical matching named items did not already exist. This is a **title/DOI identity check**, not an assertion of a cryptographically exhaustive identical-byte search across every unrelated Drive file. Separate original paper **Lee & Bareinboim (2020), *Causal Effect Identifiability under Partial-Observability*** remains a different paper in 10_PAPERS; never conflate with Lee/Correa/Bareinboim 2020. Both moved file IDs read back in target `10_PAPERS`, no longer in intake.

## Rival A — Spatial map stability as established ecological practice

**Source sections read:** Grimmett abstract, §2.1–2.6, §§3.1–3.3, §§4–5. They used **ten virtual species**, five presence-size × five sample-prevalence sampling strategies with 20 replicates per strategy, evaluated **Maxent, GLM, RF, SVM**, and contrasted evaluation with **real known absences** vs presence-background validation. Importantly, they differentiated (a) single-model predictive success, (b) between-algorithm map consistency, and (c) within-algorithm **replicate map stability**. They used agreement between **thresholded spatial predictions**, including **Fleiss' κ** across replicate maps, and found reliance on AUC alone inadequate. The conclusion recommends spatial prediction stability alongside discrimination metrics, while algorithm-specific sample/background ratio effects differ (e.g. Maxent vs RF/SVM).

**Novelty ruling:** The proposition “two fitted models with similar/different AUC can have different geographic stability” and the practice of comparing prediction maps for variability are clearly **known before MQR**. Our observed 40 original fitted-fold target AUC values and rank reversal are **new source reconstructions for a particular Matsui 2026 dataset**, not the invention of spatial stability assessment.

**Direct competitive test:** In MQR's ten source-attested original fold rasters, compare pairwise continuous spatial **Spearman map-rank correlations**, raw-score Pearson correlations, and mean absolute score differences on identical valid target cells, alongside (but DISTINCT FROM) source-labelled AUC gaps. Record common mask/extent and four-fold source identifiers. Spearman is NOT Grimmett's Fleiss' κ; no claim of numeric direct equality or equivalent estimator. Source file `experiments/mqr-4.91/spatial_map_agreement.py` holds zero-effect synthetic rank tests; original replay source scanner `experiments/mqr-4.91/ten_target_fold_matrix.py` will emit actual scores only when raw CI completes with pinned original MD5. **Do not promote scientific PASS before CI and map statistics are verified.**

**Transfer Harvest:** MQR→C3X: scalar engine success or chess win rate cannot substitute for map/state-level agreement across repeated search traces; test independently with legal PV and fixed budget before accepting. MQR→RITHM: observed aggregate stability does not establish spatial/population coverage stability, needs denominator/capture audit. Conceptual questions only, not evidence that those labs have the same result.

## Rival B — Complete causal transport algorithms already exist under SCM assumptions

**Source sections read:** Lee/Correa/Bareinboim 2020 abstract, Algorithm 1 (GTR/GTRU), Theorems 1–3, concluding section. The paper formalizes **g-transportability** of **conditional interventional causal distributions**, under assumptions supplied by a qualitative causal graph, heterogeneous domains, and available observational/experimental distributions. Its GTR/GTRU algorithm is proven sound and complete (Thm. 3) **for that formal task**. The paper argues completeness of do-calculus for its specified general transportability problem. These are profound prior results, not a generic heuristic.

**MQR 4.91 non-equivalence:** Our `evaluation_contract_guard.py` checks compatibility of rank-AUC comparisons over different fitted score functions on identical specified external positive/negative reference populations. It **does not** take structural causal models, selection diagrams, interventional causal effects, d-separation or experimental distributions as inputs; therefore cannot inherit or contradict the **formal completeness** theorem of GTR/GTRU. Conversely a GTR causal effect transport formula does not establish score-cohort identity or automatically supply missing raster coordinates, original fitted .lambdas, source masks, spatial dependencies, and computational source artifacts. MQR's checker is **restricted engineering validation**, with no general completeness, optimal repair or scientific causal-transport theorem.

**Novelty ruling:** No title or abstract may claim invention of general heterogeneous evidence fusion, general transportable causal effect discovery, or complete minimal evidence-repair algorithm. Publication merit would need independent datasets and measured benefit vs (i) a human source audit, (ii) fixed-reference/source evaluation comparators, and (iii) pre-existing provenance/transportability tools, with a precisely stated engineering problem.

**Methodical caution:** Original Grimmett 20 replicates per sampling strategy vs original Matsui 4 fitted CV-fold models **have different sampling schemes**; their metrics and replicates are not comparable as independent effect estimates. General causal transport effects and target-rank AUCs likewise cannot be pooled. The source-Dryad/Zenodo file contracts remain empirically separate.

## Active experiment and nonadmission

Prior verified source: original Matsui 2026 **10/10** original target AUC reproduced, four fitted source-fold models projected onto each same target, many target-wise fold AUC gaps, dual-centered within-species fold×target descriptive interaction. CI `37786496173` and `37786929506` SUCCESS. Source-run map agreement **not yet admitted until new CI green**. If Zenodo GET transient 504, only bounded HTTP 429/502/503/504 retries and existing source digest checks are allowed; never lower hash gate, invent maps, or substitute post-selected score correlations. Review after actual run. The historical 4.90 closed state and 4.91 open state stay intact.

## Citation and reading integrity

PDF primary source identities and methods confirmed by directly reading stored Drive originals. No independent byte-level duplicate digest was obtained from Drive API. We did not claim original publication DOI content contradicts any other source. Do not fabricate comparable Spearman/Fleiss metrics or claim an original causal graph exists where none is recorded.

## Data and Notion governance

Only authorized active MQR Notion root: `3c8ef561-cf92-8156-93b6-fcf6de9955f7`. All stages of 4.91 are **headings within the existing root page**, not separate Lab rows or child pages. `doctrine/MQR-NOTION-SINGLE-LAB-CONTRACT.md` is mandatory. No request to move unrelated incidental PDFs or clutter intake was issued in this court.
