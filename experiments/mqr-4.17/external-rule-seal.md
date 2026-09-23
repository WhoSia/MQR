# MQR-4.17 — Externally Selected Replacement Rule

Status: SEALED BEFORE OUTCOME

External selector:
Factagora/Agora deep research.

External selection:
MIDPOINT-NEAREST SAMPLE.

Operational constitution:
1. For the first future matched production/consumption 3-minute interval [t0,t1), compute midpoint t_mid.
2. Consider only frequency observations whose timestamps/intervals lie within the same 3-minute power interval.
3. Select the single frequency observation whose representative timestamp is closest to t_mid.
4. If exactly tied, choose the earlier timestamp.
5. If no frequency observation is available inside the power interval, admission_status = INCONCLUSIVE.
6. No averaging, endpoint substitution, interpolation, or outcome-dependent fallback is permitted.

For the Fingrid interval representation used here, each frequency record [u0,u1) is represented by its midpoint (u0+u1)/2 for distance-to-t_mid.

Freshness:
- power interval endTime must be later than 2026-09-23T15:30:00Z.
- data must be retrieved after this rule-seal commit.

Dual-key ratifier appointed prospectively:
Factagora/Agora fact-check surface.
After execution it will receive the exact preselected rule and execution receipt and may return APPROVE-equivalent / REJECT-equivalent / UNCERTAIN.
UNCERTAIN or REJECT blocks governance-independence promotion.
