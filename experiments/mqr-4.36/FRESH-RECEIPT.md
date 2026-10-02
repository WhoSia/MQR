# MQR-4.36 — Fresh Naturalistic Fiber Receipt

Status: CANONICAL / FRESH NU3 COLLISION FOUND / DECISION-RELATIVE SURVIVAL / INTERNAL RESIDUE ZERO

## Frozen constitution

Primary preseal:
`903374ad64ee3c38f23598b84624166da14f718d`

Candidate manifest:
`0167f4be300b405342451f90db4fdbc8ee1729c4`

Atomic probe registry:
`b060cdb8ee2177f6e9396a322118b2f4a6b9532b`

No candidate, version, probe, adapter, NU3 coordinate or decision map was changed after behavioral reveal.

## Pre-reveal infrastructure failures

The following workflow runs ended before provider execution and therefore exposed no package behavior:

- `36142993145`: manifest-integrity string mismatch;
- `36143144417`: rustfmt-only gate;
- `36143737121`: Clippy type-complexity gate;
- `36143880329`: triggered before the final pre-reveal quality repair and did not establish canonical provider evidence.

Allowed pre-reveal repairs were infrastructure-only:
- manifest grep repair;
- rustfmt-only rewrite;
- a Rust type alias eliminating Clippy type-complexity.

The final pre-reveal implementation repair commit was:
`2ae08754422ed01fc72654599f952b86930afc4a`.

## Canonical first world contact

Run:
`36143991326`

Evidence head:
`2ae08754422ed01fc72654599f952b86930afc4a`

Conclusion:
SUCCESS.

All 12 frozen package-version installations succeeded.

Canonical artifact:
- id: `10868447613`
- name: `mqr-4.36-fresh-naturalistic-receipt`
- artifact digest: `sha256:638b6785870af428393050bbbb4c9818109c6011c852eb2bd413343cac5acd30`

Concatenated raw TSV:
- data rows: 132
- SHA-256: `a04fab623a7302f55e41e9a08d685047c3232b77a2b008888b3feba7254b342e`

## Exact machine adjudication

```text
CASE=JSCHEMA-001  FIBER=F-R1  ADMITTED=true  REACH=E1_QUOTIENT_ONLY  D36=ACTION_CORE_ONLY  D36_CORE=ALLOW_CORE_REUSE
CASE=OASV-001     FIBER=F-R1  ADMITTED=true  REACH=E0_FULL           D36=ACTION_FULL_REUSE  D36_CORE=ALLOW_CORE_REUSE
CASE=UCD2-001     FIBER=F-R2  ADMITTED=true  REACH=E1_QUOTIENT_ONLY D36=ACTION_CORE_ONLY  D36_CORE=ALLOW_CORE_REUSE
CASE=WCWIDTH-001  FIBER=F-R2  ADMITTED=true  REACH=E1_QUOTIENT_ONLY D36=ACTION_CORE_ONLY  D36_CORE=ALLOW_CORE_REUSE

NU3_COLLISION_FIBER=F-R1
REACHES=E0_FULL,E1_QUOTIENT_ONLY

FRESH_CASES=4
FRESH_LINEAGE_KINDS=1
FRESH_RESEARCH_LAB_N=0
NU3_FRESH_E_COLLISION_FIBERS=1
D36_COLLISION_FIBERS=1
D36_CORE_COLLISION_FIBERS=0
EXECUTED_ATOMIC_ROWS=132
UNRESOLVED_ATOMIC_ROWS=0
DECLARED_PROBE_CLASS_ENUMERATION=COMPLETE
INTERNAL_RESIDUE_WITHIN_DECLARED_PROBE_CLASS=ZERO
OPEN_WORLD_RESIDUE=NOT_ELIMINATED
NU3_NATURALISTIC_SUFFICIENCY=FAIL
NU3_NATURALISTIC_IDENTIFICATION=HOLD
POST_REVEAL_RESCUE=FORBIDDEN
```

## Fresh naturalistic collision

The strict-extension fiber F-R1 was frozen to one exact NU3 receipt:

```text
MU = R1|INCLUSION|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT
MAP_ALGEBRA = PARTIAL
INTERVENTION_ALIGNMENT = EMPIRICAL_ONLY
SENSITIVITY_SCOPE = BOUNDARY
```

Yet:

```text
JSCHEMA-001 -> E1_QUOTIENT_ONLY
OASV-001    -> E0_FULL
```

Therefore the presealed falsifier fires:

```text
NU3_NATURALISTIC_SUFFICIENCY = FAIL
```

This is stronger than the MQR-4.35 forcing defeat because the collision occurs under fresh package behavior rather than only constructed worlds.

## Localized JSCHEMA difference

JSCHEMA-001 A=3.2.0 and C=4.25.1 agree exactly on all six frozen core probes.

On the frozen JSON-Schema-2020-12 refinement probes:
- R01: A=INVALID, C=VALID;
- R02: A=INVALID, C=INVALID;
- R03: A=VALID, C=VALID;
- R04: A=VALID, C=INVALID.

B=4.17.3 agrees with C on those frozen refinement outcomes.

No post-reveal probe was added.

## OASV comparator

OASV-001 matches exactly across A/B/C on all eight frozen probes.

Thus the F-R1 collision is not produced by a shared execution failure or missingness.

## R2 fiber

Both UCD2-001 and WCWIDTH-001 have:
`E1_QUOTIENT_ONLY`.

Their frozen coarse/core behavior survives while successor-sensitive refinement outputs differ.

No same-NU3 E collision appears in F-R2.

## Decision-relative sufficiency

The fine decision D36 is injective over E0/E1/E2/E3.

Because F-R1 contains E0 and E1:

```text
D36_COLLISION_FIBERS=1
```

The coarser frozen decision D36_CORE asks only whether core reuse is permitted:

```text
E0_FULL or E1_QUOTIENT_ONLY -> ALLOW_CORE_REUSE
```

Both F-R1 cases therefore map to the same action:

```text
D36_CORE_COLLISION_FIBERS=0
```

Hence on this fresh corpus:

```text
NU3 exact empirical-reach sufficiency = FAIL
NU3 D36 fine-decision sufficiency = FAIL
NU3 D36_CORE decision-relative sufficiency = NOT_DEFEATED
```

This does not establish universal D36_CORE sufficiency.

## Finite residue result

All 132 frozen atomic execution rows completed with zero unresolved rows.

Therefore the declared finite probe class is exhaustively discharged:

```text
INTERNAL_RESIDUE_WITHIN_DECLARED_PROBE_CLASS = ZERO
```

This result is quantified only over the preregistered finite class.

It does not imply:
- every scientifically relevant probe was represented;
- every future intervention is reducible to the class;
- every successor observable has been anticipated;
- open-world residue is zero.

Therefore simultaneously:

```text
OPEN_WORLD_RESIDUE = NOT_ELIMINATED
```

## Promotion ceiling

The fresh corpus was frozen at:
- N=4;
- domain families=2;
- lineage kinds=1;
- RESEARCH_LAB N=0.

Thus positive NU3 naturalistic identification was impossible under the preseal.

The actual collision gives a stronger negative result:

```text
NU3_NATURALISTIC_SUFFICIENCY = FAIL
NU3_NATURALISTIC_IDENTIFICATION = HOLD
```

No fresh replacement case is allowed.

## Workflow state

After canonical world contact, the provider workflow was frozen to manual replay at:

`5a6efe3efa8ba0c60a0999306dbf552b673ea889`.

No later documentation commit can silently create new canonical world-contact evidence.
