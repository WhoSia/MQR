# MQR-4.91 — CANDIDATE PRECOMMIT (NOT AN OPEN STAGE)

**Proposed official title:** MQR-4.91 — Target-Reference Normalization, Counterfactual Evaluation Bridges, Partial Identification of Transport Bias & Minimal Evidence-Repair Witnesses

**Date of first materialized evidence:** 2026-10-08. **Ancestor:** MQR-4.90 P8. **Status:** CANDIDATE WITH A REAL EMPIRICAL SUBSTRATE / SCIENTIFIC NOVELTY UNPROVEN / UNOPENED.

## 1. Founding scientific problem

Scores that nominally share a metric name (AUC) may evaluate different combinations of (i) predictor version/deployment policy, (ii) positive reference population, (iii) negative/background sampling design, (iv) geographical/temporal target, and (v) selection policy, with correlated raw-cohort genealogy.

The intended object is the typed functional

`AUC(f;P_positive,Q_negative) = Pr(f(X+) > f(X-)) + 0.5 Pr(f(X+) = f(X-))`.

The candidate is **not** a project to newly establish that background-point choice affects AUC; that is prior art. Its scientific task is to identify *which additional source observations suffice* to form honest same-functional comparisons and to certify that missing information prevents invalid pooling.

## 2. Source-backed experiments already executed under MQR-4.90

### A. Original-external AUC replication: 10/10 PASS

Original paper Matsui 2026 `10.1002/ece3.73534`, corrected `10.1002/ece3.73828`; publisher-linked raw prediction archive `10.5281/zenodo.19970795`. Verified 96,676,282-byte Maxent ZIP, MD5 `aa9c99dd43b3060589fa31dddf8501a4`, SHA256 `cca5973b5a09eacd11255c665cca5f3554370ec0970114a59395d6f8325838d5`. Ten prespecified native-only calibration→external-region cases within **three species and one publication** independently re-evaluated from raw positive/unrecorded-negative score files using Rust rank-pair AUC. **All ten match original printed Appendix A1–A3 to two decimals.** This is computational reproduction of source evidence, not ten independent new research studies.

GitHub `experiments/mqr-4.90/matsui_2026_native_only_raw_auc_reproduction.csv`; Actions run **37728772674 PASS**; source and run receipts in Google Drive folder `1szynM5kvA7sMExkaJ5sjvwrO3HPaXT1X`, file `17KY_T358qlBzgB58iUUqzDLwNTNj0N9k`.

### B. Original fold CV replication: 12 fold models / 3 cohorts PASS

Read exactly the published Maxent `maxentResults.csv` of fourfold models from the three native-only calibration cohorts; Rust recomputed fold-average test AUC:

- Oxalis America: 0.86625 (Appendix A4 prints 0.87). Fold reference backgrounds approximately 10,001–10,002 locations.
- Digitaria Europe: 0.816025 (A4 0.82). Background locations 5,609 per fold.
- Amaranthus North America: 0.85370 (A4 0.85). Background locations 10,108–10,120.

Actions **37729333280 PASS**; Drive receipt `19caqFqm8CxAx2Lxu8xP9pkH-kpNseftn`. A CV fold-specific fitted model is **not** the same as the cross-region fully fitted prediction model. The internal CV background is **not** the external region's set of unrecorded grid cells. No signed optimism identification follows.

### C. First *actual* within-predictor evaluation-reference bridges: 10/10 PASS

For each of the ten models, hold its published external prediction scores and scored positive cells fixed; compare (1) negative reference `Q_unrecorded`, the external target's grid cells without recorded presence, with (2) `Q_all_scored`, the empirical union of scored positive cells and unrecorded cells in that target. This second comparison is source-derived and **does not claim to reproduce the original fourfold Maxent CV background**.

If `n_pos` and `n_neg` refer to these scored cell sets, the identity

`AUC(f;P+,Q_all_scored) = (n_neg/(n_pos+n_neg)) AUC(f;P+,Q_unrecorded) + (n_pos/(n_pos+n_neg)) * 0.5`

holds because evaluating an empirical positive sample against the identical positive reference distribution yields pairwise AUC 0.5 (ties half-weighted). Rust **recomputed both AUCs from independent rank comparisons** and checked the identity in all ten cases; Actions **37729497381 SUCCESS**.

Examples:
- Oxalis America→Europe: 0.89026119 → 0.83452732 solely from reference choice (−0.05573387).
- Digitaria Europe→North America: 0.72092385 → 0.68950592 (−0.03141793).
- Amaranthus North America→Europe: 0.81076226 → 0.67241819 (−0.13834407, largest observed absolute change among ten prespecified cases).
- The smallest observed magnitude in these ten cases: Oxalis America→Oceania, 0.53192970 → 0.53078585 (−0.00114385).

GitHub `experiments/mqr-4.90/matsui_2026_reference_only_empirical_bridges.csv`, Rust `canonical/src/bin/reference_union_auc.rs`; independently verified receipt archived on Drive file `1wEjdfi573Ax8oVtVP8_EtpQobhyY2Jnk`. All numeric effects are reference-definition effects in a source-conditioned scored-cell sample. There are no independent confidence intervals and we make no claim of spatial leakage magnitude.

