# MQR44 — Šíra QuantumPower/PJVS source archive: actual raw-sample witnesses

## Identity and custody
Archive: [Šíra (2023) Zenodo 10046413](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view), deposited 2023, `71,607,511` compressed bytes, MD5 `e53319bb7d760122979e9b6c60395598`, SHA256 `a4a68342b1e514d7611e6bd6a93d12a4afe5cc5531b92af5ae711a3eb233583e`. Local `7z` listing: **769 archive members**: 4 MATLAB samples `.mat`, 28 `.info` metadata objects, 12 `.csv` tables, 7 `.txt`, 337 `.fig` and 339 `.png` with 1 `.ods` (the sum is 728? **check counts through actual 7z manifest before relying on breakdown**; total 769 verified). Original archive retained, never overwritten by extracted derivatives.

### Four original measurement streams

All four MAT objects `y` contain **3,420,000 int32 samples**, at **60,000 Sa/s =57s per acquisition**, `NI PXI-5922` 24-bit ADC serial `F22D5B`; recorded gain `5.5250876 × 10^-9 V/count`, offset zero, nominal **0.8 V, 60 Hz**  `calibrator_F7520A` source. Four original run labels include different `slave_Gnd` and `slave_Gnd_i_Grd` conditions. The .info metadata and QPSW processing recipe must be parsed before declaring a voltage result.

| Run | session local timestamp CET | indicated temperature °C | SIMPLE sample-count×gain RMS, V | simple mean (DC), V |
|---|---|---:|---:|---:|
| 0015 | 2023-03-10 16:50:40 | 35.994 | 0.812609293 | -0.001075457 |
| 0016 slave Gnd | 2023-03-10 16:55:22 | 36.431 | 0.813035970 | -0.000834951 |
| 0019 slave Gnd i Grd | 2023-03-10 17:04:08 | 36.988 | 0.813023608 | -0.001724032 |
| 0020 slave Gnd i Grd | 2023-03-10 17:05:55 | 36.977 | 0.813300092 | -0.006257626 |

**WARNING (important scientific gate):** numbers above are naïve uncorrected RMS and offset of a digitizer stream. The archive's `qwtb.info` names QPSW processing `TWM-QPSW` / `TWM-PSFE`, reference `Uref`, multiplexer switching and correction steps. It does not justify `0.813 V` as a true calibrated test voltage, “0.8V source failed by 13mV”, a comparison of QuantumPower vs differential PJVS method, or causal effect of swapping ground. No before/after pairing identity is established merely from run order or identical instrument metadata. Run 0020's DC offset (−6.26mV) is visibly different and makes uncorrected waveform magnitude comparisons even more suspect. A corrected method-by-method result is a **HOLD** until reference channels, switching periods and calibration logic are reconstructed.

### Audit boundaries and next gate

The same file *really contains raw digitizer samples*, an advance over only paper figures; this **closes the availability gap for an alternative 2023 method dataset**, not the exact historical `2013 Burroughs` or `2015 Behr` waveform runs. To estimate physical method differences, parse measured reference `Uref` and channel switching sequences, apply correction and uncertainty, identify which modes are *simultaneous paired samples* vs separate sequential runs, and test a holdout of corrected result. If no exact pairing, report observational differences only. Archive originals are in central non-paper sources, not MQR chat history.
