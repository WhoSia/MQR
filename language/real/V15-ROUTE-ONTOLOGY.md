# Real-Language v0.15 — Defeat-Route Ontology Constitution

Status: EXECUTABLE CANDIDATE / MQR-4.48 / CONTENT-SENSITIVE / SPLIT-MERGE-AWARE / ANCESTRY-AWARE / HIDDEN-ROUTE-REOPENABLE

## Boundary

MQR-4.47 replaced raw probe multiplicity with declared defeat-route coverage.

MQR-4.48 moves one level upstream: a defeat route is not a primitive merely because it has a name in the coverage matrix.

v0.15 evaluates whether coverage authority survives changes in the ontology used to individuate defeat routes.

## Canonical objects

- DROCR — Defeat-Route Ontology Constitution Receipt
- RIW — Route-Identity Witness
- DCL — Defeat-Content Ledger
- RAG — Route-Ancestry Graph
- RSMR — Route Split/Merge Receipt
- CTL — Coverage-Transport Ledger
- CEE — Coverage-Equivalence Envelope
- HDR — Hidden-Route Discovery Receipt
- RRL — Route Residue Ledger
- RCAE — Route-Constitution Admissibility Envelope

## Core rule

~~~text
ROUTE LABEL != ROUTE IDENTITY
ROUTE COUNT != DEFEAT-CONTENT COUNT
ROUTE SPLIT != NEW DEFEAT CAPACITY
ROUTE MERGE != COVERAGE DISCHARGE
EQUAL COVERAGE FRACTIONS != COVERAGE EQUIVALENCE
~~~

## Grammar

~~~text
REALROUTE 0.15
id <id>
claim_scope <scope>
source_ontology <id>
target_ontology <id>
content <id>
source_route <id> <ancestry> <content+...> <COVERED|UNCOVERED>
target_route <id> <ancestry> <content+...>
map <source+...> <EXACT|REFINE|MERGE|OVERLAP|DISJOINT|UNMAPPED> <target+...>
coverage_witness <source> <target> <content+...>
hidden_route <id> <NOVEL_ROUTE|REFINEMENT_OF_EXISTING|MERGE_CORRECTION|PREVIOUSLY_UNMAPPED_CONTENT|ANCESTRY_REVELATION|UNRESOLVED> <content+...>
path <id> <PASS|HOLD|REOPEN>
authorize_...
END
~~~

## Defeat-content semantics

Routes carry declaration-relative defeat content.

Cross-version coverage is evaluated over defeat content rather than route names or percentages.

A content-preserving refinement can transport coverage:

~~~text
r:{x,y}
->
r1:{x}
r2:{y}
~~~

only when coverage witnesses preserve both x and y.

A syntactically identical split with a witness for x alone cannot duplicate coverage onto y.

## Split / merge

v0.15 records split and merge counts but they have no truth authority.

Target routes with duplicate defeat-content signatures are explicitly marked as route duplication.

For MERGE, coverage collapse is detected when:
- source defeat content disappears from the target route surface; or
- covered source content is not preserved by the declared coverage witnesses.

## Coverage equivalence

The positive state requires:
- source route coverage complete on its declared content surface;
- target content surface equal to the source content surface;
- every target defeat content carried by explicit coverage witnesses;
- no coverage collapse;
- no ancestry-entanglement hold;
- no hidden-route or revision-path reopening.

Thus:

~~~text
EQUAL COUNTS / EQUAL FRACTIONS
!=
COVERAGE EQUIVALENCE
~~~

## Route ancestry

Named route plurality is separated from ancestry plurality.

If multiple routes collapse to fewer declared load-bearing ancestries, v0.15 marks route-ancestry entanglement.

This does not prove that the routes are identical; it blocks an inference from route plurality to independent defeat geometry.

## Hidden-route discovery

A hidden-route receipt is revision evidence.

- NOVEL_ROUTE / PREVIOUSLY_UNMAPPED_CONTENT can introduce new defeat content and reopen coverage.
- REFINEMENT_OF_EXISTING / MERGE_CORRECTION can reopen route constitution even without new content.
- ANCESTRY_REVELATION can alter independence geometry without changing route labels.

A hidden-route discovery reopens the affected coverage authority. It does not assert that every historical scoped result was false.

## Revision path

Multiple declared revision paths may disagree on coverage state.

~~~text
DIRECT != COMPOSED
-> REOPEN_REVISION_PATH_CONFLICT
~~~

No path is a truth oracle by default.

## Canonical authority states

~~~text
AUTHORIZED_CONTENT_PRESERVING_TRANSPORT
REOPEN_HIDDEN_NOVEL_CONTENT
REOPEN_HIDDEN_ROUTE_REVISION
REOPEN_REVISION_PATH_CONFLICT
HOLD_COVERAGE_COLLAPSE
HOLD_SOURCE_COVERAGE_INCOMPLETE
HOLD_COVERAGE_TRANSPORT
HOLD_CONTENT_SURFACE_CHANGE
HOLD_TARGET_COVERAGE_INCOMPLETE
HOLD_ROUTE_ANCESTRY_ENTANGLEMENT
HOLD_COVERAGE_INEQUIVALENT
~~~

These are governance states, not truth values.

## Hard guards

~~~text
route.current_route_ontology_complete=NO
route.future_defeat_space_closed=NO
route.route_count_truth_oracle=NO
route.route_label_identity_oracle=NO
route.coverage_fraction_truth_oracle=NO
route.revision_path_truth_oracle=NO
route.guidance_mode=VERSIONED_DEFEAT_CONTENT_COVERAGE
~~~

## Implementation

- canonical evaluator: Rust `src/route_v15.rs` / `real-v15-route`
- independent relational evaluator: Prolog `prolog/route_v15.pl`
- formal boundary: Lean `lean/MQR/RouteOntology.lean`

Rust–Prolog concordance is evidence about the declared receipt semantics only.

## Novelty ceiling

v0.15 does not re-claim fault models, fault-class hierarchies, mutation subsumption, test adequacy, defeater taxonomy, ontology evolution, classification non-neutrality, challenge-generator exteriority, or generic route-vocabulary incompleteness.

Its narrow target is **coverage authority across contestable, versioned defeat-route ontologies**.