### D. Complementary CV-to-external fidelity evidence

Koldasbayeva & Zaytsev 2025 `10.1016/j.ecoinf.2025.103521`, official supplement Tables S4.1–S4.2: 108 metric rows over 2 biological families, 2 deployment policies, 9 CV methods, 3 metrics (MAE, Pearson, Spearman), 4 algorithms per row. Rust audit is based on source-reported summaries, NOT underlying 100 hyperparameter-level independent tests. Retained under `experiments/mqr-4.90/koldasbayeva_2025_s4_validation_fidelity.csv`; publisher source PDF preserved with checksums in Drive file `15ckVaSuCp2znB3XGXkpHopjJHARYT50p`. Uncertainty, sign and variance need new source detail.

## 3. Existing literature that limits novelty claims

- Phillips et al., 2009, DOI `10.1890/07-2153.1`, **Sample selection bias and presence-only distribution models: implications for background and pseudo-absence data**. Background sampling is consequential and was systematically studied long ago.
- VanDerWal et al., 2009, DOI `10.1016/j.ecolmodel.2008.11.010`, **Selecting pseudo-absence data for presence-only distribution modeling**. Importantly, the paper used **a fixed evaluation area with common pseudo-absence samples** for consistent model comparisons. Hence *fixing evaluation design to compare models is not novel*.
- Steen et al., 2024, DOI `10.1016/j.ecolmodel.2024.110754`, directly compares spatial/environmental background strategies for species at different equilibrium levels, source already in MQR paper set.
- Presence-only sample-prevalence/AUC sensitivity in *Ecological Modelling* 431 (2020) 109194, DOI `10.1016/j.ecolmodel.2020.109194`.
- Baker et al., 2024 DOI `10.1111/ddi.13802`, prior meta-analysis of spatial sampling-bias correction, 10 independent test studies / 13 effect estimates; no novelty in generic failure of random CV.
- Classical total-variation bounds for bounded function expectations, and elementary AUC mixture identities, are mathematical background, not claimed as new.

## 4. Proposed distinct contribution, to be tested, not presumed

A cross-study **scientific warrant repair compiler** with:
1. A lossless study-level declaration of the exact predictor `f`, positive target `P+`, negative reference `Q-`, reference/geographical domain, temporal orientation, model training policy, selection use of target labels, raw cohort parent IDs and associated precision.
2. Executable *counterfactual bridge operations* that reevaluate the **same predictor on the same labelled target scores** under two reference schemes, thereby separating reference-only numerical effects from changes requiring new model fit or external target labels.
3. A **partial-identification decision rule** that outputs a demonstrated interval when empirical constraints exist, or a typed unidentifiability witness when they do not. Standard total-variation sensitivity calculation is explicitly conditional on evidence of a bound; never fabricate a measured `δ`.
4. A *provenance-sensitive repair witness set* listing what would need to be acquired for an otherwise prohibited promotion. The current Prolog four-obligation list is a **candidate requirement set, not a proof of global minimality or optimality**.
5. Rust canonical executable plus Lean proof of the mathematical fragment and Prolog dependency challenge, with independent source-specific reproducibility receipts. Cross-paper pooled results only in genuinely harmonized units.

## 5. Falsifiers / opening gates

4.91 should **not** open as a claimed novel scientific method merely because MQR-4.90 independently reproduced AUC and demonstrated the known background-reference effect.

- **PASS**: published raw external AUC 10/10 and source fold AUC 12/12 re-evaluated.
- **PASS**: 10 fixed-`f), fixed-`P+) source reference-only counterfactual re-evaluations, with an exact verified mixture identity.
- **PASS**: Rust/Lean/Prolog typed nonpromotion and minimal-witness candidate gate, four-court run 37729126873 PASS.
- **HOLD**: true common scoring comparator between original CV fold-fitted `f_fold) and original externally deployed `f_final), across the same target positive and negative populations.
- **HOLD**: empirical upper bound for target-reference negative distribution distance, *not* an arbitrary TV sensitivity parameter.
- **HOLD**: source-level dependence/covariance handling, interval calibration, and at least two independently sourced article families under a comparable estimand.
- **HOLD**: evidence that the proposed repair compiler yields a new testable characterization or method improvement beyond established fixed-background comparisons and transportability tools.

**Next MQR-4.90 P9**: reconstruct fold-specific Maxent predictors from published `.lambdas` and available environmental grids at the target region, or prove that such fixed-target scoring is not recoverable from archived data; then directly test common scoring functionals with read-only source/materialization protocols. Keep the signed same-design cross-study meta-analytic effect on HOLD until genuinely admitted.

**No MQR-4.91 Notion page should be created by this precommit alone.** Maintain this as a candidate in MQR-4.90 and in GitHub docs until the independent 4.90 source/novelty court permits promotion.
