# MQR-4.96 — FINAL BOUNDED SCIENTIFIC CLOSEOUT

**User-confirmed name:** **MQR-4.96 — Observation-Process Confounding, Source-Conditioned Label Semantics & Calibratability Under Provenance Shift**.

**Date:** 2026-10-09 (KST). **Court:** `CLOSED / ORIGINAL 2024 GBIF SOURCE-CONDITIONED LABEL SUPPORT PASS / REPORTED COORDINATE-UNCERTAINTY AUDIT PASS / COARSE SPACE–TIME WITHIN-OVERLAP DISCORDANCE PASS-DESCRIPTIVE / LEAN SOURCE-ERASURE + NONDETECTION COUNTEREXAMPLE PASS / ECOLOGICAL OCCUPANCY & FINNISH TARGET CALIBRATION HOLD / SPATIAL-CAUSAL ATTRIBUTION & POPULATION CI HOLD / NEW-ALGORITHM NOVELTY HOLD`.

This is a **bounded observational discovery and formal semantic distinction**, not invention of source adjustment, occupancy models or new spatial-inference coverage guarantees. Scientific study **4.96 CLOSED**, with a new genuine discriminant identified below, not because all desired causal estimands were proven.

## 1. Original source and advance lock

Serov, Koldasbayeva & Zaytsev (2026), *Scientific Reports*, DOI [10.1038/s41598-026-36740-7](https://doi.org/10.1038/s41598-026-36740-7). Original GBIF occurrence archive `0031144-240626123714530`, DOI [10.15468/dl.7jsjca](https://doi.org/10.15468/dl.7jsjca); created 2024-07-20, **29,543** original Finnish *Anemone nemorosa L.* occurrence records from **27** GBIF constituent datasets. Serov's fixed repository commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`; original `anemone.csv` git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`. Previous 4.95 recovered full original 2024 ZIP, verified row-ordered mapping of all 29,543 raw `occurrenceStatus=ABSENT/PRESENT` to author `presence=0/1`, exact year/normalized coordinates, and recorded all original GBIF observation IDs. **Publisher CSV lacks gbifID and source identifiers and the original feature ETL remains absent**; unordered ID join is not claimed.

4.96's [frozen research contract](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.96-FROZEN-EMPIRICAL-AND-LEAN-SOURCE-COURT.md) was written **after** 4.95 had already shown that 11,165 of 11,166 recorded negatives originated from the Finnish Nature League Spring Monitoring, and **after** a preliminary inspection of coordinate uncertainty had shown 4,010 Spring records at ≥100km and none under 1km. These are **not ex ante discoveries**, and their apparent replication in code is an audit with correct data ancestry. New predeclared measurements were the exact uncertainty-by-label profile, source-class entropy, common geospatial/year support contrasts, Lean logical erasure and detection witness.

Frozen original evidence archive, **actual full raw GBIF ZIP and Serov full CSV+notebook**, already in canonical Drive [4.95 original sources](https://drive.google.com/file/d/1OBJ7DJqNKUH5-GgMX5I10xlyr6erVj3v/view), with [29,543 ID-to-label lineage](https://drive.google.com/file/d/1VzoJYfMnp17cDBKXD3MPLRyJ0-w4YHNy/view). **Do not duplicate upstream raw data** to fabricate independent original roots.

## 2. Completely observed 27-source recorded-binary support

Original *2024 frozen records*, not a later changing GBIF live-index approximation:

| Recording-source group | Original GBIF `ABSENT` (Serov 0) | `PRESENT` (Serov 1) | Total |
|---|---:|---:|---:|
| Finnish Nature League — Spring Monitoring, UUID `acf9b46d-e71a-4ccb-91d2-a021ffda4dd4` | **11,165** | 3,486 | 14,651 |
| All other 26 publishers | **1** | 14,891 | 14,892 |
| Entire 2024 parent | **11,166** | **18,377** | **29,543** |

**25 of 27 contributor datasets have NO recorded negative examples**, 2 have both, and none have exclusively negative examples. The one non-Spring negative comes from GBIF contributor `887bd779-6454-436f-b1f8-86b70488b59f` (one absence and 134 presences, 135 total). The original Kastikka Floristic Archives `f2e389da-39c3-4f21-8d72-b7d574d924a9` has **0 absence, 9,686 presence**. `11,165/11,166 = 99.991%` of negatives came from one monitoring source.

**Crucial semantic limit:** `P(Y_{recorded}=0\mid S=s)=0` in the empirical original records for a source DOES NOT mean the relevant biological landscape has no absent species or that source-specified ecological occupancy is one. Most external records are collections of opportunities to report occurrences. Absence from a presence-only corpus is not measured field non-detection. Conversely the monitoring `ABSENT` means recorded non-detection under its protocol, not verified latent ecological absence.

## 3. How much the source name predicts the *recorded class* — descriptive only

The Rust std-only executable computes these finite-dataset association summaries using all original 29,543 records. A **Spring-versus-other group-majority** classifier that always predicts ABSENT for Spring records and PRESENT for other records has **in-sample**:
- accuracy **0.881968656**, compared with predicting overall majority class PRESENT **0.622042447**;
- balanced accuracy **0.905108402**;
- empirical binary outcome entropy **H(Y)=0.956586725 bit**;
- `H(Y|Spring-or-other)=0.393084813 bit`, empirical mutual information **0.563501911 bit**;
- `H(Y|27 dataset IDs)=0.392854954 bit`, mutual information **0.563731771 bit**.

The **single Spring-versus-other split accounts for practically all the observed 27-source/class empirical mutual information** (0.563502 versus 0.563732 bit). There is no train/test holdout on independent observation processes. These are **in-sample descriptive quantities** and should not be presented as out-of-sample source-aware risk-estimator gains, model leakage causally established or a source-adjustment innovation.

## 4. Geographic authority audit: the same source cohort has very different reported position fidelity

Official GBIF Darwin Core description: [GBIF data-quality recommendations, `coordinateUncertaintyInMeters`](https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations) represents a **reported horizontal radial uncertainty** around the published coordinates, a smallest-location-enclosing circle convention, **not** independent measurements of actual location error. Zero is an invalid value; missing uncertainty is unquantified. It cannot be treated as a probability distribution for hidden true coordinates, nor as an empirically estimated spatial autocorrelation scale.

Real full original 2024 field values:

| Source group | Reported uncertainty <1km | 1–<10km | 10–<100km | ≥100km | Missing |
|---|---:|---:|---:|---:|---:|
| Spring Monitoring (14,651) | **0** | **0** | 10,641 | 4,010 | 0 |
| Other 26 (14,892) | 5,195 | 7,580 | 926 | 863 | 328 |

Class-specific check from actual original fields:
- Spring `ABSENT` **11,165**: 8,068 at 10–<100km, **3,097 ≥100km**; **0 reported under 10km**.
- Spring `PRESENT` **3,486**: 2,573 at 10–<100km, 913 ≥100km; **0 under 10km**.
- Other `PRESENT` **14,891**: 5,194 under 1km, 7,580 1–<10km, 926 10–<100km, 863 ≥100km, 328 missing; one other-source `ABSENT` is under 1km.

**Implication:** exact six-decimal observed coordinates and source-site deduplication (including 4.93–4.95's site-based geographic holdouts) cannot be promoted to verified fine-resolution ecological field-site separation or spatial independence without additional source-georeference grounding. Earlier held-out loss calculations remain **valid computations conditional on their printed source values**; their interpretation as truly independent geographic transfer is further constrained. Do not assert that 10km reported radius equals actual ≥10km displacement of each specimen.

## 5. Fixed coarse geography×year common-support comparisons

Post-contact but pre-execution frozen checks. Rust bins original reported coordinate values and year into:
- **Primary:** 1° latitude × 1° longitude × consecutive 3-year bins from year 2000.
- **Secondary sensitivity:** 2° × 2° × 5-year bins from year 2000.

Within a coarse stratum *containing both Spring and another original source*, a constructed hypothetical **conditional source-label exchangeability** benchmark expects `E[A_s]=Σ_j (n_{j,Spring}·n_{j,ABSENT}/n_j)`. This is a deterministic aggregate-table benchmark. The source assignment was NOT randomized, observation events may be clustered/repeated, and geographic coordinate uncertainty often greatly exceeds nominal cell resolution. It licenses no classical p-value, causal source effect or sampling-design confidence interval.

| Freeze | Total observed strata | Source-overlap strata | Records in overlapping strata | Actual Spring ABSENT in overlap | Exchangeability-benchmark expected Spring ABSENT |
|---|---:|---:|---:|---:|---:|
| 1° × 3-year primary | 384 | 156 | 24,364 | **10,522** | **7,083.353** |
| 2° × 5-year sensitivity | 97 | 46 | 25,860 | **11,016** | **7,025.829** |

Original rows without valid original coordinates/year for bin construction: **36**. In overlapping strata, the count of recorded absences in Spring is higher than the benchmark by **3,438.647** (primary) or **3,990.171** (secondary). This holds for both predeclared coarse bin definitions but **cannot isolate source semantics versus ecological conditions, measurement effort, site coarsening, varying sampling-year environment or repeated visits**. We do NOT infer generalization to the full Finnish landscape.

## 6. Conditional statistical obstacle and Lean executable logic

A latent ecological occupancy model distinguishes `O∈{0,1}` (actually occupied), `D∈{0,1}` (successfully detected given occupancy) and **observed** binary `Y=O·D` with no false positives as an explicit simplifying assumption. Even with fixed covariates, `P(Y=1|X,S)=P(O=1|X,S)·P(D=1|O=1,X,S)`, and the product alone cannot separately identify occupancy and detection probabilities. Two extreme worlds (`O=0,D=1` and `O=1,D=0`) both record `Y=0`. Real repeated-detection surveys/effort designs may supply missing data but are not present in the original author reduced CSV. This is a standard occupancy/detection identifiability issue, not new MQR mathematics; see MacKenzie et al. (2002), *Ecology* 83:2248–2255 DOI [10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2](https://pubs.usgs.gov/publication/5224176).

Lean 4.24.0 `experiments/mqr-4.96/lean/Mqr496SourceCourt.lean`, zero Mathlib, **no `sorry`**, verifies:
1. Dropping a source ID from two otherwise identical `TaggedRecord` values yields identical reduced data;
2. Distinct source-tagged records genuinely differ;
3. The source-erasure map is not injective (a constructive counterexample);
4. A presence-only source list containing only `true` records has no recorded `false` values;
5. A typed negative observation authorization rule cannot grant a negative receipt without the specified survey evidence;
6. The Boolean non-detection world counterexample: real absence and failed detection yield identical observed `false` despite different underlying occupancy state.

All are *conditional syntactic/mathematical facts* about explicitly declared types/semantics; they do not certify GBIF data collection or true site presence, nor prove causal confounding. A temporary rational-number `decide` tactic failure in GitHub CI [37887302966](https://github.com/WhoSia/MQR/actions/runs/37887302966) was retained and corrected by switching to an explicit Boolean construction directly representing the scientific negative-label ambiguity. Earlier run [37887103137](https://github.com/WhoSia/MQR/actions/runs/37887103137) had both initial jobs SUCCESS. **Final [37887381670](https://github.com/WhoSia/MQR/actions/runs/37887381670) both jobs SUCCESS**, Rust 5 unit tests + full raw original input checksum/actual data court PASS, Lean proof library six declarations built PASS; no bot-authored commits.

## 7. Evidence custody and scientific stopping rule

**Original source evidence reused, not duplicated:** Drive `02_ANALYSIS_SAFE` original 2024 GBIF+Serov author source [file](https://drive.google.com/file/d/1OBJ7DJqNKUH5-GgMX5I10xlyr6erVj3v/view) and 4.95 all-GBIF-ID [mapping](https://drive.google.com/file/d/1VzoJYfMnp17cDBKXD3MPLRyJ0-w4YHNy/view).

**New current derived original-replay receipts:** [Rust original 2024 27-source/class/support, reported position uncertainty-by-class, coarse geography/year contract comparison and SHA log](https://drive.google.com/file/d/1XYTtWN05h6VcTgPZYQJ_CAtGQkaCoJBo/view) and [Lean proof source and successful final build log](https://drive.google.com/file/d/1Ia3GngxS4LabFf3l-PmZgGvi8lmgIaLA/view), both saved into the existing Drive `02_ANALYSIS_SAFE`. They do not represent an independent publication root or new collected organisms.

**PASS:** Original GBIF 27-source class support, entropy/accuracy finite-table analysis, 29,543-record coordinate-uncertainty stratification, descriptive coarse source-overlap contrast, six formally checked Lean source/detection logic declarations, Rust exact source-boundary CI.

**HOLD:** Inference from observed `ABSENT` to latent biological absence, field detection probability and observer effort, exact true-location site correspondence for high-uncertainty coordinates, statistical spatial independence, causal effect of publisher source, conditional ecological occupancy or *true population* risk transport, independent matched Finnish 64-site calibration, valid sampling coverage intervals, and method novelty.

**Scientific stopping:** This version has answered its **source-observation-contract audit** question: observed labels and reported location reliability differ markedly between source processes, with most other datasets providing no negative recorded-label support. Identifiable ecological occupancy/risk transfer does NOT follow. **4.96 CLOSED BOUNDED**, not indefinite reruns; historical result remains qualified, not deleted.

**Proposed (NOT OPEN) successor:** **MQR-4.97 — Detection-Protocol Identifiability, Spatial Observation Footprints & Risk Transport Across Sampling Frames**. Its admissibility must depend on an actual repeated-detection or field-protocol source (or mathematically sharp nonidentification benchmark) and a demonstrably different empirical discriminant. Do not open 4.97 without user confirmation or new instruction.

**Research OS:** canonical only one Notion MQR root `3c8ef561cf92815693b6fcf6de9955f7` updated in place; no Labs duplicate, no new child page. GitHub main human-authored commits, Actions read-only and no `github-actions[bot]` commit/push/tag. Notion metadata after final scientific adjudication should reflect 4.96 CLOSED and proposed 4.97 NOT OPEN.
