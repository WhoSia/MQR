# MQR-4.21 — Identity–Clock Separation & Persistent-Author-Key Receipt

Status: IDENTITY-CLOCK SEPARATION PASS / PERSISTENT AUTHOR-KEY HOLD

## Inherited canonical evidence
MQR-4.20 evidence bundle SHA-256:
98f27bfe1f39cc131f07ba6e07a241d5d75ff6ae185e1a7dd3bb112132c5d9bc

## Preseal
Commit:
58fcfc5b5d1f5e1336e95261178dd641c58c97f4

Frozen rule:
- identity/signing-event authority and clock authority must be separated;
- persistent author-key requires stable public fingerprint across multiple signing events;
- private key may not be exposed in repository, logs, or artifacts.

## Identity root
GitHub Actions OIDC + Fulcio / Sigstore keyless signing.

Cross-root run:
35891478701

Job:
107284743417

Workflow:
.github/workflows/mqr-4.21-cross-root.yml

Canonical evidence signing:
PASS

Cosign verification:
Verified OK

Rekor tlog index:
2922947600

Raw Sigstore signature SHA-256:
ea254f3c77c0ae02b32bd9ce4a9b75bb1f4fcce506bd2d7c32b3182c3c2eb233

## Independent clock root
Independent RFC3161 TSA operator:
DigiCert

Endpoint used:
http://timestamp.digicert.com

Timestamp input:
raw Sigstore signature bytes

Thus the TSA countersigns the signing event rather than merely timestamping an unrelated artifact.

RFC3161 response status:
Granted

Policy OID:
2.16.840.1.114412.7.1

Hash algorithm:
sha256

Message imprint:
ea254f3c77c0ae02b32bd9ce4a9b75bb1f4fcce506bd2d7c32b3182c3c2eb233

Serial:
0x11419293E32110571FFA631D235591CD

Timestamp:
2026-09-23T16:50:15Z

Nonce:
0xBB611FF3C45E0558

OpenSSL RFC3161 verification:
Verification: OK

## Cross-root concordance
The Sigstore signature hash independently computed before TSA request exactly equals the RFC3161 message imprint:
ea254f3c77c0ae02b32bd9ce4a9b75bb1f4fcce506bd2d7c32b3182c3c2eb233

Therefore:
IDENTITY ROOT -> same signing event -> CLOCK ROOT

FULCIO/OIDC SIGNATURE VERIFICATION = PASS
DIGICERT RFC3161 TOKEN VERIFICATION = PASS
SIGNATURE-IMPRINT CONCORDANCE = PASS
IDENTITY–CLOCK AUTHORITY SEPARATION = PASS
CROSS-TRUST-ROOT REDUNDANCY = PASS-NARROW

## Persistent author-key audit
Repository audit found no existing persistent author signing key material.

More importantly, no secure private-key custody channel is available in this execution context that would:
- keep the private key secret;
- preserve it across independent signing events;
- allow two future signatures with the same author-controlled key;
- expose only a stable public fingerprint.

Generating a private key and placing it in GitHub source, logs, or workflow artifacts would violate the frozen MQR-4.21 contract.

Therefore:
PERSISTENT AUTHOR-KEY = HOLD / NOT ESTABLISHED.

This is not evidence against persistent author-key attestation as a method. It is a refusal to fabricate secure custody.

## Governance conclusion
The MQR-4.19/4.20 governance-independence result survives explicit separation of identity authority from clock authority.

This is stronger than Rekor-integratedTime-only evidence because the RFC3161 clock assertion is signed under a separate DigiCert TSA trust chain.

However:
FULL MQR-4.21 ALL-AXIS CLOSURE = HOLD
because persistent author-key continuity is not established.

## Verdict
CANONICAL-EVIDENCE-DIGEST-STABLE /
SIGSTORE-IDENTITY-SIGNATURE-PASS /
FULCIO-OIDC-IDENTITY-ROOT-PASS /
DIGICERT-RFC3161-TSA-PASS /
RFC3161-STATUS-GRANTED /
RFC3161-VERIFY-PASS /
SIGNATURE-IMPRINT-EXACT-MATCH /
IDENTITY-CLOCK-AUTHORITY-SEPARATION-PASS /
CROSS-TRUST-ROOT-CONCORDANCE-PASS /
GOVERNANCE-INDEPENDENCE-SURVIVES-IDENTITY-CLOCK-SEPARATION /
PERSISTENT-AUTHOR-KEY-NOT-ESTABLISHED /
INSECURE-PRIVATE-KEY-MATERIALIZATION-REFUSED /
FULL-4.21-ALL-AXIS-CLOSURE-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
