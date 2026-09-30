# Real-Language / Real-Packet v0.3–v0.24

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


## v0.14 — translation-challenge constitution

MQR-4.47 adds `REALCHALLENGE 0.14`.

Canonical Rust: `src/challenge_v14.rs` / `real-v14-challenge`.
Independent relational evaluator: `prolog/challenge_v14.pl`.
Lean boundary: `lean/MQR/Challenge.lean`.
Constitution: `V14-CHALLENGE-CONSTITUTION.md`.

v0.14 moves one level upstream from v0.13's world-facing separator: a probe does not gain narrowing authority merely because it is world-facing. The live receipt distinguishes the registered family, selected packet, selection rule and timing; computes declared defeat-route coverage; audits probe ancestry and candidate-derived relevance/scoring; retains omitted counterprobes; and reopens under challenge expansion.

Canonical guards:

~~~text
WORLD_FACING != SELECTION_AUTHORIZED
PROBE COUNT != ROUTE COVERAGE
PROBE COUNT != ANCESTRY INDEPENDENCE
CURRENT FAMILY COMPLETE = NO
FUTURE CHALLENGE SPACE CLOSED = NO
GUIDANCE = CONSTITUTED_REOPENABLE_SEPARATOR_AUTHORITY
~~~

A clean ancestry-separated, route-covering, prospectively selected packet may earn `AUTHORIZED_PROVISIONAL_NARROWING`. A post-outcome selection, captured discriminator, omitted counterprobe, coverage hole, common ancestry, or expansion conflict yields HOLD/REOPEN rather than silent promotion.

The live doctrine is **constituted and reopenable separator authority without a final challenge space**.


## v0.15 — defeat-route ontology constitution

MQR-4.48 adds `REALROUTE 0.15`.

Canonical Rust: `src/route_v15.rs` / `real-v15-route`.
Independent relational evaluator: `prolog/route_v15.pl`.
Lean boundary: `lean/MQR/RouteOntology.lean`.
Constitution: `V15-ROUTE-ONTOLOGY.md`.

v0.15 moves one level upstream from v0.14's defeat-route coverage matrix. Route labels and route counts are no longer treated as stable coverage primitives. The live receipt tracks declaration-relative defeat content, route ancestry, EXACT/REFINE/MERGE/OVERLAP/DISJOINT/UNMAPPED route transport, content-level coverage witnesses, hidden-route discoveries and revision-path disagreement.

Canonical guards:

~~~text
ROUTE LABEL != ROUTE IDENTITY
ROUTE COUNT != DEFEAT-CONTENT COUNT
ROUTE SPLIT != NEW DEFEAT CAPACITY
ROUTE MERGE != COVERAGE DISCHARGE
EQUAL COVERAGE FRACTIONS != COVERAGE EQUIVALENCE
CURRENT ROUTE ONTOLOGY COMPLETE = NO
FUTURE DEFEAT SPACE CLOSED = NO
GUIDANCE = VERSIONED_DEFEAT_CONTENT_COVERAGE
~~~

A content-preserving refinement or merge may carry local coverage authority. Undertransport, coverage collapse, ancestry entanglement, hidden-route discovery or noncommuting revision paths yield HOLD/REOPEN rather than silent inheritance.

The live doctrine is **versioned defeat-content coverage without a final taxonomy of ways to fail**.


## v0.16 — defeat-content constitution

MQR-4.49 adds `REALDEFEAT 0.16`.

Canonical Rust: `src/defeat_v16.rs` / `real-v16-defeat`.
Independent relational evaluator: `prolog/defeat_v16.pl`.
Lean boundary: `lean/MQR/DefeatContent.lean`.
Constitution: `V16-DEFEAT-CONTENT.md`.

v0.16 moves one level upstream from v0.15's defeat-content ledger. A content name, mechanism, manifestation or representation cell is no longer treated as an identity primitive. The live object is a claim-relative Counterfactual Defeat Profile (CDP) over a declared challenge family.

