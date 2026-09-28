# Real-Language v0.19 — Naturalistic Trace / Authority-Mode Boundary

Status: EXECUTABLE-CANDIDATE / MQR-4.52 / NATURALISTIC-TRACE / PARTIAL-IDENTIFICATION / MODE-RELATIVE / REALSTOP-0.18-REVISION

## Why v0.19 exists

MQR-4.51 calibrated the timing of a binary STOP action on generated traces.

MQR-4.52 naturalistic reconstruction exposes two representation failures that are logically prior to asking whether `lambda=1` predicts well:

1. one checkpoint is not a domain-invariant scientific unit;
2. stopping a claim, stopping evidence acquisition, authorizing action, handing off inquiry and archiving a programme are distinct state transitions.

Therefore v0.19 does not retune v0.18. It represents the richer state that v0.18 projects away.

## Grammar

~~~text
REALTRACE 0.19
id <id>
source_cutoff <YYYY-MM-DD>
mapping <EXACT|BOUNDED|PROXY|UNKNOWN>
claim <OPEN|RESTRICTED|FROZEN>
probe <ACTIVE|PAUSED|HANDOFF|ARCHIVED>
use <NONE|PROVISIONAL|AUTHORIZED>
live_obligation <CLEAR|LIVE|BOUNDED|UNKNOWN>
criterion <AGREE|DISAGREE|UNKNOWN>
break <NONE|WORLD_CONTACT|DECISION_CONTRACT|PATH_CONFLICT>
projection <UNIQUE|MULTI_MODE|NONE>
granularity <REGULAR|IRREGULAR|UNKNOWN>
stop_window <IDENTIFIED|INTERVAL|LEFT_CENSORED|RIGHT_CENSORED|NONIDENTIFIABLE>
historical_action <CONTINUE_PROBING|CLAIM_FREEZE|PROVISIONAL_USE|ARCHIVE|HANDOFF|REOPEN>
END
~~~

## Core semantics

Authority is a vector, not a bit:

~~~text
A_t =
(
  claim authority,
  probe allocation,
  use/action authority,
  live obligation state,
  criterion state,
  reopening state
)
~~~

A frozen claim may coexist with active probes.

A provisional action may be licensed while mechanistic inquiry remains open.

A programme may be archived without a truth declaration.

A later world-contact break may reopen one coordinate without globally negating all others.

## Naturalistic admission

A checkpoint is primary-transport admissible only if load-bearing coordinates are source-supported as EXACT or BOUNDED and neither live-obligation nor criterion state is UNKNOWN.

PROXY and UNKNOWN remain representable but cannot silently earn primary transport authority.

## Partial identification

Naturalistic inquiry generally identifies a stop window rather than a unique true instant.

~~~text
IDENTIFIED / INTERVAL / LEFT_CENSORED /
RIGHT_CENSORED / NONIDENTIFIABLE
~~~

The language never infers a unique stop time merely because a finite history is available.

## Binary projection audit

~~~text
projection = MULTI_MODE or NONE
->
binary_projection_loss = YES
~~~

This is not an automatic scientific failure. It is a failure of the binary STOP representation to preserve the authority state.

## Event-count lag audit

~~~text
granularity = IRREGULAR
->
fixed_event_lag_transport = REJECT
~~~

This rejects transport of a fixed *event-count* confirmation lag. It does not imply that all confirmation requirements are useless. A later stage may investigate invariant coordinates such as information gain, unresolved burden, independent ancestry, decision loss, or physical-time/resource bounds.

## Anti-Popper boundary

~~~text
POPPERIAN MASTER SEMANTICS = REJECT
WORLD CONTACT NEGATIVE ONLY = NO
~~~

World contact includes positive convergence, intervention success, calibration, instrument failure, representation change, independent replication, action-relevant transport and other authority-changing encounters.

Falsification remains one defeat route, not the ontology of science.

## Naturalistic 4.52 result boundary

The first frozen naturalistic pool contains:
- 7 PRIMARY cases;
- 1 SENSITIVITY case;
- 1 REJECTED programme-level candidate;
- 5 PRIMARY cases with source-supported identified/bounded claim-freeze windows;
- 6/7 PRIMARY cases whose inquiry state is multi-mode rather than faithfully binary;
- 2 cases where a unique stopping window is contract-dependent or right-censored.

Raw OQSC and lag-1 produce no definite PSE/OIW on the five identified claim-freeze windows.

This does **not** externally validate either rule.

The lag-1 policy is non-invariant to inert checkpoint refinement in every primary case with an eligible episode in the frozen reconstruction.

Therefore:

~~~text
CLAIM-FREEZE COMPATIBILITY = PARTIAL
BINARY NATURALISTIC STOP ONTOLOGY = FAIL
FIXED EVENT-COUNT LAG TRANSPORT = REJECT
PROSPECTIVE EXTERNAL CALIBRATION = NOT ESTABLISHED
~~~

## Canonical guards

~~~text
trace.unique_stop_time_inferred=NO
trace.historical_action_truth_oracle=NO
trace.naturalistic_retuning_lambda=NO
trace.prospective_external_validation=NO
trace.popperian_master_semantics=REJECT
trace.world_contact_negative_only=NO
trace.guidance_mode=MODE_RELATIVE_REOPENABLE_AUTHORITY
~~~

## Philosophical ceiling

v0.19 supports an executable thesis weaker than a final metaphysics but stronger than falsification-centered bookkeeping:

~~~text
SCIENTIFIC AUTHORITY IS
A MODE-RELATIVE,
WORLD-COUPLED,
REOPENABLE CONTROL STATE

OVER CLAIMS,
PROBES,
USES,
DISTINCTIONS,
FAILURES,
AND RESOURCE FLOWS.
~~~

This is not yet a universal theory of science. It is the representation that survived the first naturalistic attack better than a binary STOP ontology.
