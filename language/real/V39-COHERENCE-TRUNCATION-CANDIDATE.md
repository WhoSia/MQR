# REALTRUNCATE 0.39-CANDIDATE — Coherence-Termination Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED**

## Candidate coordinates

- claim.scope_hash
- checked.coherence_level_max
- checked.obstruction_family_hash
- coherence_basis_hash
- basis_authority_source
- higher_level_relevance_rule_hash
- residual_higher_order_debt
- reopening_trigger
- scope_version
- certificate_version

## Hard boundaries

```text
FINITE_COHERENCE_PASS != OPEN_WORLD_COHERENCE_COMPLETENESS
NO_OBSTRUCTION_BELOW_N != NO_OBSTRUCTION_ABOVE_N
TRUNCATION_LEVEL != NATURAL_AUTHORITY_BOUNDARY
MINIMAL_BASIS != GLOBAL_COMPLETENESS
HIGHER_ORDER_CERTIFICATE != SELF_WARRANTING_CERTIFICATE
FINITE_TERMINATION != FINALITY
REOPENABILITY != FAILURE_OF_PRIOR_SCOPED_AUTHORITY
```

## Positive rule

Finite coherence recursion may terminate only relative to an explicit claim scope, independently warranted higher-level relevance rule, a scope-relative sufficient basis, explicit residual higher-order debt, and a reopening trigger.

## Promotion boundary

`REALTRUNCATE 0.39-CANDIDATE` is not promoted.

`REALACQUIRE 0.29` remains latest promoted syntax.
