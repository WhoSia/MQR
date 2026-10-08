# MQR-4.90 P9 — Pre-Publication Scientific Claim and Rivalry Court

**Research state (2026-10-08):** OPEN, source-backed pilot and formally tested summary-level nonidentification; `MQR-4.91` is a **candidate, not an authorized new stage**. This document distinguishes finished reproductions, immediately executable projects, and rejected novelty claims.

## Summary and falsifiable scientific claim

The tempting scalar `CV AUC − external AUC` is **not a well-defined estimand** when the two AUC scores depend on different fitted predictors, reference-negative populations, positive cohorts, target domains, selection rules or correlated sample ancestry. Our target is not to rename standard AUC/sample-bias facts. The candidate contribution is an executable, source-attested comparability compiler producing either a same-functional score comparison, an explicit conditional bound, or a *constructive, testable explanation of why the attempted inference is unavailable and what additional source data would repair it*.

Crucially, **summary-only nonidentification** is narrower than **raw-source nonidentification**. The original Matsui native-only fold models and environmental rasters are actually published: absence of numbers from a paper's main tables does not imply inability to calculate them from source archive. P9 must attempt the projection before declaring a nonidentification theorem over the full original data.

### Source-backed executed experiments

- **10/10** Matsui 2026 native-only external-region AUCs reproduced by Rust on original source positive cells and unrecorded-negative grid cells; exact source cells and scores hashed; CI `37728772674`. One article, three biological species lineages; not ten independent scientific studies.
- **12/12** original Maxent fourfold CV test-AUC values recovered from the 3 native-only training datasets; source-fold aggregates 0.86625 / 0.816025 / 0.85370, same rounded manuscript table A4 values; CI `37729333280`.
- **10/10** same-predictor, same-positive target scores rescored against a different *constructed*, explicitly documented negative reference: unrecorded external grid vs union of presence+unrecorded scored external cells. Actual AUC reference-only changes −0.00114385 to −0.13834407; mixture identity reproduced in Rust, CI `37729497381`. The constructed denominator is NOT the original Maxent internal CV background: do not call these observations original CV-optimism corrections.
- **108** source table rows from Koldasbayeva & Zaytsev 2025 supplementary Tables S4.1–S4.2 checked (two source biological families, absolute CV–external test discrepancy plus Pearson/Spearman); no pseudo-replication or signed meta-analysis.
- **P9 source feasibility**: DOI `10.5281/zenodo.19970795` contains all 12 individually fitted CV-fold `.lambdas` and 312 original environmental ASCII `.asc` files (with companion MXE etc.), including the chosen externally tested regions. Pinned both 96,676,282-byte model archive and 46,960,740-byte climate archive, MD5 checked; CI `37732263030 SUCCESS`. Official open-source Java Maxent v3.4.4 includes version-matched `maxent.jar` in `mrmaxent/Maxent/ArchivedReleases/3.4.4/maxent.jar` (675,926 bytes, Git blob `1a0a1826cbefdaf551463ed20e3a41944801955a`). Maxent's documented `density.Project` consumes `.lambdas` and environmental grids for target projection. **Projection itself has not yet passed an actual CI re-run**. Source pilot `p9_original_maxent_projection.py` is an *unexecuted*, fail-closed test proposal. Its existence proves no projection result.

## Paper candidate ranking (a design decision, not a journal prediction)

### A — Reproducible methodological audit (best presently supportable)

**Proposed title:** *When Validation AUCs Are Not Comparable: Source-Based Reconstruction and Reference-Design Audits of Spatial Model Transfer*.

**Research questions**: (1) Which apparently comparable validation AUCs evaluate the same predictor/reference/target functional? (2) Can published raw model and environment artefacts repair these mismatches? (3) How much of the observed change arises solely from deliberate reference-negative construction *under the same predictor*? (4) Which conclusions remain unidentified after valid source reproduction?

**Contribution:** audited 10 original external scores, 12 native CV fold scores, 10 within-predictor reference counterfactuals; separately classified 108 supplementary CV-to-test fidelity values; source-genealogy and failure-mode ledger. This is an empirical *audit protocol and case study*, not proof that spatial CV fails in all settings. Publishability requires at least one external independently authored study family or a convincing methodological comparison, a source-to-prediction fold replay, and spatially meaningful uncertainty.

Potential research communities: ecological forecasting evaluation, geospatial model validation, reproducible research methods. Journals should not be chosen prior to independent novelty scrutiny.

### B — Evidence-repair compiler (more ambitious, currently lower evidence)

**Proposed title:** *Compiling Comparability: A Typed, Provenance-Aware Repair System for Heterogeneous Predictive Performance Claims*.

