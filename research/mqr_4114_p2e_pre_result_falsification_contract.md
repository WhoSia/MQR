# MQR-4.114 P2-E — PRE-RESULT-ROW LOCK: CCQM-K11.2 Cross-Laboratory Rival Falsification Contract

**Status: FROZEN BEFORE INSPECTION OF INDIVIDUAL LABORATORY RESULT TABLES.** Source abstract/introduction and the historical 2.5% anchor/participant discordance were already known; this is **NOT** an outcome-blinded preregistration or a prospective experiment. Freeze timestamp: GitHub main commit; retain and disclose that it is source-aware, row-level pre-analysis. No changes to these criteria after inspecting numeric results; diagnostic additions must be clearly labeled post hoc.

**Original primary report:** Wise et al., *CCQM-K11.2 Determination of Glucose in Human Serum and CCQM-K12.2 Determination of Creatinine in Human Serum*, 2018, Metrologia 55 Tech. Suppl. 08012, DOI 10.1088/0026-1394/55/1A/08012. BIPM original 70-page PDF: https://www.bipm.org/documents/20126/44596658/CCQM-K11.2_and_12.2.pdf/1e39817b-940d-09a5-d098-651f65a2ab27 . Public source provides participant result summaries, uncertainty statements, assay descriptions, KCRV deliberation, NOT automatically raw instrument acquisitions or certified material-level traceability.

## Ontic target, source population, and fixed experimental unit

- **Primary:** CCQM-K11.2 *glucose mass fraction in the SAME distributed serum material*, an original participating institute one analytical result per institute, unit mg/g. If the paper reports multiple corrected/submitted results per institute, combine using the report's documented selection/combination policy; no duplicate institute or methods counted as independent unless explicit disjoint physical ancestry is validated.
- **Secondary (not pooled):** CCQM-K12.2 creatinine mass fraction in its distinct material, unit µg/g, same analysis only as mechanistic contrast. Do **not** treat glucose and creatinine as two measurements of the same measurand.
- Separate ORIGINAL PARTICIPANTS from AFTER-RESULT FOLLOW-UP REFERENCE LABORATORIES and intended original ANCHOR. Later recruits are never a truly prospective held-out dataset because they were specifically solicited after discordance. Explicitly mark if the anchor laboratory is also the pilot or coordinator and whether a reported value is included in a consensus KCRV.
- Source sampling/comparison design: serum aliquots from a distributed pool can be common material *class* yet not identical molecules or actual same aliquot; retain homogeneity/stability uncertainty. Multiple labs are different institutions, **not proven independent traceability chains**.

## Rival worlds, identification target and non-identifiability boundary

Observed institute summary `y_i = θ + b_common + b_family(i) + b_i + ε_i` with reported standard uncertainties `u_i`. 
- **R0 (strict published-uncertainty compatibility):** `b_family = b_i = 0`, zero correlation among laboratories' reported errors, their reported u_i are valid for this experiment. Unknown θ fitted by a weighted mean. `b_common` is observationally indistinguishable from θ on a single shared material; it cannot be refuted/detected by cross-sectional agreement or heterogeneity alone. The target is R0's *independent centered errors with stated uncertainty*, **not** the general no-common-bias universe.
- **R1 (family-dependent rival):** LC-MS vs GC-MS (or differently documented isotope dilution/derivatization paths) carry systematic shifts, with potentially shared reagent/metrological calibration, matrix or instrument-response assumptions. Report cross-family difference as a diagnosis only if valid source-tagged independent families are documented.
- **R2 (unknown anchor bias/reference ancestry):** putative anchor vs participant discordance may arise from anchor, participant, shared matrix, or uncertainty model. A consensus `KCRV` derived from tested outcomes is **not** an external independent ground truth and cannot validate R0 by regressing it against its own contributors.

Under any common additive shift c, `θ' = θ+c, b_common'=b_common−c` gives exactly the same y_i. **No scalar common-mode calibration error magnitude is identifiable from one material without a genuinely externally independent reference.** Even observed heterogeneity or method-specific disagreement cannot alone prove the *cause* is correlated calibration.

## Fixed numerical statistical gate, not adjusted to observed results

1. Source measurement rows must have the same measurand and same material; record reported numeric value, units, whether its uncertainty is standard or expanded and coverage factor; place a HOLD when the uncertainty convention is ambiguous. Use the source-reported institute combined result rather than alternative derived summaries that reuse the same data.
2. If at least 4 unambiguously distinct participant institute rows have finite positive **standard** uncertainties (or stated expanded U converted by explicit source k), compute:
   `w_i=1/u_i², μ=Σw_i y_i/Σw_i, Q=Σw_i(y_i−μ)²`; compare with chi-square(ν=n−1) 0.99 critical value, **alpha=0.01**, with degrees ν (heteroscedastic known uncertainties). Exact numerical critical-value table must be fixed in code prior to reading report rows. `Q>χ²_ν(.99)` -> **REJECT R0 CONDITIONAL**; otherwise **NOT REJECT**, NEVER 'certify independence'. If n<4 or u_i unusable -> **HOLD**.
3. Error correlation / same calibration ancestry are unverified, so even Q rejection is evidence against the joint model (zero family bias, independent centered correctly scaled uncertainties). It cannot uniquely attribute rejection to common bias, between-method correlation, error underestimation, matrix instability or reported variance omission. If same calibration source or materials are documented among participants, label **INDEPENDENCE_UNVERIFIED**, do not treat degrees of freedom as an empirically certified effective sample size.
4. Diagnostic **leave-one-institute-out** Q and source method family (LC vs GC) only after frozen primary is evaluated, always label DIAGNOSTIC/POST_HOC. Family contrast available only if 2+ eligible distinct institutes each and non-overlapping documented methods; compute weighted signed family difference and uncertainty as an indicator, **not a causal independence test**, and freeze threshold `abs(diff) > 3*sqrt(1/ΣwA+1/ΣwB)`. Label `FAMILY_CONTRAST_DIAGNOSTIC`; no inferential claim without covariance.
5. The final report's published KCRV, confidence/expanded uncertainties, Track C conversion, and time of reference laboratory addition are **sources to contrast**, not independent calibration truths. Don't count KCRV plus constituents as independent measurements; compute leave-one-out KCRV sensitivity if possible.
6. **No adaptation** of thresholds, row exclusions, core model or claims based on observed source values. Missingness/duplicates are reported as HOLD, not filtered to manufacture a PASS.

## Typed outcome labels

- `ROW_SUMMARIES_VERIFIED`: directly transcribed published institute results, uncertainty and source page, **not raw detector time series**.
- `R0_REJECT_CONDITIONAL` or `R0_NOT_REJECT_CONDITIONAL` or `R0_HOLD_DATA_DEFICIT`.
- `COMMON_MODE_BIAS_IDENTIFIED=NO` except under an externally witnessed identifiable reference contrast.
- `SOURCE_ANCESTRY_INDEPENDENT=HOLD` unless independently certified source and calibration genealogy materialized.
- `PROSPECTIVE_EXTERNAL_INTERVENTION=NOT_PERFORMED` (a follow-up lab reaction to discordance is not preregistered laboratory perturbation).
- `MQR_4114_STAGE=P2_E_ONLY`; do not open P3/P4, do not promote Real Lang 0.44.

**Source custody:** Source metadata and reported numerical results belong to authors and metrological institutions. Derived institute result rows may be indexed with exact report page and table; avoid redistributing the entire underlying 70-page report. Use only the amount necessary for reproducibility.
