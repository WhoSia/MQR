# MQR 5.4 — MQR 43 · 기록 17: Shared calibration-file ancestry and unverified reference-log time brackets

**Date:** 2026-11-21. **Conversation MQR 43; research version MQR 5.4 unchanged.**
**Status:** ACTUAL ORIGINAL CALIBRATION FILE HASHES AND REFERENCE LOGS EXAMINED / FOUR RUNS' BYTE-LEVEL COMMON ANCESTRY PASS / FORMAL TRACEABILITY AND CLOCK SYNCHRONIZATION HOLD.
**Archive:** [Šíra (2023), QuantumPower versus differential PJVS original data, DOI 10.5281/zenodo.10046413](https://zenodo.org/records/10046413); [already held source 7z in Drive](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view).
**New executable:** [reference lineage audit](../language/real/experiments/reference_lineage_v54.py) · [8 tests](../language/real/experiments/test_reference_lineage_v54.py) · [source/clock receipt](evidence/mqr_54_chat43_reference_lineage_receipt.json). The byte-identical copy of new code and tests was verified against GitHub Git-blob hashes. Selected four-suite local regression **41/41 PASS** (8 new, plus 12 source audit, 8 segmentation, 13 prior anomaly evidence tests).

## 1. Physical source hierarchy and evidence identity

The source 7z archive contains not only four raw digitizer MAT records, QWTB processing descriptions, and plotted images, but also original **run-owned calibration correction files and seven reference measurement logs**. We performed another exact selective extraction from the same source archive, retaining its original SHA-256 (a4a68342b1e514d7611e6bd6a93d12a4afe5cc5531b92af5ae711a3eb233583e) and hashing every copied calibration file.

Across **four separately timestamped QPSW sessions** 0015, 0016, 0019, 0020, all **six** original calibration-related paths have **exactly the same SHA-256 bytes in every run**:

| Shared source artifact | SHA-256 prefix (full digest in receipt) |
|---|---|
| DIGITIZER/Digitizer correction with MX.info | ffb9ece67353 |
| DIGITIZER/chn1/dummy_chn1.info | c515bc3b35a3 |
| DIGITIZER/chn1/csv/SFDR.csv | 641c4169c1ca |
| DIGITIZER/chn1/csv/Y_inp.csv | aa89b9aebd98 |
| TRANSDUCERS/T01/dummy.info | d059565e77c2 |
| TRANSDUCERS/T01/csv/Z_low.csv | 05ae7bf6158e |

This is a **stronger concrete common-ancestry finding** than merely saying the sessions are on the same day or have similar setup. It establishes that the four observations have overlapping, identical supplied calibration-file inputs. It does NOT establish that their raw waveforms are identical (they are separately hashed and different), that their actual physical calibration errors have identical realized values, or that the correction files' quality is independently certified. It prevents treating the four runs as **four independent calibration ancestries**.

## 2. A real potential before/after reference, with a critical time-clock hold

The archive also contains **seven separate PJVS/Fluke reference-log text files**, each with ten attempted observations. A total of **69 actual numeric voltage measurements** is present (one missing measurement marked by a dash); raw rows contain printed naive local timestamps but no verified timezone or synchronization offset. Those are authentic source-owned reference measurements, not source data synthesized by the analyst.

The QPSW session timestamps explicitly include **+01:00**. Under the **extra assumption** (not yet verified) that the naive PJVS local-time clock matches the QPSW wall clock, the closest reference events before and after all four QPSW run starts are:

- Early reference event **2023-03-10 16:22:05**, value **0.799998157 V** from the 16-03-52 Fluke log.
- Later reference event **2023-03-10 17:15:13**, value **0.799998529 V** from the 17-12-56 Fluke log.

| QPSW run start (+01:00) | Seconds since early reference | Seconds until later reference |
|---|---:|---:|
| 0015, 16:50:40 | 1,715.17 | 1,472.83 |
| 0016, 16:55:22 | 1,997.03 | 1,190.97 |
| 0019, 17:04:08 | 2,523.33 | 664.67 |
| 0020, 17:05:55 | 2,630.79 | 557.21 |

**No formal physical pairing is inferred.** The PJVS reference file names and timestamps do not by themselves establish which QPSW run each reference event calibrates, whether the clocks were synchronized, whether the reported voltage has the identical measurand, or what time interpolation/uncertainty propagation would be justified. The executable defaults to **HOLD_CLOCK_SYNC_UNVERIFIED** and only emits explicitly labeled *candidate temporal brackets* when an investigator sets the clock-comparability assumption. No interpolated calibrator value or purported independent correction is computed.

## 3. What this specifically changes in the previous research

[Records14–15](mqr_54_chat43_14_sira_raw_mat_processing_boundary.md) established that raw digitizer samples and the published QWTB U_t estimates are different mathematical processing objects, and that actual QWTB segmentation can exactly reconstruct full-trace RMS. The new file-level genealogy adds a second axis: **which calibration records have truly noncommon ancestry?**

At least six named correction files are shared byte-for-byte across all four runs. Thus counting the four raw time-series as four independent *calibration routes* would be unsupported. On the other hand the seven original reference logs are potentially useful **additional source evidence**, even though neither their physical pairing nor independence has been verified. Their existence means "there are no reference records" would be factually false; the actual hold is *unverified correspondence and uncertainty*.

The correct next scientific step is not to paste a nearby 0.8 V reading into the QWTB RMS report near 1.13137 V. Instead independently trace the hardware timebase, calibration intent, measured waveform/reference relation, and TWM-QPSW/PSFE algorithm. Only then can a prospective source-to-measurand comparison be warranted.

## 4. Result and MQR origin return

**PASS (scoped):** authentic archive membership; six shared correction SHA lineages; seven reference logs and their numeric observation count; actual timestamp ordering *conditional on common local clock*; transactional error checks. **HOLD:** clocks; physical reference matching; calibrated correction; independent failure ancestry; full processing algorithm; any 5.5 stage promotion.

This adds a real-data illustration to MQR's *finite route separation*: multiple real measured traces with a shared calibration-file ancestor do not represent entirely independent chances for the world to defeat the measurement model. Empirical science does not reduce to the number of printed observations; the apparatus, corrections and source lineage determine what their agreement can justify.