Canonical guards:

~~~text
DEFEAT LABEL != DEFEAT IDENTITY
MECHANISM != MANIFESTATION != DEFEAT ROLE
CONTENT COUNT != INDEPENDENT FAILURE DIMENSIONS
CURRENT CDP EQUIVALENCE != FUTURE/WORLD IDENTITY
CURRENT DEFEAT ATOMS COMPLETE = NO
FUTURE DEFEAT SPACE CLOSED = NO
GUIDANCE = REOPENABLE_COUNTERFACTUAL_DEFEAT_QUOTIENT
~~~

A counterfactually identical split earns no new distinction. A prospectively separated refinement may earn local authority. A fully witnessed scope quotient may merge defeat roles without asserting metaphysical identity. Common cause compresses independence rather than automatically collapsing content. Challenge expansion, hidden-content genesis, representation collapse or revision-path conflict yields HOLD/REOPEN.

The live doctrine is **route identity through reopenable, claim-relative defeat-role equivalence without final error atoms**.


## v0.17 — constitutional regress boundary

MQR-4.50 adds `REALREGRESS 0.17`.

Canonical Rust: `src/regress_v17.rs` / `real-v17-regress`.
Independent relational evaluator: `prolog/regress_v17.pl`.
Lean boundary: `lean/MQR/RegressBoundary.lean`.
Constitution: `V17-REGRESS-BOUNDARY.md`.

v0.17 does not search for a final foundation. It asks when recursive critique of the current scientific-authority constitution may stop *operationally* at a declared claim/use surface. The live receipt freezes claim scope, challenge and world-contact families, decision contract, registered refinements and materiality criteria; requires replay of every admitted refinement; carries unresolved debt explicitly; separates descriptive from action authority; and preserves activation-capable reopening.

Canonical guards:

~~~text
METAPHYSICAL TERMINATION != OPERATIONAL TERMINATION
CURRENT FIXED POINT != GLOBAL FIXED POINT
REGISTERED STABILITY != FUTURE REFINEMENT-SPACE COMPLETENESS
DESCRIPTIVE SUFFICIENCY != UNIVERSAL ACTION WARRANT
OPERATIONAL STOP != OPEN-WORLD SEARCH RETIREMENT

FINAL ONTOLOGY = NO
FUTURE REFINEMENT SPACE CLOSED = NO
STOP-RULE TRUTH ORACLE = NO
OPERATIONAL STOP PERMANENT = NO
REOPENING RESERVE = ACTIVE
GUIDANCE = REOPENABLE_OPERATIONAL_FIXED_POINT
~~~

Input-admissibility firewall:

~~~text
CRBR CONSUMES CONSTITUTIONALLY ADMITTED S/Q/W/R/K.
CRBR DOES NOT SELF-AUTHORIZE A THIN SURFACE.
UPSTREAM HOLD/REOPEN CANNOT BE LAUNDERED INTO PASS BY v0.17.
~~~

A nonvacuous, replay-complete, debt-free, criterion-invariant current surface may earn `AUTHORIZED_CRITERION_ROBUST_OPERATIONAL_STOP`. An explicit decision contract with action invariance may additionally earn `AUTHORIZED_ACTION_UNDER_DECLARED_CONTRACT`. Material refinements, live debt, post-outcome scope/criterion capture, criterion disagreement, meta-cycles, path conflict, new distinguishing world contact, criterion-envelope break or decision-contract change yield HOLD/REOPEN.

The live doctrine is **reopenable operational sufficiency without a final ontology, global stopping rule, or retirement of open-world inquiry**.


## v0.18 — stopping-rule calibration

MQR-4.51 adds `REALSTOP 0.18`.

Canonical local evaluator: Rust `src/stop_v18.rs` / `real-v18-stop`.
Independent relational evaluator: `prolog/stop_v18.pl`.
Prospective calibration harness: `experiments/mqr-4.51/benchmark.py`.
Finite Lean boundary: `lean/MQR/StoppingCalibration.lean`.
Constitution: `V18-STOPPING-CALIBRATION.md`.

