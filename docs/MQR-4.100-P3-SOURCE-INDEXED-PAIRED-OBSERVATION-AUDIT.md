# MQR-4.100 — P3: Source-Indexed Paired-Observation Empirical Contact and Its Warrant Limits

> **This is an internal P3 record, NOT a new MQR official name.** The official title remains:
> **MQR-4.100 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport**.

**Date:** 2026-10-09. **Status at initial publication:** a retrospective, post-exploration empirical source check; actual CI and summary receipt pending. **No new statistical theorem, novel estimator, independent second instrument, population-identification result or external transfer is claimed.**

## 1. Why P3 departs from P1/P2

P1/P2 verified known exact/approximate experiment-comparison identities on **constructed distributions**. Those are valid mathematical local contracts but not biological discoveries. P3 must contact a real measurement table with **two separately named attributes recorded for the same source row** and explicit observation keys. This does NOT by itself imply two independent instruments or establish a parameter-indexed Blackwell/Le Cam experiment correspondence.

Actual source: `palmerpenguins` R data package's **combined** `penguins_raw.csv` of Gorman / Palmer Station Long Term Ecological Research 2007–2009 adult penguin measurements, repo `allisonhorst/palmerpenguins`, commit `8957207b78d6ccd1b4654a9dd9c9041b657478ab` (2024-09-19), exact git blob SHA1 `ba99fbd527f0bb983b3d9615ef5c81a5917ab7d9`.
Permanent repo blob URL: https://github.com/allisonhorst/palmerpenguins/blob/8957207b78d6ccd1b4654a9dd9c9041b657478ab/inst/extdata/penguins_raw.csv

Source's upstream publications and EDI record families:
- Original field interpretation: Gorman, Williams & Fraser (2014), *Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins*, DOI https://doi.org/10.1371/journal.pone.0090081.
- Adélie, 2020 EDI version 5: https://doi.org/10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f
- Gentoo, 2020 EDI version 5: https://doi.org/10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689
- Chinstrap, 2020 EDI version 6: https://doi.org/10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e
- Data dissemination and cleaning account: Horst, Hill & Gorman (2022), *The R Journal*, https://journal.r-project.org/articles/RJ-2022-020/.

**Crucial qualification:** we audit a **published combined secondary CSV curated from EDI source datasets**, not 2007–2009 handwritten notebooks, measurement-instrument logs or the independently downloaded three original EDI bundles. The combined rows constitute real observational records, but the source chain remains common. The two anatomical lengths are recorded in the SAME row, not by proven independent observers.

## 2. Original-byte and row-identity contract

Download the exact combined CSV from the pinned upstream commit; `git hash-object` must equal `ba99fbd527f0bb983b3d9615ef5c81a5917ab7d9`. Run independent Python stdlib and Rust parsers against **the exact same source bytes**. No fabricated records, invented extra measurements or silent row reordering.

The raw CSV has 344 rows and 17 fields. Two anatomical columns of interest are `Culmen Length (mm)` (old Y) and `Flipper Length (mm)` (paired Z). The two-length complete-case subset has 342 rows. Source-specific categorical labels are Species; `studyName` spans PAL0708, PAL0809 and PAL0910. Missingness is not randomness: retain all source rows for count audit and exclude only rows missing either of the two announced inputs from the downstream old-vs-paired comparison.

**Key audit:** (`studyName`, `Individual ID`) is unique inside this combined version (344/344). (`studyName`, `Sample Number`) is **not unique** (124 collisions); raw `Individual ID` **alone** also repeats across expedition years and must NOT be treated as a globally unique independent bird identifier. A row has its original simultaneous pair by source-schema authority. Any distinct across-year linkage requires original band identity metadata unavailable here.

## 3. Fixed exploratory comparison, no causal/novelty promotion

One lightweight, documented comparison: predict original 3-category `Species` with *only bill length* versus *bill length + flipper length*, for 2009 PAL0910 holdout rows with both fields available. Fit a **nearest-class-centroid** Euclidean classifier from complete-case PAL0708 and PAL0809 rows ONLY, using pooled training-population feature SD for each feature; tie-break by species name. Score 0–1 top-one accuracy on PAL0910. All three species occur in both sets.

This is an **exploratory retrospective model comparison** on a well-known source; model/feature choices were informed by dataset inspection; it is NOT blind preregistration. A time-split is not a population-independent or instrument-independent study. Species is documented in the same dataset, not an independently adjudicated external ground-truth endpoint. Correlated specimen identities and site/species composition could drive differences. No leave-site-out/leave-identity-out guarantees unless explicitly tested.

Negative audits:
- Test whether `Individual ID` strings in 2009 also occur in 2007/2008; report overlap counts, *not* independently verified same-bird matches.
- Report results for 2009 rows with ID strings absent from training; acknowledge altered species composition and small n.
- Rotate 2009 Z values by a deterministic 17-row shift **within the same 2009 holdout** to break row pairing while preserving the unconditional 2009 Z marginal. This is a synthetic negative control, not an equivalent natural observation regime; it does not preserve species-conditional Z distributions and cannot isolate a causal benefit of pairing.
- A 2,000-replicate, fixed-seed **row bootstrap** of the paired *accuracy difference*, if reported, is descriptive under the observed rows and ignores clustering, location and across-year identity uncertainty. It is not a confidence interval for biological population risk.

## 4. What is and is not licensed

- **Can verify:** source provenance and byte identity, one-row Y/Z joint provenance within the combined survey table, missingness and keys, deterministic old-vs-joint selected classifier performance on a named 2009 holdout, exposure to a real selection and repeated-ID problem, Python/Rust arithmetic concordance.
- **Cannot verify:** true conditional parameter kernel `E_θ` and `J_θ` across a controlled parameter family, actual supremum projection error ε over Θ, independent instruments, unbiased latent-state census, Blackwell dominance for the population, measured *identification* of species parameters, ecological causality, future-year or geographic transport, full independence of training/test individuals, new method novelty.
- Even if empirical accuracy increases when adding a variable, this **does not entail strict observation-quotient refinement or a partial identification theorem** without the true experiment kernels and pairing/invariance assumptions. Empirical classifier performance is an entirely different object.
- P1/P2 identities and prior-art limitations remain intact; MQR-4.99 independent behavioral event log still missing.

## 5. Execution, archival and possible P4 gate

- `experiments/mqr-4.100/p3_paired_original.py`: standard library independent CSV/key audit, heldout centroid scoring, row-bootstrap receipt and sham-pairing negative control.
- `experiments/mqr-4.100/src/bin/p3_paired_original.rs`: separate source parser, full count audit and centroid reconstruction.
- `.github/workflows/mqr-4.100-p3-paired-source.yml`: read-only Actions downloading pinned original; exact Git blob check; produces fixed original CSV and audit receipts as downloadable artifact.
- CI can certify local source/replay code only; archival to Drive must be **separately completed and reverified** before claiming Drive custody.

A genuine next empirical gate would require **two independently recorded and reliably linked measurements of the same entity**, or matched intervention/repeated-measurement records with a documented selection mechanism and a target-specific source/target correspondence. Only then investigate uncertainty-aware ε bounds or a claim-relevant conditional identification improvement. This particular penguin demonstration supplies no such independent second observation instrument.

**P3 initial verdict: OPEN / SOURCE-ACCOUNTING & EXPLORATORY SCORING CI NOT YET CHECKED / SCIENTIFIC TRANSPORT HOLD.**
