# Real-Language v0.13 — Contestable Burden-Translation Authority

Status: EXECUTABLE / MQR-4.46 CLOSED / SET-VALUED / ANCESTRY-AWARE / STANDARD-AUDITED / OPEN-META

## Boundary

MQR-4.45 made burden transport typed and loss-aware but still consumed declared BTR edges.

MQR-4.46 asks what authority those edges have when the mapping witness, adjudicator, standard or meta-standard is itself contestable.

v0.13 evaluates a Translation-Authority Receipt (TAR). It does not infer unique metaphysical correspondence between source and target burden concepts.

## Canonical objects

- TAR — Translation-Authority Receipt
- MWG — Mapping-Witness Graph
- AIE — Adjudicator Independence Envelope
- SCR — Standard Capture Receipt
- CAS — Correspondence Admissible Set
- MCR — Mapping-Conflict Receipt
- TCP — Translation Challenge Packet
- MTDG — Meta-Translation Dependency Graph
- MRB — Meta-Regress Boundary

## Core rule

```text
VALID BTR SYNTAX
!=
EARNED BTR AUTHORITY
```

Authority depends on the declared provenance and contestability of the witness process.

## Grammar

```text
REALMAPAUTH 0.13
id <id>
claim_scope <scope>
source_ontology <id>
target_ontology <id>
candidate_relation <EXACT|REFINE|MERGE|OVERLAP|DISJOINT|UNMAPPED>
proposer <id> <ancestry>
adjudicator <id> <ancestry> <INTERNAL|EXTERNAL|MIXED>
standard <id> <ancestry> <PRESEALED|POST_OUTCOME|INHERITED>
witness <id> <standard> <adjudicator> <DIRECT|META> <relation+...>
challenge <id> <INTERNAL|WORLD_FACING> <relation+...>
meta_dep <from-node> <to-node>
meta_anchor <node> <WORLD_FACING|DECLARED>
force_singleton <YES|NO>
authorize_...
END
```

## Correspondence admissible set

Every witness/challenge contributes a set of relations compatible with that declared evidence item.

v0.13 computes:

```text
CAS = intersection(all declared support sets)
```

If `|CAS| > 1`, the mapping remains set-valued.

```text
MULTIPLE SURVIVING RELATIONS
!=
PARSER FAILURE
```

Forcing a singleton when the declared surface remains non-singleton is an authority overclaim.

## Independence

Named adjudicator plurality is separated from ancestry plurality.

```text
ADJUDICATOR COUNT
!=
ADJUDICATOR ANCESTRY COUNT
```

Self-certification is detected when the proposer and an adjudicator share identity or declared load-bearing ancestry.

Common-mode adjudication is detected when several adjudicators collapse to fewer declared ancestries.

Neither externality nor plurality is a truth oracle.

## Standard capture

A standard is capture-risk when:
- it was declared POST_OUTCOME; or
- it shares the proposer's declared ancestry.

This is a deliberately narrow executable criterion, not a complete sociology of standards.

The hard doctrine is:

```text
STANDARDIZED != TRUE
PRESTIGE != TRUE
RECENCY != TRUE
```

## World-facing narrowing

Let CAS_pre be the relation set supported before WORLD_FACING challenges.

A frozen world-facing challenge is a separator when:

```text
0 < |CAS_final| < |CAS_pre|
```

This may earn local narrowing of mapping authority.

It does not prove unique world correspondence beyond the declared challenge family.

## Direct/meta conflict

DIRECT and META witness layers are audited independently.

If their layer-wise intersections are disjoint:

```text
DIRECT / META CONFLICT
-> REOPEN
```

No layer is made an oracle by default.

## Meta-regress

MTDG records declared meta-dependencies.

A cycle is not independent support:

```text
META CYCLE != AUTHORITY ROOT
```

A finite acyclic chain ending at an unanchored node is represented as explicit `meta_debt`.

This permits operational stopping with an unresolved receipt rather than pretending either:
- an infinite regress has been completed; or
- a final meta-standard exists.

## Canonical authority states

```text
EARNED_PROVISIONAL
SET_VALUED_PROVISIONAL
HOLD_SELF_CERTIFIED
HOLD_COMMON_ANCESTRY
HOLD_STANDARD_CAPTURE
HOLD_META_DEBT
HOLD_CANDIDATE_UNSUPPORTED
CONTESTED_NO_COMMON_RELATION
REOPEN_FORCED_SINGLETON
REOPEN_META_CYCLE
REOPEN_DIRECT_META_CONFLICT
```

These are governance states, not truth values.

## Hard guards

```text
authority.unique_world_correspondence_inferred=NO
authority.future_translation_closed=NO
authority.consensus_truth_oracle=NO
authority.standard_truth_oracle=NO
authority.externality_truth_oracle=NO
authority.meta_cycle_authority=NO
authority.guidance_mode=CONTESTABLE_SET_VALUED_TRANSLATION_AUTHORITY
```

## Implementation

- canonical evaluator: Rust `src/map_authority_v13.rs` / `real-v13-map-authority`
- independent relational evaluator: Prolog `prolog/map_authority_v13.pl`
- formal boundary: Lean `lean/MQR/MapAuthority.lean`

Rust–Prolog concordance is implementation-diversity evidence over the declared receipt surface only.


## Post-preseal novelty boundary

MQR-4.46 explicitly inherits and does not re-claim:
- MQR-3.171 translation-loss and residual-disagreement preservation;
- MQR-3.172 alignment-set audit and the rule that one admissible map is not the unique correct map;
- theoretical-equivalence pluralism;
- ontology-matching uncertainty;
- scientific expert dependence and disagreement;
- standardization, calibration networks and boundary-object coordination.

The live v0.13 contribution candidate is narrower:

```text
WHO MAY AUTHORIZE MEMBERSHIP IN THE ADMISSIBLE MAP SET?
```

Accordingly v0.13 audits:
- proposer/adjudicator ancestry;
- common-mode adjudication;
- standard timing and proposer dependence;
- set-valued correspondence;
- world-facing narrowing;
- direct/meta disagreement;
- meta-dependency cycles;
- finite unresolved meta-debt.

This is a governance layer over mapping claims, not a new ontology matcher and not a final theory of semantic correspondence.


## Final closure boundary

MQR-4.46 closes only the declared mapping-authority problem.

~~~text
DECLARED BTR EDGE != EARNED TRANSLATION AUTHORITY
ADJUDICATOR COUNT != ANCESTRY INDEPENDENCE
SELF-CERTIFICATION != INDEPENDENT WITNESS
STANDARDIZED != TRUE
NON-SINGLETON CAS MUST REMAIN NON-SINGLETON
FORCED SINGLETON -> REOPEN
WORLD-FACING CHALLENGE MAY NARROW CAS, NOT CLOSE CORRESPONDENCE
DIRECT / META CONFLICT -> REOPEN
META CYCLE != INDEPENDENT ROOT
FINITE UNRESOLVED META-DEPENDENCY -> EXPLICIT META-DEBT
UNIQUE WORLD CORRESPONDENCE = NOT INFERRED
FUTURE TRANSLATION CLOSURE = NO
~~~

The exact final same-head commit and workflow receipts are kept in the external Research OS closure receipt so recording those identifiers does not mutate the sealed Git head.

<!-- mqr-4.46-final-same-head-seal -->
