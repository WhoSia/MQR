# Real-Language v0.23 — World-Contact Expansion-Policy Constitution

Status: **EXECUTABLE-CANDIDATE / MQR-4.56 / PRESEALED / NOT-YET-PROMOTED**

## Purpose

REALVALUE 0.23 serializes a **challenge-value constitution** over admissible consequence-expansion directions.

It deliberately does not define one universal scientific utility.

## Packet

~~~text
REALVALUE 0.23
id <token>
target_contract DECLARED | HOLD
typed_value_profile PASS | FAIL
value_provenance PASS | FAIL | UNKNOWN
proxy_dependence DECLARED | HIDDEN
target_drift_sentinel ACTIVE | ABSENT
adversarial_decoy_test PASS | HOLD | FAIL
opportunity_cost DECLARED | HOLD
unit_audit PASS | FAIL
horizon DECLARED | HOLD
option_value TRACKED | UNTRACKED
exterior_value_challenge ACTIVE | ABSENT
reopening ACTIVE | INACTIVE
optimizer_scope DECLARED_MODEL | NONE | WORLD
scalar_default OFF | ON
world_optimum NO_CLAIM | CLAIMED
END
~~~

## Core boundary

~~~text
CHALLENGE VALUE
!=
ONE NUMBER

INFORMATION GAIN
!=
TARGET RELEVANCE
!=
ACTION VALUE
!=
ESCAPE VALUE
!=
OPTION VALUE
~~~

## Local guidance

A packet can earn local guidance only if:
- the target/use contract is declared;
- value dimensions remain typed;
- value-estimator provenance is audited;
- proxy dependence is explicit;
- target drift is monitored;
- adversarial decoys are tested;
- opportunity cost and horizon are declared;
- cost-unit sensitivity is audited;
- option value is tracked;
- the value model can be challenged externally;
- reopening is active;
- optimizer scope is not WORLD;
- scalar default remains OFF;
- no world-optimum claim is made.

## Diagnostics

The canonical evaluator may emit:
- `TARGET_CONTRACT_HOLD`
- `VALUE_PROFILE_COLLAPSE`
- `VALUE_PROVENANCE_GAP`
- `HIDDEN_PROXY_DEPENDENCE`
- `TARGET_DRIFT_BLIND`
- `DECOY_RESISTANCE_GAP`
- `OPPORTUNITY_COST_HOLD`
- `UNIT_RANK_REVERSAL`
- `HORIZON_HOLD`
- `OPTION_VALUE_BLIND`
- `VALUE_MODEL_SELF_INSULATION`
- `VALUE_REOPENING_FAILURE`
- `WORLD_OPTIMIZER_OVERCLAIM`
- `SCALAR_DEFAULT_ON`
- `WORLD_OPTIMUM_OVERCLAIM`
- `LOCAL_EXPANSION_GUIDANCE_ADMISSIBLE`

## WCEPR

The executable candidate is **WCEPR — World-Contact Expansion-Policy Receipt**.

A successful packet may emit:

~~~text
value.local_guidance=YES
value.wcepr=EARNED_LOCAL_CANDIDATE
value.universal_scientific_utility=REJECT
value.world_optimal_policy=NOT_EARNED
~~~

## Claim ceiling

REALVALUE 0.23 does not establish:
- a universal scientific utility function;
- a complete total ranking of all conceivable research directions;
- calibrated value over unconceived consequences;
- a universal exchange rate among information, novelty, relevance, actionability, cost and option value;
- a world-optimal expansion policy.

Promotion requires the qualifying MQR-4.56 Court and proof boundary.


## Aggregate integration

The Lean aggregate module `MQR.lean` imports `MQR.ExpansionPolicy`, so pinned lean4export and independent nanoda can replay the v0.23 boundary from the cumulative package rather than from an unmaterialized standalone source file.
