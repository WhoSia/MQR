# MQR-4.91 P1.5 — Source-Matched Four-Fold Target Evaluation

**Scientific status:** ORIGINAL_SOURCE_COORDINATE_MATCHED_AUC_COMPUTED / SAME-TARGET-MODEL-CONTRAST ADMITTED / SPATIAL_CV_OPTIMISM_NOT_ADMITTED. Date 2026-10-08. Parent one MQR canonical Notion Lab (no separate MQR version rows).

## Original source + independently executed result

Matsui 2026 DOI 10.1002/ece3.73534 with correction 10.1002/ece3.73828, original Zenodo 19970795 archive, verified source MD5, Maxent 3.4.4 official Git blob SHA1 1a0a1826cbefdaf551463ed20e3a41944801955a.

Exact specimen: *Oxalis latifolia*, American calibration, Oceania original target. The author archives a **separately named actual Oceania projection** `Oxalis_latifolia_オセアニア.asc`, in addition to `Oxalis_latifolia.asc` (the latter is a source/model-native map). Original model final .lambdas replayed 2,931 scored cells, max raster error 0.0; original four CV fold model .lambdas likewise successfully projected onto matching target climate layers, source replay CI 37777179020 SUCCESS.

Original coordinate-labeled evaluation records are source CSV `.../2_Maxent_values/1_Maxent_values_for_presence_cells/Oxalis_latifolia_America-Oceania.csv` with `species,X,Y,SAMPLE_1` and `.../2_Maxent_values/2_Maxent_values_for_absence_cells/Oxalis_latifolia_America-Oceania_2.csv` with `X,Y,SAMPLE_1`. Not training labels from the American area.

**P1.4:** Source coordinate audit CI 37778805874 SUCCESS.

**P1.5** original source-joined target results; source CSV 2,934 total rows, exactly three blank prediction values; 2,931 admissible matched rows = 105 external positive presence points and 2,826 external unrecorded-reference cells; 0 post-source-filter out-of-range points and 0 missing matched raster cells. Recomputed full-final source sample prediction scores differ by max 3.0000000039720476e-08 and 0 rows differ by >1e-4, confirming coordinate index. Exact same original target P+ and Q− retained for five fitted model score functions.

| Original fitted predictor | External Oceania AUC (same target) |
| --- | ---: |
| Original CV fold 0 model | 0.488346308091531 |
| Original CV fold 1 model | 0.5178242847032656 |
| Original CV fold 2 model | 0.5614262123816264 |
| Original CV fold 3 model | 0.5193003740774441 |
| Original final deploy model | 0.5319297004010379 |

First source-verified numeric run 37779242071 completed all numeric calculations but GitHub workflow FAIL because inherited P1.3 receipt strings did not match P1.5 grep. Script commit 9c995d40077d921d6ede7923e08cfb0751924b1f fixes receipt output and launches follow-up run **37779744065**; judge its actual CI result before attesting green.

## Typed interpretation and remaining inferential debt

This result is **not** CV optimism. Four fold models and one separately fitted final model are scored on identical positive and negative external target records. Their variation represents **model-fit sensitivity on a fixed target**, conditional on common accessible source mask and method. The original source-region CV AUCs were calculated with different training-set folds, validation source positives and source-region background. Comparisons across these reported measures remain non-commensurable unless the selection and validation protocols are modeled explicitly.

No 4-fold sampling standard error can be obtained by treating the 2,931 grid points or 4 fold model fits as independent biological units. No pooling beyond one species has been done here. Different fitted models may share source points/data genealogy. Original final AUC 0.5319297004 agrees with P8 rank-based 0.53192970.

**Novelty boundary:** The correct discovery is a demonstrably executable source-identity repair of a mistakenly joined training/base output with a named target-output raster, and its quantitative downstream effect on what can be computed. Raster file naming, fixed-negative-reference AUC and original-bias literature already exist; not a general complete or minimal evidence repair algorithm without larger case suite and explicit formal soundness claims.

## Next

P1.6: replicate across *Digitaria sanguinalis* (Europe calibration) and *Amaranthus retroflexus* (North America calibration), identify target-language output maps by content and geography rather than hardcoded filename translations, and run same source coordinate validation. Compare effect direction within species before any cross-source extrapolation. Add source-root dependence graph and uncertainty designs; direct competitor benchmarks Phillips/VanDerWal/Baker/Serov. Keep this MQR record inside existing single Notion MQR root; GitHub files are acceptable separate source artifacts.
