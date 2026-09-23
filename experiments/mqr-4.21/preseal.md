# MQR-4.21 — Independent Timestamp Authority, Persistent Author-Key Attestation, Cross-Trust-Root Redundancy, Sigstore–TSA Concordance & Whether Governance Independence Survives Identity–Clock Authority Separation

Status: ACTIVE / PRESEAL

## Objective
Separate identity authority from clock authority and test concordance on one frozen MQR evidence object.

## Trust roots
I. Identity / signing-event axis
- GitHub Actions OIDC identity
- Fulcio short-lived signing certificate
- Sigstore signature transparency evidence

II. Clock axis
- RFC3161 signed timestamp from a trusted TSA
- TSA verification must not reduce to Rekor v1 integratedTime alone

III. Persistent author-key axis
- A persistent author-controlled signing key must exist across independent signing events and be verifiable by a stable public key fingerprint.
- GitHub Actions OIDC/Fulcio ephemeral keys do NOT satisfy this axis.

## Frozen evidence object
Reuse the MQR-4.20 canonical evidence bundle bytes without semantic change:
SHA-256 expected:
98f27bfe1f39cc131f07ba6e07a241d5d75ff6ae185e1a7dd3bb112132c5d9bc

## Acceptance
TSA PASS:
- an RFC3161 timestamp token is present or newly obtained;
- its signed time is cryptographically verified against the relevant signature/artifact;
- TSA certificate/root information is independently inspectable.

CROSS-ROOT CONCORDANCE PASS:
- Fulcio/identity signature verifies;
- RFC3161 timestamp verifies;
- both bind the same signing event/evidence object without contradiction.

PERSISTENT AUTHOR-KEY PASS:
- stable long-term public key fingerprint;
- at least two independently recorded signing events use the same author key;
- private key is not committed to the repository or exposed in logs/artifacts.

If no secure persistent author private-key custody is available, return HOLD for that axis. Never generate and publish an unprotected private key merely to obtain PASS.

## Promotion ceiling
Identity-clock separation may PASS even if persistent-author-key remains HOLD.
Full MQR-4.21 cross-root + persistent-author attestation requires all three axes.
