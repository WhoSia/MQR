# MQR-4.17 — Externally Constituted Replacement Protocol

Status: ACTIVE / PRESEAL

## Objective
Positively realize governance independence after the MQR-4.16 veto.

## Independent rule-selection procedure
Before any fresh outcome is retrieved:
1. An external scholarly/search adjudication surface will be queried for a prospective, outcome-insensitive rule for aligning a 3-minute power interval with higher-frequency frequency observations.
2. MQR will adopt the first clearly operational rule returned that:
   - is defined without access to future outcome values;
   - uses only timestamps/interval structure;
   - yields a deterministic single frequency summary per power interval;
   - has an explicit missingness/non-uniqueness failure condition.
3. MQR may not substitute a different rule after seeing fresh data.
4. If no operational rule is returned, replay is blocked.

## Dual-key promotion
Promotion requires BOTH:
KEY A — MQR mechanical execution receipt:
- fresh post-preseal interval;
- frozen externally selected rule applied exactly;
- no post-outcome repair.

KEY B — external constitutional ratification after execution:
- confirms that the executed rule matches the prospectively selected rule;
- confirms no rule was changed after outcome reveal;
- may return APPROVE / REJECT / UNCERTAIN.

Only APPROVE + KEY A PASS can realize positive governance independence for this stage.
REJECT or UNCERTAIN => HOLD.

No fresh outcome retrieval before the independent rule is sealed.
