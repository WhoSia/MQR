# MQR-4.51 — First Authoritative Holdout Results

Status: FIRST HOLDOUT REVEALED / RAW-OQSC FAIL / CALIBRATED LAG-1 SUCCESSOR PASS / EXTERNAL CALIBRATION HOLD / NO POST-HOLDOUT SCIENTIFIC REPAIR

## Custody

Preseal:
`c61c9516a4e38ee1241a30ca3d09186bc58b53e8`

Calibration-family freeze:
`44f9c91ad0be6691e02970e40643962dd59c5caf`

First authoritative benchmark workflow head:
`458c1bbeb37f876dde3189ed08226ee52f6aca78`

First authoritative run:
`36382410016` — **SUCCESS**

The uploaded report artifact is keyed to that head SHA.

No generator, scoring rule, policy family, hidden-gold semantics or holdout seed rule is modified after this reveal.

## Benchmark census

~~~text
domains      = 3
families     = 12
DISCOVERY    = 108 traces
CALIBRATION  = 144 traces
HOLDOUT      = 216 traces
TOTAL        = 468 traces
~~~

Holdout seeds are SHA256-derived from the MQR-4.51 preseal commit, domain, family, split and replicate index.

Anti-self-scoring audit: **PASS**.

## Calibration-only selections

~~~text
P-FIXED-k        -> k = 12
P-LAST-CHANGE-h  -> h = 6
P-OQSC-LAG-lambda -> lambda = 1
~~~

Lambda was selected on the 144-trace calibration split before holdout scoring.

Calibration grid for the OQSC lag family:

~~~text
lambda=0  PSE=37  AE=37  OIW=21.5
lambda=1  PSE=0   AE=0   OIW=215.5   <- selected
lambda=2  PSE=0   AE=0   OIW=417.5
lambda=3  PSE=0   AE=0   OIW=613.0
~~~

The result is a genuine calibration trade-off: one confirmation transition eliminated calibration premature/action errors while adding inquiry cost.

## Untouched holdout primary vectors

Order:

~~~text
(PSE_live, PD_live, AE_live, OIW, RL_max, MISSED_REOPEN, BER)
~~~

### Raw OQSC

~~~text
(51, 51, 51, 38.5, 0, 0, 18)
~~~

Verdict: **FAIL**.

C1 premature-stop competence failed in all three domains.

### Calibrated OQSC, lambda=1

~~~text
(0, 0, 0, 338.5, 0, 0, 18)
~~~

Verdict: **PASS**.

All C1–C5 conditions passed independently in:
- FAULT;
- MEASUREMENT;
- SEARCH.

### Fatal / comparison controls

~~~text
STOP_NOW
(288, 1272, 288, 0.0, 0, 0, 0)

CONTINUE_ALL
(0, 0, 0, 2367.0, 0, 0, 216)

FIXED-12
(24, 47, 24, 1458.0, 0, 0, 72)

PATIENCE-6
(54, 187, 54, 1227.5, 0, 0, 50)
~~~

The calibrated successor is therefore not just an always-stop or always-continue surrogate.

It removes the holdout premature/action errors observed in the raw rule while using far less additional inquiry than CONTINUE_ALL.

## Domain detail

Calibrated lambda=1:

~~~text
FAULT       PSE=0 AE=0 OIW=78.0  RL=0 MISSED_REOPEN=0 BER=6
MEASUREMENT PSE=0 AE=0 OIW=112.5 RL=0 MISSED_REOPEN=0 BER=6
SEARCH      PSE=0 AE=0 OIW=148.0 RL=0 MISSED_REOPEN=0 BER=6
~~~

Raw OQSC:

~~~text
FAULT       PSE=12 AE=12 OIW=8.0
MEASUREMENT PSE=21 AE=21 OIW=16.5
SEARCH      PSE=18 AE=18 OIW=14.0
~~~

The raw failure is cross-domain rather than localized to one adapter.

## Counterfactual STOP/CONTINUE replay

Raw OQSC:

~~~text
material_continue = 51
inert_continue    = 147
no_stop           = 18
~~~

Calibrated lambda=1:

~~~text
material_continue = 0
inert_continue    = 198
no_stop           = 18
~~~

Thus the 51 raw premature stops coincide exactly with holdout cases where continuing within the already-live inquiry episode would still have produced material information.

The amendment prevents genuinely novel post-stop contacts from being counted as retroactive premature-stop failures.

## Reopening

Both raw and calibrated OQSC achieved:

~~~text
RL_max = 0
MISSED_REOPEN = 0
~~~

on the declared generated post-stop break families.

This establishes only benchmark-internal immediate reopening competence.

## Scientific verdict

MQR-4.51 rejects the behavioral strengthening:

~~~text
OQSC ELIGIBLE
->
STOP NOW IS CALIBRATED
~~~

The inherited 4.50 constitution survives in a thinner role:

~~~text
OQSC ELIGIBLE
->
STOP IS CONSTITUTIONALLY ADMISSIBLE FOR CALIBRATION
~~~

On the declared benchmark family, a one-transition confirmation wrapper earns:

~~~text
PROSPECTIVELY CALIBRATED
INTERNAL CROSS-DOMAIN STOPPING COMPETENCE
~~~

This does **not** promote:

~~~text
lambda=1 AS A UNIVERSAL STOPPING CONSTANT
EXTERNAL SCIENTIFIC CALIBRATION
UNIVERSAL OPTIMALITY
FUTURE-SPACE COMPLETENESS
~~~

## Hard guards

~~~text
PRIMARY SCALAR SCORE = OFF
FUTURE ORACLE = FORBIDDEN
NOVEL POST-STOP CONTACT CHARGED AS PSE = NO
POST-HOLDOUT SCIENTIFIC REPAIR = FORBIDDEN
EXTERNAL CALIBRATION = HOLD
UNIVERSAL OPTIMALITY = FORBIDDEN
~~~
