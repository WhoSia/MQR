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

Machine calibration is pending.

If the frozen S1 classifier returns prediction_match=false, S1 may remain only a risk indicator in 4.33; it cannot be promoted as a deterministic support-domain separator.

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
