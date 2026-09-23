# MQR-4.10 — Context-Isolated Fresh-Source Adjudication, Compiler–Predictor Separation, Mechanical Scoring, Post-Training Live Engineering Measurement & Whether All Four Blindness Axes Can Be Jointly Satisfied

## 0. Purpose
MQR-4.10 tests whether the four blindness dimensions frozen in MQR-4.8 can be jointly realized in a fresh engineering execution:

1. SEQUENCE-HELD-OUT
2. IDENTITY-MASKED
3. CONTEXT-INDEPENDENT
4. TRAINING-INDEPENDENT OUTCOME

The stage explicitly reuses canonical literature and Harvest rather than inventing a new evaluator theory.

## 1. Literature / Harvest inheritance
### Stegenga & Menon (2017)
Robustness requires genuine independence; nominal diversity does not guarantee confirmational independence.

MQR consequence:
DIFFERENT ROLE / PROMPT / LABEL != INDEPENDENT EVALUATION.

### MQR LR-20260914-C/D
Method-count and mode-count are not independence.
Same-data or same-pipeline multiplicity can reproduce shared error.

### MQR-3.35
Already froze:
- same model with another prompt;
- same conversation with another role;
- self-critique;
- delayed rereading
do not count as independent evaluator execution.

### ScienceAgentBench (Chen et al. 2025)
Contamination control is executable:
- alter/withhold evaluation-critical data;
- hide test labels;
- use executable success criteria.
Prompt instructions alone are insufficient.

### REFLECT (Lin et al. 2026)
Narrative attribution is weaker than targeted intervention + execution-grounded outcome change.

### Parvinian et al. / NASA M&S credibility
Evidence rigor is context-of-use dependent.
Calibration/development evidence is not interchangeable with validation evidence.
Scope, uncertainty, applicability and caveats remain explicit.

This literature synthesis was canonically stored as:
MQR Literature Harvest LR-20260923-A — Evaluation Independence, Contamination-Resistant Scientific Benchmarks, Intervention-Grounded Attribution & Context-of-Use Credibility.

## 2. Preferred isolated runtime failed cleanly
A separate Hugging Face CPU job was attempted as the preferred predictor runtime.

Result:
HTTP 402 / compute unavailable on current account.

No substitute external LLM was fabricated.

Fallback:
a deterministic computation runtime receiving only explicit numeric/time inputs and no conversational hidden state.

This is:
CONTEXT-FREE MECHANICAL RUNTIME.

It is NOT:
INDEPENDENT LANGUAGE-MODEL EVALUATOR.

## 3. Elering first attempt — invalid-as-blind
An initial 4.10 masked Elering baseline fetch returned timestamp:

1790142300

This was the exact snapshot already revealed in MQR-4.9.

Therefore even though frequency was withheld in the new C1 call, the adjudicator already knew its outcome from the previous stage.

Verdict:
INVALID-AS-BLIND / PRESERVED AS LEAKAGE WITNESS.

This is a concrete demonstration that field masking cannot restore blindness to an already-seen case.

## 4. Elering Lane D — freshness gate
Preseal:
272efe671ab186172ca90c4035bd0f654ef551b5

Frozen rule:
accept only timestamp > 1790142300.

Fresh fetch again returned:
1790142300.

Verdict:
NO-NEW-SNAPSHOT.

No predictor receipt was created.
No outcome was reused.

## 5. Rail Lane E — context-free mechanical path sanity
Preseal:
ed0192e24781ac002dd53d26c3231d30046f6865

C1 selection:
first live train / first timetable row under frozen rule.

Compiler-visible identity:
- date 2026-09-22
- train 265
- HKI
- DEPARTURE
- scheduled 2026-09-22T16:29:00Z

Predictor received scheduledTime only.

Predictor receipt:
54841c54a4976247d4e52346e5facf5254acba8b

C2 reveal:
actualTime = 2026-09-22T16:29:17Z
liveEstimateTime = null

Mechanical delay:
+17 s

Frozen scorer:
A_CONSISTENT (|delay| <= 30 s).

Interpretation:
This validates the masked mechanical execution path but does not establish training-independent outcome because the event was historical relative to the 4.10 preseal and no training-exclusion evidence exists.

## 6. Rail Lane F — future-event prospective lane
Preseal:
febef2fcb6b0e5b7f1f18ab51dccb60968569a79

Frozen temporal gate:
eligible timetable rows must have scheduledTime >= 2026-09-23T06:10:00Z.

Deterministic selection:
earliest eligible row among first 20 live trains, independent of outcome fields.

C1 selected:
- date 2026-09-23
- train 1
- LRS
- ARRIVAL
- scheduledTime 2026-09-23T06:10:00Z

Predictor received scheduledTime only.

Predictor receipt:
34c66b5db0d1fd4f80b9d7b753117d1f14b2505c

Frozen rivals:
- A static timetable: ±30 s
- B operational-state: material deviation allowed
- STRONG_B if |delay_est| >= 120 s

## 7. Lane F held-out reveal
C2 exact-row reveal returned:

liveEstimateTime = null
actualTime = 2026-09-23T06:24:56Z

The actual realized delay is:

14 min 56 s = 896 s.

If actualTime were admissible, this would satisfy STRONG_B by a very large margin.

But the preseal explicitly states:

if liveEstimateTime is null and actualTime exists only after event occurrence, Lane F is INCONCLUSIVE for the post-preseal prediction; do not substitute another outcome.

Therefore:

LANE F VERDICT = INCONCLUSIVE.

The 896-second tempting post hoc success is constitutionally inadmissible.

## 8. Why the strong actual result is not used
Using actualTime after seeing that liveEstimateTime is null would change the outcome contract post reveal.

