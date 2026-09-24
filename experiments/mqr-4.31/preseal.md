# MQR-4.31 — Transport Construct Reconstitution, Target–Evaluability–Survival Decomposition, Untested-vs-Failed Semantics, Componentwise Cross-Regime Transport & Whether T Can Become Externally Valid without Collapsing into Success

Status: ACTIVE / PRESEAL

## Objective
Reconstitute the legacy Real-Language transport axis T after MQR-4.30 showed that a single scalar/ordinal coordinate conflates:
1. what is being transported;
2. whether the target regime was actually evaluable/tested;
3. whether the claim survived conditional on evaluation.

The target is NOT to repair T by changing thresholds.
The target is to determine whether transport should cease to be a scalar axis and become a typed relation.

## Lineage taxonomy
External examples are typed by what they actually are.

RESEARCH_LAB:
scientific/research programmes whose primary outputs are empirical/theoretical research claims.

ENGINEERING_DEVELOPMENT:
software/tool/product development lineages whose outputs are engineering behavior, implementation semantics, regressions, compatibility, or production capability.

METHODOLOGY_DEVELOPMENT:
methods/tooling work whose primary output is a research method or evaluation framework rather than a substantive scientific claim.

OTHER:
explicit fallback; never silently coerced to RESEARCH_LAB.

ChatGPT-Web-HWPX-MCP is frozen as:
LINEAGE_KIND = ENGINEERING_DEVELOPMENT.

It may be used as an external transport case precisely because transport semantics should work outside research.
It must not be called an MQR/HWPX "Lab".

## Discovery vs confirmation
MQR-4.30 mismatches A03/A05/A08 are DISCOVERY ONLY.
They may motivate the new grammar but may not validate it.

Fresh confirmatory cases must come from source files not used in MQR-4.30 profile sealing.

## Transport object
Legacy:
T = one LOW/MID/HIGH/HOLD coordinate.

Candidate successor:
TRANSPORT(component, source_regime -> target_regime) = {
  TARGET,
  EVALUABILITY,
  SURVIVAL,
  RECEIPT
}

### TARGET
An explicit atomic claim component/relation and an explicit regime transition.

A target must identify:
- claim component;
- source regime;
- target regime;
- transition dimension (version/site/population/renderer/task/representation/resource regime/etc.).

If one target contains multiple relations that can differ in transport behavior:
TARGET_GRANULARITY = SPLIT_REQUIRED.

### EVALUABILITY
Exactly one:
- TESTED
- UNTESTED_AVAILABLE
- TARGET_UNAVAILABLE
- OUT_OF_SCOPE

TESTED:
the relevant target regime was instantiated and the component was actually challenged there.

UNTESTED_AVAILABLE:
the target regime existed/was in principle available but this component was not challenged.

TARGET_UNAVAILABLE:
the requested target regime/world could not be instantiated or observed.

OUT_OF_SCOPE:
the claimed transport relation is not part of the authorized claim.

Evaluability is not success.

### SURVIVAL
Defined only when EVALUABILITY=TESTED.

Exactly one:
- SURVIVED
- FAILED
- MIXED_OR_NONATOMIC

SURVIVED:
the atomic component satisfies its frozen survival criterion in the target regime.

FAILED:
the target test was executed and the atomic component violated the frozen survival criterion.

MIXED_OR_NONATOMIC:
the apparent component contains subrelations with different outcomes.
This forces target splitting; it is not averaged.

When EVALUABILITY != TESTED:
SURVIVAL = NA.

## Derived transport authority
For one atomic target cell:

TESTED + SURVIVED -> TRANSPORT_PASS
TESTED + FAILED -> TRANSPORT_FAIL
TESTED + MIXED_OR_NONATOMIC -> SPLIT_REQUIRED
UNTESTED_AVAILABLE -> HOLD_UNTESTED
TARGET_UNAVAILABLE -> HOLD_TARGET_UNAVAILABLE
OUT_OF_SCOPE -> OUT_OF_SCOPE

No scalar averaging.

