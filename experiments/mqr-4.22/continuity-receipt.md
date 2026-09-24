# MQR-4.22 — Persistent Author-Key Custody & Continuity Receipt

Status: CUSTODY CONSTITUTION PASS / NON-EXPORTABLE KEY NOT MATERIALIZED / PRINCIPAL CONTINUITY PASS / KEY CONTINUITY FAIL / ANTI-RECENTRALIZATION PASS

## Preseal
Commit:
748b00f72470afb4bb9f264393b52af2c2f7c900

Frozen distinctions:
- stable OIDC principal != stable author-controlled signing key;
- OIDC continuity may not be promoted to persistent-author-key continuity;
- author key is an attestation lane, never a scientific promotion super-key.

## Current secure-custody capability audit
Current execution/tool surface exposes no KMS, HSM, hardware-token, or secret-management action capable of:
- creating or referencing a non-exportable persistent author private key;
- preserving it across independent runs;
- allowing this execution context to sign without exposing private-key bytes.

Repository audit also found no existing persistent author signing-key material.

Therefore:
NON-EXPORTABLE AUTHOR SIGNING AUTHORITY = NOT MATERIALIZED.

No local private key was generated and committed.
No private key was written to workflow logs, caches, repository files, or artifacts.

## Two-event continuity negative control
Workflow:
.github/workflows/mqr-4.22-continuity.yml

### Event A
Run:
35962743497

Commit:
4b889fd4e78993d0a37ffe532c8e4cdfa9615cc7

OIDC subject:
repo:WhoSia@71053804/MQR@1370659163:ref:refs/heads/main

Job workflow ref:
WhoSia/MQR/.github/workflows/mqr-4.22-continuity.yml@refs/heads/main

SPKI SHA-256:
081ef8f6742f6c9707e169057a42574ce76c775a4121b271ccd9c82052bbe4a4

### Event B
Run:
35962809856

Commit:
2312dafccca8898db412e20c470de42e96449f7b

OIDC subject:
repo:WhoSia@71053804/MQR@1370659163:ref:refs/heads/main

Job workflow ref:
WhoSia/MQR/.github/workflows/mqr-4.22-continuity.yml@refs/heads/main

SPKI SHA-256:
4766e3e7711a6642259ddbbcb5352edd1e1daa98e3c57a4781ceee37dc6f8ffc

## Continuity adjudication
OIDC subject A == OIDC subject B:
PASS.

Workflow identity A == workflow identity B:
PASS.

SPKI(A) == SPKI(B):
FAIL.

Therefore:
PRINCIPAL CONTINUITY = PASS.
EPHEMERAL-KEY ROTATION = OBSERVED.
PERSISTENT AUTHOR-KEY CONTINUITY = FAIL / NOT ESTABLISHED.

This experimentally confirms that keyless workflow identity continuity cannot be substituted for persistent author-key continuity.

## Rotation / compromise recovery gate
Workflow:
.github/workflows/mqr-4.22-rotation-recovery.yml

Run:
35962896880

Commit:
79179f8924fbdfb6ba29dd00865d0c994ae46bc3

Mechanical tests:
- rotation_with_old_key = PASS
- rotation_with_recovery = PASS
- rotation_without_authority_blocked = PASS
- author_key_cannot_override_constitution_fail = PASS
- author_key_cannot_override_execution_fail = PASS
- author_key_cannot_override_provenance_fail = PASS
- promotion_without_author_key_still_scientifically_valid = PASS
- compromised_k1_future_authorization_blocked = PASS
- recovery_reaches_active_k2 = PASS

Machine verdict:
ROTATION_RECOVERY_GATE = PASS
AUTHOR_KEY_SUPERKEY_ATTACK = BLOCKED

## Recovery semantics
Frozen state machine:
ACTIVE(K_n)
 -> ROTATION_PENDING(K_n,K_{n+1})
 -> ACTIVE(K_{n+1})

or:
ACTIVE(K_n)
 -> COMPROMISED(K_n)
 -> REVOKED(K_n)
 -> RECOVERY_PENDING
 -> ACTIVE(K_{n+1})

A compromised K_n cannot authorize future promotion.
Historical pre-revocation receipts remain historically attributable but cannot authorize new work.

## Anti-recentralization result
Scientific promotion remains dependent on:
CONSTITUTIONAL AUTHORITY
AND EXECUTION RECEIPT
AND PROVENANCE/TIME AUTHORITY.

The author-continuity key is deliberately excluded from unilateral promotion power.

Therefore the tested governance architecture permits an author-continuity lane without re-centralizing scientific authority into the author key.

This is an ARCHITECTURE PASS, not a positive persistent-key realization.

## Positive realization boundary
Sigstore supports external KMS and hardware-token signing in principle, and GitHub Actions OIDC can federate to external cloud providers without repository-stored long-lived credentials.

However no such KMS/HSM/hardware key is provisioned and accessible in the current execution context.

Therefore:
PERSISTENT AUTHOR-KEY POSITIVE REALIZATION = HOLD.

## External adversarial review
An external fact-check surface returned TRUE with 86% confidence for the non-recentralization architecture, but its cited evidence set included weak/off-topic sources.
It is therefore recorded as diagnostic only and is NOT used to support the scientific verdict.

## Verdict
PERSISTENT-AUTHOR-KEY-CUSTODY-CONSTITUTION-PASS /
TWO-INDEPENDENT-EVENTS-EXECUTED /
OIDC-PRINCIPAL-CONTINUITY-PASS /
EPHEMERAL-SPKI-DIVERGENCE-CONFIRMED /
KEYLESS-IDENTITY-NOT-LAUNDERED-AS-PERSISTENT-KEY /
NON-EXPORTABLE-AUTHOR-KEY-NOT-MATERIALIZED /
INSECURE-PRIVATE-KEY-CREATION-REFUSED /
ROTATION-STATE-MACHINE-PASS /
COMPROMISE-REVOCATION-PASS /
INDEPENDENT-RECOVERY-PATH-PASS /
AUTHOR-KEY-SUPERKEY-ATTACK-BLOCKED /
ANTI-RECENTRALIZATION-ARCHITECTURE-PASS /
AUTHOR-CONTINUITY-CAN-BE-ADDED-WITHOUT-SCIENTIFIC-SUPERKEY-CONDITIONAL-PASS /
PERSISTENT-AUTHOR-KEY-POSITIVE-REALIZATION-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
