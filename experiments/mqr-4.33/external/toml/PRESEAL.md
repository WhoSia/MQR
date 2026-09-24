# MQR-4.33 TOML-001 — Fresh Engineering Triangle Preseal

Status: FROZEN / NO TOML-001 EXECUTION YET

## Regimes

A = toml 0.8.23
B = toml 0.9.12+spec-1.1.0
C = toml 1.0.7+spec-1.1.0

## Component

Parser acceptance over a declared TOML syntax family.

Observable:
for each fixture, exactly one symbol:

OK
or
ERR

Error-message text, parse-tree formatting, serializer output, performance and internal representation are out of scope.

## Bridge surface

B01 — integer scalar
B02 — mixed numeric array
B03 — nested standard table
B04 — single-line inline table
B05 — local time with explicit seconds
B06 — multiline basic string

These are chosen from the TOML 1.0 common syntax surface.

Adjacent A->B and B->C PASS requires byte-identical ordered OK/ERR vectors across B01..B06.

## Held-out direct surface

H01 — multiline inline table with trailing comma
H02 — basic string using \xHH escape
H03 — basic string using \e escape
H04 — local time with omitted seconds

These were selected after the version triple was frozen and from the published TOML 1.1 specification-change families, before any A/B/C execution.

The held-out family is disjoint from B01..B06.

## Structural class

S1_GENERALIZATION_RISK

component_identity = true
direct_independent = true
domain_covered = false
information_preserved = true
state_reset = true
adapter_commutative = true

Rationale:
adjacent bridge tests cover only the common 1.0 syntax subdomain, while direct testing targets a frozen 1.1 boundary family.

## Prediction before adjacent execution

The structural classifier predicts NONTRANSITIVITY_WITNESS pressure.

The actual mediated A->C prediction is not yet sealed.

It may be sealed only after:
- bridge A->B result is persisted;
- bridge B->C result is persisted;
- direct H01..H04 remains unexecuted.

## Claim ceiling

A direct mismatch would establish support-domain nontransitivity for parser acceptance across this version/spec boundary.

It would not establish logical nontransitivity of equality, whole-crate incompatibility, or failure of TOML itself.

## Direct lock

No TOML-001 direct workflow exists at this preseal.

H01..H04 may exist in source but may not be executed before the mediated seal.

## Verdict

TOML-001=FRESH-ELIGIBLE /
SUPPORT_CLASS=S1_GENERALIZATION_RISK /
BRIDGE_SURFACE=COMMON-TOML-1.0 /
DIRECT_SURFACE=HELDOUT-TOML-1.1-BOUNDARY /
OBSERVABLE=PARSE-ACCEPTANCE-ONLY /
DIRECT_EXECUTION=FORBIDDEN-BEFORE-MEDIATED-SEAL.
