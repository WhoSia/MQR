# Real-Language v0.5 — Authority-Transfer Boundary

Status: CONSTITUTIONAL DIRECTION / MQR-4.37

Real-Language v0.5 does not add a truth score.

It separates three objects that MQR-4.36 PCRA held too close together:

```text
WORLD-CASES / RECEIPTS
FORMAL CUSTODY
CLAIM-TRANSFER CONTRACT
```

## Required semantics

### Receipt ancestry

A world-facing premise must be able to point to the load-bearing ancestry that can alter its authority state.

Compression is allowed only when omitted ancestors cannot change the promoted claim's authority or scope.

### Statement bridge

A formal theorem name/proof receipt is insufficient.

A world-dependent claim must expose the mapping between:

```text
scientific claim
<-> formal statement
<-> typed premise set
```

The bridge itself has an authority state.

### Closure scope

Every finite closure receipt is indexed by an explicit scope identity.

```text
closure(scope_id, probe_class_id, residue_state)
```

No closure state may be inherited by a strict extension without a new receipt.

### Independence vector

Checker independence is represented componentwise:

```text
independence STATEMENT <state>
independence COMPILER  <state>
independence KERNEL    <state>
independence WORLD     <state>
```

Suggested states:

```text
INDEPENDENT
PARTIALLY_INDEPENDENT
SHARED
UNTESTED
NOT_APPLICABLE
```

No aggregate independence scalar is defined.

### Split authority

Real-Language distinguishes:

```text
FORMAL_CUSTODY = PASS / HOLD / FAIL
WORLD_AUTHORITY = PASS / HOLD / FAIL
TRANSFER = PASS / HOLD / FAIL
```

Independent rechecking may strengthen custody robustness without changing WORLD_AUTHORITY.

A world-dependent consequence may receive TRANSFER=PASS only when:
- its load-bearing receipt ancestry is reachable;
- its formal statement correspondence is explicit;
- its declared claim scope does not exceed the world-facing premises;
- its proof/custody state satisfies the inference mode actually claimed;
- open-world defeat/reopening remains represented.

## Anti-laundering rules

Reject:

```text
ZERO_INTERNAL_RESIDUE(P1) -> ZERO_INTERNAL_RESIDUE(P2) where P1 ⊂ P2
COARSE_PREMISE_PASS -> hidden HOLD ancestor deletion
DUAL_CHECKER_PASS -> WORLD_AUTHORITY_PASS
FORMAL_REGION_EXPANDED -> TRUTH_PROXIMITY_INCREASED
FORMAL_CUSTODY_PASS -> TRANSFER_PASS without statement/scope bridge
```

## Lean role

Lean remains a formal backend.

The MQR-4.37 theorems are countermodel guards showing that:
- closure at a smaller declared scope need not survive extension;
- compressed premise identity can hide a world-authority distinction;
- formal-region growth need not establish world adequacy;
- checker plurality need not establish statement/world correspondence;
- formal-custody ordering does not identify truth ordering.

These are boundary theorems, not world measurements.

## Direction

v0.5 should be implemented incrementally on top of the v0.4 proof lane.

The compiler must not force all scientific claims to use Lean.

For non-formal claims, FORMAL_CUSTODY may be NOT_APPLICABLE while world-facing scientific authority remains evaluable by the existing MQR gates.

The proof assistant is a conditional inference-custody instrument, not a universal scientific-authority primitive.