v0.18 separates **constitutional stop eligibility** from **calibrated stop timing**.

The first prospective court materialized 468 generated traces across three independently coded domains and twelve forcing families, with 108 discovery / 144 calibration / 216 untouched holdout traces.

Raw immediate OQSC stopping failed C1 in every domain:

~~~text
RAW OQSC HOLDOUT
PSE_live = 51
AE_live = 51
OIW = 38.5
VERDICT = FAIL
~~~

The calibration split selected one additional eligible transition, `lambda=1`, from the frozen `{0,1,2,3}` family. Without holdout tuning, that successor passed C1–C5 in FAULT, MEASUREMENT and SEARCH:

~~~text
CALIBRATED OQSC-LAG-1 HOLDOUT
PSE_live = 0
AE_live = 0
OIW = 338.5
RL_max = 0
MISSED_REOPEN = 0
VERDICT = PASS
~~~

The increase in OIW is retained as a load-bearing trade-off; no scalar score erases it.

Canonical guards:

~~~text
OQSC ELIGIBLE != CALIBRATED STOP NOW
LIVE-OBLIGATION PREMATURE ERROR != FUTURE REOPENING
PRIMARY SCALAR SCORE = OFF
HIDDEN GOLD ACCESS = NO
FUTURE ORACLE = NO
POST-HOLDOUT POLICY REPAIR = FORBIDDEN
EXTERNAL CALIBRATION = HOLD
UNIVERSAL OPTIMALITY = FORBIDDEN
GUIDANCE = CALIBRATED_REOPENABLE_STOP
~~~

The benchmark-specific `lambda=1` result is **not** a universal real-world stopping constant. v0.18 makes the calibration coordinate explicit while preserving v0.17's reopening reserve and upstream-admissibility firewall.

The live doctrine is **internally calibrated, reopenable stop timing on the declared benchmark family, with external scientific calibration still on HOLD**.


## v0.19 — naturalistic trace / authority-mode boundary

MQR-4.52 adds `REALTRACE 0.19`.

Canonical evaluator: Rust `src/trace_v19.rs` / `real-v19-trace`.
Independent relational evaluator: `prolog/trace_v19.pl`.
Naturalistic reconstruction/scorer: `experiments/mqr-4.52/naturalistic_cases.py` + `naturalistic_court.py`.
Finite proof boundary: `lean/MQR/NaturalisticTrace.lean`.
Constitution: `V19-NATURALISTIC-TRACE.md`.

v0.19 is a **representation revision** forced by the first naturalistic transport attack on v0.18.

The frozen MQR-4.52 corpus admitted 7 PRIMARY episodes across seven instrument/science regimes, retained 1 ozone-hole episode as SENSITIVITY, and rejected the currently unresolved Hubble-tension programme from primary scoring.

Five PRIMARY episodes admit source-supported claim-freeze windows. On those windows:

~~~text
RAW OQSC:
  definite N-PSE = 0
  definite N-OIW = 0
  within window = 5

OQSC-LAG-1:
  definite N-PSE = 0
  definite N-OIW = 0
  within window = 5
~~~

This is **partial naturalistic compatibility**, not prospective external validation.

Two stronger results defeat direct transport of the v0.18 ontology:

~~~text
6 / 7 PRIMARY EPISODES = MULTI-MODE AUTHORITY

6 / 6 EPISODES WITH AN ELIGIBLE STATE
= FIXED EVENT-COUNT LAG
  SENSITIVE TO INERT CHECKPOINT REFINEMENT
~~~

A claim can freeze while probing continues. A treatment can be provisionally usable while mechanism remains open. An investigation can be handed off or archived without a truth declaration. A novel post-closure world contact can reopen one coordinate without globally reversing every prior result.

Therefore v0.19 tracks:

