# MQR-4.41 — World-Contact Basis Rank Court

Status: CLOSED / C+E+F+G / FRONTIER-RELATIVE CONTACT RANK / EMPIRICAL-DEGREE PRIMITIVE RETIRED / GENERICALLY NONMATROIDAL / OPEN-WORLD NONFINAL / MAIN-ONLY

## Formal stage name

**MQR-4.41 — World-Contact Basis Rank Court, Empirical-Degree Independence, Root-Set Nonuniqueness, Anchor Exchangeability, Drift-Triggered Basis Expansion & Whether Minimal External Contact Can Be Identified without Smuggling an Ontology of Independent Degrees into the Certificate**

## Research OS runtime

The court was presealed under the Research OS Argument-First / Literature Non-Sovereignty doctrine before literature contact.

```text
THINK -> ARGUE -> ATTACK -> SEARCH -> TEST -> REVISE
```

Literature was admitted only as:
- prior-art / novelty-kill pressure;
- rival and counterexample source;
- experimental-design and mathematical machinery donor;
- evidential constraint.

It was not allowed to decide the verdict by prestige, citation count, consensus, or venue.

## Question

Can MQR identify a minimum external world-contact burden without stipulating a privileged ontology of independent empirical degrees?

Answer:

```text
NOT AS AN INTRINSIC WORLD RANK.

YES AS A FRONTIER-RELATIVE, INSTRUMENT-RELATIVE
MINIMUM EXTERNAL DISCRIMINATION COVER.
```

## Primitive replacement

MQR-4.40 used a declared set of "empirical degrees".

MQR-4.41 retires that object as a primitive ontology term for WCB minimality.

The replacement is:

### Rival-Separation Obligation (RSO)

A claim-relevant rival pair/class that must remain distinguishable for the target claim to retain its current authority.

### World-Contact Separation Hypergraph (WCSH)

A finite incidence relation:

```text
EXTERNAL ROOT r --separates--> RSO o
```

### Frontier-Relative Contact Rank (FCR)

For a frozen claim scope C, rival frontier F, query/intervention class Q, live external root family R and separation incidence S:

```text
rho(C,F,Q,R,S)
  = minimum |B|
    over B subseteq R
    such that every live RSO is separated by at least one root in B.
```

If no basis covers the live RSOs:

```text
rho = UNCOVERED / UNIDENTIFIED
```

FCR is not:
- world dimensionality;
- number of causal variables;
- number of true mechanisms;
- evidence independence;
- experiment quality;
- truth probability;
- final open-world minimality.

## Frozen attack adjudication

### 1–2. Degree split / merge

**DECLARED-DEGREE PRIMITIVE = REJECTED.**

The legacy v0.7 degree fixtures change the declared minimum from 1 to 2 under a representational split.

Therefore a minimum over analyst-declared degrees can inherit the decomposition it claims to measure.

The replacement rank is defined over frozen discrimination obligations instead.

### 3. Rival-separation reparameterization

**INCIDENCE-RELATIVE INVARIANCE = SUPPORTED.**

Representation fixtures with renamed/reparameterized obligations but isomorphic root-obligation incidence preserve:
- minimum rank;
- basis count;
- uniqueness status;
- exchange result.

Lean supplies an axiom-empty renaming witness.

This is representation invariance only relative to the frozen WCSH, not invariance to changing the scientific rival frontier.

### 4. Root-set nonuniqueness

**MINIMUM RANK -> UNIQUE BASIS = REJECTED.**

Frozen non-matroid fixture:

```text
O={o1,o2,o3,o4}

r1={o1,o2}
r2={o3,o4}
r3={o1,o3}
r4={o2,o4}

B1={r1,r2}
B2={r3,r4}
rho=2
basis_count=2
```

A rank receipt must expose the minimum-basis family rather than silently canonize one root set.

### 5. Anchor exchangeability

**GENERIC MATROIDALITY = REJECTED.**

For the same fixture:

```text
exchange_property = FAIL
```

Replacing r1 in B1 with either available element of B2 fails to preserve coverage.

Therefore arbitrary minimum WCB families are set-cover/hypergraph objects, not matroid bases in general.

