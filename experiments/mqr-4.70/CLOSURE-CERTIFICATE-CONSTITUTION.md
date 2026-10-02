# MQR-4.70 — Admissible-Envelope Closure Certificate Constitution

Status: **PRE-RESULT / THEORY-AXIS-OPEN / BLACKWELL-RELATIVE-SUFFICIENCY-BASELINE / OPEN-WORLD-HOLD**

## Motivation

MQR-4.70 has now absorbed the following into established theory:

- input-conditioned predictive state;
- separating intervention systems;
- adaptive experiment selection;
- minimally sufficient experimental design;
- comparison and deficiency of statistical experiments;
- alternative minimal probe bases.

The surviving question is not whether one can optimize or compare experiments inside a declared family.

It is:

> What warrants treating a declared intervention or measurement family as sufficiently closed for a scientific state-minimality claim?

## Core distinction

Let:

- H be a declared hypothesis/history/model space;
- A be a scientifically admissible intervention envelope;
- U be the currently admitted finite or represented family, U subseteq A;
- R(h,u) be the declared response semantics.

A predictive quotient relative to U is:

    h ~_U h'
    iff
    for every u in U,
    R(h,u) = R(h',u).

A family-relative minimality claim is local unless there is additional warrant that U represents A adequately for the declared scientific purpose.

## Closure certificate hierarchy

### C0 — No closure certificate

Only U-relative minimality is earned.

Canonical authority:

    LOCAL_FAMILY_RELATIVE_MINIMALITY

Exterior-probe debt remains OPEN.

### C1 — Finite enumeration certificate

A is finite and independently frozen, and U has been exhaustively checked against every element of A.

Authority:

    FINITE_ENVELOPE_COMPLETENESS

This does not transport beyond A.

### C2 — Response-signature closure certificate

Every admissible intervention a in A is proven response-equivalent, on the declared H, to some represented intervention or represented composition in U.

Formally, for every a in A there exists u* in closure(U) such that:

    for every h in H,
    R(h,a) = R(h,u*).

Authority:

    H_RELATIVE_RESPONSE_CLOSURE

This is stronger than finite enumeration when A is generated symbolically or is infinite but has finitely many response signatures.

### C3 — Separation-profile closure certificate

For every pair h,h' still equivalent under U, no admissible intervention in A separates them.

Equivalent form:

    SEP_A(h,h') is empty
    for every h ~_U h'.

Authority:

    H_RELATIVE_PARTITION_CLOSURE

This is exactly sufficient for the current predictive partition, but need not preserve richer decision-theoretic information.

### C4 — Blackwell-class domination certificate

Construct the joint experiment E_U induced by the admitted family.

For a declared parameter/model class and decision-problem class D, every admissible future experiment E_a is Blackwell-dominated by E_U, or is deficient by no more than a declared tolerance.

Authority:

    DECISION_CLASS_RELATIVE_EXPERIMENT_CLOSURE

This is not universal scientific closure. It is indexed by:
- model/parameter class;
- observation semantics;
- decision-problem class;
- exact or approximate domination criterion.

### C5 — Generative-envelope closure certificate

A is specified by an independently warranted intervention grammar G.

The grammar is shown to generate every intervention admitted by the declared scientific scope, and the induced response/separation signatures of G are completely represented by U or by a proven quotient of U.

Authority:

    GRAMMAR_RELATIVE_ADMISSIBLE_ENVELOPE_CLOSURE

This level requires an independent argument that G itself captures the admissible scientific scope.

### C6 — Open-world scientific closure

Not authorized by MQR-4.70.

No finite executable Court, statistical-experiment order, or grammar proof inside a currently declared ontology can by itself establish that no scientifically relevant future intervention can arise outside that ontology.

Canonical status:

    OPEN_WORLD_CLOSURE_NOT_EARNED

## Important non-equivalences

    RESPONSE CLOSURE
    !=
    BLACKWELL CLOSURE

    BLACKWELL CLOSURE FOR D
    !=
    CLOSURE FOR ALL FUTURE SCIENTIFIC PURPOSES

    GENERATIVE GRAMMAR COMPLETENESS
    !=
    WORLD COMPLETENESS

    NO KNOWN EXTERIOR SEPARATOR
    !=
    PROOF OF NO ADMISSIBLE EXTERIOR SEPARATOR

## Latest literature pressure

### Torgersen 1991
Experiment deficiency, randomization, equivalence, sufficiency and local comparison are mature baselines.

### Barnett & Crutchfield 2015
Input-conditioned predictive-state minimality is mature baseline machinery.

### Elahi et al. 2024
A graph separating system plus adaptive allocation and stopping can justify local causal-identification sufficiency under declared assumptions.

### Tigas et al. 2022
Experiment choice can be optimized over target and intervention value through expected information gain.

### Gevertz & Kareva 2024
Minimally sufficient experiment design is already operationalized through practical identifiability and experimental cost.

### Lahiry 2026
A very recent quantum-statistical result explicitly defines sufficiency relative to a prescribed measurement class using Blackwell domination, while separating:
1. reduction of the measurement class;
2. identification of a sufficient measurement inside that class.

This is a direct baseline for the C4 layer.

MQR-4.70 therefore gets no novelty credit merely for separating family reduction from within-family sufficiency.

## Candidate MQR residue

The candidate contribution is now a typed authority discipline:

> Every state-minimality claim should carry the strongest independently warranted closure certificate actually available, and should not inherit authority from stronger closure levels.

In particular:

    LOCAL MINIMALITY
    MUST NOT BE LAUNDERED INTO
    OPEN-WORLD MINIMALITY

## Falsification / absorption rule

If established experiment-comparison, active-design, formal testing and domain-specific admissibility theory already provide an equivalent closure-certificate hierarchy with the same authority boundary, MQR-4.70 should report BASELINE_ABSORBED.

If the hierarchy adds no predictive, audit, transport or error-prevention value, it should not be promoted.

## Naturalistic burden

The K562 Perturb-seq lane should be used to test:
- C0 local family-relative state;
- a finite held-out approximation to C1;
- whether held-out perturbations expose exterior separation debt;
- whether a domain-specific perturbation grammar can support a stronger C2/C3 claim.

No current K562 analysis can earn C6.
