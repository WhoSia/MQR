# MQR-4.64 — Acquisition-Constraint Binding Characterization Study

Status: **PRESEALED / MAIN-ONLY / PRE-LITERATURE-CONTACT**

## Formal name

**MQR-4.64 — Acquisition-Constraint Binding Characterization Study, Diagnostic→Controller Promotion Boundary, Scarce-Separator Reachability, Reopening-Constraint Activation, Irreversible Option-Loss Geometry, Strong-Baseline Absorption Equivalence, Minimal Binding Witnesses, Constraint Redundancy and Release, Cross-Policy Behavioral Equivalence & Whether a Typed Scientific-Acquisition Diagnostic Earns Action Authority Only When It Defines Nonredundant Feasible-Set Structure beyond Constrained Bayesian Design, Sequential Planning and Real-Option Value**

## Canonical parent

MQR-4.63 canonical head:
`1dc3fcd183631c48d9cabc03b573bfbb8eb1cb9f`

Inherited scientific result:
- diagnostic separability != policy incrementality;
- OPR / ARR / EAI / exterior control collapsed to strong baselines in 4.63;
- NEDL survived locally in SCOUT-PARK only;
- no REALACQUIRE v0.30 promotion.

## Explanandum lock

MQR-4.64 does **not** ask which MQR controller wins.

It asks:

> Under what exact structural conditions does a typed acquisition diagnostic become a **binding action constraint** rather than a descriptive coordinate, redundant constraint, or behavior already induced by a strong baseline?

The target transition is:

```text
DIAGNOSTIC COORDINATE
→ CONSTRAINT CANDIDATE
→ FEASIBLE-SET CHANGE?
→ REACHABILITY CHANGE?
→ BASELINE ALREADY SATISFIES?
→ INDEPENDENT ACTION AUTHORITY?
```

## Primitive objects

For a world state `s`:
- `A(s)`: physically/logically available acquisition actions.
- `F_B(s)`: feasible actions under baseline constraints.
- `C_x(s)`: feasible actions after imposing typed constraint `x`.
- `R_H(s, a)`: future scientific-reachability set over horizon `H` after action `a`.
- `D_x(s)`: diagnostic value for typed coordinate `x`.
- `Sep(s)`: currently reachable rival-separating actions.
- `Reopen(s)`: reachable routes that can reopen a locally closed claim/frontier.
- `Irrev(s,a)`: irreversible destruction induced by `a`.
- `Anc(s,a)`: acquisition/evidence ancestry state.
- `Debt(s,a)`: future unresolved-distinction debt induced by `a`.

Typed candidate constraints:
- OPR-like separator preservation;
- ARR-like reopening floor;
- ancestry-diversity/common-mode ceiling;
- NEDL-like future-separator debt ceiling;
- bounded exterior-access floor.

## Frozen classifications

### DIAGNOSTIC_ONLY
A coordinate varies and may distinguish histories, but imposing it does not change the feasible action set under the tested state/baseline:
`F_B(s) = F_B(s) ∩ C_x(s)`.

### REDUNDANT_CONSTRAINT
The typed constraint removes actions in principle, but every action selected by the strong baseline already satisfies it over the tested support. Removing the constraint leaves policy behavior/reachability unchanged.

### BASELINE_ABSORBED
A baseline mechanism not phrased in MQR terms induces behaviorally equivalent feasible/reachability consequences:
`R_H^{baseline}(s) ≈ R_H^{typed}(s)`
under frozen equivalence criteria.

### BINDING_LOCAL
The typed constraint changes feasible actions and future reachability in at least one eligible regime, its own removal changes behavior/outcome, and the strong baseline does not already induce the same restriction.

### BINDING_STRUCTURAL
A stronger target. Requires the same minimal binding condition to recur across at least two structurally distinct world families and survive baseline substitution.

### OVERCONSTRAINING
The typed constraint binds but destroys scientifically material reachable states/actions without compensating preservation/reopening benefit under the declared contract.

### ORACLE_DEPENDENT
The constraint can bind only using information unavailable to the acting policy at that state. Such authority is rejected.

## Binding test

A typed constraint `x` is action-authoritative only if all required conditions hold:

1. **Activation**: some baseline-feasible action violates `x`.
2. **Feasible-set effect**: imposing `x` removes at least one baseline-feasible action.
3. **Reachability effect**: at least one removed/admitted action changes a declared future scientific reachability set.
4. **Materiality**: the reachability difference affects a live rival, separator, reopening route, independence class or declared scientific use.
5. **Non-absorption**: a strong matched baseline does not already induce an equivalent restriction/reachability outcome.
6. **Information admissibility**: activation is computable from the policy's contemporaneous information.
7. **Counterfactual own-ablation**: removing only `x` changes behavior or reachable scientific states.
8. **Scope locality**: authority is indexed to the declared world, horizon and scientific contract.

If 1–4 fail: DIAGNOSTIC_ONLY or REDUNDANT.
If 5 fails: BASELINE_ABSORBED.
If 6 fails: ORACLE_DEPENDENT.
If binding causes net loss outside the declared contract: OVERCONSTRAINING.

## Minimal binding witness

A minimal witness must identify:
- one state `s`;
- baseline policy `π_B`;
- typed constraint `x`;
- one action `a_v` violating `x`;
- one admissible alternative `a_p`;
- a future scientific capability/reachability element `r`;
such that:
- `a_v = π_B(s)` without `x`;
- `a_v` is excluded with `x`;
- `r ∉ R_H(s,a_v)`;
- `r ∈ R_H(s,a_p)`;
- baseline `π_B` does not independently exclude `a_v`;
- the witness uses no hidden future-state oracle.

Minimality is evaluated by removing witness components/conditions and checking whether binding still holds.

## Strong-baseline families to confront

Without assuming any is universal:
- constrained Bayesian experimental design;
- sequential/Bayes-adaptive experimental planning;
- POMDP active sensing;
- robust/misspecification-aware design;
- safe/constrained exploration;
- dual control;
- real-options / value-of-information under irreversibility;
- causal intervention design;
- diversity/representativeness constraints.

## Claim ceiling

4.64 may earn:
- a binding-condition taxonomy;
- minimal/nonminimal witness separation;
- equivalence/collapse results against existing baseline families;
- a formal promotion boundary from diagnostic receipt to action constraint;
- retirement/release rules for nonbinding constraints.

It may not earn:
- universal MQR controller superiority;
- a universal scientific feasible set;
- novelty for constrained planning, option value, safe exploration or sequential design;
- action authority from diagnostic magnitude alone.

No executable-reveal scientific mutation is permitted.
