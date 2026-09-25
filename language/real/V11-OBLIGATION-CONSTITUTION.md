# Real-Language v0.11 — Exploration-Obligation Constitution

Status: EXECUTABLE CANDIDATE / MQR-4.44 / OPEN-WORLD / PARTITION-AUDITED

## Boundary

MQR-4.43 governed finite attention relative to a declared obligation set. MQR-4.44 moves one level upstream and asks whether that obligation set itself can be treated as epistemically legitimate.

v0.11 does not make agenda choice value-free and does not identify a complete obligation ontology. It evaluates a declared Exploration-Obligation Constitution Receipt (EOCR).

## Canonical objects

- EOCR — Exploration-Obligation Constitution Receipt
- SBA — Search-Burden Atom
- OBM — Obligation-Burden Map
- APG — Agenda Provenance Graph
- SCW — Successor-Coverage Witness
- ODCL — Obligation Debt Continuity Ledger
- CAE — Constitution Admissibility Envelope

## Core rule

```text
OBLIGATION LABEL COUNT != SEARCH BURDEN
```

The same declared burden may be represented as one merged obligation or several split obligations. v0.11 therefore exposes the sorted declared burden union and rejects obligation count as an adequacy primitive.

## Grammar

```text
REALCONSTITUTE 0.11
id <id>
claim_scope <scope>
agenda_source <id> <ancestry> <ENDOGENOUS|EXTERNAL|MIXED>
burden <id> <GENERATOR|QUERY|REPRESENTATION|INSTRUMENT|RESIDUAL|EXTERNAL_CASE>
obligation <id> <source> <MANDATORY|OPTIONAL> <burden+...>
predecessor <id> <burden+...> <DEBT|CLEAR>
successor <predecessor> <obligation+...>
withdraw <predecessor> <DECLARED|NONE>
debt_transfer <predecessor> <obligation+...>
challenge_route <LIVE|ABSENT>
escape_burden <burden|NONE>
witness_omitted_burden <token|NONE>
authorize_...
END
```

The witness-only omitted burden is excluded from the `constitution.*` decision surface.

## Successor semantics

A successor label is not enough. For every declared successor claim, the union of successor burdens must cover the predecessor burden.

For a predecessor carrying debt, full successor coverage still does not discharge debt. The receipt must either:

- declare an explicit withdrawal; or
- carry a `debt_transfer` whose successor burden union covers the predecessor burden.

Thus:

```text
SUCCESSOR COVERAGE != DEBT DISCHARGE
RENAME != DEBT RETIREMENT
```

## Provenance semantics

v0.11 reports agenda-source count and ancestry count separately.

```text
SOURCE COUNT != AGENDA-ANCESTRY DIVERSITY
```

Endogenous-only agenda formation and external provenance are both allowed as declared states. Neither becomes a truth oracle.

## Constitution admissibility

The implemented CAE is a membership predicate, not an optimizer.

A packet is admissible only when:

- the challenge route is LIVE;
- all declared burdens are covered by current obligations;
- all successor claims preserve predecessor burden;
- no predecessor debt is laundered;
- no frontier escape currently requires reconstitution.

Common-mode provenance or endogenous-only formation is exposed but is not itself an automatic FAIL.

## Hard guards

```text
constitution.partition_count_authority=REJECT
constitution.partition_audit_surface=DECLARED_BURDEN_UNION
constitution.external_source_truth_oracle=NO
constitution.endogenous_source_truth_oracle=NO
constitution.world_obligation_complete=NO
constitution.burden_atom_ontology_complete=NO
constitution.omitted_burden_inferred=NO
constitution.open_world_receipt=REQUIRED
constitution.guidance_mode=CONTRACT_RELATIVE_CONSTITUTIONAL
constitution.reopen_on_escape=YES
```

## Meaning

```text
AUDIT WHAT THE OBLIGATION ACTUALLY COVERS,
NOT HOW MANY LABELS IT HAS.

TRACK WHO CONSTITUTED IT AND FROM WHICH ANCESTRY.

DO NOT LET SUCCESSOR LABELS, RENAMES OR DELETIONS
ERASE PREDECESSOR BURDEN OR DEBT.

AND DO NOT TURN A FINITE PASSING CONSTITUTION
INTO A COMPLETE ONTOLOGY OF WHAT SCIENCE OUGHT TO SEARCH.
```
