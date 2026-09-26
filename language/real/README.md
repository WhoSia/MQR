# Real-Language / Real-Packet v0.4 proof boundary + v0.3 transport compatibility

Real-Language is MQR's active event-to-realist-authority language.

It compiles a scientific, methodological, or engineering event into a scoped authority packet while preserving open-world residue and successor vulnerability.

## Version boundary

### v0.2
Historical profile grammar:

- C/E/P/R authority gates
- W/N/I/T/D profile
- scalar projection OFF by default

v0.2 remains readable for archival reproducibility.

### v0.3
Transport grammar retained for canonical/historical compatibility:

- C/E/P/R authority gates
- W/N/I/D profile
- **legacy axis T is forbidden**
- transport is represented by a typed relation map
- lineage kind is explicit

### v0.4 — live proof-boundary lane

v0.4 adds explicit formal/empirical ancestry without replacing world contact:

- typed FORMAL / DEFINITION / MODEL / EMPIRICAL premises;
- FORMAL_ONLY / WORLD_DEPENDENT obligations;
- explicit dependency ancestry;
- CHECKED / UNCHECKED / REFUTED / NOT_APPLICABLE proof states;
- empirical authority ceilings;
- finite probe-class / internal-residue receipts;
- mechanical rejection of axiom laundering.

Canonical proof receipt:

`language/real/V04-PROOF-RECEIPT.md`

Canonical v0.4 proof run:

`36146576232`

The target Lean theorems have empty axiom ancestry and were independently rechecked by a pinned nanoda stack.

The first world-contact-bound v0.4 packet is:

`language/real/examples/mqr-4.36-fresh-fiber-pcra.real`

It permits PASS for the narrowly receipt-backed internal-residue claim, keeps open-world adequacy at HOLD, and records fresh NU3 sufficiency as FAIL.

Therefore:

```text
KERNEL_VERIFIED != WORLD_VERIFIED
FORMAL_CERTAINTY_CANNOT_LAUNDER_EMPIRICAL_UNCERTAINTY
ZERO_INTERNAL_RESIDUE != ZERO_OPEN_WORLD_RESIDUE
```

MQR-4.31 found that one T coordinate conflated:
1. transport target/component,
2. evaluability,
3. survival conditional on evaluation.

Therefore:

```text
legacy.profile.T = DEPRECATED
transport.mode = TYPED_RELATION_MAP
```

## Lineage kinds

Every v0.3 packet must declare exactly one:

- `RESEARCH_LAB`
- `ENGINEERING_DEVELOPMENT`
- `METHODOLOGY_DEVELOPMENT`
- `OTHER`

This prevents development lineages from being silently reconstructed as scientific Labs.

Example:
ChatGPT-Web-HWPX-MCP is `ENGINEERING_DEVELOPMENT`.

The lineage kind changes interpretation/context, not the mechanical transport semantics.

## Authority gates

- C: constitutional/adjudication legitimacy
- E: admissible world-contact
- P: provenance/time/auditability
- R: open-world rival invariance

If any gate is not PASS:
authority = HOLD.

## Current profile

v0.3 retains:

- W: world resistance
- N: noncommon evidence-route strength
- I: inferential identification
- D: defeat exposure / corrigibility

Calibration status after MQR-4.30:

```text
W = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
I = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
N = LEVEL-3 HOLD
D = external polarity PASS / Level-3 discriminant HOLD
```

The old scalar TPX remains retired.

```text
PROFILE_ORDER = PARETO_PARTIAL
SCALAR_PROJECTION_DEFAULT = OFF
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```

## Typed transport

v0.3 transport syntax:

```text
transport "<component>" "<source-regime>" "<target-regime>" <DIMENSION> <EVALUABILITY> <SURVIVAL> "<note>"
```

### Evaluability

Exactly one:

- `TESTED`
- `UNTESTED_AVAILABLE`
- `TARGET_UNAVAILABLE`
- `OUT_OF_SCOPE`

### Survival

When evaluability is `TESTED`:

- `SURVIVED`
- `FAILED`
- `MIXED_OR_NONATOMIC`

Otherwise:

- `NA`

### Derived transport authority

```text
TESTED + SURVIVED            -> TRANSPORT_PASS
TESTED + FAILED              -> TRANSPORT_FAIL
TESTED + MIXED_OR_NONATOMIC -> SPLIT_REQUIRED
UNTESTED_AVAILABLE           -> HOLD_UNTESTED
TARGET_UNAVAILABLE           -> HOLD_TARGET_UNAVAILABLE
OUT_OF_SCOPE                 -> OUT_OF_SCOPE
```

