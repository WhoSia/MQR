# Real-Language v0.16 — Defeat-Content Constitution

Status: EXECUTABLE / MQR-4.49 CLOSED / ROLE-RELATIONAL / MECHANISM-MANIFESTATION-SEPARATED / COUNTERFACTUAL-QUOTIENT / EXPANSION-REOPENABLE

## Boundary

MQR-4.48 grounded route identity in declaration-relative defeat content.

MQR-4.49 moves one level upstream: defeat content is not a primitive merely because it has a name in a route ontology.

v0.16 evaluates whether defeat-role identity can survive content split/merge, mechanism/manifestation aliasing, common-cause dependence, representation change and challenge expansion.

## Canonical objects

- DCCR — Defeat-Content Constitution Receipt
- DIW — Defeat-Identity Witness
- MMM — Mechanism–Manifestation Matrix
- CDP — Counterfactual Defeat Profile
- CDEE — Counterfactual Defeat Equivalence Envelope
- CSMR — Content Split/Merge Receipt
- CCCG — Common-Cause Compression Graph
- CRDT — Cross-Representation Defeat Transport
- HCGR — Hidden-Content Genesis Receipt
- DCRL — Defeat-Content Residue Ledger
- DCAE — Defeat-Content Admissibility Envelope

## Core rule

~~~text
DEFEAT LABEL != DEFEAT IDENTITY
MECHANISM != MANIFESTATION
CONTENT COUNT != INDEPENDENT FAILURE DIMENSIONS
CONTENT SPLIT != NEW COUNTERFACTUAL DISTINCTION
CONTENT MERGE != COUNTERFACTUAL EQUIVALENCE
CURRENT COUNTERFACTUAL EQUIVALENCE != FUTURE EQUIVALENCE
~~~

## Grammar

~~~text
REALDEFEAT 0.16
id <id>
claim_scope <scope>
source_representation <id>
target_representation <id>
challenge <id>
source_content <id> <mechanism> <manifestation> <ancestry> <challenge+...>
target_content <id> <mechanism> <manifestation> <ancestry> <challenge+...>
map <source+...> <EXACT|REFINE|MERGE|OVERLAP|DISJOINT|UNMAPPED> <target+...>
role_witness <source> <target> <challenge+...>
hidden_content <id> <NOVEL_COUNTERFACTUAL_DISTINCTION|REFINEMENT_OF_EXISTING|MECHANISM_REASSIGNMENT|MANIFESTATION_REASSIGNMENT|COMMON_CAUSE_REVEAL|REPRESENTATION_ESCAPE|PREVIOUSLY_UNMAPPED|UNRESOLVED> <challenge+...>
expansion <id> <source-content> <target-content> <SAME|DISTINGUISHES>
path <id> <PASS|HOLD|REOPEN>
authorize_...
END
~~~

## Counterfactual defeat profile

For the declared challenge family Q:

~~~text
CDP_Q(d) = declared set of challenge-conditioned defeat consequences
~~~

Two mapped contents may be locally counterfactually equivalent when their CDPs coincide at the declared claim scope.

This earns only a local quotient:

~~~text
LOCAL CDP EQUIVALENCE
!=
WORLD-FUNDAMENTAL ERROR IDENTITY
~~~

## Mechanism / manifestation separation

v0.16 tracks mechanisms, manifestations and defeat roles separately.

One mechanism may generate multiple manifestations.
One manifestation may alias multiple mechanisms.
Neither cardinality is allowed to manufacture or erase defeat-role distinctions.

## Content split

A split with more target content names but no increase in distinct CDP profiles is flagged as:

~~~text
HOLD_SPLIT_WITHOUT_NEW_DISTINCTION
~~~

A refinement that introduces prospectively distinguishable CDP profiles while preserving the predecessor defeat role may earn:

~~~text
AUTHORIZED_COUNTERFACTUAL_REFINEMENT
~~~

## Content merge

A merge that fails to transport all predecessor challenge-conditioned defeat roles yields:

~~~text
HOLD_MERGE_DISTINCTION_LAUNDERING
~~~

A scope-local quotient merge may be authorized where every predecessor defeat consequence remains explicitly witnessed:

~~~text
AUTHORIZED_SCOPE_QUOTIENT_MERGE
~~~

The merged content is not thereby declared metaphysically identical to its predecessors.

## Common cause

Shared ancestry compresses independence:

