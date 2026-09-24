# MQR-4.33 TOML-D1 — Post-Failure Diagnostic Receipt

Status: COMPONENT ADAPTER RECOVERED / DIAGNOSTIC SUPPORT-BOUNDARY WITNESS / ZERO PROMOTION CREDIT

Canonical diagnostic run:
36042021948

Trigger SHA:
6bedb2890bc1138e7ced8b168f0c0f73204ef56b

## Frozen repair adapter

toml::from_str::<toml::Value>(input)

## Bridge recovery

A = toml 0.8.23:
B01..B06 = OK,OK,OK,OK,OK,OK

C = toml 1.0.7+spec-1.1.0:
B01..B06 = OK,OK,OK,OK,OK,OK

Workflow adjudication:
COMPONENT_ADAPTER_RECOVERY=PASS

Therefore the fresh TOML-001 bridge failure is localized to the originally frozen method-level parsing surface rather than to the six common TOML documents themselves.

This does not repair TOML-001.

## Held-out diagnostic boundary

A:
H01..H04 = ERR,ERR,ERR,ERR

C:
H01..H04 = OK,OK,OK,OK

Workflow adjudication:
DIAGNOSTIC_SUPPORT_BOUNDARY_WITNESS=YES

## Frozen lexical minimization

Initial mismatch set:
H01,H02,H03,H04

Delete H01:
mismatch survives.

Delete H02:
mismatch survives.

Delete H03:
mismatch survives.

Remaining deterministic 1-minimal witness:
H04

H04:
local time with omitted seconds.

The diagnostic relation therefore has a single-fixture witness under the presealed deletion order.

## Interpretation

TOML-D1 demonstrates two different boundaries:

1. component-adapter identity must be earned before a composition triangle is even admitted;
2. after a common parser adapter is restored, the older/newer regimes separate on the predeclared TOML-1.1 boundary family.

Because the adapter was selected only after TOML-001 failed, this result is diagnostic only.

It cannot count as a fresh NONTRANSITIVITY_WITNESS.

## Artifact custody

A artifact:
10826434720
digest sha256:2d4bd775dc969eb98f88f72cdc351b976b0ceb6035c37b35df72c9009eeef018

C artifact:
10827375174
digest sha256:ace47855747b65daefbd20ffc1957a5848a135b5c293e181d8e2f74d0c6af48c

Adjudication artifact:
10826847585
digest sha256:466e29b8ee9150cf9d35e1dba2b8ce1c3ba4790169170a4929cc9012e317428d

## Verdict

FRESH-TOML-001=IMMUTABLE-NO-CANDIDATE /
COMPONENT-ADAPTER-RECOVERY=PASS /
DIAGNOSTIC-SUPPORT-BOUNDARY-WITNESS=YES /
MINIMAL-WITNESS=H04 /
PROMOTION-CREDIT=ZERO.
