# Real-Language v0.12 — Burden-Ontology Revision Transport

Status: EXECUTABLE / MQR-4.45 CLOSED / VERSIONED / LOSS-AWARE / MAPPED-SUBSPACE / OPEN-REVISION

## Boundary

MQR-4.44 established that obligation labels and counts are not adequate primitives and moved governance to a declared burden ontology. MQR-4.45 attacks the persistence of that burden ontology across constitution revision.

v0.12 evaluates a declared Burden-Ontology Revision Receipt (BORR). It does not infer metaphysical identity between scientific burden concepts.

## Canonical objects

- BORR — Burden-Ontology Revision Receipt
- BTR — Burden Transport Relation
- BIW — Burden-Identity Witness surface
- DTL — Debt-Transport Ledger
- RLV — Revision Loss Vector
- CCE — Cross-Constitution Comparability Envelope
- OCR — Obligation Conflict Receipt
- RDR — Revision Diamond Receipt

## Transport kinds

```text
EXACT
REFINE
MERGE
OVERLAP
DISJOINT
UNMAPPED
```

These are declared transport semantics, not world-identity certificates.

## Grammar

```text
REALREVISE 0.12
id <id>
claim_scope <scope>
source_ontology <id>
target_ontology <id>
source_burden <id> <challenge+...> <DEBT|CLEAR>
target_burden <id> <challenge+...>
map <source+...> <EXACT|REFINE|MERGE|OVERLAP|DISJOINT|UNMAPPED> <target+...> <INTERNAL|EXTERNAL|MIXED>
target_cover <target+...>
withdraw_source <source> <DECLARED|NONE>
debt_trace <source> <target>
debt_count_mode <SOURCE_ANCESTRY|TARGET_CARRIER>
conflict <id> <source-obligation> <target-obligation> <MANDATE|WITHDRAWAL|UNMAPPED|MERGE_COLLISION>
path <id> <source> <DIRECT|via-ontology> <target> <FULL|PARTIAL|NONE>
witness_future_burden <token|NONE>
authorize_...
END
```

## Debt continuity

A debt-bearing source burden may be locally transported only when one of the following holds:

- explicit source withdrawal;
- EXACT/REFINE mapping with full declared challenge preservation, full target coverage and source-ancestry debt traces;
- MERGE mapping whose target coverage includes the source burden and whose source debt ancestry remains explicitly traced.

OVERLAP, DISJOINT and absent mapping do not discharge source debt.

## Split/merge accounting

Historical debt multiplicity is keyed by source ancestry, not target-cardinality.

```text
ONE SOURCE DEBT -> TWO REFINED TARGET CARRIERS
!= TWO INDEPENDENT HISTORICAL DEBTS
```

Conversely:

```text
TWO SOURCE DEBTS -> ONE MERGED TARGET
!= ONE HISTORICAL DEBT
```

The target representation may split or merge while the debt ancestry set remains preserved.

## Partial comparability

```text
revision.comparability_mode=MAPPED_SUBSPACE_ONLY
```

A mapped subset licenses comparison only on that subset. It does not establish whole-ontology commensurability.

## Revision diamonds

Direct and composed revision paths may disagree. v0.12 treats unequal declared strengths for the same source/target pair as a reopening event.

```text
DIRECT != COMPOSED
-> REOPEN
```

This does not make the direct path infallible.

## Conflict boundary

Conflict declarations are localized and counted. The evaluator can require arbitration but never chooses a scientifically true winner from recency, provenance or scalar severity.

## Hard guards

```text
revision.comparability_mode=MAPPED_SUBSPACE_ONLY
revision.conflict_scalar_default=OFF
revision.reopen_on_path_conflict=YES
revision.world_burden_identity_inferred=NO
revision.future_revision_closed=NO
revision.newer_ontology_truth_oracle=NO
revision.provenance_truth_oracle=NO
revision.guidance_mode=VERSIONED_LOSS_AWARE_TRANSPORT
```

## Implementation

- canonical evaluator: Rust `src/revision_v12.rs` / `real-v12-revise`
- independent relational evaluator: Prolog `prolog/revision_v12.pl`
- formal boundary: Lean `lean/MQR/Revision.lean`

Rust–Prolog concordance is implementation-diversity evidence only. Lean certifies finite structural countermodels, not world identity between evolving scientific concepts.


## Final closure boundary

MQR-4.45 closes only the declared cross-version transport problem.

The final executable boundary is:

```text
SAME LABEL != BURDEN IDENTITY
DIFFERENT LABEL != BURDEN NONIDENTITY
REFINE REQUIRES FULL DECLARED COVERAGE FOR DEBT CONTINUITY
MERGE MUST PRESERVE EACH SOURCE-DEBT ANCESTRY
UNMAPPED DEBT REMAINS UNRESOLVED
TARGET NOVELTY IS NOT RETROACTIVE SOURCE DEBT
COMPARABILITY = MAPPED_SUBSPACE_ONLY
CONFLICT LOCALIZATION != TRUE WINNER
DIRECT / COMPOSED DISAGREEMENT -> REOPEN
WORLD BURDEN IDENTITY = NOT INFERRED
FUTURE REVISION CLOSURE = NO
```

The exact final same-head commit and workflow receipts are kept in the external Research OS closure receipt so recording those identifiers does not mutate the sealed Git head.

<!-- mqr-4.45-final-same-head-seal -->
