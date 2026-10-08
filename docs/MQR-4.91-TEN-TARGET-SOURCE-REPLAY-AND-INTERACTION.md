# MQR 4.91 — Original Fold Models Across Ten External Targets

**Scientific state (2026-10-08):** Source reprojected 10/10 target cases; 40 source-reprojected original fold-to-final matched-target comparisons; descriptive fold-by-target interaction analyzed; typed evaluation guard PASS. **Not a signed spatial-CV optimism meta-analysis.** All ten target cases belong to ONE original Matsui 2026 publication and THREE calibrated species families.

## Primary scientific finding

Matsui (2026), *Ecology and Evolution*, original DOI 10.1002/ece3.73534 and correction DOI 10.1002/ece3.73828; publisher materials Zenodo 10.5281/zenodo.19970795. The original published fitted Maxent `.lambdas`, target environment rasters, geographic positive/source-reference-negative coordinate CSVs, and official Java Maxent 3.4.4 source were pinned and reconciled. Ten distinct original target-region final model score maps and four originally fitted CV fold model maps per target were used, without refitting on external test labels.

Exact technical read-only run **37786496173 SUCCESS**; fold-target interaction plus restricted evidence-type guard run **37786929506 SUCCESS**. Both synthetic tests and source-data jobs PASSED. Source original full final prediction rasters exactly match the original target-published maps; source final AUC reproduces the publisher's two-decimal external target AUC in 10/10 cases. Edge source scores were used only to match uniquely adjacent candidate pixels at exactly defined cell edges; otherwise the script fails closed. For each target and model, the denominator and positive coordinates are held fixed.

| Calibration species | External target | Original final AUC | Min original fold AUC | Max original fold AUC | Four-fold external range |
| --- | --- | ---: | ---: | ---: | ---: |
| Oxalis, America | Oceania | 0.531930 | 0.488346 | 0.561426 | 0.073080 |
| Oxalis, America | Africa | 0.810255 | 0.764363 | 0.833828 | 0.069465 |
| Oxalis, America | Europe | 0.890261 | 0.880697 | 0.891755 | 0.011058 |
| Digitaria, Europe | Oceania | 0.768372 | 0.265959 | 0.875743 | 0.609783 |
| Digitaria, Europe | Africa | 0.559356 | 0.356674 | 0.710402 | 0.353728 |
| Digitaria, Europe | North America | 0.720924 | 0.709702 | 0.728457 | 0.018755 |
| Digitaria, Europe | South America | 0.607864 | 0.491407 | 0.674385 | 0.182978 |
| Amaranthus, North America | Oceania | 0.915903 | 0.906484 | 0.920649 | 0.014165 |
| Amaranthus, North America | East Asia | 0.794028 | 0.786117 | 0.798587 | 0.012470 |
| Amaranthus, North America | Europe | 0.810762 | 0.798707 | 0.810660 | 0.011953 |

Complete full-precision AUC (all four folds, final, sample counts, edge-exclusion scores, boundary source-repair counts): `experiments/mqr-4.91/matsui_2026_ten_source_matched_fold_auc.csv`.

**Most informative example:** Digitaria Europe→Oceania original four fold models produce source-matched target AUC [0.265959398674, 0.545377604167, 0.649386837121, 0.875742779356] against the same 320 source-reported external presence and 2640 source reference-negative cells. Original separately fitted final model is 0.768372395833. The fold model index 3 has highest AUC for all four Digitaria target regions, but three of six fitted-model rank pairings reverse somewhere across regions; no iid fold hypothesis test or cross-species generalization may be inferred.

## Double-centred descriptive fold × geographic target decomposition

Compute a four-fitted-fold score matrix for each species, external targets as rows. Algebra `A[t,k] = grand_mean + (target_mean[t]-grand_mean) + (fold_mean[k]-grand_mean) + residual[t,k]` with residual double-centred, sum-of-squares identity unit-tested and source-run verified; no stochastic model fitted.

| Species | Target main SS | Model identity main SS | Target × fold residual SS | Total SS | Reversed model-pair ranks |
| --- | ---: | ---: | ---: | ---: | ---: |
| Oxalis | 0.292778237 | 0.003275837 | 0.002291569 | 0.298345642 | 2 of 6 |
| Digitaria | 0.077145763 | 0.121714936 | 0.153141372 | 0.352002071 | 3 of 6 |
| Amaranthus | 0.035370806 | 0.000145379 | 0.000146223 | 0.035662408 | 4 of 6 |

Digitaria descriptive SS composition: target ~21.9%, model ~34.6%, interaction ~43.5%. By contrast target differences dominate Oxalis ~98.1% and Amaranthus ~99.2%; Amaranthus has rank reversals but very small fold AUC differences. These are **numerical decompositions of AUCs defined on DIFFERENT regional P+ and Q−**. They are NOT variances of a randomly sampled population, causal effects, design-based uncertainty, proof of spatial leakage, or proof of true regional adaptation.

