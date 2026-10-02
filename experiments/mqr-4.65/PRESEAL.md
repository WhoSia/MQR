# MQR-4.65 — Scientific-Reachability Constraint Compilation Court

Status: **PRESEALED / MAIN-ONLY / PRE-EXECUTABLE-REVEAL / PRIOR-HARVEST-ACKNOWLEDGED**

## Formal name

**MQR-4.65 — Scientific-Reachability Constraint Compilation Court, State-Augmentation Sufficiency, Typed Diagnostic→Constraint→Policy Translation, Behavioral and Reachability Bisimulation, Strong-Baseline Representability, Open-Frontier State Nonclosure, Endogenous Rival-Genesis Compilation Failure, Minimal Nonrepresentability Witnesses & Whether MQR Acquisition Authority Reduces Losslessly to Ordinary Constrained Sequential Planning Once the Planner Is Given the Right Scientific State Variables**

## Canonical parent

MQR-4.64 canonical head:

`74ea204d90567e5f873b5aac688eb6ae98672cb0`

Inherited scientific result:

- binding is relational, not intrinsic;
- minimum-separator OPR is fully absorbed by a matched constrained baseline in the frozen 4.64 grammar;
- NEDL has local nonabsorption when multiple future separators are non-substitutable;
- ARR / EAI / EXTERIOR can bind locally and can overconstrain;
- every surviving 4.64 typed constraint is still expressible as an ordinary state/action feasibility predicate in that finite grammar;
- binding action authority does **not** establish MQR-specific control semantics;
- REALACQUIRE 0.29 remains current; v0.30 is unearned.

## Prior-Harvest acknowledgment

Before 4.65 opened, the literature Harvest had already sharpened several pressures:

- Blackwell comparison can be decision-universal inside a fixed experiment/state constitution without being a scalar whole-science ruler.
- Lindley expected information is weaker than Blackwell decision dominance even when it orders some experiment pairs.
- Bernardo shows that an epistemically described information objective can be represented as Bayesian expected utility after an appropriate decision-space constitution.
- Ay–Jost–Lê–Schwachhöfer show that invariance under sufficient statistics can positively characterize Fisher geometry relative to a declared category of models/transformations.
- Yamaguchi–Nozawa show that approximate sufficiency can be represented by a quantitative bounded-distortion condition inside an explicit validity region.

These sources are **pressure**, not 4.65 outcomes. No result below may be mutated after executable reveal to agree with them.

## Explanandum lock

4.65 does **not** ask whether MQR vocabulary is distinctive.

It asks:

> If an ordinary constrained sequential planner is given all contemporaneously admissible scientific state variables needed by a surviving MQR acquisition constraint, can the constraint and its induced policy/reachability behavior be compiled losslessly into ordinary state/action constraints and state augmentation?

The target chain is:

```text
MQR DIAGNOSTIC
→ BINDING CONSTRAINT
→ DECLARE SOURCE-STATE DEPENDENCE
→ COMPILE SCIENTIFIC STATE
→ COMPILE FEASIBLE-ACTION PREDICATE
→ BEHAVIORAL EQUIVALENCE?
→ REACHABILITY BISIMULATION?
→ RELEASE EQUIVALENCE?
→ NONREPRESENTABILITY WITNESS?
```

## Source semantics

A source MQR acquisition system is a tuple:

`M = (H, O, A, T, X, C, L, R)`

where:

- `H`: finite histories;
- `O(h)`: contemporaneously observable scientific state at history `h`;
- `A(h)`: physically/logically available actions;
- `T(h,a)`: next-history transition relation or kernel;
- `X`: typed acquisition-constraint family;
- `C_x(h,a)`: whether action `a` is admissible under typed constraint `x`;
- `L_x(h)`: whether authority for `x` is live or released;
- `R_H(h,a)`: declared future scientific-reachability labels over horizon `H`.

The initial typed family is inherited from 4.64:

- OPR;
- ARR;
- EAI;
- EXTERIOR;
- NEDL.

4.65 may test additional **syntactic forms** of history/frontier dependence, but it may not invent a favorable new scientific constraint after reveal.

## Target ordinary planner

The target planner is not allowed to receive an MQR policy-output lookup table.

A compiled planner is:

`P = (S+, φ, A+, T+, G, Q)`

where:

- `S+`: augmented planner state;
- `φ : H → S+`: admissible state compiler;
- `A+(φ(h)) = A(h)`: same physical action set;
- `T+`: transition induced from source transitions through `φ`;
- `G_x(s+,a)`: ordinary feasibility predicate;
- `Q`: ordinary objective/tie-breaking mechanism, frozen independently of the source output.

The compiler may use only information derivable from contemporaneously admissible history/observations.

## Admissible compiler classes

Representability will be tested cumulatively.

### C0 — BASE-STATE

No added memory or scientific variables beyond the baseline planner state.

### C1 — FINITE-FEATURE AUGMENTATION

Adds a frozen finite tuple of contemporaneously observable/derivable scientific variables such as:

- irreversibility;
- separator count/identity class;
- separator substitutability;
- reopening-route liveness;
- ancestry-independence summaries;
- exterior-route liveness;
- typed debt counters.

### C2 — FINITE-MEMORY PRODUCT STATE

Adds a bounded-memory summary or a finite automaton state updated compositionally from observations/actions.

### C3 — GENERIC FINITE-SET / GRAPH STATE

Allows generic finite containers whose cardinality can grow with observed history:

- live rival set;
- separator relation;
- ancestry/provenance graph;
- reopening-route set;
- exterior-access relation.

The schema/container type must be frozen; newly observed members may be added online.

### C4 — FULL FINITE-HISTORY REFERENCE

Allows the entire finite contemporaneously available history as planner state.

C4 is a **maximal expressivity reference**, not a practical recommendation.

If a constraint fails under C0–C3 but compiles under C4, the result is memory/state-compression failure, not semantic nonrepresentability.

## Anti-vacuity guards

A compilation is invalid if it:

1. stores the source MQR-selected action as a state variable;
2. stores a precomputed source-policy table keyed by history;
3. uses hidden future outcomes, latent true rival identity, or post-action information unavailable at decision time;
4. changes the physical action set;
5. changes the source transition law to manufacture equivalence;
6. replaces hard feasibility semantics by an arbitrarily hand-fit reward whose only purpose is to reproduce observed source actions;
7. declares a new state feature only after seeing a failed witness unless that feature belongs to a frozen generic container class;
8. hides unbounded source semantics inside an opaque identifier with no compositional update rule.

## Lossless compilation criteria

A typed constraint `x` is **LOSSLESSLY_COMPILED** under compiler class `Ck` only if all conditions hold on every reachable eligible history.

### 1. Feasible-set equivalence

`C_x(h,a) ↔ G_x(φ(h),a)`.

### 2. Behavioral equivalence

Given the same frozen ordinary objective/tie-breaking rule, source and target select the same admissible action set and policy action(s).

### 3. Transition homomorphism

For each eligible source transition `h --a--> h'`, target state updates to `φ(h')` with the same transition probability or relation.

### 4. Scientific-label preservation

Declared scientific reachability labels are preserved under the state relation.

### 5. Reachability bisimulation

For the frozen horizon/label grammar, source and target simulate each other's reachable labeled states and actions.

### 6. Release equivalence

`L_x(h)` changes exactly when compiled authority changes/release predicates change.

### 7. Own-ablation equivalence

Removing the source typed constraint and removing its compiled target predicate produce matching counterfactual feasible/reachable behavior.

### 8. Information admissibility

The compiler and compiled predicate use only contemporaneously available information.

Failure of any item blocks `LOSSLESSLY_COMPILED`.

## Compilation verdicts

### LOSSLESS_C0 / C1 / C2 / C3 / C4

First compiler class at which every required equivalence criterion holds.

### FIXED_SCHEMA_NONCLOSURE

A fixed finite feature basis fails because novel observed rival/route/provenance members require state growth, while C3 generic-container compilation succeeds.

This is **not** MQR-specific semantic irreducibility.

### MEMORY_NONCLOSURE

C0/C1 fail but bounded or full-history augmentation succeeds.

This is **not** semantic irreducibility.

### COMPUTATIONAL_BLOWUP

A lossless representation exists but incurs declared state-size or transition-complexity growth beyond the frozen budget.

This is a computational result, not an expressivity result.

### ORACLE_DEPENDENT_SOURCE

The source MQR authority itself depends on information unavailable contemporaneously.

Such a case cannot support MQR-specific action authority.

### NONREPRESENTABLE_C4

