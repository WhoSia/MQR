# MQR-4.46 — Burden-Translation Authority Court

Status: **CLOSED / B+C+D+E+F+G / A REJECTED-AS-DECLARATION-SUFFICIENT / H REJECTED / I REJECTED / TAR+MWG+AIE+SCR+CAS+MCR+TCP+MTDG+MRB / CONTESTABLE-SET-VALUED / OPEN-META / MAIN-ONLY**

## Formal stage name

**MQR-4.46 — Burden-Translation Authority Court, Mapping-Witness Independence, Adjudicator Conflict, Standard Capture, Correspondence Underdetermination, Meta-Translation Regress & Whether Versioned Burden Transport Can Earn Scientific Authority When the Relation Used to Declare EXACT, REFINE, MERGE or OVERLAP Is Itself Contestable**

## Verdict

MQR-4.46 rejects the assumption that a typed burden-transport edge gains scientific authority merely by being declared, standardized, multiply endorsed or meta-validated.

~~~text
TAR  Translation-Authority Receipt
+ MWG Mapping-Witness Graph
+ AIE Adjudicator Independence Envelope
+ SCR Standard Capture Receipt
+ CAS Correspondence Admissible Set
+ MCR Mapping-Conflict Receipt
+ TCP Translation Challenge Packet
+ MTDG Meta-Translation Dependency Graph
+ MRB Meta-Regress Boundary
------------------------------------------------
CONTESTABLE, SET-VALUED, ANCESTRY-AWARE
BURDEN-TRANSLATION AUTHORITY
~~~

This can license a provisional BTR relation or a set of admissible BTR relations without asserting a unique metaphysical correspondence.

It does not license:

~~~text
VALID MAPPING SYNTAX -> EARNED AUTHORITY
ADJUDICATOR COUNT -> INDEPENDENCE
CONSENSUS -> UNIQUE CORRESPONDENCE
STANDARDIZATION -> TRUTH
EXTERNALITY -> TRUTH
META-VALIDATION -> FINAL FOUNDATION
CURRENT TAR PASS -> FUTURE TRANSLATION CLOSURE
~~~

## Frozen branch verdicts

- **A DECLARATION-SUFFICIENT — REJECTED.** A syntactically valid BTR edge has no automatic scientific authority.
- **B ANCESTRY-AWARE — PASS.** Mapping authority tracks proposer/adjudicator/standard ancestry.
- **C SET-VALUED — PASS.** Several mapping relations may remain jointly admissible.
- **D STANDARD-AUDITED — PASS.** Standards are provenance-bearing and contestable objects.
- **E WORLD-SEPARABLE — PASS.** Frozen world-facing challenges may narrow an admissible correspondence set.
- **F CONFLICT-LOCALIZED — PASS.** Adjudicator/standard/direct-meta conflict can be exposed without hidden winner selection.
- **G REGRESS-EXPLICIT — PASS.** Finite meta-dependency can terminate operationally with explicit unresolved meta-debt.
- **H META-ORACLE — REJECTED.** Higher-order translation does not automatically provide a final correspondence oracle.
- **I AUTHORITY-FATAL — REJECTED.** Contestable mapping relations do not destroy all cross-version governance; scoped provisional authority survives under declared conditions.

## Internal novelty kill

MQR-3.171 already established translation-loss, residual-disagreement preservation, and the non-neutrality of a shared vocabulary.

MQR-3.172 already established that one admissible map is not necessarily the unique correct map, that several defensible maps may preserve different distinctions, and that map-selection laundering must be audited.

Therefore MQR-4.46 claims no novelty for translation loss, multiple valid maps or alignment-set auditing in the abstract.

The residual question is:

~~~text
WHO OR WHAT AUTHORIZES
MEMBERSHIP IN THE ADMISSIBLE MAP SET?
~~~

## Mapping-witness independence

The executable court separates adjudicator count from adjudicator ancestry count.

A three-member panel whose members inherit one load-bearing ancestry does not acquire three independent evidential roots.

Likewise, a proposer that supplies and adjudicates its own decisive mapping witness is explicitly classified HOLD_SELF_CERTIFIED.

Self-coherence may be useful, but it does not manufacture independent confirmation.

## Correspondence Admissible Set

v0.13 preserves unresolved relation plurality.

~~~text
W1 supports {REFINE, OVERLAP}
W2 supports {REFINE, OVERLAP}

CAS = {REFINE, OVERLAP}
state = SET_VALUED_PROVISIONAL
~~~

Forcing a singleton on this surface produces REOPEN_FORCED_SINGLETON.

This is an authority rule for preserving unresolved scientific-governance correspondence, not a new ontology-matching algorithm.

## Competing standards

The same source/target pair may receive incompatible relation support under different standards.

~~~text
K1 -> EXACT
K2 -> OVERLAP
----------------
CAS = EMPTY
CONTESTED_NO_COMMON_RELATION
~~~

No default rule promotes the newest, external, prestigious or majority-supported standard.

## Standard capture

The executable Standard Capture Receipt marks two deliberately narrow but load-bearing failure modes:
- post-outcome standard revision;
- decisive standard sharing the proposer’s declared ancestry.

Hence STANDARDIZED != TRUE and POST-OUTCOME STANDARD REVISION != INDEPENDENT VALIDATION.

Absence of these two frozen capture witnesses does not prove a standard neutral.

## World-facing separator

