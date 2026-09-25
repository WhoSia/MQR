# MQR-4.38 — World–Statement Transfer Contract Adversarial Court

Status: CLOSED / B+C+E / TRANSFER RELATION SURVIVES / UNIFIED AUTHORITY CONDUIT REJECTED / FORMALIZATION OPTIONAL / MAIN-ONLY

## Canonical question

Can scientific authority cross a formal boundary without smuggling world adequacy into the bridge?

Answer:

```text
YES, only in a non-amplifying preservation sense.
NO, if "cross" means the formal bridge creates, increases, or independently certifies world authority.
```

## Frozen attacks

All seven preregistered attacks received executable/formal witnesses:

1. Semantic Alias Problem.
2. Scope Promotion Laundering.
3. Provenance Homomorphism Insufficiency.
4. Defeatability Mirage.
5. Bridge Bootstrap Paradox.
6. Formalization Gatekeeping Error.
7. Implementation-Diversity Reification.

## Adjudication

### Semantic correspondence

The formal system cannot manufacture the interpretation that connects a world predicate to a formal predicate.

A semantic witness is therefore a typed, defeasible world-facing warrant. The compiler may verify its identity, declared predicates, state, and noncircular provenance, but its correctness about the world remains externally earned.

```text
SEMANTIC_WITNESS_PASS
!=
WORLD_SEMANTICS_PROVED_BY_COMPILER
```

### Scope

The transfer relation is indexed by three scopes:

```text
WORLD_SCOPE
STATEMENT_SCOPE
CLAIM_SCOPE
```

A formally mediated scientific claim is admissible only when the claim lies inside both the supported world scope and the formal statement scope.

The theorem may be broader than the evidence. The scientific claim may not inherit the excess.

### Ancestry

Compilation need not preserve every byte of provenance.

It must preserve every LOAD_BEARING ancestor whose state can change the target claim's authority under admissible successor evidence.

Thus graph-shape preservation and terminal-label preservation are insufficient.

### Defeat reachability

`REOPENABLE=true` is not enough.

Defeatability requires an operational path by which admissible successor evidence can reach re-adjudication.

`DEAD` or `FORBIDDEN` paths fail this coordinate; no demonstrated path remains HOLD.

### Bridge noncircularity

A bridge cannot satisfy its own semantic adequacy obligation merely by importing `BRIDGE_ADEQUATE` from itself.

Self-certified semantic witnesses fail the noncircular-warrant coordinate.

### Formalization optionality

The nonformal positive control survived:

```text
WORLD_AUTHORITY = PASS
FORMAL_CUSTODY = NOT_APPLICABLE
TRANSFER = NOT_APPLICABLE
```

Formal proof is therefore route-relative inference custody, not a universal prerequisite for scientific authority.

### Cross-language agreement

Rust and Haskell agree on the positive, HOLD, nonformal, and negative fixture family.

This is implementation-diversity evidence only.

It does not vary the interpretation, empirical ancestry, or world-contact lineage and therefore does not establish semantic/world independence.

## Surviving transfer object

The unified authority-conduit interpretation is rejected.

The surviving object is a typed relation indexed by:

```text
(claim, world scope, statement scope, interpretation witness,
 authority-relevant ancestry, defeat regime, inference-custody route)
```

For a formally mediated route the executable coordinates are:

```text
SEMANTIC_CORRESPONDENCE
SCOPE_ADMISSIBILITY
ANCESTRY_PRESERVATION
DEFEAT_REACHABILITY
NONCIRCULAR_WARRANT
FORMAL_CUSTODY_IF_APPLICABLE
```

States remain:

```text
PASS / HOLD / FAIL / NOT_APPLICABLE
```

No numeric transfer score is defined.

On the frozen attack family, Haskell exhaustive subset search found that all six coordinates are required to block all six corresponding failure families:

```text
MINIMUM_BLOCKING_COORDINATES = 6
MINIMALITY_SCOPE = FROZEN_ATTACK_FAMILY_ONLY
```

This is not a universal theorem that no future transfer coordinate can be reduced or replaced.

## Non-amplification law

Real-Language v0.5 assigns PASS the meaning:

```text
STRUCTURAL_ADMISSIBILITY_NONAMPLIFYING
```

Target scientific authority is bounded above by source world authority.

Lean theorem:

```text
MQR.transferMeetCannotRaiseWorldAuthority
```

Therefore:

```text
TRANSFER PASS != AUTHORITY CREATION
TARGET AUTHORITY <= SOURCE WORLD AUTHORITY
FORMAL CUSTODY != WORLD AUTHORITY
```

## Real-Language v0.5

Canonical Rust compiler:

`language/real/src/transfer_v05.rs`

Independent Haskell evaluator:

`language/real/haskell/TransferV05.hs`

Formal countermodels:

`language/real/lean/MQR/Transfer.lean`

Positive controls:

- `mqr-4.38-transfer-positive.real`;
- `mqr-4.38-transfer-hold.real`;
- `mqr-4.38-nonformal-world-authority.real`.

Negative guards:

- self-certified bridge;
- scope promotion;
- ancestry loss;
- defeatability mirage;
- world-authority laundering.

## Canonical receipts

Real-Language v0.5 Rust/Haskell transfer CI:

```text
run 36171972769 = SUCCESS
REAL_LANGUAGE_V05_TRANSFER_GUARDS=PASS
REAL_LANGUAGE_V05_RUST_HASKELL_CONCORDANCE=PASS
REAL_LANGUAGE_V05_FORMALIZATION_OPTIONALITY=PASS
IMPLEMENTATION_DIVERSITY_NOT_SEMANTIC_INDEPENDENCE=TRUE
```

Pinned Lean + nanoda boundary:

```text
run 36171858105 = SUCCESS
REAL_LANGUAGE_AXIOM_ANCESTRY=EMPTY
MQR438_TRANSFER_COUNTERMODELS=PASS
REAL_LANGUAGE_NANODA_INDEPENDENT_CHECKER=PASS
MQR438_NANODA_TRANSFER_COUNTERMODELS=PASS
```

Canonical stage court:

```text
run 36172207016 = SUCCESS
MQR438_RUST_TRANSFER_COURT=PASS
MQR438_HASKELL_INDEPENDENT_EVALUATOR=PASS
MQR438_TRANSFER_RELATION_INDEXED=PASS
MQR438_TRANSFER_IS_NONAMPLIFYING=PASS
MQR438_FORMALIZATION_OPTIONAL=PASS
MQR438_OUTCOME_B_C_E=PASS
```

Failed precursor receipts remain in Actions history.

The first v0.5 workflow-generation failure was a CI serialization/replacement bug and was repaired rather than waived.

The first transfer proof-boundary formulation exposed a `propext` dependency in a needlessly global finite-scope proposition. The countermodel was localized to a Boolean witness; the canonical run has empty axiom ancestry.

## Literature constraints

Abstraction/translation literature was used as a constraint source rather than as promotion evidence:

- refinement/compiler correctness motivates explicit semantic-preservation maps rather than label correspondence;
- proof-carrying code separates proof validity from the policy/specification being proved;
- abstract interpretation demonstrates that useful sound abstraction need not be complete;
- robust-compilation work shows that preservation of one formal equivalence can miss properties outside that observation criterion;
- causal-abstraction work makes observation/intervention mappings explicit and treats compositionality as an additional property rather than an automatic consequence.

These analogies do not certify MQR's world-facing witnesses.

## Outcome branches

```text
A = REJECTED as a unified scientific-authority conduit.
B = SUPPORTED: transfer survives only as an indexed relation.
C = SUPPORTED: the relation decomposes into typed coordinates; no scalar aggregate is licensed.
D = REJECTED: local bridge warrants and a useful transfer object do survive.
E = SUPPORTED: formalization is optional and route-relative.

CANONICAL SYNTHESIS = B + C + E
```

## Strongest result

Scientific authority can cross a formal boundary only as **preserved, scope-bounded, defeasible authority under an explicitly warranted interpretation relation**.

The bridge contributes auditability and inference custody.

It does not contribute world truth.

```text
WORLD WARRANT
+ NONCIRCULAR SEMANTIC WITNESS
+ SCOPE CONTAINMENT
+ AUTHORITY-RELEVANT ANCESTRY PRESERVATION
+ REACHABLE DEFEAT
+ FORMAL CUSTODY WHEN THE ROUTE USES FORMAL INFERENCE
-> NON-AMPLIFYING TRANSFER ADMISSIBILITY
```

## Verdict

```text
SEMANTIC-ALIAS-ATTACK=PASS
SCOPE-PROMOTION-LAUNDERING-GUARD=PASS
ANCESTRY-PRESERVATION-GUARD=PASS
DEFEATABILITY-MIRAGE-GUARD=PASS
BRIDGE-BOOTSTRAP-GUARD=PASS
FORMALIZATION-GATEKEEPING-ATTACK=PASS
RUST-HASKELL-CONCORDANCE=PASS
IMPLEMENTATION-DIVERSITY-SEMANTIC-INDEPENDENCE=REJECT
TRANSFER-RELATION-INDEXED=PASS
TRANSFER-STRUCTURAL-ADMISSIBILITY=PASS
TRANSFER-AUTHORITY-AMPLIFICATION=REJECT
FORMALIZATION-OPTIONALITY=PASS
FINAL-TRUTH-DISTANCE=UNIDENTIFIED
OUTCOME=B+C+E
GENERATION-IV-CONTINUES
```