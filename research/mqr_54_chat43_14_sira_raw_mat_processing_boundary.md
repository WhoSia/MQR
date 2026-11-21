# MQR 5.4 — MQR 43 · 기록 14: Real raw AC-voltage records and the QWTB processing boundary

**2026-11-21. Conversation MQR 43; research version 5.4 unchanged.**
**Status:** REAL DIGITIZER MAT SAMPLES EXAMINED / PROCESSING-TO-RAW MISMATCH IN ESTIMAND FOUND / FULL QWTB ALGORITHM REPLICATION AND PHYSICAL METHOD COMPARISON HOLD.
**Original archive:** [Šíra (2023), Dataset for comparison of QuantumPower method to the differential PJVS method](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view); provider [Zenodo DOI 10.5281/zenodo.10046413](https://zenodo.org/records/10046413). The provider describes calibration-method comparison with a digitizer and programmable Josephson voltage standard (PJVS); our restricted analysis below **does not** re-perform that two-method comparison.
**Reproduce:** [real metrology audit code](../language/real/experiments/metrology_source_audit_v54.py), [12 unit tests](../language/real/experiments/test_metrology_source_audit_v54.py), [source-hash/stats receipt](evidence/mqr_54_chat43_real_metrology_source_receipt.json).

## 1. Physical data, not a plotted synthetic surrogate

The original, already held Drive 7z archive was mounted into the analysis container and opened with libarchive; SHA-256:

a4a68342b1e514d7611e6bd6a93d12a4afe5cc5531b92af5ae711a3eb233583e

The archive contains **769 entries**, **728 files**, and four nonempty digitizer MAT files, one for each session whose identifiers include **0015, 0016, 0019, 0020**. The four raw MAT members were extracted without changing source byte content and separately hashed (complete SHA-256 recorded in the JSON receipt). Each session has its own session.info, QWTB processed RESULTS file, and raw MAT recording; the full archive includes reference files as well, but those references were **not independently matched to every sample** in this study.

The session files state **3,420,000 digitizer counts per MAT recording**, 60,000 samples per second, nominal record duration 57 seconds, and the same declared count-to-voltage gain **5.5250876e-9 V/count**. The MAT variable y was verified to contain integer digitizer counts. The RESULTS section named U_t is labeled RMS voltage and contains **30 processed values per session**. The QWTB setup states **uncertainty mode: none**, so no published U_t measurement uncertainty is available through this specific processing configuration.

## 2. The actual numbers and the critical comparability boundary

An intentionally simple *full-record unsegmented* RMS over raw digitizer samples is computed as square root of the mean square of all reconstructed voltage samples. A separate summary reads the **reported U_t** values and computes their arithmetic mean. The two estimators do **not** use the same selection/processing pipeline and must not be called competing estimates of an established common measurand without additional verification.

| Session ID | Session timestamp (+01:00) | Full-record unsegmented RMS (V) | Mean of 30 processed U_t (V) |
|---|---|---:|---:|
| 0015 | 2023-03-10 16:50:40 | 0.812609293 | 1.131369320 |
| 0016 | 2023-03-10 16:55:22 | 0.813035970 | 1.131368430 |
| 0019 | 2023-03-10 17:04:08 | 0.813023608 | 1.131367865 |
| 0020 | 2023-03-10 17:05:55 | 0.813300092 | 1.131367740 |

This is a substantial, reproducible **processing sensitivity observation** from real recorded bytes. The raw samples can contain source segments, duty cycles, transitions, or conditioning effects that are not simply represented by the PSFE/QPSW processed RMS; it is **not** justified to call the difference calibration failure or software error. Specifically, we did not implement the full supplied TWM-QPSW / TWM-PSFE segmentation, source-reference and correction pipeline or verify its physical definition of U_t. An exact figure-only publication does not resolve this automatically.

The four sessions have distinct timestamps and raw SHA-256 hashes but share the model family and stated digitizer gain. Their adjacent run identities and common instrument lineage **do not** constitute four independent laboratory routes. The 30 processed U_t entries in one session are not automatically 30 statistically independent experiments. No conclusion about separate PJVS calibration methods is claimed from this one-routine comparison.

## 3. DFS outcome: evidence-processing rules are substantive

The original MQR UV–Vis problem asked whether science could be reduced to outputs displayed by instruments. Here the complete raw MAT trace plus a declared volts-per-count conversion is an **incomplete model of the experimental claim**: QWTB's segment masks, nominal reference, timing, channel correction, and applied source model determine the derived RMS voltage. Without them, visually compelling numbers from the same source may answer *different* measurement questions.

A follow-on DFS would need exact PSFE algorithm implementation, all reference/calibrator provenance, explicit coincidence/paired-run metadata, and independent calibration checks. It must be preregistered against the recorded processing expectation and report which pipeline decisions are really tested. The source's declared QWTB uncertainty mode none is a blocking issue for promoting a calibrated confidence interval.

## 4. Honest cross-dataset scope

[Kraus record13](mqr_54_chat43_13_kraus_real_timeseries_autocorrelation.md) is a **different optical-JAWS apparatus at another institution/publication** and does not measure the same physical object and condition as these Šíra data. Both are genuine measurement-derived artifacts, but comparing their numerical RMS or time drift **cannot** establish cross-science agreement, metrological equivalence, or independence of failure modes. The research program now has two real-data **evidence-custody exemplars**, not one joint experiment.

**Director decision:** real source-access and sample-level measurement arithmetic PASS; exact published processed-algorithm reproducibility HOLD; two-calibration-method comparison HOLD; actual physical cross-laboratory bridge HOLD; MQR 5.4 remains open. Preserve these targets in the live missing-source ledger without incorrectly declaring an old A1/A2 missing raw series closed.
