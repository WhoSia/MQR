# MQR-4.35 — Relational-Receipt Collision Search

Status: PRESEALED / OUTCOME-BLIND

## Question

Does the six-coordinate MQR-4.34 relation receipt

`MU(B->D) = {DOMAIN_RELATION, SEMANTIC_MAP, COMPONENT_RELATION, QUOTIENT_RELATION, STATE_RELATION, ENDPOINT_CONTRACT}`

contain enough information to determine the empirically admissible reach of bridge support, or can two worlds with the same full MU require different support reach?

This stage attacks MQR-4.34 rather than protecting it.

## Explanandum lock

The target is **not** raw direct PASS/FAIL and is **not** the authority label compiled by the MQR-4.34 grammar. Those would make a same-MU authority test partly tautological.

For each world `w`, freeze a probe family `P(w)` before direct reveal. Let `m_w(p)` be the bridge-mediated prediction for probe `p`, and `d_w(p)` the independently executed direct result.

Define empirical reach:

- `E0_FULL`: `m_w(p)=d_w(p)` for every frozen core and refinement probe.
- `E1_QUOTIENT_ONLY`: equality on every frozen coarse/core probe but at least one refinement-only probe diverges.
- `E2_NONE`: at least one frozen core probe diverges.
- `E3_UNRESOLVED`: execution or admission failure prevents adjudication.

The empirical reach label is produced only after direct reveal and is independent of the MQR-4.34 authority compiler.

## Primary falsifier

A **relational-receipt collision** exists iff there are admitted worlds `x,y` such that

`MU(x) = MU(y)` but `E(x) != E(y)`.

Any admitted collision defeats the claim that full MQR-4.34 MU is sufficient for empirical support reach on the admitted probe family.

One non-gerrymandered forcing collision is sufficient to defeat **universal** MU sufficiency. Fresh external collisions are required before making a stronger claim about naturalistic prevalence.

## Anti-gerrymandering rule

A forcing collision counts only if the hidden differentiator is independently specified before direct outputs and belongs to one of the following ordinary mechanism classes:

1. map algebra;
2. intervention alignment;
3. sensitivity/support boundary.

Outcome literals, direct-result hashes, case IDs, filenames, timestamps, or hand-written exception lists may not be used as differentiators.

## Predeclared refinement ladder

No post-reveal feature invention is allowed in MQR-4.35.

- `NU0 = MU`.
- `NU1 = MU + MAP_ALGEBRA`, with values `HOMOMORPHIC`, `QUOTIENT_HOMOMORPHIC`, `PARTIAL`, `CONTEXTUAL`, `UNKNOWN`.
- `NU2 = NU1 + INTERVENTION_ALIGNMENT`, with values `COMMUTES_BY_CONSTRUCTION`, `EMPIRICAL_ONLY`, `MISALIGNED`, `UNKNOWN`.
- `NU3 = NU2 + SENSITIVITY_SCOPE`, with values `GLOBAL`, `LOCAL`, `BOUNDARY`, `UNKNOWN`.

These coordinates are mechanism-side descriptors and must be assigned before direct reveal.

## Finite minimality criterion

For an admitted corpus C and frozen empirical reach E, a candidate NU_k is **collision-free on C** iff no two cases share NU_k while differing in E.

The **coarsest observed separating refinement** is the least k in {0,1,2,3} that is collision-free on C.

This is deliberately weaker than a sufficient statistic theorem. It establishes only finite-corpus separation relative to the frozen probe algebra.

## Open-world residue

Even if NU_k is collision-free on every MQR-4.35 case, MQR may not infer universal sufficiency. Future worlds can reveal an unconceived differentiator. A finite corpus can earn only:

`OBSERVED_SEPARATION_UNDER_FROZEN_PROBE_ALGEBRA`

not

`UNIVERSAL_SUFFICIENCY`.

This distinction is constitutive, not a cautionary footnote.

## Forcing court

The forcing court must contain at least three same-MU pairs covering R0, R1 and R2. Each pair must differ in empirical reach by a simple lawful mechanism, not by an outcome lookup table. At least one collision must survive NU1 and at least one must survive NU2, so that the refinement ladder itself is tested rather than ceremonially confirmed.

Expected forcing property, frozen before execution:

- NU0: >=3 collisions;
- NU1: >=2 collisions;
- NU2: >=1 collision;
- NU3: 0 collisions.

If these exact expectations fail, the implementation/constitution is HOLD and no external promotion is allowed.

## Inherited evidence

MQR-4.33 TKN/TOML and MQR-4.34 REGEX/SJSON/UNORM may be used only after this preseal and carry zero fresh promotion credit.

## Fresh-world admission

A fresh external case must have its candidate identity, lineage endpoints, MU/NU1/NU2/NU3 descriptors, probe family and exclusion rule frozen before behavioral reveal. Changelog, issue, commit-message or result-guided candidate selection disqualifies the case from fresh credit.

Candidate families whose behavior-changing release notes were inspected before this preseal are ineligible for fresh credit in 4.35, including `packaging` and `idna`.

## Promotion / defeat logic

1. If forcing court produces a same-MU opposite-E collision: `MU_UNIVERSAL_SUFFICIENCY = FAIL`.
2. If no forcing collision exists: `COURT_INVALID_OR_MU_SURVIVES_FORCING`; inspect exact forcing expectations before any stronger inference.
3. If a predeclared NU_k is the coarsest collision-free refinement on forcing + admitted fresh corpus, it may earn `OBSERVED_SEPARATION_UNDER_FROZEN_PROBE_ALGEBRA` only.
4. Any fresh collision at the selected NU_k defeats that refinement on the observed corpus; no new coordinate may be added in 4.35.
5. Post-reveal retyping of MU/NU coordinates is forbidden.

## Philosophical claim ceiling

MQR-4.35 may distinguish:

- a representation being useful;
- a representation separating an observed corpus;
- a representation being sufficient relative to a specified experiment/probe family;
- universal sufficiency across open-ended future inquiry.

Only the first three can receive positive finite evidence here, and the third requires explicit relativization to the frozen probe family. Universal sufficiency is not promotable in this stage.

## Literature role

Literature may constrain interpretation but receives zero case credit. In particular, the court will distinguish transient/contrastive underdetermination from a global skeptical claim, and will treat new measurements/probes as possible refinements of the evidential partition rather than as retrospective rescue.
