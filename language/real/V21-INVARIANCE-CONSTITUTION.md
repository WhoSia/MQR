# Real-Language v0.21 — World-Contact Invariance Constitution

Status: **PROMOTED-LIVE / MQR-4.54 / QUALIFYING-COURT+PROOF+INTEGRATED-CI-PASS / FINAL-SAME-HEAD-SEAL-PENDING**

## Purpose

REALINVARIANCE 0.21 makes the constitution of scientific sameness explicit.

It does not ask only whether a quantity is invariant under a transformation. It records the contract under which a transformation grammar is currently licensed as inert.

## Packet

~~~text
REALINVARIANCE 0.21
id <token>
target PROGRESS | MEASUREMENT | CAUSAL | REPRESENTATION | OTHER
grammar GROUP | GROUPOID | PSEUDOGROUP | MONOID | PARTIAL_FAMILY
scope SUBSYSTEM | COMPOSITE | GLOBAL
probe_preservation PASS | FAIL | UNKNOWN
intervention_preservation PASS | FAIL | UNKNOWN
composition_status PASS | FAIL | PARTIAL_VERIFIED | UNKNOWN
defeat_preservation PASS | FAIL | UNKNOWN
embedding_status PASS | LOCAL_ONLY | FAIL | UNKNOWN
morphism_integrity PASS | FAIL | UNKNOWN
preseal_provenance SEALED | POSTHOC
reopening ACTIVE | INACTIVE
END
~~~

## Constitutional distinction

~~~text
ACTUAL CONSEQUENCE-PRESERVING TRANSFORMATION
!=
TRANSFORMATION CERTIFIED INERT
UNDER THE DECLARED CONTRACT
~~~

A set of generators that passes isolated checks is not promoted to a symmetry group unless the claimed composition/closure obligations are also discharged.

## Grammar typing

A global group is not the default representation.

- `GROUP` — globally defined invertible action at the declared domain;
- `GROUPOID` — typed local arrows with object-dependent composition;
- `PSEUDOGROUP` — locally defined invertible transformations with restriction/gluing structure;
- `MONOID` — compositional transformations where inverse authority is not claimed;
- `PARTIAL_FAMILY` — a deliberately weaker family with only explicitly verified local composition.

The language does not infer mathematical structure beyond the declared and checked receipt.

## Admissibility

A receipt is executable-local-admissible only when:
- probe, intervention and defeat preservation pass;
- the declared grammar's closure obligation is adequate;
- the embedding claim is no stronger than the evidence;
- morphism admission has integrity;
- the constitution was presealed rather than selected post hoc;
- reopening is active.

For `PARTIAL_FAMILY`, `PARTIAL_VERIFIED` composition may be enough because no stronger closure is claimed.

For a `GLOBAL` scope, `LOCAL_ONLY` embedding support is insufficient.

## Diagnostics

The canonical evaluator may emit:
- `OVER_QUOTIENT`
- `PROBE_FAILURE`
- `CLOSURE_FAILURE`
- `DEFEAT_ERASURE`
- `SCOPE_EXPORT_FAILURE`
- `MORPHISM_CAPTURE`
- `CONSTITUTION_CAPTURE`
- `REOPENING_FAILURE`
- `ADMISSIBLE_LOCAL`

These diagnose receipt failure modes. They are not metaphysical classifications of all possible equivalence relations.

## Global receipt is not unique-global authority

A globally scoped packet can earn:

~~~text
invariance.global_transport=YES_WITHIN_DECLARED_SCOPE
~~~

while the evaluator still emits:

~~~text
invariance.unique_global_constitution=NOT_EARNED
~~~

This is deliberate. One successful global-scope receipt does not establish that every rival constitution has been defeated.

## WCICR

The live executable object is the **World-Contact Invariance Constitution Receipt (WCICR)**.

A successful packet earns only a local/scoped candidate receipt:

~~~text
invariance.wcicr=EARNED_LOCAL_CANDIDATE
~~~

WCICR has passed the qualifying MQR-4.54 Court, dedicated Lean+nanoda boundary, integrated Real-Language CI and integrated Lean+nanoda replay. Final stage closure still requires the same-head final seal.

## Reopening

A later fresh intervention may split an earlier equivalence class.

If the earlier receipt:
- declared its scope,
- preserved raw/reconstructible provenance,
- and kept reopening active,

then the successor state is a refinement of authority rather than evidence that the earlier scoped receipt was fabricated.

## Claim ceiling

REALINVARIANCE 0.21 does not establish:
- a uniquely correct global ontology;
- a uniquely privileged equivalence relation;
- completeness of the current probe or intervention family;
- physical equivalence from formal equivalence alone;
- final termination of meta-level justification.

It exposes and audits the constitution under which invariance claims are currently made.
