# MQR-4.32 — Prospective Transport Composition Preseal

Status: PRESEALED / OUTCOMES UNOPENED / COMPOSITION AUTHORITY HOLD

## Stage
MQR-4.32 — Prospective Transport Composition, Three-Regime Bridge Receipts, Component-Identity Drift, Nontransitivity Witnesses, Path-Dependent Edge Algebra & Whether Typed Transport Can Compose without Smuggling Equivalence

## Inheritance
MQR-4.31 retired legacy scalar/ordinal T and replaced it with typed transport relations:

TRANSPORT(component, source_regime -> target_regime) = {
  TARGET,
  EVALUABILITY,
  SURVIVAL,
  RECEIPT
}

MQR-4.31 also froze:
A->B TRANSPORT_PASS
AND
B->C TRANSPORT_PASS
DOES NOT imply
A->C TRANSPORT_PASS.

MQR-4.32 tests that default rather than assuming it.

## Primary question
Can two earned transport edges ever license a composed transport claim without silently replacing:
- component correspondence with component identity;
- local survival with global equivalence;
- bridge compatibility with transitivity;
- implementation success with epistemic authority?

## Three-regime object
A confirmatory triangle contains regimes A, B, C and one atomic source component c_A.

Observed/direct edges:
- e_AB
- e_BC
- e_AC

Translation receipts:
- tau_AB: c_A -> c_B
- tau_BC: c_B -> c_C
- tau_AC: c_A -> c_C when a direct translation is defined.

The mediated translation is:
tau_ABC = tau_BC o tau_AB.

No equality tau_ABC = tau_AC is presumed.

## Component-identity status
Each bridge must be typed as one of:

EXACT
QUOTIENT_COMPATIBLE
SUCCESSOR_REFINEMENT
LOSSY
NONCOMMENSURABLE
UNRESOLVED

Semantics:

EXACT:
same declared atomic component semantics under a reversible representation change.

QUOTIENT_COMPATIBLE:
the target preserves exactly the distinctions required by the declared transport claim, but not necessarily all source distinctions.

SUCCESSOR_REFINEMENT:
the target adds distinctions; a source component may map to a proper target refinement set. No reverse identity is licensed.

LOSSY:
one or more distinctions required by the claim are erased.

NONCOMMENSURABLE:
no admissible component bridge is defined.

UNRESOLVED:
available receipts do not identify the bridge class.

These states are not ordered scores.

## Edge states
Inherited from MQR-4.31:

TRANSPORT_PASS
TRANSPORT_FAIL
SPLIT_REQUIRED
HOLD_UNTESTED
HOLD_TARGET_UNAVAILABLE
OUT_OF_SCOPE

## Composition candidate rule
A mediated composition candidate may be emitted only when:

1. e_AB = TRANSPORT_PASS;
2. e_BC = TRANSPORT_PASS;
3. both translation receipts are present;
4. neither bridge is LOSSY, NONCOMMENSURABLE, or UNRESOLVED;
5. the intermediate B state used by e_BC is the state actually produced/admitted by e_AB;
6. no successor-only distinction required downstream is silently absent upstream.

This creates:

COMPOSITION_CANDIDATE

not:

COMPOSITION_PASS.

## Direct validation rule
COMPOSITION_PASS requires independent direct A->C world-contact after the mediated prediction is sealed.

Direct A->C adjudication:

direct TRANSPORT_PASS + path congruence
-> COMPOSITION_PASS

direct TRANSPORT_PASS + semantically different target component/path
-> PATH_DIVERGENT_PASS

direct TRANSPORT_FAIL
-> NONTRANSITIVITY_WITNESS

direct SPLIT_REQUIRED
-> COMPOSITION_SPLIT_REQUIRED

direct HOLD_UNTESTED
-> COMPOSITION_HOLD_UNTESTED

direct HOLD_TARGET_UNAVAILABLE
-> COMPOSITION_HOLD_TARGET_UNAVAILABLE

direct OUT_OF_SCOPE
-> COMPOSITION_OUT_OF_SCOPE

No direct test:
no composition promotion.

## Path-congruence test
If tau_AC exists, compare it with tau_ABC at the declared claim scope.

Congruence states:

COMMUTES_EXACT
COMMUTES_AT_CLAIM_QUOTIENT
NONCOMMUTES_REFINEMENT
NONCOMMUTES_LOSS
NONCOMMUTES_OTHER
UNTESTED

A commuting diagram is an empirical/receipt-bearing result, not a notation convention.

## Nontransitivity witness
A canonical nontransitivity witness requires:

e_AB = TRANSPORT_PASS
e_BC = TRANSPORT_PASS
direct e_AC = TRANSPORT_FAIL or SPLIT_REQUIRED

with the A/B/C regimes and component translations independently bound before direct reveal.

A HOLD does not count as a failure witness.

