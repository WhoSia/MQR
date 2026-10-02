# MQR-4.48 — Defeat-Route Ontology Constitution Court

Status: **CLOSED / B+C+D+E+F+G / A REJECTED-AS-ROUTE-PRIMITIVE / H REJECTED / I REJECTED / DROCR+RIW+DCL+RAG+RSMR+CTL+CEE+HDR+RRL+RCAE / VERSIONED-CONTENT-SENSITIVE / HIDDEN-ROUTE-REOPENABLE / MAIN-ONLY**

## Formal stage name

**MQR-4.48 — Defeat-Route Ontology Constitution Court, Route-Identity Nonuniqueness, Split/Merge Gerrymandering, Coverage-Equivalence Failure, Hidden-Route Discovery, Route-Ancestry Entanglement, Defeat-Class Revision & Whether Separator Adequacy Can Be Audited When the Defeat Routes Used as the Coverage Basis Are Themselves Contestable**

## Verdict

MQR-4.48 rejects the assumption that a declared defeat route is a stable coverage primitive merely because it has a name, a count or a position in a coverage matrix.

~~~text
ROUTE LABEL != ROUTE IDENTITY
ROUTE COUNT != DEFEAT-CONTENT COUNT
ROUTE SPLIT != NEW DEFEAT CAPACITY
ROUTE MERGE != COVERAGE DISCHARGE
EQUAL COVERAGE FRACTIONS != COVERAGE EQUIVALENCE
~~~

The positive result is narrower:

~~~text
DROCR Defeat-Route Ontology Constitution Receipt
+ RIW Route-Identity Witness
+ DCL Defeat-Content Ledger
+ RAG Route-Ancestry Graph
+ RSMR Route Split/Merge Receipt
+ CTL Coverage-Transport Ledger
+ CEE Coverage-Equivalence Envelope
+ HDR Hidden-Route Discovery Receipt
+ RRL Route Residue Ledger
+ RCAE Route-Constitution Admissibility Envelope
------------------------------------------------
VERSIONED, CONTENT-SENSITIVE
SEPARATOR ADEQUACY
WITHOUT A FINAL DEFEAT-ROUTE ONTOLOGY
~~~

## Frozen branch verdicts

- **A ROUTE-PRIMITIVE — REJECTED.** Route labels and counts are not sufficient coverage primitives.
- **B WITNESS-RELATIONAL — PASS.** Cross-version route identity requires explicit defeat-content and ancestry witnesses.
- **C SPLIT-MERGE-AWARE — PASS.** Route cardinality change is separated from defeat-content change.
- **D ANCESTRY-AWARE — PASS.** Nominal route plurality can collapse under shared load-bearing ancestry.
- **E COVERAGE-TRANSPORT — PASS.** Prior coverage may survive ontology revision where defeat content is explicitly preserved.
- **F HIDDEN-ROUTE-REOPENABLE — PASS.** Newly discovered defeat content or route structure reopens affected adequacy.
- **G REVISION-AWARE — PASS.** Loss-bearing or noncommuting route revision remains explicit and reopenable.
- **H ROUTE-CLOSURE — REJECTED.** Stable finite route ontologies do not certify the complete defeat space.
- **I COVERAGE-FATAL — REJECTED.** Route contestability does not make separator adequacy impossible; scoped versioned coverage survives.

## Internal novelty kill

MQR-2.41-D already established that registered failure vocabularies can be overfit and vulnerability can migrate outside the known route ontology.

MQR-3.39 and MQR-3.136 already established open-set defeat, fresh noncommon defeat exposure, challenge-generator exteriority and unknown-route reserve.

MQR-4.45 already established generic ontology revision, split/merge transport, same-label drift, different-label aliasing and noncommuting revision reopening.

MQR-4.47 already established that raw probe count is not defeat-route coverage.

Therefore MQR-4.48 claims no novelty for fault taxonomies, route-vocabulary incompleteness, ontology revision or split/merge in the abstract.

The residual problem is:

~~~text
WHEN DEFEAT-ROUTE COVERAGE
IS THE BASIS OF SEPARATOR ADEQUACY,
HOW CAN THAT COVERAGE SURVIVE
CONTESTABLE ROUTE INDIVIDUATION
AND ROUTE-ONTOLOGY REVISION?
~~~

