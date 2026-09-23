# MQR-4.9 — Live Grid Recovery Lane — PRESEAL B

## Trigger
Lane A current snapshot was INCONCLUSIVE because displayed frequency was exactly 50.0 Hz and system_balance was null.

This file defines a NEW prospective lane. It does not retroactively alter Lane A.

## Source
Elering grid history through NordAPI, which archives 5-minute snapshots of production, consumption, frequency, system balance and related quantities.

## Selection rule frozen before reveal
Open the newest available history records and select the first record, scanning backward in time, satisfying all of:
1. frequency is non-null;
2. system_balance is non-null;
3. frequency differs from 50.000 by at least the source's displayed precision;
4. timestamp is after 2026-09-23T00:00:00+03:00 if such a record is available; otherwise report NO-QUALIFYING-POSTDATE RECORD.

No outcome-dependent skipping beyond these rules is allowed.

## Rivals
Rival A — balance-sensitive snapshot relation:
sign(system_balance) should match sign(frequency-50 Hz), subject to source sign convention and timestamp alignment.

Rival B — snapshot-decoupled relation:
no directional sign relation is expected between the local balance field and contemporaneous frequency.

## Separator
A-consistent: same nonzero sign with unambiguous sign convention.
B-compatible: opposite nonzero signs with unambiguous convention.
INCONCLUSIVE: sign convention cannot be established from source documentation, timestamp fields are mismatched, or no qualifying record exists.

## Honesty constraints
- do not reinterpret the sign convention after seeing values;
- do not change the qualifying-record rule after reveal;
- one snapshot cannot establish causality, inertia, droop or the swing equation;
- even a clean A-consistent snapshot earns only a scoped directional-support update.

## Blindness status
The numeric outcome is generated after model training and is therefore eligible for TRAINING-INDEPENDENT OUTCOME status.
CONTEXT-INDEPENDENT remains NO in this conversation.