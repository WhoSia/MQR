# MQR 5.4 · Chat45 R70 — Verification and adversarial claim audit: R61–R69

**2026-11-23 KST | MQR 5.4 OPEN | audit, NOT theory promotion.** The newly located 1969 CHSH published original, 1972 original institutional preprint, and 1958 JBC original paper were read through public browser retrieval. **All three are online-located for this turn; none is certified uploaded to shared Drive.** Keep custody separate from web access.

## Source-reading verification receipts

| Source | Status | Scope / failure bound |
|---|---|---|
| CHSH (1969), PRL 23:880, [scan](https://quantum.country/assets4/Clauser1969.pdf) | Public primary facsimile directly text-read; screenshot p. 881 **success** | Read observable-rate Eq (2a)/(2b), explicit detection-bridge assumption, Kocher–Commins insufficiency, 22.5°/67.5° geometry and polarizer-removal controls |
| Freedman & Clauser (January 1972), [LBL-392 original university preprint](https://escholarship.org/content/qt5qs9830k/qt5qs9830k_noSplash_f76b31bfeb77e6b12c55f3cbd8f6de86.pdf) | Original preprint directly text-read, institutional preservation proven, PDF screenshot request failed **remote cache miss** | Distinct from April 1972 final publisher page; authors' reported rates/uncertainties and setup read; no raw counter time-series; page images not independently validated |
| Hoagland et al. (1958) [JBC original](https://njc.rockefeller.edu/pdf4/Class4-HoaglandZemecnik1958.pdf) | Original publication text read, Figure/Table text read, PDF screenshot request failed **remote cache miss** | No pixel-level re-digitization or figure-data precision claim, no original lab notebooks |

## Exact executable-source verification, resolving the R61/R63 caveat

Three Python sources were retrieved from *GitHub main* using the GitHub connector and recreated byte-identically in the local Python execution environment. Python compilation and module execution succeeded in this turn. Local Git blob SHA-1 (from `git hash-object`) **equaled remote GitHub `fetch_file.result.sha`** for each:

| Python source | remote Git blob SHA and equal local git-hash | Executed result |
|---|---|---|
| `language/real/experiments/mqr45_r61_postselection_threshold.py` | `ac553a9ef37ce4a1d2705fef7b82eca3e7a8f295` | 6 exact rho scenarios and 65,535 setting-independent subsets pass |
| `language/real/experiments/mqr45_r63_prediction_discovery_causal_equivalence.py` | `8b5c304ea3c709fb9b7d7b35346cd01a6b470a5a` | observational distributions identical and do(P) effects 1 vs 0 |
| `language/real/experiments/mqr45_r68_freedman_clauser_1972_rounded_rates.py` | `12e20e8257c26181afa8e29ee32b2ee42b9d4345` | D22=13/125, D67=−137/125, delta=1/20, rounding interval [0.049,0.051] |

This is more than independent algorithmic re-expression: SHA equality demonstrates that the tested byte stream matches each committed Git blob. **It is not a repository-wide integration/CI pass**, and no original laboratory raw data were executed or collected.

## Five overclaims deliberately rejected

1. **1969 CHSH Eq. (2a) is not identical to the textbook ideal `|S|≤2`.** The original derives a measurement-rate bridge with extra detection and normalization assumptions. Treat the logical derivation, its laboratory operationalization and later test separately.
2. **1972 authors did not assume single-arm rates were orientation-invariant in their data analysis.** Original preprint note 4 says explicitly so, despite using R1 and R2 as shorthand. A loose paraphrase of 1969's simplified inequality must not be forced onto 1972 analysis.
3. **Rounded values reproduce D67=−1.096, whereas authors report −1.097.** This is not a mismatch of laws or a coding error; the article summary is rounded, whereas the published statistic can come from unrounded values. The source figures cannot support reconstruction of all original counts and covariance.
4. **The 1972 optical experiment did not close all Bell loopholes.** The additional detection-probability assumption appears explicitly in the original; the different R61 rho-threshold is a synthetic global adversarial filter, NOT an experimental efficiency bound.
5. **1958 RNA-labeled fraction is not already the whole modern mechanism of tRNA.** The authors themselves consider contamination and alternative storage behavior, cannot resolve the bond, and note preparation-dependent ATP carryover. Absence of direct Crick guidance does not mean absence of all local biochemical research hypotheses.

## Selection for a next genuine advance

Do not promote MQR 5.4 merely because verified historical examples are intellectually satisfying. Attempt to identify **a discriminating, independently measurable research-design change** not captured by standard philosophy-of-experiment historiography. A strong negative test: if a standard chronology/protocol reconstruction answers every MQR question with no additional predictive constraints, classify MQR as an organized interpretive synthesis, not a new explanatory law.

**OPEN | no new Drive file | no independent new lab data | no unearned paper priority | AUTHORITY TRANSFERRED NONE.**