Matroid structure is admissible only when independently proved for a particular scientific surface.

### 6. Instrument-family dependence

**INSTRUMENT RELATIVITY = SUPPORTED.**

Frozen transition:

```text
before improved root family: rho=2
after genuinely external joint discriminator: rho=1
```

A lower contact rank can therefore result from better measurement technology without any reduction in world complexity.

### 7–8. Rival/query expansion

**FRONTIER MONOTONICITY UNDER FIXED OLD INCIDENCE = SUPPORTED.**

Frozen frontier fixture:

```text
base frontier: rho=1
expanded frontier: rho=2
```

The theorem is conditional on preserving the old root-obligation incidence. A changed query class may generate new RSOs and reopen the receipt.

### 9. Root drift / edge deletion

**DRIFT-TRIGGERED BASIS EXPANSION = SUPPORTED.**

```text
before drift: rho=1
after separation edge loss: rho=2
```

Old coverage cannot survive by receipt inertia.

### 10. Root improvement / edge addition

**RANK CAN DECREASE = SUPPORTED.**

FCR is therefore not a monotone history of discovered ontic dimension.

### 11. Cost vs cardinality

**RANK != BEST EXPERIMENT DESIGN.**

The non-matroid fixture has two minimum-cardinality bases of size 2 with costs:

```text
min basis cost = 2
max basis cost = 200
```

Cardinality rank does not select the cheaper, safer, fresher, more robust or less correlated basis.

Those are separate objectives.

### 12. Common-cause root compression

**LOW FCR != EVIDENCE INDEPENDENCE.**

One root may discriminate many RSOs while carrying one shared failure mode.

Real-Language v0.8 explicitly outputs:

```text
rank.common_cause_independence_inferred=false
```

Existing EFCG/UCCR/common-cause governance remains load-bearing.

### 13. Open-world rival injection

**FINITE FCR != FINAL OPEN-WORLD MINIMALITY.**

Every finite rank is indexed by a frozen frontier/query/root universe.

A successor rival outside that frontier may require an additional external discriminator.

### 14. Ontology-from-optimizer circularity

**OPTIMIZER COMPLETENESS != FRONTIER COMPLETENESS.**

The optimizer can minimize only over the obligations it is given.

It cannot infer that the supplied RSO set is the complete space of scientifically relevant distinctions.

## Rank does not recover ontology

Two frozen fixtures with different obligation counts can have the same minimum contact rank:

```text
ontology fixture A: obligation_count=2, rho=1
ontology fixture B: obligation_count=3, rho=1
```

Therefore:

```text
SAME FCR != SAME FRONTIER ONTOLOGY
FCR VALUE != NUMBER OF EMPIRICAL DEGREES
```

## Real-Language v0.8

Canonical Rust:

`language/real/src/contact_rank_v08.rs` / `real-v08-rank`

Independent relational evaluator:

`language/real/prolog/contact_rank_v08.pl`

Formal boundary:

`language/real/lean/MQR/ContactRank.lean`

Grammar:

```text
REALCONTACTRANK 0.8
id ...
claim_scope ...
frontier ...
query_class ...
root <id> EXTERNAL|INTERNAL LIVE|STALE|EXPIRED
cost <root> <integer>
obligation <id>
separates <root> <obligation>
authorize_rank ...
authorize_unique ...
authorize_exchange ...
END
```

Core outputs:

```text
rank.coverage_complete
rank.minimum
rank.basis_count
rank.unique
rank.exchange_property
rank.minimum_basis_cost_min
rank.minimum_basis_cost_max
rank.minimum_bases
rank.obligation_count
rank.eligible_root_count
rank.frontier_relative=true
rank.instrument_relative=true
rank.ontic_dimension=false
rank.degree_ontology_primitive=false
rank.cost_objective=SEPARATE
rank.open_world_final=false
rank.common_cause_independence_inferred=false
```

Meaning:

```text
FROZEN_FRONTIER_MINIMUM_EXTERNAL_DISCRIMINATION_COVER
```

## Executable receipts

Canonical repaired stage court:

