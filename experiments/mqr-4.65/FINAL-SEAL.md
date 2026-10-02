# MQR-4.65 — FINAL SEAL

Status: **FINAL-SEAL / EXACT-HEAD-VERIFICATION-REQUIRED**

## Canonical parent

MQR-4.64 FINAL-SAME-HEAD-VERIFIED:
`74ea204d90567e5f873b5aac688eb6ae98672cb0`

## Frozen ancestry

- PRESEAL: `bf579654ec22e91686968932417f145f717f8a84`
- LITERATURE boundary: `783d17e49d4cdf97c79ae42a38197c73f205372f`
- COMPILATION-GRAMMAR-FREEZE: `2d1bfe4ef072603c91ac2898c83d65553d9ab991`
- canonical Rust implementation: `e339593d421960d9cf36ede1d4dd1198f7bed62b`
- independent Python implementation: `d9df149c7d0e7f840a1394ff82dd151bdf4f7925`
- Lean C4 boundary: `6ab9e5e300ac687e1ab023e436bf6da9024cc0e7`
- first executable reveal: `2ff4de69859528f1bfa3658b3ec6d5defb75aa5d`
- first reveal run: `36973240051` — 5/5 SUCCESS
- scientific result: `bf77184f10176767f3641b512a892aac5121ecc7`
- doctrine 422–430: `a333930241d6cd2b329a627975f6fbea592c06c7`
- README boundary: `afb6922f8b95c066228f73d2bdce3735cd9a975c`
- paper-prospect reframe: `af14e166e038f6ee6cc2f1a0fa191311f99323ee`

No compiler class, test family, horizon, fixed-slot capacity, event alphabet, classification rule, anti-vacuity guard, scientific threshold or claim ceiling changed after first executable reveal.

## Sealed result

### C1 closed-state compilation

Frozen 4.64 typed-constraint surface:
- 391,680 feasibility comparisons
- **0 source/target mismatches**

Frozen policy comparison:
- 522,240 policy comparisons
- **0 source/target mismatches**

Verdict:
**LOSSLESS_C1_CLOSED**.

### C2 finite-memory compilation

Frozen history surface:
- 364 histories
- 1,092 action predicates
- current-event-only C1: **58 state collisions**
- one-bit C2 product state: **0 mismatches**

Verdict:
**MEMORY_NONCLOSURE_C1 / LOSSLESS_C2**.

### C3 generic-set open-frontier compilation

Frozen frontier surface:
- 87,380 comparisons
- fixed-two-rival C1 schema: **39,312 mismatches**
- generic finite-set C3 state: **0 mismatches**

Frozen endogenous rival-genesis surface:
- 4,681 histories
- source replay vs incremental C3 update: **0 mismatches**

Verdict:
**FIXED_SCHEMA_NONCLOSURE / LOSSLESS_C3**.

### C4 full-history representation ceiling

Lean certifies, without `sorryAx`, that for an acquisition semantics whose:
- feasibility;
- release/liveness;
- scientific labels;
- transitions

are defined over contemporaneously available finite history, taking the full history itself as target state and using the identity compiler preserves these structures definitionally. Identity is a transition bisimulation.

Verdict:
**C4_REPRESENTATION_THEOREM**.

No `NONREPRESENTABLE_C4` witness is earned under the declared source contract.

## Scientific synthesis

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

MQR-4.65 therefore earns a **control-expressivity reduction**:

> Once sufficient contemporaneous scientific state is supplied, the tested MQR acquisition authorities are representable within ordinary constrained sequential planning.

The surviving MQR problem is not a new control language. It is the **constitution, audit, compression, reopening and revision of the scientific state/constraint surface** supplied to ordinary planning.

## Compatibility with the open-frontier doctrine

MQR-4.42 remains intact.

```text
A PLANNER CAN REPRESENT
A RIVAL AFTER ADMISSION

!=

ALL SCIENTIFICALLY RELEVANT
RIVALS HAVE BEEN GENERATED
OR ADMITTED
```

4.65 reduces planner expressivity claims; it does not establish frontier completeness.

## Semantic-version decision

**NO REALACQUIRE v0.30 PROMOTION.**

REALACQUIRE 0.29 remains current.

No new Real-Language acquisition syntax is earned.

## Publication effect

The broad MQR-specific acquisition-controller thesis is closed negative under the declared source contract.

Future acquisition publication work should focus on:
- scientific-state constitution;
- faithful/lossy state compression;
- quotient sufficiency;
- state-schema reopening under new rival generation;
- naturalistic cases where compact planner states alias scientifically material distinctions.

Paper I — *Local Progress Geometry and Partial Scientific Authority* remains the strongest near-term manuscript prospect.

## Exact-head closure gate

The commit containing this FINAL-SEAL is canonical only if that exact SHA has all of:

1. `MQR-4.65/Canonical-Rust` SUCCESS
2. `MQR-4.65/Independent-Concordance` SUCCESS
3. `MQR-4.65/Deterministic-Replay` SUCCESS
4. `MQR-4.65/C4-Lean-Boundary` SUCCESS
5. `MQR-4.65/Structural-Guards` SUCCESS

Repository policy remains **MAIN_ONLY**.

No repository mutation is permitted after verified exact-head closure.
