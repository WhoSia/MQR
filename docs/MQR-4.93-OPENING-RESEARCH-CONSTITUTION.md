# MQR 4.93 — Opening Research Constitution

**Author-confirmed full formal name (2026-10-09):**
**MQR-4.93 — Spatial Holdout Admissibility, Coordinate Semantics & Target-Risk Identifiability**

**State:** `OPEN / P0 FORMAL / SOURCE-SEMANTICS GATE PRIOR TO EMPIRICAL RISK`.
**Predecessor:** MQR 4.92 `CLOSED / BOUNDED ORIGINAL-DATA TEMPORAL RISK–FEATURE-BALANCE DISCORDANCE / SPATIAL HOLD`, evidenced by `docs/MQR-4.92-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md`.
**One Lab:** All Notion research writing must update the SINGLE existing MQR page `3c8ef561cf92815693b6fcf6de9955f7`; no new version row, child page or folder. GitHub `main` only. Human-authored commits; GitHub Actions read-only and never commit/tag/push.

## Explanandum and prior-art boundary

Serov, Koldasbayeva & Zaytsev (2026), *Scientific Reports*, doi `10.1038/s41598-026-36740-7`, original commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8` studies spatial clustering using **early-vs-late temporal species source-target sampling** as well as other data. MQR 4.92 independently replayed original author functions on a **temporal** Anemone subset, finding KMM weighted BIO-mean mismatch proxy smaller but target risk estimate worse on that fixed subset. This is not a genuine geographic holdout, and an improved proxy does not identify predictive risk.

MQR 4.93 asks: **Can a geographically disjoint held-out target risk be scientifically evaluated on a genuine frozen original species source, given coordinate naming ambiguities, missingness and label sampling, withheld target labels, and a source/target shift that may invalidate the covariate-shift assumption?**

## Source roots and claim scope

Original publisher `egorser0v/Importance-reweighting`, author commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`. Original active `datasets/species/anemone.csv` immutable Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`; original `source/estimations.py` blob `9ce9a0c4639bdce4faace03a4b9236e92aa0f446`; original notebook `notebooks/datasets.ipynb` blob `5d9dc434b2bf7d070f44501b2e97f8ce3abd9ec0`. Caltha and Tussilago may act as source-internal support checks; they are NOT independent publication roots.

## Gate 0 — Coordinate and sampling semantics BEFORE outcome observation

1. Hash-check publisher raw bytes. Independently inspect `lat` and `long` bounds, per-axis Finland geographic feasibility and their correspondence with the notebook remap `lat → decimalLongitude`, `long → decimalLatitude`. The paper reports Finnish plant-occurrence study geography. The field-name reversal is a REVIEW FLAG; only joint raw-value/geographic/use evidence may support a scoped coordinate interpretation.
2. Count null/nonfinite/out-of-bounds coordinates, duplicate coordinate locations, years, missing 19 BIO features, source label class support and spatial quantile-group size. Class counts may be used only to judge *whether* a prespecified design is feasible; never to select a desired result. Explicitly separate feature-complete and coordinate-valid sampling frames.
3. **Stop if** geographic interpretation remains ambiguous (`COORDINATE_SEMANTICS_HOLD`); too few accessible valid coordinates/eligible binary source labels (`SPATIAL_HOLDOUT_INFEASIBLE`); raw hash unavailable (`SOURCE_HOLD`). No spatial-risk claims may be made from a failed gate. Gate0 code must not train, weight or compute target outcomes.
4. Audit output/CI receipt shall report not just a Boolean PASS but the actual coordinate ranges, interpretation scores and failure counts, with fallback `HOLD` allowed.

## Gate 1 — Frozen geographical risk test (eligible only after Gate 0)

A downstream experiment must register before any target-loss access: deterministic **longitude quantile** partition over the original fully valid source frame, west source region `longitude <= median`, east target region `longitude >= 75th percentile`, central 50–75% excluded as a spatial buffer. Geographic disjointness alone is not independence: report separation, coordinate duplicates, spatial clustering and sampling overlap. Use 2013–2024 complete-case original records, include `bio1…bio19` as features, never leak longitude/year/target label into predictor unless expressly predeclared. No retrofitting geographic split after seeing source or target risk. Deterministic source-only stratified fit/source-validation rule must be frozen, label classes need at least one of each in source fit, and actual source and target cap/sample sizes precommitted. Target-label selection is prohibited; target labels used only after prediction+reweighting to compute oracle. If the exact frozen split is infeasible, report negative not redesign.

Run original author unmodified MCE/NW and KMM functions on source validation losses and unlabeled target covariates, compare to post-hoc target oracle log-loss and ESS; report standardization/selection, class composition, count and geographic separations. The resulting bounded point-level test is NOT published Serov authors' exact table, nor a publisher continuous map/raster or population-level spatial transport theorem.

## Gate 2 — Rival explanations and termination

Test dependence of claim on: (i) coordinate field semantics, (ii) source vs target label/missingness/time composition, (iii) covariate distribution mismatch and overlap, (iv) conditional loss changes under shift, and (v) reweighting sample concentration. A point estimate does not attribute causality; no iid CI for spatial points. No general KMM failure/advantage or MQR novelty promotion. Source code reference remains Python for exact upstream fidelity; Rust can enforce claim-typed admission and Lean/Prolog only when an actual theorem or dependent source-graph warrants their cost.

**Stop rule for short version:** `PASS-BOUNDED/CLOSE` for source-verified plausible geography, genuinely held-out spatial target, documented original-estimator numeric comparison and target post-hoc risk on a fixed protocol; `NEGATIVE/CLOSE` for structurally infeasible spatial split; `HOLD/CLOSE` for coordinate or source uncertainty. All failures/negative findings retained. A completed real geographic experiment does not automatically establish spatial-map correlation or independent-source confidence intervals. No successor opens automatically.

**Immutable statement:** The 4.92 previous target outcomes were already known before the present 4.93 study design. Any fresh geographical test may be geographically held out within Serov's data but cannot be described as independent *paper-level* confirmation.
