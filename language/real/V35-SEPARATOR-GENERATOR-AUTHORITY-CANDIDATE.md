# REALGENERATE 0.35-CANDIDATE — Separator-Generator Authority Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED**

## Purpose

Represent the authority conditions of a separator/witness generator without converting generator plurality, search effort or current-family saturation into a scalar independence or completeness score.

## Required semantic coordinates

- `generator.id`
- `generator.provenance_hash`
- `target.claim_scope_hash`
- `source.graph_family_hash`
- `generator.grammar_hash`
- `generator.ontology_ancestry_hash`
- `generator.search_ancestry_hash`
- optional domain-specific calibration/preprocessing/formalization ancestry hashes
- `construction.prospective`
- `witness_family.hash`
- `coverage.scope`
- `coverage.warrant_kind`
- `ancestry.equivalence_class`
- `family.split_merge_receipt`
- `saturation.scope`
- `completeness.claim_kind`
- `reopen.trigger`

## Hard boundaries

```text
SEPARATOR_FOUND != SEPARATOR_FAMILY_ADEQUATE
NO_SEPARATOR_FOUND != NO_SEPARATOR_EXISTS
PROBE_DIVERSITY != GENERATOR_INDEPENDENCE
CURRENT_FAMILY_SATURATION != OPEN_WORLD_NONSEPARABILITY
GENERATOR_OUTPUT != GENERATOR_COMPLETENESS_PROOF
POSTOUTCOME_GENERATION != PROSPECTIVE_AUTHORITY
```

## Forbidden authority move

`SELF_INDUCED_INDISTINGUISHABILITY_AS_COMPLETENESS_EVIDENCE`

A generator may not cite the indistinguishability induced by its own grammar/ontology restrictions as evidence that its witness family is complete.

## Relative termination

A completeness claim may be scoped to an independently warranted finite grammar/universe/contract. This does not imply open-world completeness.

## Promotion boundary

`REALGENERATE 0.35-CANDIDATE` is not promoted.

`REALACQUIRE 0.29` remains the latest promoted syntax.
