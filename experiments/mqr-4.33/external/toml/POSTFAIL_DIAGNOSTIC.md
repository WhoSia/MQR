# MQR-4.33 TOML-D1 — Post-Failure Component-Adapter Diagnostic

Status: DIAGNOSTIC-ONLY / FRESH TOML-001 VERDICT IMMUTABLE

## Inherited fresh result

TOML-001 canonical adjacent bridge:

A = 0.8.23
B = 0.9.12+spec-1.1.0
C = 1.0.7+spec-1.1.0

Observed on the frozen `input.parse::<toml::Value>()` surface:

A vector = OK,OK,OK,OK,OK,OK
B vector = ERR,ERR,ERR,ERR,ERR,ERR
C vector = ERR,ERR,ERR,ERR,ERR,ERR

Therefore:

A -> B = TRANSPORT_FAIL
B -> C = TRANSPORT_PASS
COMPOSITION_CANDIDATE = NO
DIRECT = NOT_EXECUTED

This verdict cannot be repaired.

## Diagnostic question

Was the bridge failure caused by the frozen method-level parsing surface rather than the underlying TOML document grammar?

## Frozen repair adapter

Use exactly:

toml::from_str::<toml::Value>(input)

No other parser entry point may be tried in MQR-4.33.

Versions, B01..B06 and H01..H04 remain identical to TOML-001.

## Diagnostic execution

Because TOML-D1 is explicitly post-outcome and nonconfirmatory, bridge and held-out fixtures may be executed in the same diagnostic workflow.

Outputs remain only OK/ERR.

## Diagnostic interpretations

If repaired B01..B06 agree across A/B/C:
COMPONENT_ADAPTER_RECOVERY = PASS.

If they do not:
COMPONENT_ADAPTER_RECOVERY = FAIL.

If recovery passes and A/C held-out vectors differ:
DIAGNOSTIC_SUPPORT_BOUNDARY_WITNESS = YES.

This may illustrate the 4.33 S1 mechanism but cannot count as a fresh NONTRANSITIVITY_WITNESS because the adapter was selected after TOML-001 failed.

## Frozen mismatch minimizer

For any A/C held-out mismatch vector:

1. sort mismatching fixture IDs lexically;
2. attempt deletion from lowest ID upward;
3. retain a deletion whenever at least one mismatch remains;
4. stop when one mismatching fixture remains.

The remaining fixture is the deterministic 1-minimal diagnostic witness under the presealed deletion order.

## Verdict ceiling

TOML-D1 cannot:
- alter TOML-001;
- count toward fresh confirmatory N;
- satisfy external NONTRANSITIVITY promotion;
- rescue SUPPORT_DOMAIN_DISCOVERY.

It can localize component-identity drift and demonstrate a candidate support-boundary mechanism.

## Pre-diagnostic verdict

FRESH-TOML-001=IMMUTABLE-NO-CANDIDATE /
REPAIR-ADAPTER=TOML-FROM_STR /
POSTFAIL-DIAGNOSTIC=AUTHORIZED /
PROMOTION-CREDIT=ZERO.
