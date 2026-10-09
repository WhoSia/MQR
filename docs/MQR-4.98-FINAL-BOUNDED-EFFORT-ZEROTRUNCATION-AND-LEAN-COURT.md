# MQR-4.98 — FINAL BOUNDED SCIENTIFIC CLOSEOUT

**Official title, confirmed 2026-10-09:** **MQR-4.98 — Closure-Sensitive Detection Models, Survey-Effort Transport & the Identifiability of Ecological Risk Across Observation Regimes**.

**Final scientific verdict:** `CLOSED BOUNDED / DISTINCT 2005 REAL ALDER FLYCATCHER 3×5-MIN FIELD PROTOCOL PASS / ORIGINAL PER-BIRD VS PER-STATION AGGREGATE CUSTODY PASS / ZERO-TRUNCATED CONDITIONAL DETECTION MLE PASS / SITE-HELDOUT EFFORT-HETEROGENEITY CONTRAST PASS-DESCRIPTIVE / LEAN MISSING-NONDTECTIONS + CONDITIONAL EXPOSURE COMPOSITION PASS / ORIGINAL UNOBSERVED POPULATION COUNT, BIOLOGICAL SITE OCCUPANCY AND CROSS-REGIME ECOLOGICAL RISK HOLD / NEW THEOREM OR CALIBRATION ALGORITHM NOVELTY HOLD`.

This court did not prove unconditional ecological occupancy or identify physical sampling footprints. It answered one distinct scientific question: **known fixed secondary effort can identify an explicit detection parameter under zero-truncation assumptions among positive field histories, but does not by itself reconstruct the unseen population or make risks transport across biologically different sampling frames.**

## 1. Data ancestry, scholarly precedent, protocol

