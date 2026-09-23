# MQR-4.10 Lane F Mechanical Predictor Receipt — Frozen Before Live Estimate Reveal

Predictor input:
- scheduledTime = 2026-09-23T06:10:00.000Z
- on-time window = ±30 s
- strong deviation threshold = 120 s

Predictor did NOT receive:
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
- scheduled_epoch = 1790143800
- Rival A expectation = ON_TIME_WINDOW_±30s
- Rival B expectation = DELAY_ALLOWED
- STRONG_B threshold = |delay_est| >= 120 s
- A_CONSISTENT threshold = |delay_est| <= 30 s
- otherwise INCONCLUSIVE

No winner assigned before reveal.

This receipt was frozen before C2 liveEstimateTime reveal.