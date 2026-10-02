# MQR-4.70 — K562 Metadata-Only Family Assignment Constitution

Status: **PRE-RESPONSE / TARGET-LIST-NOT-YET-READ / ASSIGNMENT-FUNCTION-FROZEN**

## Purpose

Create CURRENT / HELD_OUT / REPLICATION perturbation families before any transcriptional response, TE_ratio, differential-expression statistic, learned causal effect, or response embedding is inspected.

## Eligible identity field

Use only a canonical perturbation target identifier derived from source metadata.

Preferred identity order:
1. stable gene identifier if available;
2. canonical gene symbol otherwise.

Guide identity may be retained for audit but does not independently determine family assignment when multiple guides map to the same target gene.

Controls remain in a separate CONTROL class.

## Canonicalization

For each non-control target:

1. trim whitespace;
2. uppercase gene symbol when symbol is used;
3. preserve stable identifier exactly when an Ensembl-like stable identifier is available;
4. create the assignment key:

    MQR470-K562-V1|<CANONICAL_TARGET_ID>

No outcome-derived metadata may enter the key.

## Assignment function

Compute SHA-256 of the UTF-8 assignment key.

Take the first unsigned byte B.

Assign by B mod 10:

- 0,1,2,3,4 -> CURRENT
- 5,6,7 -> HELD_OUT
- 8,9 -> REPLICATION

Expected proportions:
- CURRENT: 50%
- HELD_OUT: 30%
- REPLICATION: 20%

These proportions are frozen before target-list inspection.

## Multi-guide targets

All guides mapped to the same canonical target remain in the same family.

No guide-level split of one target across CURRENT and HELD_OUT is allowed.

## Controls

Non-targeting controls and declared technical controls are never hashed into the three scientific target families.

They remain:

    CONTROL

and may be used only for normalization/noise estimation defined independently of family outcomes.

## Missing / ambiguous identifiers

Targets without a stable canonical identity are labeled:

    IDENTITY_HOLD

before response reveal.

They are excluded from the primary Court and may enter only a successor robustness analysis after identity resolution.

## Data fields forbidden before family seal

Before the assignment receipt is committed, do not inspect or use:

- TE_ratio;
- target-expression reduction;
- pseudobulk expression values;
- single-cell expression values;
- differential-expression scores;
- p-values / FDR;
- learned network edges;
- response embeddings;
- graph centrality;
- cluster assignment derived from expression;
- Brown et al. 2025 0.75-SD quality pass/fail.

## Metadata fields permitted before family seal

- canonical target identity;
- guide-to-target mapping;
- cell line;
- screen name;
- collection day;
- library/gemgroup identity;
- file/source provenance;
- raw cell-count metadata only if it is not computed from expression effect size.

Cell count may be used for a predeclared coverage stratum but must not alter CURRENT/HELD_OUT/REPLICATION hash assignment.

## Primary receipt

After target metadata are acquired, produce a TSV with:

- canonical_target_id;
- source_target_label;
- guide_count;
- source_screen;
- assignment_hash;
- assignment_bucket;
- family;
- identity_status.

Commit the TSV and its SHA-256 before opening expression-response arrays.

## Scientific rationale

The family split is not intended to optimize prediction.

It is intentionally neutral to outcome and mechanism.

The goal is to test whether a currently admitted perturbation family supports a state/equivalence claim that is later refined by a disjoint, prospectively fixed intervention family.

## Failure conditions

The primary naturalistic Court is invalid if:
- target assignment is changed after expression inspection;
- response-derived quality metrics determine family membership;
- individual genes are moved to balance observed effects;
- held-out targets are chosen because they are known strong perturbations;
- failed targets are silently removed after reveal without retaining a receipt.

## Authority boundary

A positive held-out refinement result earns only:

    PROSPECTIVE_NATURALISTIC_FAMILY_REFINEMENT_CONTACT

It does not establish:
- completeness of the K562 perturbation universe;
- open-world closure;
- universal intervention-family endogeneity;
- a new causal discovery algorithm.
