# REGEX-001 — Fresh Strict-Domain-Extension Preseal

Status: FROZEN BEFORE EXECUTION

Repository:
rust-lang/regex

Regimes:
- A = regex 1.10.6
- B = regex 1.11.3
- C = regex 1.12.4

## Component

Observable component:
regex compile state plus boolean match state for a declared pattern/text packet.

Receipt token per fixture:
- COMPILE_ERR
- MATCH_0
- MATCH_1

Error message text, internal automata, performance and capture internals are out of scope.

## Bridge support B

B01..B06 are an ASCII-core regex support packet:
- literal concatenation
- ASCII character class
- alternation
- repetition
- bounded repetition
- anchors/grouping

The bridge support constitution intentionally excludes Unicode-property syntax.

## Direct support D

H01..H06 add Unicode-property / Unicode-aware character-class families while preserving the same compile+match endpoint contract.

The direct family is therefore a strict semantic extension of the frozen bridge support constitution.

## Frozen relation

```text
DOMAIN_RELATION = BRIDGE_SUBSET_DIRECT
SEMANTIC_MAP = INCLUSION
COMPONENT_RELATION = SAME_COMPONENT
QUOTIENT_RELATION = SAME_QUOTIENT
STATE_RELATION = STATE_IRRELEVANT_BY_CONSTRUCTION
ENDPOINT_CONTRACT = SAME_ENDPOINT_CONTRACT

RELATION = R1_STRICT_DOMAIN_EXTENSION
AUTHORITY = A1_EXTENSION_REQUIRES_FRESH_CONTACT
```

## Authority prediction

Even if A→B and B→C are identical on B01..B06, adjacent bridge evidence does not itself license a claim over H01..H06.

The direct extension must be executed independently.

If H01..H06 later pass across A/C, that does not retroactively convert R1 to R0.

If H01..H06 fail, that does not create R1; R1 was frozen already.

## Direct lock

No behavior has been executed at this preseal.

Bridge and direct source may be committed together, but the workflow must persist/print bridge comparison before interpreting the direct comparison.