That would violate:
- ScienceAgentBench-style executable evaluation integrity;
- MQR-3.35 anti-self-certification;
- MQR-4.8 outcome-sealing doctrine;
- MQR's own preseal rule.

Thus:

POST-HOC BETTER OUTCOME != ADMISSIBLE EVIDENCE.

This is a positive rigor result even though it blocks a scientific win.

## 9. Four-axis adjudication
### Axis 1 — SEQUENCE-HELD-OUT
Lane F:
PASS.

Predictor receipt existed before C2 reveal.

### Axis 2 — IDENTITY-MASKED
Predictor runtime:
PASS.

It received only scheduledTime + fixed thresholds.

It did not receive train identity, station, domain or source URL.

### Axis 3 — CONTEXT-INDEPENDENT
NARROW PASS / GLOBAL HOLD.

PASS for deterministic predictor/scorer runtime:
no conversational hidden context entered the computation.

HOLD at experiment-governance level:
the same ChatGPT context selected the source family, designed rivals and interpreted the final result.

Therefore:
MECHANICAL CONTEXT ISOLATION != INDEPENDENT SCIENTIFIC EVALUATOR.

### Axis 4 — TRAINING-INDEPENDENT OUTCOME
For the realized actualTime of the future event:
outcome occurred after the preseal and therefore cannot have been part of pretraining.

However actualTime was not an admissible Lane-F scoring field.

The admissible field liveEstimateTime was null.

Therefore:
TRAINING-INDEPENDENT OUTCOME EXISTS / ADMISSIBLE SCORING OUTCOME ABSENT.

## 10. Joint four-axis verdict
All four blindness axes were NOT jointly satisfied for one admissible scored outcome.

The closest lane achieved:
- sequence holdout;
- identity masking;
- mechanical runtime isolation;
- a genuinely post-preseal realized outcome;

but the frozen admissible outcome field was missing.

Thus:

ALL-FOUR JOINT SATISFACTION = HOLD.

This is stronger than falsely declaring success using the actualTime after reveal.

## 11. Source-adequacy consequence
MQR-4.9 established:
freshness != discriminative adequacy.

MQR-4.10 strengthens this:

FRESHNESS + MASKING + RUNTIME ISOLATION != COMPLETE BLIND ADJUDICATION
unless the prospectively admissible outcome field is actually available.

Outcome-schema adequacy is part of the preseal.

## 12. Mechanical scoring result
Mechanical scoring removes:
- post-reveal threshold drift;
- free-form judge preference;
- hidden prompt changes.

But it does not remove:
- source choice;
- rival choice;
- threshold design;
- compiler bugs;
- provenance problems.

Therefore:
MECHANICAL != EPISTEMICALLY INDEPENDENT BY ITSELF.

Its value is inspectability and immutability.

## 13. Literature backflow result
The existing corpus substantially predicts the 4.10 outcome.

- Stegenga & Menon: independence is structurally demanding.
- LR-20260914-C/D: multiple routes do not automatically create independent evidence.
- ScienceAgentBench: contamination defenses must alter the executable evaluation surface.
- REFLECT: intervention/execution outcomes should ground attribution.
- Parvinian/NASA: credibility is context-of-use and evidence-role dependent.
- MQR-3.35: internal role switching cannot certify external reliability.

Therefore MQR-4.10 adds no independent-evaluation novelty.

Its contribution is constitutional integration and disciplined refusal to consume inadmissible evidence.

## 14. Generation-IV authority consequence
A Generation-IV authority object for AI-mediated scientific adjudication must now distinguish:

- source freshness;
- source identity masking;
- outcome sealing;
- predictor runtime isolation;
- experiment-level evaluator independence;
- admissible outcome-schema completeness;
- world-contact provenance.

These belong as typed evidence metadata, not new constitutional primitives.

## 15. Strongest result
The strongest MQR-4.10 result is negative but operational:

> A formally stronger, outcome-blind execution can rationally end with less apparent evidence than an informal analysis, because presealed admissibility blocks opportunistic substitution after reveal.

In compact form:

RIGOR CAN CONTRACT EVIDENCE.

That contraction is a feature, not a failure.

## 16. Next pressure
Do not add another conceptual blindness axis.

The next valid step is to solve the remaining execution debt:

1. choose a source whose admissible held-out field is guaranteed available;
2. use a genuinely isolated external predictor if available;
3. keep mechanical scoring;
4. preserve post-preseal/future measurement;
5. freeze source-schema adequacy before execution.

If external compute remains unavailable, MQR must not relabel a deterministic runtime as an independent model evaluator.

## 17. Verdict
**PASS-CONTEXT-ISOLATION-STRESS / LITERATURE-HARVEST-BACKFLOW-ACTIVE / HF-EXTERNAL-RUNTIME-UNAVAILABLE-NOT-LAUNDERED / REUSED-ELERING-SNAPSHOT-CAUGHT-AS-BLINDNESS-FAIL / FRESHNESS-GATE-NO-NEW-SNAPSHOT / LANE-E-MECHANICAL-PATH-A-CONSISTENT / LANE-F-FUTURE-EVENT-PRESEAL-PASS / IDENTITY-MASKED-PREDICTOR-PASS / SEQUENCE-HELD-OUT-PASS / DETERMINISTIC-RUNTIME-CONTEXT-ISOLATION-PASS-NARROW / POST-PRESEAL-ACTUAL-OUTCOME-EXISTS-BUT-INADMISSIBLE / LIVE-ESTIMATE-MISSING / POST-HOC-ACTUALTIME-SUBSTITUTION-REFUSED / ALL-FOUR-JOINT-SATISFACTION-HOLD / RIGOR-CAN-CONTRACT-EVIDENCE / NO-NEW-EPISTEMIC-PRIMITIVE / GENERATION-IV-CONTINUES.**