No averaging is permitted.

Claim-level transport is compiled to one of:

- `ALL_REQUIRED_CELLS_PASS`
- `SOME_REQUIRED_CELLS_FAIL`
- `PARTIAL_WITH_HOLDS`
- `SPLIT_REQUIRED`
- `NO_EVALUABLE_TARGET`

## MQR-4.31 validation

Fresh transport confirmation was sealed before native-label reveal.

Confirmatory corpus:
- RESEARCH_LAB: C3X and EPISTEME
- ENGINEERING_DEVELOPMENT: ChatGPT-Web-HWPX-MCP

Result:

```text
16 confirmatory cells
15/16 exact typed-state agreement = 0.9375
C1 untested-vs-failed = PASS
C2 componentwise transport = PASS
C3 cross-lineage concordance = PASS
C4 HWPX engineering/non-Lab typing = PASS
C5 success-collapse attack = PASS
```

The one mismatch was informative:
an operation-level `reject_all` promotion was incorrectly generalized to an uninstantiated component-specific `insert-reject` round-trip specimen.

Therefore:
**component-specific evaluability cannot be inherited from broader operation success.**

## Packet grammar

```text
REALPACKET 0.3
id "packet-id"
epoch "epoch"
claim CONSTRAINT "claim text"
scope "licensed scope"
lineage ENGINEERING_DEVELOPMENT

gate C PASS
gate E PASS
gate P PASS
gate R PASS

axis W 0.75 "why"
axis N 0.50 "why"
axis I 0.75 "why"
axis D 0.75 "why"

transport "component-a" "source" "target" VERSION TESTED SURVIVED "why"
transport "component-b" "source" "target" VERSION UNTESTED_AVAILABLE NA "why"

generator STRUCTURAL "description"
rival SURVIVING "description"
residue MODERATE "description"
mystery OPEN "description"
ontic HOLD "description"
successor VULNERABLE
source "source pointer"
END
```

## Canonical implementation policy

- Rust is the canonical compiler and the default for newly touched executable MQR surfaces.
- Python is retained as an independent reference/audit implementation where useful.
- Existing Python is not mechanically rewritten merely to change repository language statistics.
- Migration occurs when a surface becomes live again or when Rust/static implementation has a concrete reliability, portability, or performance advantage.

CI requires:
- v0.2 archival packet compatibility;
- v0.3 Rust/Python canonical-receipt concordance;
- rejection of v0.3 legacy `axis T`;
- Rust-first build success.

Implementation language is not an epistemic primitive.

## Proof-assistant division of labor

Real-Language is the typed boundary between world contact and proof systems.

Target architecture:

```text
WORLD CONTACT
 -> native evidence
 -> typed empirical receipt
 -> Real-Language premise authority
 -> formal obligation
 -> Lean proof
 -> independent formal recheck
 -> scoped consequence
```

Lean or another prover may certify derivability inside the formal region.
It does not certify the truth of empirical premises merely because they are formalized.

MQR-4.37 retires **PCRA as one monolithic scientific-authority construct** while preserving it as historical workflow architecture. The live decomposition is: **formal custody + world-facing authority + explicit transfer contract**. See `V05-AUTHORITY-TRANSFER.md`.

## Ceiling

Real-Language is allowed to represent earned authority, transport relations, premise ancestry and proof receipts.

It is not allowed to infer `TRANSFER=PASS` merely from formal-custody PASS.

It is not allowed to manufacture:
- a truth percentage,
- final ontology,
- universal cross-domain numeric units,
- transport authority for an untested component.


## v0.5 — executable world–statement transfer lane

MQR-4.38 makes the MQR-4.37 transfer boundary executable without turning it into a truth oracle.

Canonical implementation:
- Rust: `src/transfer_v05.rs` / binary `real-v05-transfer`;
- independent evaluator: `haskell/TransferV05.hs`;
- formal countermodels: `lean/MQR/Transfer.lean`.

The live transfer coordinates are:
- semantic correspondence;
- scope admissibility;
- authority-relevant ancestry preservation;
- defeat reachability;
- noncircular warrant;
- formal custody when applicable.

Each coordinate uses `PASS / HOLD / FAIL / NOT_APPLICABLE`. No numeric transfer score exists. HOLD is not collapsed into FAIL.

For a formally mediated route, `TRANSFER=PASS` means only:

```text
STRUCTURAL_ADMISSIBILITY_NONAMPLIFYING
```

The transfer contract cannot raise the source world-authority ceiling. A semantic-correspondence receipt remains a defeasible world-facing warrant rather than something the compiler can certify into existence.

