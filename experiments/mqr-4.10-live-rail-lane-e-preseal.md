# MQR-4.10 — Live Rail Context-Isolation Lane E — PRESEAL

## Purpose
Test all four blindness axes using a fresh engineering/operations measurement whose exact outcome is generated after model training.

## Source
NordAPI Finland live trains endpoint, upstream Fintraffic/Digitraffic.
Documentation states currently-running trains with full timetable rows and live arrival/departure estimates, refresh cadence ~10 seconds.

## Deterministic selection rule
C1 fetches:
https://nordapi.ee/api/v1/finland/rail/live-trains?limit=20

Select:
1. array element index 0;
2. timetableRows element index 0.

No outcome-dependent skipping is allowed.

## C1 compiler output allowed
Only:
- departureDate
- trainNumber
- stationShortCode
- type (ARRIVAL/DEPARTURE)
- scheduledTime

Forbidden from C1:
- actualTime
- liveEstimateTime
- differenceInMinutes
- causes
- runningCurrently
- source metadata beyond fields needed to re-fetch exact train

## Masked predictor input
Predictor receives only:
- s = scheduledTime
- epsilon_on_time = 30 seconds
- epsilon_delay = 120 seconds

It does NOT receive:
- train number
- date
- station
- rail/train/domain label
- source URL
- actual or estimated time

## Frozen rivals
Rival A — static-timetable representation:
held-out event time should equal scheduledTime within ±30 s.

Rival B — operational-state representation:
live event time may materially depart from schedule because realized operations contain state not represented in the static timetable.

## Predictor receipt
Context-free deterministic runtime outputs:
- A_EXPECTATION = ON_TIME_WINDOW
- B_EXPECTATION = DELAY_ALLOWED
- reference event time = s

No winner is assigned before reveal.

## C2 reveal
After immutable predictor receipt:
fetch exact train detail:
 /finland/rail/train/:date/:number

Select the timetable row exactly matching:
- stationShortCode
- type
- scheduledTime

Reveal:
- actualTime if available;
- otherwise liveEstimateTime;
- if neither exists => INCONCLUSIVE.

## Mechanical scorer
Let y be actualTime, else liveEstimateTime.
Let delay = y - scheduledTime.

- STRONG_B if |delay| >=120 s.
- A_CONSISTENT if |delay| <=30 s.
- INCONCLUSIVE otherwise.

No narrative override.

## Four-axis target
SEQUENCE-HELD-OUT = YES if predictor receipt precedes C2.
IDENTITY-MASKED = YES for predictor.
CONTEXT-INDEPENDENT = YES for deterministic predictor/scorer runtime; source-selection/compiler remains shared-context.
TRAINING-INDEPENDENT OUTCOME = YES because live operational timestamp is generated post-training.

## Authority ceiling
If STRONG_B:
only scoped support that static timetable alone was insufficient for the revealed operational event.

If A_CONSISTENT:
no general claim that timetables are sufficient; only this event failed to separate the rivals.

## Literature inheritance
- MQR-3.35: same-model role switching is not independent evaluation.
- ScienceAgentBench: withhold/alter evaluation-critical information and use executable criteria.
- REFLECT: tested execution outcome outranks narrative attribution.
- Stegenga & Menon + LR-20260914-C/D: independence is dependence-structure sensitive, not nominal diversity.
- Parvinian/NASA: authority remains context-of-use scoped.

No new epistemic primitive.