```text
36186041842 = SUCCESS
MQR441_RUST_PROLOG_CONCORDANCE=PASS
MQR441_DEGREE_ONTOLOGY_AS_PRIMITIVE=REJECT
MQR441_SEPARATION_RELATIVE_RANK=PASS
MQR441_ROOT_SET_NONUNIQUENESS=PASS
MQR441_GENERIC_BASIS_EXCHANGE=FAIL
MQR441_DRIFT_TRIGGERED_BASIS_EXPANSION=PASS
MQR441_OPEN_WORLD_FINAL_MINIMUM=UNIDENTIFIED
```

Canonical full Real-Language CI:

```text
36186041813 = SUCCESS
REAL_LANGUAGE_V08_RUST_PROLOG_CONCORDANCE=PASS
MQR441_DECLARED_DEGREE_ONTOLOGY_PRIMITIVE=REJECT
MQR441_FRONTIER_RELATIVE_CONTACT_RANK=PASS
MQR441_MINIMUM_BASIS_UNIQUENESS=REJECT
MQR441_GENERIC_MATROID_EXCHANGE=REJECT
MQR441_RANK_FRONTIER_AND_INSTRUMENT_RELATIVE=PASS
```

## Formal receipts

Lean/nanoda run:

```text
36184144483 = SUCCESS
MQR441_CONTACT_RANK_AXIOM_ANCESTRY=EMPTY
MQR441_NANODA_INDEPENDENT_CHECKER=PASS
MQR441_CONTACT_RANK_COUNTERMODELS_REPLAY=PASS
```

Axiom-empty theorem surface:

- `twoMinimumCoverWitnesses`
- `minimumWorldContactBasesNeedNotSatisfyExchange`
- `frontierExpansionCanIncreaseContactRank`
- `rootDriftCanIncreaseContactRank`
- `instrumentExpansionCanDecreaseContactRank`
- `incidenceRenamingPreservesRankWitness`
- `sameMinimumRankDoesNotIdentifyFrontierOntology`
- `declaredDegreeCountCanChangeWithoutAWorldWitness`

## Failed precursor custody

Failed 4.41 runs remain preserved.

The final scientific result was not obtained by waiving them.

The main implementation defects were:
- early Lean witness/formulation defects, later repaired to axiom-empty proofs;
- Prolog packet invocation/entry-point defects;
- blank-line tokenization causing `load_packet` failure;
- a Prolog negation-precedence bug in the basis-exchange search.

The canonical Rust result existed before the Prolog repair. The Prolog lane was repaired until it independently reproduced the same finite rank/basis/exchange result.

## Literature pressure after preseal

The independent candidate structure survived literature contact only after losing novelty in its combinatorial core.

### Prior-art / novelty-kill role

Classical model-discrimination design already treats rival models as objects to be separated by informative experiments.

Minimum-test-cover sensor placement already formulates minimum sensor selection for fault isolability as a combinatorial cover problem.

Therefore MQR-4.41 does **not** claim invention of minimum distinguishing-test selection.

### Machinery / boundary role

Controlled-sensing work makes explicit that sensing modes differ in information and cost, reinforcing the separation between:
- cardinality of a covering basis;
- information quality;
- resource cost;
- sequential sensing policy.

### Residual MQR contribution

The surviving contribution is constitutional:

1. contact rank is indexed to a claim/rival/query/root surface;
2. analyst-declared empirical degrees are not primitive;
3. incidence-preserving reparameterization may preserve FCR without licensing ontic invariance;
4. minimum basis nonuniqueness must remain visible;
5. generic matroid exchange is not assumed;
6. cost, robustness, freshness and common-cause independence are separate objectives;
7. root semantics and rival-frontier drift reopen rank;
8. finite minimum does not become final open-world minimality;
9. rank equality does not identify a world ontology.

The literature wins the combinatorial-precedent question because the same mathematical problem was already occupied.

It does not defeat the authority-boundary result because that result is not entailed by the precedence alone; it survives the executable/formal attacks above.

## Research OS sidecar adjudication

The Research OS sidecar supplied four cross-axis attacks after the independent 4.41 candidate had been frozen. They were treated as adversarial probes, not auto-imported doctrine.

### Metrology — PARTIAL / UPSTREAM BOUNDARY