~~~text
CLAIM
PROBE
USE
LIVE OBLIGATION
CRITERION
BREAK / REOPENING
SOURCE-TEMPORAL MAPPING
PARTIAL STOP WINDOW
AUTHORITY-MODE PROJECTION
TRACE GRANULARITY
~~~

Canonical non-inferences:

~~~text
CLAIM FREEZE != PROBE STOP
PROVISIONAL USE != UNIVERSAL MECHANISTIC CLOSURE
ARCHIVE != TRUTH
HISTORICAL ACTION != GOLD
ONE EVENT != ONE UNIT OF WORLD CONTACT
LAG-1 GENERATED CALIBRATION != NATURALISTIC UNIVERSAL CONSTANT
NATURALISTIC COMPATIBILITY != PROSPECTIVE EXTERNAL VALIDATION
WORLD CONTACT != FALSIFICATION ONLY
~~~

Canonical guards:

~~~text
trace.unique_stop_time_inferred=NO
trace.historical_action_truth_oracle=NO
trace.naturalistic_retuning_lambda=NO
trace.prospective_external_validation=NO
trace.popperian_master_semantics=REJECT
trace.world_contact_negative_only=NO
trace.guidance_mode=MODE_RELATIVE_REOPENABLE_AUTHORITY
~~~

The live MQR-4.52 thesis is intentionally broader than a falsification-centred picture but does not claim originality for being “post-Popperian.” Exploratory experimentation, active/pragmatic realism, perspectival realism, local realism and conditional robustness are prior-art constraints.

The candidate MQR excess is narrower: **an executable, source-temporal, partially identified and reopenable authority state over claims, probes, uses, obligations and resource transitions**.

v0.19 does not infer that these coordinates are final or that one universal ontological principle governs all sciences.


## v0.20 — world-contact progress atlas

MQR-4.53 adds `REALPROGRESS 0.20`.

Canonical evaluator: Rust `src/progress_v20.rs` / `real-v20-progress`.
Independent relational evaluator: `prolog/progress_v20.pl`.
Countermodel court: `experiments/mqr-4.53/progress_court.py`.
Finite proof boundary: `lean/MQR/ProgressGeometry.lean`.
Constitution: `V20-PROGRESS-ATLAS.md`.

The first qualifying post-Amendment-A Court reveal was:

~~~text
head = 632e748367b7793bc1a5d85b766e2c1018f3c3dc
run = 36389215348
verdict = SUCCESS
~~~

Thirteen candidate progress families were attacked. No unlicensed universal scalar survived.

~~~text
EVENT COUNT = REJECT
ELAPSED TIME = POLICY INPUT ONLY
RESOURCE COST = POLICY INPUT ONLY
SHANNON / KL = LOCAL ONLY
VOI = CONTRACT-LOCAL
FISHER-RAO = LOCAL METRIC
BLACKWELL = LOCAL PARTIAL ORDER
OBLIGATION COUNT = REJECT
BURDEN DISCHARGE = LOCAL PREORDER
AUTHORITY PATH LENGTH = REJECT
NET AUTHORITY LEVEL = REJECT
PARETO / VECTOR = PARTIAL ONLY
WCPA = PROMOTED
~~~

The positive result is not anti-metric.

Fisher geometry, Blackwell/Le Cam comparison, observability/identifiability and other local constructions show that representation-invariant metrics/orders may exist once a target space and admissible transformations are constituted.

The live MQR result is narrower:

~~~text
LOCAL METRIC / ORDER / PREORDER /
REACHABILITY STRUCTURE
MAY BE SCIENTIFICALLY EARNED

WITHOUT A
GLOBAL SCIENTIFIC-PROGRESS RULER.
~~~

v0.20 therefore represents a **World-Contact Progress Atlas**:

~~~text
chart =
(
  inquiry-state space,
  declared inert transformations,
  quotient,
  claim/use/decision contract,
  reopening/world-contact structure,
  local progress structure
)
~~~

Core non-identities:

