# Real-Language v0.17 — Constitutional Regress Boundary

Status: EXECUTABLE / MQR-4.50 ACTIVE / OPERATIONAL-FIXED-POINT / SCOPE-PROVENANCED / CRITERION-SENSITIVE / DECISION-CONTRACT-INDEXED / REOPENABLE

## Boundary

v0.16 makes defeat content a claim- and challenge-relative counterfactual role rather than a final error atom.

v0.17 asks when the recursive audit of those constitutions may stop for a current scientific purpose without claiming either a final ontology or a completed regress.

## Canonical objects

- CRBR — Constitutional Regress Boundary Receipt
- OQSC — Operational Quotient Sufficiency Certificate
- CSPR — Claim-Scope Provenance Receipt
- SECS — Scope-Endogeneity / Capture Sentinel
- MCRR — Meta-Criterion Recursion Receipt
- CSE — Criterion-Sensitivity Envelope
- WCTR — World-Contact Termination Receipt
- RFPS — Reopening Fixed-Point State
- RDL — Refinement Debt Ledger
- RAR — Reopening Activation Receipt

## Core distinction

```text
METAPHYSICAL TERMINATION
!=
OPERATIONAL TERMINATION

CURRENT FIXED POINT
!=
GLOBAL FIXED POINT

REGISTERED-REFINEMENT STABILITY
!=
FUTURE REFINEMENT-SPACE COMPLETENESS

DESCRIPTIVE SUFFICIENCY
!=
UNIVERSAL ACTION WARRANT
```

## Operational-quotient sufficiency

An operational stop is admissible only when:
- claim scope is nonvacuous and prospectively frozen or prospectively revised;
- challenge and world-contact families are nonempty;
- every registered refinement is replayed;
- no replayed refinement changes defeat, discrimination, or decision-relevant authority;
- every registered materiality criterion classifies every registered refinement as inert;
- no material or unknown live debt remains;
- no criterion is introduced post-outcome or supported only by a meta-cycle;
- no direct/composed path conflict is live;
- no new contact or criterion breaks the envelope.

The evaluator deliberately treats this as a *local authorization state*.

## Action boundary

Action authority additionally requires an explicit decision/use contract and action invariance under that contract.

```text
ACTION INVARIANCE UNDER D
!=
UNIVERSAL ACTION WARRANT
```

A changed decision contract reopens the receipt.

## Hard guards

```text
regress.metaphysical_termination=NO
regress.final_ontology_inferred=NO
regress.future_refinement_space_closed=NO
regress.stop_rule_truth_oracle=NO
regress.claim_scope_truth_oracle=NO
regress.meta_criterion_truth_oracle=NO
regress.operational_stop_permanent=NO
regress.reopening_reserve=ACTIVE
regress.guidance_mode=REOPENABLE_OPERATIONAL_FIXED_POINT
```

## Relation to the pre-existing Meta-Regress Boundary

Earlier MQR doctrine already allowed an operational boundary to remain at explicit HOLD with finite unresolved meta-debt rather than inventing an infinite completed regress or a final meta-standard.

v0.17 does **not** claim novelty for that possibility.

The new target is stricter and positive:

```text
EXPLICIT UNRESOLVED MATERIAL META-DEBT
-> HOLD IS LEGITIMATE

NO LIVE MATERIAL DEBT
+ NONVACUOUS FROZEN SURFACE
+ REPLAYED INERT REFINEMENTS
+ CRITERION-ROBUSTNESS
+ WORLD-CONTACT REOPENABILITY
-> SCOPED OPERATIONAL AUTHORIZATION MAY BE LEGITIMATE
```

## Grammar

```text
REALREGRESS 0.17
id <id>
claim_scope <scope>
scope_timing <FROZEN|PROSPECTIVE_REVISION|POST_OUTCOME_REVISION>
scope_nonvacuous <YES|NO>
challenge <id>
world_contact <id>
decision_contract <id|NONE>
action_invariant <YES|NO>
decision_contract_change <YES|NO>
stability_rounds <nat>
refinement <id> <REPLAYED|DEFERRED|UNEXECUTED> <INERT|CHANGES_DEFEAT|CHANGES_DISCRIMINATION|CHANGES_DECISION|UNKNOWN>
criterion <id> <PROSPECTIVE|INHERITED|POST_OUTCOME> <INDEPENDENT|DEPENDENT|CYCLIC>
criterion_verdict <criterion> <refinement> <INERT|MATERIAL|UNKNOWN>
debt <id> <MATERIAL|NONMATERIAL|UNKNOWN> <LIVE|RESOLVED>
path <id> <PASS|HOLD|REOPEN>
new_contact <id> <INERT|DISTINGUISHES>
new_criterion <id> <AGREES|BREAKS>
END
```

## Canonical states

```text
AUTHORIZED_CRITERION_ROBUST_OPERATIONAL_STOP
AUTHORIZED_ACTION_UNDER_DECLARED_CONTRACT
HOLD_PREMATURE_TERMINATION
HOLD_LIVE_REFINEMENT_DEBT
HOLD_SCOPE_CAPTURE
HOLD_META_CRITERION_CAPTURE
HOLD_META_CRITERION_NONINVARIANCE
HOLD_META_CYCLE
HOLD_VACUOUS_TERMINATION
REOPEN_NEW_WORLD_CONTACT
REOPEN_DECISION_CONTRACT_CHANGE
REOPEN_CRITERION_ENVELOPE
REOPEN_REGRESS_PATH_CONFLICT
```

These are governance states, not truth values.

## Implementation

- canonical evaluator: Rust `src/regress_v17.rs` / `real-v17-regress`
- independent relational evaluator: Prolog `prolog/regress_v17.pl`
- formal finite boundary: Lean `lean/MQR/RegressBoundary.lean`

Rust–Prolog agreement checks the declared receipt semantics only. Lean proves finite countermodels only and is not an empirical or metaphysical oracle.
