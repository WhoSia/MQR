# MQR-4.14 — Prospective Temporal-Join Constitution

Status: ACTIVE PRESEAL
Date: 2026-09-23

## Frozen inheritance
Source class: Fingrid Open Data.
Datasets:
- 177 frequency [Hz]
- 192 production [MW]
- 193 consumption [MW]

Frozen separator inherited unchanged:
- strong-B iff |production-consumption| >= 100 MW
- and |frequency-50.00| <= 0.01 Hz.

Required fields remain timestamp, production, consumption, frequency.
No post-reveal fallback or threshold change is authorized.

## Temporal join operator J_mid
1. Select the first future production interval P=[t0,t1) observed after this preseal for which dataset 192 and dataset 193 have identical startTime and endTime.
2. Compute t_mid=(t0+t1)/2.
3. In dataset 177 select the unique frequency record F=[u0,u1) satisfying u0 <= t_mid < u1.
4. If no such F exists, more than one F satisfies it, or any required value/time is null or malformed: INCONCLUSIVE.
5. Set frequency := F.value.
6. Set local_balance := production.value - consumption.value.
7. Apply the frozen separator mechanically.

No nearest-neighbor, endpoint, mean, interpolation, or alternate frequency observation may be substituted after reveal.

## Freshness
All selected records must be retrieved after this GitHub preseal commit.
The power interval endTime must be later than the latest power interval used in MQR-4.13 (2026-09-23T06:45:00Z).

## Authority ceiling
Runtime mechanical scoring may satisfy narrow context isolation.
Governance independence remains HOLD because source family, join rule and separator lineage are governed in the same research context.

This file is the sole active experiment artifact for the current MQR stage; historical research records live in Notion.
