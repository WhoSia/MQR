# Real-Language v0.18 — Stopping-Rule Calibration Boundary

Status: EXECUTABLE / MQR-4.51 CLOSED / RAW-OQSC-CALIBRATION-FAIL / LAG-1-INTERNAL-CROSS-DOMAIN-PASS / OUTCOME-SEQUESTERED / REOPENABLE / EXTERNAL-CALIBRATION-HOLD

## Boundary

v0.17 states when a current constitutional regress may stop operationally.

v0.18 asks a different question:

~~~text
WHEN AN OPERATIONAL STOP IS ELIGIBLE,
IS STOPPING NOW BEHAVIORALLY CALIBRATED?
~~~

The answer is not built into the language. MQR-4.51 evaluates it prospectively.

## Grammar

~~~text
REALSTOP 0.18
id <id>
upstream <PASS|HOLD|REOPEN>
oqsc <YES|NO>
live_debt <YES|NO>
criterion_invariant <YES|NO>
break <NONE|WORLD_CONTACT|DECISION_CONTRACT|PATH_CONFLICT>
confirmation_required <0..3>
eligible_streak <nat>
END
~~~

Hidden gold, future separator times, tau*, family labels, final outcomes, and scorer-only losses are not legal grammar fields.

## Decision semantics

Define current eligibility as:

~~~text
upstream = PASS
AND oqsc = YES
AND live_debt = NO
AND criterion_invariant = YES
AND break = NONE
~~~

Then:

~~~text
break != NONE OR upstream = REOPEN
-> REOPEN

eligible
AND eligible_streak >= confirmation_required + 1
-> STOP

otherwise
-> CONTINUE
~~~

`confirmation_required=0` reproduces immediate raw OQSC stopping.

A positive value is not a truth threshold. It is a calibration-only confirmation lag selected under MQR-4.51's frozen calibration protocol.

## Scoring firewall

The policy surface and scoring surface are structurally separate.

~~~text
POLICY INPUT
= Observable

SCORER-ONLY GOLD
= HiddenGold

Observable
DOES NOT CONTAIN
live_unsafe
action_wrong_if_stop
future separator time
gold stop index
~~~

This is stronger than merely promising not to inspect hidden labels: the benchmark policy functions are typed over a different object.

## Two-clock correction

A missed obligation already live/reachable at stopping time counts as premature stop.

A genuinely new post-stop world-contact break does not retroactively make the earlier local stop premature.

It starts the reopening clock instead.

~~~text
MISSED LIVE OBLIGATION
-> PSE_live

NOVEL POST-STOP BREAK
-> RL / MISSED_REOPEN
~~~

## Calibration family

MQR-4.51 admits:

~~~text
P-OQSC-LAG-lambda
lambda in {0,1,2,3}
~~~

Lambda is selected on calibration data only by the frozen fatal-error-first order.

Holdout uses hash-derived seeds rooted in the MQR-4.51 preseal commit.

No post-holdout policy repair is permitted.

## Primary metric vector

~~~text
(PSE_live,
 PD_live,
 AE_live,
 OIW,
 RL_max,
 MISSED_REOPEN,
 BER)
~~~

No scalar truth or universal stopping score is emitted.

## Canonical guards

~~~text
stop.hidden_gold_access=NO
stop.future_oracle=NO
stop.post_holdout_policy_repair=FORBIDDEN
stop.primary_scalar_score=OFF
stop.external_calibration=HOLD
stop.universal_optimality=FORBIDDEN
stop.guidance_mode=CALIBRATED_REOPENABLE_STOP
~~~

## Implementation

- canonical stop-state evaluator: Rust `src/stop_v18.rs` / `real-v18-stop`
- independent relational evaluator: Prolog `prolog/stop_v18.pl`
- prospective calibration benchmark: `experiments/mqr-4.51/benchmark.py`
- independently coded domain adapters: `fault.py`, `measurement.py`, `search.py`
- finite formal boundary: Lean `lean/MQR/StoppingCalibration.lean`

The Rust/Prolog evaluator checks local stop semantics only. The Python benchmark owns generated known-outcome scoring and must not be interpreted as an independent empirical world oracle.

## Promotion ceiling

The strongest possible MQR-4.51 promotion is:

