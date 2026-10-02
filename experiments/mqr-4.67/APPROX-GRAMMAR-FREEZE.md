# MQR-4.67 — Typed Approximation Grammar Freeze

Status: **FROZEN / POST-LITERATURE / PRE-EXECUTABLE-REVEAL**

PRESEAL:
`2be9ea7c9aa94cd36ca3540e3306a193234af84a`

LITERATURE:
`3b4e46fb98196451b45c0eb619a686cb6434e411`

No state bit, event, loss coordinate, observation function, horizon, severity mapping, candidate quotient, budget vector, scalar-attack grid, verdict rule, or Real-Lang packet rule may change after first executable reveal.

## 1. Inherited source machine

4.67 reuses the exact 4.66 9-bit deterministic machine:

`(R0,R1,R2,S0,S1,S2,C,P,X)`

with exactly 512 source states and the same 18 events:

- R0+, R1+, R2+
- R0-, R1-, R2-
- S0+, S1+, S2+
- S0-, S1-, S2-
- P+, P-
- AUDIT
- X+, X-
- NOVELTY

Transitions are byte-for-byte reimplemented from the 4.66 frozen semantics.

This reuse is intentional: 4.67 changes the approximation question, not the source world.

## 2. Typed loss coordinates

For any pair of source states `s,t`, define five coordinate-specific observational semantics.

### SEP — rival/separator capability
Observation:
`SEP_OBS(s) = (u0,u1,u2)`
where
`ui = Ri ∧ ¬Si`.

Event alphabet used for SEP refinement:
all 12 rival/separator set/clear events.

### REOPEN — reason for reopening
Observation:
`REOPEN_OBS(s) = (U>0, C=0)`.

This distinguishes:
- no reopening reason;
- unresolved-rival reason;
- ancestry/provenance reason;
- both.

Event alphabet:
all 18 events.

### PROV — currently exposed ancestry state
Observation:
`PROV_OBS(s) = C`.

Event alphabet:
`P+, P-, AUDIT`.

The P bit is therefore not directly observed; it becomes visible through AUDIT.

### EXT — novelty-route consequence
Observation:
`EXT_OBS(s) = (R2 ∧ ¬S2)`.

Event alphabet:
`X+, X-, NOVELTY, R2+, R2-, S2+, S2-`.

X is not directly observed; it becomes behaviorally visible through NOVELTY.

### RELEASE — release/commit eligibility
Observation:
`RELEASE_OBS(s) = (U=0 ∧ C=1)`.

Event alphabet:
all 18 events.

## 3. Coordinate-specific distinguishability horizon

For each coordinate independently:

- Level 0 partition groups equal current coordinate observations.
- Level k+1 refines each state by:
  - current Level k block;
  - ordered successor Level k blocks under that coordinate's event alphabet.

Compute levels 0 through 4.

For pair `s,t`, define:
`h_i(s,t)`
as the first level 0..4 at which the coordinate partition separates them.

If no separation occurs by Level 4:
`h_i = INF4`.

This is a bounded finite semantic object, not unrestricted future equivalence.

## 4. Frozen severity map

Each coordinate receives:

- `FATAL` if first separated at horizon 0 or 1;
- `MATERIAL` if first separated at horizon 2 or 3;
- `BOUNDED` if first separated at horizon 4;
- `NONE` if not separated through horizon 4.

Ordering for budget comparison only:

`NONE < BOUNDED < MATERIAL < FATAL`.

This ordinal order is coordinate-local.

No cross-coordinate numerical distance is authoritative.

## 5. Candidate quotient family

Exactly seven candidates are tested.

### A0 — FULL
Identity partition over all 512 states.

### A1 — DROP_P
Merge states that differ only in P.
Signature:
all bits except P.

### A2 — DROP_X
Merge states that differ only in X.
Signature:
all bits except X.

### A3 — VISIBLE_7
Merge by:
`(R0,R1,R2,S0,S1,S2,C)`.
Drops P and X.

### A4 — Q2_4.66
The 4.66 one-step authority refinement partition, recomputed independently under inherited semantics.

### A5 — Q3_4.66
The 4.66 three-round authority refinement partition, recomputed independently.

### A6 — CURRENT_AUTHORITY
The 4.66 current-authority Q1 partition.

