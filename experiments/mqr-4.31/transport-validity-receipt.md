# MQR-4.31 — Transport Construct Reconstitution Receipt

Status: LEGACY T DEPRECATED / TYPED TRANSPORT RELATION PASS / REAL-LANGUAGE v0.3 LIVE

## Stage
MQR-4.31 — Transport Construct Reconstitution, Target–Evaluability–Survival Decomposition, Untested-vs-Failed Semantics, Componentwise Cross-Regime Transport & Whether T Can Become Externally Valid without Collapsing into Success

## Problem inherited from MQR-4.30
The legacy Real-Language T coordinate matched only 5/8 external judgments.

The three canonical mismatch types were:
1. mixed claim-component transport compressed into one score;
2. tested-and-defeated transport confused with unscored/unevaluated transport;
3. untested transport confused with low transport.

Therefore MQR-4.31 did not retune T.
It reconstituted the construct.

## Preseal
Preseal commit:
d182b76aa2e9cab13580cef306ed00fe9b5a63b8

Fresh source manifest initial seal:
01f4775c7460f1ad95cc9d12a2962d5b1a763caf

Fresh source manifest was extended before opening added results as masking weaknesses were discovered.
Latest pre-reveal candidate-manifest commit:
36a045601d1689b3b96700c66b4a5adcca7180d3

## Lineage taxonomy
Frozen kinds:
- RESEARCH_LAB
- ENGINEERING_DEVELOPMENT
- METHODOLOGY_DEVELOPMENT
- OTHER

ChatGPT-Web-HWPX-MCP is:
ENGINEERING_DEVELOPMENT.

It is not an HWPX Lab.

It remains a valuable external transport case because the target construct should work for engineering/development behavior as well as scientific research.

## Masking self-audit
The stage records and excludes imperfectly masked candidates rather than laundering them into confirmation.

Excluded from confirmatory counting:
- MQR-4.30 A03/A05/A08: discovery cases that generated the new decomposition;
- C3X P14/P15: narrative interpretation text leaked through initial masking;
- EPISTEME P22/P23: classification/invariance fields leaked through initial masking;
- EPISTEME P27/P28: native fail-labelled keys leaked through the raw scrubber.

These remain diagnostic/stress evidence only.

Fresh confirmatory seal:
100ab6c9740d01c6222131b737abad74f686ae10

No sealed transport classification was edited after native reveal.

## Candidate successor construct

Transport is no longer a single scalar/ordinal axis.

For an atomic claim component:

TRANSPORT(component, source_regime -> target_regime) = {
  TARGET,
  EVALUABILITY,
  SURVIVAL,
  RECEIPT
}

### Evaluability
- TESTED
- UNTESTED_AVAILABLE
- TARGET_UNAVAILABLE
- OUT_OF_SCOPE

### Survival
Defined only when TESTED:
- SURVIVED
- FAILED
- MIXED_OR_NONATOMIC

Otherwise:
NA.

### Derived transport state

TESTED + SURVIVED
-> TRANSPORT_PASS

TESTED + FAILED
-> TRANSPORT_FAIL

TESTED + MIXED_OR_NONATOMIC
-> SPLIT_REQUIRED

UNTESTED_AVAILABLE
-> HOLD_UNTESTED

TARGET_UNAVAILABLE
-> HOLD_TARGET_UNAVAILABLE

OUT_OF_SCOPE
-> OUT_OF_SCOPE

No averaging is permitted.

## Fresh confirmatory cases

### C3X — RESEARCH_LAB
P12 dual-target instrument receipt.

Source:
frozen_20260810 engine target.

Target:
Stockfish 19 engine target.

Component:
TT-read instrument engagement across MAIN/SUCCESSOR/QSEARCH semantic paths under fixed-node harness.

Sealed:
TESTED + SURVIVED -> TRANSPORT_PASS.

Native reveal:
both targets have:
- patch-packet roundtrip PASS;
- UCI smoke PASS;
- native-sham identity PASS;
- breadth=3 semantic engagement;
- positive semantic-use counts.

Native:
TRANSPORT_PASS.

Agreement:
PASS.

### EPISTEME — RESEARCH_LAB
P30 prospective critical-world contact.

Source:
P29 additive skin+intervention geometry fitted to prior/training-held-out structure.

Target:
six fresh P30 worlds, each with a 32-cell predicted geometry row.

Sealed before native verdict reveal:
all six full-row transport cells = TESTED + FAILED.

Raw independently recomputed row agreement:
- P30W01: 15/32
- P30W02: 13/32
- P30W03: 15/32
- P30W04: 17/32
- P30W05: 17/32
- P30W06: 16/32

Native reveal:
- exact cells = 93/192;
- mismatches = 99/192;
- exact world rows = 0/6;
- native verdict = ADDITIVE_GEOMETRY_DEFEATED_INTERACTION_REQUIRED.