~~~text
PROGRESS STATE != CONTINUATION VALUE
MORE CLAIM AUTHORITY != MORE PROGRESS
INFORMATION != INTERVENTION REACH != ACTION VALUE
PATH LENGTH != NET PROGRESS
STRUCTURAL TRANSPORT != MAGNITUDE TRANSPORT
LOCAL GEOMETRY != GLOBAL RULER
~~~

Stop semantics are correspondingly non-scalar:

~~~text
CURRENT STATE IN PAR
+ LIVE MATERIAL DEBT EMPTY
+ CVE BELOW DECLARED OPPORTUNITY-COST BOUND
+ REOPENING RESERVE ACTIVE
----------------------------------------------
=> LOCAL STOP ELIGIBILITY
~~~

This does not quantify unconceived probes.

Post-reveal proof integration exposed one namespace collision between the old Constitution and new ProgressGeometry witness names. It was repaired at `740011008f81d5b766894e8123b69028e11add96` without changing any theorem statement or scientific result.

The remaining constitutional debt is explicit:

~~~text
INVARIANCE UNDER G_inert
DOES NOT SELF-AUTHORIZE
THE CHOICE OF G_inert.
~~~

The chart target, inert-transformation class and cross-chart morphism authority remain open to successor attack.


## v0.21 — world-contact invariance constitution

MQR-4.54 adds `REALINVARIANCE 0.21`.

Canonical implementation:
- Rust: `src/invariance_v21.rs` / `real-v21-invariance`;
- independent evaluator: `prolog/invariance_v21.pl`;
- formal boundary: `lean/MQR/InvarianceConstitution.lean`;
- executable constitution: `V21-INVARIANCE-CONSTITUTION.md`.

The live constitution object is:

```text
C = (T, X, Γ, P, A, M, D, S)
```

The transformation surface is typed rather than presumed globally group-valued:

```text
GROUP | GROUPOID | PSEUDOGROUP | MONOID | PARTIAL_FAMILY
```

v0.21 distinguishes an actual consequence-preserving symmetry from a transformation currently certified inert under the declared probe/intervention/morphism/defeat/scope contract. It detects over-quotienting, under-quotienting, scope-export failure, morphism capture and post-reveal constitution capture.

The key authority boundary is:

```text
EQUIVALENCE-KERNEL ORDER
!=
SCIENTIFIC-AUTHORITY ORDER
```

A globally scoped successful receipt may earn transport within its declared scope without establishing a unique global invariance constitution.

The live receipt is **WCICR — World-Contact Invariance Constitution Receipt**. It is reopenable and explicitly does not certify completeness of the consequence families used to audit it.


## v0.22 — world-contact consequence-family constitution

MQR-4.55 adds `REALCONSEQUENCE 0.22`.

Canonical implementation:
- Rust: `src/consequence_v22.rs` / `real-v22-consequence`;
- independent evaluator: `prolog/consequence_v22.pl`;
- formal boundary: `lean/MQR/ConsequenceFamily.lean`;
- executable constitution: `V22-CONSEQUENCE-FAMILY.md`.

The live consequence-family constitution is:

```text
F = P ⊔ A ⊔ M ⊔ D ⊔ S
Ψ = (T, F, Γ_F, Π, E, H, R)
```

where the receipt audits current consequence contents, generation grammar, ancestry/common-mode structure, exterior expansion, heuristic/tacit proposal ecology and reopening.

The key authority boundaries are:

```text
MORE TESTS
!= MORE INDEPENDENCE
!= MORE ADEQUACY
!= MORE AUTHORITY

FORMAL COMPLETENESS(L)
!= WORLD CONSEQUENCE COMPLETENESS

HEURISTIC GENERATION
!= CLAIM AUTHORITY
```

v0.22 therefore permits diagrams, analogy, model manipulation, trained recognition and tacit competence to **generate** candidate consequences without letting those channels self-authorize their products.

The live methodological asymmetry is:

