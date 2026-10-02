# MQR-4.43 — Rival-Search Allocation Court

Status: **CLOSED / B+C+D+E+F+G / A REJECTED-AS-FREE-UNIVERSAL-OPTIMUM / H REJECTED / DECLARED-MODEL LOCAL OPTIMIZATION ONLY / AAE+ACRR+TYPED-EDL / OPEN-FRONTIER / MAIN-ONLY**

## Formal stage name

**MQR-4.43 — Rival-Search Allocation Court, Generator-Portfolio Selection, Exploration Debt, Search Opportunity Cost, Adaptive Discovery Policy, Reopening-Reserve Goodharting & Whether Finite Scientific Attention Can Be Allocated across an Open Rival Frontier without Smuggling a Utility Function over the Unknown**

MQR lineage remains flat. All attack, repair, implementation and closure work belongs to MQR-4.43.

## Verdict

MQR-4.43 rejects the idea that an open rival frontier plus a finite budget uniquely determines a scientifically optimal search policy.

The positive result is narrower:

```text
RIVAL-SEARCH ALLOCATION RECEIPT (RSAR)
+ ALLOCATION ADMISSIBILITY ENVELOPE (AAE)
+ ACTIVATION-CAPABLE REOPENING RESERVE (ACRR)
+ TYPED EXPLORATION-DEBT LEDGER (EDL)
+ ESCAPE-TRIGGERED REALLOCATION
------------------------------------------------
CONTRACT-RELATIVE, SET-VALUED ALLOCATION GUIDANCE
```

This does **not** imply:

```text
UNIVERSALLY BEST NEXT SEARCH ACTION
WORLD-OPTIMAL SCIENTIFIC POLICY
COMPLETE PRIOR OVER UNCONCEIVED RIVALS
SCIENTIFIC STOPPING RULE
WORLD FRONTIER COMPLETENESS
```

The core distinction is:

> Open-frontier science can govern finite attention without pricing every unknown rival, but it cannot call that governance a universal optimum unless the missing probabilistic/normative structure is explicitly constituted.

## Frozen branches

- **A UNIVERSAL-OPTIMAL — REJECTED AS A FREE INFERENCE.** No unique world-optimal search policy is identified from the open-frontier receipt alone.
- **B NONIDENTIFIABLE — PASS.** Identical visible RSAR histories can hide opposite next-step escape routes.
- **C CONTRACT-RELATIVE — PASS.** Budget, activation cost, obligations, due horizons and declared normative inputs legitimately constrain allocation.
- **D SET-VALUED — PASS.** Multiple schedules may remain admissible without a total order.
- **E ACTIVATION-CAPABLE — PASS.** Nominal reserve is distinguished from reserve sufficient to activate a declared reopening lane.
- **F DEBT-TYPED — PASS.** Exploration debt remains indexed to obligation and search class; default scalarization is OFF.
- **G ADAPTIVE-BUT-NONORACULAR — PASS.** Explicit update semantics and escape-triggered reopening are allowed; adaptive search is not treated as an epistemic oracle.
- **H ALLOCATION-FATAL — REJECTED.** Open-world uncertainty does not make all finite guidance illegitimate; narrow procedural guidance survives.

## Exact non-identifiability result

Two executable twin worlds expose the same visible allocation surface but reverse the witness-only next escape lane.

Lean proves the stronger functional boundary:

```text
for every deterministic policy
  policy : VisibleHistorySignature -> SearchLane

the same visible signature cannot select an action
that captures both opposite twin-world escapes.
```

The generalized theorem is axiom-free.

This is deliberately not advertised as a new No-Free-Lunch theorem. It is a narrow executable impossibility result at the frozen RSAR observation surface.

Randomization may support bounded procedural access, but no calibrated discovery probability or utility over unconceived rivals is inferred from randomization alone.

## Positive scheduling result

The preseal anti-starvation claim was narrowed during audit.

