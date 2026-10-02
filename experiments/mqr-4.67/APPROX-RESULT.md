# MQR-4.67 — Scientific-Authority Approximation Court Result

Status: **QUALIFIED / APPROXIMATION-NEGATIVE-ON-FROZEN-CANDIDATES / SCALAR-ATTACK-NONIDENTIFYING / REALAPPROX-CANDIDATE-VALIDATED-AS-SOFTWARE / NATURALISTIC-PROV-PARTIAL / NO-v0.30-PROMOTION / FINAL-SEAL-PENDING**

## Evidence discipline

Every claim below remains typed as:

- **OBSERVED**
- **PROVED**
- **ENUMERATED**
- **SIMULATED**
- **INFERRED**
- **OPEN**

The Court explicitly rejects:
`SIMULATED = WORLD-TRUE`.

## Frozen ancestry

- MQR-4.66 parent: `7a797e04b90c4a0cad4ed5045fc15f086c0e502c`
- PRESEAL: `2be9ea7c9aa94cd36ca3540e3306a193234af84a`
- LITERATURE: `3b4e46fb98196451b45c0eb619a686cb6434e411`
- APPROX-GRAMMAR-FREEZE: `f3f46ca09320331058686982804bcc5b1ed5e772`
- Rust REALAPPROX candidate: `c6140b075e695b9ca88353b848361bf26803ba0e`
- Prolog REALAPPROX evaluator: `c9903b65fa7664368108568ab47bcea96b1c2bc5`
- Lean approximation boundary: `fb86f01f70e3de19ca264b2309e748c67ea42432`
- Haskell canonical Court: `0045a659d7f861e82249add5fc16d2849afdc066`
- C++ independent Court: `d87acb1ec48c151233a3dae61f1a9e7e826da227`
- pre-reveal Haskell/C++ plumbing commits: `b97d2663cca41b0de0b2c8798f02931774bc3292`, `f46e39ce45fc816e20a6d0ef7141d6daa488f5b5`
- Cargo candidate registration: `ccabe11d6d4d3a535107ce71c1d683d9d854ce57`
- first executable reveal: `60536969221cf396a8bcf0400de320d4cd2db45b`
- first reveal run: `36981160693` — **6/6 SUCCESS**
- naturalistic audit: `bff0dea132c149a0bce7982a1299b54c606b9f3b`

No loss coordinate, severity rule, budget contract, candidate quotient, scalar attack grid, debt threshold or verdict rule changed after first executable reveal.

## Qualification

First reveal run `36981160693`:

1. Haskell canonical Court — **SUCCESS**
2. Haskell↔C++ exact profile/summary concordance — **SUCCESS**
3. REALAPPROX Rust↔Prolog fixture concordance + scalar-mode rejection — **SUCCESS**
4. Lean componentwise boundary — **SUCCESS**
5. deterministic replay — **SUCCESS**
6. structural guards — **SUCCESS**

Implementation agreement is not world validation.

## Frozen candidate result

**ENUMERATED.**

The Court evaluated exactly seven frozen candidate abstractions.

| Candidate | Blocks | Merged pairs | SEP | REOPEN | PROV | EXT | RELEASE |
|---|---:|---:|---|---|---|---|---|
| A0 FULL | 512 | 0 | NONE | NONE | NONE | NONE | NONE |
| A1 DROP_P | 256 | 256 | NONE | FATAL | FATAL | NONE | FATAL |
| A2 DROP_X | 256 | 256 | NONE | FATAL | NONE | FATAL | FATAL |
| A3 VISIBLE_7 | 128 | 768 | NONE | FATAL | FATAL | FATAL | FATAL |
| A4 Q2_4.66 | 319 | 412 | NONE | FATAL | FATAL | MATERIAL | MATERIAL |
| A5 Q3_4.66 | 508 | 4 | NONE | FATAL | FATAL | NONE | BOUNDED |
| A6 CURRENT_AUTHORITY | 5 | 37,360 | FATAL | FATAL | FATAL | FATAL | FATAL |

The loss profile is the coordinate-wise worst case over all state pairs merged by that abstraction.

### Main result

Under the frozen severity semantics, every non-identity candidate has at least one **FATAL** authority-loss coordinate.

Therefore all three frozen budget contracts select:

- B0 CONSERVATIVE → **A0 FULL**
- B1 EXPLORATORY → **A0 FULL**
- B2 ARCHIVAL → **A0 FULL**

Frozen finite verdict:

**APPROXIMATION_ALWAYS_REJECTED_ON_TESTED_CANDIDATES_AND_CONTRACTS**.

This does not prove that no useful approximate quotient exists in general.

It proves only that none of the seven predeclared candidate abstractions is admissible under any of the three predeclared contracts on this finite machine.

## Why approximation failed

**ENUMERATED + INFERRED.**

The failure is not driven by SEP for most candidates.

The dominant failure is the retained future semantics of:
- reopening;
- provenance audit;
- novelty/exterior routes;
- release authority.