## Route identity

A route name is not an identity primitive.

Same-label drift is executable:

~~~text
O1: r -> {x}
O2: r -> {x,y}

same label
different declared defeat content
-> no automatic route identity
~~~

Different-label alias is also executable:

~~~text
O1: old -> {x}
O2: new -> {x}

preserved content + witness
-> local coverage transport allowed
~~~

## Split gerrymandering

One route can be split into many names without adding defeat content:

~~~text
source routes = 1
target routes = 5
source defeat content = 1
target defeat content = 1
~~~

v0.15 separately detects duplicated target content and ancestry collapse.

Thus:

~~~text
1 ROUTE -> 5 ROUTE NAMES
!=
5 INDEPENDENT DEFEAT ROUTES
~~~

## Split undertransport and positive refinement

For:

~~~text
r:{x,y}
->
rx:{x}
ry:{y}
~~~

a witness for x alone produces:

~~~text
HOLD_COVERAGE_TRANSPORT
~~~

Witnesses preserving both x and y produce:

~~~text
AUTHORIZED_CONTENT_PRESERVING_TRANSPORT
~~~

This is the positive control against the claim that every route revision destroys prior adequacy.

## Merge laundering

Two source routes:

~~~text
rx:{x}
ry:{y}
~~~

may be merged as:

~~~text
rxy:{x,y}
~~~

but one witness for x cannot silently discharge y.

The executable court records:

~~~text
route.coverage_collapse_detected=YES
route.coverage_authority=HOLD_COVERAGE_COLLAPSE
~~~

A provenance-complete x+y merge is transportable.

## Coverage-equivalence failure

Two route ontologies may have equal route counts and equal coverage fractions while preserving different defeat content.

The executable equal-count pair holds:

~~~text
source_route_count = 2
target_route_count = 2
~~~

constant while one case earns content-preserving transport and the other fails coverage transport.

Therefore:

~~~text
EQUAL ROUTE COUNT
OR
EQUAL COVERAGE FRACTION
!=
COVERAGE EQUIVALENCE
~~~

## Route ancestry

Route count and route ancestry count are separated.

Two named routes with one declared load-bearing ancestry yield:

~~~text
route.ancestry_entanglement=YES
HOLD_ROUTE_ANCESTRY_ENTANGLEMENT
~~~

This does not prove the routes metaphysically identical. It blocks the stronger inference from nominal plurality to independent defeat geometry.

## Hidden-route discovery

A new route can be:
- novel defeat content;
- refinement of an existing route;
- merge correction;
- previously unmapped content;
- ancestry revelation;
- unresolved.

Novel or previously unmapped defeat content yields:

~~~text
REOPEN_HIDDEN_NOVEL_CONTENT
~~~

A refinement without novel content yields:

~~~text
REOPEN_HIDDEN_ROUTE_REVISION
~~~

This reopening is local to the affected adequacy scope.

The court explicitly rejects:

~~~text
NEW HIDDEN ROUTE
->
ALL PRIOR SCOPED RESULTS WERE FALSE
~~~

## Revision path conflict

When direct and composed route-ontology revisions give different coverage states:

~~~text
DIRECT != COMPOSED
-> REOPEN_REVISION_PATH_CONFLICT
~~~

No revision path is promoted to a truth oracle by default.

## Finite stability

Several route revisions can preserve coverage.

This may earn local, version-relative robustness.

It never changes:

~~~text
route.current_route_ontology_complete=NO
route.future_defeat_space_closed=NO
~~~

## Real-Language v0.15

Canonical surface:
- Rust: `language/real/src/route_v15.rs` / `real-v15-route`
- independent relational evaluator: `language/real/prolog/route_v15.pl`
- Lean: `language/real/lean/MQR/RouteOntology.lean`
- constitution: `language/real/V15-ROUTE-ONTOLOGY.md`

Hard guards:

~~~text
route.current_route_ontology_complete=NO
route.future_defeat_space_closed=NO
route.route_count_truth_oracle=NO
route.route_label_identity_oracle=NO
route.coverage_fraction_truth_oracle=NO
route.revision_path_truth_oracle=NO
route.guidance_mode=VERSIONED_DEFEAT_CONTENT_COVERAGE
~~~

