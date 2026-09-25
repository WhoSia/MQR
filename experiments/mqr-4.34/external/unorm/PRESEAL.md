# UNORM-001 — Fresh Successor-Refinement Preseal

Status: FROZEN BEFORE NORMALIZATION EXECUTION

Repository:
unicode-rs/unicode-normalization

Regimes and embedded Unicode data epochs:
- A = unicode-normalization 0.1.22 / Unicode 15.0.0
- B = unicode-normalization 0.1.23 / Unicode 15.1.0
- C = unicode-normalization 0.1.24 / Unicode 16.0.0

The Unicode version constants were inspected only as package data-epoch metadata before behavioral execution.

## Component

Observable:
NFC normalization output represented as an ordered uppercase Unicode-code-point sequence.

Performance, internal tables, quick-check implementation details and allocation are out of scope.

## Bridge support B

B01..B06 use characters and canonical-composition patterns already established before Unicode 15.0.

The bridge asks whether the old normalization quotient is preserved across A/B/C.

## Direct successor support D

H01..H06 use Unicode-16.0 successor-only normalization contexts.

The packet is derived from Unicode normalization documentation before crate execution.

It includes Kirat Rai and Tulu-Tigalari sequences specifically identified as exercising new composition/normalization context.

## Forgetting map

Let q_D be the Unicode-16.0 normalization behavior over the expanded repertoire.

Let q_B be the normalization behavior restricted to the pre-15.0 bridge repertoire.

Define:

```text
pi : q_D -> q_B
```

by restriction of the successor normalization function to the bridge repertoire.

This preserves all bridge-observable behavior while forgetting successor-only inputs/distinctions.

## Frozen relation

```text
DOMAIN_RELATION = BRIDGE_SUBSET_DIRECT
SEMANTIC_MAP = FORGETFUL_SURJECTION
COMPONENT_RELATION = REFINED_COMPONENT
QUOTIENT_RELATION = DIRECT_REFINES_BRIDGE
STATE_RELATION = STATE_IRRELEVANT_BY_CONSTRUCTION
ENDPOINT_CONTRACT = COARSE_ENDPOINT_PRESERVED

RELATION = R2_SUCCESSOR_REFINEMENT
AUTHORITY = A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED
```

## Authority prediction

Adjacent evidence may support the preserved bridge quotient.

It does not license successor-only Unicode-16.0 normalization behavior without direct contact.

A/C may therefore:
- agree on B;
- differ on D;
without contradiction.

Such divergence is expected to be interpretable as successor refinement rather than generic composition failure if the frozen relation survives.

## Direct lock

No unicode-normalization crate execution has occurred at this preseal.

The exact bridge/direct code-point packets are frozen in source before the workflow is launched.
