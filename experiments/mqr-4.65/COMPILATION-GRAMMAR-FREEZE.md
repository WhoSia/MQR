# MQR-4.65 — Compilation Grammar Freeze

Status: **FROZEN / POST-LITERATURE / PRE-EXECUTABLE-REVEAL**

PRESEAL:
`bf579654ec22e91686968932417f145f717f8a84`

LITERATURE boundary:
`783d17e49d4cdf97c79ae42a38197c73f205372f`

No test family, horizon, state-capacity, event alphabet, classification rule, or expected count may change after first executable reveal.

## Purpose

The frozen suite does not attempt to prove an open-world impossibility theorem from finite cases.

It tests four distinct representability surfaces:

1. closed 4.64 typed constraints under finite-feature state;
2. genuinely history-dependent authority under finite-memory augmentation;
3. open-frontier object growth under fixed-slot versus generic set state;
4. exact full-history compilation as a formal ceiling.

## Surface A — 4.64 closed-state compilation

Reuse the exact 4.64 finite action/world grammar:

- 16 action types;
- 816 unordered action triples with replacement;
- 32 world-flag configurations;
- 26,112 worlds;
- 5 typed constraints: OPR / ARR / EAI / EXTERIOR / NEDL;
- 3 action positions per world.

Frozen predicate-comparison count:

`26,112 × 5 × 3 = 391,680`.

The source predicate is the 4.64 typed `allowed` semantics.

The C1 target compiler is allowed the complete contemporaneous finite feature tuple already present in the 4.64 world/action grammar.

Expected classification:
- if all 391,680 predicates agree: `C1_CLOSED_COMPILATION_PASS`;
- any disagreement is a compiler failure and must be investigated without changing source semantics.

This surface does **not** establish practical compactness; it tests exact representability.

## Surface B — finite-memory history compilation

Event alphabet is frozen:

- `N`: neutral/no debt-changing event;
- `D`: separator-destroying/debt-opening event;
- `R`: reopening/debt-closing event.

Enumerate every history of length 0 through 5.

History count:

`1 + 3 + 9 + 27 + 81 + 243 = 364`.

Action alphabet:

- `SAFE`;
- `DROP`;
- `REOPEN`.

Source memory state:
- initial debt-open = false;
- event `D` sets debt-open = true;
- event `R` sets debt-open = false;
- event `N` leaves it unchanged.

Source constraint:
- if debt-open = true, `DROP` is forbidden;
- otherwise all three actions are admissible.

Frozen comparisons:
`364 × 3 = 1,092`.

C1 current-event-only approximation:
- last `D` → debt-open;
- last `R` → debt-closed;
- last `N` or empty → debt-closed.

C2 product-state compiler:
- carries the one-bit automaton state `debt_open`.

Required verdict pattern:
- C1 must exhibit at least one collision;
- C2 must match all 1,092 source predicates.

Minimal C1 collision target:
- histories `[D,N]` and `[R,N]`;
- identical current event `N`;
- different source debt state;
- different admissibility of `DROP`.

## Surface C — open-frontier fixed-schema versus generic-set compilation

For frontier sizes `n = 1..8`:

- source live-rival set is any subset of `{0,...,n-1}`;
- an action is represented by the subset of live rivals for which it preserves a separator;
- source action is admissible iff it covers every currently live rival.

For each `n`, enumerate every pair:

`(live_mask, coverage_mask)`.

Frozen comparison count:

`Σ_{n=1..8} 4^n = 87,380`.

### C1-FIXED2 target

A deliberately fixed two-slot representation may inspect only rival IDs 0 and 1.

This target is not expected to be universally sufficient.

Required result:
- exact for `n ≤ 2`;
- at least one mismatch for `n ≥ 3`.

Frozen minimal witness:
- `n=3`;
- live set = `{2}`;
- action coverage = empty;
- source forbids;
- C1-FIXED2 cannot see rival 2 and therefore admits.

### C3-SET target

State stores the generic finite live-rival set and action coverage set.

Required result:
- all 87,380 source predicates match.

This demonstrates fixed-schema nonclosure without semantic nonrepresentability.

## Surface D — endogenous rival-genesis transition audit

Rival IDs:
`0,1,2,3`.

Event alphabet:
- `A0,A1,A2,A3`: rival arrival;
- `X0,X1,X2,X3`: rival removal.

Enumerate every event history of length 0 through 4.

History count:

`1 + 8 + 64 + 512 + 4096 = 4,681`.

Source state is obtained by replaying the complete history from the empty live set.

C3 target state is updated incrementally by the frozen set update rule.

Required result:
- source replay state = C3 incremental state for all 4,681 histories.

This is a transition-homomorphism check for endogenous rival genesis.

## Surface E — C4 formal ceiling

Formal theorem target:

For arbitrary history type `H`, action type `A`, source feasibility predicate
`C : H → A → Prop`, release predicate/label functions on `H`, and transition relation on histories:

- target state `S := H`;
- state compiler `φ := id`;
- target feasibility `G := C`;
- target transition := source transition.

Then feasibility, release, labels and transitions are preserved definitionally, and identity relation is a bisimulation.

The theorem is a representation theorem only.

It does not prove:
- computational tractability;
- that a compressed scientific state exists;
- that the source constraint is scientifically justified;
- that the full-history state is practical.

## Frozen classifications

### LOSSLESS_C1_CLOSED
All Surface A predicates match.

### MEMORY_NONCLOSURE_C1 / LOSSLESS_C2
Surface B has a C1 collision and exact C2 recovery.

### FIXED_SCHEMA_NONCLOSURE / LOSSLESS_C3
Surface C has fixed-slot failure and exact generic-set recovery; Surface D transition update also passes.

### C4_REPRESENTATION_THEOREM
Lean boundary proves identity-history compilation.

### NONREPRESENTABLE_C4
Available only if the formal premises of Surface E fail without triggering `ORACLE_DEPENDENT_SOURCE` or redefining the source semantics.

## Anti-inflation rules

- A finite mismatch under C1/C2 is not evidence against C3/C4.
- State-size growth is not semantic nonrepresentability.
- Computational cost is recorded separately from expressivity.
- Generic set/graph containers are ordinary state representations.
- Full-history identity compilation is a ceiling reference, not a practical planner proposal.
- No post-reveal replacement of C1-FIXED2 with a more favorable capacity.
- No post-reveal new history event added to create/remove a witness.
- No new MQR-specific constraint is admitted after reveal.