~~~text
CONTENT PLURALITY
>
ANCESTRY PLURALITY
->
COMMON_CAUSE_COMPRESSION
~~~

This is not an identity theorem.
Two contents can share one cause and remain counterfactually distinct.

## Cross-representation defeat transport

Different labels, mechanisms or manifestations may still preserve the same claim-relative defeat role under explicit role witnesses.

Representation change is therefore neither an identity oracle nor a nonidentity oracle.

## Hidden content

A hidden-content receipt can reopen current constitution because of:
- novel counterfactual distinction;
- refinement;
- mechanism or manifestation reassignment;
- common-cause revelation;
- representation escape;
- previously unmapped defeat role.

Novel distinctions are separated from revisions of how an existing role is represented.

## Expansion

A pair currently equivalent under Q may become distinguishable under Q+.

~~~text
CURRENT CDP EQUIVALENCE
+ NEW DISTINGUISHING CHALLENGE
->
REOPEN_EXPANSION_BREAK
~~~

## Canonical authority states

~~~text
AUTHORIZED_LOCAL_DEFEAT_ROLE_TRANSPORT
AUTHORIZED_LOCAL_COUNTERFACTUAL_QUOTIENT
AUTHORIZED_COUNTERFACTUAL_REFINEMENT
AUTHORIZED_SCOPE_QUOTIENT_MERGE
HOLD_ROLE_DRIFT
HOLD_SPLIT_WITHOUT_NEW_DISTINCTION
HOLD_ROLE_TRANSPORT
HOLD_MERGE_DISTINCTION_LAUNDERING
HOLD_REPRESENTATION_COLLAPSE
REOPEN_EXPANSION_BREAK
REOPEN_HIDDEN_NOVEL_DISTINCTION
REOPEN_HIDDEN_CONTENT_REVISION
REOPEN_REVISION_PATH_CONFLICT
~~~

These are governance states, not truth values.

## Hard guards

~~~text
defeat.current_defeat_atoms_complete=NO
defeat.future_defeat_space_closed=NO
defeat.label_identity_oracle=NO
defeat.mechanism_identity_oracle=NO
defeat.manifestation_identity_oracle=NO
defeat.counterfactual_equivalence_truth_oracle=NO
defeat.representation_truth_oracle=NO
defeat.guidance_mode=REOPENABLE_COUNTERFACTUAL_DEFEAT_QUOTIENT
~~~

## Implementation

- canonical evaluator: Rust `src/defeat_v16.rs` / `real-v16-defeat`
- independent relational evaluator: Prolog `prolog/defeat_v16.pl`
- formal boundary: Lean `lean/MQR/DefeatContent.lean`

Rust–Prolog concordance is evidence about the declared receipt semantics only.

## Novelty ceiling

v0.16 does not re-claim causal mechanism individuation, interventionism, causal abstraction, exact transformation, compositional abstraction, causal representation learning, multiple realization, ontology split/merge, common-cause dependence, partition granularity or fault taxonomy.

Its narrow target is **route identity through reopenable, claim-relative defeat-role equivalence across changing content representations**.


## Final closure boundary

MQR-4.49 closes only the declared defeat-content constitution problem.

~~~text
DEFEAT LABEL != DEFEAT IDENTITY
MECHANISM != MANIFESTATION != DEFEAT ROLE
CONTENT COUNT != INDEPENDENT FAILURE DIMENSIONS
COUNTERFACTUALLY IDENTICAL SPLIT != NEW DEFEAT DISTINCTION
ROLE-PRESERVING REFINEMENT MAY EARN LOCAL AUTHORITY
MERGE REQUIRES PREDECESSOR ROLE PRESERVATION
COMMON CAUSE != CONTENT IDENTITY
LOCAL CDP EQUIVALENCE != WORLD IDENTITY
CHALLENGE EXPANSION MAY BREAK THE QUOTIENT
CROSS-REPRESENTATION ROLE TRANSPORT MAY PRESERVE LOCAL IDENTITY
HIDDEN CONTENT -> LOCAL REOPEN
CURRENT DEFEAT ATOMS COMPLETE = NO
FUTURE DEFEAT SPACE CLOSED = NO
~~~

The exact final same-head commit and workflow receipts are recorded in the external Research OS closure receipt so writing those identifiers does not mutate the sealed Git head.

<!-- mqr-4.49-final-same-head-seal -->
