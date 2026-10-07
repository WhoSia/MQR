# REALCOMPARE 0.40-CANDIDATE — Cross-Truncation Authority-Comparison Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED**

## Candidate coordinates

- source.certificate_id
- target.certificate_id
- direction
- source.claim_scope_hash
- target.claim_scope_hash
- scope_correspondence_receipt
- source.relevance_rule_hash
- target.relevance_rule_hash
- relevance_correspondence_receipt
- source.basis_authority_receipt
- target.basis_authority_receipt
- basis_authority_transport_receipt
- refinement_map_receipt
- source.residual_debt_hash
- target.residual_debt_hash
- debt_migration_receipt
- depth_only_flag
- cross_level_escape_trigger
- relation_state
- certificate.version

## Relation states

- A_AUTHORITY_DOMINATES_B
- B_AUTHORITY_DOMINATES_A
- AUTHORITY_EQUIVALENT_AT_SHARED_SCOPE
- AUTHORITY_INCOMPARABLE
- DEPTH_LAUNDERING
- REFINEMENT_WITHOUT_AUTHORITY_TRANSPORT
- BASIS_AUTHORITY_NONINHERITANCE
- RESIDUAL_DEBT_MIGRATION_FAILURE
- REOPEN_CROSS_LEVEL_ESCAPE

## Hard boundaries

```text
DEEPER_TRUNCATION != STRONGER_AUTHORITY
TRUNCATION_MAP != AUTHORITY_TRANSPORT
CERTIFICATE_REFINEMENT != SCIENTIFIC_SUBSUMPTION
SCOPE_INCLUSION != AUTHORITY_INCLUSION
BASIS_INCLUSION != BASIS_AUTHORITY_INHERITANCE
BIDIRECTIONAL_TRANSLATION != AUTHORITY_EQUIVALENCE
```

## Promotion boundary

`REALCOMPARE 0.40-CANDIDATE` is not promoted.

`REALACQUIRE 0.29` remains latest promoted syntax.
