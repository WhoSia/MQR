# MQR-4.10 Lane E Mechanical Predictor Receipt — Frozen Before Outcome Reveal

Predictor runtime input:
- scheduledTime only: 2026-09-22T16:29:00.000Z
- on-time window: ±30 s
- strong-delay threshold: 120 s

Predictor runtime did NOT receive:
- train number
- departure date
- station code
- rail/train/domain label
- source URL
- actualTime
- liveEstimateTime
- delay field
- cause field

Deterministic output:
- scheduled_epoch = 1790094540
- Rival A expectation = ON_TIME_WINDOW_±30s
- Rival B expectation = DELAY_ALLOWED
- STRONG_B threshold = |delay| >= 120 s
- A_CONSISTENT threshold = |delay| <= 30 s
- otherwise INCONCLUSIVE

No winner is assigned before reveal.

This receipt was frozen before C2 actual/estimate reveal.