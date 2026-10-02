# MQR-4.63 — Frozen World & Calibration Manifest

Status: **FROZEN BEFORE HARVEST WORLD SELECTION AND EXECUTABLE REVEAL**

## World-selection rule

Harvest/literature may supply candidate worlds only after this file is committed.

Candidates are admitted by the eight eligibility criteria in PRESEAL.md. If more than three worlds qualify, choose for structural heterogeneity and source quality, **not MQR-favorable pilot performance**.

## Minimum final pack

At least **3 worlds**, preferably **4**, with no two worlds sharing the same primary acquisition mechanism.

Required heterogeneity dimensions across the pack:
- reversible vs irreversible action;
- static vs policy-altered evidence distribution;
- known vs open rival/model set;
- independent vs common-mode acquisition ancestry;
- passive-measurement vs intervention semantics where possible.

## Baseline contract

Every world must have:
1. at least one strong domain baseline;
2. random/exterior reference where meaningful;
3. no-MQR or baseline-only control;
4. full typed MQR policy or diagnostic layer;
5. one-at-a-time ablations for MQR objects actually active in that world.

## Calibration ledger schema

For every world × policy × seed/trace:
- world_id
- policy_id
- step
- action
- observed outcome
- active rivals / models
- nominal evidence count
- ancestry classes
- reachable separators
- reopening routes
- contamination state
- option-loss state
- conventional metric vector
- ERR
- FSR
- RCR
- RL
- EAI
- BOD
- CSD
- NED
- BSI

## Frozen failure modes

1. **Metric laundering** — deriving MQR metrics from the same score used to select actions.
2. **Outcome-aware world editing** — changing world transitions after pilot results.
3. **Weak-baseline substitution** — replacing a known strong baseline with an easier comparator.
4. **Hidden oracle** — giving MQR access to rival/world information denied to baselines.
5. **Ablation compensation** — removing one MQR object while strengthening another.
6. **Synthetic-to-natural overclaim** — treating simulation success as historical/scientific validation.
7. **Retrospective hindsight** — using later-known truth to choose historical actions.
8. **Common-seed leakage** — allowing one policy's discoveries to alter another policy's world.
9. **Scalar rescue** — combining vector metrics post hoc to manufacture a winner.
10. **Selective domain retention** — dropping a valid world because MQR underperforms.
11. **Stopping asymmetry** — giving policies different budgets/stopping rules without explicit matching.
12. **Baseline misparameterization** — tuning baselines less carefully than MQR.
13. **Representation favoritism** — choosing encodings that expose MQR-relevant structure only to MQR.
14. **Reopening after impossible destruction** — crediting a reopening route that the world dynamics have actually removed.
15. **Ancestry fiction** — counting formally different measurements as independent when their evidence-generating cause is shared.
16. **Debt double counting** — counting one skipped separator repeatedly without state transition.
17. **Hidden-rival omniscience** — computing policy actions using rival identities not yet available to the policy.
18. **Cost erasure** — ignoring materially different acquisition costs when conventional baselines require them.
19. **Cross-domain unit collapse** — averaging incomparable raw metrics across worlds.
20. **Publication cherry-pick** — selecting only the metric/world combination with favorable narrative.

## Frozen positive controls

1. Fully reversible IID measurement world: OPR/NED should mostly collapse.
2. Irreversible separator-destruction world: OPR should become active.
3. Hidden-rival arrival world: ARR/ERR/BSI should activate.
4. Common-mode evidence world: EAI should fall below nominal evidence multiplicity.
5. No-common-mode world: ancestry correction should not create a phantom penalty.
6. Fixed closed model world: conventional EIG/identifiability baseline should remain strong.
7. Open model world: low internal uncertainty must not imply exterior saturation.
8. Random exterior policy: may improve exterior coverage while paying local cost.
9. Strong robust baseline: may absorb misspecification-related MQR effects.
10. Equal reachable-separator world: NED should remain zero despite different action order.
11. Contamination-free intervention world: CSD should remain zero.
12. Drift/contamination world: later measurement semantics should visibly change.
13. Matched-budget comparison: policy differences must survive equal budget.
14. Ablation sanity: removing inactive object should not change policy.
15. World-removal robustness: any cross-domain conclusion must report leave-one-world-out sensitivity.

## Promotion gate

A typed distinction is promoted from synthetic constitution to calibrated cross-domain candidate only if:
- its metric is nontrivial in at least two structurally distinct worlds **or** it has one strong natural/reconstructed world plus a formal positive-control world;
- its effect survives its own one-at-a-time ablation;
- the comparison uses a strong matched baseline;
- the result is not reducible to an already-tracked conventional metric within the tested pack;
- the result is reported with failure/negative domains intact.

Otherwise the distinction remains local, collapses into prior art, or is retired.

No result-dependent changes after first executable reveal.
