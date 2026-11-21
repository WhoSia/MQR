# MQR 5.4 — MQR 43 · 기록 13: Real Josephson voltage measurements, temporal dependence and admissible physical pairing

**Date:** 2026-11-21. **Conversation:** 43. **Research version:** 5.4 unchanged.
**Status:** REAL PROCESSED MEASUREMENT DATA ANALYZED / METROLOGICAL AND INTERVENTION CLAIMS HOLD.
**Input:** [Kraus et al. (2025) complete Drive measurement dataset](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view); official [PTB DOI 10.7795/720.20250210](https://oar.ptb.de/resources/show/10.7795/720.20250210); parent publication [DOI 10.1088/1361-6501/adfc87](https://doi.org/10.1088/1361-6501/adfc87).
**Executable:** [measurement source audit](../language/real/experiments/metrology_source_audit_v54.py); [12 unit tests](../language/real/experiments/test_metrology_source_audit_v54.py); [JSON evidence receipt](evidence/mqr_54_chat43_real_metrology_source_receipt.json).

## 1. Actual file bytes and provenance

The locally accessed complete ZIP SHA-256 is cdc5cfe15c2d5f81e59515113b78a5eff5abdcffda624849a154cd3ca5836a8c. Its README identifies the authors as Kraus, Kieler, Behr and Palafox, specifies CC BY 4.0 and describes twelve plot datasets **processed and exported from Origin**. This is a genuine public instrument-derived dataset, **NOT** the original complete 500 kSa/s ADC acquisition or independent verification of a calibration standard.

Figure 6 archive member (Opto-JAWS/fig6a+b.txt), SHA-256 c6e286941e7def4c8b66fa6ed8b3d32b89c9bdb44e108dac175f12d4f6791d8a, has **2,101 rows**, **ten numeric columns**, and no missing entries. Timestamp columns correspond to integer seconds 0 to 2,100 and a rounded 0-to-35-minute scale. Two ADC channel columns can be aligned **within the same table row**, not treated as independent calibrated devices.

## 2. Empirical first/final five-minute contrasts

Select the first and last **300 rows** of the Figure 6 derived amplitude deviation and total harmonic distortion (THD) series:

| Source-derived metric | First-window mean | Final-window mean | Final minus first |
|---|---:|---:|---:|
| Amplitude deviation, microV/V | -97.4835105 | -99.1483566 | **-1.6648460 microV/V** |
| THD, dB | -103.874514 | -103.651557 | **+0.2229565 dB** |

Lag-1 serial correlation: amplitude deviation **0.838647**, THD **0.718867**. Already published moving-average columns have lag-1 correlations **0.999776** and **0.999734**: a derived smoothed trace is **not a new independent evidence route**. Treating the 2,101 seconds as 2,101 independent measurement experiments would be invalid.

An exploratory **within-window moving-block bootstrap** with block length 60 seconds, 2,000 replications and random seed 43 returned central 95% resampling intervals for final-minus-initial means:
- amplitude deviation: **[-2.715408, -0.574383] microV/V**;
- THD: **[+0.138571, +0.305668] dB**.

These are descriptive **dependence-sensitivity intervals**, not ISO/GUM metrological uncertainty, not independent-laboratory confidence, and not evidence of a causal time effect. Window selection, nonstationarity, drift or unknown common calibration error may affect inference. Both effects are small variations within the recorded published series; no claim about the instrument's universal traceability follows.

The row-aligned published dBV difference (Ch1 minus Ch0) averages **+0.0001599524 dBV**, a within-table channel descriptor whose systematic source and calibration cannot be inferred from these data alone.

## 3. Negative controls and root-question relevance

The same ZIP has frequency spectra with identical numerical frequency bins for positive, negative, full-sine and RF-bias-off-noise plots, plus 2-ms trace sections. Common x-axis labels **do not prove same-run or same-specimen pairing** across different figure exports. They must not be relabeled as randomized AB/BA interventions or an independently calibrated device comparison.

The founding MQR UV–Vis question asks why digitized outputs warrant scientific statements. This *world-derived* example shows that row identity, temporal dependence, data smoothing, calibration ancestry, and the estimand determine what conclusions are actually licensed. It supports a source-grounded contrast between physical readouts and evidence-processing decisions, **not** a general metaphysical claim that scientific observations create reality.

**Status:** physical source-byte access and reproducible tabular analysis PASS; original ADC samples for this PTB dataset HOLD; causal intervention comparison HOLD; independent source-to-source same-measurand validation HOLD. [Record14](mqr_54_chat43_14_sira_raw_mat_processing_boundary.md) analyzes a different experiment with genuine raw digitizer MAT files and separate processed QWTB estimates.
