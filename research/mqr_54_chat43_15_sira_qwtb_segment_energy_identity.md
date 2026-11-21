# MQR 5.4 — MQR 43 · 기록 15: Real QWTB segment geometry and exact source-to-statistic non-equivalence

**Date:** 2026-11-21. **Conversation:** MQR 43. **Program version:** MQR 5.4 (unchanged).
**Status:** FOUR REAL RAW MAT FILES, PARSED EXPERIMENT METADATA, EXACT ENERGY-PARTITION CHECK / FINAL QWTB TWM-PSFE REPLICATION HOLD.
**Dataset:** [Šíra (2023) Zenodo 10.5281/zenodo.10046413](https://zenodo.org/records/10046413), [Drive-held original bytes](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view). Earlier [record14](mqr_54_chat43_14_sira_raw_mat_processing_boundary.md) established raw MAT and U_t processing disagreement without equating distinct estimands.
**Code:** [QWTB segmentation reader](../language/real/experiments/qwtb_segment_geometry_v54.py), [8 new unit tests](../language/real/experiments/test_qwtb_segment_geometry_v54.py) and [numeric receipt](evidence/mqr_54_chat43_qwtb_segmentation_receipt.json).

## 1. The source's own segmentation coordinates

We parsed actual QWTB setup metadata from the processed-results INFO file of **each of four original sessions**, not guessed arbitrary time partitions. The matrix S contains **61 one-based sample boundaries**, starting with index 1 and ending at index 3,420,001. The matrix M contains 60 alternating negative/positive markers. These are source **metadata labels**; we do not presume knowledge of how the full TWM-PSFE algorithm uses M or whether a stated source polarity was physically realized correctly.

The S intervals, after converting to zero-based Python indices, partition each **3,420,000-sample** raw MAT record into **60 adjacent segments**: 30 short and 30 long. In every one of four measured runs the exact interval-width census is:

- 2 short segments of 11,999 samples and 28 of 12,000;
- 28 long segments of 102,000 samples and 2 of 102,001.

There are no gaps, overlaps or unmatched samples. These tiny one-sample deviations are present **in the source metadata**; we did not repair or regularize them.

## 2. Independently recomposed raw-signal RMS

For disjoint intervals indexed j, with sample counts n_j, interval RMS r_j and total number of samples N, the identity

R_all = sqrt( sum_j [n_j * r_j^2] / N )

is an exact algebraic consequence of the definition of the root mean square. It does **not** prove that r_j is a quantum voltage standard's properly corrected traceable output or that QWTB uses this formula as its final estimator.

Applying this exact partition using the *real source-defined S* to all four MAT recordings gives:

| Run | Arithmetic mean of 30 short-segment RMS (V) | Mean of 30 long-segment RMS (V) | Full-record and reweighted RMS (V) |
|---|---:|---:|---:|
| 0015 | 0.928578114 | 0.797858564 | 0.812609293 |
| 0016 | 0.930776713 | 0.798042979 | 0.813035970 |
| 0019 | 0.928302578 | 0.798367839 | 0.813023608 |
| 0020 | 0.936316312 | 0.797581256 | 0.813300092 |

The absolute difference between direct all-sample RMS and sample-count-weighted segment reconstruction is **at most 1.11e-16 V**, consistent with ordinary floating-point rounding. This is a genuine byte-grounded arithmetic **PASS** on source segmentation: all samples are accounted for and the energy decomposition is correct.

The average short and long segment RMS are visibly different, while the long segments dominate the time-weighted aggregate. Averaging segment RMS without respecting segment lengths would change the question being calculated, even before specialized metrological correction.

## 3. What this does *not* establish

The results do **not** reconstruct the separately published QWTB processed U_t means near 1.13137 V (see [record14](mqr_54_chat43_14_sira_raw_mat_processing_boundary.md)). QWTB may use pattern markers, phase-sensitive fits, source-reference vectors, segment selection, digitizer calibration and other transformations that the simple energy identity does not implement. The resulting two RMS numbers are **not certified estimates of the same measurand**, so their difference is not a proof of failure of quantum standards or of the published paper.

The source metadata's uncertainty mode is explicitly none; we do not infer a calibrated instrument uncertainty from the dispersion of the 30 U_t output entries. Those entries share the same experimental route.

The real-world advance is more narrow but important: the previous MQR finite toy framework assumed a map from raw states to outputs. This case gives a **physical trace, a real source-owned segmentation operator, and exact calculational controls** showing how far a raw numeric summary can be reproduced before source-model-specific physical semantics become essential.

## 4. DFS exit and BFS return

**DFS PASS:** source archive SHA, actual MAT counts, acquisition gain, 61 source boundaries, 60 segment lengths, zero gaps/overlaps and the exact RMS energy partition.
**DFS HOLD:** implement the actual TWM-PSFE/QWTB estimator, source pattern Uref, calibration corrections, uncertainty propagation and independent reference comparison.
**BFS return:** compare this with [Kraus's real Figure 6 temporal series](mqr_54_chat43_13_kraus_real_timeseries_autocorrelation.md): one source gives many timestamped **processed** outputs without full ADC signals; the other gives raw ADC signals plus a source-specific calibration/processing language. Neither makes a neutral, theory-free measurement value available by just displaying a number.

The original MQR question about digitization and the construction of scientific measurement can now be sharpened using **actual measured bytes**, not only simulated possible-science state maps. No concept genesis or MQR 5.5 upgrade is claimed.
