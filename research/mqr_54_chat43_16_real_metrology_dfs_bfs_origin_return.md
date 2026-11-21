# MQR 5.4 — MQR 43 · 기록 16: DFS/BFS return from actual electrical-metrology archives to the founding scientific question

**2026-11-21 · conversation MQR 43 · research version MQR 5.4 unchanged.**
**Status:** TWO REAL WORLD-DERIVED SOURCES / EXACT SOURCE BYTE AND ARITHMETIC REPRODUCTION / NO CROSS-LAB SAME-SPECIMEN BRIDGE OR PHILOSOPHICAL FIRST-DISCOVERY CLAIM.

## 1. What was actually completed

Two distinct, already-held public scientific archives were retrieved via connected Google Drive and materialized in a local runtime. Their official data-publisher pages were cross-checked by DOI.

**Source A — Kraus et al. (2025), PTB optical Josephson voltage standard**, DOI [10.7795/720.20250210](https://oar.ptb.de/resources/show/10.7795/720.20250210). The archive README explicitly calls its 12 figure files *processed Origin exports*, not full raw ADC data. The Figure 6 time-series table has 2,101 one-second observations over 35 minutes. For two nonoverlapping five-minute windows, amplitude deviation changes by -1.664846 microV/V and THD by +0.222957 dB; autocorrelation prevents treating the seconds as independent replicates. A 60-second moving-block bootstrap gives explanatory sensitivity bounds but **not a metrological uncertainty certificate**. [Detailed record13](mqr_54_chat43_13_kraus_real_timeseries_autocorrelation.md).

**Source B — Šíra (2023), Zenodo quantum-power versus PJVS measurement data**, DOI [10.5281/zenodo.10046413](https://zenodo.org/records/10046413). The complete 7z archive was opened with libarchive; four MAT raw samples (3,420,000 integer ADC counts each, 60,000 Sa/s and source-owned gain 5.5250876e-9 V/count) and corresponding session/processed result files were extracted and inspected. All-source-byte hashes and per-run timestamps were sealed in [measurement receipt](evidence/mqr_54_chat43_real_metrology_source_receipt.json). The naive entire-record RMS ranges from 0.812609 to 0.813300 V, whereas the separately reported 30-value QWTB U_t means range from 1.131368 to 1.131369 V. These are **not shown to be the same estimator/measurand**, and the actual full TWM-PSFE/QWTB algorithm has NOT been independently implemented. [Record14](mqr_54_chat43_14_sira_raw_mat_processing_boundary.md).

A further real-source **source-segmentation DFS** read 61 sample-boundary indices and 60 operator markers from the four QWTB result files, reconstructing the exact source-defined partition into 30 shorter and 30 longer intervals. Reweighting each interval's actual raw RMS squared by its sample count recovers full raw RMS with absolute error ≤1.11e-16 V for all four original files. This checks arithmetic identity and metadata alignment, **not** QWTB's fitted scientific result. [Record15](mqr_54_chat43_15_sira_qwtb_segment_energy_identity.md) and [segment receipt](evidence/mqr_54_chat43_qwtb_segmentation_receipt.json).

## 2. Analytic origin return: reading a number is not yet measuring the intended quantity

The foundational 2026-08-26 MQR UV–Vis concern can be recast as a concrete research question: **What independently defeasible evidence links a digitized trace, an instrument transformation, a calibration convention and the exact scientific claim being reported?**

In the two real examples, there are multiple separable levels:

- **Physical acquisition and raw preservation**: who measured what, when, on which instrument, with what sampling conditions and time alignment?
- **Software/source transformation**: what was selected, averaged, fitted, linearized or otherwise turned into a reported numeric feature?
- **Calibration and intended measurand**: which independently checked reference chain and model connect that feature to the quantity the laboratory actually claims?
- **Epistemic task/authority**: which scientific decision does this reported quantity support, and what alternative physical outcome could defeat it?

None can be derived from syntactic equality of displayed numbers or a code checksum alone. A checksum proves reproducible *bytes*, not that the sensor physically captured the declared phenomenon or that the chosen interpretation is correct. A perfect arithmetic identity over partitioned samples is more than a toy but remains an algorithmic verification rather than independent metrological calibration.

Conversely, **source-bound transparency is a genuine research advance**: without the actual MAT and S boundary values, the analyst could only speculate about whether the reported figure and the raw signal concerned the same operation. Their access makes a precise empirical processing stage testable and explicitly identifies where the physical model still cannot be reconstructed.

## 3. Serious BFS rivals and research consequences

| Competing perspective | What these examples bear on | What they do not prove |
|---|---|---|
| Pure digital reduction | Both archives contain machine-readable numerical traces that can be computationally processed. | The provenance of transduction, calibration, experimental intent or world contact follows from digits alone. |
| Fixed instrumental realism | The original MAT counts, sampling rate, gain and processed data are genuine empirical records with checkable hashes and structure. | A single uncorrected RMS is automatically the correctly calibrated physical measurand. |
| Unrestricted conventionalism | Different software operations can produce different statistics from the same data. | All operations are equally useful or equally validated; the source's actual experimental constraints restrict interpretations. |
| MQR's candidate open-world account | Record the admissible claim, independent failure routes, processing maps and surviving rivals, and re-open the question when the intended measurand is not identified. | A new conceptual ontology or experimentally independent common-world bridge has been earned by these archives. |

This synthesis is consistent with the long-standing metrological literature and MQR's held Chang/Tal/Feest-Nersessian primary-source reading, so **no new philosophical theorem or physical standard** is claimed.

## 4. Research portfolio decision, 5.4 seven branches

- **DFS KEEP (branches 1,5,6):** work on actual digitization, software estimands and uncertainty/source controls, not simulated permutation-only data.
- **DFS STOP:** no additional whole-record-versus-processed RMS comparison should be rhetorically called calibration failure until TWM-PSFE's exact segment sign/source pattern, correction and phase estimands are implemented.
- **BFS KEEP (branches 2,3,4,7):** historical cases of different scientific languages and changing questions remain essential. A processing disagreement across two numerical quantities is **not** itself a newly created concept.
- **Prioritize next (concrete):** reproduce the source's QWTB algorithm and cross-check its reported U_t using its true calibration/reference model; inspect calibration provenance and uncertainty mode; attempt a separately documented physically paired reference chain. If the source lacks required metadata, explicitly return HOLD with a reproducible failure.
- **BACKTRACK capsule:** both published datasets are *from different institutions/apparatus* and are **not an independent matched head-to-head experiment** on one specimen. Do not claim physical cross-science transport or close old A1/A2 missing original raw records from unrelated studies.

## 5. Reproducible work and degree of evidence

[Measurement code](../language/real/experiments/metrology_source_audit_v54.py) · [12 tests](../language/real/experiments/test_metrology_source_audit_v54.py) · [QWTB segment code](../language/real/experiments/qwtb_segment_geometry_v54.py) · [8 tests](../language/real/experiments/test_qwtb_segment_geometry_v54.py).

The 12 new source-audit tests and 8 new segment tests both passed. A local combined run with the **13 prior anomaly-custody tests** obtained **33/33 passed**. This is a selected cross-unit local regression, not the whole Real-Language repository CI and not independent physical replication. Repo code Git blob SHA was checked against executed local bytes and the full dataset hashes are recorded; the input archives themselves remain in connected Drive and are **not** checked into GitHub.

**MQR 5.4 remains OPEN.** This is an actual-world-data DFS gain and a sharper founding-question specification, not a forced version change.