Internal evidence may leave CAS_pre = {EXACT, OVERLAP}. A frozen world-facing challenge can narrow it to CAS_final = {OVERLAP}.

The court treats 0 < |CAS_final| < |CAS_pre| as locally earned discrimination.

It does not infer unique world correspondence because successor challenge families may reopen the mapping.

## Direct / meta conflict

DIRECT and META witness layers are evaluated separately.

If their surviving relation sets are disjoint:

~~~text
DIRECT ∩ META = EMPTY
-> REOPEN_DIRECT_META_CONFLICT
~~~

Neither layer is an oracle by default.

## Meta-translation regress

MQR-4.46 rejects both:
1. every mapping authority must terminate in a final unquestionable meta-standard;
2. without such a final standard, no mapping authority is possible.

MTDG records explicit meta-dependencies.

A cycle such as r -> K -> r yields REOPEN_META_CYCLE with authority.meta_cycle_authority=NO.

A finite acyclic chain whose terminal support remains unanchored is carried as HOLD_META_DEBT.

This is an operational stopping boundary with explicit unresolved debt, not metaphysical foundationalism.

## Real-Language v0.13

Canonical surface:
- Rust: language/real/src/map_authority_v13.rs / real-v13-map-authority
- independent relational evaluator: language/real/prolog/map_authority_v13.pl
- Lean: language/real/lean/MQR/MapAuthority.lean
- constitution: language/real/V13-TRANSLATION-AUTHORITY.md

Hard guards:

~~~text
authority.unique_world_correspondence_inferred=NO
authority.future_translation_closed=NO
authority.consensus_truth_oracle=NO
authority.standard_truth_oracle=NO
authority.externality_truth_oracle=NO
authority.meta_cycle_authority=NO
authority.guidance_mode=CONTESTABLE_SET_VALUED_TRANSLATION_AUTHORITY
~~~

## Formal boundary

Lean proves, with empty axiom ancestry:
- adjudicator count does not imply ancestry independence;
- self-certification adds no independent witness;
- one declared surface may leave multiple relation classes admissible;
- adjudicator consensus does not imply unique world correspondence;
- standard agreement does not create a truth oracle;
- cyclic meta-support does not create an independent root;
- a world-facing separator may narrow the candidate set without closing correspondence;
- finite unresolved meta-debt can remain explicit without a final oracle;
- current mapping authority does not imply future translation closure.

The theorem set is independently replayed through pinned lean4export + nanoda.

## Literature pressure and novelty ceiling

Post-preseal pressure places MQR-4.46 beside mature literatures on expert dependence/disagreement, scientific standards and calibration, boundary objects, theoretical-equivalence pluralism, ontology-matching uncertainty and evidential discordance.

The surviving candidate contribution is their constitutional recombination around scientific-search burden translation authority:

~~~text
MAPPING-WITNESS PROVENANCE
+ ADJUDICATOR ANCESTRY
+ STANDARD-CAPTURE AUDIT
+ SET-VALUED CORRESPONDENCE
+ WORLD-FACING NARROWING
+ DIRECT/META CONFLICT
+ META-CYCLE DETECTION
+ FINITE META-DEBT
------------------------------------------------
PROVISIONAL TRANSLATION AUTHORITY
WITHOUT A CORRESPONDENCE OR META ORACLE
~~~

## Executable / CI closure checkpoint

Common-head checkpoint: 55b331edb731677dd064695ab5b0379189d72e5d

All four validation surfaces passed at that same head:

~~~text
36215278890  MQR-4.46/Court             SUCCESS
36215278886  MQR-4.46/Lean+nanoda       SUCCESS
36215278851  Real-Language/CI            SUCCESS
36215278913  Real-Language/Lean+nanoda   SUCCESS
~~~

The final external Research OS receipt records the final same-head seal after doctrine/documentation promotion.

## Stop-rule audit

- self-certification executable: PASS
- adjudicator-count/common-ancestry collision executable: PASS
- independent adjudicator positive control: PASS
- competing-standard conflict executable: PASS
- set-valued CAS executable: PASS
- forced-singleton overclaim detected: PASS
- post-outcome standard capture executable: PASS
- world-facing CAS narrowing executable: PASS
- direct/meta conflict executable: PASS
- meta-cycle executable and denied authority: PASS
- finite unresolved meta-debt executable: PASS
- Rust-Prolog concordance: PASS
- Lean axiom ancestry: EMPTY
- independent nanoda replay: PASS
- literature contacted after preseal: PASS
- unique world correspondence inference disabled: PASS
- future translation closure disabled: PASS
- main-only policy: REQUIRED FOR FINAL SEAL

## Closure thesis

~~~text
A BURDEN-TRANSLATION EDGE
IS NOT AUTHORITATIVE
BECAUSE IT HAS A NAME,
A STANDARD,
A PANEL,
OR A META-STANDARD.

AUTHORITY CAN BE EARNED
ONLY AT THE DECLARED SCOPE
THROUGH AUDITABLE WITNESS PROVENANCE,
ANCESTRY-AWARE ADJUDICATION,
EXPLICIT ALTERNATIVE MAPPINGS,
CAPTURE-SENSITIVE STANDARDS,
AND REOPENABLE WORLD-FACING CHALLENGE.

WHEN CORRESPONDENCE REMAINS PLURAL,
KEEP IT PLURAL.

WHEN META-JUSTIFICATION RUNS OUT,
RECORD THE DEBT.

DO NOT INVENT A FINAL DICTIONARY.
~~~