A nonformal route is a first-class positive control:

```text
WORLD_AUTHORITY=PASS
FORMAL_CUSTODY=NOT_APPLICABLE
TRANSFER=NOT_APPLICABLE
```

Therefore formalization is optional and route-relative, not a universal condition for scientific authority.

Rust/Haskell concordance is implementation-diversity evidence only. It does not establish semantic or world independence.


## v0.6 — compositional transfer boundary

MQR-4.39 adds `REALCOMPOSE 0.6` and separates algebraic composition from scientific composition.

Canonical Rust: `src/compose_v06.rs` / `real-v06-compose`.
Independent Haskell: `haskell/ComposeV06.hs`.
Lean boundary: `lean/MQR/Composition.lean`.

The authority meet is associative and NoLaunder is transitive, but local transfer PASS does not imply composite PASS. The composition lane tracks endpoint compatibility, semantic composition, pathwise scope mapping, original-source ancestry, end-to-end defeat segments, assumption closure, global non-amplification and a direct source-to-target receipt.

A full PASS therefore means **conditional pathwise non-amplification**, not categorical closure of scientific authority. The live structural classification is **partial / witness-indexed composition**. See `V06-COMPOSITION.md`.


## v0.7 — world-contact substitution boundary

MQR-4.40 adds `REALSUBSTITUTE 0.7`.

Canonical Rust: `src/substitute_v07.rs` / `real-v07-substitute`.
Independent Haskell: `haskell/SubstituteV07.hs`.
Lean boundary: `lean/MQR/Substitution.lean`.
Constitution: `V07-SUBSTITUTION.md`.

v0.7 removes the universal requirement that every composed endpoint receive a fresh direct receipt. A TRANSPORT_ONLY or BASIS_GENERATED endpoint may receive substitution PASS with `direct_receipt ABSENT` when a live external World-Contact Basis covers every declared load-bearing empirical degree, the endpoint query is generated from the anchored basis, naturality/path/coherence obligations survive, ancestry and defeatability remain live, and global authority remains non-amplifying.

A NEW_EMPIRICAL endpoint is not substitution-eligible without new world-facing support.

The External Root Cut prevents closed transfer/justification loops from grounding themselves. Path agreement does not count as independent evidence; derived receipts do not refresh stale roots. Later direct disagreement reopens the substituted claim rather than acting as an infallible oracle.

The checker can report a minimum external-root cover only **relative to the declared empirical-degree/coverage graph**. It does not identify a complete or uniquely correct ontology of empirical degrees.

```text
FRESH DIRECT ENDPOINT CONTACT != UNIVERSAL PREREQUISITE
INTERNAL COHERENCE != WORLD CONTACT
WORLD-CONTACT BURDEN TRACKS UNCOVERED EMPIRICAL BURDEN, NOT ENDPOINT COUNT
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```


## v0.8 — frontier-relative contact rank

MQR-4.41 adds `REALCONTACTRANK 0.8`.

Canonical Rust: `src/contact_rank_v08.rs` / `real-v08-rank`.
Independent relational evaluator: `prolog/contact_rank_v08.pl`.
Lean boundary: `lean/MQR/ContactRank.lean`.
Constitution: `V08-CONTACT-RANK.md`.

v0.8 retires analyst-declared empirical degrees as a primitive basis for contact minimality. It instead takes a frozen set of claim-relative Rival-Separation Obligations and a versioned external-root separation incidence, then enumerates the exact minimum external discrimination covers for that finite court.

The result is **frontier-relative and instrument-relative**. It is not world dimensionality. Minimum bases may be nonunique and need not satisfy matroid basis exchange. Root cost is reported separately from cardinality. Rival/query expansion or root drift may raise rank; improved instrumentation may lower it.

```text
MINIMUM COVER != WORLD DIMENSION
SAME RANK != SAME ONTOLOGY
LOW RANK != INDEPENDENT EVIDENCE
OPTIMIZER COMPLETENESS != FRONTIER COMPLETENESS
FINITE MINIMUM != FINAL OPEN-WORLD MINIMUM
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```


### v0.8 cross-axis non-inferences

Calibration authority, selection-history sufficiency, decision warrant, and evaluation-contract authority are not inferred by contact-rank minimization.

```text
rank.calibration_authority_inferred=false
rank.selection_history_sufficiency_inferred=false
rank.decision_warrant_inferred=false
rank.evaluation_contract_authority_inferred=false
```

These are deliberate scientific boundaries: the finite optimizer operates after a separation relation has been constituted; it does not certify the upstream operation that constituted it.


