# REALPROMOTE 0.28 — Promotion-Conflict Dynamics

Status: **CANDIDATE / PRE-REVEAL**

MQR-4.61 extends REALPROMOTE 0.27 from static promotion-reason conflict to typed relation transitions.

## Live candidate objects

- **PRTR** — Promotion-Relation Transition Receipt
- **PHL** — Promotion History Ledger
- **ODR** — Option/Debt Receipt
- **RMR** — Reason-Mutation Receipt

## Constitutional rule

Historical path is promotion-relevant only when it leaves a typed material consequence in the current authority state, including option loss, irreversible debt, provenance change, contamination, or another explicitly represented state-bearing consequence.

Mere chronology, sunk effort, prestige, narrative continuity, or revision count does not create authority.

## Transition surface

~~~text
STABLE
INCOMPARABLE_TO_DOMINATES
DOMINATES_TO_INCOMPARABLE
RELATION_REVISED
VETO_ACTIVATED
VETO_RETIRED
SCOPE_REVERSED
HORIZON_REVERSED
REASON_MUTATED
REOPENED
CYCLE_ENTERED
CYCLE_EXITED
HISTORY_IRRELEVANT
~~~

## Dynamic guards

~~~text
CURRENT RELATION LABEL != COMPLETE CONSTITUTIONAL STATE
SAME TERMINAL RELATION != SAME MATERIAL HISTORY
REVISION ORDER MAY BE NONCOMMUTATIVE
RESOLUTION != PERMANENT RESOLUTION
VETO AUTHORITY NEED NOT BE MONOTONE
MORE EVIDENCE != MONOTONE AUTHORITY
REASON MUTATION != NEW INDEPENDENT WARRANT
OLD LABEL != EXACT RESTORATION
MATERIAL HYSTERESIS = ADMISSIBLE
CHRONOLOGY / SUNK-COST HYSTERESIS = REJECT
CONFLICT CYCLE != OBLIGATION TO SCALARIZE
HISTORY SCALARIZATION = OFF
UNIVERSAL HISTORICAL META-UTILITY = NOT EARNED
~~~

## Packet

A v0.28 packet begins with `REALPROMOTE 0.28` and ends with `END`.

Fields may include prior/new relation, scope/horizon before/after, reason type before/after, ancestry continuity, veto state before/after, reopening, cycle state, option loss, irreversible debt, provenance change, chronology-only marker, material-history marker and event-order sensitivity.

Absent optional fields use conservative defaults. Governance gates default PASS only inside the dedicated audited evaluator; packets that explicitly fail sealing, lineage or audit are rejected by the evaluator.

## Authority ceiling

v0.28 is not:
- a utility over histories;
- a ranking of all constitutional paths;
- a convergence theorem;
- a universal transition priority;
- an argument that all path dependence is epistemically legitimate.

It is an auditable transition receipt whose authority remains local to its declared evidence, scope, horizon, ancestry and material state.
