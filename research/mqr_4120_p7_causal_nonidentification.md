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

## Retrospective prior-work and novelty correction (2026-10-17)
**MQR-4.89 directly anticipated this countermodel.** See [the prior exact-rational causal/nonidentifiability bridge](../experiments/mqr-4.89/causal_nonidentifiability_bridge.py), itself a bridge to [MQR-4.87 source-family adjudication](../experiments/mqr-4.87/real_lang_p1.py). It uses U~Bernoulli(1/2), identical observed diagonal laws, and two causal orientations with different do-distributions; it returns HOLD_CAUSAL_WARRANT_NONIDENTIFIABLE despite a hypothetical source-family AUTHORIZED_FOR_USE. P7 relabels the variables and uses the same *identification-obstruction pattern*. It does **not** establish a new nonidentification theorem, new empirical causal finding, or a new general warrant principle. The P7 [0,1] sharp bound is a scoped illustration for the specified binary law under consistency, not an independent discovery.

Crucial difference in construction: 4.89 contrasts X=U,Y=X with Y=U,X=Y; P7 contrasts A=U,Y=U with A=U,Y=A. These are not literally identical SCM pairs, although their observed laws and ATE extremal pattern coincide. The scientifically substantive unresolved work is *transport*: define a well-specified remedial intervention and actual outcome, locate legitimate observational or interventional records with independent provenance, and show the inference is licensed within its claim scope. Re-running exact arithmetic, adding languages, or another staged filename is not such evidence.

Review also reconnects the older MQR program: non-injective measurements/observational quotient at origin; 4.53 non-universal progress metric; 4.76 ancestry-sensitive independence; 4.87 scoped source receipts; 4.89 causal HOLD; 4.101–4.104 fallible verification/adjudication; 4.113 stochastic experimental comparisons; 4.114 calibration source ancestry; 4.117 unencoded objections; 4.118 translation and Kuhn; 4.119 contestable exemplar evaluation. All inherited Greenberg/CCQM/Harvest and unperformed R0/R+/E evaluations remain HOLD. Before P8, require a prior-art/genealogy gate rather than more synthetic checkers by default.
