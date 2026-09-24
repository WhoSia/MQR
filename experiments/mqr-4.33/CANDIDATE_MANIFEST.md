# MQR-4.33 — Candidate and Contamination Manifest

Status: FROZEN BEFORE FRESH TOML BEHAVIOR EXECUTION

Preseal:
e11f55cff2d8754f862c9edab711ae15539bc4c8

## Fresh confirmatory eligibility

### TOML-001 — ELIGIBLE

Repository:
toml-rs/toml

Lineage:
ENGINEERING_DEVELOPMENT

Version selection rule applied:
latest stable patch from each of the latest three **completed** stable minor lines.

The current 1.1 line is treated as active and therefore not a completed line.

Frozen regimes:
- A = toml 0.8.23
- B = toml 0.9.12+spec-1.1.0
- C = toml 1.0.7+spec-1.1.0

Eligibility evidence inspected before this manifest:
release/version metadata only.

No TOML behavioral result has been executed or read for A/B/C under the MQR-4.33 probe.

Structural class before direct reveal:
S1 GENERALIZATION_RISK.

Reason:
A is from the final 0.8 line while B/C explicitly carry TOML-spec-1.1.0 lineage metadata. The fresh probe will separate a common-subset bridge surface from a predeclared held-out boundary surface. This classification does not assume the actual parser result.

Frozen prediction:
if adjacent common-subset bridges pass, the held-out boundary surface is predicted to exert NONTRANSITIVITY_WITNESS pressure.

The exact fixtures are frozen separately before any execution.

### URL-001 — DISQUALIFIED_FROM_FRESH_CONFIRMATION

Repository:
servo/rust-url

Reason:
before an exact version triple was written to the 4.33 manifest, release-note/changelog text became visible during metadata retrieval, including behavior-relevant URL/IDNA/path-normalization changes.

This violates the presealed screening order.

Consequences:
- may be used later only as diagnostic/prior-art engineering context;
- may not count toward fresh confirmatory N;
- may not satisfy S0/S1/S2 promotion requirements.

No replacement engineering repository may be added.

### SEMVER-001 — DISQUALIFIED_FROM_FRESH_CONFIRMATION

Repository:
dtolnay/semver

Reason:
release-note/changelog text became visible before a mechanically selected version triple was sealed.

Even though the exposed notes were mostly dependency/documentation oriented, the preseal forbids changelog inspection categorically before version sealing.

Consequences:
diagnostic only; no fresh-confirmatory count.

No replacement engineering repository may be added.

## Research-lab lane

### EPISTEME-001 — DISQUALIFIED_FROM_FRESH_CONFIRMATION

Repository:
WhoSia/EPISTEME

Lineage:
RESEARCH_LAB

Eligibility inspection exposed outcome-bearing commit messages before the three-stage regime triple and structural support class were frozen.

Examples of exposed outcome-bearing metadata include stage messages describing:
- replication failure;
- instance-law defeat.

The contents of result JSON files were not opened, but commit-message outcome exposure is sufficient to violate the presealed screening order.

Consequences:
- EPISTEME may be used only as diagnostic structural context in 4.33;
- it cannot count as fresh RESEARCH_LAB confirmation;
- no alternate research lab may be added after this contamination.

Fresh independently admitted RESEARCH_LAB triangle count is therefore frozen at a maximum of 0 for MQR-4.33.

This alone makes SUPPORT_DOMAIN_DISCOVERED impossible under the presealed promotion rule.

The stage continues because minimal counterexamples, path-divergence constructions, external engineering evidence and research-measurement diagnostics remain scientifically informative.

## Research-measurement diagnostic

CODATA-DIAG remains eligible as a diagnostic lane under the original preseal.

It cannot satisfy RESEARCH_LAB confirmation.

Frozen sources:
official NIST/CODATA 2010, 2014, 2018, 2022 recommended-value releases.

Frozen constants:
G, alpha, m_e, m_p, R_inf, mu_0.

Frozen relation:
z(i,j)=|x_i-x_j|/sqrt(u_i^2+u_j^2)

TRANSPORT_PASS iff z<=1.

## Promotion consequence before any fresh direct result

Because fresh RESEARCH_LAB confirmatory N can no longer reach 2:

SUPPORT_DOMAIN_DISCOVERY = STRUCTURALLY_HOLD.

This is a pre-outcome ceiling, not a conclusion from TOML/CODATA behavior.

4.33 may still earn:
- EXTERNAL_NONTRANSITIVITY_WITNESS;
- EXTERNAL_PATH_DIVERGENT_PASS;
- MINIMAL_WITNESS;
- SUPPORT_DOMAIN_CANDIDATE;
- or SUPPORT_CLASSIFIER_FALSIFICATION.

## Verdict

TOML-001=FRESH-ELIGIBLE /
URL-001=CONTAMINATED-DIAGNOSTIC /
SEMVER-001=CONTAMINATED-DIAGNOSTIC /
EPISTEME-001=CONTAMINATED-DIAGNOSTIC /
FRESH-RESEARCH-LAB-N=0-MAX /
POST-REVEAL-REPLACEMENT=FORBIDDEN /
SUPPORT_DOMAIN_DISCOVERY=STRUCTURALLY-HOLD /
COUNTEREXAMPLE-SEARCH=CONTINUES.