A strongest candidate verdict. Even full finite-history state plus an ordinary contemporaneous feasibility predicate cannot preserve the source's feasible-set, transition, scientific-label, release and ablation semantics.

This verdict requires a minimal prospective witness and must survive anti-vacuity audit.

## Minimal nonrepresentability witness

A valid witness must identify:

- two source histories or one branching source history;
- identical admissible compiled information under the challenged compiler class;
- a difference in source admissibility / release / labeled reachability that the target cannot reproduce;
- no hidden-future oracle;
- no difference removable by an admissible state augmentation in that class;
- a proof that adding the smallest forbidden information/state structure resolves the collision.

For `NONREPRESENTABLE_C4`, the witness must remain after full finite contemporaneous history is exposed. Vocabulary difference, implementation inconvenience, dynamic set growth, or fixed-dimensional state failure are insufficient.

## Open-frontier stress

The Court will include prospective cases where:

- new rival identities appear after new observations;
- new separator relations are created endogenously;
- a reopening route becomes scientifically meaningful only after a newly observed anomaly;
- ancestry graphs gain new dependency/common-cause edges;
- exterior evidence channels become newly available.

The frozen question is:

> Does this defeat ordinary planning itself, or only a closed fixed-dimensional state representation?

A generic set/graph state in C3 is an admissible ordinary representation. Therefore open-frontier novelty counts as semantic nonrepresentability only if it defeats the frozen generic-container representation rather than merely exceeding a preallocated slot count.

## Strong-baseline representability target

The comparison target includes ordinary:

- constrained finite-horizon planning;
- CMDP-style feasibility constraints;
- sequential Bayesian design;
- online replanning;
- safe/constrained exploration;
- POMDP/finite-memory state augmentation;
- real-option / irreversibility state variables;
- automaton/product-state encodings of history-dependent conditions;
- generic graph/set-valued scientific state.

4.65 may not claim novelty merely because a baseline paper uses different vocabulary.

## Frozen hypotheses

### H1 — CLOSED-MARKOV COMPILATION

Every 4.64 constraint whose authority is a contemporaneous predicate of a finite declared state vector should compile losslessly under C1.

### H2 — FINITE-MEMORY COMPILATION

Every constraint depending only on a bounded/regular history property should compile under C2 product-state augmentation.

### H3 — OPEN-FRONTIER FIXED-SCHEMA FAILURE

Endogenous rival/route/provenance genesis may defeat a fixed finite feature basis.

### H4 — GENERIC-CONTAINER RECOVERY

If all newly relevant scientific objects are contemporaneously observed and their authority rule is compositional over a generic set/graph state, C3 should restore lossless representability.

### H5 — C4 CEILING

No MQR-specific control semantics is earned unless a prospective source authority survives the anti-vacuity guards yet remains nonrepresentable even with full finite contemporaneous history.

These are hypotheses, not desired outcomes.

## Claim ceiling

4.65 may earn:

- a constructive compilation theorem for one or more source classes;
- a hierarchy of state-augmentation sufficiency;
- a precise distinction between fixed-schema nonclosure and semantic nonrepresentability;
- behavioral + reachability bisimulation criteria;
- minimal compilation-failure witnesses;
- a negative result that MQR acquisition authority reduces to ordinary constrained planning at the control layer;
- or, if actually demonstrated, a narrow nonrepresentability result.

4.65 may **not** earn:

- a new MQR controller merely from terminology;
- nonrepresentability from fixed-vector overflow alone;
- nonrepresentability from computational hardness alone;
- authority from an oracle-dependent source;
- an unbounded/open-world impossibility theorem from a finite stress suite;
- REALACQUIRE v0.30 without an independently earned semantic surface.

## Semantic-version gate

If all surviving acquisition authorities compile under C1–C4:

```text
MQR ACQUISITION CONTRIBUTION
= DIAGNOSTIC / CONSTITUTIONAL / GOVERNANCE LAYER

NOT

A NEW CONTROL FORMALISM
```

If a valid `NONREPRESENTABLE_C4` witness survives:

```text
ONLY THE MINIMAL
PROSPECTIVELY DEMONSTRATED
NONREPRESENTABLE SURFACE
MAY BE CONSIDERED
FOR NEW SEMANTIC PROMOTION
```

No executable-reveal scientific mutation is permitted.
