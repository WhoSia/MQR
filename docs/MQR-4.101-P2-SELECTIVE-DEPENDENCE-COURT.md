# MQR-4.101 — P2 Internal Court: Selective Adjudication, Correlated Error and External-Certificate Allocation

**Official research name remains:** MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability.

**Research verdict at drafting:** P2 SOURCE-AUDIT/PARTIAL-IDENTIFICATION MATHEMATICS CHECKED LOCALLY, real-world reference-error authority HOLD. Do **not** close P2 or claim CI PASS before the linked GitHub execution succeeds. This is an internal P-stage, *not* a distinct formal title.

## 1. Exact source and declared target

Input is the identical **P8/P1 source-hash-verified derived** PhysioNet QT Database per-beat receipt in `experiments/mqr-4.101/p8_publisher_verified_487beat_receipt.csv`, SHA-256 `d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842`. P8 authenticated the *individual expert annotation files*; P2 adds no independent truth collection and does not re-download ECG signals. Selected reference set = 487 beat opportunities across 11 records for which a first-annotator QT value is available. Paired QT values = 402; a second QT value is missing/incomplete in 85. Label `h_i = 1[reader1_QT_i >= 440 ms]`, `b_i = 1[reader2_QT_i >= 440 ms]` on paired cases only, for a **nonclinical mathematical threshold probe**. Neither is ground truth nor a clinical diagnostic rule.

The **source-observed selection** is highly concentrated: `sel102` contains 85 selected beats but only **2 paired**, **83 unpaired**; `sel213` has 71 selected / 69 paired / 2 unpaired; the remaining nine source records have no missing pair at this fixed selected-beat level. **83/85 = 97.65%** of incompleteness lies in `sel102`, even though it holds 85/487 = 17.45% of selected beats. No reason for the source's selection decision, blinding, dropout mechanism, or missing-at-random condition is documented by this audit; these observed numbers **do not prove MNAR**. At cutoff 440, `sel223` has **26 disagreements among 31 paired**, while `sel100` has **0/30**; reader concordance is heterogeneous across records. A naive `76/402` pooled reader disagreement is not a validated estimator for a hypothetical different case distribution.

## 2. Dependence-robust two-stratum *sharp finite risk* identity

Among the 402 *paired* examples, let `D=76` cases with `h != b`, `G=326` with `h=b`, and `U=85` missing `b`. For **hypothetical externally warranted** separate upper caps `k_D <= D` and `k_G <= G` on the number of false `b` labels **within observed disagreement and agreement strata respectively**, the exact finite number of wrong h predictions relative to latent binary T lies in:

`R_count(h,T) in [D-k_D, D+k_G+U]`.

This is elementary sharp Hamming-label reasoning, valid with **arbitrary dependence between annotators' errors** and arbitrary selection of which 85 cases lack b: on D cases, h is wrong unless b is wrong; on G cases, h is wrong only if b is wrong; on U cases T is unconstrained. Every endpoint is constructible by labeling the relevant D/G/U cases appropriately; no factorization or conditional independence enters. The bound is **not original mathematics**. Note the caps `k_D`,`k_G` are statements about *latent truth and b's error*, **not estimated from D or G themselves**. Consequently even a certificate stratified by the *observed* h/b relationship requires external truth validation.

| Reference-label assumptions | Sharp wrong-h count / 487 | Evidentiary status |
| --- | --- | --- |
| **Actual source, no certified truth whatsoever** | **[0,487] / 487** | Actual scientific ceiling: HOLD |
| Hypothetical pooled external cap `k<=10` (P1) | [66,171] / 487 | Sensitivity, **not measured** |
| Hypothetical `k_D<=7, k_G<=3` | **[69,164] / 487** | Sensitivity, *conditional improvement* |
| Hypothetical `k_D<=10, k_G<=0` | [66,161] / 487 | Sensitivity, different certificate allocation |
| Hypothetical `k_D<=0, k_G<=10` | [76,171] / 487 | Sensitivity, different certificate allocation |

Even if pooled caps total 10 in each sensitivity experiment, the *location of errors* matters to both endpoints. The improvements result from **stronger, more detailed external certification**, not from a favorable fit to the observed two-expert disagreement. In the current data `k_D`, `k_G` are **both unknown**; setting them to 0 on any stratum is unsupported.

