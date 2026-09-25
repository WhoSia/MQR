# Real-Language v0.10 — Open-Frontier Attention Allocation

Status: EXECUTABLE / MQR-4.43 CLOSED / CONTRACT-RELATIVE / SET-VALUED / WORLD OPTIMUM FORBIDDEN

## Boundary

MQR-4.42 established an Open Frontier Receipt plus a Frontier Reopening Reserve. MQR-4.43 asks whether finite attention can be allocated across that open frontier without silently manufacturing a prior, utility function, loss function or probability distribution over rivals that have not yet been conceived.

v0.10 deliberately does **not** solve that problem by inventing a scalar discovery objective. It instead evaluates a declared Rival-Search Allocation Receipt (RSAR).

## Typed inputs

A packet declares finite budget/horizon, search lanes, ancestry, activation cost, mandatory/optional status, reopening/exploitation role, typed lane class, obligations and due steps, actual allocations/outcomes, nominal reserve, declared prior/utility status, path/history signature, and a witness-only latent escape lane.

The witness-only escape lane is excluded from the `allocation.*` decision surface. Paired fixtures use it only to prove that identical visible histories may hide opposite next-step escape routes.

## Activation-Capable Reopening Reserve

A positive reserve is not enough.

```text
NOMINAL RESERVE
+ reserve >= activation cost of at least one declared reopening lane
= ACTIVATION-CAPABLE REOPENING RESERVE (ACRR)
```

An ACRR remains a narrow scheduling/governance fact. It does not certify that represented lanes exhaust future rival-generating routes.

## Typed exploration debt

An obligation becomes debt when its due step is inside the declared horizon and cumulative qualifying spend on its target lane remains below the lane's activation cost. Debt is emitted as typed items such as `OQ@QUERY` and `OR@REPRESENTATION`.

```text
allocation.debt_scalar_default=OFF
allocation.opportunity_cost_mode=VECTOR
```

Equal debt counts do not imply equal debt geometry.

## Set-valued guidance

The checker can report whether one declared schedule lies inside a narrow admissibility envelope:

```text
BUDGET VALID
AND NO DUE MANDATORY DEBT
AND ACRR LIVE
```

This is feasibility/admissibility only:

```text
ADMISSIBLE != OPTIMAL
```

## Twin-world boundary

Two packets can share the same visible history, lanes/ancestries, budget, horizon, reserve and declared normative inputs while their witness-only next escape route differs. Canonical Rust and independent Prolog must emit identical `allocation.*` output for both.

```text
VISIBLE RSAR EQUIVALENCE
DOES NOT IDENTIFY
UNIVERSALLY CORRECT NEXT SEARCH ACTION
```

## Hard guards

```text
allocation.hidden_prior_inferred=NO
allocation.hidden_utility_inferred=NO
allocation.expected_discovery_value_inferred=NO
allocation.unique_optimum_authorized=NO
allocation.universal_next_action=UNIDENTIFIED
allocation.debt_scalar_default=OFF
allocation.opportunity_cost_mode=VECTOR
allocation.guidance_mode=SET_VALUED_CONTRACT_RELATIVE
allocation.randomization_epistemic_oracle=NO
allocation.world_optimum_identified=NO
allocation.world_frontier_complete=NO
allocation.stopping_rule=FORBIDDEN
```

If both a prior and utility are explicitly declared, v0.10 may acknowledge `allocation.local_optimizer_scope=DECLARED_MODEL_ONLY`; it still does not convert that local model optimum into a universal scientific optimum.

## Implementation

- canonical evaluator: Rust `src/allocation_v10.rs` / `real-v10-allocate`;
- independent relational evaluator: Prolog `prolog/allocation_v10.pl`;
- formal boundary: Lean `lean/MQR/Allocation.lean`.

Rust–Prolog concordance is implementation-diversity evidence only. Lean certifies finite structural countermodels and scheduling facts, not the world truth of future rival distributions.

## Final scope sharpening

The closure court narrows several preseal phrases deliberately.

- **AAE is implemented as a membership/admissibility checker, not an optimizer or exhaustive schedule enumerator.**
- **ACRR certifies activation capability only.** Generator-ancestry common mode remains a separate coordinate; ACRR does not imply independent search ancestry.
- The formal anti-starvation result is a **finite, unit-activation, one-cycle scheduling theorem**. It establishes that every declared lane can receive a qualifying slot under sufficient one-cycle budget; it is not a heterogeneous-cost optimal scheduling theorem.
- Periodic reserve exercise is not inferred from reserve existence. It must be constituted as an explicit obligation/due horizon, otherwise no debt may be manufactured after the fact.
- Explicit prior + explicit utility may authorize `DECLARED_MODEL_ONLY` optimization. That local authorization never implies a universal next action, world-optimal scientific search, frontier completeness or a stopping rule.
- The Rust–Prolog agreement is a declared-surface implementation concordance result, not evidence of independent world-contact ancestry.

## Meaning

```text
DECLARE WHAT YOU ARE OBLIGED TO KEEP SEARCHABLE,
PAY THE ACTIVATION COST OR CARRY THE DEBT,
PRESERVE AN EXERCISABLE REOPENING ROUTE,
REOPEN THE PLAN ON ESCAPE,
AND DO NOT CALL THE RESULT WORLD-OPTIMAL.
```
