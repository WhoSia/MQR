# MQR 4.93 — Final Bounded Scientific Closeout: Coordinate-Semantics Audit and Real Geographic Site-Holdout

**Date:** 2026-10-09 (KST).
**Author-confirmed name:** **MQR-4.93 — Spatial Holdout Admissibility, Coordinate Semantics & Target-Risk Identifiability**.

**Final scientific verdict:**
`CLOSED / ORIGINAL COORDINATE SEMANTICS PASS-BOUNDED / GEOGRAPHIC ORIGINAL-DATA TARGET-RISK PASS-DESCRIPTIVE / SPATIAL INDEPENDENCE AND CAUSAL IDENTIFICATION HOLD / METHOD NOVELTY HOLD`.

This version closes after one precommitted source audit and one genuinely geographic source/target split experiment, not after demonstrating a new universal risk-estimation theory. This is a **file in GitHub** and a section in ONE existing MQR Notion Lab—not permission to create a new Notion Lab, child page, folder or an automatically opened successor.

## I. Historical role and faithful external-source identification

Founding MQR observation: a digital/signal/instrument representation determines only distinctions licensed by its actual measurement mapping, not all underlying properties. 4.91 verified ten original Matsui external AUC cases and 40 within-one-paper fold/final matched contrasts but did not verify source-original spatial raster map comparisons (Zenodo 502/503/504). 4.92 independently verified original Serov functions and data and observed a feature mean balance–target loss discordance on a one-split **temporal**, not spatial, original-data pilot (CLOSED; method novelty HOLD).

4.93 used the **same author-published Serov root**, not a third independent article. Serov, Koldasbayeva & Zaytsev (2026), *Kernel mean matching enhances risk estimation under spatial distribution shifts*, Scientific Reports 16:6921, DOI `10.1038/s41598-026-36740-7`, describes ecological source/target splitting by early and late years to obtain differences in spatial clustering. The 4.93 direct WEST–EAST spatial split is a **new MQR-designed diagnostic**, not original published Serov evaluation or full reproduction of its MAPE claims.

