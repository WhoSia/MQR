# MQR 45 — Šíra QPSW: original archived processing results are evidence, not yet a calibration reproduction

**Source:** [Šíra (2023), original Zenodo 10046413 archive](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view), 71,607,511-byte 7z with original experimental MAT and sidecar `qwtb.info`, `session.info`, `DIGITIZER`, `RESULTS/TWM-QPSW-G0001-A0001.info`, several `QPSW_plots`. Source-relative paths preserved in extracted local analysis, the original 7z is canonical on Drive; no edited archive was uploaded. Previous [uncorrected signal audit](mqr_54_mqr44_qpsw_four_run_diagnostic.md) reported 4×3,420,000 integer counts at 60kSa/s; the previous warning "reference correction not yet reproduced" remains true.

## Work unit and executable checks

We independently located and inspected four **publisher-created processed** `TWM-QPSW-G0001-A0001.info` outputs, in addition to `qwtb.info` input sidecars. The following metadata was checked per run (0015, 0016, 0019, 0020):

- **M**: 60 alternating ±1 signs; **S**: 61 one-based sample boundaries starting at 1 and ending 3,420,001, covering exactly 3,420,000 MAT samples; **Uref**: 20 listed reference voltage levels. Window differences: 28×12,000 + 2×11,999 + 28×102,000 + 2×102,001 samples. The 60 intervals are 30 short + 30 long; their *meaning* as reference or source windows is a separate pipeline question, not inferred from length alone.
- `RESULTS` has `U_t`: 30 processed numbers; `U`: one summary. Arithmetic average of the 30 output values matches the recorded summary to about 3×10⁻¹⁵ V (double precision), independently for each run. `uncertainty mode:: none` is explicitly declared.
- Stored processed summary and SD of 30 *within-run* outputs (not externally validated standard uncertainty):

| Run label | Author's stored `U`, V | SD of thirty `U_t`, µV |
|---|---:|---:|
| 0015 | 1.13136932024924 | 2.803179 |
| 0016 (`slave Gnd`) | 1.13136842965589 | 2.470136 |
| 0019 (`slave Gnd i Grd`) | 1.13136786503653 | 2.984978 |
| 0020 (`slave Gnd i Grd`) | 1.13136773999032 | 1.995162 |

The largest pairwise difference among reported means is ~**1.580259 µV**, but runs are sequential, within-run windows are correlated, and the paper's conditions differ. No statistical test of grounding or method superiority follows from those four means.

## A *new* important semantic gap

The source filename names a **0.8 V RMS / 60 Hz calibrator setting**, but the stored `U_t` and `U` sections are explicitly described as *RMS voltage* and lie at **1.1313677–1.1313693 V**, numerically within about **−1.35 to −2.75 ppm of 0.8×√2 V**. The correspondence to nominal *peak* amplitude may be informative, but there are multiple live explanations: whether the source setting or reference waveform represents RMS vs peak, a normalization/scale convention internal to `TWM-QPSW` / `TWM-PSFE`, stored result naming conventions, and actual signal conditions. **This is a metadata-to-physical-meaning HOLD, not proof of a software bug or calibrated 1.131 V quantum output.** Reference `Uref` levels reach ±1.35 V and have distinct roles; do not confuse the array extrema with the test-source RMS.

The original `RESULTS` is precomputed by the original experimental authors. Reading, validating its internal arithmetic and comparing source labels **is not the same as independent rerunning the full QPSW algorithm** on the 3.42 million sample traces. This distinction corrects the previously stated simplistic gate "need raw calibration": actual processed outputs are *already held*, but method chain verification is still open.

## Claim conditions

1. **Reproduce** precisely the QWTB `TWM-QPSW` with 60 switching windows, `M/S/Uref`, digitizer correction files, `TWM-PSFE` numerical options, clock and recorder settings. Compare per-window outputs, not only the final U scalar.
2. **Cross-validate** the amplitude semantics with the original paper's method description and independent Fluke5720A reference TXT values, and test whether the result uses peak or RMS normalization. Before that, do not report an inferred physical mismatch/error.
3. **Pair run comparisons only with documented shared reference and timing**; two 0019/0020 tags share a wording but not a simultaneous preparation by assertion.
4. **Do not use n=30 windows as independent experimental replicates** for the uncertainty budget; archive explicitly leaves uncertainty off.

[Reader and gate](../language/real/experiments/sira_qwtb_archived_output_audit_v54.py) · [9 local counterexample/validation tests](../language/real/experiments/test_sira_qwtb_archived_output_audit_v54.py). Source authenticity: archive MD5 previously verified against Zenodo metadata; the extracted result .info files were read directly from that held 7z, not external copies. No claim of full software pipeline reproduction or new SI traceability.
