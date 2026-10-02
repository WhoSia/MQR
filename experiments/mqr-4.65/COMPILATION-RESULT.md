# MQR-4.65 — Scientific-Reachability Constraint Compilation Result

Status: **QUALIFIED / CONTROL-EXPRESSIVITY-REDUCTION-EARNED / SCIENTIFIC-STATE-CONSTITUTION-SURVIVES / NO-v0.30-PROMOTION / FINAL-SEAL-PENDING**

## Frozen ancestry

- MQR-4.64 canonical parent: `74ea204d90567e5f873b5aac688eb6ae98672cb0`
- PRESEAL: `bf579654ec22e91686968932417f145f717f8a84`
- LITERATURE boundary: `783d17e49d4cdf97c79ae42a38197c73f205372f`
- COMPILATION-GRAMMAR-FREEZE: `2d1bfe4ef072603c91ac2898c83d65553d9ab991`
- canonical Rust implementation: `e339593d421960d9cf36ede1d4dd1198f7bed62b`
- independent Python implementation: `d9df149c7d0e7f840a1394ff82dd151bdf4f7925`
- Lean C4 boundary: `6ab9e5e300ac687e1ab023e436bf6da9024cc0e7`
- first executable reveal: `2ff4de69859528f1bfa3658b3ec6d5defb75aa5d`
- first reveal run: `36973240051`

No compiler class, test family, horizon, fixed-slot capacity, event alphabet, classification rule, anti-vacuity guard, scientific threshold, or claim ceiling changed after first executable reveal.

## First-reveal qualification

Run `36973240051`: **SUCCESS**.

Five frozen jobs:
1. MQR-4.65/Canonical-Rust — SUCCESS
2. MQR-4.65/Independent-Concordance — SUCCESS
3. MQR-4.65/Deterministic-Replay — SUCCESS
4. MQR-4.65/C4-Lean-Boundary — SUCCESS
5. MQR-4.65/Structural-Guards — SUCCESS

Rust and independently spelled Python implementations agree on the complete frozen summary.

The Lean C4 boundary contains no `sorryAx` dependency for the declared representation theorems.

## Result A — closed 4.64 constraints compile under C1

Frozen surface:
- 26,112 worlds
- 5 typed constraints
- 3 actions/world
- **391,680 source-vs-target feasibility comparisons**

Result:
- predicate mismatches: **0**

Policy-level check:
- 26,112 worlds
- 5 constraints
- 4 frozen baseline objectives
- **522,240 policy comparisons**

Result:
- policy mismatches: **0**

Verdict:

```text
OPR / ARR / EAI / EXTERIOR / NEDL
ON THE CLOSED 4.64 GRAMMAR

= LOSSLESS_C1_CLOSED
```

Once the planner is given the finite contemporaneous feature tuple already used by the source constraint, no extra MQR control language is needed to reproduce the constraint or the frozen policy behavior.

This does **not** show that the feature tuple is scientifically obvious, naturally given, or cheap to construct.

## Result B — history dependence creates memory nonclosure, not semantic nonrepresentability

Frozen histories:
- alphabet `{N,D,R}`
- lengths 0..5
- **364 histories**
- 3 actions/history
- **1,092 feasibility comparisons**

A current-event-only C1 representation has:
- **58 state collisions** relative to the source debt state.

The frozen minimal collision is:
- `[D,N]`
- `[R,N]`

Both end in the same current event `N`, but the first retains open debt and the second does not. Therefore `DROP` has different source admissibility.

A one-bit C2 product state `debt_open` recovers the source exactly:
- C2 mismatches: **0**

Verdict:

```text
CURRENT OBSERVATION
CAN BE INSUFFICIENT

BUT

FINITE-MEMORY PRODUCT STATE
CAN RESTORE EXACT CONTROL SEMANTICS
```

Classification:
**MEMORY_NONCLOSURE_C1 / LOSSLESS_C2**.

## Result C — open rival growth defeats a fixed slot basis, not a generic set state

Frozen frontier surface:
- live-rival sets of sizes `n=1..8`
- all live masks × all action-coverage masks
- **87,380 comparisons**

