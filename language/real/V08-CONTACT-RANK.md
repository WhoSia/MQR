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