Notably:
- A5 Q3_4.66 merges only four pairs and has RELEASE merely BOUNDED, but still has FATAL REOPEN and PROV.
- A4 Q2 has no SEP loss at all, yet FATAL REOPEN/PROV.
- dropping P or X produces immediate downstream authority failures under the inherited AUDIT/NOVELTY machinery.

Thus:

```text
SMALL BEHAVIORAL COMPRESSION ERROR
DOES NOT IMPLY
SMALL SCIENTIFIC-AUTHORITY ERROR
UNDER THIS FROZEN CONTRACT.
```

This is contract-relative, not a theorem about all state abstraction.

## Severity census

**ENUMERATED.**

Examples:

### A1 DROP_P
Among 256 merged pairs:
- PROV: 256 FATAL
- REOPEN: 256 FATAL
- RELEASE: 108 FATAL / 144 MATERIAL / 4 BOUNDED

### A2 DROP_X
Among 256 merged pairs:
- EXT: 192 FATAL / 64 MATERIAL
- REOPEN: 108 FATAL / 144 MATERIAL / 4 BOUNDED
- RELEASE: 54 FATAL / 153 MATERIAL / 38 BOUNDED / 11 NONE

### A5 Q3_4.66
Only four merged pairs:
- REOPEN: 4 FATAL
- PROV: 4 FATAL
- RELEASE: 4 BOUNDED
- SEP/EXT: NONE

This is a particularly sharp finite witness that “almost exact” compression can still merge states separated immediately by a coordinate that the authority contract declares load-bearing.

## Scalarization attack

### Whole candidate family

**ENUMERATED.**

Two monotone severity encodings were tested:
- `NONE=0, BOUNDED=1, MATERIAL=2, FATAL=3`
- `NONE=0, BOUNDED=1, MATERIAL=3, FATAL=9`

For each, all 243 positive weight vectors were tested.

Results for both encodings:
- number of distinct global scalar winners: **1**
- global scalar winner: **A0 FULL**
- weight vectors matching all B0/B1/B2 selections: **243 / 243**

Therefore:

**SCALARIZATION_NONUNIQUE_FINITE is NOT earned for the whole frozen selection problem.**

The scalar baseline is not defeated here.

The reason is structurally simple:
A0 FULL has zero loss in every coordinate and therefore dominates every compressed candidate under every positive monotone weighted sum.

### Compression-candidate internal reversals

**ENUMERATED.**

Despite the global domination by A0, there are **4 pairwise preference reversals** over the 243 weight vectors:

- A1 DROP_P ↔ A2 DROP_X
- A1 DROP_P ↔ A4 Q2
- A2 DROP_X ↔ A4 Q2
- A2 DROP_X ↔ A5 Q3

The same count survives the alternative severity encoding.

This shows only:

> among lossy compression candidates, their scalar ordering depends on coordinate weights.

It does not show:
- scalarization is impossible;
- typed loss is universally superior;
- no utility representation exists.

### Scalar attack verdict

**SCALAR_ATTACK_NONIDENTIFYING_DUE_TO_ZERO_LOSS_FULL_BASELINE**.

This is an important negative result.

4.67 cannot use this Court to justify a universal anti-scalar claim.

## Sequential accumulation stress

Frozen sequence:
`A3 → A4 → A3 → A5`.

**ENUMERATED.**

First debt-threshold crossing steps:
- SEP: none through sequence
- REOPEN: step 1
- PROV: step 1
- EXT: step 1
- RELEASE: step 1

Interpretation:

The intended accumulation question was not identified cleanly because the first abstraction A3 already contributes FATAL-level losses in four coordinates.

Thus:

**SEQUENTIAL_LOSS_REEXPANSION_TRIGGERED**, but
**ACCUMULATION-BEYOND-SINGLE-STEP NOT IDENTIFIED**.

The Court must not claim evidence for gradual accumulation dynamics from this stress sequence.

## Bisimulation / state-abstraction baseline

**OBSERVED from literature.**

Ferns-style bisimulation metrics already provide quantitative approximate state similarity and downstream value-error relationships.

Li–Walsh–Littman and related abstraction literature already cover:
- preservation-dependent abstraction;
- approximate abstraction;
- coarser-compression / looser-bound tradeoffs;
- adaptive aggregation/disaggregation.

Therefore:

**BASELINE_ABSORBED** for generic approximate state compression machinery.

MQR does not earn novelty for:
- approximate quotienting;
- re-expansion itself;
- vector objectives;
- Pareto incomparability;
- weighted metrics;
- error budgets.

## Real-Language candidate

### Technical qualification

**OBSERVED from CI.**

`REALAPPROX 0.30-CANDIDATE`:
- Rust canonical candidate builds;
- independent Prolog evaluator exactly agrees on frozen fixtures;
- scalar_mode other than OFF is mechanically rejected;
- SIMULATED packet emits `world_validity=NOT_ESTABLISHED`;
- global loss score is mechanically forbidden;
- re-expansion fixture emits `REEXPAND_REQUIRED`.

Technical verdict:

**REALAPPROX_CANDIDATE_VALIDATED_AS_SOFTWARE**.

### Critical separation

The positive-control fixture:

`mqr-4.67-simulated-local.real`

