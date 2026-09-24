# MQR-4.33 — Inherited TKN Support-Classifier Calibration Receipt

Status: FROZEN CLASSIFIER MISMATCH / S1 DETERMINISTIC PREDICTION DEFEATED

Run:
36042235864

Trigger SHA:
aad8d1ffafd5b0c9df5497bbfcad8b053cfb23a2

Frozen mapping:
TKN-001 -> S1_GENERALIZATION_RISK

Historical observation:
COMPOSITION_PASS

Machine replay:

TRIANGLE=TKN-001-CAL
candidate=true
structural_valid=true
composition=COMPOSITION_PASS
prediction_match=false

FORCING_EXPECTATION_MISMATCHES=1
SUPPORT_DOMAIN_DISCOVERY=HOLD

## Interpretation

The 4.33 S1 classifier cannot be promoted as a deterministic rule:

domain_covered=false
does not imply
NONTRANSITIVITY_WITNESS.

TKN-001 and TOML-D1 now supply opposite outcomes inside the coarse coverage-risk family:

- TKN-001: uncovered/disjoint held-out surface, COMPOSITION_PASS;
- TOML-D1: uncovered specification-extension surface, diagnostic direct failure.

Therefore support coverage alone is not an identifying coordinate.

At least one further distinction is required, plausibly the relation between the bridge support and direct support:
- held-out sample from the same behavioral regime;
- strict domain/language extension;
- successor refinement;
- constitutive component change.

This successor distinction is not retrofitted into the frozen 4.33 classifier.

## Verdict

S1-RISK-INDICATOR=RETAINABLE /
S1-DETERMINISTIC-PREDICTOR=DEFEATED /
SUPPORT-CLASSIFIER=UNDERIDENTIFIED /
POSTHOC-RULE-REPAIR=FORBIDDEN /
SUPPORT_DOMAIN_DISCOVERY=HOLD.
