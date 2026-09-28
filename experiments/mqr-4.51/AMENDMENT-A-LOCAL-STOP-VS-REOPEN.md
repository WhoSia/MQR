# MQR-4.51 — Scoring Amendment A: Local Stop vs Future Reopening

Status: POST-PRESEAL / PRE-IMPLEMENTATION / CORRECTION OF SCORER SEMANTICS / NO POLICY ADVANTAGE

## Why this amendment exists

The frozen preseal used a single full-trace suffix-stable stop index `tau*` while also requiring positive cases in which a locally justified stop is later reopened by genuinely new admissible world contact.

Those two requirements conflict if every future event is retrospectively charged against the earlier stop.

A rule designed to be reopenable would then be punished merely because the open world later supplied a distinction that was not yet a live/reachable obligation.

That would smuggle a future oracle into the scorer.

## Corrected two-clock semantics

The benchmark therefore separates:

1. **current-obligation stop safety** — whether all material obligations already live/reachable at time t were discharged before stopping;
2. **future reopening competence** — how quickly the policy reopens when genuinely new admissible world contact arrives later.

Define scorer-only `tau_live*(episode,D)` as the earliest stop index in the current inquiry episode such that:
- every obligation already admitted/live in that episode is discharged or explicitly HOLD;
- no still-reachable current suffix event changes the declared authority/action projection;
- no upstream HOLD is laundered;
- current OQSC requirements are satisfied.

A later event tagged `NOVEL_AFTER_STOP` does **not** retroactively make the earlier stop premature.

Instead it starts a separate reopening clock:

~~~text
break_time = first newly admissible post-stop fixed-point break
reopen_time = first policy REOPEN caused by that break
RL = reopen_time - break_time
~~~

By contrast, an event tagged `LIVE_BEFORE_STOP` that was already a registered/reachable obligation when the policy stopped remains part of the premature-stop scorer.

## Consequences

~~~text
MISSED LIVE OBLIGATION
-> PREMATURE-STOP ERROR

GENUINELY NEW POST-STOP CONTACT
-> NO RETROACTIVE PSE
-> REOPENING-LATENCY TEST

FUTURE ORACLE
-> FORBIDDEN
~~~

This correction is applied identically to every policy and every domain.

It does not tune P-OQSC, add a favorable threshold, or alter the hidden holdout after reveal. It removes a scorer contradiction before benchmark materialization.

## Revised primary vector

Primary reporting remains non-scalar:

~~~text
(PSE_live, PD_live, AE_live, OIW, RL, MISSED_REOPEN, BER)
~~~

where PSE/PD use only obligations that were already live/reachable in the current episode.

## Claim ceiling

Passing this benchmark can establish at most prospective internal stopping competence on the declared generated trace families.

It cannot establish that the scorer knows all future obligations or that a current operational stop is future-proof.
