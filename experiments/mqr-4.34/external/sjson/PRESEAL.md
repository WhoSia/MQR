# SJSON-001 — Fresh Same-Generator-Heldout Preseal

Status: FROZEN BEFORE EXECUTION

Repository:
serde-rs/json

Regimes:
- A = serde_json 1.0.140
- B = serde_json 1.0.145
- C = serde_json 1.0.151

## Component

Observable component:
parse of a declared RFC-8259 JSON packet into serde_json::Value followed by compact serialization.

Receipt token per fixture:
- ERR
- OK:<compact JSON>

Parser error text, allocation, map internals and performance are out of scope.

## Common support generator G

Both bridge B01..B06 and direct H01..H06 are disjoint, balanced samples from the same declared JSON support constitution.

Each packet includes the same semantic families:
- scalar;
- number;
- string;
- array;
- object;
- nested object/array.

The direct packet does not add a new grammar, new specification epoch or new endpoint distinction.

## Frozen relation

```text
DOMAIN_RELATION = SAME_GENERATOR
SEMANTIC_MAP = IDENTITY_ON_SCOPE
COMPONENT_RELATION = SAME_COMPONENT
QUOTIENT_RELATION = SAME_QUOTIENT
STATE_RELATION = STATE_IRRELEVANT_BY_CONSTRUCTION
ENDPOINT_CONTRACT = SAME_ENDPOINT_CONTRACT

RELATION = R0_SAME_GENERATOR_HOLDOUT
AUTHORITY = A0_HOLDOUT_SUPPORT_ADMISSIBLE
```

## Authority prediction

If adjacent bridge receipts survive, MQR-4.34 allows a mediated A→C prediction over H01..H06 at the same endpoint scope.

The direct packet remains an independent held-out test and may falsify that prediction.

A direct failure would falsify the mediated prediction; it would not retroactively retype R0.

## Direct lock

No behavior has been executed at this preseal.

Bridge and direct source may be committed together, but bridge comparison and mediated prediction must be emitted before direct comparison is adjudicated.