## Claim-level transport
A claim with multiple transport cells is represented as a transport map.

The claim-level output may be:
- ALL_REQUIRED_CELLS_PASS
- SOME_REQUIRED_CELLS_FAIL
- PARTIAL_WITH_HOLDS
- SPLIT_REQUIRED
- NO_EVALUABLE_TARGET

A single HIGH/MID/LOW number is prohibited for confirmatory adjudication.

## Success-collapse prohibition
Transport survival is not generic success.

A target may have:
- strong world-contact but failed transport;
- successful native performance but no cross-regime transport test;
- transport PASS for one component and FAIL for another;
- transport HOLD despite excellent source-regime performance.

Therefore:
SOURCE_SUCCESS != TRANSPORT_SURVIVAL.
TARGET_SUCCESS != TRANSPORTABILITY unless tied to the same frozen claim component and source->target relation.

## Literature constraints
Pearl & Bareinboim:
transportability is relation- and domain-difference-specific; transport requires explicit assumptions/identification, not superficial similarity.

Vandenberg & Lance:
cross-group/time equivalence cannot be assumed; invariance claims require staged tests and noninvariance can be partial.

Tal:
measurement outcomes must be distinguished from raw indications; calibration is model-mediated and scope-bound.

MQR consequence:
transport evaluability and transport survival are different epistemic states.

## Fresh confirmatory lanes
Lane R — fresh RESEARCH_LAB cases:
- CUBE-REV current validation/gate receipts not used in MQR-4.30.
- EvoNOMOS result seals not used in MQR-4.30.

Lane E — fresh ENGINEERING_DEVELOPMENT cases:
- ChatGPT-Web-HWPX-MCP tracked-resolution native -> round-trip receipts.
- ChatGPT-Web-HWPX-MCP existing group/ungroup native -> round-trip receipts.

The selected files are frozen by path and blob SHA before native status/verdict lines are revealed.

## Blindness
For fresh cases:
1. source files are selected and SHA-frozen;
2. tool-side masking removes status/verdict/conclusion/pass/fail/hold/authority/promotion keys/lines before model inspection;
3. TARGET/EVALUABILITY/SURVIVAL prediction is sealed;
4. only then native outcome labels/full receipts are revealed;
5. no transport cell may be edited after reveal.

## Confirmatory success criteria
C1 — Untested vs failed:
at least one fresh case must distinguish HOLD_UNTESTED or HOLD_TARGET_UNAVAILABLE from TRANSPORT_FAIL exactly.

C2 — Componentwise transport:
at least one fresh case must contain >=2 components whose transport states differ, and the typed map must preserve the difference rather than average it.

C3 — Cross-lineage:
exact transport-state agreement >= 80% over evaluable fresh cells,
with at least one RESEARCH_LAB lineage and one ENGINEERING_DEVELOPMENT lineage represented.

C4 — Engineering non-lab transport:
HWPX cases must be typed ENGINEERING_DEVELOPMENT and must not require scientific-claim semantics to be evaluated.

C5 — Success-collapse attack:
at least two cells must demonstrate that source/native success alone does not determine transport state.

C6 — Discovery repair prohibition:
A03/A05/A08 may be replayed only after fresh confirmation and may not count toward C1-C5.

## Promotion
If C1-C5 pass:
- legacy scalar/ordinal T is DEPRECATED;
- Real-Language transport becomes a typed relation/map;
- Real-Language version increments to v0.3;
- no replacement scalar is introduced.

If fresh confirmation fails:
- legacy T remains HOLD;
- candidate decomposition remains provisional.

## Implementation policy
New MQR executable surfaces default to:
1. Rust canonical implementation when practical;
2. another compiled/static language only when it provides a concrete advantage;
3. Python as independent reference/audit harness, not default canonical engine.

Existing Python code is not mechanically rewritten for appearance.
Migration occurs when a live surface is touched by a successor stage.

Implementation language remains epistemically irrelevant.

## Metaphysical ceiling
Transport authority concerns claim preservation across explicit regimes.
It does not establish final truth, ontology identity, or universal lawhood.