No candidate is added or removed after reveal.

## 6. Quotient-level loss profile

For each candidate abstraction A:

For every unordered pair of distinct source states merged by A:
- compute the five coordinate severities;
- take the coordinate-wise maximum across all merged pairs.

The abstraction's profile is therefore:

`L(A) = (max SEP, max REOPEN, max PROV, max EXT, max RELEASE)`.

Also record, for each coordinate:
- count of merged pairs at NONE;
- BOUNDED;
- MATERIAL;
- FATAL.

This worst-case profile is deliberately conservative.

## 7. Frozen budget contracts

Three hypothetical contracts are tested.

They are **not** claims about correct scientific preferences.

### B0 — CONSERVATIVE
- SEP ≤ BOUNDED
- REOPEN ≤ BOUNDED
- PROV ≤ BOUNDED
- EXT ≤ BOUNDED
- RELEASE ≤ BOUNDED

### B1 — EXPLORATORY
- SEP ≤ MATERIAL
- REOPEN ≤ BOUNDED
- PROV ≤ BOUNDED
- EXT ≤ MATERIAL
- RELEASE ≤ BOUNDED

### B2 — ARCHIVAL
- SEP ≤ MATERIAL
- REOPEN ≤ MATERIAL
- PROV ≤ NONE
- EXT ≤ MATERIAL
- RELEASE ≤ BOUNDED

The contracts exist to test contract-dependence, not to recommend one.

## 8. Hard vetoes

Independently of budget:

- any RELEASE = FATAL → FORBID_MERGE;
- any REOPEN = FATAL → REEXPAND_REQUIRED;
- any PROV = FATAL → REOPEN_REQUIRED;
- any EXT = FATAL → REOPEN_REQUIRED.

SEP alone has no unconditional hard veto in this frozen Court.

This asymmetry is a hypothesis under test, not a universal rule.

## 9. Componentwise decision compiler

For one abstraction and one budget:

1. if hard veto FORBID_MERGE fires → `FORBID_MERGE`;
2. else if REEXPAND_REQUIRED fires → `REEXPAND_REQUIRED`;
3. else if REOPEN_REQUIRED fires → `REOPEN_REQUIRED`;
4. else if any coordinate exceeds its budget → `HOLD_INCOMPARABLE`;
5. else if any coordinate is non-NONE → `ACCEPT_WITH_AUDIT`;
6. else → `ACCEPT_LOCAL`.

No scalar score is used.

## 10. Compression selector

Within each budget, after componentwise admissibility:

Among candidates with decision:
- ACCEPT_LOCAL
- ACCEPT_WITH_AUDIT

select the one with the fewest quotient blocks.

Tie break:
candidate order A0..A6.

This is a computational compression selector **conditional on the budget contract**.

It is not a universal scientific ranking.

## 11. Scalarization attack

For attack only, encode severity:

- NONE = 0
- BOUNDED = 1
- MATERIAL = 2
- FATAL = 3

Weight grid:
`w_i ∈ {1,2,4}`
for each of five coordinates.

Total:
`3^5 = 243` weight vectors.

For each candidate:
`D_w(A) = Σ_i w_i * severity_i(A)`.

Attack measurements:

1. number of distinct scalar-best candidates across the 243 weights;
2. pairwise candidate preference reversals across admissible weight vectors;
3. whether one weight vector reproduces B0/B1/B2 componentwise selected candidate simultaneously;
4. whether the scalar winner violates a hard veto;
5. whether scalar ranking changes under the alternative monotone encoding:
   NONE=0, BOUNDED=1, MATERIAL=3, FATAL=9.

A failure to find one universal scalar is finite evidence only.

## 12. Sequential accumulation stress

A fixed sequence of candidate abstraction choices is tested:

`A3 → A4 → A3 → A5`.

At each step the quotient-level typed severity is added to a coordinate-local debt counter using:
- NONE +0
- BOUNDED +1
- MATERIAL +2
- FATAL +3

This arithmetic is **within coordinate only**.

Frozen re-expansion thresholds:
- SEP debt ≥ 4
- REOPEN debt ≥ 3
- PROV debt ≥ 2
- EXT debt ≥ 3
- RELEASE debt ≥ 2