~~~text
PROSPECTIVELY CALIBRATED
INTERNAL CROSS-DOMAIN STOPPING COMPETENCE
ON THE DECLARED BENCHMARK FAMILY
~~~

Always forbidden:

~~~text
UNIVERSALLY OPTIMAL STOPPING RULE
EXTERNAL SCIENTIFIC CALIBRATION
METAPHYSICAL TERMINATION
FUTURE-REFINEMENT COMPLETENESS
~~~


## First prospective calibration result

The frozen benchmark materialized:

~~~text
3 domains
12 forcing families
108 discovery traces
144 calibration traces
216 untouched holdout traces
468 total traces
~~~

The calibration split selected:

~~~text
confirmation_required = 1
~~~

from the predeclared `{0,1,2,3}` family.

Untouched holdout:

~~~text
RAW OQSC
PSE_live = 51
PD_live = 51
AE_live = 51
OIW = 38.5
RL_max = 0
MISSED_REOPEN = 0
BER = 18
VERDICT = FAIL

CALIBRATED OQSC-LAG-1
PSE_live = 0
PD_live = 0
AE_live = 0
OIW = 338.5
RL_max = 0
MISSED_REOPEN = 0
BER = 18
VERDICT = PASS
~~~

The calibrated successor passed C1–C5 separately in FAULT, MEASUREMENT and SEARCH with the same policy kernel and no domain-specific threshold.

The cost increase is load-bearing. The result is not scalarized.

## Constitutional consequence

~~~text
OQSC PASS
->
STOP ELIGIBLE FOR CALIBRATION

NOT

OQSC PASS
->
FIRST ELIGIBLE INSTANT
IS CALIBRATED
~~~

v0.17 remains the constitutional admissibility layer.

v0.18 adds explicit stopping-time calibration.

The first benchmark supports one extra eligible transition only on the declared generated family.

## Counterfactual replay result

~~~text
RAW OQSC
material_continue = 51

CALIBRATED OQSC-LAG-1
material_continue = 0
~~~

The 51 raw errors are therefore tied to episodes where additional already-live inquiry would still have yielded material information.

Genuinely novel post-stop world contact is scored through reopening latency and is not retroactively charged as premature stop.

## Closure guards

~~~text
RAW_OQSC_CALIBRATED = NO
CALIBRATED_LAG1_INTERNAL_CROSS_DOMAIN = YES
EXTERNAL_SCIENTIFIC_CALIBRATION = HOLD
UNIVERSAL_LAMBDA_1 = FORBIDDEN
UNIVERSAL_STOPPING_OPTIMALITY = FORBIDDEN
PRIMARY_SCALAR_SCORE = OFF
FUTURE_ORACLE = FORBIDDEN
POST_HOLDOUT_POLICY_REPAIR = FORBIDDEN
REOPENING_RESERVE = ACTIVE
~~~

## Literature ceiling

Post-preseal literature already contains:
- epistemic norms permitting the end of inquiry under unresolved uncertainty;
- higher-order uncertainty at the end of inquiry;
- context-sensitive speed–accuracy trade-offs between stopping rules;
- sufficiency/closure without exhaustive data;
- value-of-information stopping;
- resource-bounded metareasoning;
- active sensing/data selection;
- prioritized scientific search;
- robust/adaptive decision under deep uncertainty.

MQR-4.51 therefore claims no invention of those ideas.

The surviving candidate contribution is the executable, outcome-sequestered calibration constitution applied specifically to MQR's reopenable scientific-authority stop receipt.

## Final claim ceiling

Earned:

~~~text
PROSPECTIVELY CALIBRATED
INTERNAL CROSS-DOMAIN STOPPING COMPETENCE
FOR P-OQSC-LAG-1
ON THE DECLARED MQR-4.51 BENCHMARK FAMILY
~~~

Not earned:

~~~text
RAW OQSC STOP-TIMING CALIBRATION
EXTERNAL SCIENTIFIC CALIBRATION
REAL-WORLD EFFECTIVENESS
UNIVERSAL CONFIRMATION LAG
UNIVERSAL STOPPING OPTIMALITY
FINAL ONTOLOGY
FUTURE-REFINEMENT CLOSURE
~~~