Lean proves an axiom-free finite scheduling theorem for the **unit-activation, one-cycle** case: with one budget unit per declared lane, every lane can receive a qualifying slot inside the cycle.

That proves a scheduling fact, not:
- heterogeneous-cost optimality;
- calibrated discovery probability;
- equal epistemic importance;
- frontier completeness.

The executable v0.10 surface handles declared activation costs and debt thresholds, but MQR-4.43 does not claim a general optimal scheduler for heterogeneous search costs.

## Reopening reserve: final decomposition

The preseal candidate risked merging two distinct properties.

Final closure separates:

```text
ACRR = can the reserved resource activate at least one declared reopening lane?
COMMON-MODE / ANCESTRY GEOMETRY = are the funded search routes independent enough to diversify failure ancestry?
```

Therefore:

```text
ACRR_LIVE != ANCESTRY_INDEPENDENCE
```

A nominal reserve can be Goodharted by spreading resources below activation thresholds. A live ACRR prevents that specific failure only. Common-mode concentration remains separately exposed and cannot be laundered into ACRR.

Periodic reserve exercise is also not inferred from reserve existence. If exercise within a horizon is mandatory, it must be encoded as an obligation; missed activation then remains typed debt.

## Exploration debt and opportunity cost

Two states may have the same debt count while owing different scientific search obligations.

Executable fixtures instantiate:

```text
1 debt in QUERY
!=
1 debt in REPRESENTATION
```

Hence:

```text
allocation.debt_scalar_default=OFF
allocation.opportunity_cost_mode=VECTOR
```

Weighted prioritization is allowed only when the weights are declared outside the checker.

## Greedy and common-mode attacks

The court executes:
- greedy recent-yield starvation of a mandatory reopening lane;
- nominal multi-generator funding with shared ancestry and an unfunded independent route;
- reserve amount equality with different activation capability;
- escape-triggered allocation reopening.

Therefore the following shortcuts are rejected:

```text
RECENT RIVAL YIELD -> FUTURE DISCOVERY PROBABILITY
RIVALS PER COST -> DISCOVERY VALUE
LOCAL FCR GAIN -> PERMISSION TO STARVE FRONTIER SEARCH
GENERATOR COUNT -> ANCESTRY DIVERSITY
RESERVE > 0 -> REOPENING COMPETENCE
SCALAR DEBT COUNT -> DEBT GEOMETRY
ADMISSIBLE -> OPTIMAL
ANTI-STARVATION -> FRONTIER COMPLETE
RANDOMIZATION -> EPISTEMIC ORACLE
MORE BUDGET -> WORLD CLOSURE
RECENT SILENCE -> RETIREMENT AUTHORITY
```

## Declared-model optimization boundary

A positive fixture declares both a prior and a utility.

The evaluator then allows:

```text
allocation.local_optimizer_scope=DECLARED_MODEL_ONLY
```

while retaining:

```text
allocation.unique_optimum_authorized=NO
allocation.world_optimum_identified=NO
allocation.world_frontier_complete=NO
allocation.stopping_rule=FORBIDDEN
```

MQR therefore does not oppose optimization. It refuses only the laundering of a model-relative optimum into an open-world scientific optimum.

## Real-Language v0.10

Canonical surface:

- Rust: `src/allocation_v10.rs` / `real-v10-allocate`;
- independent relational evaluator: `prolog/allocation_v10.pl`;
- Lean boundary: `lean/MQR/Allocation.lean`;
- constitution: `V10-ALLOCATION.md`.

The Rust and Prolog grammars now both require the v0.10 packet boundary, including the `REALALLOCATE 0.10` header and `END`. Negative fixtures cover missing header, missing END, invalid lane role and unknown lane references.

The AAE implementation is a **membership predicate** over a declared schedule. It does not enumerate or rank every possible schedule.

## Formal boundary