## Boundary-blind falsifier and source provenance

Every original positive coordinate that fell exactly on an ASCII grid boundary was excluded using original X/Y and grid metadata alone, ignoring source scores, to create an independent sensitivity set. All ten target cases include full and interior-only fold AUC, and all source-valid reference negative records stayed in place. In Digitaria Oceania, 41 boundary positive observations (30 uniquely source-score-resolved for complete join) are excluded in the interior-only sensitivity. The maximum change in one fold's AUC was **0.012846705**, while the full fold spread was **0.609783381**; the broad fold-model disparity persists. Boundary exclusion changes the positive sample distribution, so it is a **sensitivity check**, not an unbiased replacement and not proof of the original GIS convention. Disclose the original-score-conditioned tie resolution. The audit deliberately does not silently discard ambiguous sources or impute missing prediction scores.

The original source-output identity mistake observed in early work was choosing the calibration-native `species.asc` from an external prediction directory instead of the separately labelled target `species_<target language>.asc`; corrected by original archive semantic/geometry inspection and verified by zero-error author-map replay. This is an actual **artifact-identity provenance repair instance**, not a demonstrated globally minimum-cost repair algorithm.

## Executable claim type guard

`experiments/mqr-4.91/evaluation_contract_guard.py` tests each case for held-fixed source positive/negative reference CSVs, target, inclusion mask, metric and label selection policy. It admits **40 paired original-fold vs fitted-final model contrasts** where these evaluation inputs are shared. It intentionally rejects source-native cross-validation AUC as though it were the identical external target estimand: native held-out positives, native-background negatives, fitted-training/evaluation policy differ. Both synthetic adversarial tests and the complete source matrix run PASS. This is a **restricted evidence precheck**, not a general Pearl-Bareinboim transportability completeness theorem or novel database why-provenance complexity result.

## Prior art and genuine article scope

Phillips et al. (2009) and VanDerWal et al. (2009) had already studied background selection and fixed-region AUC; Baker et al. (2024) warns about bias-correction validation without independent test data; Serov, Koldasbayeva & Zaytsev (2026) directly investigates spatial target-risk estimation via KMM, NW/IW/classifier weighting; Bareinboim & Pearl (2013) developed general causal-effect meta-transportability; Calautti et al. (2024) differentiates minimal/explanation provenance. These are direct novelty constraints, not citations offered as proof of MQR's new methods.

**Candidate paper direction (not yet admitted):** *Source-Attested Model–Target Evaluation Matrices: Reconstructing Fitted-Fold Instability and Enforcing Comparable Performance Contracts*. Publishability requires an independent second publication/dataset, a real competing audit baseline, predeclared uncertainty/selection design, and clear demonstration that automated provenance-typed repair adds value beyond ordinary file inspection and fixed-reference AUC. Do not claim general-purpose transportability or original discovery of reference dependence.

Serov et al. (2026) has its own public reproduction repository at `https://github.com/awesomeslayer/Importance-reweighting` and an independent data/code availability statement in the paper; **not yet audited/replayed by MQR**. Their metrics are target risk/error, NOT automatically an AUC matched across study roots. Next follow-up: identify an exact shared score/selection contract or use independent evidence repair adjudication without pooling incompatible metrics.

## Provenance and storage

- Original 10-case CI: `https://github.com/WhoSia/MQR/actions/runs/37786496173`, artifact `MQR491-Ten-Target-Source-Matched-Fold-Matrix`, ID 11553764139.
- Derived factorial + typed-guard CI: `https://github.com/WhoSia/MQR/actions/runs/37786929506`, artifact ID 11554073909.
- Original-matrix GitHub CSV `experiments/mqr-4.91/matsui_2026_ten_source_matched_fold_auc.csv`; algebra CSV `experiments/mqr-4.91/ten_target_fold_interaction_descriptive.csv`.
- Independent evidence replay programs `ten_target_fold_matrix.py`, `fold_target_interaction_analysis.py`, `evaluation_contract_guard.py`. All human-authored GitHub commits, no bot commits.
- GitHub-generated source JSON/log receipts mirrored **without mutation** into existing MQR Drive `02_ANALYSIS_SAFE`: file ID `1JrllZVj-JpMrlFlAGbohp3jabJFYt8Q-`, metadata verified ZIP 8324 bytes; derived analysis and guard receipt file ID `1Kp_q3YzJhAqEgUwA8jD0tQdfcWAPODsb`, metadata verified ZIP 4670 bytes. Do not conflate these receipts with fully archived 96MB+47MB original publisher raw ZIPs.
- Canonical MQR Notion root **only**: `3c8ef561cf92815693b6fcf6de9955f7`. No 4.91 Lab row/folder/child page. 4.91 remains **OPEN**, within-stage empirical expansion and test checks PASS. No 4.92 opened.
