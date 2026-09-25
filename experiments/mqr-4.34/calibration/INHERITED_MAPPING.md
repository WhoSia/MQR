# MQR-4.34 — Inherited Collision Mapping

Status: ZERO-CREDIT CALIBRATION / RULES FROZEN BEFORE MAPPING

Primary relation grammar preseal:
16c0d474075fbff5a3b17a12c41baee6a810b664

## TKN-001

Inherited facts from MQR-4.32/4.33:
- bridge fixtures and direct fixtures were disjoint;
- both were generated under the same declared WordLevel vocabulary, [UNK] token, Whitespace pre-tokenizer and token-output quotient;
- direct testing did not add a new tokenization grammar or successor-only output distinction;
- executions were reset/stateless at the declared claim scope;
- endpoint contract was the same ordered token-ID/token-string quotient.

Frozen 4.34 mapping:

```text
DOMAIN_RELATION = SAME_GENERATOR
SEMANTIC_MAP = IDENTITY_ON_SCOPE
COMPONENT_RELATION = SAME_QUOTIENT
QUOTIENT_RELATION = SAME_QUOTIENT
STATE_RELATION = RESET_EQUIVALENT
ENDPOINT_CONTRACT = SAME_ENDPOINT_CONTRACT

=> R0 SAME_GENERATOR_HOLDOUT
=> A0 HOLDOUT_SUPPORT_ADMISSIBLE
```

Historical direct outcome remains COMPOSITION_PASS.

The outcome is not an input to the mapping.

## TOML-D1

Inherited post-failure diagnostic facts from MQR-4.33:
- bridge B01..B06 used common TOML-1.0-style syntax;
- direct H01..H04 were frozen TOML-1.1 boundary families;
- the common post-failure adapter recovered bridge acceptance across A/B/C;
- direct support therefore added admissible syntax families outside the bridge support constitution;
- observable remained parser OK/ERR;
- executions were reset/stateless.

Frozen 4.34 mapping:

```text
DOMAIN_RELATION = BRIDGE_SUBSET_DIRECT
SEMANTIC_MAP = INCLUSION
COMPONENT_RELATION = SAME_COMPONENT
QUOTIENT_RELATION = SAME_QUOTIENT
STATE_RELATION = RESET_EQUIVALENT
ENDPOINT_CONTRACT = SAME_ENDPOINT_CONTRACT

=> R1 STRICT_DOMAIN_EXTENSION
=> A1 EXTENSION_REQUIRES_FRESH_CONTACT
```

Historical diagnostic outcome remains a boundary NONTRANSITIVITY_WITNESS.

The outcome is not an input to the mapping.

## Calibration question

MQR-4.33 had:

```text
P_433(TKN-001) = P_433(TOML-D1)
```

The frozen MQR-4.34 relation grammar predicts:

```text
MU_434(TKN-001) != MU_434(TOML-D1)
```

If the independent compilers agree on this mapping:

```text
DIAGNOSTIC_INHERITED_SEPARATION = PASS
```

This earns zero fresh external validity.

It only shows that the new representation can express a distinction the old Boolean quotient erased.

## Credit

Fresh N:
0.

Promotion credit:
0.

Post-mapping rule changes:
forbidden.
