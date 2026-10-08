# MQR 4.92 — First Independent Source, Real-Data Risk and Claim-Contract Court
**Date:** 2026-10-08.
**Version state:** `OPEN / TITLE CONFIRMED / FIRST INDEPENDENT SOURCE PARTIAL EMPIRICAL PASS / METHOD NOVELTY HOLD`.

Full formal title: **MQR-4.92 — Cross-Study Evaluation Contracts, Spatial Prediction–Performance Discordance, Source-Root Dependence & Falsifiable Evidence-Repair Benchmarks**. Author confirmed verbatim.

This document concerns ONE continuous MQR 4.92 research version; it is a GitHub source artifact, NOT a separate Notion Lab, version page, folder, or a newly opened version.

## I. Genuine independent source identity

Primary distinct publication: Serov, Koldasbayeva & Zaytsev (2026), *Kernel mean matching enhances risk estimation under spatial distribution shifts*, `Scientific Reports` DOI **10.1038/s41598-026-36740-7**. Unlike the Matsui 2026 *Ecology and Evolution* source that supplied the ten 4.91 AUC targets, Serov is an independent paper root and estimates **risk / error**, not source-matched rank-AUC. The article's former public repo pointer `awesomeslayer/Importance-reweighting` now redirects to **`egorser0v/Importance-reweighting`**. GitHub canonical source frozen to original commit **`46c4d011c9f0cd0614c08e7edb68ac2491f659c8`** (2025-11-21). The source tree has author-defined executable risk estimators, a dataset notebook, eight plant CSVs and cell spatial data. Repository `pyproject.toml` still refers to legacy `awesomeslayer/Spatial_Errors`; code/repo URL text by itself is not an immutable study-root identifier.

Original code files are **verified by Git blob SHA** before execution. Essential `source/estimations.py` blob is `9ce9a0c4639bdce4faace03a4b9236e92aa0f446`; frozen original source functions `MCE`, `KMM_error`, `kernel_mean_matching`, `compute_rbf`, `adjust_sigma` were executed unaltered via AST loading from pinned source; original KMM uses CVXOPT quadratic programming. The code is **not copied into MQR repository**; runtime download is checked against the original Git blob.

**Synthetic numerical smoke replay:** `experiments/mqr-4.92/serov_author_function_replay.py`, CI **37793832383 SUCCESS**. Original function MCE source risk 0.4668705361, KMM-reweighted risk 0.3127783592, synthetic target oracle 0.5439649085, where KMM performed worse than NW on THIS separately designed fixed synthetic fixture. The KMM output exactly matches independently computed original QP-weighted source loss and original MCE matches means; not an author-table replication, not evidence of general superiority/inferiority.

## II. Source specimen and source-selection validity

Frozen original plant CSV `datasets/species/oxalis.csv` Git blob **`b083688856e2cc8376df9e83cca42160450f469d`** has **7,507 rows × 23 columns**, with `lat,long,presence,year,bio1…bio19`; observed `presence` was **0 in all 7,507 rows**. The author notebook `notebooks/datasets.ipynb` (blob `5d9dc434b2bf7d070f44501b2e97f8ce3abd9ec0`) **comments out `oxalis.csv`** in the active species dictionary. Therefore using this particular CSV for a binary class-supervised cross-study experiment would be unfounded. It is NOT Matsui's Oxalis latifolia sample root merely because of the common “oxalis” string.