A Python stdlib brute-force proof oracle enumerates **8,200 distinct finite count/budget cases** across all `n<=6` observed types, and for each checks all `2^n` latent truth assignments. The independently written Rust court tests the sharp identity for all `n<=5` and separately recounts the actual P8 CSV, including the record-specific missingness distribution. These are *finite constructive verification*, not external annotation error verification.

## 3. Selective third-party review: what actually contracts a set?

If an independently reliable adjudication establishes truth for `s` of `U=85` unpaired beats and exactly `v` of those `s` are wrong under h, then under a separate (still hypothetical) guarantee that b is perfect on the 402 paired cases, the sharp total wrong-h range is `[76+v,76+v+(85-s)]`. With `s=10`, its width is **75** instead of **85**, whether `v=0` or `v=10`: this is *fixed-population* contraction by observing ten previously unconstrained truths. **No such third-party audit of even one beat has been acquired**. A reviewer chosen for easy cases does not yield a representative estimate for the unsampled population. An arbitrary ten paired reviews may or may not contract endpoints as much; budget allocation and sampling frame must be fixed prior to seeing truth outcomes. No claim of a unique best audit allocation is made here.

No `P(T | h,b,S)` is identified merely from the first two experts agreeing, even when paired cases are numerous. Correlated mistakes can be perfectly aligned, anti-aligned, or selectively concentrated while leaving the actual `(h,b,S)` distribution unchanged. Two extreme latent worlds `T=h` and `T=1-h` yield the same source observations and source missingness, yet h's true 0–1 risk respectively **0 or 1**. External validation of b's mistakes or strong externally defended structural error restrictions are required to narrow that range.

## 4. Genuine Real-Language development, deliberately not promoted

The new **`REALREFERENCE 0.41-CANDIDATE`** is an executable, additive governance/decision-authority lane; no changes to canonical `REALPACKET 0.2/0.3` or promoted `REALACQUIRE 0.29`. Executable Rust binary: `language/real/src/reference_v41.rs`; entry `real-v41-reference` is registered in existing `language/real/Cargo.toml` with *backward compatible independent target*. Grammar requires an exact 8-field object: target `n`, paired count, disagreement count, typed pair-stratified caps, reference-error certificate status (`NONE|HYPOTHETICAL|CLAIMED_EXTERNAL`), selection scope, and SHA-256 source. Unknown fields, missing counts, unearned positive accuracy assurances and invalid cap/count combinations **fail closed**.

The compiler always prints `reference.formal_arithmetic=PASS` if counts are well-typed and `reference.world_authority=HOLD:...`, even when the input literally says `CLAIMED_EXTERNAL`: this executable **cannot validate an external physician adjudication source or certify transport just from a string**. It emits `[0,n]` for `NONE`, `[69,164]` for the stipulated `HYPOTHETICAL 7/3` packet, and never emits real clinical correctness or assumption-independent accuracy. This is a **candidate**, not a promoted v0.41 implementation with a published semantics theorem. Direct negative fixtures reject invalid `NONE`+positive cap cases.

This design is intentional: it makes the difference between proven arithmetic and world-facing authority executable **without introducing an arbitrary new 0–1 epistemic score**, and without disturbing hundreds of old `language/real` examples or baseline Real-Lang CI. Unit tests are Rust canonical local type/semantics guards; neither a Lean theorem nor a comprehensive parser security audit has been performed.

## 5. Falsification and next gate

- Verified source: 487 exact selected-beat records, 402 paired, 85 missing, 76 binary cross-threshold disagreements, D/G = 76/326, 83/85 missing on `sel102`, heterogeneity 26/31 on `sel223`.
- **No verified source:** why `q2c` annotation is missing, true QT for any of the 487, independently adjudicated reference mistakes, source-to-target population inclusion probabilities, conditional error independence, or a clinical target utility.
- Finite sharpness + conditional selection accounting are existing classical mathematics. This trial is a **bounded methodological countermodel and a source-native audit**, not a novel theorem or medical diagnostic conclusion.
- Next substantial experiment: legitimately acquire a third annotator or independently established QT boundary accuracy on a protocol-defined, *preselected* overlap/missing sample; preserve sampling probabilities and reviewer blinding provenance. Failing that, keep `true_risk=HOLD` and optimize **hypothetical** information collection without presenting it as empirically measured. Compare joint *risk differences* with common truth assignments, not merely separate non-overlapping scalar marginal intervals.

**P2 status is determined by subsequent CI evidence; MQR-4.101 stays OPEN.**