## v0.9 — open rival-frontier governance

MQR-4.42 adds `REALFRONTIER 0.9`.

Canonical Rust: `src/frontier_v09.rs` / `real-v09-frontier`.
Independent relational evaluator: `prolog/frontier_v09.pl`.
Lean boundary: `lean/MQR/Frontier.lean`.
Constitution: `V09-FRONTIER.md`.

v0.9 treats the live rival frontier as a generated, query-relative and admission-governed object rather than a supplied complete set. It records generator ancestry, query families, discovery history, finite grammar state, frontier escapes and the before/after FCR surface.

No packet can earn world-frontier completeness. Repeated no-discovery supports only generator-relative saturation. Current-rival separation does not imply query-language closure. Multiple generators do not imply independent search when ancestry collapses. Stable FCR can coexist with important discovery, while rank increase is not a scalar discovery-value measure.

The positive operating rule is:

```text
OPEN FRONTIER RECEIPT
+ LIVE FRONTIER REOPENING RESERVE
+ AUDITABLE CURRENT-RIVAL DISCRIMINATION
+ EXPLICIT GENERATOR / QUERY / ADMISSION PROVENANCE
----------------------------------------------------
=> CONDITIONAL LOCAL USE OF FCR

NOT
=> FRONTIER COMPLETENESS
=> SCIENTIFIC STOPPING RULE
=> FINAL TRUTH
```

Canonical guards:

```text
frontier.world_complete=NO
frontier.discovery_value_scalar=OFF
frontier.fcr_guidance_scope=CONDITIONAL
frontier.open_frontier_receipt=REQUIRED
frontier.reopening_reserve=REQUIRED
frontier.reopen_on_escape=YES
frontier.completeness_claim=FORBIDDEN
frontier.discovery_impact_mode=VECTOR
```

The live doctrine is **reopening competence rather than completeness certification**.


## v0.10 — open-frontier attention allocation

MQR-4.43 adds `REALALLOCATE 0.10`.

Canonical Rust: `src/allocation_v10.rs` / `real-v10-allocate`.
Independent relational evaluator: `prolog/allocation_v10.pl`.
Lean boundary: `lean/MQR/Allocation.lean`.
Constitution: `V10-ALLOCATION.md`.

v0.10 treats finite scientific attention as a declared budget over typed search lanes with activation costs, ancestry, obligations, due horizons, reopening/exploitation roles and a witness-level exploration-debt ledger.

The positive object is an **Allocation Admissibility Envelope (AAE)**, not a unique optimizer. The 4.42 Frontier Reopening Reserve is strengthened operationally to an **Activation-Capable Reopening Reserve (ACRR)**: nominal reserve must be large enough to exercise at least one declared reopening lane.

Twin-world fixtures hold the visible RSAR surface fixed while reversing the witness-only next escape route. The evaluator therefore refuses to infer a universally correct next action from observationally identical open-frontier histories.

```text
ADMISSIBLE != OPTIMAL
NOMINAL RESERVE != ACTIVATION-CAPABLE RESERVE
EXPLORATION DEBT = TYPED LEDGER
OPPORTUNITY COST = VECTOR
UNIVERSAL NEXT ACTION = UNIDENTIFIED
WORLD FRONTIER COMPLETE = NO
STOPPING RULE = FORBIDDEN
```

Declared priors/utilities may authorize optimization only inside that declared model. They do not become a probability distribution or utility function over unconceived rivals.

Final MQR-4.43 scope:
- AAE is an admissibility-membership surface, not a universal optimizer;
- ACRR is activation capability, while ancestry/common-mode exposure remains separate;
- Lean proves the twin-world deterministic-policy boundary and a narrow finite unit-activation anti-starvation theorem with empty axiom ancestry;
- explicit obligation/debt semantics, not reserve existence alone, govern periodic exercise;
- declared-model optimization never lifts `allocation.world_optimum_identified` or `allocation.world_frontier_complete`.

The live doctrine is **finite attention governance without pricing the unknown**.


## v0.11 — exploration-obligation constitution

MQR-4.44 adds `REALCONSTITUTE 0.11`.

Canonical Rust: `src/constitution_v11.rs` / `real-v11-constitute`.  
Independent relational evaluator: `prolog/constitution_v11.pl`.  
Lean boundary: `lean/MQR/Constitution.lean`.  
Constitution: `V11-OBLIGATION-CONSTITUTION.md`.

v0.11 moves one level upstream from v0.10's allocation contract and audits the constitution of the obligations themselves.

Its primary representation attack is:

