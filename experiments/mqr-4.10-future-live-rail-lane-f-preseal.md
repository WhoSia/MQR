# MQR-4.10 — Future-Event Live Rail Lane F — PRESEAL

## Purpose
Obtain a genuinely post-preseal operational outcome, not a past event whose actual time may already exist.

## Source
NordAPI Finland live trains endpoint backed by Fintraffic/Digitraffic live rail data.

## Temporal gate
Only timetable rows with:
scheduledTime >= 2026-09-23T06:10:00.000Z
are eligible.

This threshold is frozen before C1.

## Deterministic selection rule
From /finland/rail/live-trains?limit=20:
1. enumerate all timetable rows from the returned first 20 trains;
2. retain rows with scheduledTime >= 2026-09-23T06:10:00.000Z;
3. select the row with earliest scheduledTime;
4. ties: lower trainNumber, then earlier row index.

Outcome fields must not influence selection.

## C1 compiler output allowed
- departureDate
- trainNumber
- stationShortCode
- type
- scheduledTime

Forbidden:
- actualTime
- liveEstimateTime
- differenceInMinutes
- causes

## Masked predictor input
Predictor receives only:
- scheduledTime s
- on-time threshold 30 s
- strong-deviation threshold 120 s

No source identity, train identity, station, domain, date, URL or outcome.

## Frozen rivals
Rival A — static timetable:
live operational prediction should remain within ±30 s of scheduledTime.

Rival B — dynamic operational-state:
current operational estimate may differ materially from schedule because realized network state is not encoded in static timetable.

## C2 held-out outcome
After immutable predictor receipt:
fetch exact train detail and exact matching row.
Reveal:
- liveEstimateTime if non-null;
- if liveEstimateTime is null and actualTime exists only after event occurrence, this lane is INCONCLUSIVE for post-preseal prediction;
- do not substitute another row.

## Mechanical scorer
delay_est = liveEstimateTime - scheduledTime.

STRONG_B:
|delay_est| >= 120 s.

A_CONSISTENT:
|delay_est| <= 30 s.

INCONCLUSIVE:
otherwise or liveEstimateTime null.

## Four-axis target
SEQUENCE-HELD-OUT = YES if receipt precedes C2.
IDENTITY-MASKED = YES for predictor.
CONTEXT-INDEPENDENT = YES for deterministic predictor/scorer runtime only.
TRAINING-INDEPENDENT OUTCOME = YES if liveEstimateTime is generated after this preseal for the future event.

## Authority ceiling
A single train event can only update the claim that a static timetable was or was not sufficient for this event's live operational timing.
No general railway-dynamics theory is promoted.

## No laundering
If no qualifying future row or no liveEstimateTime exists, result = INCONCLUSIVE.