C1-FIXED2 target:
- can inspect only rival IDs 0 and 1
- mismatches: **39,312**

Frozen minimal witness:
- `n=3`
- live rival set `{2}`
- action coverage `∅`
- source forbids
- C1-FIXED2 admits because rival 2 is outside its fixed slots.

C3 generic finite-set state:
- mismatches: **0**

Verdict:

```text
OPEN-FRONTIER OBJECT GENESIS
CAN BREAK A CLOSED FIXED-DIMENSIONAL SCHEMA

WITHOUT BREAKING

ORDINARY GENERIC SET-VALUED
SEQUENTIAL STATE REPRESENTATION
```

Classification:
**FIXED_SCHEMA_NONCLOSURE / LOSSLESS_C3**.

## Result D — endogenous rival genesis preserves C3 transition semantics

Frozen rival event histories:
- rival IDs 0..3
- arrival/removal alphabet size 8
- lengths 0..4
- **4,681 histories**

Source full replay and C3 incremental set update agree on every history:
- transition-state mismatches: **0**

Thus dynamic rival admission/removal does not, by itself, defeat ordinary state-transition semantics when the state representation admits a generic set and the update rule is compositional.

This is a finite constructive result. It is not a proof that all possible scientific rival genesis admits such a representation.

## Result E — C4 full-history representation theorem

The Lean boundary formalizes a source acquisition semantics over:
- history type `H`;
- action type `A`;
- feasibility predicate `H → A → Prop`;
- release/liveness function on `H`;
- scientific-label function on `H`;
- transition relation on histories.

The target is:
- state type `S := H`;
- compiler `φ := id`;
- target feasibility predicate := source feasibility predicate;
- target release/labels := source release/labels;
- target transition := source transition.

The following are preserved definitionally:
- feasibility;
- release state;
- scientific labels;
- transitions.

Identity on histories is a two-way transition simulation.

Therefore:

```text
IF MQR ACTION AUTHORITY
IS A CONTEMPORANEOUSLY DECIDABLE
PREDICATE OF FINITE AVAILABLE HISTORY,

THEN FULL-HISTORY STATE AUGMENTATION
GIVES AN ORDINARY LOSSLESS
CONSTRAINED-PLANNING REPRESENTATION.
```

This is a **representation theorem**, not a computational theorem.

It does not establish:
- finite-state compactness;
- tractability;
- learnability;
- observability of hidden world state;
- correctness of the scientific constitution;
- practical adequacy of storing full history.

## The central distinction earned by 4.65

The Court separates three questions that had previously been too easy to conflate:

```text
1. IS THE CURRENT STATE REPRESENTATION SUFFICIENT?
2. CAN A RICHER ORDINARY STATE REPRESENT THE AUTHORITY?
3. HOW IS THE SCIENTIFICALLY RIGHT STATE / CONSTRAINT CONSTITUTED?
```

4.65 finds:

```text
STATE-SUFFICIENCY FAILURE
!=
CONTROL-LANGUAGE FAILURE

FIXED-SCHEMA NONCLOSURE
!=
SEQUENTIAL-PLANNING NONREPRESENTABILITY

SCIENTIFIC SEMANTIC DISTINCTIVENESS
!=
CONTROL-EXPRESSIVITY DISTINCTIVENESS
```

## What is reduced

Under the declared 4.65 source semantics, the **control-expression layer** reduces to ordinary constrained sequential planning once sufficient contemporaneous state is exposed.

In particular:
- 4.64 closed constraints compile under C1;
- bounded history dependence compiles under C2 in the frozen witness;
- finite open-frontier object growth compiles under C3 in the frozen witness;
- arbitrary contemporaneous finite-history predicates compile under C4 by construction.

Thus 4.65 does **not** earn an MQR-specific sequential-control expressivity class.

## What survives

The reduction does not trivialize MQR.

The unresolved/nonreduced problem moves to **scientific state constitution**:

- Which rivals count as live?
- Which separators are genuinely non-substitutable?
- Which ancestry relations count as independent?
- Which reopening routes remain scientifically material?
- Which objects/relations should enter the state at all?
- Which compression preserves the authority-relevant distinctions?
- When should a state schema reopen rather than absorb a newly discovered distinction?
- Which state variables are contemporaneously observable versus retrospectively invented?
- Which constraint receives action authority, and when should it release?

