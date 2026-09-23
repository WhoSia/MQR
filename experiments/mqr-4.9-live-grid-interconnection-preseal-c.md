# MQR-4.9 — Live Grid Interconnection Lane C — PRESEAL

## Trigger
Lane A was inconclusive because system_balance was null / frequency nominal.
Lane B found no qualifying post-2026-09-23 history record with nonzero balance.
This Lane C is a NEW prospective test, not a repair of either earlier lane.

## Source
A fresh Elering current grid snapshot fetched after this commit with maxAge=0.

## Selection rule
Use the first current snapshot whose timestamp is strictly later than the Lane A current-response timestamp and which contains non-null production, consumption and frequency.
If the timestamp has not advanced, return NO-NEW-SNAPSHOT.

## Rival A — national-island balance representation
Treat Estonia as if local active-power balance were captured by P_local = production - consumption.
Frozen prediction:
- large negative P_local should correspond to frequency below 50 Hz;
- large positive P_local should correspond to frequency above 50 Hz;
- if |P_local| >= 100 MW while |f-50| <= 0.01 Hz, Rival A is strongly contradicted.

## Rival B — synchronous-interconnection representation
Estonia is embedded in a larger interconnected power system. Local production-consumption difference can be balanced by cross-border exchange and control action.
Frozen prediction:
- local P_local may be hundreds of MW away from zero while system frequency remains very close to 50 Hz;
- sign(P_local) need not match sign(f-50) in a single national snapshot.

## Separator
Strong B win:
|production-consumption| >= 100 MW and |frequency-50| <= 0.01 Hz in the fresh snapshot.

A-consistent:
|production-consumption| >= 100 MW and frequency deviation is >=0.02 Hz with matching sign, provided no explicit cross-border field reveals offsetting imports/exports.

Inconclusive:
timestamp not new; fields null; or deviation/imbalance are below thresholds.

## Authority ceiling
A single snapshot cannot establish the full swing equation or quantify interconnector flows.
A strong B result licenses only:
SCOPED SUPPORT that local national generation-consumption balance is not by itself sufficient to determine synchronous-grid frequency.

## Blindness
The exact fresh numeric outcome must be generated after this preseal and therefore cannot be pretraining memory.
CONTEXT-INDEPENDENT remains NO.