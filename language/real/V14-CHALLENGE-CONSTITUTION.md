# Real-Language v0.14 — Translation-Challenge Constitution

Status: EXECUTABLE / MQR-4.47 CLOSED / ROUTE-COVERAGE / ANCESTRY-AWARE / CAPTURE-SENSITIVE / EXPANSION-REOPENABLE

## Boundary

MQR-4.46 allowed a frozen world-facing challenge to narrow a Correspondence Admissible Set (CAS), while refusing correspondence closure.

MQR-4.47 moves one level upstream: a world-facing probe does not gain separator-selection authority merely by touching the world.

v0.14 evaluates the constitution of the finite separator family used to narrow a specific translation CAS.

## Canonical objects

- TCCR — Translation-Challenge Constitution Receipt
- SFR — Separator Family Registry
- DRCM — Defeat-Route Coverage Matrix
- PAG — Probe-Ancestry Graph
- SSR — Separator-Selection Receipt
- DCR — Discriminator Capture Receipt
- CER — Challenge Expansion Receipt
- CRL — Challenge Residue Ledger
- SAE — Separator Admissibility Envelope

## Core rule

~~~text
WORLD-FACING != SELECTION-AUTHORIZED
PROBE COUNT != ROUTE COVERAGE
PROBE COUNT != ANCESTRY INDEPENDENCE
FINITE COVERAGE != CHALLENGE-SPACE COMPLETENESS
~~~

## Grammar

~~~text
REALCHALLENGE 0.14
id <id>
claim_scope <scope>
candidate_relations <relation+...>
selector <id> <ancestry>
selection_timing <PRESEALED|POST_OUTCOME>
selection_rule <id> <ancestry> <INDEPENDENT|INCUMBENT_DEFINED|UNRESOLVED>
route <id>
probe <id> <ancestry> <SELECTED|UNSELECTED> <WORLD_FACING|INTERNAL> <relation+...>
covers <probe> <route>
score_source <probe> <INDEPENDENT|CANDIDATE_DERIVED|STANDARD_DERIVED>
relevance_source <probe> <INDEPENDENT|CANDIDATE_DERIVED|STANDARD_DERIVED>
expansion <id> <relation+...>
authorize_...
END
~~~

## Selection surface

The evaluator distinguishes:
- all registered probes;
- selected probes;
- selected world-facing probes;
- ancestry classes among selected world-facing probes.

A registered family may contain an omitted world-facing counterprobe. If a selected narrowing is disjoint from a registered but unselected counterprobe that remained compatible with the pre-challenge CAS, the court reopens for selection bias.

## Defeat-route coverage

Route coverage is computed from selected world-facing probes only.

~~~text
NAMED PROBE MULTIPLICITY
!=
DECLARED DEFEAT-ROUTE COVERAGE
~~~

The route ontology remains declaration-relative. Complete declared route coverage never sets challenge.current_family_complete=YES.

## Discriminator capture

The executable v0.14 capture predicate is deliberately narrow:
- INCUMBENT_DEFINED selection rule;
- CANDIDATE_DERIVED relevance for a selected world-facing probe;
- CANDIDATE_DERIVED scoring for a selected world-facing probe.

These are sufficient capture witnesses for the court, not a complete theory of test bias.

## Expansion

After the selected family produces CAS_after, each declared expansion is applied as additional discriminatory support.

A disjoint expansion produces:

~~~text
REOPEN_EXPANSION_CONFLICT
~~~

Stable finite expansions may earn family-relative robustness, but never future challenge-space closure.

## Canonical authority states

~~~text
AUTHORIZED_PROVISIONAL_NARROWING
ADMISSIBLE_NO_NARROWING
HOLD_POST_OUTCOME_SELECTION
HOLD_DISCRIMINATOR_CAPTURE
REOPEN_OMITTED_COUNTERPROBE
HOLD_NO_WORLD_FACING
HOLD_ROUTE_COVERAGE
HOLD_COMMON_ANCESTRY
REOPEN_EXPANSION_CONFLICT
REOPEN_SELECTED_CONFLICT
~~~

These are governance states, not truth values.

## Hard guards

~~~text
challenge.current_family_complete=NO
challenge.future_challenge_space_closed=NO
challenge.probe_count_truth_oracle=NO
challenge.externality_truth_oracle=NO
challenge.cost_truth_oracle=NO
challenge.selection_rule_truth_oracle=NO
challenge.guidance_mode=CONSTITUTED_REOPENABLE_SEPARATOR_AUTHORITY
~~~

## Implementation

- canonical evaluator: Rust `src/challenge_v14.rs` / `real-v14-challenge`
- independent relational evaluator: Prolog `prolog/challenge_v14.pl`
- formal boundary: Lean `lean/MQR/Challenge.lean`

Rust–Prolog concordance is evidence about the declared receipt semantics only.

## Novelty ceiling

v0.14 does not re-claim challenge-generator exteriority, challenge admission, resource allocation, severe testing, triangulation, independent evidence, researcher degrees of freedom, multiverse analysis, adaptive holdout validity, or test-suite adequacy.

Its narrow target is the constitutional authority of the separator packet that directly narrows a translation CAS.


## Final closure boundary

MQR-4.47 closes only the declared separator-family authority problem.

~~~text
WORLD-FACING != SELECTION-AUTHORIZED
REGISTERED FAMILY != SELECTED PACKET
PROBE COUNT != DEFEAT-ROUTE COVERAGE
PROBE COUNT != ANCESTRY INDEPENDENCE
DECLARED COVERAGE COMPLETE != CHALLENGE-SPACE COMPLETE
POST-OUTCOME SELECTION -> HOLD
CANDIDATE-DERIVED RELEVANCE/SCORE -> CAPTURE HOLD
OMITTED REGISTERED COUNTERPROBE -> REOPEN
CHALLENGE EXPANSION CONFLICT -> REOPEN
REPEATED FINITE STABILITY != FUTURE CLOSURE
CURRENT FAMILY COMPLETE = NO
FUTURE CHALLENGE SPACE CLOSED = NO
~~~

The exact final same-head commit and workflow receipts are recorded in the external Research OS closure receipt so writing those identifiers does not mutate the sealed Git head.

<!-- mqr-4.47-final-same-head-seal -->
