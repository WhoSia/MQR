# MQR-4.22 — Persistent Author-Key Custody Constitution, Non-Exportable Signing Authority, Two-Event Continuity Proof, Rotation/Compromise Recovery & Whether Author Continuity Can Be Added without Re-Centralizing Governance

Status: ACTIVE / PRESEAL

## Objective
Test whether a persistent author-signing authority can be added without collapsing the governance separation established in MQR-4.19–4.21.

## Required distinction
The following are NOT equivalent:
1. stable workflow/OIDC identity across runs;
2. stable author-controlled signing key across runs.

OIDC continuity alone is a negative control and may not be promoted to persistent-author-key continuity.

## Custody constitution
A qualifying author key must satisfy all of:
K1. persistent public-key fingerprint across >=2 independent signing events;
K2. private key is non-exportable or equivalently protected by an external KMS/HSM/hardware-token boundary;
K3. signing authorization is obtained through short-lived federated identity or explicit human presence, not a repository-stored long-lived private key;
K4. repository source, logs, caches and artifacts never contain private-key bytes;
K5. verification requires only public material plus independently auditable receipts.

## Governance anti-recentralization
Author-key continuity alone may attest authorship/continuity but may NOT:
- choose source/join/rival rules;
- override external veto;
- override TSA/provenance failure;
- unilaterally promote scientific authority.

Scientific promotion remains multi-key:
CONSTITUTIONAL AUTHORITY + EXECUTION RECEIPT + PROVENANCE/TIME AUTHORITY.
Author-key continuity is an additional attestation lane, not a super-key.

## Rotation / compromise recovery
Pre-frozen state machine:
ACTIVE(K_n)
 -> ROTATION_PENDING(K_n,K_{n+1})
 -> ACTIVE(K_{n+1})
or
ACTIVE(K_n)
 -> COMPROMISED(K_n)
 -> REVOKED(K_n)
 -> RECOVERY_PENDING
 -> ACTIVE(K_{n+1})

Rules:
R1. Rotation requires old-key authorization OR independent recovery authority.
R2. Compromise declaration immediately blocks K_n from future promotion receipts.
R3. Historical receipts signed before revocation remain historically attributable but cannot authorize new work.
R4. K_{n+1} must receive a new independent clock/provenance binding.
R5. No scientific claim may be promoted merely because a key rotated successfully.

## Two-event test
Event A and Event B must be independent workflow runs.
First run: measure stable OIDC principal and perform Sigstore keyless signature.
Second run: repeat on identical canonical evidence.
If OIDC subject is stable but public signing keys differ, record:
PRINCIPAL CONTINUITY PASS / KEY CONTINUITY FAIL.
This must not be laundered into persistent-author-key PASS.

## Positive realization gate
Persistent author-key PASS requires a provisioned external non-exportable KMS/HSM/hardware signing key available to this execution context.
If unavailable, HOLD.
