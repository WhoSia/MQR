# MQR-4.63 — FINAL SEAL

Status: **FINAL-SEAL / EXACT-HEAD-VERIFICATION-REQUIRED**

## Frozen ancestry

- MQR-4.62 canonical parent: `e39eab7701eba885e76aaf617ee19825550cc508`
- PRESEAL: `a0dcb1605dbc691cca414d5b27b4fcdf8dc5e910`
- WORLD-CALIBRATION-MANIFEST: `d114f87ba2e295a6a838c74989f12173f213d312`
- WORLD-SELECTION final pre-reveal pack: `010ee9dca471b1a144b8ae67de9682af4ecb3ee7`
- ANALYSIS-PLAN: `818798005b9e02ec73c03ef98cfa1b0e98c8efed`
- first executable reveal: `34a22befcb30e8328c19d29b0964ab3ebe84f248`
- first reveal run: `36963803586`

No world, policy family, seed count, action budget, metric orientation, effect threshold, bootstrap rule, non-reducibility threshold, negative-control rule or classification criterion changed after first executable reveal.

No scientific or plumbing repair was required on the first reveal.

## First-reveal qualification

The first reveal completed:
- 5 frozen worlds;
- 3,392 paired policy runs;
- independent metric recomputation;
- deterministic exact replay;
- frozen bootstrap analysis;
- negative-control checks;
- scalar-score prohibition.

All four dedicated jobs passed.

## Sealed scientific result

~~~text
OPR       COLLAPSES_TO_BASELINE
ARR       COLLAPSES_TO_BASELINE
EAI       COLLAPSES_TO_BASELINE
EXTERIOR  COLLAPSES_TO_BASELINE
NEDL      SURVIVES_LOCAL (SCOUT-PARK only)

SURVIVES_CROSS_DOMAIN = NONE
~~~

NEDL / SCOUT-PARK:
- own-ablation mean benefit delta on NED: `0.1539`
- bootstrap 95% CI: `[0.1337, 0.1760]`
- positive sign fraction: `0.917`

Negative controls:
- CAUSAL-SEP: `mqr_full == causal_identifiability` on conventional success; BOD/CSD/NED remain inactive.
- SENSING-GRID: `mqr_full == entropy_greedy` on conventional success; BOD/CSD/NED remain inactive.

## Primary doctrinal result

~~~text
DIAGNOSTIC SEPARABILITY
!=
POLICY INCREMENTALITY

TYPED RECEIPT
!=
INDEPENDENTLY EARNED CONTROLLER

STRONG-BASELINE ABSORPTION
=> NO REDUNDANT GOVERNANCE PROMOTION
~~~

THEORY-ECOLOGY demonstrates that ERR/RCR/NED/BSI can separate acquisition histories whose selected conventional terminal success is equal.

But the explicit MQR-specific ARR/EAI/NEDL/exterior controls do not add own-ablation value there because strong disagreement / representative / random / robust-multifactor acquisition already avoids the exposed failure.

## Semantic-version decision

**NO REALACQUIRE v0.30 PROMOTION.**

REALACQUIRE 0.29 remains the typed diagnostic/constitutional surface.

MQR-4.63 narrows, rather than deletes, the authority of 4.62 acquisition receipts:
- OPR / ARR / EAI / exterior reserve remain diagnostic and locally constitutive, but no cross-domain independent controller authority is earned.
- NEDL remains a local action-guiding candidate in the SCOUT-PARK regime only.

## Publication consequence

- Broad cross-domain MQR acquisition-controller paper: **not supported**.
- Narrow diagnostic-geometry acquisition paper: **still plausible**, but not yet publication-ready.
- Local Progress Geometry / Partial Scientific Authority paper: **relative priority increased**.
- Executable Scientific Constitutions methods paper: 4.63 becomes an anti-inflation negative-result case study.

## Exact-head closure gate

The commit containing this file is canonical only if that exact SHA has all of:
1. `MQR-4.63/Calibration` SUCCESS
2. `MQR-4.63/Independent-Audit` SUCCESS
3. `MQR-4.63/Analysis` SUCCESS
4. `MQR-4.63/Deterministic-Replay` SUCCESS

No cumulative Real-Language qualification is required because MQR-4.63 promotes no new Real-Language surface and changes no Real-Language implementation.

Repository policy remains **MAIN_ONLY**.

No repository mutation is permitted after verified closure.
