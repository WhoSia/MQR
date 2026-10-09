# REALREFERENCE 0.41-CANDIDATE — Fallible Adjudication Authority Firewall

**Status: DEVELOPMENT CANDIDATE / NOT PROMOTED / NO EXTERNAL TRUTH REVIEW.** Does not replace or alter the existing Real-Language `REALPACKET 0.2/0.3` compiler nor `REALACQUIRE 0.29` promoted surface.

## Syntax

```text
REALREFERENCE 0.41-CANDIDATE
n 487
paired 402
disagree 76
cap_disagree 7
cap_agree 3
certificate HYPOTHETICAL
selection STUDY_SELECTED
source_sha256 d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842
END
```

Exactly eight typed declarations required; no ad hoc `truth` or `independence` field is allowed. Caps are about *errors of the observed reference relative to an unobserved truth* conditional on whether the reference disagrees with the test decision; they are **not learned from the observed labels**.

- `certificate NONE`: no error budget may be asserted; typed formal output is `[0,n]` and world authority HOLD.
- `certificate HYPOTHETICAL`: conditional sharp Hamming arithmetic is evaluated, but world authority still HOLD: no real external validation.
- `certificate CLAIMED_EXTERNAL`: self-attestation is not validation; external custody/authorization/evidentiary review must occur outside this parser. World authority remains HOLD. A SHA256 source pin is data *custody*, not reviewer validation.
- `selection STUDY_SELECTED|TARGET_ENUMERATED` signals only the user's declared domain. This parser **does not independently validate selection probabilities or sampling contracts**. Transport stays HOLD in either case.

## Finite semantics

Let `m=paired`, `d=disagree`, `g=m-d`, `u=n-m`. Under externally supported separate ceilings `k_d` and `k_g` on reference-label mistakes in d and g groups, sharp **fixed-source** true mistake bounds for a binary h are `[d-k_d,d+k_g+u]`. The endpoints are sharp by constructing truth labels on the disjoint observed D/G/U partitions; error correlation is arbitrary. For `certificate NONE`, compiler returns `[0,n]` even when existing reader data show significant disagreements. This is a **finite feasibility statement**, not an estimate of clinical risk or outcome truth.

## Decision and authority ceiling

Output always includes:

```text
reference.formal_arithmetic=PASS
reference.world_authority=HOLD:<reason>
reference.target_transport=HOLD
reference.statistical_independence=NOT_ESTABLISHED
reference.real_language_promotion=UNPROMOTED_CANDIDATE
```

These constraints defeat the common failure mode `TWO_EXPERTS_AGREE -> GOLD_STANDARD_VERIFIED`. The executable rejects malformed/unsupported keys and mismatched totals. This is a conservative small candidate rather than a breaking modification of the existing Real-Language grammar. Add a serious externally validated authority channel in a separate future stage only if warranted.

## Evidence and tests

Source-native input is P8 derived QTDB per-beat receipt from PhysioNet expert files, 11 selected records/487 opportunities/402 complete pairs, SHA256 pinned. See `experiments/mqr-4.101/p2_selective_dependence.py` and accompanying P2 court. The negative grammar example attempts `certificate NONE` with positive caps and must return nonzero. Rust unit tests include absence of a certificate, fully hypothetical bounds, rejection of invented independence, and refusal to treat `CLAIMED_EXTERNAL` as a verified credential.

**Not claimed:** reference accuracy, medical conclusions, conditional independence, adjudicator selection causal mechanism, data transport, formal Lean proof, or novelty of finite Hamming bounds.
