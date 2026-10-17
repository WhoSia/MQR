# MQR-4.120 P7 — Observational Equivalence, Causal Nonidentification and Repair Consequences

2026-10-17. BOUNDED classical synthetic countermodel, not observational proof of real-world effects.

## Continuity
4.119 evaluation legitimacy -> 4.120 J1/J2 dual ledger -> P3/4 dependency and provenance -> P5 procedural repair vs outcome -> P6 outcome vs causal effect. P7 returns to early MQR observational equivalence and partial-identification tools rather than introducing a disconnected theme.

## Exact finite construction
Let U be Bernoulli(1/2), observed intervention A=U, and binary outcome Y. Model M0: Y=U; model M1: Y=A. Both observational distributions are P(A=0,Y=0)=P(A=1,Y=1)=1/2 and zero otherwise. Under do(A=a), M0 gives Y=U, so ATE=0. M1 gives Y=a, so ATE=1. Hence observed law equality does not imply causal-effect equality.

[Exact rational Python witness](../experiments/mqr-4.120/p7_observational_equivalence.py) runs algebraic assertions for observational equality, intervened-law difference, both ATE endpoints, and partial-identification limits. Local Python execution passed exact arithmetic checks.

## Sharp partial-identification range
Assuming only consistency of potential outcomes and the stated binary observed law (without ignorability or randomization), E[Y(1)] lies in [1/2,1], E[Y(0)] lies in [0,1/2], hence ATE lies in [0,1]. Both endpoints are attained by M0 and M1. Under this observed distribution, no further generic causal point estimate is justified. Adding valid randomization, exchangeability, instrumental variables or restrictions may shrink the set; the example does not deny identification under stronger assumptions.

## Evidence ceiling
These are constructed SCMs and a classical observation-versus-intervention distinction, not a new theorem or evidence of an actual appeal body causing real changes. A registry receipt or an independently logged post-event outcome does not by itself supply the unobserved counterfactual. The P6 boolean 'confounding_addressed' cannot certify identification.

## P8
Examine intervention-definition drift: 'order issued', 'implementation', 'successful correction' are different treatments with noncompliance and selection. Separate intention-to-treat from effect of actual repair and check whether the treatment itself is well defined and documented. Carry Greenberg seven-row, CCQM source-custody, 4.118 Harvest and 4.119 R0/R+/E HOLD.
