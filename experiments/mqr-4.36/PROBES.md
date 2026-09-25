# MQR-4.36 — Frozen Probe Registry

Status: SEALED BEFORE PACKAGE BEHAVIOR EXECUTION

## Unicode successor probes

Source:
Unicode 16.0.0 UCD `DerivedAge.txt`.

Mechanical selection rule inherited from the candidate manifest:
for each age in {15.0, 15.1, 16.0}, take the three lowest scalar values assigned at that age, excluding surrogates and noncharacters.

Official first ranges imply:

- Unicode 15.0 starts at U+0CF3, then the next assigned scalar is U+0ECE, followed by U+10EFD.
- Unicode 15.1 starts with U+2FFC..U+2FFF; therefore the lowest three are U+2FFC, U+2FFD, U+2FFE.
- Unicode 16.0 starts at U+0897, followed by U+1B4E..U+1B4F.

Frozen refinement sequence:

```text
U15_0_01  U+0CF3
U15_0_02  U+0ECE
U15_0_03  U+10EFD

U15_1_01  U+2FFC
U15_1_02  U+2FFD
U15_1_03  U+2FFE

U16_0_01  U+0897
U16_0_02  U+1B4E
U16_0_03  U+1B4F
```

Frozen core sequence:

```text
C01 U+0041 LATIN CAPITAL LETTER A
C02 U+00E9 LATIN SMALL LETTER E WITH ACUTE
C03 U+0301 COMBINING ACUTE ACCENT
C04 U+4E00 CJK UNIFIED IDEOGRAPH-4E00
```

No Unicode package output was consulted in selecting these probes.

## JSCHEMA-001 atomic probes

Core:
- C01 integer type / integer instance
- C02 integer type / string instance
- C03 required x with integer property / empty object
- C04 numeric minimum 5 / value 6
- C05 minItems 2 / one-element array
- C06 additionalProperties false / undeclared property

Refinement, each with explicit 2020-12 metaschema:
- R01 prefixItems [integer,string], items false / [1,"x"]
- R02 same / [1,2]
- R03 properties x + unevaluatedProperties false / {"x":1}
- R04 same / {"x":1,"y":2}

## OASV-001 atomic probes

Core:
- C01 minimal OpenAPI 3.0.3 document
- C02 OpenAPI 3.0.3 document missing required info
- C03 OpenAPI 3.0.0 GET /ping with 200 response description
- C04 OpenAPI 3.0.3 component schema using nullable:true

Refinement:
- R01 minimal OpenAPI 3.1.0 document
- R02 3.1.0 document with jsonSchemaDialect
- R03 3.1.0 component schema with type ["string","null"]
- R04 3.1.0 document with webhooks:{}

## Closure

For all four cases, the declared probe closure is exactly the listed finite atomic set.

No generated compositions are part of MQR-4.36 P.

Therefore exhaustive execution of every listed D-relevant atom can earn:

```text
INTERNAL_RESIDUE_WITHIN_DECLARED_PROBE_CLASS = ZERO
```

provided execution is complete.

It cannot earn open-world closure.
