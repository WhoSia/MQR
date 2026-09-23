# MQR-4.20 — Cryptographic Non-Repudiation Boundary, Third-Party Timestamp Authority, Signed Preseal–Execution Binding, History-Rewrite Attack & Whether Governance Independence Survives Adversarial Provenance Tampering

Status: ACTIVE / PASS-NARROW

## Core result
A deterministic MQR evidence bundle was SHA-256 hashed, keylessly signed from GitHub Actions via Sigstore, entered into Rekor's append-only transparency log, publicly retrievable with inclusion proof, and verified successfully.

Canonical bundle SHA-256:
98f27bfe1f39cc131f07ba6e07a241d5d75ff6ae185e1a7dd3bb112132c5d9bc

Rekor:
- log index: 2922673972
- integratedTime: 1790180833
- UUID: 108e9186e8c5677af7c67858e1c250601e68b00a80194227dfcd2f25743608e54373cbdfac6f7cde
- log ID: c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d

Original verification:
Verified OK

## Adversarial rewrite
Attack commit:
38f434c4b1e8711f3fd7088e7c2bfbf29b3bcbce

Protected provenance rewritten:
- selected_frequency_hz 49.975 -> 49.994
- frequency_deviation_hz -0.025 -> -0.006

Attacked SHA-256:
6a6e4d7fae44a62f491fbacfba45b72a804133769ed2bdb50d313e7d011be567

Verification with canonical receipt:
invalid signature

Machine verdict:
ATTACK_DETECTED

## Adjudication
The MQR-4.19 governance-independence result survives the tested history/provenance tampering attack.

Scoped limits:
- Rekor is a signed append-only transparency-log notary, not a classical RFC3161 TSA.
- Sigstore identity is bound to the GitHub Actions OIDC workflow identity, not a persistent human-author private key.
- This is not an absolute guarantee against compromise of GitHub, Sigstore trust roots, or every possible provenance attack.

## Verdict
CRYPTOGRAPHIC-EVIDENCE-BUNDLE-FROZEN /
SHA256-BINDING-PASS /
SIGSTORE-KEYLESS-SIGNATURE-PASS /
REKOR-TRANSPARENCY-LOG-NOTARIZATION-PASS /
PUBLIC-MERKLE-INCLUSION-PROOF-PASS /
CANONICAL-VERIFY-PASS /
HISTORY-REWRITE-ATTACK-EXECUTED /
ATTACK-SIGNATURE-VERIFICATION-FAIL-AS-EXPECTED /
ATTACK-DETECTED /
GOVERNANCE-INDEPENDENCE-SURVIVES-TESTED-PROVENANCE-TAMPERING /
RFC3161-TSA-NOT-ESTABLISHED /
HUMAN-AUTHOR-LONG-TERM-KEY-NOT-ESTABLISHED /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