## Formal boundary

Lean proves with empty axiom ancestry:
- equal route counts do not imply equal defeat content;
- equal coverage fractions do not imply coverage equivalence;
- splitting one route does not create new defeat content;
- merging routes does not discharge uncovered predecessor content;
- same route label does not guarantee route identity;
- different route labels can preserve declared defeat content;
- content-preserving refinement can preserve local coverage;
- hidden-route discovery can reopen locally without globally negating prior scoped results;
- repeated finite route stability does not imply future defeat-space closure.

The theorem family is independently replayed with pinned lean4export + nanoda.

## Literature pressure and novelty ceiling

Post-preseal literature pressure included:
- Kuhn on fault classes and detection-condition hierarchies;
- Weyuker on test adequacy and implicit error-model assumptions;
- mutation testing and mutant subsumption/redundancy;
- Fraser & Walkinshaw on behavioural adequacy;
- Gohar et al. on extensible, overlapping defeater taxonomies;
- Bowker & Star on consequential classification systems;
- generic ontology/schema evolution work.

The surviving candidate contribution is their constitutional specialization around **coverage authority across versioned, contestable defeat-route ontologies**.

## Hilbert-24 methodological analogy

Hilbert's unpublished twenty-fourth problem asks for criteria of proof simplicity and a general theory of proof methods.

MQR-4.48 is not a solution, extension or direct instance of Hilbert's mathematical problem.

The methodological analogy is narrower but substantive:

~~~text
OBJECT-LEVEL SUCCESS
->
CRITERIA FOR METHODS
->
THE CRITERIA / METHOD CLASSES
THEMSELVES BECOME FORMAL OBJECTS
~~~

Hilbert-24 asks how proof methods should be compared and organized.

MQR-4.48 asks how defeat methods/routes should be individuated, refined, merged and compared before coverage over those routes can carry scientific authority.

The shared move is meta-methodological constitution; the domains and target notions are different.

## Pre-closure executable checkpoint

Dedicated and integrated pre-closure validation surfaces passed:

~~~text
36228254762  MQR-4.48/Court                 SUCCESS
36228256863  MQR-4.48/Lean+nanoda           SUCCESS
36228319410  Real-Language/CI                SUCCESS
36228340275  Real-Language/Lean+nanoda       SUCCESS
~~~

The final same-head seal reruns all four surfaces together.

## Stop-rule audit

- same-label drift executable: PASS
- different-label alias executable: PASS
- route split count inflation executable: PASS
- split coverage undertransport executable: PASS
- content-preserving refinement positive control: PASS
- merge coverage laundering executable: PASS
- provenance-preserving merge positive control: PASS
- equal-count coverage inequivalence executable: PASS
- route ancestry entanglement executable: PASS
- hidden novel route reopening executable: PASS
- hidden refinement reopening executable: PASS
- direct/composed route revision conflict executable: PASS
- finite stable revision remains non-closure: PASS
- Rust-Prolog concordance: PASS
- Lean axiom ancestry: EMPTY
- independent nanoda replay: PASS
- literature contacted after preseal: PASS
- route ontology completeness disabled: PASS
- future defeat-space closure disabled: PASS
- main-only policy: REQUIRED FOR FINAL SEAL

## Closure thesis

~~~text
A COVERAGE CLAIM
IS ONLY AS STABLE
AS THE DEFEAT DISTINCTIONS
IT ACTUALLY PRESERVES.

COUNTING MORE ROUTES
DOES NOT CREATE
MORE WAYS TO BE WRONG.

MERGING ROUTES
DOES NOT ERASE
UNTESTED WAYS TO BE WRONG.

ROUTE NAMES MAY CHANGE
WHILE DEFEAT CONTENT PERSISTS,
AND ROUTE NAMES MAY PERSIST
WHILE DEFEAT CONTENT CHANGES.

THEREFORE
SEPARATOR ADEQUACY
MUST TRANSPORT THROUGH
DEFEAT CONTENT,
ANCESTRY,
AND VERSIONED REVISION RECEIPTS.

WHEN A NEW WAY TO FAIL
BECOMES VISIBLE,
REOPEN THE AFFECTED CLAIM.

DO NOT INVENT
A FINAL TAXONOMY OF ERROR.
~~~
