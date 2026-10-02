# Real-Language v0.8 — Frontier-Relative Contact Rank

Status: EXECUTABLE / MQR-4.41 / FRONTIER-RELATIVE / INSTRUMENT-RELATIVE / NON-ONTIC

## Purpose

v0.8 replaces the v0.7 primitive of analyst-declared empirical degrees for minimum-basis reasoning.

It represents a finite scientific discrimination problem using:
- claim scope;
- rival frontier;
- query/intervention class;
- external root universe;
- rival-separation obligations;
- root-to-obligation separation incidence.

The compiler computes an exact finite minimum external discrimination cover.

## Primitive objects

### Rival-Separation Obligation

An obligation records a distinction among live rivals that the claim must be able to expose.

It is not asserted to be an ontic coordinate.

### World-Contact Separation Hypergraph

```text
root --separates--> obligation
```

Only LIVE EXTERNAL roots are eligible for the canonical rank.

### Frontier-Relative Contact Rank

```text
rho = minimum number of eligible external roots
      whose union of separation edges covers every declared live obligation.
```

If no cover exists, the result is UNCOVERED.

## Nonclaims

`rank.minimum` is not:
- a causal dimension;
- a number of mechanisms;
- a truth score;
- evidence-route independence;
- a cost optimum;
- a robustness optimum;
- a final open-world minimum.

## Minimum basis family

v0.8 enumerates all minimum-cardinality bases for small frozen finite courts.

A minimum rank does not imply a unique basis.

The minimum basis family need not satisfy matroid basis exchange.

## Costs

Root cost is recorded separately.

The checker reports minimum and maximum cost among minimum-cardinality bases.

It does not collapse cardinality and cost into one scalar.

## Dynamics

A rank receipt is invalidated when its load-bearing:
- rival frontier;
- query/intervention class;
- root universe;
- root semantic version/freshness;
- or separation incidence

changes.

Frontier expansion or root drift can increase rank.

New external instrumentation can decrease rank.

Therefore rank history is not an ontic monotone.

## Representation boundary

Incidence-isomorphic finite WCSHs preserve the finite rank result.

This does not mean all scientific reparameterizations are innocuous. A change that alters which rivals matter, what queries are load-bearing, or which root distinguishes what is a new court surface.

## Grammar

```text
REALCONTACTRANK 0.8
id <id>
claim_scope <scope>
frontier <frontier-id>
query_class <query-class-id>

root <id> EXTERNAL|INTERNAL LIVE|STALE|EXPIRED
cost <root> <nonnegative integer>

obligation <id>
separates <root> <obligation>

authorize_rank <integer|UNCOVERED>
authorize_unique YES|NO
authorize_exchange PASS|FAIL|VACUOUS|UNAVAILABLE
END
```

## Canonical implementation

- Rust: `src/contact_rank_v08.rs` / `real-v08-rank`
- independent relational evaluator: `prolog/contact_rank_v08.pl`
- Lean: `lean/MQR/ContactRank.lean`

Rust/Prolog agreement is implementation-diversity evidence only.

Lean proves finite structural/countermodel claims only.

None of the implementations certifies that the supplied rival frontier is complete.

## Canonical meaning

```text
rank.meaning=FROZEN_FRONTIER_MINIMUM_EXTERNAL_DISCRIMINATION_COVER
rank.frontier_relative=true
rank.instrument_relative=true
rank.ontic_dimension=false
rank.degree_ontology_primitive=false
rank.cost_objective=SEPARATE
rank.open_world_final=false
rank.common_cause_independence_inferred=false
```

## Scientific ceiling

```text
OPTIMIZER COMPLETENESS != FRONTIER COMPLETENESS
MINIMUM COVER != WORLD DIMENSION
LOW ROOT COUNT != INDEPENDENT EVIDENCE
SAME RANK != SAME ONTOLOGY
FINITE MINIMUM != FINAL OPEN-WORLD MINIMUM
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```


## Research OS cross-axis boundary

MQR-4.41 separately stress-tested four operations that can be hidden behind an apparently clean rank result.

### Calibration / metrology

Root material and minimum coverage do not establish calibration authority.

A root may enter FCR only after whatever calibration/comparability warrant makes its separation edges admissible. FCR does not manufacture that warrant.

```text
COVER MINIMALITY != CALIBRATION AUTHORITY
```

### Evaluation / metric construction

The separation incidence is produced under an evaluation contract: metric, threshold, partition, equivalence relation, or other rule declaring what counts as discrimination.

The same measurement material can support different finite ranks under different admissible separation contracts.

Therefore that contract is load-bearing provenance even though v0.8 does not convert it into an ontic coordinate.

### Post-selection

Exact minimality over the realized WCSH does not establish that a data-dependent procedure which selected the frontier, roots, or edges preserved inferential authority.

```text
REALIZED MINIMUM != SELECTION-HISTORY SUFFICIENCY
```

Selection history is an upstream authority problem, not something solved by the rank optimizer.

### Decision warrant

FCR is a descriptive discrimination burden. It does not order decision warrant.

A robust action may be available despite unresolved descriptive rivals under an explicit decision contract. Conversely, a low contact rank does not automatically license action.

```text
DESCRIPTIVE CONTACT RANK != DECISION WARRANT
```

Canonical non-inference outputs:

```text
rank.calibration_authority_inferred=false
rank.selection_history_sufficiency_inferred=false
rank.decision_warrant_inferred=false
rank.evaluation_contract_authority_inferred=false
```
