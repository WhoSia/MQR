# Real-Language / Real-Packet v0.3

Real-Language is MQR's active event-to-realist-authority language.

It compiles a scientific, methodological, or engineering event into a scoped authority packet while preserving open-world residue and successor vulnerability.

## Version boundary

### v0.2
Historical profile grammar:

- C/E/P/R authority gates
- W/N/I/T/D profile
- scalar projection OFF by default

v0.2 remains readable for archival reproducibility.

### v0.3
Current grammar:

- C/E/P/R authority gates
- W/N/I/D profile
- **legacy axis T is forbidden**
- transport is represented by a typed relation map
- lineage kind is explicit

MQR-4.31 found that one T coordinate conflated:
1. transport target/component,
2. evaluability,
3. survival conditional on evaluation.

Therefore:

```text
legacy.profile.T = DEPRECATED
transport.mode = TYPED_RELATION_MAP
```

## Lineage kinds

Every v0.3 packet must declare exactly one:

- `RESEARCH_LAB`
- `ENGINEERING_DEVELOPMENT`
- `METHODOLOGY_DEVELOPMENT`
- `OTHER`

This prevents development lineages from being silently reconstructed as scientific Labs.

Example:
ChatGPT-Web-HWPX-MCP is `ENGINEERING_DEVELOPMENT`.

The lineage kind changes interpretation/context, not the mechanical transport semantics.

## Authority gates

- C: constitutional/adjudication legitimacy
- E: admissible world-contact
- P: provenance/time/auditability
- R: open-world rival invariance

If any gate is not PASS:
authority = HOLD.

## Current profile

v0.3 retains:

- W: world resistance
- N: noncommon evidence-route strength
- I: inferential identification
- D: defeat exposure / corrigibility

Calibration status after MQR-4.30:

```text
W = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
I = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
N = LEVEL-3 HOLD
D = external polarity PASS / Level-3 discriminant HOLD
```

The old scalar TPX remains retired.

```text
PROFILE_ORDER = PARETO_PARTIAL
SCALAR_PROJECTION_DEFAULT = OFF
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```

## Typed transport

v0.3 transport syntax:

```text
transport "<component>" "<source-regime>" "<target-regime>" <DIMENSION> <EVALUABILITY> <SURVIVAL> "<note>"
```

### Evaluability

Exactly one:

- `TESTED`
- `UNTESTED_AVAILABLE`
- `TARGET_UNAVAILABLE`
- `OUT_OF_SCOPE`

### Survival

When evaluability is `TESTED`:

- `SURVIVED`
- `FAILED`
- `MIXED_OR_NONATOMIC`

Otherwise:

- `NA`

### Derived transport authority

```text
TESTED + SURVIVED            -> TRANSPORT_PASS
TESTED + FAILED              -> TRANSPORT_FAIL
TESTED + MIXED_OR_NONATOMIC -> SPLIT_REQUIRED
UNTESTED_AVAILABLE           -> HOLD_UNTESTED
TARGET_UNAVAILABLE           -> HOLD_TARGET_UNAVAILABLE
OUT_OF_SCOPE                 -> OUT_OF_SCOPE
```

No averaging is permitted.

Claim-level transport is compiled to one of:

- `ALL_REQUIRED_CELLS_PASS`
- `SOME_REQUIRED_CELLS_FAIL`
- `PARTIAL_WITH_HOLDS`
- `SPLIT_REQUIRED`
- `NO_EVALUABLE_TARGET`

## MQR-4.31 validation

Fresh transport confirmation was sealed before native-label reveal.

Confirmatory corpus:
- RESEARCH_LAB: C3X and EPISTEME
- ENGINEERING_DEVELOPMENT: ChatGPT-Web-HWPX-MCP

Result:

```text
16 confirmatory cells
15/16 exact typed-state agreement = 0.9375
C1 untested-vs-failed = PASS
C2 componentwise transport = PASS
C3 cross-lineage concordance = PASS
C4 HWPX engineering/non-Lab typing = PASS
C5 success-collapse attack = PASS
```

The one mismatch was informative:
an operation-level `reject_all` promotion was incorrectly generalized to an uninstantiated component-specific `insert-reject` round-trip specimen.

Therefore:
**component-specific evaluability cannot be inherited from broader operation success.**

## Packet grammar

```text
REALPACKET 0.3
id "packet-id"
epoch "epoch"
claim CONSTRAINT "claim text"
scope "licensed scope"
lineage ENGINEERING_DEVELOPMENT

gate C PASS
gate E PASS
gate P PASS
gate R PASS

axis W 0.75 "why"
axis N 0.50 "why"
axis I 0.75 "why"
axis D 0.75 "why"

transport "component-a" "source" "target" VERSION TESTED SURVIVED "why"
transport "component-b" "source" "target" VERSION UNTESTED_AVAILABLE NA "why"

generator STRUCTURAL "description"
rival SURVIVING "description"
residue MODERATE "description"
mystery OPEN "description"
ontic HOLD "description"
successor VULNERABLE
source "source pointer"
END
```

## Canonical implementation policy

- Rust is the canonical compiler and the default for newly touched executable MQR surfaces.
- Python is retained as an independent reference/audit implementation where useful.
- Existing Python is not mechanically rewritten merely to change repository language statistics.
- Migration occurs when a surface becomes live again or when Rust/static implementation has a concrete reliability, portability, or performance advantage.

CI requires:
- v0.2 archival packet compatibility;
- v0.3 Rust/Python canonical-receipt concordance;
- rejection of v0.3 legacy `axis T`;
- Rust-first build success.

Implementation language is not an epistemic primitive.

## Ceiling

Real-Language is allowed to represent earned authority and transport relations.

It is not allowed to manufacture:
- a truth percentage,
- final ontology,
- universal cross-domain numeric units,
- transport authority for an untested component.
