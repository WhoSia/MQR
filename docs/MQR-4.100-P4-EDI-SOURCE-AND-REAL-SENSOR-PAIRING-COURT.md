# MQR-4.100 — P4 Source-Provenance, EDI Version Gating and Independent-Channel Contact

**Internal stage P4, not a separate official research title.** The fixed official name remains **MQR-4.100 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport**.

**Date:** 2026-10-09. **Research type:** retrospective external-source verification and a single-source, two-physical-sensor exploratory comparison. NOT a pre-registered experiment, new theorem, proof of sensor noise independence, estimate of Blackwell/Le Cam deficiency, or evidence of target-population transport.

## A. Source version court: Palmer three independent EDI data packages

The original 2007–2009 Palmer Station LTER penguin collection is cited in the *palmerpenguins* R Journal publication as the combination of three EDI data packages, each species-specific:

| Species | Research-package identifier | Published EDI DOI |
| --- | --- | --- |
| Adélie | `knb-lter-pal.219.5` | https://doi.org/10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f |
| Gentoo | `knb-lter-pal.220.5` | https://doi.org/10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689 |
| Chinstrap | `knb-lter-pal.221.6` | https://doi.org/10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e |

Citation: Horst, Hill & Gorman (2022), *Palmer Archipelago Penguins Data in the palmerpenguins R Package*, https://journal.r-project.org/articles/RJ-2022-020/. The original research Gorman, Williams & Fraser (2014): https://doi.org/10.1371/journal.pone.0090081.

**VERSION COLLISION:** The palmerpenguins online download vignette `https://allisonhorst.github.io/palmerpenguins/articles/download.html` illustrates `knb-lter-pal.219.3`, `220.3`, `221.2` earlier package versions. These are NOT interchangeable with the 2020-cited `219.5/220.5/221.6` without a version reconciliation. Do not infer a first-party file-byte match merely from DOI and column names.

**Acquisition attempts 2026-10-09:** The actual three historical EDI source bytes were NOT acquired. `pasta.lternet.edu/package/data/eml/...` returned HTTP 403 on the tested route, `portal.edirepository.org/nis/dataviewer?...packageid=...` served a Data Portal Login HTML page rather than a CSV, and the alternative PASTA host did not resolve from the retrieval environment. No original-record EDI source SHA-256 or source row-level join has been verified. The previously pinned 344-row `palmerpenguins/inst/extdata/penguins_raw.csv` Git blob alone is a **secondary combined CSV**, not proof of exact consistency with the three EDI originals.

To prohibit a silent source substitution, `experiments/mqr-4.100/p4_edi_reconcile.py` provides a **manual, currently unexecuted three-input source contract**. It checks species/version input labels, byte checksums, `studyName+Individual ID` keys, 17 field values (Decimal-normalized where numeric), missing and extra source keys. It **refuses to run** without actual three supplied files. This utility being committed is NOT an EDI lineage PASS.

**EDI verdict: SOURCE ENTITY IDs / published VERSION DOIs CONFIRMED; THREE ORIGINAL CSV BYTES & JOIN: HOLD_ACCESS_NOT_VERIFIED.**

## B. Separate physical channels from an ORIGINAL dataset record — UCI HAR

Original UCI Machine Learning Repository dataset https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones ; DOI https://doi.org/10.24432/C54S4K. Credits: Jorge Reyes-Ortiz, Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra. Released in 2012/2013. Independent of the Palmer study in source lineage (but **not independent sensors/labels within itself**).

From 30 volunteers with waist-mounted smartphones: raw physical accelerometer and gyroscope, sampled at 50 Hz, preprocessed into 2.56-second 128-sample overlapping 50%-stride windows, with video-derived activity labels for six states. Data contains explicitly split training and test **subject identifiers**, where participants do not overlap. It is a *preprocessed* sensor-window archive, NOT external confirmation of raw device clock synchronization or a field trial.

**Official published archive, observed bytes**:
- UCI outer double-zip URL: `https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip`.
- Byte SHA256 (outer): `c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031`; exact size **61,005,872**.
- Nested `UCI HAR Dataset.zip`: SHA256 `2045e435c955214b38145fb5fa00776c72814f01b203fec405152dac7d5bfeb0`; exact size **60,999,314**.
- Two physical sensor classes: accelerometer `total_acc_[x|y|z]_[train|test].txt` (includes gravity) and gyroscope `body_gyro_[x|y|z]_[train|test].txt` (angular velocity).
- 7,352 training windows, 2,947 test windows. Each of twelve axis × partition source text files has exactly the corresponding N rows, each with 128 numeric time positions, indexed to that partition's `subject_*.txt` and video-derived `y_*.txt`.
- Exactly 21 training subjects, 9 distinct test subjects, none overlapping; all 6 activity labels represented in both partitions. The original train/test are the publishers' subject split, not a new split invented by MQR.

