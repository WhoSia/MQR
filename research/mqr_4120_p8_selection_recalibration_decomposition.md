# MQR-4.120 P8 — Two-Operation Decomposition: Restriction versus Median Recalibration

2026-10-17. Direct computation from publicly rendered full MIT jtpa.raw (11,204) and a later researcher-hosted jtpa_han.tab (9,223 unique recid matches). Historical Han official ZIP byte identity, exclusion algorithm, and original causal analysis are HOLD.

## Fixed common outcome and exact finite-sample paths
Let P be the MIT full empirical population, S the retained recid cohort, T(P)=$11,010 and T(S)=$11,187. Let L_t(y)=1{earnings>t}. On a fixed reference population S, changing t changes individual labels; selection P->S changes the denominator and included persons.

A: Full P / original median threshold 11010: 5601/11204 = 0.499910746162085.
B: Selected S / threshold held at 11010: 4647/9223 = 0.5038490729697496.
C: Selected S / recomputed median 11187: 4611/9223 = 0.4999457877046514.

Decomposition C-A = (B-A)+(C-B):
- Fixed-cutoff selection component: +0.003938326807664594 = +0.3938326808 percentage points.
- Within-selected threshold recalibration: -0.0039032852650981442 = -0.3903285265 percentage points.
- Net: +0.000035041542566449646 = +0.0035041543 percentage points.

The almost-zero net **does not imply data-production equivalence**: denominators, reference thresholds, and 36 labels on same retained subjects differ. The decomposition is PATH-CONDITIONAL: changing the order or reference definition changes component interpretation. It is arithmetic, not a causal decomposition nor identification of the original selection rule.

## Assigned versus unassigned descriptive contrasts
At full P with fixed threshold 11010: Z=0 1798/3717=0.4837234329; Z=1 3803/7487=0.5079471083; contrast +0.02422367545.
At selected S with fixed threshold 11010: Z=0 1515/3090=0.4902912621; Z=1 3132/6133=0.5106799283; contrast +0.02038866612.
At selected S with reset threshold 11187: Z=0 1500/3090=0.4854368932; Z=1 3111/6133=0.5072558291; contrast +0.02181893592.
These **are unadjusted observed assignment-group contrasts**, not design-adjusted ITT, IV LATE, Han's dynamic policy results, or certified causal effects. Their apparent magnitudes depend on both reference-population and outcome-definition decisions.

## Philosophical genealogy and scope
MQR original quotient (different microhistories can agree after measurement projection), 3.100 target-relative informativeness, 4.53 nonuniversal scalar progress, 4.101 target-selective verification, 4.107 data-production history, 4.109 provenance-sensitive sufficiency, 4.113 target-relative Blackwell comparison, 4.119/4.120 J1 validity versus J2 revisable authority. The present empirical calculation is *a bounded real-data illustration* of the difference between final marginal summaries and path-sensitive judgment provenance, not a new generic theorem or any verification of scientific appeal legitimacy.

## Source hold
Third-party tab recid matches all 9,223 MIT identities and seven variables in Zenodo, but official Han archive bytes unavailable, precise 1,981-record exclusion criterion unknown. Inherited Greenberg, CCQM, Harvest, 4.119 human evaluator and original causal QTE/LP replication HOLD continue. Stage 4.120 ACTIVE / P8. No P9 promotion.