All six:
TRANSPORT_FAIL.

Agreement:
6/6.

### ChatGPT-Web-HWPX-MCP P3.34-R2 — ENGINEERING_DEVELOPMENT
Native tracked-change semantics -> implementation-generated Hancom round-trip.

Sealed components:
- insert-accept: TRANSPORT_PASS;
- insert-reject: TRANSPORT_PASS;
- bounded delete/replace semantics: TRANSPORT_PASS;
- protected/password resolution: HOLD_UNTESTED;
- selective per-change resolution: OUT_OF_SCOPE.

Native reveal:
- insert-accept specimen PASS;
- no insert-reject round-trip specimen;
- delete-reject / replace-accept / replace-reject specimens PASS;
- protected/password resolution remains explicitly held;
- selective per-change resolution remains outside promoted whole-document scope.

Exact:
4/5.

The mismatch:
INSERT-REJECT sealed as TRANSPORT_PASS
but native criterion requires HOLD_UNTESTED.

This mismatch is retained as scientific information.

Lesson:
operation-level reject_all success cannot be inherited by an uninstantiated component-specific specimen.

BROADER OPERATION SUCCESS != COMPONENT-SPECIFIC EVALUABILITY.

### ChatGPT-Web-HWPX-MCP P3.34-R3 — ENGINEERING_DEVELOPMENT
Native group/ungroup semantics -> implementation-generated Hancom round-trip.

- group-existing: TRANSPORT_PASS;
- ungroup-existing: TRANSPORT_PASS;
- ungroup-translated: TRANSPORT_PASS;
- rotated/scaled/nested/mixed-anchor families: OUT_OF_SCOPE.

Native reveal:
all three admitted round-trip cases preserve bounded geometry/topology;
unsupported families remain explicitly outside evidence/production bounds.

Agreement:
4/4.

## Rust canonical evaluator
Package:
experiments/mqr-4.31/rust/

Rust implementation commit:
a937850f1d493259ce48c833b44eb2ca2a1512ae

Workflow:
.github/workflows/mqr-4.31-typed-transport.yml

Workflow commit:
d9a6e0e849987959b07a5cbb6b8e3bf28679eeba

Canonical fresh-confirmation run:
36018530909

Rust:
1.98.1.

Machine output:

CONFIRMATORY_CELLS=16
EXACT_TRANSPORT_STATE_AGREEMENT=15/16
EXACT_TRANSPORT_STATE_RATE=0.937500

LINEAGES=
ENGINEERING_DEVELOPMENT,RESEARCH_LAB

NATIVE_STATES=
HOLD_UNTESTED,
OUT_OF_SCOPE,
TRANSPORT_FAIL,
TRANSPORT_PASS

SUCCESS_COLLAPSE_COUNTEREXAMPLES=7

C1_UNTESTED_VS_FAILED=PASS
C2_COMPONENTWISE_TRANSPORT=PASS
C3_CROSS_LINEAGE_CONCORDANCE=PASS
C4_HWPX_ENGINEERING_NONLAB=PASS
C5_SUCCESS_COLLAPSE_ATTACK=PASS

MQR431_FRESH_CONFIRMATION=PASS
LEGACY_T=DEPRECATE
REAL_LANGUAGE_TRANSPORT=TYPED_RELATION_MAP

## Success-collapse attack
Seven source-side-positive cells do not yield transport PASS:
- six EPISTEME fresh worlds: prior/source additive geometry fit does not survive fresh world contact;
- HWPX protected encoding: native protected artifact exists and encoding is valid, but protected resolution round-trip remains untested.

Therefore:
SOURCE SUCCESS != TRANSPORT SURVIVAL.

Transport does not collapse into generic success.

## Componentwise semantics
Fresh cases contain:
TRANSPORT_PASS,
TRANSPORT_FAIL,
HOLD_UNTESTED,
OUT_OF_SCOPE.

The same engineering operation family can contain both PASS and HOLD/OUT_OF_SCOPE components.

Therefore:
one claim-wide HIGH/MID/LOW transport score is not lossless.

## Literature result
See:
experiments/mqr-4.31/literature-transport-audit.md

Load-bearing literature:
- Pearl & Bareinboim (2011): transportability is relation/domain-difference-specific and requires explicit identification assumptions;
- Vandenberg & Lance (2000): equivalence/invariance must be tested and can be partial;
- Tal (2017): calibration is model-mediated; indications and measurement outcomes must be distinguished.

MQR result:
transport evaluability and transport survival are separate epistemic states.

## Transport graph semantics
Transport is best represented as a directed typed graph.

Nodes:
regime-indexed claim components.

Edges:
explicit tested/untested transport relations with provenance.

Default composition rule:

A->B PASS
AND
B->C PASS
DOES NOT imply
A->C PASS.