returns `ACCEPT_WITH_AUDIT`.

But this fixture is **SIMULATED / hand-constructed software test input**.

It is not the output of the finite Court and is not empirical evidence that an admissible lossy scientific compression exists.

In fact, the actual frozen Court found no admissible compressed candidate.

Therefore:

```text
SOFTWARE CAN REPRESENT
AN ADMISSIBLE TYPED-LOSS RECEIPT

!=

THE SCIENTIFIC COURT FOUND
AN ADMISSIBLE APPROXIMATION.
```

This distinction is load-bearing.

## Lean boundary

**PROVED.**

Lean proves only the declared componentwise rules:

- coordinatewise weakening preserves a satisfied coordinatewise budget;
- a fatal RELEASE loss cannot be compensated by unrelated coordinate improvement;
- a fatal REOPEN loss cannot be compensated by unrelated coordinate improvement;
- fatal PROV/EXT loss blocks componentwise admissibility;
- no theorem uses a cross-coordinate weighted scalar.

Lean does not prove:
- that five coordinates are scientifically complete;
- that frozen budgets are correct;
- that hard vetoes are naturally justified;
- that the candidate language should be promoted.

## Naturalistic transport

Naturalistic audit:
`experiments/mqr-4.67/NATURALISTIC-TRANSPORT.md`.

### OBSERVED external support

Goodman–Fanelli–Ioannidis, the Duke omics / Baggerly–Coombes case family, Silberzahn et al., and EFSA guidance provide independent examples where:
- provenance/process metadata;
- analysis ancestry;
- batch/process details;
- explicit uncertainty/evidence criteria

can materially affect later checking, inference or downstream scientific use.

### Transport status

**INFERRED.**

This gives qualitative external support to the general **PROV / ancestry** family.

But there is no external validation in this pass for the entire frozen tuple:

`(SEP, REOPEN, PROV, EXT, RELEASE)`.

Therefore:

- `NATURALISTIC_TRANSPORT_PARTIAL_PROV_ONLY`
- `FULL_TYPED_VECTOR_TRANSPORT_HOLD`

The naturalistic lane is retrospective, not prospective.

## Real-Lang semantic promotion decision

The PRESEAL promotion gate required:
1. nontrivial prior-art survival;
2. implementation concordance;
3. formal boundary;
4. naturalistic transport;
5. no hidden scalar selector;
6. reusable semantics beyond the synthetic machine.

Current status:

- implementation concordance: PASS
- formal boundary: PASS
- scalar-authority OFF: PASS
- naturalistic transport: PARTIAL / full vector HOLD
- generic approximation novelty: BASELINE_ABSORBED
- actual frozen Court produced an admissible lossy compression: NO
- reusable full scientific-loss ontology: OPEN

Therefore:

**NO v0.30 PROMOTION.**

`REALAPPROX 0.30-CANDIDATE` remains a development surface only.

REALACQUIRE 0.29 remains the latest promoted acquisition syntax.

## Scientific synthesis

The main earned result is negative:

```text
EXACT COMPRESSION FAILED IN 4.66.

APPROXIMATION DID NOT RESCUE
THE FROZEN CANDIDATE FAMILY IN 4.67.

AND THE SCALAR BASELINE
WAS NOT DEFEATED,
BECAUSE FULL STATE DOMINATED.
```

This is a stronger result than forcing a positive MQR-specific theory.

The Court leaves three distinct questions:

1. **Existence:** are there scientifically defensible lossy merges under a less synthetic, externally motivated authority contract?
2. **Representation:** if such merges exist, is typed loss more than ordinary multiobjective/constrained control?
3. **Constitution:** which loss dimensions and vetoes deserve scientific authority independently of the simulator?

All three remain partly **OPEN**.

## Anti-self-confirmation verdict

The finite Court is a characterization of its frozen semantics only.

It does not show:
- that science has exactly five loss coordinates;
- that the severity thresholds are true;
- that real inquiry should never compress;
- that full state is universally preferable;
- that REALAPPROX captures scientific truth.

The strongest valid statement is:

> Under the frozen 4.67 finite machine, candidate abstraction family, coordinate semantics, severity map and three predeclared budget contracts, every tested lossy abstraction violates at least one hard/material authority condition and no tested compression is admitted.

## Publication consequence

4.67 is useful mainly as an anti-inflation result:

- it prevents claiming approximate compression merely because exact compression failed;
- it prevents treating a successful software fixture as scientific evidence;
- it fails to defeat scalarization on the actual whole selection problem;
- it shows where naturalistic support is currently thin.

This improves a future paper by making its epistemic boundaries sharper.

It is not standalone evidence for a new approximation theory.

## Successor pressure

Do **not** simply loosen B0/B1/B2 after seeing this result.

That would be result-dependent mutation.

A legitimate successor must independently justify a new contract or bring in naturalistic scientific cases **before** defining its acceptance thresholds.

One promising direction is prospective naturalistic reconstruction:
freeze the relevant state/loss representation from historical evidence available before a documented later audit/reopening event, then test whether a compact representation would have erased the distinction that later became material.

That would attack the simulator-to-world transport gap directly.
