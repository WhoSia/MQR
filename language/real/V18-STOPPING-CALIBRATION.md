# Real-Language v0.18 — Stopping-Rule Calibration Boundary

Status: CANDIDATE / MQR-4.51 ACTIVE / OUTCOME-SEQUESTERED / CALIBRATION-ONLY CONFIRMATION / REOPENABLE / EXTERNAL-CALIBRATION-HOLD

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
