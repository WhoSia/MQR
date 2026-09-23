# MQR-4.14 — Prospective Temporal-Join Constitution

Status: ACTIVE / EXECUTED
Date: 2026-09-23
Preseal commit: 94fa632a4f302fbaaba7067349a2fc84a07302cd

## Frozen inheritance
Source class: Fingrid Open Data.
Datasets:
- 177 frequency [Hz]
- 192 production [MW]
- 193 consumption [MW]

Frozen separator inherited unchanged:
- strong-B iff |production-consumption| >= 100 MW
- and |frequency-50.00| <= 0.01 Hz.

Required fields remain timestamp, production, consumption, frequency.
No post-reveal fallback or threshold change is authorized.

## Temporal join operator J_mid
1. Select the first future production interval P=[t0,t1) observed after preseal for which dataset 192 and dataset 193 have identical startTime and endTime.
2. Compute t_mid=(t0+t1)/2.
3. In dataset 177 select the unique frequency record F=[u0,u1) satisfying u0 <= t_mid < u1.
4. If no such F exists, more than one F satisfies it, or any required value/time is null or malformed: INCONCLUSIVE.
5. Set frequency := F.value.
6. Set local_balance := production.value - consumption.value.
7. Apply the frozen separator mechanically.

No nearest-neighbor, endpoint, mean, interpolation, or alternate frequency observation may be substituted after reveal.

## Fresh post-preseal replay
Matched power interval:
- P/C interval: 2026-09-23T06:48:00Z -> 2026-09-23T06:51:00Z
- production: 7200.84 MW
- consumption: 8982.72 MW
- local_balance: -1781.88 MW
- midpoint: 2026-09-23T06:49:30Z

Unique frequency interval containing midpoint:
- 2026-09-23T06:48:56Z -> 2026-09-23T06:49:56Z
- frequency: 50.041 Hz
- |frequency-50| = 0.041 Hz

Mechanical result:
- |local_balance| = 1781.88 MW >= 100 MW: PASS
- |frequency-50| = 0.041 Hz <= 0.01 Hz: FAIL
- STRONG-B WITNESS: NOT PRESENT

This is not an A win. The frozen separator only tests for a strong-B witness; failure to satisfy it leaves the rival comparison unresolved under this single interval.

## Authority receipt
- timestamp-certified fresh source: PASS
- cross-source temporal join executable: PASS
- post-preseal outcome bytes: PASS
- mechanical scoring without outcome repair: PASS
- sequence-held-out: PASS for this replay
- identity-masked final scorer: PASS-NARROW (only numeric/time contract required)
- runtime-context-independent: PASS-NARROW
- governance-independent: HOLD
- all-four joint adjudication: HOLD because governance independence remains unresolved

## Verdict
TEMPORAL-JOIN-CONSTITUTION-PASS /
CLOCK-ALIGNMENT-PRESEALED /
FRESH-INTERVAL-REPLAY-PASS /
MECHANICAL-SCORING-PASS /
STRONG-B-WITNESS-NOT-PRESENT /
NO-A-WIN-INFERENCE /
POST-REVEAL-REPAIR-NOT-USED /
CROSS-SOURCE-REPRESENTATION-TRANSPORT-EXECUTABLE /
GOVERNANCE-INDEPENDENCE-HOLD /
ALL-FOUR-JOINT-SATISFACTION-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.

Historical research records are canonical in Notion. GitHub experiments/ retains only the current active stage.