Ordinary planning can optimize or enforce over a supplied state/constraint representation. It does not by itself determine that scientific ontology/authority constitution.

Therefore the strongest surviving MQR acquisition thesis after 4.65 is:

```text
MQR'S DISTINCTIVE ACQUISITION ROLE,
IF ANY,

IS NOT A NEW CONTROL LANGUAGE.

IT IS THE CONSTITUTION,
AUDIT, REOPENING AND REVISION
OF THE SCIENTIFIC STATE
AND CONSTRAINT SURFACE
ON WHICH ORDINARY PLANNING OPERATES.
```

## Open-frontier consequence

MQR-4.42's open-frontier result is not overturned.

4.42 denied that current-rival separation or generator saturation establishes world-frontier completeness.

4.65 adds a different result:

> Once a newly admitted rival is contemporaneously represented as an object in the planner state, ordinary generic-container planning can act on it.

These are compatible.

```text
THE PLANNER CAN REPRESENT
A RIVAL AFTER ADMISSION

!=

THE PLANNER CAN GUARANTEE
THAT ALL WORTHWHILE RIVALS
HAVE BEEN GENERATED OR ADMITTED
```

Thus **frontier discovery/constitution** remains prior to planner optimization.

## Minimal nonrepresentability verdict

No `NONREPRESENTABLE_C4` witness is earned.

More strongly, under the PRESEAL's source contract—action authority as a contemporaneously available finite-history predicate—the C4 identity construction blocks such a witness by construction.

To escape that theorem, a future source semantics would need some additional structure not reducible to a predicate over available finite history. Candidate escapes must not smuggle in:
- hidden future truth;
- inaccessible latent state;
- oracle identity;
- policy outputs as state.

If the escape requires such information, it is `ORACLE_DEPENDENT_SOURCE`, not scientific action authority.

## Relation to prior literature

The negative control-expressivity result is consistent with strong prior art:
- history-dependent objectives can be Markovized by richer states;
- POMDPs use information-state representations;
- sequential Bayesian experimental design is formulated via dynamic programming/POMDPs;
- dynamic constraints can be handled by online constrained planning;
- relational/object representations weaken fixed-slot state limitations.

The 4.65 contribution is therefore not a claim to invent state augmentation. It is the explicit **scientific-authority compilation court** separating:
- diagnostic semantics;
- state sufficiency;
- control representability;
- schema reopening;
- and nonrepresentability burden.

## Semantic-version decision

**NO REALACQUIRE v0.30 PROMOTION.**

Reason:

```text
BINDING BOUNDARY = EARNED IN 4.64
STATE-COMPILATION BOUNDARY = EARNED IN 4.65

BUT

MQR-SPECIFIC CONTROL EXPRESSIVITY
= NOT EARNED
```

REALACQUIRE 0.29 remains current.

No new Real-Language acquisition syntax is justified by 4.65.

## Publication consequence

The old Paper-II possibility should not be framed as a novel MQR acquisition controller.

A stronger and more defensible future paper shape is:

**Scientific State Constitution before Sequential Experimental Design: Diagnostic Authority, State Sufficiency, Open-Frontier Reopening and Compilation into Constrained Planning**

Its central claim would be constitutional rather than control-theoretic:
ordinary planners can act over a supplied scientific state, but constructing, auditing and reopening that state under open rival generation is a separate methodological problem.

Publication readiness remains HOLD pending naturalistic/real scientific cases and a stronger comparison with state abstraction, belief-state construction, relational planning and scientific-discovery literatures.

## Successor debt

4.65 closes the direct controller-novelty route.

The next high-value question is no longer:
> Can MQR invent a controller that ordinary planning cannot express?

It is:
> Under what conditions can an authority-relevant scientific history be **compressed** into a smaller state representation without losing future scientific distinctions, reopening triggers, ancestry information or constraint-release semantics?

That successor should test minimal scientific state, quotient sufficiency and lossy/faithful compression—not revive controller novelty by renaming state variables.
