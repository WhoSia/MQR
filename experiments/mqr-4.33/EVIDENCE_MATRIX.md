# MQR-4.33 — Support-Domain Evidence Matrix

Status: LIVE EVIDENCE INDEX / NO RULE CHANGES

## Diagnostic forcing worlds

| ID | Lineage | Frozen class | Observed | Role |
|---|---|---|---|---|
| F0 | SYNTHETIC | S0 STRICT_SUPPORT | COMPOSITION_PASS | positive control |
| F1 | SYNTHETIC | S1 GENERALIZATION_RISK | NONTRANSITIVITY_WITNESS | coverage counterexample control |
| F2 | SYNTHETIC | S2 PATH_RISK | PATH_DIVERGENT_PASS | order/loss control |
| F3 | SYNTHETIC | S2 PATH_RISK | COMPOSITION_SPLIT_REQUIRED | lossy-refinement control |

Canonical forcing run:
36041061957

All frozen diagnostic expectations matched.

## Fresh engineering lane

### TOML-001

Regimes:
- A = toml 0.8.23
- B = toml 0.9.12+spec-1.1.0
- C = toml 1.0.7+spec-1.1.0

Pre-execution structural map:
S1 GENERALIZATION_RISK.

Frozen bridge:
B01..B06 common TOML-1.0-style documents.

Observed:
- A bridge vector = OK,OK,OK,OK,OK,OK
- B bridge vector = ERR,ERR,ERR,ERR,ERR,ERR
- C bridge vector = ERR,ERR,ERR,ERR,ERR,ERR
- A -> B = TRANSPORT_FAIL
- B -> C = TRANSPORT_PASS

Therefore:
COMPOSITION_CANDIDATE = NO.

Direct H01..H04 remains unopened in the fresh lane.

Interpretation:
the prospective assumption that the chosen method-level parse surface represented the same component across A/B/C was defeated before composition could be tested.

This is not a NONTRANSITIVITY_WITNESS.
It is an earlier admission failure:

COMPONENT_IDENTITY_ASSUMPTION_DEFEATED.

Canonical fresh run:
36041355002.

Canonical receipt:
receipts/mqr-4.33/toml-bridge.tsv.

## Research-measurement diagnostic

CODATA-DIAG uses the frozen naive agreement relation:

z(i,j) = |x_i-x_j| / sqrt(u_i^2+u_j^2)

PASS iff z <= 1.

The diagnostic corpus contains twelve rolling constant triangles:
six constants × two rolling three-release windows.

Observed composition candidates:
- G, 2010 -> 2014 -> 2018: PASS / PASS / direct PASS
- G, 2014 -> 2018 -> 2022: PASS / PASS / direct PASS

All other frozen constant/windows lack two adjacent PASS edges.

Therefore:
- CODATA COMPOSITION_PASS diagnostics = 2
- CODATA NONTRANSITIVITY_WITNESS diagnostics = 0

Independent Rust recomputation:
- run 36098164402
- 12 triangles recomputed
- composition candidates = 2
- candidate direct PASS = 2
- candidate direct FAIL = 0
- committed z-results byte-match the recomputation

This lane has zero RESEARCH_LAB promotion credit because the adjustments are not independent direct experimental routes and the frozen z relation ignores cross-adjustment covariance.

## Contaminated/excluded fresh candidates

URL-001:
diagnostic only due pre-triple behavior-bearing release-note exposure.

SEMVER-001:
diagnostic only due pre-triple changelog exposure.

EPISTEME-001:
diagnostic only due pre-triple outcome-bearing commit-message exposure.

No replacements are allowed under the 4.33 preseal.

## Inherited calibration

TKN-001 from MQR-4.32 is mapped retrospectively under the frozen S0-S3 classifier.

Structural mapping:
S1 GENERALIZATION_RISK because bridge and direct fixture surfaces were disjoint.

Historical result:
COMPOSITION_PASS.

Machine calibration completed.

Canonical calibration run:
36042235864.

Observed:
- TKN-001-CAL composition = COMPOSITION_PASS;
- prediction_match = false;
- FORCING_EXPECTATION_MISMATCHES = 1.

Therefore:
S1_GENERALIZATION_RISK is not a deterministic NONTRANSITIVITY separator.

It may remain only a risk/pressure indicator in 4.33.

## Promotion ceiling

Fresh independently admitted RESEARCH_LAB count is structurally 0.

Therefore:

SUPPORT_DOMAIN_DISCOVERY = HOLD

regardless of any remaining diagnostic outcome.

The remaining question is whether 4.33 earns:
- a useful risk taxonomy;
- a component-identity admission lesson;
- a post-failure diagnostic support-boundary witness;
- or a direct falsification of its own S1 predictor.


## Frozen support-profile collision

TKN-001 and TOML-D1 share the exact frozen six-coordinate support profile:

```text
(component_identity,
 direct_independent,
 domain_covered,
 information_preserved,
 state_reset,
 adapter_commutative)

= (1,1,0,1,1,1)
```

But their observed outcomes differ:
- TKN-001 = COMPOSITION_PASS
- TOML-D1 = NONTRANSITIVITY_WITNESS at the postfail diagnostic adapter surface

Canonical collision run:
36098297037.

Machine certificate:
```text
PROFILE_COLLISION_COUNT=1
SUPPORT_PROFILE_IDENTIFIABILITY=FAIL
OUTCOME_FACTORIZATION_THROUGH_FROZEN_PROFILE=FAIL
FROZEN_SUPPORT_QUOTIENT_SUFFICIENCY=FAIL
```

Therefore no deterministic function of the frozen six-coordinate profile alone can reproduce both observed outcomes.

This is an exact representational-insufficiency result on the observed pair.

It does not identify the missing coordinate and does not promote TOML-D1 to fresh confirmation.

## Integrated closure

Canonical closure run:
36098340499.

All of the following passed in one current-head replay:
- formatting;
- Clippy with warnings denied;
- unit tests;
- release build;
- F0-F3 forcing-world expectations;
- inherited TKN classifier-defeat replay;
- support-profile collision/factorization certificate;
- CODATA recomputation;
- fresh TOML admission-defeat receipt;
- H04 minimal diagnostic witness receipt;
- structural promotion ceiling.

Closure summary:
```text
MQR433_COUNTEREXAMPLE_FIRST=PASS
MQR433_EXTERNAL_FRESH_NONTRANSITIVITY=NOT_EARNED
MQR433_DIAGNOSTIC_NONTRANSITIVITY=MINIMAL_H04
MQR433_CLASSIFIER_SELF_FALSIFICATION=PASS
MQR433_FROZEN_SUPPORT_QUOTIENT_IDENTIFIABILITY=FAIL
MQR433_STRONGEST_EARNED_RESULT=SUPPORT_REPRESENTATION_INSUFFICIENT
MQR433_SUPPORT_DOMAIN_DISCOVERY=HOLD
```
