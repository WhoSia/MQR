# MQR-4.19 — Publicly Auditable Provenance Chain

Status: ACTIVE / PUBLIC-AUDIT PRESEAL

## Scope
This stage does not alter the MQR-4.17 rule, the MQR-4.18 fresh outcome, or the MQR-4.18 mechanical result.
It only tests whether the already-existing GitHub history is externally auditable enough to satisfy the previously missing ratification key.

## Immutable anchors to be audited
External rule seal commit:
c44c6446dd865bb50453390981075123dbc74d76

Fresh execution receipt commit:
7317e7ec57deccd2cfb6ada286b2d589eef17fad

Prior external ratifier receipt:
ddfc008d47baa2d29cc3a3614d1a89214d061598

## Audit questions
An independent public-web verifier must establish:
1. the rule-seal commit existed before the fresh replay interval;
2. the rule content contains midpoint-nearest selection and forbids post-outcome fallback;
3. the execution receipt uses the same rule;
4. the fresh interval is later than the rule-seal time;
5. the execution receipt records the two candidate frequency observations and selects the nearest one;
6. no intervening commit modified the sealed rule before execution.

## Re-adjudication contract
KEY A remains inherited PASS from MQR-4.18.
KEY B may be upgraded from UNCERTAIN only if an external verifier can independently retrieve and verify the public GitHub commit chain and timestamps.

The verifier must use public repository URLs / commit metadata, not MQR-provided prose alone.
If any anchor is inaccessible or chronology cannot be verified: HOLD.
