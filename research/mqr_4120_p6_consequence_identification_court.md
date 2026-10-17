# MQR-4.120 P6 — Consequence Observation, Counterfactual Support and Scope-Limited Repair

2026-10-17. P6 is a **bounded, synthetic methodological exercise**. No real institutional or causal effect has been established.

## Inherited lineage
P1 established J1 conditional scientific warrant and J2 evaluation authority. P2 blocked transfers of warrant across their types. P3–P4 audited declared ancestry and edge erasure. P5 distinguished receiving a complaint, reopening a question, power to remedy, actual intervention, and an observed consequence. P6 tests why those stages cannot be silently collapsed into causal impact.

## Estimand and identification
For a well-defined intervention A and outcome Y, the average effect E[Y(1)-Y(0)] concerns counterfactual potential outcomes, not merely before/after change. Identifying it requires defensible assignment or exchangeability assumptions, measurement consistency, positivity where applicable, temporal ordering, source independence and an explicit intervention/target scope. Confounding, co-interventions, reporting changes and selection can all defeat naive attribution. These are classical causal-inference considerations, not new MQR theorems.

## Synthetic executable
[Eight local fixture gates](../experiments/mqr-4.120/p6_consequence_gate.py) separate (1) all declared hypothetical preconditions, (2) out-of-scope remedy, (3) absent order, (4) unverified implementation, (5) absent post-observation, (6) dependent observation ancestry, (7) incomparable baseline and (8) unaddressed confounding. Local Python execution yielded eight of eight expected classifications, but all flags are stipulated booleans. The strongest outcome is named CONDITIONAL_CAUSAL_SUPPORT_IN_FIXTURE rather than world-grounded causal PASS.

## Critical reservations
Passing seven booleans does NOT in reality identify the ATE. In particular, a 'confounding_addressed' flag does not show conditional exchangeability or a credible identification design; 'independent_observation' is not evidence authenticity. This is a schema sanity test only. In a genuinely investigated case, ask for the intervention assignment mechanism, outcome timestamps, denominator, counterfactual support, competing causal explanations, and provenance of implementation and outcome records. The null result and the existence of a remedy without demonstrated measurable consequences remain legitimate results.

## P7 research fork
Construct two observationally indistinguishable synthetic causal worlds with different intervention effects, then demonstrate why the P6 boolean audit is not a sufficient identification criterion. Reuse earlier MQR observational-equivalence and partial-identification tools; P7 should avoid an unrelated problem. Existing Greenberg seven ambiguous rows, CCQM standard-custody gaps, 4.118 Harvest candidates, and 4.119 R0/R+/E unevaluated human cognition all remain HOLD.