The final Lean allocation file proves, with empty axiom ancestry:
- opposite twin-world escape actions under equal visible history;
- no single action that captures both twin-world escapes;
- no deterministic visible-signature policy that captures both;
- nominal reserve does not imply activation capability;
- an activation threshold can certify narrow reserve competence;
- equal scalar debt count does not identify debt geometry;
- finite declared anti-starvation witnesses;
- finite one-cycle unit-activation round-robin coverage;
- procedural coverage does not imply frontier completeness;
- local exploitation gain does not license exploration retirement;
- set-valued admissibility does not identify a unique world optimum;
- frontier escape can mandate allocation reopening;
- randomized coverage is not an epistemic oracle.

Formal custody remains a theorem about the declared model. It does not create world-contact authority.

## Literature pressure

The independent structure was presealed before the literature pass.

Post-preseal literature was used only as novelty-kill, countermodel pressure and machinery donation.

- Weitzman-style optimal search shows how optimization becomes well-defined once search costs and payoff distributions are constituted.
- Bayesian experimental design makes prior/utility dependence explicit.
- multi-armed bandit theory supplies exploration/exploitation machinery and finite-time guarantees inside a constituted arm/reward problem.
- No-Free-Lunch results block any casual novelty claim for unrestricted universal optimization.
- epistemic-landscape and novelty-search work supply prior art for cognitive-labor diversity, path dependence and objective escape.

MQR-4.43 therefore claims no invention of optimal search, bandit exploration, Goodhart effects, unconceived alternatives or scientific division of labor.

Its live contribution is constitutional: an executable separation between **declared-model optimization** and **open-frontier allocation governance**.

## Final canonical objects

```text
RSAR  Rival-Search Allocation Receipt
AAE   Allocation Admissibility Envelope
ACRR  Activation-Capable Reopening Reserve
EDL   Exploration Debt Ledger
RAB   Research-Attention Budget
SOCV  Search Opportunity-Cost Vector
```

The 4.42 OFR/FRR remain upstream. For allocation governance, ACRR is the activation-capability refinement of the reserve surface, not a frontier-completeness certificate.

## Stop-rule audit

- twin-world allocation non-identifiability executable: PASS
- deterministic universal next-action inference rejected: PASS
- nominal versus activation-capable reserve executable: PASS
- greedy-yield starvation executable: PASS
- common-mode portfolio inflation executable: PASS
- equal scalar debt / different debt geometry executable: PASS
- positive anti-starvation scheduling theorem: PASS, narrow unit-activation scope
- escape-triggered reallocation executable: PASS
- declared-model local optimizer ceiling executable: PASS
- literature contacted after preseal: PASS
- v0.10 default debt scalarization disabled: PASS
- v0.10 world-optimum and frontier-completeness inference disabled: PASS
- Rust–Prolog grammar boundary aligned and negative-tested: PASS
- Lean allocation theorem axiom ancestry empty: PASS
- main-only branch policy: PASS

## Seal condition

This court is canonical only when the same repository head containing this file passes:
- MQR-4.43 Rival-Search Allocation Court;
- MQR-4.43 Allocation Lean Boundary;
- Real-Language CI;
- Real-Language v0.4–v0.10 Lean Proof Boundary, including independent nanoda replay of the strengthened 4.43 theorems.

The exact final SHA and workflow-run identifiers belong in the external Research OS / Notion closure receipt so documenting the receipts does not mutate the sealed Git head.

## Closure thesis

```text
OPEN FRONTIER + FINITE ATTENTION
DOES NOT IDENTIFY A UNIVERSAL OPTIMUM.

BUT

EXPLICIT OBLIGATIONS
+ ACTIVATION-CAPABLE REOPENING
+ TYPED DEBT
+ NON-STARVATION SCHEDULING
+ ESCAPE-TRIGGERED REALLOCATION
------------------------------------------------
CAN DEFINE AUDITABLE CONTRACT-RELATIVE GUIDANCE

WITHOUT
PRICING EVERY UNCONCEIVED RIVAL.
```