```text
GENERATION:
BROAD / PLURAL / PRE-FORMAL-ADMISSIBLE

ADJUDICATION:
STRICT / SCOPED / PROSPECTIVE /
WORLD-CONTACTED / DEFEAT-RESPONSIVE
```

Rigor remains load-bearing: when a compressed/tacit/high-level move becomes defeat-sensitive, enough of it should be made explicit to audit failure. But ex-ante formalizability is not a universal admission requirement for scientific search.

The live receipt is **WCCFR — World-Contact Consequence-Family Receipt**. It can earn local family adequacy only while emitting `world_family_complete=NO`.

REALCONSEQUENCE 0.22 is not a universal discovery algorithm and does not define one homogeneous faculty of intuition.


## v0.23 — world-contact expansion-policy constitution

MQR-4.56 adds `REALVALUE 0.23`.

Canonical implementation:
- Rust: `src/value_v23.rs` / `real-v23-value`;
- independent evaluator: `prolog/value_v23.pl`;
- formal boundary: `lean/MQR/ExpansionPolicy.lean`;
- executable constitution: `V23-EXPANSION-POLICY.md`.

The live expansion-policy constitution is:

```text
Ω = (T, C, V, Q, Π_V, A, O, D, R)
```

The key authority boundaries are:

```text
ADMISSIBLE ALLOCATION
!= GOOD CHALLENGE PREFERENCE

INFORMATION GAIN
!= TARGET RELEVANCE
!= ACTION VALUE
!= ESCAPE VALUE
!= OPTION VALUE

GENERATOR DIVERSITY
!= VALUATION DIVERSITY

LOCAL OPTIMUM
!= WORLD-OPTIMAL SCIENCE
```

Challenge value is typed and target-relative rather than scalar by default. `REALVALUE 0.23` audits target/use contracts, value-estimator provenance, proxy dependence, target drift, adversarial decoys, opportunity-cost semantics, horizon, option value, exterior value challenge and reopening.

The live receipt is **WCEPR — World-Contact Expansion-Policy Receipt**.

WCEPR may license:
- local dominance;
- partial-order guidance;
- declared-model optimization;
- option-opening preference;
- world-contacted revision of the value constitution.

It does not license a universal scientific utility or a world-optimal expansion policy. Scalar default remains OFF.


## v0.24 — world-contact strategic-ecology constitution

MQR-4.57 adds `REALSTRATEGY 0.24`.

Canonical implementation:
- Rust: `src/strategy_v24.rs` / `real-v24-ecology`;
- independent evaluator: `prolog/strategy_v24.pl`;
- formal boundary: `lean/MQR/StrategicEcology.lean`;
- executable constitution: `V24-STRATEGIC-ECOLOGY.md`.

The live discovery-ecology constitution is:

```text
Ξ = (A, Θ, M, Ω, Σ, U, Φ, X, R)
```

Its key authority boundaries are:

```text
LOCAL WCEPR PASS
!= INCENTIVE-ROBUST SEARCH

OBSERVED CHALLENGE SUPPLY
!= EXOGENOUS FRONTIER

REPORTED COST
!= REALIZED COST
!= SOCIAL OPPORTUNITY COST

STABLE EQUILIBRIUM
!= EPISTEMIC ADEQUACY

NOMINAL AGENT COUNT
!= STRATEGIC INDEPENDENCE

LOCAL MECHANISM SUCCESS
!= UNIVERSAL SCIENTIFIC MECHANISM
```

`REALSTRATEGY 0.24` audits agent/role maps, private-information surfaces, incentive maps, challenge-supply provenance, reported-vs-realized cost, target/proxy choice provenance, performative feedback, strategic ancestry, identity multiplicity, mechanism counterfactuals, exterior reserves, equilibrium ceilings, capture attribution and reopening.

The live receipt is **WCSER — World-Contact Strategic-Ecology Receipt**.

WCSER can license scoped strategic-robustness claims only while the institutional mechanism itself remains a defeasible world-contact object. It does not certify truthful revelation, an epistemically adequate equilibrium, or a universal scientific institution.
