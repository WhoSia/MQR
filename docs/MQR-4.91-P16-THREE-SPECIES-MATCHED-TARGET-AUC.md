# MQR-4.91 — P1.6 Three-Species Source-Fold Matched Target AUC

2026-10-08. Status: TWO_NEW_SPECIES_SOURCE_TARGET_REPLAY_PASS / FOUR_FOLD_SAME_TARGET_COMPUTED / GLOBAL_SPATIAL_CV_OPTIMISM_HOLD.

Independent Maxent Java v3.4.4 source archive replays published native-only calibration→external deployment maps with zero raster cell discrepancies across 8,352 Africa Digitaria and 5,919 Europe Amaranthus valid external scores. Original target label and unrecorded negative reference CSV coordinates are preserved, and all original four fitted 4-fold model lambdas projected into the same target rasters. P1.6 GitHub Actions run [37782481228](https://github.com/WhoSia/MQR/actions/runs/37782481228) SUCCESS, source code experiments/mqr-4.91/p16_multispecies_fold_auc.py, CI source pinned by publisher MD5 and Maxent Git blob. P1.5 predecessor Oxalis run 37779744065 SUCCESS.

## AUC with the same species-specific source target positive/negative references

| Case | P+ | Target Q- | Fold0 | Fold1 | Fold2 | Fold3 | Final |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Oxalis America→Oceania | 105 | 2826 | 0.4883463081 | 0.5178242847 | 0.5614262124 | 0.5193003741 | 0.5319297004 |
| Digitaria Europe→Africa | 174 | 8178 | 0.5377723525 | 0.3566739191 | 0.5116780232 | 0.7104015399 | 0.5593564034 |
| Amaranthus NorthAmerica→Europe | 2635 | 3284 | 0.8000561055 | 0.8084821006 | 0.7987070888 | 0.8106602191 | 0.8107622606 |

The last model per row is the original separately fitted FINAL deployment model. It is **NOT** a CV fold estimate; the original reported native-region CV scores use DIFFERENT validation positive and reference distributions.

## The boundary-join correction and limits

P1.6 first exact coordinate-to-ASCII cell method rejected 5 Digitaria and 6 Amaranthus original score rows, while author full raster pixel replay matched exactly 0.0 difference. CI 37782125620 reported mismatches; coordinates included exact .0/.5 geographical edges and alternative grid cell assignments. Corrected script enumerates **only** the adjacent raster pixels available when a coordinate lies on a grid cell edge (including corner diagonal if on both). A repair is permitted only if exactly one candidate reproduces the original source-provided fitted FINAL model score to 1e-4. Ambiguous/non-edge mismatch remains FAIL CLOSED. Run 37782481228 SUCCESS with both cases, showing all previous 5/6 mismatches were uniquely resolvable under this source-score-constrained rule; numerical fold arrays are real original fitted model outputs on these selected original target cells.

**Crucial qualification:** This join uses the SOURCE FINAL MODEL SCORE to determine one borderline coordinate's cell identity. It is an independent negative control on the model's source-lambda replay, but not an independent provenance for the author's original GIS edge-point assignment convention. In any scientific paper, report sensitivity to dropping all boundary-ambiguous rows, and separately justify that source-score resolution did not select test scores to optimize the fold AUC. The recorded max source score errors 0.025015994999999958 (Digitaria) and 0.12172497299999996 (Amaranthus) in P1.6 log refer to the **unrepaired initial point-in-cell lookup**, not post-boundary-resolved source model score discrepancies. Improve receipts to explicitly present both pre- and post-repair errors.

## What follows

1. P1.7 source-map GIS boundary independent nearest-centre/edge convention sensitivity; report AUC excluding all edge-affected source records and compare to the uniquely rejoined full source record set.
2. P1.8 broader Matsui 10 external targets, with source root grouping species instead of treating 10 targets as 10 studies, followed by explicit spatial dependence/uncertainty court.
3. Formal typed evidence identity: native fit map vs labelled geographic target map; source point raster edge-resolution plus blinded score join; prevent recurrence in source-repair compiler and test recovery across source studies.
4. Direct prior art baseline VanDerWal fixed-region AUC and Baker independence uncertainty; cannot claim AUC normalization novel.

Original MQR-4.90 historical court CLOSED remains unchanged; all MQR-4.91 Notion version updates are headings within single canonical MQR root, never new Labs/children. Scientific stage MQR-4.91 P1.6 CLOSED/PASS for bounded three-species same-target fit-identity comparison, global CV optimism HOLD.