**Method object:** `ScoreContract=(f_model,train_policy,selection_information,target_positive_distribution,negative_reference,spatiotemporal_scope,metric,root_sample_family,precision)`; operations carry typed preconditions, source hashes, and computational receipts. The system emits `COMPARABLE`, `CONDITIONAL_ONLY`, `FAMILY_DEPENDENT`, or `NOT_IDENTIFIABLE_GIVEN_DECLARED_INPUTS`.

**Necessary baselines/rivals:** common-background Maxent evaluation (Phillips et al. 2009, VanDerWal et al. 2009), formal causal transport/data fusion (Pearl and Bareinboim 2011; Bareinboim and Pearl 2013; Lee et al. 2020), and database why-provenance/minimal witness reasoning. A four-item Prolog witness list is **not** a proof of globally minimum or cheapest repair. The contribution would need a *new, restricted-domain complete* search algorithm or a substantial real-data reduction in misleading score promotions relative to baselines. Avoid conflating predictive-score evaluation transport with causal-effect transportability.

### C — Partial identification theorem (highest novelty barrier)

**Proposed title:** *What Can Published Validation Summaries Identify About External Performance?*.

A Lean/Prolog finite countermodel now shows that one can hold a published source-CV aggregate and externally deployed model target AUC constant while admitting hidden fold-target performance completions on opposite sides. This is **only a summary-information theorem** and a familiar type of partial-identification argument; do not call it a new impossibility theorem for full original data (which include model `.lambdas` and environments). Standard TV bounds and AUC mixture identities are known. A theory submission needs a substantively new sharp bound or optimal source-repair characterization conditional on realistic structural assumptions.

## P9 falsifiers and work program

**P9-A — true same-target model projection:** Use original Maxent 3.4.4 jar pinned by Git blob SHA. Reproject one **published final model** on its originally used 8 climate rasters and compare its entire output grid against the original archived target `.asc` before using predictions from any fold model. Failure to match blocks numerical claims. Then project four original CV-fold `.lambdas` onto the *same* target grid. Preserve environmental grid geometry and exact clamping/output transformation.

**P9-B — point/score alignment and selection information:** Join cell predictions with the same original external positive and reference-negative coordinates. Compute per-fold external AUC for each predictor. Do not treat the average of those AUCs as the expected external performance of the original full-refit model. Keep `fold`, `full`, `native internal CV`, `external target` typed as distinct evaluations.

**P9-C — dependence:** The target points/grid cells are spatially dependent; simple Bernoulli or cell-level i.i.d. bootstrap uncertainty is not defensible. Obtain metadata supporting spatial resampling, or report descriptive values without an SE. Separate species families, model folds, prediction targets, geographic raw source roots and different papers.

**P9-D — literature and implementation court:** Benchmark versus standard fixed-background comparisons and established transportability/provenance techniques. Strongest novelty opportunity is source-backed *certificate of what would repair a previously incomparable metric claim*, not a re-labeled familiar bound. Rust canonical primary; Lean theorem should be about a precisely stated restricted model; Prolog should detect unauthorized promotion and source ancestry.

**P9-E — stage closeout:** MQR-4.90 may legitimately close on a **bounded, source-reproduced noncomparability/repair boundary** with the remaining missing original fold-target scores stated explicitly. It must not close as positive signed pooled spatial-CV optimism without true study-level sample design, model selection and variance comparability. Opening 4.91 and any external paper submission needs a new explicit precommit and no claim of novelty solely from common-background AUC effects.

## External prior art list

- Phillips et al. 2009, DOI `10.1890/07-2153.1` (presence/background design).
- VanDerWal et al. 2009, DOI `10.1016/j.ecolmodel.2008.11.010` (fixed evaluation-area pseudo-absence comparisons).
- Pearl & Bareinboim 2011, DOI `10.1609/aaai.v25i1.7861` (transport conditions).
- Bareinboim & Pearl 2013, `https://proceedings.mlr.press/v31/bareinboim13a.html` (meta-transportability).
- Lee, Correa & Bareinboim 2020, DOI `10.1609/aaai.v34i06.6582` (general transport/data fusion).
- Database why-provenance, e.g. `https://doi.org/10.1145/3695829`; smallest-witness issues studied explicitly.
- Baker et al. 2024, DOI `10.1111/ddi.13802` (spatial bias corrective meta-analysis).
- Wang et al. 2023, DOI `10.1016/j.jag.2023.103364`, source `10.5281/zenodo.7546907` (secondary, still not an independent comparable signed optimism effect).

### Decision

The strongest defensible paper *today* is a **transparent source replay and inferential-boundary audit**; the most ambitious *possible future* paper is a **complete executable comparability and repair protocol for a precisely restricted class of model-performance claims**. A theoretical sharp-identification result is a stretch goal, not yet achieved. This document does not authorize MQR-4.91 or scientific closure of MQR-4.90.
