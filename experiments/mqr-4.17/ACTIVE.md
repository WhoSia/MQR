# MQR-4.17 — Externally Constituted Replacement Protocol, Independent Rule Selection, Post-Veto Fresh Replay, Dual-Key Promotion Authority & Whether Governance Independence Can Be Positively Realized

Status: ACTIVE / EXTERNAL CONSTITUTION PASS / FRESH REPLAY PENDING

## Constitutional preseal
Initial dual-key preseal commit:
b5bc6ee31802f98d3c38c8727b8d61f6d5150ba7

## Independent rule selection
External selector:
Factagora/Agora deep research.

External rule selected:
MIDPOINT-NEAREST SAMPLE.

Operational rule:
- first future matched 3-minute production/consumption interval;
- compute interval midpoint;
- among frequency observations inside the same power interval, choose the observation whose representative timestamp is closest to the midpoint;
- exact tie -> earlier observation;
- no candidate -> INCONCLUSIVE;
- no averaging, endpoint substitution, interpolation, or outcome-dependent fallback.

External rule seal commit:
c44c6446dd865bb50453390981075123dbc74d76

Rule seal timestamp:
2026-09-23T15:51:19Z.

## Dual-key promotion
KEY A — MQR mechanical execution receipt.
KEY B — external constitutional ratification.

Positive governance-independence promotion requires BOTH keys.

## Freshness audit
Forced-live Fingrid retrieval after rule sealing showed:

Production/consumption latest matched interval:
2026-09-23T15:45:00Z -> 15:48:00Z

This interval predates the external-rule seal timestamp.

Frequency observations had advanced through:
2026-09-23T15:50:56Z -> 15:51:56Z

But a valid replay requires a matched power interval generated after the rule seal.

Therefore:
KEY A = NOT AVAILABLE.
FRESH POST-SEAL POWER INTERVAL = NOT YET ADMITTED.
MECHANICAL REPLAY = NOT RUN.
KEY B RATIFICATION = NOT INVOKED, because there is no executed receipt to ratify.

No historical interval was reused.
No freshness criterion was relaxed.
No source was switched after reveal.

## Result
MQR-4.17 positively realizes one missing governance component:
an external authority selected a constitution-level temporal rule prospectively, and MQR bound itself to that rule before outcome retrieval.

This is stronger than MQR-4.16 because the external authority not only vetoed but also supplied the replacement constitution.

However full positive governance independence is NOT YET REALIZED because the dual-key promotion cannot be completed without a post-seal fresh execution receipt and subsequent external ratification.

## Verdict
EXTERNAL-REPLACEMENT-CONSTITUTION-PASS /
INDEPENDENT-RULE-SELECTION-PASS /
MIDPOINT-NEAREST-RULE-SEALED /
EXTERNAL-AUTHORITY-CHANGED-EXPERIMENT-CONSTITUTION /
DUAL-KEY-PROMOTION-PRESEALED /
POST-SEAL-FRESH-POWER-INTERVAL-NOT-YET-AVAILABLE /
HISTORICAL-REPLAY-REFUSED /
KEY-A-NOT-YET-AVAILABLE /
KEY-B-NOT-YET-INVOKED /
POSITIVE-GOVERNANCE-INDEPENDENCE-PARTIAL /
FULL-GOVERNANCE-INDEPENDENCE-NOT-YET-REALIZED /
ALL-FOUR-JOINT-SATISFACTION-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.

Historical research records are canonical in Notion. GitHub experiments/ retains only the current active stage.
