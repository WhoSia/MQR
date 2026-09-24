# MQR-4.23 — Persistent-Authorship Necessity Attack Receipt

Status: SCIENTIFIC-AUTHORITY DELTA = 0 / ATTRIBUTION DELTA = 1

## Preseal
Commit:
36fea64e32bdcd4f8d892529bc64d0444a6e0fe1

Frozen authority split:
- attribution authority: identity, continuity, accountability, archival linkage;
- epistemic authority: whether a scientific claim satisfies the MQR promotion constitution.

## Missing-key counterfactual
Workflow:
.github/workflows/mqr-4.23-missing-key.yml

Run:
35963206996

Commit:
91b6ecdca11e484e04860b962d8e5cc7048b657e

Frozen promotion law:
PROMOTE := C AND E AND P

K denotes persistent-author-continuity attestation.

World K+:
C=PASS, E=PASS, P=PASS, K=present
=> PROMOTE

World K-:
C=PASS, E=PASS, P=PASS, K=absent
=> PROMOTE

Therefore:
SCIENTIFIC_AUTHORITY_DELTA(K+ - K-) = 0.

Attribution continuity differs:
ATTRIBUTION_CONTINUITY_DELTA = 1.

## Failure rescue attacks
C FAIL + K present:
HOLD.

E FAIL + K present:
HOLD.

P FAIL + K present:
HOLD.

Thus author continuity cannot rescue:
- constitutional failure;
- execution failure;
- provenance/time failure.

Missing K also does not create false promotion when C/E/P fail.

Machine receipts:
missing_key_counterfactual_invariant = PASS
author_key_cannot_rescue_constitution = PASS
author_key_cannot_rescue_execution = PASS
author_key_cannot_rescue_provenance = PASS
missing_key_does_not_create_false_promotion = PASS
SCIENTIFIC_AUTHORITY_DELTA_K_PLUS_MINUS_K_MINUS = 0
ATTRIBUTION_CONTINUITY_DELTA = 1
MISSING_KEY_COUNTERFACTUAL = PASS

## Keyless-principal equivalence
MQR-4.22 already established:
- OIDC principal continuity = PASS;
- persistent signing-key continuity = NOT ESTABLISHED.

MQR-4.23 therefore uses keyless principal continuity only as an attribution comparator.
It is not treated as cryptographic equivalence to persistent authorship.

Because scientific promotion is invariant under both:
- persistent-author attestation present/absent; and
- keyless-principal continuity vs no persistent key,
no scientific-authority gain is identified from the authorship lane under the current contract.

## Necessity adjudication
N1:
Removing author continuity does not make the otherwise identical claim non-identifiable or non-auditable because constitution, execution and provenance/time receipts remain independently available.
NOT ESTABLISHED.

N2:
Removing author continuity does not invalidate C/E/P.
NOT ESTABLISHED.

N3:
No independently credible non-attribution scientific failure caused specifically by missing persistent authorship was established.
NOT ESTABLISHED.

Therefore:
PERSISTENT AUTHORSHIP IS NOT EPISTEMICALLY NECESSARY under the present MQR Generation-IV authority constitution.

## Literature cross-check
Current ICMJE authorship guidance treats authorship as conferring credit and responsibility/accountability.
ICMJE editorial-integrity guidance separately says editorial decisions should turn on originality, quality and contribution to evidence, not personal relationships or agendas.

This literature cross-check is consistent with, but does not itself prove, the MQR attribution/epistemic separation.

Consensus academic-search connector was attempted but monthly quota was exhausted.
No result from that failed search was used.

## Interpretation
Persistent author continuity may still add:
- accountability;
- provenance linkage;
- attribution continuity;
- compromise/rotation traceability.

But under this contract it contributes no additional scientific promotion authority once C/E/P are already satisfied.

Thus:
AUTHORSHIP VALUE != SCIENTIFIC AUTHORITY VALUE.

This is a scoped necessity result.
It does not claim that authorship is socially or legally unimportant.

## Verdict
PERSISTENT-AUTHORSHIP-NECESSITY-ATTACK-PASS /
MISSING-KEY-COUNTERFACTUAL-PASS /
K-PLUS-PROMOTE /
K-MINUS-PROMOTE /
SCIENTIFIC-AUTHORITY-DELTA-ZERO /
ATTRIBUTION-CONTINUITY-DELTA-ONE /
AUTHOR-KEY-CANNOT-RESCUE-CONSTITUTION-FAILURE /
AUTHOR-KEY-CANNOT-RESCUE-EXECUTION-FAILURE /
AUTHOR-KEY-CANNOT-RESCUE-PROVENANCE-FAILURE /
KEYLESS-PRINCIPAL-NOT-LAUNDERED-AS-PERSISTENT-KEY /
ATTRIBUTION-EPISTEMIC-AUTHORITY-SEPARATION-PASS /
PERSISTENT-AUTHORSHIP-NOT-EPISTEMICALLY-NECESSARY-UNDER-CURRENT-CONTRACT /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.
