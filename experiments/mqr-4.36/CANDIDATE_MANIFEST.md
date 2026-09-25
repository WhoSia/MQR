# MQR-4.36 — Frozen Naturalistic Candidate Manifest

Status: SEALED BEFORE PACKAGE BEHAVIOR EXECUTION

Primary preseal:
`903374ad64ee3c38f23598b84624166da14f718d`

## Exposure ledger

Before this manifest:
- package/repository identities were known;
- PyPI simple-index version filenames were inspected for `jsonschema` and `wcwidth` only;
- no changelog, issue, PR, behavior fixture, test output or release-note behavior summary for any candidate was inspected;
- package behavior for the declared probes has not been executed.

The candidates below are frozen now. Install failure or API incompatibility is an admissible E3_UNRESOLVED outcome and will not be repaired by substituting a different package.

## Fiber F-R1 — strict domain extension

Frozen NU3 key:

```text
MU = R1|INCLUSION|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT
MAP_ALGEBRA = PARTIAL
INTERVENTION_ALIGNMENT = EMPIRICAL_ONLY
SENSITIVITY_SCOPE = BOUNDARY
```

### JSCHEMA-001

Lineage:
ENGINEERING_DEVELOPMENT.

Package:
`jsonschema`.

Frozen versions:
- A = 3.2.0
- B = 4.17.3
- C = 4.25.1

Probe domain:
JSON Schema + JSON instance pairs.

Observable:
`VALID | INVALID | EXECUTION_ERROR`.

Core subalgebra:
a finite set of Draft-7-style schema/instance pairs using only:
- type;
- required;
- properties;
- minimum;
- minItems;
- additionalProperties.

Refinement set:
a finite set explicitly marked as JSON Schema 2020-12 and using:
- prefixItems;
- unevaluatedProperties.

Adapter:
version-local Python process using the public `jsonschema.validators.validator_for` surface when available.
If the declared adapter cannot execute in a version, record EXECUTION_ERROR; do not invent a replacement surface after reveal.

### OASV-001

Lineage:
ENGINEERING_DEVELOPMENT.

Package:
`openapi-spec-validator`.

Frozen versions:
- A = 0.5.6
- B = 0.6.0
- C = 0.7.2

Probe domain:
OpenAPI documents represented as Python dictionaries.

Observable:
`VALID | INVALID | EXECUTION_ERROR`.

Core subalgebra:
minimal OpenAPI 3.0.x documents plus bounded perturbations in paths/components/schema fields.

Refinement set:
minimal OpenAPI 3.1.x documents using 3.1-specific schema-language surface, including a type-array nullability case.

Adapter:
version-local Python process calling the public package validation entry surface selected in the frozen harness source.
If that exact frozen adapter is unavailable, record EXECUTION_ERROR.

## Fiber F-R2 — successor refinement

Frozen NU3 key:

```text
MU = R2|SURJECTIVE|SAME_COMPONENT|COARSE_QUOTIENT|SUCCESSOR|SAME_ENDPOINT
MAP_ALGEBRA = QUOTIENT_HOMOMORPHIC
INTERVENTION_ALIGNMENT = EMPIRICAL_ONLY
SENSITIVITY_SCOPE = BOUNDARY
```

### UCD2-001

Lineage:
ENGINEERING_DEVELOPMENT.

Package:
`unicodedata2`.

Frozen versions:
- A = 14.0.0
- B = 15.1.0
- C = 16.0.0

Probe domain:
Unicode scalar values.

Observable:
tuple `(category, combining, east_asian_width, name_present)`.

Core subalgebra:
fixed ASCII/Latin/combining probes known to precede all three declared standards.

Refinement set:
code points selected mechanically from Unicode 16.0 DerivedAge data by the frozen rule:
- lowest scalar values whose age is 15.0;
- lowest scalar values whose age is 15.1;
- lowest scalar values whose age is 16.0;
with noncharacters/surrogates excluded.

No package outcome is used to choose the refinement points.

Coarsening:
`assigned := category != "Cn"`.

### WCWIDTH-001

Lineage:
ENGINEERING_DEVELOPMENT.

Package:
`wcwidth`.

Frozen versions:
- A = 0.2.5
- B = 0.2.10
- C = 0.2.14

Probe domain:
single Unicode scalar values.

Observable:
`wcwidth(character)`.

Core subalgebra:
the same frozen pre-successor ASCII/Latin/combining set used by UCD2-001.

Refinement set:
the exact same Unicode-16 DerivedAge-generated code-point set as UCD2-001.

Coarsening:
width class collapsed to `NEGATIVE | ZERO | POSITIVE`.

## Frozen probe-expression bound

For each case:
- each atomic frozen core/refinement probe is executed once per A/B/C;
- no pairwise/product expansion is added after reveal;
- the declared closure is exactly the finite atomic probe set.

This deliberately makes the first finite-residue theorem modest and auditable.

## Adjudication

For each version V, let `o_V(p)` be the exact frozen observable.

Bridge admissibility:
- A/B core equality after declared coarsening;
- B/C core equality after declared coarsening.

Empirical reach A/C:
- E2_NONE if any core probe differs after coarsening;
- E0_FULL if every core and refinement probe matches exactly;
- E1_QUOTIENT_ONLY otherwise when core coarsened equality holds;
- E3_UNRESOLVED if the frozen adapter/environment prevents adjudication.

NU3 collision search is performed only between cases in the same frozen fiber.

## Decision family D36

Freeze a coarse decision:

```text
ACTION_FULL_REUSE      <- E0_FULL
ACTION_CORE_ONLY       <- E1_QUOTIENT_ONLY
ACTION_REJECT_REUSE    <- E2_NONE
ACTION_HOLD            <- E3_UNRESOLVED
```

Because this action map is injective over E labels, any E collision is also a D36 collision.

A second deliberately coarser diagnostic decision is frozen:

```text
D36_CORE:
  ALLOW_CORE_REUSE <- E0_FULL or E1_QUOTIENT_ONLY
  REJECT_CORE_REUSE <- E2_NONE
  HOLD <- E3_UNRESOLVED
```

This permits a representation to fail exact reach sufficiency while remaining sufficient for the narrower core-reuse decision.

## Promotion ceiling

The sealed fresh corpus has:
- N = 4;
- domain families = 2;
- lineage kinds = 1;
- RESEARCH_LAB N = 0.

Therefore the presealed MQR-4.36 rule already implies:

```text
NU3_NATURALISTIC_IDENTIFICATION = HOLD
```

unless the constitution is explicitly revised before any behavioral reveal, which is not authorized.

A fresh same-NU3 opposite-E collision still earns:

```text
NU3_NATURALISTIC_SUFFICIENCY = FAIL
```

No post-reveal replacement case is allowed.
