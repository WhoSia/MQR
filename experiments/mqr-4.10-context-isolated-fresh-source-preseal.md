# MQR-4.10 — Context-Isolated Fresh-Source Adjudication — PRESEAL

## Literature/Harvest inheritance
This design reuses already-custodied and harvested constraints rather than inventing a new evaluator theory.

1. MQR-3.35: same model + different prompt/role/self-critique does NOT count as independent evaluation.
2. LR-20260914-C/D + Stegenga & Menon (2017): nominal diversity does not establish evidential independence; shared dependencies must be exposed.
3. ScienceAgentBench (Chen et al. 2025): contamination/shortcut mitigation requires modifying/withholding evaluation-relevant information and executable success criteria.
4. REFLECT (Lin et al. 2026): correction/attribution must be grounded by targeted intervention and execution outcomes, not narrative judgment alone.
5. Parvinian et al. (2019) + NASA M&S credibility doctrine: evidence rigor is context-of-use dependent; calibration/development evidence is distinct from validation evidence; scope/caveats remain explicit.

## Runtime integrity
Preferred isolated Hugging Face CPU job was attempted but unavailable due account compute/payment restriction.
Fallback is a deterministic local computation runtime with no access to conversational hidden context beyond explicit numeric inputs.

This is NOT an independent language-model evaluator.
It is a context-free mechanical predictor/scorer.

## Live source
Fresh Elering/NordAPI current system snapshot.

## Two-stage compiler
Stage C1 before prediction may expose ONLY:
- timestamp t;
- production p;
- consumption c.

Frequency f and any balance field are forbidden from the C1 return.

Stage C2 may expose frequency ONLY after a prediction receipt has been generated and frozen.

## Identity masking
The mechanical predictor receives only:
- u = p;
- v = c;
- threshold delta = 100.

It receives no source name, country, engineering-domain labels, frequency, balance field, URL, or timestamp.

## Frozen rivals
Rival A (island-coupled rule):
if |u-v| >= 100, predict held-out outcome class DEVIATED, meaning |f-50| >= 0.02 Hz with sign matching u-v.

Rival B (interconnection rule):
if |u-v| >= 100, predict held-out outcome class NEAR_NOMINAL_ALLOWED, meaning |f-50| <= 0.01 Hz is allowed despite large |u-v|.

## Mechanical predictor output
Given u,v:
- compute d = u-v;
- if |d| < 100 => NOT_SEPARATING;
- else output both frozen rival expectations and SEPARATOR_READY.

## Mechanical scorer
After reveal of f:
- STRONG_B if |d| >=100 and |f-50| <=0.01;
- A_CONSISTENT if |d| >=100 and |f-50| >=0.02 and sign(f-50)=sign(d);
- INCONCLUSIVE otherwise.

No narrative override is allowed after reveal.

## Four blindness axes targeted
SEQUENCE-HELD-OUT = target YES.
IDENTITY-MASKED = target YES for mechanical predictor.
CONTEXT-INDEPENDENT = target YES for deterministic runtime only, NOT for source/compiler selection.
TRAINING-INDEPENDENT OUTCOME = target YES because fresh telemetry is generated post-training.

## Acceptance rule
All-four-joint satisfaction may be claimed ONLY in the narrow execution-path sense if:
1. C1 returns no f;
2. predictor receipt exists before C2;
3. predictor saw masked u,v only;
4. scorer is purely mechanical;
5. C2 timestamp matches C1 snapshot;
6. fresh outcome was generated after training.

Otherwise contract the corresponding label.

## Authority ceiling
Even if STRONG_B:
only scoped support for wider interconnection/balancing structure is licensed.
No exact inertia, interchange, droop, reserve contribution, or full grid ontology is inferred.