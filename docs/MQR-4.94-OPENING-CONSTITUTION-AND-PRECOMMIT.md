# MQR-4.94 — Frozen Opening Constitution

**Author-confirmed full title:** MQR-4.94 — Spatial Dependence, Conditional-Loss Shift, Partial Target-Risk Identification & Geographic Holdout Robustness.
**State:** OPEN / PRE-OUTCOME 4.94 DIAGNOSTIC GRID FROZEN.
**Predecessor:** MQR-4.93 CLOSED, source-original geographic 512/64/64 site-level risk PASS-DESCRIPTIVE, dependence/identification HOLD.

## Epistemic timing and originality
The 4.93 target outcome is already known, so this 4.94 study is a retrospective follow-up; freezing a new set of calculations now does **not** confer an independent blind experiment. All five geographic variants share one Serov original-paper root; no independent-publication replication, method novelty, causal conditional shift, population inference or spatial iid confidence interval is licensed. Roberts et al. (2017), DOI 10.1111/ecog.02881, is explicit prior art for blocked spatial validation.

## Immutable source contract
Serov 2026 original `egorser0v/Importance-reweighting` Git commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`; `datasets/species/anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`; original `source/estimations.py` Git blob `9ce9a0c4639bdce4faace03a4b9236e92aa0f446`. Preserve original data and author MCE, KMM_error, kernel_mean_matching functions. Original 4.93 algorithm/row hashes/6-decimal site key preserved.

## Frozen five-contract grid
All original 2013–2024 rows with finite actual coordinates and 19 BIO features, no labels used for frame selection or rank. For four variants select west source sites longitude <= eligible-row quantile 0.40 or 0.50, east target sites longitude >= eligible-row quantile 0.75 or 0.85; use all four combinations, with central longitude buffer excluded. Freeze original 4.93 SHA256 site dedup/ranking, 512 unique west FIT sites, next 64 west G validation sites, 64 unique east P target sites; no fit-source-target exact site overlaps. Source-only scaler and logistic regression C=1.0, max_iter 2000, random_state=493, 19 BIO, KMM B=10. Compare original NW/MCE and KMM estimates with the target oracle; show all outcomes and feasibility failures.

Fifth variant holds west q50/east q75 fixed but separates G geographically by latitude: choose eligible unique WEST sites with latitude >= west-site 80th percentile for G; west sites <=65th percentile for FIT; middle latitude excluded. SHA rank FIT512/G64 from each non-overlapping area, target EAST64 as q75 first64 sites. If not feasible, record infeasibility without tuning.

**Label seal:** prior 4.93 results known. Nevertheless this computation must choose all five site cohorts, fit models, calculate predictions and original source-only risk estimates and theoretical bounds BEFORE reading any selected target labels for its own posthoc oracle evaluation. No outcome-adaptive sample replacement.

For each variant report site counts, source-FIT-to-G nearest-distance minimum/median and fractions within 100m, 1km and 5km, source FIT+G to P minimum Haversine distance, class/year balance posthoc, original NW and KMM risks, KMM weight ESS, target oracle, absolute oracle gaps and which source estimator is closer. Reproduce the exact original 4.93 q50/east q75 baseline numbers (0.4587061383023344, 0.41023871824198993, 0.7495034100861271) within 1e-9 or fail.

## Sharp target-specific partial identification
For the 64 fixed target predicted probabilities `p_i`, let `a_i=-log(1-p_i)`, `b_i=-log(p_i)`. If all target labels are missing, the **sharp extrema over binary target-label assignments** are `Llo=mean(min(a_i,b_i))` and `Lhi=mean(max(a_i,b_i))`. The attainable finite sample risk set is generally discrete, with **sharp interval convex hull** [Llo,Lhi]; two constructed assignments attain its extrema with identical unlabeled target features.

After independent source risk/label-bound calculations, permit posthoc opening of target labels and k positives. An additional retrospectively prevalence-conditioned sharp interval has `d_i=b_i-a_i`, `base=sum(a_i)`; its min and max add the sums of the smallest and largest k values of d_i, divided by n. k is NOT available for unlabeled deployment. Include an exhaustive combinatorial verifier for n=6, k=3; its PASS is an engineering check, not theorem novelty.

**Conditional-calibration sensitivity:** Given an explicitly unverified assumption `P_target(Y=1|x_i)` lies within ±η of the fitted source model's predicted p_i, η fixed at 0, 0.1, 0.25, 0.5, 1, bound the expected target risk by choosing lower/upper q_i based on sign d_i. These are expected-risk sensitivity bands, **not realized-sample predictive intervals or confidence intervals**, and the calibration transfer premise is not source-identified. Compare but never assert oracle-band coverage as proof of assumption soundness.

## Stop conditions
Complete four fixed geography variants plus one blocked-G rival and exact small-n sharp-bound checks, preserve failures, CI and Drive receipts; then bounded PASS/CLOSE, NEGATIVE/CLOSE or HOLD/CLOSE according to execution and scientific admissibility. No endless version inflation or novel risk algorithm claim. Strict one MQR Notion Lab, one canonical page `3c8ef561cf92815693b6fcf6de9955f7`; GitHub MAIN_ONLY, human-authored commits; Actions read-only and no bot commits/push.
