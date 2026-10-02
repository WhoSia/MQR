# MQR-4.64 — Acquisition-Constraint Binding Characterization Result

Status: **QUALIFIED / BINDING-BOUNDARY-EARNED / MQR-SPECIFIC-CONTROLLER-NOT-EARNED / FINAL-SEAL-PENDING**

## Frozen ancestry

- MQR-4.63 canonical parent: `1dc3fcd183631c48d9cabc03b573bfbb8eb1cb9f`
- PRESEAL: `517da250c97c84770be3fae543ba2b6b9a3c0407`
- BINDING-MANIFEST: `3365c6ce4b87c7a9e7281246b3aac1de73c6209a`
- LITERATURE boundary: `4eff4a51fd7cfa58fbf32494760bfe1c4ea4e703`
- finite enumeration freeze: `df14dda7b42d4746d7b6c3100d8d23c1463a3a2e`
- first executable reveal: `3090717f84b5d7d26aaecceebd5f4871fa2e0ac2`
- first reveal run: `36965537337`
- plumbing-only guard repair: `4d28431985a551df3a5f97b35031e0b3086b0c7c`
- frozen minimality audit implementation: `8e69c4d71046fbc282179abc6a8d790889de5cb1`
- full qualification workflow integration: `c139fd32b1265e4c5f2497428442cdeae4a20575`
- full 5-job qualification run: `36965974819`

No action catalog, world flag, baseline weight, typed constraint, classification rule, release rule or scientific threshold changed after executable reveal.

The only first-reveal failure was a literal workflow grep string that did not match the already-frozen PRESEAL wording. The scientific enumeration, independent concordance and deterministic replay passed before that repair.

## Exhaustive finite surface

The frozen study enumerates:
- 16 action types;
- all unordered triples with replacement: 816;
- 32 binary world-flag configurations;
- **26,112 worlds**.

Every world is evaluated under:
- MYOPIC;
- LOOKAHEAD;
- CONSTRAINED;
- DIVERSITY;

against:
- OPR;
- ARR;
- EAI;
- EXTERIOR;
- NEDL.

Total classified world × baseline × constraint cases:
**522,240**.

Rust canonical enumeration and independent Python enumeration agree on the complete count matrix.

Deterministic exact replay: PASS.

## Primary characterization result

The empirical/formal transition is not:

~~~text
DIAGNOSTIC LARGE
=> CONTROLLER
~~~

It is:

~~~text
DIAGNOSTIC VARIATION
!= ACTIVATION

ACTIVATION
!= BINDING

BINDING
!= NONREDUNDANCY

NONREDUNDANCY
!= MQR-SPECIFIC NOVELTY
~~~

A typed diagnostic earns local action-authority candidacy only when:
1. the constraint activates;
2. the baseline-feasible set is actually restricted;
3. the restriction changes future material scientific reachability;
4. the baseline does not already enforce equivalent reachability;
5. activation uses contemporaneously available information;
6. own-ablation changes behavior/reachability;
7. the constraint releases when scarcity/irreversibility/materiality disappears.

## OPR — option preservation

### Against MYOPIC
- DIAGNOSTIC_ONLY: 18,192
- REDUNDANT: 2,960
- BINDING_LOCAL: 4,960

### Against LOOKAHEAD
- DIAGNOSTIC_ONLY: 18,192
- REDUNDANT: 7,020
- BINDING_LOCAL: 900

### Against matched CONSTRAINED baseline
- DIAGNOSTIC_ONLY: 18,192
- **BASELINE_ABSORBED: 7,920**
- **BINDING_LOCAL: 0**

### Against DIVERSITY
- DIAGNOSTIC_ONLY: 18,192
- REDUNDANT: 2,164
- BINDING_LOCAL: 5,756

### Verdict

**OPR has local binding witnesses against weak/soft baselines, but its independent controller authority is absorbed by the matched minimum-separator constrained baseline.**

Thus:

~~~text
OPTION PRESERVATION
CAN BIND

BUT

MINIMUM-SEPARATOR OPR
IS COMPILABLE INTO
ORDINARY CONSTRAINED FEASIBILITY
~~~

OPR does not earn MQR-specific controller promotion.

## NEDL — nonmyopic exploration debt / separator coverage

### Against MYOPIC
- DIAGNOSTIC_ONLY: 16,736
- REDUNDANT: 2,808
- BINDING_LOCAL: 6,568

### Against LOOKAHEAD
- DIAGNOSTIC_ONLY: 16,736
- REDUNDANT: 7,632
- BINDING_LOCAL: 1,744

### Against CONSTRAINED
- DIAGNOSTIC_ONLY: 16,736
- REDUNDANT: 600
- BASELINE_ABSORBED: 6,800
- **BINDING_LOCAL: 1,976**
- OVERCONSTRAINING: 0

### Against DIVERSITY
- DIAGNOSTIC_ONLY: 16,736
- REDUNDANT: 2,196
- BINDING_LOCAL: 7,180

### Strong minimal witness

Frozen strong-baseline witness:

- actions:
  - `A0_HI_DROP`
  - `A1_FULL`
  - `A3_S0_HI`
- irreversible = YES
- separator substitutability = NO
- matched CONSTRAINED baseline chooses `A3_S0_HI`: preserves one separator;
- NEDL constraint chooses `A1_FULL`: preserves both non-substitutable separators.

If separators are made substitutable, the stronger NEDL requirement releases.

### Verdict

