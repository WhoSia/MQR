# MQR-4.10 Mechanical Predictor Receipt — Frozen Before Outcome Reveal

Input received by predictor:
- u = 885.84
- v = 988.83

No source identity, domain label, frequency, balance field, URL or timestamp was provided to the predictor runtime.

Deterministic computation:
- d = u - v = -102.99
- |d| = 102.99 >= 100
- separator_ready = TRUE

Frozen rival expectations:
- Rival A: DEVIATED
- Rival B: NEAR_NOMINAL_ALLOWED

Mechanical scoring after held-out reveal:
- STRONG_B if |d| >= 100 and |f-50| <= 0.01
- A_CONSISTENT if |d| >= 100 and |f-50| >= 0.02 and sign(f-50)=sign(d)
- INCONCLUSIVE otherwise

This receipt was created before the held-out frequency value was revealed to the adjudication sequence.