The original active notebook species CSVs were independently verified by original SHA and audited on CI **37794756586 SUCCESS**:
- `anemone.csv`, blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`: **29,543** rows; label0=11,166 and label1=18,377.
- `caltha.csv`, blob `48cb935dbfb7c05c07a3919e38b26f46530f2237`: **25,233** rows; label0=9,200 and label1=16,033.
- `tussilago.csv`, blob `d0b5f44dea32e80a148d501b91682c941b63551b`: **45,683** rows; label0=14,883 and label1=30,800.

The source notebook uses these variables in a year-based selection and employs class-handling/selection criteria; the code contains a noteworthy coordinate field rename `lat → decimalLongitude`, `long → decimalLatitude`. Treat this as a **source-axis semantic REVIEW FLAG**, not proof of published result errors until actual coordinate use is traced. These source CSVs are NOT necessarily independent species effects; same paper, shared code/source context.

Crucial joint source audit **37795655846 SUCCESS**: For all three active species, original 2000–2012 COMPLETE-CASE records (finite 19 bioclimates, valid binary label) have **only `presence=1`**, and original complete-case `presence=0` begins in 2013. In Anemone, 2000–2012 contains 758 complete climate+label rows but **zero negative class**. The raw population includes earlier and later data, but model admissibility depends on `year × label × missingness`, not the raw row count alone. This finding is a source-selection/estimand contract hazard; its cause (collector history, deliberate resampling, preprocessing) is NOT identified by this audit.

## III. Transparent real original-data pilot and revisions

Researcher-authored experimental design on genuine ORIGINAL source `anemone.csv` using original publisher risk code, but **NOT** original article's published experiment. Historical failed attempts are preserved:
1. Planned 2000–2012 fitted source sample 1200 fails for only 758 complete original cases; no risk estimated (CI 37795093226 FAILURE).
2. Revised to 512 on same original 2000–2012 fit slice fails because every original complete case belongs to class1; no model can fit a binary classifier (CI 37795516278 FAILURE).
3. **Only after both source-only gates, before any risk result**, frozen new design: training years 2013–2018, original source validation 2019–2020, external *temporal* evaluation 2021–2024. Outcome-blind deterministic row hash selection, capped **512 / 64 / 64**, fully observed original 19 bio feature columns, source-only fit scaler, logistic classifier C=1.0. Target labels NEVER used in training, weight selection or loss estimator; available ONLY as post-hoc target error oracle. Because this split is calendar-based, it is NOT evidence of any spatial deployment shift.

In source root all original eligible complete labelled source rows by third fixed temporal group are **fit 1,100; source validation 738; target evaluation 1,068**, respectively; deterministic capped selection `512/64/64`. Original observations selected as positives (fit,source,target) = **223, 42, 47**. This is not a representative random sample of all ecological environments and 19-feature completeness can be selection-biased.

Results, unchanged upon descriptive weight-inventory rerun **37796041048 SUCCESS**, experimental controls `experiments/mqr-4.92/serov_anemone_temporal_risk_pilot.py`:
- Target held-out oracle average log-loss = **0.9844141078434838**.
- Published original MCE/NW source-heldout risk estimator = **0.9084266190158496**, absolute target oracle gap **0.07598748882763418**.
- Published original KMM source-heldout reweighted risk estimator = **0.4249084025150559**, absolute target oracle gap **0.5595057053284279**.
- Reweighted source loss equals the independent dot product of published KMM weights and original source losses (numerical verification).
- Source heldout 64 items: **KMM effective weighted sample size ≈5.4858**, weight range **5.91187765×10⁻⁷ to 8.5981547**. Weight concentration is a plausible instability mechanism, **not** proved causal by this single pilot.

**Scientific interpretation:** KMM estimate is worse than NW in this *one* predeclared small real-data temporal split. This is an honest negative instance against universal algorithm dominance, but does **not** contradict Serov's published aggregate results because predictor, sample selection, data split, spatial assumptions and risk-estimand design differ; it is not a reproduction of Serov's paper numbers. No iid CIs or independent-source meta-analysis may be inferred. In particular, a user can calculate target loss here only because the original publication provides target labels; target-label access was withheld from the estimator design and permitted only for evaluation.

## IV. Cross-source evidence contract regression (CONSTRUCTED benchmark)

Python `experiments/mqr-4.92/source_contract_adversarial_benchmark.py`, CI **37794048359 SUCCESS**, test set 20 source-schema-grounded but **researcher-constructed perturbations**: 4 stipulated admissible contrasts and 16 deliberately non-comparable. A weak filename+metric guard yielded **15 false admissions**, a somewhat stronger study+target metadata guard **12 false admissions**, and the restricted typed comparison guard **0 false admissions / 0 false rejections** on THESE stipulated rules. This is a code regression/self-check with known labels, **not independent evidence that MQR outperforms existing published source auditing or manual curation**; baselines were intentionally limited. Full case-level receipts are in the CI artifact, including source/target reference, metric, model root, mask, coordinate source, selection screen and target-label leakage mutations.

Critical cross-paper nonadmission: Matsui rank-AUC and Serov target-loss risk **are different mathematical objects**; matching the token `oxalis` or a nominal source/target label does not establish shared data population, common evaluation distributions, or commensurable estimands. All AUC/risk pooling remains rejected.

## V. Current scientific verdict and next run

**PASS:** independent true source Git root discovered, frozen original code and real active datasets actually hash-verified, original risk functions executed numerically on synthetic AND source-original active plant data, source class/period/complete-case selection failures exposed, typed benchmark regression executed.

**HOLD:** paper's full original experimental MAPE/KMM result replication; independent second *publication-level* result reproduced; objective external method superiority; spatial holdout, spatial dependence uncertainty; completeness/minimality of any evidence repair proof; significant out-of-distribution risk correction; error-correctness improvement beyond human/file/numeric baselines.

**Actionable next within 4.92:** Reconstruct exactly the authors' study active-notebook preprocessing including year/class screens without relabeling; compare four estimators under original source trials with prespecified class balance and actual space/time split; benchmark contract rule against a serious rival and blinded original source human audit. Record costs and false admission rates without optimistic tuning. Check coordinate-name inversion by geographic knowledge and downstream use before assigning defect severity. Preserve one MQR Notion canonical root, no version subpages or Labs rows; do not open 4.93.

## VI. Permanent raw source receipts (Google Drive 02_ANALYSIS_SAFE)

Both the GitHub human-authored source code and actual CI artifacts are preserved. Original code, raw plant CSV and notebook files remain in the pinned author repository; these small receipts hold hashes, command output and JSON audit results, not full hundreds-of-MB original research datasets.

- Author function risk source smoke CI 37793832383 → Drive file `1_nELQEPNIq8XnXhLm5J0mXi93eaobaTS` (1,293 B).
- Two-root constructed contract regression CI 37794048359 → Drive file `1EPzX88O4b_wTB-RalQWAxp7Ya7z1Lm_b` (1,658 B).
- Original active species year×label×BIO-completeness CI 37795655846 → Drive file `1VWZSq4qNPLoYiVBu11pweKqLbzTihO0p` (4,593 B).
- Anemone actual original risk function year-split pilot and reweighting diagnostics CI 37796041048 → Drive file `15douq9UXvqf7b29-vaEK1JP4n9LmvoL1` (2,079 B).

Each file's name, size, ZIP MIME type and existing `02_ANALYSIS_SAFE` parent ID `1szynM5kvA7sMExkaJ5sjvwrO3HPaXT1X` were independently confirmed by Drive metadata readback after upload. No original publisher files renamed, copied or modified; no new MQR Notion Lab or child was created.
