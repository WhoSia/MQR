# MQR-4.34 — Candidate, Regime and Contamination Manifest

Status: FROZEN BEFORE ANY FRESH 4.34 BEHAVIORAL EXECUTION

Primary preseal:
16c0d474075fbff5a3b17a12c41baee6a810b664

## Engineering candidates

### REGEX-001 — ELIGIBLE

Repository:
rust-lang/regex

Metadata inspected:
Git tag refs only.

No changelog, release-note body, commit message, test output or behavioral source was read before regime sealing.

The latest visible stable line is 1.13.x and is treated as active.

Under the presealed rule, use the latest stable patch from each of the latest three completed stable minor lines:

- A = regex 1.10.6
- B = regex 1.11.3
- C = regex 1.12.4

Fresh relation surface:
to be frozen before compilation from a mechanically generated regex packet.

No behavioral execution has occurred.

### UNORM-001 — CONDITIONALLY ELIGIBLE

Repository:
unicode-rs/unicode-normalization

Metadata inspected:
Git tag refs only.

The repository exposes one long 0.1.x release line rather than three completed minor lines.

Under the presealed fallback, the mechanically selected latest three stable tags are:

- A = v0.1.22
- B = v0.1.23
- C = v0.1.24

Before any normalization execution, 4.34 may inspect only version/Unicode-data metadata sufficient to determine whether these regimes span at least two Unicode-data epochs.

If they do not, or if the epoch cannot be established without reading behavioral outcomes, UNORM-001 becomes R5/diagnostic-only and will not execute as fresh confirmation.

### SJSON-001 — ELIGIBLE

Repository:
serde-rs/json

Metadata inspected:
Git tag refs and release timestamps only.

Because all current releases are in the 1.0 line, use the presealed chronological fallback with at least 180 days between selected release epochs where practical.

Frozen regimes:

- A = serde_json v1.0.140, published 2025-03-03
- B = serde_json v1.0.145, published 2025-09-14
- C = serde_json v1.0.151, published 2026-07-20

No release-note body, changelog, commit message or behavioral result was read before regime sealing.

Fresh relation surface:
RFC/JSON-specification-derived packet to be frozen before execution.

## Research-lab candidates

### C3X-001 — CONTAMINATED / DIAGNOSTIC ONLY

Repository:
WhoSia/C3X

Permitted metadata screening exposed workflow filenames including:

- p21-hold-closure.yml
- p21-hold-diagnostic.yml

The preseal permits workflow-name inspection but separately declares verdict labels to be contaminating.

The literal HOLD label is outcome-bearing under that rule.

Therefore C3X loses fresh-confirmatory status before any result file or workflow body is opened.

No C3X outcome is read for fresh selection.

### CUBE-001 — STRUCTURALLY INELIGIBLE FOR A FRESH THREE-REGIME TRIANGLE

Repository:
WhoSia/CUBE-REV

Permitted metadata screening observed:
- research/0.7.12/
- research/registry/cumulative_registry.json
- one opaque release-snapshot directory
- validation/gate-status filenames inside research/0.7.12

No result JSON content, registry content, README content, commit message or quantitative value was read.

Under the presealed admission rule a RESEARCH_LAB triangle needs three regimes/stages to be frozen from outcome-independent metadata.

Only one explicit research stage identifier is visible without opening potentially outcome-bearing registry/result content.

Therefore CUBE-001 cannot form a fresh 4.34 three-regime triangle under the frozen screening rules.

Diagnostic-only structural context is allowed; fresh promotion credit is zero.

No third research lab may be added.

## Full-promotion ceiling before fresh behavior

Fresh RESEARCH_LAB admitted case count maximum:

0.

Fresh engineering repository candidates maximum:

3.

The full promotion rule requires:
- >= 6 fresh admitted external cases;
- >= 2 independently admitted RESEARCH_LAB cases.

Those conditions are already unreachable.

Therefore, before any fresh 4.34 behavioral reveal:

```text
RELATIONAL_SUPPORT_GEOMETRY_EXTERNAL_IDENTIFICATION = STRUCTURALLY_HOLD
POST_REVEAL_RESCUE = FORBIDDEN
```

This does not end the stage.

MQR-4.34 may still earn:
- prospective engineering relation receipts;
- forcing-world validation;
- independent compiler concordance;
- inherited TKN/TOML zero-credit separation;
- decoy-invariance results;
- relation-changing intervention sensitivity;
- a narrower operational-identifiability result;
- or a new proof that the relational representation remains insufficient.

## Verdict

REGEX-001=FRESH-ELIGIBLE /
UNORM-001=CONDITIONAL-METADATA-GATE /
SJSON-001=FRESH-ELIGIBLE /
C3X-001=CONTAMINATED-DIAGNOSTIC /
CUBE-001=THREE-REGIME-INELIGIBLE-DIAGNOSTIC /
FRESH-RESEARCH-LAB-N-MAX=0 /
FULL-EXTERNAL-PROMOTION=STRUCTURALLY-HOLD /
POST-REVEAL-REPLACEMENT=FORBIDDEN /
ENGINEERING-RELATIONAL-STRESS=CONTINUES.