**NEDL is locally nonabsorbed by a minimum-one-separator constrained baseline when multiple future separators are genuinely non-substitutable.**

This is the strongest 4.64 positive result.

But:

~~~text
NONABSORBED BY
ONE MATCHED CONSTRAINT

!=

SEMANTICALLY IRREDUCIBLE TO
CONSTRAINED SEQUENTIAL PLANNING
~~~

The finite grammar still represents NEDL as an ordinary state-indexed hard constraint. Therefore no MQR-specific controller novelty is earned.

## ARR — reopening floor

Against CONSTRAINED:
- DIAGNOSTIC_ONLY: 21,576
- REDUNDANT: 424
- BASELINE_ABSORBED: 1,344
- BINDING_LOCAL: 2,320
- **OVERCONSTRAINING: 448**

ARR can bind locally when reopening is declared material, but it also exposes a nonzero overconstraint region.

Verdict:
**BINDING_LOCAL / OVERCONSTRAINT-RISK / NOT MQR-SPECIFICALLY EARNED.**

## EAI — ancestry independence

Against CONSTRAINED:
- DIAGNOSTIC_ONLY: 17,040
- REDUNDANT: 2,016
- BASELINE_ABSORBED: 840
- BINDING_LOCAL: 5,448
- **OVERCONSTRAINING: 768**

Verdict:
**BINDING_LOCAL / OVERCONSTRAINT-RISK / generic state constraint representable in ordinary constrained planning.**

## EXTERIOR — exterior-access floor

Against CONSTRAINED:
- DIAGNOSTIC_ONLY: 17,040
- REDUNDANT: 1,360
- BASELINE_ABSORBED: 840
- BINDING_LOCAL: 6,104
- **OVERCONSTRAINING: 768**

Verdict:
**BINDING_LOCAL / OVERCONSTRAINT-RISK / generic state constraint representable in ordinary constrained planning.**

## Release results

The frozen controls establish:

- OPR releases under reversible action dynamics.
- Separator-preservation debt releases when the allegedly distinct separators are substitutable.
- ARR requires a live reopening contract.
- EAI requires a material independent ancestry route.
- EXTERIOR requires a declared material exterior route.
- oracle-only activation is rejected as ORACLE_DEPENDENT.

Therefore a diagnostic is not entitled to remain a permanent hard constraint after its binding condition disappears.

## Minimality result

Every emitted local witness reduces to a two-action choice:
- baseline action;
- typed-constrained alternative.

The relevant live condition is necessary in the witness:
- OPR / NEDL → irreversibility;
- ARR → live reopening need;
- EAI → live ancestry-independence need;
- EXTERIOR → live exterior-access need.

For the strongest NEDL-vs-CONSTRAINED witness, **non-substitutability** is additionally necessary.

## What 4.64 earns

### Earned

1. **Binding is relational, not intrinsic.**

A diagnostic coordinate is not binding simpliciter. Binding is indexed to:
`world × baseline × constraint × horizon × scientific contract`.

2. **Baseline absorption is a first-class negative result.**

If a competent matched baseline already excludes all typed-violating actions, an MQR controller is redundant even when the underlying diagnostic is scientifically meaningful.

3. **Constraint release is constitutive.**

Reversibility, substitutability or disappearance of the live scientific need can terminate action authority.

4. **Minimal binding witnesses are possible.**

One can exhibit the smallest local action pair and state condition that turns a diagnostic into an action-changing constraint.

5. **Overconstraint must be visible.**

A constraint that binds is not automatically good. ARR/EAI/EXTERIOR all exhibit frozen overconstraint regions under the matched constrained baseline.

6. **NEDL supplies a local nonabsorption witness.**

Preserving all non-substitutable future separators can exceed a minimum-one-separator baseline.

### Not earned

- a universal MQR controller;
- BINDING_STRUCTURAL across heterogeneous natural/scientific world families;
- semantic irreducibility to constrained Bayesian design / CMDP / sequential planning;
- MQR-specific novelty for hard reachability constraints;
- REALACQUIRE v0.30;
- a scalar acquisition score.

## Strongest synthesis

~~~text
DIAGNOSTIC
EARNS ACTION AUTHORITY
ONLY WHEN ITS CONSTRAINT
CHANGES A MATERIAL
FUTURE SCIENTIFIC
REACHABILITY SET

AND IS
NONREDUNDANT,
NONORACULAR,
OWN-ABLATION-ACTIVE,
AND RELEASE-CAPABLE.

BUT

BINDING ACTION AUTHORITY
DOES NOT BY ITSELF
ESTABLISH
MQR-SPECIFIC CONTROL SEMANTICS.
~~~

## Semantic-version decision

**NO REALACQUIRE v0.30 PROMOTION.**

Reason:

~~~text
BINDING BOUNDARY = EARNED
LOCAL NONABSORPTION = EARNED FOR NEDL

BUT

NON-REPRESENTABILITY
BEYOND STRONG
CONSTRAINED PLANNING
= NOT EARNED
~~~

The Rust binding characterizer and independent enumerator remain as reusable study machinery.

## Successor debt

The immediate successor question is representability:

> If a strong constrained sequential planner is given the right state variables and reachability predicates, can every surviving MQR acquisition constraint be compiled into ordinary state/action constraints without loss?

If YES, MQR's acquisition contribution is diagnostic/constitutional rather than a new control formalism.

If NO, the failure of compilation must be demonstrated prospectively and minimally rather than asserted from vocabulary differences.
