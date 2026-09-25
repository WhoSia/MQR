# Real-Language v0.6 — Compositional Transfer Boundary

Status: EXECUTABLE CANDIDATE / MQR-4.39 / CONDITIONAL PATHWISE NON-AMPLIFICATION

## Purpose

v0.6 does not make v0.5 transfer automatically compositional.

It represents a path of locally admissible transfers and asks whether scientific authority can survive the path without being reset, widened, detached from ancestry, or insulated from defeat.

```text
A --T1--> B --T2--> C
```

Local v0.5 PASS on T1 and T2 creates only a composition candidate.

## Algebraic skeleton

The authority lattice itself is compositional.

Lean proves:
- `MQR.authorityMeetAssociative`;
- `MQR.authorityMeetPassIdentity`;
- `MQR.noLaunderTransitive`.

Thus, if the same authority ordering and source identity are genuinely preserved,

```text
A2 <= A1 <= A0
=> A2 <= A0
```

The scientific problem is whether each bridge preserves the objects to which that inequality applies.

## Composition coordinates

v0.6 uses:

```text
ENDPOINT_COMPATIBILITY
SEMANTIC_COMPOSITION
SCOPE_PULLBACK
ANCESTRY_PULLBACK
DEFEAT_PULLBACK
ASSUMPTION_CLOSURE
LOCAL_TRANSFER_STATE
GLOBAL_NONAMPLIFICATION
DIRECT_PATH_RECEIPT
```

and a derived:

```text
COMPOSITION
```

States remain PASS / HOLD / FAIL. No scalar exists.

## Endpoint compatibility

The target representation of each bridge must match the declared source representation of the next bridge.

Syntactic endpoint compatibility is necessary but not sufficient for semantic composition.

## Semantic composition

Each local semantic witness must survive, and the path must carry an explicit composite semantic witness.

```text
LOCAL WITNESS PASS + LOCAL WITNESS PASS
!=
COMPOSITE SEMANTICS PASS
```

The composite witness remains defeasible and world-facing.

## Scope pullback

Composite claim scope is calculated through the declared scope maps from the original source.

A final claim receives PASS only when every claimed element lies in the image reachable through the full bridge path.

Therefore:

```text
COMPOSITE SCOPE <= PATHWISE PULLBACK/IMAGE
COMPOSITE SCOPE != UNION OF LOCAL SCOPES
```

## Ancestry pullback

Every original LOAD_BEARING ancestor must remain preserved across every bridge in the path.

The intermediate representation may not become a fresh provenance origin merely because local compilation succeeded.

This blocks the Intermediate Provenance Reset.

## Defeat pullback

Each local bridge must expose a reachable defeat segment whose endpoints align with that bridge.

Local reopenability does not establish end-to-end scientific corrigibility by itself; v0.6 treats the path as requiring a compatible chain of defeat segments.

This is a first executable approximation of defeat pullback. It does not claim exhaustive open-world defeat coverage.

## Hidden-assumption closure

All path assumptions are accumulated.

The composite route:
- takes the weakest assumption status into its ceiling;
- rejects contradictory values for the same load-bearing assumption key;
- does not reset the assumption ledger at an intermediate representation.

Thus two locally admissible assumption sets may fail jointly.

## Global non-amplification

The final authority is bounded against the original path source, not the most recent intermediate packet.

The ceiling is the meet of:
- original source authority;
- all pulled-back load-bearing ancestors;
- all load-bearing assumptions.

A downstream bridge may not treat an intermediate PASS label as a new independent source ceiling.

## Direct-path receipt

MQR retains the earlier principle:

```text
ADJACENT TRANSPORT SURVIVAL != COMPOSITION SUPPORT
```

Therefore v0.6 requires a direct A->C receipt for full composite PASS.

If the direct receipt is HOLD, the composition remains HOLD even when every local coordinate is PASS.

If it is FAIL, the composition fails.

This is intentionally conservative: it prevents a long chain of locally certified transformations from laundering the absence of a direct world-facing adjudication.

## Categorical status

The authority meet operation has identity and associativity.

The full scientific transfer object does not thereby become a strict category.

At MQR-4.39 preclosure the best candidate description is:

```text
PARTIAL / WITNESS-INDEXED COMPOSITION
```

Composition is defined only when endpoint, semantic, scope, ancestry, defeat, assumption, global-ceiling and direct-path obligations are satisfied.

Semantic witnesses behave more like explicit higher cells or proof objects than invisible categorical equality.

MQR does not yet claim a bicategory theorem; "bicategorical-like" is only a structural analogy until the witness equivalences and coherence laws are earned.

## Executable implementation

Canonical Rust:

```text
language/real/src/compose_v06.rs
binary: real-v06-compose
```

Independent Haskell:

```text
language/real/haskell/ComposeV06.hs
```

Lean:

```text
language/real/lean/MQR/Composition.lean
```

## Core anti-laundering rules

Reject or hold:

```text
LOCAL_PASS(T1) + LOCAL_PASS(T2) -> COMPOSITE_PASS
without semantic_comp receipt

LOCAL_SCOPE_PASS + LOCAL_SCOPE_PASS -> final claim outside pathwise mapped scope

INTERMEDIATE_PASS -> reset original LOAD_BEARING ancestry

LOCAL_REOPENABLE(T1) + LOCAL_REOPENABLE(T2)
-> global reopenability without endpoint-compatible defeat chain

ASSUMPTION(A) in T1 + ASSUMPTION(not A) in T2 -> PASS

SOURCE_HOLD -> intermediate reindex -> FINAL_PASS

ADJACENT_PASS + ADJACENT_PASS -> DIRECT_PASS
```

## Ceiling

v0.6 can certify conditional pathwise transfer admissibility.

It cannot certify that the world-facing semantic witnesses are true merely because they compose syntactically.

```text
ALGEBRAIC COMPOSABILITY != EPISTEMIC COMPOSABILITY
LOCAL NON-AMPLIFICATION != GLOBAL NON-AMPLIFICATION WITHOUT SOURCE CONTINUITY
COMPOSITION PASS != TRUTH ORACLE
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```
