# MQR-4.20 — Cryptographic Provenance Receipt

Status: TAMPER-DETECTION PASS / REKOR NOTARIZATION PASS-NARROW

## Preseal
Protocol commit:
5c7c72f5a66d3304ed03f330903f4b22ae318995

## Frozen evidence bundle
Bundle commit:
bf582eccde3275e271f8d234d710d4fed4e78337

SHA-256:
98f27bfe1f39cc131f07ba6e07a241d5d75ff6ae185e1a7dd3bb112132c5d9bc

## Sigstore / Rekor notarization
GitHub Actions run:
35888832342

Workflow identity:
https://github.com/WhoSia/MQR/.github/workflows/mqr-4.20-sigstore.yml@refs/heads/main

OIDC issuer:
https://token.actions.githubusercontent.com

Original cosign verification:
Verified OK

Rekor log index:
2922673972

Rekor integratedTime:
1790180833

Rekor UUID:
108e9186e8c5677af7c67858e1c250601e68b00a80194227dfcd2f25743608e54373cbdfac6f7cde

Rekor log ID:
c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d

Independent public Rekor retrieval returned:
- the same SHA-256 digest;
- signed entry timestamp;
- log index;
- integrated time;
- Merkle inclusion proof.

## Adversarial history-rewrite attack
Disposable attack branch:
mqr-4.20-history-rewrite-attack

Attack commit:
38f434c4b1e8711f3fd7088e7c2bfbf29b3bcbce

Protected facts rewritten:
selected_frequency_hz: 49.975 -> 49.994
frequency_deviation_hz: -0.025 -> -0.006

Attacked bundle SHA-256:
6a6e4d7fae44a62f491fbacfba45b72a804133769ed2bdb50d313e7d011be567

Attack verification run:
35888981473

Original canonical bundle:
Verified OK

Attacked bundle checked against canonical Sigstore/Rekor receipt:
invalid signature when validating ASN.1 encoded signature

Machine receipt:
ATTACK_DETECTED

## Adjudication
CANONICAL-DIGEST-BINDING = PASS.
THIRD-PARTY-TRANSPARENCY-LOG-NOTARIZATION = PASS.
PUBLIC-INCLUSION-PROOF = PASS.
CANONICAL-VERIFY = PASS.
ADVERSARIAL-REWRITE-DETECTED = PASS.
CANONICAL-MAIN-UNMODIFIED-BY-ATTACK = PASS.

Therefore:
MQR-4.19 governance-independence result survives this adversarial provenance-tampering attack.

## Scope limits
1. Rekor is an append-only signed transparency log, not a classical RFC3161 timestamp authority.
2. The Sigstore certificate binds the artifact to the GitHub Actions workflow OIDC identity, not directly to a human author's long-term private key.
3. This stage demonstrates non-repudiation/tamper resistance for the signed evidence object and workflow identity under the tested attack model; it is not an absolute guarantee against compromise of GitHub, Sigstore roots, or all possible provenance attacks.

## Verdict
CRYPTOGRAPHIC-EVIDENCE-BUNDLE-FROZEN /
SHA256-BINDING-PASS /
SIGSTORE-KEYLESS-SIGNATURE-PASS /
REKOR-TRANSPARENCY-LOG-NOTARIZATION-PASS /
PUBLIC-MERKLE-INCLUSION-PROOF-PASS /
CANONICAL-VERIFY-PASS /
HISTORY-REWRITE-ATTACK-EXECUTED /
ATTACK-DIGEST-DIVERGENCE-PASS /
ATTACK-SIGNATURE-VERIFICATION-FAIL-AS-EXPECTED /
ATTACK-DETECTED /
CANONICAL-MAIN-PRESERVED /
GOVERNANCE-INDEPENDENCE-SURVIVES-TESTED-PROVENANCE-TAMPERING /
RFC3161-TSA-NOT-ESTABLISHED /
HUMAN-AUTHOR-LONG-TERM-KEY-NOT-ESTABLISHED /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