Frozen original publication repo: `egorser0v/Importance-reweighting`, source commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`. Original active `datasets/species/anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`; original estimator `source/estimations.py` blob `9ce9a0c4639bdce4faace03a4b9236e92aa0f446`; original notebook `notebooks/datasets.ipynb` blob `5d9dc434b2bf7d070f44501b2e97f8ce3abd9ec0`.

## II. Gate 0 — Evidence-admissible physical coordinate semantics

Original data-only, source-hash-verifying `experiments/mqr-4.93/serov_coordinate_gate.py`, CI **[37802338677](https://github.com/WhoSia/MQR/actions/runs/37802338677)** SUCCESS, log states `SOURCE_COORDINATE_SEMANTICS_PLAUSIBLE_PASS_WITH_NOTEBOOK_REMAP_FLAG`. No predictor fitting or target risk used in this gate; only WEST source class feasibility was inspected, EAST target labels unopened.

- Frozen nonlabel-filtered analysis frame: finite raw latitude, longitude and all 19 bio1–bio19 features for years 2013–2024 = **2,905 original rows**, **1,841 distinct 6-decimal geographic sites**; **1,386 rows on repeated sites**, with up to **71** rows sharing one site.
- Original `lat` = **59.774082–66.666254°N**, `long` = **20.839486–30.432037°E**. 100% of that frame fits a broad external Finland envelope with raw labels as-is; 0% fits when swapped. This strongly favors raw CSV `lat` physical latitude and `long` physical longitude **at declared plausibility scope**. No record-level independent GBIF geocoding was performed.
- Original notebook text transforms `lat → decimalLongitude`, `long → decimalLatitude`, and then renames these to `Longitude`/`Latitude`. Therefore names downstream can indicate wrong coordinate roles. No blanket claim that published spatial cluster values or experiment outcomes are wrong: a simultaneous coordinate-axis permutation does not alter Euclidean distances, and an ordinary relabeling need not modify numerical arrays. An axis-specific geographic bounding predicate **would** depend on the correct semantic coordinates.
- Longitude frame median **24.720692°E** and q75 **25.278482°E**; WEST <= median = **1,460 original rows**, EAST >= q75 = **727 original rows**, excluded buffer = **718**; 0.55779° longitude threshold gap. WEST source labels 574 zero and 886 one (not used to pick target). EAST target labels remained withheld.
- Gate0 artifact **11561712571**, verified Drive `02_ANALYSIS_SAFE` ZIP id `1b9qlVBjWmbMa3FvkLtmmORC67wj4nyCn` (2,097 bytes).

## III. Outcome-frozen spatial source/target protocol

After Gate0, but **before any new spatial experiment loss or target labels**, file `docs/MQR-4.93-PREOUTCOME-GEOSITE-RISK-PRESEAL.md` fixed site-level selection based only on original coordinates/features/year and deterministic SHA256. The immutable source-commit, country-consistent raw latitude/longitude and year 2013–2024 plus finite BIO case screen are the input. A site is `(round(lat,6),round(lon,6))`. Select precisely ONE record per coordinate by fixed row SHA256, rank WEST/EAST sites separately using a frozen salt. Select WEST first 512 distinct sites FIT, next 64 distinct sites source validation G, and EAST first 64 distinct sites target P. The middle longitude quantile region is excluded. **Presence target labels are not read** until all site choice, predictor fitting, weight estimation and source-only risk values are computed. No outcome-adaptive split retries occurred.

FIT model is LogisticRegression(C=1.0,max_iter=2000,random_state=493) with FIT-only StandardScaler for the original 19 BIO input features; neither latitude nor longitude is used directly as a predictor. Author's unmodified `MCE`, `KMM_error`, `kernel_mean_matching` source functions applied to source validation log-loss and unlabeled target X with Gaussian/RBF KMM `B=10`. Original risk functions are numerically cross-checked against an independent source loss mean and a direct KMM weighted-loss dot product. This is an implemented numerical self-check, **not** a second research root.

Source code `experiments/mqr-4.93/serov_geosite_original_risk.py`; actual CI **[37802918396](https://github.com/WhoSia/MQR/actions/runs/37802918396)** SUCCESS, output `MQR493_GEOSITE_RISK=PASS`. Original derived JSON & log artifact **11561452801**, Drive existing `02_ANALYSIS_SAFE` file `11o1mRTYMwGmTXXblZgAYxNp3UvHjZHY9` (3,069 bytes), metadata verified.

Geographic audit:
- Available unique WEST source sites **988**, EAST target sites **411**.
- Exactly **512/64/64** unique chosen sites; identical selected 6-decimal coordinate overlap = 0.
- Minimum selected source FIT+G to EAST target Haversine distance **32.2667508574 km**.
- Minimum source FIT-to-source G separation **0.01861399446 km** (~19m). The WEST source holdout is **not** spatially independent in any strong sense and may inherit local autocorrelation; while source-vs-target geographic separation is real, neither iid-ness nor target-population representativeness is demonstrated.

## IV. Actual target risk and competing descriptions

| Original estimator | Source-based estimated log-loss | Target post-hoc oracle absolute gap |
|---|---:|---:|
| NW / MCE original source | **0.4587061383023344** | **0.29079727178379267** |
| Original author KMM, weights sum/64 formula | **0.41023871824198993** | **0.33926469184413716** |
| Actual held-out target mean log-loss (posthoc) | **0.7495034100861271** | 0 |

KMM weights: sum **59.99437187360199** for 64 source-validation observations (mean **0.9374120605250311**), ESS **33.4242590428**, maximum **2.9011776866**, minimum **4.020556e-6**, top-five share **0.23612256**. The original KMM estimator uses `sum(w_i * source_loss_i)/64` and retains this **unnormalized** source function by design.

**Analytical diagnostic only, never misreported as original author KMM:** Dividing the same weighted source-loss sum by `sum(w)` instead of 64 would yield risk **0.4376290166484748**, gap **0.3118743934376523**. Even this straightforward normalization does not outperform original NW gap **0.29079727178379267** on the fixed 64+64 specimens. No new model was trained and no alternative was optimized against the oracle to obtain this calculation. It is an algebraic normalization sensitivity, not a validated novel risk estimator.

**Target labels were revealed only for posthoc oracle.** Source G positive proportion **51/64 = 79.6875%**, negative 13; target P positive **37/64 = 57.8125%**, negative 27: a descriptive **−21.875 percentage-point** target–source positive-rate difference. The target site sample comes from a different geographic and year composition; this is evidence of selection/composition discordance, **not proof** that conditional `P(Y|X)` changed, nor identified class-shift causal mechanism.

The previous 4.92 temporal sample yielded KMM ESS~5.49 and a large KMM oracle gap. This new geographic sample has ESS~33.42 yet NW remains closer to the target oracle. Therefore extraordinarily low ESS like 5.49 is not **necessary** for KMM to be worse on this single contrast. It does not follow that ESS is irrelevant or that KMM must fail generally.

## V. Mathematical identification limitation and rival audit

For any model `f`, loss `L`, source `P` and target `Q`, define `m_P(x)=E_P[L|X=x]`, `m_Q(x)=E_Q[L|X=x]` and normalized weighted-source marginal `P_X^w`. Under integrability:

`R_Q(f)-R_{P,w}(f)=E_{Q_X}[m_Q(X)-m_P(X)]+E_{Q_X}[m_P(X)]-E_{P_X^w}[m_P(X)]`.

This separates conditional-loss transport mismatch from residual covariate matching, but **neither component is causally identified by this finite one-split experiment**. Spatial proximity (source FIT-to-G 19 m), composition shift, class-conditional drift, target feature support and source label noise remain live rival explanations. No cell-level iid confidence interval, population spatial generalization claim, original map rank correlation, root-independent result aggregation or novel universal theorem is admitted.

A serious comparator is the direct **labeled target oracle** for judging error (posthoc only); it cannot serve as the unlabeled risk estimator available for deployment. The original NW/MCE is an executable, serious simple benchmark. We have **not** benchmarked against all published estimator families (IW/classifier reweighting) under an identical original author-designed spatial split or blinded human review, so no method-superiority/novelty admission.

## VI. Verdict, failures and bounded stop

**PASS bounded:** Original coordinate/header semantics checked against source-pinned code, broad Finland plausibility, source site-duplication measured; new geographic target separate by minimum 32.27 km, one-record-per-site FIT/G/P, original source estimator function equality verified and target labels held until posthoc; actual risk gap and class composition reported with two Drive/CI receipts.

**HOLD:** Direct independent geocoding of individual locations, causal or published-model error due to notebook label inversion, strict spatiotemporal independence, conditional risk shift identification, reliable spatial population risk, full original Serov four-method MAPE study replication, actual Matsui original raster map correlation, serious 3+ estimator comparative method utility, independent publication-level root statistic, confidence intervals and methodological novelty.

**Reason for scientific bounded closure:** All three short precommitted stages (coordinate semantics, geographic heldout risk execution, critical identifiability audit) were completed at their bounded scope. Additional small resamplings or gratuitous polyglot code cannot turn one geographically partitioned published dataset into a novel generalizable algorithm. Follow-up needs a genuinely independent spatial field study/replicated geographic block collection, a strong published alternative comparison, or a formal theorem with substantive new falsifier—not merely one more version label.

**One canonical MQR Lab:** Notion page `3c8ef561cf92815693b6fcf6de9955f7`. All 4.93 text is an internal section, not another Lab row. `main` only; GitHub commits human-account authored and Actions permissions `contents: read` (no workflow commit/tag/push). Artifacts reside in existing Drive `02_ANALYSIS_SAFE`; initial failures and 4.91/4.92 holds are retained.
