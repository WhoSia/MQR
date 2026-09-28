# MQR-4.51 — Prospective Stopping-Rule Calibration Court

Status: **CLOSED-CANDIDATE / RAW-OQSC CALIBRATION FAIL / CALIBRATION-ONLY LAG-1 SUCCESSOR PASS / INTERNAL CROSS-DOMAIN CALIBRATION / EXTERNAL CALIBRATION HOLD / SRCR+IBAR+PSOIL+CCSR+RLR+HITC+CDTT+SPAR+SEL+BEC / REALSTOP-0.18 / MAIN-ONLY**

## Formal stage name

**MQR-4.51 — Prospective Stopping-Rule Calibration Court, Blind Inquiry-Budget Allocation, Premature-Stop versus Over-Inquiry Error, Reopening Latency, Counterfactual Continue/Stop Replay, Cross-Domain Termination Transport & Whether Operational Regress Boundaries Improve Scientific Inquiry Rather than Merely Formalize Its Ending**

## Verdict

MQR-4.50 answered when stopping may be constitutionally admissible.

MQR-4.51 shows that this does not determine calibrated timing.

~~~text
OPERATIONAL STOP ELIGIBILITY
!=
CALIBRATED STOPPING TIME
~~~

In the first outcome-sequestered benchmark, raw immediate OQSC stopping failed the presealed premature-stop criterion in all three domains.

A distinct calibration-only successor family had been frozen before holdout reveal.

The calibration split selected:

~~~text
lambda = 1
~~~

and that successor passed all C1–C5 holdout criteria in FAULT, MEASUREMENT and SEARCH.

## Primary result

~~~text
RAW OQSC
PSE_live = 51
AE_live  = 51
OIW      = 38.5
VERDICT  = FAIL

CALIBRATED OQSC-LAG-1
PSE_live = 0
AE_live  = 0
OIW      = 338.5
RL_max   = 0
MISSED_REOPEN = 0
VERDICT  = PASS
~~~

The scientific result is therefore not that “more waiting is better.”

It is a measured trade-off:

~~~text
ONE ADDITIONAL
STOP-ELIGIBLE TRANSITION

REMOVED
THE DECLARED HOLDOUT
PREMATURE/ACTION ERRORS

AT THE COST OF
ADDITIONAL INQUIRY.
~~~

No scalar collapses that trade-off.

## What failed

The stronger behavioral interpretation of v0.17 is rejected:

~~~text
FIRST OQSC PASS
->
CALIBRATED STOP NOW
~~~

Raw OQSC failed C1 in:
- FAULT;
- MEASUREMENT;
- SEARCH.

It nevertheless passed the over-inquiry, Pareto non-domination and reopening criteria C2–C5.

Thus the failure is specifically a **timing calibration failure**, not a failure of reopening or a return to infinite regress.

## What survived

4.50's constitutional claim remains:

~~~text
OQSC PASS
->
CURRENT STOP IS
CONSTITUTIONALLY ADMISSIBLE

NOT

OQSC PASS
->
THE FIRST ELIGIBLE INSTANT
IS EMPIRICALLY OPTIMAL
~~~

v0.18 therefore adds an explicit calibration coordinate rather than rewriting OQSC as a truth oracle.

## Scoring correction

The frozen preseal's full-suffix stop index would have retroactively punished a locally legitimate stop for genuinely new future world contact.

Before materialization, Amendment A separated:
- already-live/reachable missed obligations -> PSE_live;
- genuinely novel post-stop breaks -> reopening latency.

This prevents future-oracle scoring.

## Holdout integrity

The benchmark materialized 468 traces:
- 108 discovery;
- 144 calibration;
- 216 untouched holdout.

Three independently coded adapters generated:
- engineering fault localization;
- measurement/model discrimination;
- scientific search/allocation.

Twelve forcing families were represented in every domain.

Holdout seeds were mechanically SHA256-derived from the preseal commit and were not hand-selected.

The raw and lag policies shared the same holdout worlds.

## Baselines

Calibration selected:
- FIXED-k: k=12;
- PATIENCE-h: h=6.

Holdout totals:

~~~text
STOP_NOW      PSE=288 AE=288 OIW=0.0
CONTINUE_ALL  PSE=0   AE=0   OIW=2367.0
FIXED-12      PSE=24  AE=24  OIW=1458.0
PATIENCE-6    PSE=54  AE=54  OIW=1227.5
~~~

Calibrated OQSC-LAG-1 was not Pareto-dominated by the tuned fixed or patience baseline in any domain.

## Counterfactual continue/stop replay

Raw OQSC had 51 first-stop episodes where continuing the already-live inquiry would still reveal material information.

The calibrated successor had zero such episodes in holdout.

~~~text
RAW: material_continue=51
LAG-1: material_continue=0
~~~

This is an evaluation intervention on frozen generated traces, not a causal model of human scientists.

## Reopening latency

On the generated reopen families:

~~~text
RL_max=0
MISSED_REOPEN=0
~~~

for both raw and calibrated OQSC.

New post-stop contact therefore did not create the raw rule's 51 premature errors; those errors came from still-live current inquiry obligations.

## Literature pressure

The post-preseal literature eliminates generic novelty claims for:
- rational inquiry stopping under unresolved uncertainty;
- end-of-inquiry higher-order uncertainty;
- speed–accuracy trade-offs between stopping rules;
- sufficiency/closure without exhaustiveness;
- value of information in stopping;
- resource-bounded metareasoning;
- active data selection/sensing;
- prioritized scientific search;
- robust/adaptive decision under deep uncertainty.

The surviving candidate is narrower: prospective calibration of MQR's own constitutional stop receipt under hidden finite known-outcome traces, with live-obligation premature-stop error, over-inquiry cost, reopening latency, baseline tuning custody and same-kernel cross-domain transport.

## Real-Language v0.18

Candidate/live surface:
- Rust: `language/real/src/stop_v18.rs` / `real-v18-stop`
- independent relational evaluator: `language/real/prolog/stop_v18.pl`
- calibration harness: `experiments/mqr-4.51/benchmark.py`
- finite Lean boundary: `language/real/lean/MQR/StoppingCalibration.lean`
- constitution: `language/real/V18-STOPPING-CALIBRATION.md`

Canonical guards:

~~~text
stop.hidden_gold_access=NO
stop.future_oracle=NO
stop.post_holdout_policy_repair=FORBIDDEN
stop.primary_scalar_score=OFF
stop.external_calibration=HOLD
stop.universal_optimality=FORBIDDEN
stop.guidance_mode=CALIBRATED_REOPENABLE_STOP
~~~

## Claim ceiling

Earned:

~~~text
PROSPECTIVELY CALIBRATED
INTERNAL CROSS-DOMAIN
STOPPING COMPETENCE

FOR P-OQSC-LAG-1
ON THE DECLARED
MQR-4.51 BENCHMARK FAMILY
~~~

Not earned:

~~~text
RAW OQSC CALIBRATION
EXTERNAL SCIENTIFIC CALIBRATION
UNIVERSAL LAMBDA=1
UNIVERSAL STOPPING OPTIMALITY
REAL-WORLD EFFECTIVENESS
FUTURE REFINEMENT CLOSURE
~~~

## First authoritative receipt

~~~text
head = 458c1bbeb37f876dde3189ed08226ee52f6aca78
run  = 36382410016
court = SUCCESS
raw_oqsc = FAIL
calibrated_lag_1 = PASS
~~~

Final closure requires integrated Real-Language and Lean same-head replay plus final main-only branch audit.
