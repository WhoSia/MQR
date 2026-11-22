# MQR 5.4 · MQR 44 · R53 — DFS: selecting matching observations can manufacture a scientific 'bridge'

**2026-11-23 KST. Exact executed synthetic probability model:** `language/real/experiments/mqr_selection_colliders_v54.py` run with standard-library `fractions.Fraction`; PASS (complete four-state assertions, inverse probability check). This is standard selection/collider-bias statistics and **not** a new MQR theorem, astronomical null rate, or real single-cell dataset estimate.

## 1. A new hazard beyond pairing and measurement disturbance
Suppose two observables A and B are *truly independent*, both Bernoulli(1/2), across four equally likely states (00,01,10,11). Unconditional Cov(A,B)=0. Two scientists might jointly collect only those events/cells whose measured attributes match a cross-channel filter, without keeping the rejected sample and filter denominator.

If **S=1 only when A=B**, the retained sample has P(00|S)=P(11|S)=1/2 and P(01|S)=P(10|S)=0. Although the population variables are independent, Cov(A,B|S)=+1/4: a **perfect apparent association** manufactured by selection. If instead **S=1 when at least one attribute is positive**, the retained sample consists of 01,10,11 equally, so Cov(A,B|S)=-1/9. One selection scheme produces positive and another negative covariance from **exactly the same original population**.

The example explains why 'the two detectors agree for all selected joint observations' is not sufficient to conclude underlying phenomena always agree. It is also why multiomics viability/capture, detection thresholds and conditional follow-up can distort cross-modal associations.

## 2. When the error is repairable
If the selection probability P(S=1|A,B) is known and **strictly positive for every state**, inverse-probability weighting can recover the original joint law in this ideal exact model. Example weights 3/4 for matching outcomes and 1/4 for nonmatching outcomes cause a retained-sample covariance of +1/8; dividing each observed cell by its selection probability and renormalizing correctly recovers all 1/4 population cells and zero covariance.

If some population states have **zero probability of ever being selected**, the full distribution is generally unidentifiable without external assumptions: even an alternative population with 1/8 mass on 00,11 and 3/8 mass on 01,10 gives **the same 50-50 selected matching sample** as the independent population when only agreeing pairs are admitted. No amount of data from that selection process recovers the excluded cell masses.

A real research application requires knowing the selection denominator, background event rates and calibration, missingness and triggering dependencies; qualitative positive/negative associations alone are insufficient. **Do not assume** independent population Bernoulli bits, known selection weights or exact asymptotic cell counts apply in nature.

## 3. Source-backed cross-domain controls
**Astronomy:** LIGO/Virgo's 2017 multimessenger study [Abbott et al. (2017), ApJL 848:L12, DOI 10.3847/2041-8213/aa91c9](https://dcc.ligo.org/LIGO-P1700294-v7/public) uses time, localization and known triggers/background to associate gravitational and gamma observations. Their published rare *null-coincidence* statement must not be read as a posterior P(common source|reports) without explicit models/priors. Selection of only striking coincident events would bias an uncalibrated study. We **do not claim LIGO ignored this bias**; their original astrophysical inference has substantial additional evidence and null calibration.

**Molecular biology:** [Cao et al. (2018), *Science* 361:1380–85, DOI 10.1126/science.aau0730](https://pmc.ncbi.nlm.nih.gov/articles/6571013/) used sci-CAR joint RNA-accessibility observations, subject to the practical possibility of capture/dropout and cell-state selection. Our selection schematic is **not** a replication or specific criticism of sci-CAR's actual bias estimates.

## 4. New six-step thought-experiment ladder
1. Unpaired marginals hide the joint (R44).
2. Valid same-unit pairing reveals joint relations (R44).
3. Unknown mislinkage makes observed association a product of physics and data provenance (R46).
4. Destructive measurements can erase the original joint even with accurate IDs (R48).
5. **Selective retention can manufacture a joint correlation even with flawless individual measurements and links (R53).**
6. Fully observed descriptive joint still does not distinguish alternative causal structures (R44 fork/chain), without valid interventions/assumptions.

This is a logical-inference stress test, not evidence that scientific communities always fail to solve all six gates. Different real sciences have different protocols.

## 5. What would falsify MQR's practical relevance?
If a cross-domain real case has complete selection logs, calibrated detection efficiency, demonstrably valid specimen associations and non-disturbing assays, R53's specific confounding scenario is eliminated. MQR should describe the case as **success**, not invent a failure or invoke abstract limits to deny a high-quality result. Any novel science-of-science contribution must outperform existing missing-data, case-control, collider-bias and causal-inference baselines by historically grounded criteria.

**Status:** exact construction and correction PASS; real LIGO/sci-CAR selection-bias existence/magnitude HOLD; MQR 5.4 OPEN.
