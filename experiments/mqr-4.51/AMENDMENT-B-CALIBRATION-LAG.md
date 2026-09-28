# MQR-4.51 — Amendment B: Calibration-Only Confirmation Lag Family

Status: POST-PRESEAL / PRE-HOLDOUT / POLICY-FAMILY EXTENSION / RAW-OQSC PRESERVED

## Motivation

MQR-4.51 is a calibration court. It must be able to discover that the raw MQR-4.50 stop rule is systematically early or late without rewriting the hidden holdout after seeing it.

Therefore raw `P-OQSC` remains frozen and is scored exactly as inherited.

A distinct successor family is admitted before holdout materialization:

~~~text
P-OQSC-LAG-lambda
lambda in {0,1,2,3}
~~~

After the first OQSC stop-eligible state, the wrapper requires `lambda` additional consecutive stop-eligible inquiry transitions before emitting STOP.

Any active REOPEN, upstream HOLD/REOPEN, live debt, criterion noninvariance, decision-contract break or loss of OQSC eligibility resets the confirmation counter.

## Calibration rule

`lambda` is selected **only** on the calibration split by the predeclared safety-first ordering:

~~~text
1. minimize PSE_live
2. minimize AE_live
3. minimize MISSED_REOPEN
4. minimize OIW
5. minimize BER
6. minimize PD_live
7. minimize RL_max
8. choose smaller lambda on an exact tie
~~~

This is not claimed as a universal utility function. It is a calibration protocol that prioritizes the frozen fatal errors before resource waste.

The complete metric vector is still reported and Pareto analysis remains primary on untouched holdout.

## Holdout custody

Holdout worlds are not hand-selected.

Seeds are derived mechanically from:

~~~text
SHA256(
  "MQR-4.51"
  + preseal_commit
  + domain
  + family
  + "HOLDOUT"
  + replicate_index
)
~~~

with preseal commit:

~~~text
c61c9516a4e38ee1241a30ca3d09186bc58b53e8
~~~

The same mechanism derives discovery/calibration seeds with their own split labels.

The generator code, policy family, metric definitions and lambda-selection rule are committed before the first authoritative benchmark run.

## Interpretation

Possible outcomes:

### Raw and calibrated both pass

The v0.17 rule is already calibrated on the declared benchmark family; the lag wrapper adds no material value.

### Raw fails; calibrated passes

MQR-4.50 established **constitutional admissibility**, but the inherited immediate-stop implementation is not empirically calibrated on the benchmark. A calibrated delay wrapper is required for the tested family.

This does not falsify 4.50's metaphysical/operational distinction. It defeats the stronger behavioral claim that a first eligible OQSC state is already a calibrated stopping time.

### Both fail

No stopping competence promotion is allowed. MQR-4.51 closes as a calibration defeat and leaves v0.17 behavioral usefulness unearned.

## No holdout repair

After the first authoritative holdout report is emitted:
- no change to lambda family;
- no change to selection ordering;
- no change to generator timing distributions;
- no change to hidden scoring semantics;
- no post-hoc removal of failing world families.

Implementation bugs may be repaired only if the scientific outputs are demonstrably unchanged by the repair.
