# MQR-4.10 — Fresh Snapshot Lane D — PRESEAL

## Trigger
The first 4.10 masked-baseline attempt reused timestamp 1790142300, whose held-out frequency had already been revealed in MQR-4.9.

Therefore that attempt is INVALID-AS-BLIND and may not support SEQUENCE-HELD-OUT authority.

This Lane D is a new prospective lane.

## Freshness requirement
C1 must return a timestamp strictly greater than:

1790142300

If not, verdict = NO-NEW-SNAPSHOT and no predictor receipt is created.

## C1 allowed fields
Return ONLY:
- timestamp
- production
- consumption

Frequency and balance fields are forbidden.

## Masked predictor input
If fresh:
- u = production
- v = consumption
- threshold = 100

No source identity, timestamp, domain label, URL, frequency or balance field is supplied to the mechanical predictor.

## Frozen rival logic
Rival A:
if |u-v| >=100 MW, predicts held-out frequency class DEVIATED:
|f-50| >=0.02 Hz with sign matching u-v.

Rival B:
if |u-v| >=100 MW, allows held-out class NEAR_NOMINAL:
|f-50| <=0.01 Hz despite large local imbalance.

If |u-v| <100 MW:
NOT_SEPARATING.

## C2 reveal
Only after immutable predictor receipt:
- fetch timestamp + frequency only.
- timestamp must equal C1 timestamp.
- otherwise SNAPSHOT-MISMATCH / INVALID.

## Mechanical scorer
STRONG_B:
|u-v| >=100 and |f-50| <=0.01.

A_CONSISTENT:
|u-v| >=100 and |f-50| >=0.02 and sign(f-50)=sign(u-v).

INCONCLUSIVE otherwise.

## Blindness target
SEQUENCE-HELD-OUT = YES only if timestamp is fresh and predictor receipt precedes C2.
IDENTITY-MASKED = YES for predictor.
CONTEXT-INDEPENDENT = YES only for deterministic predictor/scorer runtime, not source selection.
TRAINING-INDEPENDENT OUTCOME = YES because fresh telemetry is post-training.

## No laundering
If no fresh snapshot is available, 4.10 may still pass infrastructure/rigor but may NOT claim all-four joint satisfaction.