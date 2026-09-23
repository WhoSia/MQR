# MQR-4.20 — Cryptographic Non-Repudiation Boundary

Status: ACTIVE / PRESEAL

## Objective
Test whether the MQR-4.19 governance-independence result survives adversarial provenance tampering.

## Frozen evidence object
Canonical object to protect:
- MQR-4.19 public-audit manifest
- MQR-4.19 KEY B verification receipt
- inherited MQR-4.17 external rule seal
- inherited MQR-4.18 KEY A execution receipt

## Cryptographic boundary
A third-party timestamp authority must bind a cryptographic digest of a frozen evidence bundle before any adversarial rewrite test is performed.

Acceptance requires:
1. deterministic bundle bytes;
2. SHA-256 digest recorded in GitHub before attack;
3. independent third-party timestamp/notary receipt binding that digest;
4. adversarial rewrite performed only on a disposable attack branch, never canonical main;
5. rewritten branch changes at least one protected provenance fact while retaining superficially plausible prose;
6. verification detects that rewritten content no longer matches the pre-attack digest/notary receipt.

## Attack model
Allowed attack:
- create disposable branch from current main;
- mutate protected provenance content or chronology representation;
- attempt to preserve narrative plausibility.

Forbidden:
- force rewrite canonical main;
- delete third-party receipts;
- alter frozen acceptance criteria after attack.

## Promotion rule
PASS only if:
- third-party timestamp/notary receipt is independently verifiable;
- canonical bundle verifies against frozen digest;
- adversarial branch fails verification;
- MQR-4.19 dual-key result remains reconstructible from canonical history.

If third-party cryptographic timestamping cannot be obtained, return HOLD rather than treating GitHub timestamps alone as cryptographic non-repudiation.