## Path dependence
Path dependence is present when two admissible routes from the same source claim to the same declared target scope yield different:
- target component identities;
- evaluability states;
- survival states; or
- required assumptions.

Path dependence does not by itself invalidate either path.

It blocks path-free transport authority.

## No-smuggled-equivalence attacks
The evaluator must include explicit attacks against:

E1. PASS + PASS => PASS without direct evidence.
E2. same component name => same component identity.
E3. reversible code adapter => epistemically reversible bridge.
E4. target refinement => source-target equivalence.
E5. operation-level success => component-level evaluability.
E6. two commuting syntax maps => world-facing transport survival.
E7. direct PASS => mediated path equivalence.
E8. endpoint agreement => identical evidential ancestry.

Any implementation that licenses these by default fails MQR-4.32.

## Confirmatory admission
A fresh confirmatory triangle must satisfy all of:

- three distinguishable regimes A/B/C;
- atomic or explicitly split component target;
- adjacent A->B and B->C receipts available without opening the direct A->C native adjudication;
- direct A->C adjudication exists or can be prospectively executed after the mediated prediction is sealed;
- translation/identity evidence is separable from direct survival verdict;
- source lineage predates the MQR-4.32 native reveal;
- no MQR-4.31 discovery case used to invent typed transport may be counted as fresh confirmation.

Case selection must be structural and outcome-blind:
regime count, artifact existence, component-addressability, and receipt availability only.

## Cross-lineage requirement
Confirmatory corpus target:

- >= 2 lineage kinds;
- >= 1 RESEARCH_LAB triangle;
- >= 1 ENGINEERING_DEVELOPMENT triangle;
- ChatGPT-Web-HWPX-MCP remains ENGINEERING_DEVELOPMENT, never RESEARCH_LAB.

METHODOLOGY_DEVELOPMENT may be admitted separately.

## Minimum confirmatory pressure
Promotion from HOLD requires:

- >= 6 confirmatory triangles total;
- >= 2 lineage kinds;
- >= 1 COMPOSITION_PASS;
- >= 1 canonical NONTRANSITIVITY_WITNESS;
- >= 1 path-congruence failure or refinement divergence;
- >= 1 case where adjacent PASS edges do not license direct PASS;
- zero post-reveal edits to sealed mediated predictions.

If the available world does not furnish all of these, the result is informative HOLD rather than repaired sampling.

## Synthetic algebra lane
Before external reveal, the canonical evaluator must exhaustively test the finite typed-state algebra over:
- adjacent edge states;
- bridge identity classes;
- direct edge states;
- path congruence states.

Synthetic tests validate implementation invariants only.
They cannot establish external transport composition.

## Implementation constitution
Canonical executable surface:
Rust.

Required gates:
- cargo fmt --check
- cargo clippy -- -D warnings
- cargo test
- release build
- synthetic algebra execution
- confirmatory execution only after sealed external packet exists.

Python is not the canonical MQR-4.32 engine.
A reference implementation may be added only if it provides independent audit value.

## Evidence/artifact architecture
Borrowing the strongest pattern from mature research/development repositories:

- small committed metadata/receipt files;
- large external artifacts referenced by immutable hashes/locations;
- explicit validation logs;
- executable examples/fixtures;
- negative fixtures for forbidden inference;
- reproducible CI;
- version/toolchain pinning when needed;
- separation between research evidence and development convenience.

Repository polish is not scientific evidence.
Scientific receipts are not a substitute for software quality.

## Outcome lock
Before native direct A->C reveal, freeze for every triangle:
- triangle ID;
- lineage kind;
- A/B/C regime IDs;
- component IDs;
- tau_AB class;
- tau_BC class;
- mediated target component;
- COMPOSITION_CANDIDATE yes/no;
- predicted direct-state class when prediction is licensed;
- expected path-congruence class or explicit UNRESOLVED;
- rationale and source artifact hashes.

No field above may be edited after native direct reveal.

## Promotion ceiling
Even a successful MQR-4.32 cannot establish universal transitivity.

Maximum possible result:

TYPED TRANSPORT SUPPORTS RECEIPT-CONDITIONED PARTIAL COMPOSITION
WITH EXPLICIT NONTRANSITIVITY AND PATH DEPENDENCE.

Forbidden conclusions:
- transport is transitive;
- regime equivalence has been established;
- endpoint agreement establishes ontological identity;
- component names are globally stable;
- a category/functor law has been earned merely from formal composition.

## Current verdict
PRESEALED /
COMPOSITION-AUTHORITY-HOLD /
DIRECT-EDGE-REVEAL-FORBIDDEN-UNTIL-MEDIATED-SEAL /
RUST-CANONICAL /
NO-SMUGGLED-EQUIVALENCE /
HWPX-ENGINEERING-NONLAB /
GENERATION-IV-CONTINUES.
