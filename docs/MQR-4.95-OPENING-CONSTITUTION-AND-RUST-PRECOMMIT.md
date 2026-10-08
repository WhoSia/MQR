# MQR-4.95 — Independent Calibration Witnesses, Spatially Dependent Sampling & the Identifiability of Informative Target-Risk Bounds

**Name author-confirmed 2026-10-09.** **State:** OPEN / RUST-NATIVE CLAIM CONTRACT + REAL TARGET SITE AUDIT PENDING. One canonical MQR Notion Lab and GitHub MAIN_ONLY.

## Lock

4.94 mathematically proved sharp finite-target binary label-loss interval extremes but yielded a broad interval for a fixed Serov target; it also found source-risk ranking sensitivity to geographic validation. 4.95 will address **which audited target labels can provably contract finite-frame uncertainty** and whether a claimed *independent* calibration source is admissible. One paper root is not transformed into many independent studies by disjoint rows, SHA seeds or programming languages. **Do not claim general population inference or calibration transfer based on one paper.**

## Genuine predecessor and competing science

Serov 2026 original author data from original Git commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`; `datasets/species/anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`. This is used only as **same-root concrete target audit**, not a new independent calibration publisher root. External distinct-root label calibration remains `EXTERNAL_WITNESS_UNAVAILABLE_HOLD` absent an authenticated, cross-matched source.

Prior art: Horvitz–Thompson design-weighted totals depend on known nonzero inclusion probabilities; their design variance includes joint inclusion probabilities. See Thompson (2012), DOI 10.1002/9781118162934.ch6; Aronow & Samii (2013), `Variance estimation for the Horvitz-Thompson estimator`, *Survey Methodology*; spatial sampling literature on GRTS/spsurvey; Roberts et al (2017), DOI 10.1111/ecog.02881. Do not claim source-root graph checking, missing-label bounds or spatial-stratified audits are novel inventions.

## Executable mathematical court, 100% Rust

Use std-only Rust crate. Download *immutable* source publisher CSV from commit and assert `git hash-object` equals pinned original SHA1 before Rust parsing. For diagnostic simplicity use 2013–2024 original complete BIO cases, original physical lat/long (not notebook swapped names), one row per 6dp geographic site determined by **stable FNV-1a hash**. This defines a NEW explicitly MQR-designed sample, not the 4.93/4.94 SHA-selected subjects, and previous exact risk numbers must NOT be claimed reproduced. Longitude cutoff 24.720692° and 25.278482° (4.93 source-only data audit). WEST hash-ranked first512 model training, next64 source validation; EAST first64 target. All site sets disjoint. This experiment requires a new original-data predictor fully implemented in Rust: source-only 19BIO standardization + fixed-step logistic regression (not original author fitted sklearn model). Its purpose is to construct nonconstant fixed target probability scores, not to compete with source published predictors or models. Pin iterations, learning rate and regularization constants in code and don't tune to audit outcomes.

**Strict target seal:** first parse original CSV without reading `presence`; later read only source-selected FIT/G labels for fitting; compute all 64 target scores, audit strategies and a priori identified bounds with target labels still unparsed. Only at the end, independently re-read 64 fixed target site labels, compute realized oracle and update sharp finite-site loss envelopes.

For each target score p_i in [1e-6,1-1e-6], define a_i=-log(1-p_i), b_i=-log(p_i), w_i=|b_i-a_i|. Unknown labels on target U imply sharp [sum min(a_i,b_i),sum max(a_i,b_i)]/n convex-hull extremes. For a **specified observed audit set A** with verified actual labels, extremes are [sum_A loss_i + sum_U min_i, sum_A loss_i + sum_U max_i]/n. The exact width is `sum_U w_i/n`. Thus observing site i reduces width by **w_i/n regardless of the audited label**. For k equal-cost audited sites, choosing largest w_i gives minimum width for the fixed finite target score vector (simple exchange argument); this is elementary finite combinatorial design, **not** a new statistical inference or independent witness discovery. A selected audit site remains *same Serov publisher root*, even if geographically distinct.

Freeze three label selection strategies BEFORE opening any EAST target Y:
1. Fixed seed stable-hash pseudo-random audit ordering (a deterministic permutation, NOT a demonstrated physically randomized probability sample). Prefix budgets k in 0,4,8,16,32,64.
2. Highest w_i first: oracle-independent score-width targeting. This deterministic design gives zero inclusion chance to some sites, so it is not a valid HT population design.
3. Geographic latitude-quartile-balanced high-w selection: sort fixed target sites by lat, group into four equal-size quartile bands (16 sites each), rank sites within each band by w; cyclically select one from each band until k sites. This is a **coverage-aware deterministic audit**, not genuine spatial independence or a probability-sampling confidence interval.

In Rust, numerical code and tests MUST verify (i) all strategies nested in budget k, (ii) width monotone under actual audited labels, (iii) realized 64-label oracle always inside every interval, (iv) width identity to 1e-10, (v) top-w strategy attains smallest possible k-site width among these deterministic strategies (not a universal budget-optimal cluster-inference estimator), (vi) k=64 reaches exact target oracle risk, (vii) explicit adversarial worlds with same observed audit labels and unchanged target X attain both remaining extrema, (viii) non-matched roots cannot be promoted as independent target calibration.

## Two-axis evidence authorization

**Axis A: finite-target direct observation**: authenticated target labels for exactly the matched fixed target site IDs narrow the finite-frame realized-loss interval even if originating from the same study. No independent-publication inference.

**Axis B: independent publication root and transport**: source-root distinctness, original frame/site matching, actual label custody, nonadaptive selection, and legitimate claim scope are needed before upgrading to **external calibration witness**. Source-root difference ALONE is not enough. A structurally typed `SameRoot` witness must be rejected for `independent` promotion; an unattested URL/root string is also rejected. No actual external root has yet been granted the external-witness type.

**Axis C: design-based uncertainty**: if first-order inclusion probabilities or appropriate second-order probability model is absent, reject Horvitz–Thompson unbiased-variance/coverage conclusions. The fixed hash and deterministic score optimization are useful for **finite target auditing**, not a random-design CI or generalization mechanism.

## Stop rule

A successful CI + full original-data receipt with material interval contraction and sharp-bounds verifier authorizes `SOURCE-CONTACT PASS / RUST INTERVAL PASS / EXTERNAL INDEPENDENCE HOLD / POPULATION INFERENCE HOLD`. This may support bounded 4.95 closure if everything is recorded precisely in canonical Notion, Drive and GitHub. Any source hash mismatch or label leakage means scientific HOLD and retained failure. Do not conceal the absence of an actual independent-root paper. No 4.96 automatic opening.