Record the first step each coordinate crosses threshold.

These numbers are synthetic stress parameters only.

## 13. Minimal harmful-merge witnesses

For each candidate with at least one MATERIAL/FATAL coordinate:
produce at least one pair:
- merged by the candidate;
- with the candidate's worst coordinate severity;
- plus a shortest distinguishing event word up to horizon 4 for that coordinate.

The witness search must be independently checked.

## 14. Real-Language candidate packet

Header:

`REALAPPROX 0.30-CANDIDATE`

Required fields:

```text
sealed PASS
lineage PASS
audit PASS
evidence_kind <OBSERVED|PROVED|ENUMERATED|SIMULATED|INFERRED|OPEN>

loss_sep <NONE|BOUNDED|MATERIAL|FATAL>
loss_reopen <NONE|BOUNDED|MATERIAL|FATAL>
loss_prov <NONE|BOUNDED|MATERIAL|FATAL>
loss_ext <NONE|BOUNDED|MATERIAL|FATAL>
loss_release <NONE|BOUNDED|MATERIAL|FATAL>

budget_sep <NONE|BOUNDED|MATERIAL|FATAL>
budget_reopen <NONE|BOUNDED|MATERIAL|FATAL>
budget_prov <NONE|BOUNDED|MATERIAL|FATAL>
budget_ext <NONE|BOUNDED|MATERIAL|FATAL>
budget_release <NONE|BOUNDED|MATERIAL|FATAL>

debt_sep <nonnegative integer>
debt_reopen <nonnegative integer>
debt_prov <nonnegative integer>
debt_ext <nonnegative integer>
debt_release <nonnegative integer>

merge_ancestry <token>
scalar_mode OFF
END
```

The compiler emits:
- typed loss receipt;
- budget exceedance flags;
- hard-veto flags;
- approximation.decision;
- reopen/reexpand flags;
- scalar authority OFF;
- evidence kind;
- simulation-world-authority ceiling.

If `evidence_kind=SIMULATED`:
`approximation.world_validity=NOT_ESTABLISHED`.

If `scalar_mode != OFF`:
the candidate compiler rejects the packet.

## 15. Real-Lang implementation lanes

### Rust canonical candidate
`language/real/src/approx_v30.rs`
binary:
`real-v30-approx`.

### Prolog independent evaluator
`language/real/prolog/approx_v30.pl`.

### Lean boundary
Prove only:
- coordinatewise budget satisfaction is preserved under coordinatewise weakening of loss;
- a hard-veto coordinate cannot become admissible merely because unrelated coordinates improve;
- no theorem assumes a cross-coordinate scalar.

Lean does not prove that the chosen coordinate ontology is scientifically correct.

## 16. Court implementation lanes

### Haskell canonical finite court
Computes:
- coordinate refinement levels;
- all candidate partitions;
- typed pair-loss census;
- quotient worst-case profiles;
- budget decisions;
- scalar attack;
- debt stress.

### C++ independent census
Reimplements the same frozen Court from scratch.

Exact summary/profile concordance required.

## 17. Naturalistic lane

Naturalistic transport is mandatory for promotion, not for finite-Court execution.

Before v0.30 promotion:
- either identify a source-backed naturalistic case with real provenance/reopening/state-aliasing content;
- or record `NATURALISTIC_TRANSPORT_HOLD`.

No synthetic case may substitute for this gate.

## 18. Frozen verdict family

- `BASELINE_ABSORBED`
- `TYPED_LOSS_SURVIVES_LOCALLY`
- `SCALARIZATION_NONUNIQUE_FINITE`
- `SCALARIZATION_SUFFICIENT_ON_FROZEN_SURFACE`
- `HARD_VETO_NOT_SCALAR_SAFE`
- `BUDGET_CONTRACT_DEPENDENT`
- `SEQUENTIAL_LOSS_REEXPANSION_TRIGGERED`
- `APPROXIMATION_ALWAYS_REJECTED`
- `APPROXIMATION_LOCALLY_ADMISSIBLE`
- `NATURALISTIC_TRANSPORT_HOLD`
- `REALAPPROX_CANDIDATE_VALIDATED`
- `NO_V030_PROMOTION`
- `V030_PROMOTION_EARNED`

No target verdict is predeclared.