```text
ONE OBLIGATION -> {A,B}
!= label count
TWO OBLIGATIONS -> {A} + {B}

while

DECLARED BURDEN UNION = {A,B}
```

Therefore obligation count is rejected as an adequacy primitive. The live audit surface is the declared obligation–burden relation.

v0.11 separately tracks agenda-source ancestry, predecessor/successor burden coverage and debt continuity. A successor label cannot retire predecessor debt merely by renaming or deletion. Full successor coverage and debt discharge are distinct checks.

Endogenous mandate formation is permitted but marked. External provenance is likewise visible without becoming a truth oracle.

The repair is explicitly second-order limited:

```text
OBLIGATION COUNT != SEARCH BURDEN
DECLARED BURDEN UNION != WORLD-FUNDAMENTAL BURDEN ONTOLOGY
SUCCESSOR COVERAGE != DEBT DISCHARGE
PROVENANCE != TRUTH ORACLE
FINITE EOCR PASS != WORLD-COMPLETE OBLIGATION ONTOLOGY
```

Canonical guards include:

```text
constitution.partition_count_authority=REJECT
constitution.partition_audit_surface=DECLARED_BURDEN_UNION
constitution.external_source_truth_oracle=NO
constitution.endogenous_source_truth_oracle=NO
constitution.world_obligation_complete=NO
constitution.burden_atom_ontology_complete=NO
constitution.open_world_receipt=REQUIRED
constitution.reopen_on_escape=YES
constitution.guidance_mode=CONTRACT_RELATIVE_CONSTITUTIONAL
```

The live doctrine is **provisional obligation constitution with burden continuity and open-world reopening**, not a complete theory of what science ought to search.


## v0.12 — burden-ontology revision transport

MQR-4.45 adds `REALREVISE 0.12`.

Canonical Rust: `src/revision_v12.rs` / `real-v12-revise`.
Independent relational evaluator: `prolog/revision_v12.pl`.
Lean boundary: `lean/MQR/Revision.lean`.
Constitution: `V12-BURDEN-REVISION.md`.

v0.12 moves the obligation-governance problem across changing burden ontologies. Labels and version succession are neither necessary nor sufficient for cross-version burden identity. Transport is typed as `EXACT / REFINE / MERGE / OVERLAP / DISJOINT / UNMAPPED`.

Historical exploration debt is keyed to source ancestry rather than target-carrier cardinality. A refinement may create several target carriers without multiplying one historical debt; a merge may create one target carrier without erasing several independently inherited debts. Full refinement coverage and provenance-preserving merge can carry debt locally, while partial overlap, unmapped disappearance and ancestry collapse require reopening.

Cross-constitution comparison is deliberately partial:

```text
COMPARABILITY = MAPPED_SUBSPACE_ONLY
CONFLICT LOCALIZATION != TRUE WINNER
DIRECT/COMPOSED REVISION DISAGREEMENT -> REOPEN
WORLD BURDEN IDENTITY = NOT INFERRED
FUTURE REVISION CLOSURE = NO
```

The live doctrine is **versioned, loss-aware burden transport without ontology-identity laundering**.


## v0.13 — contestable burden-translation authority

MQR-4.46 adds REALMAPAUTH 0.13.

Canonical Rust: src/map_authority_v13.rs / real-v13-map-authority.
Independent relational evaluator: prolog/map_authority_v13.pl.
Lean boundary: lean/MQR/MapAuthority.lean.
Constitution: V13-TRANSLATION-AUTHORITY.md.

v0.13 moves one level upstream from v0.12: a typed burden-transport relation is no longer treated as authoritative merely because it is declared. The live receipt tracks proposer/adjudicator/standard ancestry, self-certification, common-mode adjudication, capture risk, competing standards, set-valued correspondence, world-facing narrowing, direct/meta conflict and meta-dependency.

Correspondence may remain non-singleton. A forced singleton is a reopening event. A world-facing separator may narrow the surviving relation set but never creates a unique world-correspondence oracle. Cyclic meta-validation creates no independent root; finite unanchored meta-dependency is carried as explicit meta-debt.

Canonical guards:

~~~text
UNIQUE WORLD CORRESPONDENCE = NO
FUTURE TRANSLATION CLOSURE = NO
CONSENSUS TRUTH ORACLE = NO
STANDARD TRUTH ORACLE = NO
EXTERNALITY TRUTH ORACLE = NO
META-CYCLE AUTHORITY = NO
GUIDANCE = CONTESTABLE_SET_VALUED_TRANSLATION_AUTHORITY
~~~

The live doctrine is **provisional translation authority without a final dictionary or meta-standard**.