**New original field root** compared with MQR-4.97's 2001 Delaware NAAMP frog auditory surveys: Chandler and collaborators' **2005 Alder Flycatcher** (*Empidonax alnorum*) **15-minute fixed-area point-count field survey**, split into **three 5-minute secondary intervals**, with up to three primary surveys in the 2005 season. The `unmarked` first-party [capture-recapture vignette](https://mirror.nju.edu.cn/CRAN/web/packages/unmarked/vignettes/cap-recap.html) explicitly documents this protocol and the individual encounter histories. Software package is the SAME `unmarked` distribution that hosted the earlier NAAMP frog data, but the biological species, collection year and original field sampling program are different; these two biological collections are not two independent portal/index institutions nor are 2005 flycatcher bird histories a repeat of 2001 frog data.

Source GitHub `cran/unmarked` commit `fc0c7119d86c53c9e48a4db10ff2170819cd245f`, raw author-original field files:
- `inst/csv/alfl.csv`, blob SHA1 `cf8fb85ecbedad96bfd826ba8c0d28d00aa22b6c`. Every original row represents one **detected-individual encounter history within one primary 15-minute survey**, with visit `survey` 1–3 and three individual 5-minute 0/1 capture flags. The available file contains no `000` bird histories by design.
- `inst/csv/alfl.capRecap.csv`, blob SHA1 `0b20495dc49c94cdf3ee4202edc682f7e7522015`. Includes all source point-count station keys and 21 visit×binary-pattern counts; includes site-visit cells with zero detected birds.
- `inst/csv/alflCovs.csv`, blob SHA1 `7adb7214614d02c3cdf55ba07028f869d8d5d151`, original point-station covariates, survey `time.1..time.3`, `date.1..date.3`, vegetation structure, woody cover. The time and date covariates are protocol/context, not different measured durations of each known 5-minute window.

Scholarly precedents: Fiske & Chandler (2011), *Journal of Statistical Software*, DOI [10.18637/jss.v043.i10](https://doi.org/10.18637/jss.v043.i10); Chandler, Royle & King (2011), temporary emigration and detection/availability DOI [10.1890/10-2433.1](https://doi.org/10.1890/10-2433.1). The earlier 2009 Chandler forest management paper DOI `10.1016/j.foreco.2009.07.025` analyzes field sites in **2003–2004**, so **do not claim that DOI independently certifies that this `unmarked` 2005 CSV is the raw appendix to that particular 2009 paper**; source-specific dataset DOI beyond `unmarked` vignette was not verified. Retain `unmarked` package GPL≥3 and provenance on archived source code/files.

**Pre-result preseal:** [MQR-4.98 Alder Flycatcher Effort and Identification Preseal](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.98-ALDER-FLYCATCHER-EFFORT-IDENTIFIABILITY-PRESEAL.md) fixed the row-count reconciliation, 3×5-min exposure, positive-only conditional likelihood, 75/25 station site split, homogeneous vs 3-dimension interval-specific comparisons, Lean erasure court and exactly scoped HOLDs before running the original numerical Rust analysis.

## 2. Whole original source schema and a real authority mismatch

**Git blob checks PASS for all three complete raw field files**, and Rust std-only independently recomputed original seven-pattern counts per original site and per primary visit and verified **exact equality** against the 21 original aggregation columns in `alfl.capRecap.csv`. It did not merely verify that totals accidentally match.

| Real original 2005 field unit | Verified |
|---|---:|
| Distinct station keys, site summary and covariates | **50** |
| Original primary site×survey opportunities (3 each) | **150** |
| Original primary site×survey sessions with ≥1 bird heard/detected | **69** |
| Site×survey sessions without recorded detected individual | **81** |
| Original individual-positive encounter histories | **98** |
| Stations with ≥1 positively recorded individual | **35** |
| Stations with no recorded individual at any primary session | **15** |
| Positive row patterns in order 001/010/011/100/101/110/111 | **4 / 6 / 13 / 14 / 5 / 11 / 45** |
| Positive intervals out of 98 recorded positive histories, 5min 1/2/3 | **75 / 75 / 67** |
| Positive individual histories by primary survey 1/2/3 | **50 / 31 / 17** |

**Metadata/editorial mismatch preserved:** the `unmarked` software vignette prose describes *49 point-count locations*, but the exact pinned 2005 `alfl.capRecap.csv` and `alflCovs.csv` contain **50 station records** each. The independently verified 98 original individual histories reconcile with all site/visit×pattern nonzero counts. Use **50** for all actual fixed source observations and report the discrepancy rather than arbitrarily dropping a station or claiming every original site had positive recordings.

**Important units:** 98 is a **positive encounter-history row count**, not necessarily 98 unique biological birds across all primary surveys. Likewise 81 no-record sessions are **no observed captured bird in that station during that survey**, not known zero actual birds. Biological abundance and true occupancy cannot be inferred simply by subtracting from 150 or tallying 98.

## 3. Zero-truncated 5-minute detection likelihood and effort composition

Let (h_i\in\{001,010,011,100,101,110,111\}) denote an admitted detected history; its number of detections (k_i\ge1). Under an explicit, simplified closed-15-minute conditional independent homogeneous 5-minute Bernoulli parameter (p\in(0,1)), observing only (h_i\ne000) gives each individual history likelihood:

[
P(h_i\mid h_i\ne000,p)
=\frac{p^{k_i}(1-p)^{3-k_i}}{1-(1-p)^3}.
]

This is a **classical conditional capture/detection model**, not an original theorem, and cannot estimate the number of never-captured birds by itself. The denominator normalizes admission and must not be omitted.

Rust direct full original positive-history conditional MLE:
- **(\widehat p_{5\mathrm{min}}=0.72200000)**, sample log-likelihood (-167.12529799).
- Under **unverified constant p / conditional independence**, an additional independent 5-minute detection opportunity composes by (p_{10}=1-(1-p_5)^2=0.922716), (p_{15}=1-(1-p_5)^3=0.97851505).
- Among only the **98 detected-positive original histories**, the actual count with detection in one of first two 5-minute subwindows is **94/98 = 0.95918367**. This is **conditioned on eventual positive observation** (not 10-minute detection across a complete bird population), and must not be directly claimed to validate the unconditioned model (p_{10}=0.922716); fair conditional model target would use (p_{10}/p_{15}), which is a different quantity.

**Conditional exposure/transport authority:** 5min→10/15min figures are mathematical extrapolations under constant independent opportunities for available birds. They are neither separately randomized observed 10/15-min protocols nor population occupancy or whole Finland source transfer.

## 4. Pooled-vs-interval-heterogeneous detection and heldout comparison

The specified deterministic source station key split kept all positive bird records of the same station together; **70 positive histories in train / 28 positive histories in test**, which is a limited single split. The effective independent sample unit is the source station, not the 98 possibly repeated bird histories.

| Conditional positive-only history model | 70 train histories | 28 heldout histories negative log-likelihood |
|---|---|---:|
| Constant p for three 5-min windows | `p=0.73300000`, train loglik `-117.40731937` | **49.79063947** |
| Three window-specific `p1,p2,p3` | `[0.77128,0.74320,0.68712]`, train loglik `-116.74256895` | **49.53670208** |

The heterogeneous-p model has lower heldout conditional negative loglik by **only 0.25394 total** over 28 histories in this one site split. This is a small, nonindependent, unpowered difference and not evidence of a robust performance advance. Full sample fitted `p1≈0.74944, p2≈0.74944, p3≈0.66952`, full conditional loglik `-166.07981`; potential within-15-min change is *suggested descriptively*, not a causal time effect.

**Mathematical distinction:** within a short fixed 15-minute field protocol, equal 5-minute effort offers closer contact to the assumptions needed for identification of detection `p` *conditional on individual availability and having been captured at least once* than NAAMP's 2001 long-season site re-visits. But **site-level true occupancy, never-heard individuals, field availability, and between-season/collector transport remain HOLD**. Shorter survey time reduces one kind of closure concern, not all forms of detectability heterogeneity, nonstationary singing, or route clustering.

## 5. Lean 4 formal court

Lean 4.24.0 dependency-free original proof source `experiments/mqr-4.98/lean/Mqr498Effort.lean`, no `sorry` or declared axioms. Final CI compiles formal finite-level theorems:
1. Removing zero-capture histories produces exactly the SAME recorded positive sample for two physically different populations `[1,5]` and `[0,1,0,5]`; different latent bird counts cannot be identified from positive-only recorded list.
2. `000` produces no positive recorded bird under the declared three-Bool detection predicate; detecting only in third interval still admits a positive 15-minute capture.
3. Under stipulated constant and independent per-window missed probability (1/2), composing 2 and 3 windows yields exact fractions (1/4), (1/8) through finite natural-number identities. This is conditional elementary arithmetic, NOT independent empirical verification of bird detection independence.
4. Forgetting known effort duration or geographic footprint permits different field protocol records to appear identical after dropping these components. No geographic target population identity follows from a site label.

Lean does **NOT** formally verify Rust floating-point optimizer convergence, true field sample independence, or actual bird ecological occupancy. Its contribution is narrowly a machine-checked mathematical scope counterexample.

## 6. CI, Drive receipts and final scientific stop

**All PASS final GitHub Actions [37891090067](https://github.com/WhoSia/MQR/actions/runs/37891090067)**, both Rust and Lean jobs SUCCESS. Rust 5 tests PASS, full three original CSV hash checks PASS, full 98 positive rows ↔ 50-station 3-primary-survey 7-pattern source aggregate equality PASS; Rust constant p versus interval-p conditional likelihood and strict site-heldout scoring completed; Lean full source no-sorry compile PASS. Initial CI [37891053792](https://github.com/WhoSia/MQR/actions/runs/37891053792) failed Rust compiler syntax on floats without a leading 0 in initial fit starts; fixed and preserved, not deleted.

**Full raw original field data actually stored in existing Google Drive `02_ANALYSIS_SAFE`**, not only links/summary:
- [Alder Flycatcher 2005 complete 3 original source CSVs + pin/custody + exact 98 history ↔ 50 station checks + Rust output](https://drive.google.com/file/d/1Cy49e1yr2LbFV0GQHxGcgBvfyIiQC13s/view).
- [Lean conditional zero-truncation and observation-footprint proof source/build ZIP](https://drive.google.com/file/d/1g1t3URy-aCIkQIPfxPop3dvgDCR5nT_R/view).

**Provenance PASS / observation contract PASS / conditional estimator PASS:** Yes, independently authored biological field sample was verified at source, effort interval lengths are concretely documented, raw recorded positive observations fully reconciled, classical conditional MLE reimplemented in Rust, Lean missing-zero evidence theorem compiled.

**Hold:** Original full bird population and unrecorded individuals, biological occupancy ψ, true site capture/detection against latent availability, site location sampling-frame selection probabilities, verified spatial/geographic transport, NAAMP frog ↔ alder flycatcher across-protocol risk, Finnish Anemone 64 fixed target risk, new general theorems/algorithms, cross-source sample statistical coverage, full study-original researcher field notebook.

**4.98 CLOSED BOUNDED** as requested in MQR workflow: the source-only scientific question is answered with real evidence and explicit limits. Suggested next if PI later approves: **MQR-4.99 — Availability–Detection Separation, Zero-Truncated Observation Processes & Cross-Protocol Risk Identifiability**; no automatic opening or unrelated new concept. Need new independently calibrated *capture availability / known true count* or an explicitly source-grounded identifiability experiment before new investigation.

**Research OS:** only canonical Notion MQR root `3c8ef561cf92815693b6fcf6de9955f7`; append original results and status in same page, no Lab version duplicate/child page. GitHub `main` human `WhoSia` authored commits, read-only CI no github-actions[bot] authored commits.