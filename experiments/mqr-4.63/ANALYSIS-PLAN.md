# MQR-4.63 — Frozen Analysis Plan

Status: **FROZEN BEFORE EXECUTABLE REVEAL**

## Replication design

All stochastic policies are compared on paired world seeds.

Default seeds:
- CAUSAL-SEP: 64
- SENSING-GRID: 64
- SCOUT-PARK: 96
- THEORY-ECOLOGY: 96
- SAMPLE-RESERVE: 96

Fixed per-run acquisition budgets:
- CAUSAL-SEP: 6 actions
- SENSING-GRID: 12 actions
- SCOUT-PARK: 20 acquisition rounds
- THEORY-ECOLOGY: 30 experiment choices
- SAMPLE-RESERVE: 10 assay decisions

The exact same latent world instance / event stream / target trajectory / material inventory is replayed across all policies sharing a seed.

## Required policies

### CAUSAL-SEP
- causal_identifiability
- expected_elimination
- random
- mqr_full

### SENSING-GRID
- entropy_greedy
- horizon2
- random
- mqr_full

### SCOUT-PARK
- current_information
- information_per_bandwidth
- high_rate_scout
- fixed_park
- random_mix
- mqr_full
- mqr_minus_opr
- mqr_minus_arr
- mqr_minus_nedl
- mqr_minus_exterior

### THEORY-ECOLOGY
- confirmation
- falsification
- disagreement
- random
- representative
- robust_multifactor
- mqr_full
- mqr_minus_arr
- mqr_minus_eai
- mqr_minus_nedl
- mqr_minus_exterior

### SAMPLE-RESERVE
- immediate_information
- information_per_cost
- fixed_preserve
- nondestructive_first
- random
- mqr_full
- mqr_minus_opr
- mqr_minus_arr
- mqr_minus_nedl

## Primary paired comparisons

No global policy ranking is permitted.

Typed-object tests:
- **OPR/BOD:** mqr_full vs mqr_minus_opr in SCOUT-PARK and SAMPLE-RESERVE.
- **ARR/RCR/RL:** mqr_full vs mqr_minus_arr in SCOUT-PARK, THEORY-ECOLOGY and SAMPLE-RESERVE.
- **EAI:** mqr_full vs mqr_minus_eai in THEORY-ECOLOGY; SCOUT-PARK ancestry is diagnostic-only unless an explicit ancestry ablation is materialized before reveal.
- **NEDL/NED:** mqr_full vs mqr_minus_nedl in SCOUT-PARK, THEORY-ECOLOGY and SAMPLE-RESERVE.
- **Exterior reserve / ERR/BSI:** mqr_full vs mqr_minus_exterior in SCOUT-PARK and THEORY-ECOLOGY.
- **IDR:** CAUSAL-SEP and SENSING-GRID are primarily collapse/positive-control worlds; mqr_full should not receive a special IDR bonus over strong identifiability/information baselines merely for carrying the receipt.

## Statistical summaries

For every metric and paired policy comparison:
- paired mean difference;
- paired median difference;
- standardized paired effect `mean(diff) / sd(diff)` when variance is nonzero;
- fixed-seed nonparametric bootstrap 95% CI of the paired mean difference using 2,000 bootstrap resamples;
- sign fraction `P(diff > 0)`.

Bootstrap RNG seed: **4632026**.

No p-value fishing or post-hoc multiple-threshold search.

## Metric orientation

Higher is better:
- conventional_success
- ERR
- FSR
- RCR
- EAI

Lower is better:
- conventional_error
- cost
- RL
- BOD
- CSD
- NED
- BSI

Every comparison is converted to a signed `benefit_delta` where positive favors the first named policy.

## Nontriviality threshold

A typed metric effect is **nontrivial** only if both:
1. the 95% bootstrap CI of paired benefit_delta excludes 0 in the predicted direction;
2. absolute normalized mean benefit_delta >= **0.08**.

Metrics are normalized to [0,1] by world-defined natural bounds before cross-policy effect classification. Raw values are retained.

This threshold is fixed before reveal and is not tuned to results.

## Non-reducibility witness

A typed metric is not treated as empirically distinct merely because it correlates imperfectly with conventional performance.

A stronger within-world witness is required:

There must exist at least one matched policy pair with:
- absolute conventional-performance difference <= **0.05** of the world-normalized range;
- absolute typed-metric difference >= **0.15**.

Such a witness is descriptive, not a theorem of irreducibility.

## Negative-control gate

Expected inactive coordinates:
- CAUSAL-SEP closed reversible variant: BOD=0, CSD=0, NED approximately 0; mqr_full should closely match strong causal-identifiability baseline.
- SENSING-GRID: BOD=0, CSD=0, OPR/ARR/NEDL should have no material action effect.
- SAMPLE-RESERVE: EAI is not promoted unless an explicit evidence-ancestry structure is added pre-reveal.
- SCOUT-PARK: CSD remains 0 unless mode semantics are explicitly changed by the frozen world.
- THEORY-ECOLOGY: OPR/BOD should remain 0 because experiment choice does not physically destroy future contexts.

A coordinate that activates strongly in an ineligible negative-control world is a **calibration failure**, not a success.

## Typed-distinction classification

### SURVIVES_CROSS_DOMAIN
Requires:
- nontrivial own-ablation effect in at least two structurally distinct worlds, OR one natural/reconstructed world plus one dedicated formal positive-control variant;
- at least one strong-baseline comparison;
- negative-control gate not violated;
- at least one non-reducibility witness inside the tested pack.

### SURVIVES_LOCAL
Nontrivial own-ablation effect in exactly one eligible world, with no negative-control failure.

### COLLAPSES_TO_BASELINE
No nontrivial own-ablation effect, or the full typed policy is behaviorally identical to the strong matched baseline in all eligible worlds.

### RETIRE_OR_REDESIGN
The coordinate activates primarily in negative-control worlds, requires hidden oracle information, or fails independent audit.

## Cross-domain result rule

No averaging of raw metrics across worlds.

The final result is a **coordinate × world matrix** plus typed classification.

No scalar "MQR score", policy leaderboard or overall winner is permitted.

## Publication implication gate

The Paper-II prospect is strengthened only if at least one of OPR, ARR, EAI, NEDL or exterior-reserve diagnostics reaches SURVIVES_CROSS_DOMAIN under the above rules.

If all collapse or remain local, the computational-paper prospect is narrowed accordingly.

No result-dependent mutation after first executable reveal.
