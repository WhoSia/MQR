# MQR 44 — raw channel diagnostics; NOT a quantum reference validation

Source: [Šíra (2023) dataset, Zenodo 10046413](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view). Measurements from 2023-03-10, F7520A nominal 0.8V 60Hz source, NI PXI-5922 serial F22D5B, 24 bit, 60kSa/s, 3,420,000 count samples =57s per MAT file. The four sessions all report gain 5.5250876e-9 V/count and zero recorded offset. No QPSW/PSFE reference corrections were applied; numbers below are exploratory.

| Session suffix | raw sample mean, V | raw RMS, V | RMS after *arithmetic* DC centering, V |
|---|---:|---:|---:|
| 0015 | -0.001075456864 | 0.812609292612 | 0.812608580948 |
| 0016 (`slave_Gnd`) | -0.000834951197 | 0.813035969904 | 0.813035541175 |
| 0019 (`slave_Gnd_i_Grd`) | -0.001724032116 | 0.813023607718 | 0.813021779794 |
| 0020 (`slave_Gnd_i_Grd`) | -0.006257626344 | 0.813300092253 | 0.813276018441 |

For every row, by definition, `RMS^2 = (AC_RMS)^2 + (mean)^2`. The fourth session's noticeably larger DC offset explains only part of its raw RMS shift. The **mode labels, sample timestamps and digitizer channel don't establish matched paired method assignment**, and the data format contains QPSW reference switching; therefore **none of the inter-row differences measure method superiority**, quantization error, a physical ground-loop effect or bias-corrected instrument uncertainty. In particular, 0.813V must NOT be misread as a failed 0.8V absolute standard.

An actual physical comparison requires matched reference waveform stages, correction file `DIGITIZER\Digitizer correction with MX.info`, sequence/deconvolution from `qwtb.info` (algorithm `TWM-QPSW`, `TWM-PSFE`), and traceable `Uref` and a validated uncertainty budget. A valuable subsequent test is whether two distinct correction pipelines give a stable same-session transfer contrast after reference reconstruction. Until then the numerical observations are **uncorrected ADC stream characteristics only**.

[Reproducible local reader](../language/real/experiments/sira_qpsw_uncorrected_audit_v54.py) and [negative/synthetic tests](../language/real/experiments/test_sira_qpsw_uncorrected_audit_v54.py).
