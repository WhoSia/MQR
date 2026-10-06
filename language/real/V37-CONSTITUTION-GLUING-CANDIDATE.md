# REALGLUE 0.37-CANDIDATE — Constitution-Gluing Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED**

## Purpose

Represent composition of locally warranted coverage constitutions without laundering overlap agreement into global authority or deleting nonoverlap obligations.

## Candidate coordinates

- joint.claim_scope_hash
- constitution.left_id
- constitution.right_id
- overlap.scope_hash
- left_only.obligations_hash
- right_only.obligations_hash
- shared.obligations_hash
- unresolved_conflicts_hash
- translation.map_hash
- transported_obligation_provenance
- invented_obligations_hash
- dropped_obligations_hash
- joint_authority_scope
- hidden_nonoverlap_reopen_trigger
- certificate.version

## Hard boundaries

```text
OVERLAP_AGREEMENT != GLOBAL_WARRANT
LOCAL_WARRANT != GLOBAL_GLUABILITY
UNION_OF_TARGETS != WARRANTED_JOINT_CONSTITUTION
INTERSECTION_OF_TARGETS != SAFE_COMMON_DENOMINATOR
COMMON_VOCABULARY != COMMON_OBLIGATION
TRANSLATION != AUTHORITY_EQUIVALENCE
COMPOSITION != OBLIGATION_PRESERVATION
```

## Positive rule

Composition may preserve authority but cannot create it ex nihilo.

## Promotion boundary

`REALGLUE 0.37-CANDIDATE` is not promoted.

`REALACQUIRE 0.29` remains latest promoted syntax.