A minimal root cover does not establish that the calibration network or measurement relation making those roots comparable is valid.

```text
TRANSFER != CALIBRATION != EVIDENCE SYNTHESIS
COVER MINIMALITY != CALIBRATION AUTHORITY
```

FCR begins only after an admissible root/separation relation has been constructed. Calibration change may alter separation incidence and therefore reopen rank, but rank cannot self-certify calibration.

### Deep uncertainty — OUTSIDE FCR / NON-INFERENCE

FCR measures descriptive rival-separation burden.

It does not rank action warrant.

A robust decision can be available despite unresolved descriptive rivals under a separate decision contract, and a low FCR cannot be read back as decision permission.

```text
DESCRIPTIVE WARRANT != DECISION WARRANT
```

### Post-selection inference — UNRESOLVED BY STATIC FCR

Exact minimization over the realized WCSH says nothing by itself about whether data-dependent frontier construction, root pruning or edge selection preserved inferential authority.

```text
REALIZED MINIMUM != SELECTION-HISTORY SUFFICIENCY
```

If selection history is authority-relevant and unaccounted, FCR remains a correct optimizer result but not a sufficient scientific-authority receipt.

### Metric / evaluation construction — LOAD-BEARING CONTRACT

The relation `root separates obligation` is not raw ontology. It is evaluated under a metric, threshold, partition, equivalence relation or other discrimination contract.

The same measurement material can therefore produce different FCR values under different separation contracts without the world acquiring or losing dimensions.

```text
MEASUREMENT MATERIAL != EVALUATIVE ORDER != WORLD ORDER
```

The canonical Lean boundary now includes axiom-empty witnesses for all four non-inferences, and v0.8 emits explicit false flags for calibration authority, selection-history sufficiency, decision warrant and evaluation-contract authority.

## Outcome branches

```text
A. INTRINSIC-RANK = REJECTED.

B. DEGREE-RELATIVE = REJECTED AS TOO STRONG.
   Declared-degree rank is representation-dependent, but an incidence-relative
   operational rank survives after replacing degrees with RSOs.

C. SEPARATION-RELATIVE = SUPPORTED.

D. MATROIDAL = REJECTED IN GENERAL.

E. NONMATROIDAL = SUPPORTED.

F. FRONTIER-DYNAMIC = SUPPORTED.

G. OPEN-WORLD-NONFINAL = SUPPORTED.

CANONICAL SYNTHESIS = C + E + F + G
```

## Strongest surviving principle

```text
MINIMAL EXTERNAL CONTACT IS IDENTIFIABLE ONLY RELATIVE TO
A FROZEN SCIENTIFIC DISCRIMINATION PROBLEM.

IT IS NOT AN INTRINSIC RANK OF THE WORLD.
```

Expanded:

```text
claim scope
+ live rival frontier
+ query/intervention class
+ versioned external root universe
+ separation incidence
------------------------------------------------
=> finite minimum external discrimination cover

NOT
=> world dimensionality
=> complete ontology
=> evidence independence
=> optimal experiment
=> final open-world minimum
```

## Verdict

```text
EMPIRICAL-DEGREE-AS-PRIMITIVE=REJECT
RIVAL-SEPARATION-OBLIGATION=ADOPT
WORLD-CONTACT-SEPARATION-HYPERGRAPH=ADOPT
FRONTIER-RELATIVE-CONTACT-RANK=PASS
INCIDENCE-ISOMORPHISM-INVARIANCE=PASS@FROZEN-WCSH
MINIMUM-BASIS-UNIQUENESS=REJECT
GENERIC-MATROID-RANK=REJECT
INSTRUMENT-RELATIVITY=PASS
FRONTIER-EXPANSION-REOPENING=PASS
ROOT-DRIFT-REOPENING=PASS
RANK-CARDINALITY=NOT-COST
LOW-RANK=NOT-INDEPENDENT-EVIDENCE
RANK-EQUALITY=NOT-ONTOLOGY-EQUALITY
FINITE-RANK=NOT-OPEN-WORLD-FINAL
FINAL-TRUTH-DISTANCE=UNIDENTIFIED
OUTCOME=C+E+F+G
GENERATION-IV-CONTINUES
```
