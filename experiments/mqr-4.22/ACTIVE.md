# MQR-4.22 — Persistent Author-Key Custody Constitution, Non-Exportable Signing Authority, Two-Event Continuity Proof, Rotation/Compromise Recovery & Whether Author Continuity Can Be Added without Re-Centralizing Governance

Status: ACTIVE / ARCHITECTURE PASS / PERSISTENT-KEY REALIZATION HOLD

## Two-event result
Event A:
- run 35962743497
- OIDC subject: repo:WhoSia@71053804/MQR@1370659163:ref:refs/heads/main
- SPKI SHA-256: 081ef8f6742f6c9707e169057a42574ce76c775a4121b271ccd9c82052bbe4a4

Event B:
- run 35962809856
- OIDC subject: repo:WhoSia@71053804/MQR@1370659163:ref:refs/heads/main
- SPKI SHA-256: 4766e3e7711a6642259ddbbcb5352edd1e1daa98e3c57a4781ceee37dc6f8ffc

Therefore:
PRINCIPAL CONTINUITY = PASS.
PERSISTENT KEY CONTINUITY = FAIL / NOT ESTABLISHED.

Keyless workflow identity was not laundered into persistent author-key continuity.

## Rotation / compromise recovery
Mechanical state-machine run:
35962896880

Result:
ROTATION_RECOVERY_GATE = PASS.
AUTHOR_KEY_SUPERKEY_ATTACK = BLOCKED.

Compromised K_n cannot authorize future promotion.
Recovery can activate K_{n+1} only through old-key authorization or independent recovery authority.

## Governance
Author continuity is restricted to authorship/continuity attestation.

It cannot override:
- constitutional authority;
- execution receipt;
- provenance/time authority.

Thus:
AUTHOR-CONTINUITY LANE WITHOUT SCIENTIFIC RECENTRALIZATION = ARCHITECTURE PASS.

## Persistent author-key boundary
No KMS/HSM/hardware-token or secure secret-management signing surface is provisioned in the current execution context.

No insecure private key was generated.

Therefore:
NON-EXPORTABLE AUTHOR KEY = NOT MATERIALIZED.
PERSISTENT AUTHOR-KEY POSITIVE REALIZATION = HOLD.

## Verdict
CUSTODY-CONSTITUTION-PASS /
TWO-EVENT-NEGATIVE-CONTROL-PASS /
OIDC-PRINCIPAL-CONTINUITY-PASS /
EPHEMERAL-KEY-DIVERGENCE-PASS /
KEYLESS-NOT-PERSISTENT-KEY /
ROTATION-RECOVERY-GATE-PASS /
COMPROMISE-REVOCATION-PASS /
AUTHOR-KEY-SUPERKEY-ATTACK-BLOCKED /
ANTI-RECENTRALIZATION-ARCHITECTURE-PASS /
NON-EXPORTABLE-AUTHOR-KEY-NOT-MATERIALIZED /
PERSISTENT-AUTHOR-KEY-POSITIVE-REALIZATION-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