Transport composition requires an explicit bridge receipt showing:
- semantic component identity/translation;
- target/source state compatibility at the intermediate node;
- persistence of bridge assumptions;
- no silent loss of successor-only distinctions.

Therefore:
TRANSPORT EDGE COMPOSITION = HOLD BY DEFAULT.

This inherits:
FORMAL COMPOSABILITY != EPISTEMIC COMPOSABILITY.

## Real-Language v0.3
MQR-4.31 promotes Real-Language from v0.2 to v0.3.

Canonical Rust package version:
0.3.0.

v0.2 remains readable for archival reproducibility.

v0.3:
- requires explicit lineage kind;
- retains W/N/I/D;
- forbids legacy axis T;
- represents transport as typed relation entries;
- compiles claim-level transport state without averaging.

Lineage kinds:
- RESEARCH_LAB
- ENGINEERING_DEVELOPMENT
- METHODOLOGY_DEVELOPMENT
- OTHER

Example:
language/real/examples/mqr-4.31-hwpx-transport.real

Negative fixture:
language/real/tests/v03-invalid-legacy-t.real

## Real-Language v0.3 CI
Canonical Rust compiler:
language/real/src/main.rs

Independent Python reference:
language/real/reference.py

CI workflow:
.github/workflows/real-language-ci.yml

Canonical v0.3 CI run:
36019090058

Results:
- Rust v0.3 package build PASS;
- v0.2 historical packet compatibility PASS;
- v0.3 Rust/Python canonical receipt concordance PASS;
- explicit ENGINEERING_DEVELOPMENT lineage PASS;
- legacy.profile.T=DEPRECATED PASS;
- transport.mode=TYPED_RELATION_MAP PASS;
- claim-state PARTIAL_WITH_HOLDS PASS;
- diagnostic scalar disabled for v0.3 PASS;
- Rust rejects v0.3 axis T;
- Python reference rejects v0.3 axis T;
- legacy calibration scorer smoke remains PASS.

## Implementation-language policy
Newly touched executable MQR surfaces default to:
1. Rust canonical implementation when practical;
2. another compiled/static language when a concrete advantage exists;
3. Python as independent reference/audit harness rather than default canonical engine.

Existing Python is not mechanically rewritten merely to change GitHub language statistics.

Migration is successor-driven:
rewrite when a surface becomes live again or a concrete reliability/portability/performance benefit exists.

Implementation language remains epistemically irrelevant.

## Measurement status after MQR-4.31

W:
LEVEL-3 externally calibrated ordinal — retained.

I:
LEVEL-3 externally calibrated ordinal — retained.

N:
LEVEL-3 HOLD — unchanged.

D:
external polarity PASS / Level-3 discriminant HOLD — unchanged.

Legacy T:
DEPRECATED.

Transport:
TYPED RELATION MAP — fresh external cross-lineage confirmation PASS.

Numeric cross-domain transport scale:
NOT DEFINED.

Scalar truth-proximity:
OFF.

FINAL_TRUTH_DISTANCE:
UNIDENTIFIED.

## Philosophical result
MQR-4.31 shows that transport is not a degree of generic success.

The relevant questions are:
- what exact component is being moved;
- from which regime to which regime;
- whether the target was actually instantiated and challenged;
- what happened conditional on that challenge.

Absence of a test is not negative evidence.
A failed test is not missingness.
A mixed result is not an average.
Success elsewhere does not substitute for target contact.

The engineering case matters precisely because the same transport constitution works outside substantive science without converting engineering development into a research Lab.

## Verdict
TRANSPORT-CONSTRUCT-RECONSTITUTION-PASS /
FRESH-CONFIRMATION-15-OF-16 /
93.75-PERCENT-EXACT-TYPED-STATE-CONCORDANCE /
UNTESTED-VS-FAILED-SEPARATION-PASS /
COMPONENTWISE-TRANSPORT-PASS /
CROSS-LINEAGE-RESEARCH-PLUS-ENGINEERING-PASS /
HWPX-EXPLICIT-ENGINEERING-DEVELOPMENT-NONLAB /
SUCCESS-COLLAPSE-ATTACK-PASS /
OPERATION-SUCCESS-DOES-NOT-LAUNDER-COMPONENT-EVALUABILITY /
LEGACY-T-DEPRECATED /
TYPED-TRANSPORT-RELATION-MAP-PASS /
TRANSPORT-EDGE-COMPOSITION-HOLD-BY-DEFAULT /
REAL-LANGUAGE-V0.3-LIVE /
RUST-FIRST-CANONICAL-MIGRATION-POLICY-ADOPTED /
V0.2-ARCHIVAL-COMPATIBILITY-PASS /
RUST-PYTHON-V0.3-CONCORDANCE-PASS /
NO-TRANSPORT-SCALAR /
NO-TRUTH-SCALAR-RESURRECTION /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
