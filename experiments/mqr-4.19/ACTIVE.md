# MQR-4.19 — Publicly Auditable Provenance Chain, Ratifier-Visible Preseal Binding, Independent Receipt Verification, Dual-Key Re-Adjudication & Whether Governance Independence Can Survive Full External Auditability

Status: ACTIVE / KEY A PASS / KEY B PASS / DUAL-KEY CLOSED

## Inherited KEY A
MQR-4.18 KEY A mechanical execution receipt:
7317e7ec57deccd2cfb6ada286b2d589eef17fad

KEY A = PASS.

## Public provenance audit
Audit contract preseal:
ce49859de312164f3b15a3776610e000f603e01f

Public audit manifest:
5934ef620947adb78685df0d192cdf3ae920c465

External verifier:
Exa public-web fetch.

Externally verified immutable anchors:
- rule-seal commit c44c6446dd865bb50453390981075123dbc74d76 at 2026-09-23T15:51:19Z
- fresh interval 2026-09-23T15:54:00Z -> 15:57:00Z
- execution receipt commit 7317e7ec57deccd2cfb6ada286b2d589eef17fad at 2026-09-23T16:13:01Z

Externally retrieved pinned rule content:
MIDPOINT-NEAREST SAMPLE; frequency-interval midpoint representation; tie -> earlier; no averaging/endpoint/interpolation/outcome-dependent fallback.

Externally retrieved pinned execution content:
- same c44c644 rule anchor
- power midpoint 15:55:30Z
- candidate 1 midpoint 15:55:26Z, distance 4 s, 49.975 Hz
- candidate 2 midpoint 15:56:26Z, distance 56 s, 49.994 Hz
- candidate 1 selected

Public path history independently showed:
- rule creation at c44c644, 15:51:19Z
- no intervening modification before execution
- later retirement only at e465a26, 16:14:18Z

Frozen audit criteria:
A1 chronology PASS
A2 rule content PASS
A3 rule/execution identity PASS
A4 post-seal freshness PASS
A5 candidate selection PASS
A6 no pre-execution rule modification PASS

KEY B = PASS.

KEY B public-verification receipt:
c2f2d7328d824deff19e5ebd73445ba87f12e75d

## Dual-key closure
KEY A PASS + KEY B PASS
=> DUAL-KEY CLOSURE = PASS.

Within the operational MQR Generation-IV contract:
POSITIVE GOVERNANCE INDEPENDENCE = JOINTLY REALIZED.

This claim is scoped:
- external constitutional rule selection was prospective;
- fresh execution followed the externally selected rule;
- public provenance was independently retrievable and chronologically auditable;
- promotion required two separately constituted keys.

## Remaining limit
GitHub reports relevant commits as unsigned.

Therefore:
PUBLIC AUDITABILITY PASS
does not imply
CRYPTOGRAPHIC AUTHOR NON-REPUDIATION PASS.

No claim is made that repository identity, authorship, or timestamp chronology has been independently notarized outside GitHub.

## Strongest result
Governance independence can survive full public-content/chronology auditability when:
1. external authority can alter the experiment constitution;
2. the resulting rule is frozen prospectively;
3. fresh execution is mechanically compliant;
4. an independent public verifier can reconstruct the preseal -> outcome -> execution chain;
5. promotion requires both execution and provenance keys.

This is a positive realization of governance independence under the present MQR operational definition, not a metaphysical guarantee of absolute independence.

## Verdict
PUBLIC-AUDIT-PRESEAL-PASS /
RATIFIER-VISIBLE-ANCHORING-PASS /
PINNED-RULE-RETRIEVAL-PASS /
PINNED-EXECUTION-RETRIEVAL-PASS /
CHRONOLOGY-VERIFICATION-PASS /
NO-PREEXECUTION-RULE-MODIFICATION-PASS /
KEY-A-PASS /
KEY-B-PASS /
DUAL-KEY-CLOSURE-PASS /
POSITIVE-GOVERNANCE-INDEPENDENCE-JOINTLY-REALIZED /
PUBLIC-AUDITABILITY-PASS /
CRYPTOGRAPHIC-NONREPUDIATION-NOT-ESTABLISHED /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.

Historical research records are canonical in Notion. GitHub experiments/ retains only the current active stage.