**Levels of evidence:** Two sensor *types* with distinct physical measurement principles, in the same phone and experiment, vs two scientifically independent sources. The former is documented; the latter is not. Pairing comes from the **publisher's common window indexing**, not an independently verified device-clock pair identifier. Therefore this dataset justifies finite same-window feature fusion as observational data, but it does not certify matched external observation authorities, true \(E_\theta\) kernels, any \(\epsilon=\sup_\theta d_{TV}(E_\theta,\pi J_\theta)\), or a universal identification guarantee.

## C. Retrospective two-sensor decision contrast

**Predeclared computational procedure for this version of the audit, NOT blind preregistration:** for each 128-point window per axis, compute population mean and standard deviation; use six values from 3 accelerometer axes vs all twelve (plus gyroscope axes). Train nearest 6-activity class centroids using only the official **7,352 training windows**, scaling each feature by population standard deviation calculated on training windows only. Evaluate top-1 0/1 accuracy on the official subject-disjoint 2,947-window test split. The estimand here is **this fixed classifier's heldout accuracy on these recorded participants**, not the optimal Bayes risk for a known family of experiments.

Separate negative control: rotate each test gyroscope vector by 17 window rows while retaining the accelerometer row. This leaves test gyroscope marginal sample distribution fixed but changes activity/subject conditional alignment: **NOT a causal pairing effect**, and not a sensor-physics experiment.

The initial independent browser-side byte-pinned replay (prior to GitHub CI) computed:
- acceleration-only **2,121/2,947 correct**, acceleration+gyroscope **2,128/2,947 correct**; net change +7 windows (**+0.2375 percentage points**).
- 217 misclassifications corrected, 210 formerly correct rows misclassified after adding the gyroscope. The tiny net gain is NOT uniform across the nine heldout subjects; individual results diverge.
- artificial gyro-window rotation score **1,837/2,947**, which may reflect broken within-activity association, not an isolated pairing causal effect.
- subject-block descriptive 2,000-resample `delta_accuracy` percentile interval **[-0.02589,+0.02955]** (about -2.59 to +2.96 pp). Overlapping 50%-stride windows are correlated, model decisions were not blind-preregistered and only nine test people were observed. This is NOT a confirmatory CI for new-population risk, no population validity guarantee.

**A useful negative result:** even when two physical sensor channels are actually aligned in published observation windows, a **particular poorly optimized, fixed low-dimensional classifier** can gain almost no heldout accuracy when the extra signal is supplied. This does not establish that the gyroscope contains no additional information, that two-channel experiments have equal Blackwell value, or that another model cannot exploit its signal.

## D. Repository and adjudication gates

- `experiments/mqr-4.100/p4_uci_har.py`: Python stdlib original nested ZIP hash and row/window checks; nearest-centroid demonstration and subject-aware exploratory interval. Same source, not independent empirical validation.
- `experiments/mqr-4.100/src/bin/p4_sensor_structure.rs`: independent Rust parsing of window sizes, subject and label rows and within-window coordinate counts from publisher files.
- `experiments/mqr-4.100/p4_edi_reconcile.py`: **NOT executed without three actual EDI files**, source version/witness gate.
- `.github/workflows/mqr-4.100-p4-source-channels.yml`: read-only GitHub Actions; reacquires pinned original 61 MB source ZIP, validates actual axes, downloads receipt and preserves original byte/archive. No bot authored commit.
- README retains the unchanged 4.100 title and P4 as internal stage only. Do not close MQR-4.99 biological availability source HOLD or scientific MQR-4.100 based on these outputs.

**P4 initial status:** TWO SENSOR SOURCE REPLAY AWAITING MAIN CI; EDI ORIGINAL ROW MATCH HOLD; CROSS-PROTOCOL θ-IDENTIFIABILITY AND RISK TRANSPORT HOLD.

**Next substantive test:** EDI three first-party files in their exact historical versions for a real 344-row field comparison, and/or independently timestamped or manually audited physical sensor channels on the *same individual* with an independent outcome adjudication. Even that still requires a defensible population and event mapping to make transport claims.
