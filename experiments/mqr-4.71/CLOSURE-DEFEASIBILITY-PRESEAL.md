# MQR-4.71 — Closure-Certificate Defeasibility Constitution

Status: **PRESEALED / DUAL-SCOPE-CLOSURE / SCIENTIFIC-RELEVANCE-vs-EXECUTION-AUTHORITY**

## Motivation

MQR-4.70 typed closure certificates C0–C5 relative to an admitted intervention/measurement envelope.

MQR-4.71 reveals that at least two envelopes must be separated:

- **S-envelope** — scientifically relevant/discriminating contacts under the declared scientific scope;
- **X-envelope** — contacts currently executable/permitted under technology, ethics/legal and resource constraints.

In general:

    X_t subseteq S_t

A contact may belong to S_t but not X_t.

## Certificate scope

Every closure certificate must now declare:

- scope_kind = SCIENTIFIC_RELEVANCE or CURRENT_EXECUTION;
- contact_envelope;
- technology_state;
- permission_state;
- resource_state;
- generator_state;
- validity_horizon.

## Frozen rule

A new contact q can affect the two scopes differently.

### Case A — executable scientific separator

If q is scientifically discriminating, feasible, permitted and resource-admissible, then admitting q can defeat both scientific-relevance closure and current-execution closure.

### Case B — technologically unavailable scientific separator

If q is scientifically discriminating but currently unrealizable:
- scientific-relevance closure must carry exterior-contact debt / downgrade;
- current-execution closure may remain valid only if explicitly scoped to current technology.

### Case C — ethically/legal blocked scientific separator

If q is scientifically discriminating but execution is prohibited:
- scientific-relevance closure must not erase q;
- current-permission execution closure may remain valid;
- blocked status is not evidence that the scientific distinction is meaningless.

### Case D — resource-blocked scientific separator

If q is scientifically discriminating but outside the current budget/resource contract:
- budget-scoped execution closure may remain valid;
- scientific-relevance closure remains open unless independently certified.

### Case E — constraint unlock

If technology, permission or budget changes and q becomes executable:
- any execution closure certificate whose scope now includes q must be revalidated;
- a prior certificate may be downgraded without contradiction.

## Frozen test cases

1. RIVAL_X — available + permitted + low cost + scientific separator. Expected: SCI DOWNGRADE; EXEC DOWNGRADE.
2. INST_Z under T0 — currently unrealizable but scientific separator. Expected: SCI DOWNGRADE_DEBT; EXEC(T0) STABLE_SCOPED.
3. INST_Z under T1 — available scientific separator. Expected: SCI DOWNGRADE; EXEC(T1) DOWNGRADE.
4. ETH_H under E0 — available but ethics-blocked scientific separator. Expected: SCI DOWNGRADE_DEBT; EXEC(E0) STABLE_SCOPED.
5. ETH_H under E1 — permitted scientific separator. Expected: SCI DOWNGRADE; EXEC(E1) DOWNGRADE.
6. COST_Q under LOW budget — resource-blocked scientific separator. Expected: SCI DOWNGRADE_DEBT; EXEC(LOW) STABLE_SCOPED.
7. COST_Q under HIGH budget — executable scientific separator. Expected: SCI DOWNGRADE; EXEC(HIGH) DOWNGRADE.
8. THEORY_R — scientifically non-separating contact. Expected: no downgrade solely from entry.

## Hard boundary

    EXECUTION-COMPLETE
    !=
    SCIENTIFIC-CONTACT-COMPLETE

and:

    BLOCKED EXECUTION
    !=
    ABSENT SCIENTIFIC DEBT

## Falsifier

If this dual-scope distinction reduces to ordinary explicit constraint scoping with no additional audit/error-prevention value, no MQR novelty is earned.

## Claim ceiling

This Court may establish only a typed governance requirement: closure authority must declare which contact universe it closes.

It may not establish that every currently prohibited/infeasible contact is worth pursuing or should ever become executable.