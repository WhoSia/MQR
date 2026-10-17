# MQR-4.119 P1 — Preregistered Recognition and Rule-Revision Challenge

2026-10-17. ACTIVE 4.119 / P1 DESIGN ONLY. No participant experiment or CI completed.

## Research question
Can an explicitly specified rule learner or decision system generalize to genuinely unseen UV–Vis anomaly cases as well as an exemplar-trained reasoner, without post hoc rule patching? Distinguish noticing, diagnosing, requesting discriminating evidence, and justifiably changing the question.

## Frozen competing strategies
R0: documented baseline SOP with explicit checks and a fixed escalation rule, all frozen before test examples. R+: richer formal inference/update model, also frozen; it must have access to no extra observations unavailable to E. E: exemplar-conditioned reasoning trained on a specified demonstration set without seeing the held-out test families. A fully skilled human is NOT thereby operationalized by a toy E algorithm.

## Holdout structure
Training includes ordinary blank drift and a plausible calibration-range violation. Hold out three *families*: (H1) interference with spectral overlap, (H2) matrix-effect causing nonlinear concentration response, (H3) standard-custody inconsistency despite plausible final absorbance. These are hypothetical protocol families, not actual recorded failures. Freeze family labels, scenario generators, evidence access, training material, model prompts/rules, and scoring rubrics before evaluating. Avoid shared wording and same underlying simulator seed across training/test; blind adjudicators to strategy identity when feasible.

## Separate outcomes
1. Recognition: did the system flag a scientifically material challenge?
2. Diagnosis: did it name a causal candidate without converting speculation to fact?
3. Discriminating test: did it propose a feasible observation that separates alternatives?
4. Question revision: did it notice when mere calculation accuracy was the wrong target?
5. Calibration of confidence: does stated certainty track available evidence?
6. Provenance and source integrity: are invented custody certificates or experimental observations absent?
Report each axis and raw cases; do not combine into one scalar 'scientific understanding' score. Panel disagreement is itself research data.

## Adversarial checks
- R+ success is allowed to challenge the claim that recognition resists formalization.
- E failure on a shifted family is allowed to challenge exemplar superiority.
- A fluent narrative without valid distinguishing evidence gets no inferential credit.
- If adjudicators disagree about relevance, preserve their disagreement rather than force unanimous PASS.
- Changing allowed inputs after reviewing the test set invalidates the comparison.

## Interpretive and empirical ceiling
Kuhn 1974, Second Thoughts on Paradigms (Drive 1-jK0eaCXH_RvXRvFgrUCXMO_Yh8GLyiy), motivates exemplar/rule distinction but does not predict this benchmark's outcome. Original MQR method-to-logic graph, 4.114 calibration independence, 4.115 citation provenance, 4.116 archival selection, 4.117 unencoded objection and 4.118 translation work remain inherited. Historical source claims and physical witnesses HOLD.

P2 obligation: build frozen case cards and runnable deterministic sanity checks, explicitly distinguishing constructed simulation from actual human comparison.
