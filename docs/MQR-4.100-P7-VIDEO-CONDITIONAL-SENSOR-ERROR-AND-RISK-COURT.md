# MQR-4.100 — Internal P7 Video-Conditional Sensor-Error Coupling and Decision-Loss Court

**Official title remains:** MQR-4.100 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport. **P7 is NOT a new formal title.**

**2026-10-09. Retrospective empirical provenance- and decision-score court, NOT a new identification theorem.** MQR-4.100 as a whole remains OPEN. This is **real publisher-observed signal and video-annotation-conditioned event evaluation**, NOT an independent new sensor collection, externally verified truth, latent-state point identification or population-level Bayes-risk transport.

## A. Why move beyond first-party EDI table provenance?

The full original EDI P6 result is now **source-lineage PASS**: all 344 rows and 5,848 fields traced to exactly specified publisher versioned files, with 488 lexical representation differences (483 normalization-only, 5 low-order isotope precision), and **0 remaining mismatches at original printed precision**. It does NOT settle statistical independence of two feature errors. The P3 penguin morphology variables were measured during the **same field study**, while their species labels were not independently adjudicated from external observers.

P7 evaluates actually distinct physical sensor sites against a different *measurement modality* of activity, with genuinely held-out participants. The best available Clemson public source has video annotations that are NOT independently re-reviewed; furthermore the original paper reports human annotation of step times onto accelerometer waveforms using video observation. Therefore one cannot claim sensor/label error independence merely because there are multiple physical instruments.

Original project: https://cecas.clemson.edu/~ahoover/pedometer/ ; 2017 primary DOI https://doi.org/10.1109/BIBM.2017.8217769 ; Mattfeld, Jesch & Hoover (2021) https://doi.org/10.3390/s21134260 . Published sensor+annotation `Data.zip`, exact provider SHA256 `ce37832d5e234f6f014193a3a2af2f3162ab90905f303d473849512d690885da` (31,661,301 bytes). Already independently archived and TLS-verification repaired in **P5**: [whole original video-annotation text and tri-site sensor package](https://drive.google.com/file/d/1LxGvtntLgzv9UdpAdyc5eYHerbsClBCm/view). This P7 audit references those **same actual source bytes**, not any third-party interpreted or gap-filled prepared replacement.

## B. Source-aligned rows, label definition and reference authority

Original `Data.zip`: 30 participants × 3 gait regimes (Regular/SemiRegular/Irregular), exactly 90 trials, each a 9-column 15 Hz synchronized tri-axial accelerometer stream (wrist xyz, hip xyz, ankle xyz) plus separate publisher video-derived annotation `steps.txt`. The source archives contain 56,668 ordinary left/right step entries plus 4,133 separately typed leftshift/rightshift = **60,801 video annotation entries**. **Two shift indices lie beyond associated sensor lengths** (P010/Regular 9233 vs 9192 rows; P019/Irregular 10092 vs 9968 rows): flagged, not silently corrected. Both out-of-bounds labels are shifts, not ordinary steps. The historical 2017/2018 paper states 60,853 steps, different from this published ZIP; cause has not been established.

Primary endpoint deliberately counts **only left/right ordinary steps**. A separately recorded shift can be an FP under that operational event definition even if physically real; the event definition cannot be suppressed. Secondary endpoint includes shifts. No raw-video independent reviewer, sensor-clock independent timestamp audit or latent physical truth was acquired.

## C. Executable training and heldout decision contract

- **Training participants:** P001–P015, all 3 regimes (45 trials). **Held-out evaluation:** P016–P030, all 3 regimes (45 trials), **28,697 video-labelled ordinary step events**. Participant IDs do not cross splits. The split is deterministic not randomized and the broad analysis is retrospective after public knowledge of the source; do not call it a blind preregistered validation.
- For each site independently compute 3-axis magnitude, centered 13-sample local mean, absolute residual, within-trial median and median absolute deviation (MAD). Peak candidates must be local maxima above `median + t*MAD`, with amplitude-ranked nonmaximal suppression at spacing `d`.
- Search **only training-person event labels** over fixed `t ∈ {1.5,2.5,3.5,5.0}`, `d ∈ {4,6,8}`, minimizing `FP + FN` with video event matching ±3 frames. Retrospectively selected parameters: wrist `t=1.5,d=8`; hip `t=1.5,d=6`; ankle `t=2.5,d=6`. No heldout participant labels determine these parameters.
- Evaluate independently deployable **single-site** candidate peaks and deterministic **union** (merge nearby candidate positions within 3 source samples, bounded cluster span) or **intersection** (wrist and hip peaks within 3 frames). No test video labels enter the fusion algorithm.
- One-to-one chronological video↔sensor event matching within **±3 frames = ±0.2 seconds**. Reports TP, FP, FN, precision, recall and primary **event-count error cost `(FP+FN)/#video annotated steps`**. It may exceed one and is explicitly **NOT** a bounded [0,1] Bayes risk, calibrated probability or population decision risk. Multi-trial subject/time dependencies are preserved in reporting.

## D. Actual heldout event-loss results

| Sensor/policy | True positives | Missed annotated steps FN | Unmatched peaks FP | Recall | Event-count loss `(FN+FP)/28,697` |
| --- | ---: | ---: | ---: | ---: | ---: |
| Hip only | 19,900 | 8,797 | 15,901 | 69.35% | **0.86065** |
| Wrist only | 15,870 | 12,827 | 13,287 | 55.30% | **0.90999** |
| Ankle only | 14,059 | 14,638 | 11,924 | 48.99% | **0.92560** |
| Wrist+hip coincidence | 11,451 | 17,246 | 6,846 | 39.90% | **0.83953** |
| Any of three sites, peak union | 24,423 | 4,274 | 28,614 | 85.11% | **1.14604** |

**The signs are scientifically instructive, NOT a new method claim:** 3-device OR drastically increases empirical recall but can raise false alarms enough to worsen the selected total cost; 2-device AND has far fewer false positives but misses many video-labelled events. The wrist–hip consensus's apparent 0.0211-event-per-step improvement relative to hip alone is **small and uncertain**: a descriptive 2,000-resample participant-cluster delta percentile interval spans **−0.07276 to +0.03151**, and participants vary (8/15 improve, 7/15 worsen). It is NOT a confirmed population risk reduction.

**Regime heterogeneity at the same fixed thresholds and event definition** (cost `(FN+FP)/#video-labelled steps`):
- **Regular** (15,738 video steps): hip **0.456**, 3-device OR **0.377**, wrist–hip AND **0.705**.
- **SemiRegular** (10,308): hip **0.418**, 3-device OR **0.557**, wrist–hip AND **0.608**.
- **Irregular** (2,651): hip **4.984**, 3-device OR **8.003**, wrist–hip AND **2.538**.

The three policies' ranking reverses across activity regimes. This is a **real source-conditioned protocol/target heterogeneity witness**, *not* evidence that one gait class is biologically inferior or an identified causal transfer effect; FP-heavy denominators make costs much larger than one in irregular conditions. The regimes are intentionally different tasks, so unconditional global risk ranking is unsupported.

**Sensitivity:** re-evaluate the *same already selected detectors* at ±2, ±3, ±4 frames. Hip vs wrist–hip consensus losses:
- ±2: hip **1.212** vs consensus **0.997**
- ±3: hip **0.861** vs consensus **0.840**
- ±4: hip **0.718** vs consensus **0.774**

Thus an increase in tolerated event-timing discrepancy reverses the apparent ranking. Counting `leftshift/rightshift` events as positives rather than treating them as distinct gives yet another meaning of loss. Never promote the ±3 convention into event ontology.

## E. Empirical paired detection overlap really refines a *finite operational* set

On **video-labelled ordinary step events on the heldout 45 trials**, matching individual detections in two physical site streams to the same video-step index yields real 2×2 tables, rather than assuming unpaired marginal counts imply a joint distribution.

For wrist/hip: (n=28,697) video-labelled steps, wrist detects **15,870**, hip detects **19,900**, **both detect 11,411**, in this **particular video/±3-frame/matching contract**. If all we knew were separate per-trial detection margins, Fréchet allows **7,117 ≤ BOTH ≤ 15,701** (sum of each of the 45 trial-specific sharp finite integer bounds). The actual source-matched video step identity selects **11,411**. This *does* point-identify the **empirical finite-source overlap count conditional on publisher annotation and specified algorithm**, not a latent true-step parameter or independent Bernoulli detection probabilities.

Other two-site overlaps (actual / trial-stratified Fréchet lower–upper):
- wrist/ankle: **8,308 / [3,175, 13,200]**
- hip/ankle: **10,615 / [5,917, 13,900]**

**Do not confuse an oracle with a deployable device:** video-informed union of wrist/hip *matched step-sets* detects 15,870 + 19,900 − 11,411 = **24,359** video-annotated events; the **sensor-only fused timing-peak algorithm** actually matches **23,127**, because peak merging and matching are different operations. The former requires a reference label to define matching and is **not an operational detector performance claim**.

Even empirical marginal `P(D_w=1 | V=1)` and `P(D_h=1 | V=1)` do NOT show errors are conditionally independent given **true latent gait events**. Since the paper notes video-assisted annotation onto accelerometer traces, even `V` and `D` are potentially dependent through timestamp procedures. The videos were NOT independently re-annotated, and the 2017 stated aggregate differs from the currently downloaded dataset. No general statistical independence theorem was empirically proved.

## F. Source-interpretation firewall, code and receipts

1. **Confirmed bounded:** physically distinct wrist/hip/ankle accelerometer channels in the same publisher-synchronized record; actual publisher video annotation file; 45+45 participant-separated trial gate; heldout source-specific TP/FN/FP and regime-specific protocol losses; event overlap conditional on video labels; negative sensitivity by tolerance and shift ontology.
2. **Requires independent confirmation (HOLD):** manual video reannotation by distinct observers, independent clock-level sensor synchronization, truth of all unannotated events, external participant representativeness, true channel noise independence, any `θ`-indexed observation kernel, MQR-4.99 actual biological abundance/availability, Blackwell order or causal risk transport.
3. **Prior art:** sensor fusion, video-based pedometer annotation, timing peak detectors, and sharp Fréchet bounds existed before MQR; new value here is a transparent applied audit/scope discipline, not an original identification theorem.
4. **Reproducibility:** exact SHA-pinned original Clemson data persisted as **P5** [Drive original](https://drive.google.com/file/d/1LxGvtntLgzv9UdpAdyc5eYHerbsClBCm/view). P7 separate [Drive analysis and replay bundle](https://drive.google.com/file/d/15izchjtNlJ8RrWscpaLHxNqS6f01-oVZ/view), SHA256 `660a33b22f1d20d8a31d594c0cc8674cd33eb97d64bddfd1ac879d55aacee9de`. Contents: source-hash notebook, full Python script, independent Rust **source-table/bounds auditor (not a second peak detector)**, all 135 trial-wise Fréchet bound rows, all heldout per-trial method-score rows and JSON full receipt. It includes a reference **pointer** to original unmodified P5 input rather than duplicating 31MB bytes.
5. **CI acceptance gate:** `experiments/mqr-4.100/p7_video_reference_court.py`, `experiments/mqr-4.100/src/bin/p7_source_reference.rs`, `.github/workflows/mqr-4.100-p7-decision-risk.yml`. Reacquire original source from publisher with certificate intermediate chain verified against default OS roots (same as successful P5), SHA256 check, pinned Python numpy version, participant-heldout exact replay and Rust independent 90-file/event schema and Fréchet checking. CI run must be checked before claiming external PASS. Nothing writes bot-authored commits.

## G. Independent execution outcome and retained failures

**GitHub Actions P7 #37910379547 — SUCCESS** on exact original implementation commit `14e0b9781727834246b1d7ed68a07f481afa705d`. The workflow:

1. Re-downloaded exact publisher `Data.zip` under full TLS hostname validation, reconstructing the missing public intermediate chain **after validating it against the runner's existing trust roots**; confirmed SHA-256 `ce37832d5e234f6f014193a3a2af2f3162ab90905f303d473849512d690885da`. No `--insecure`, new private credentials or custom untrusted root.
2. Executed Python 3.12/numpy 2.2.6 on the **actual published 90 records**, selecting 3 sensor thresholds only from participants P001–P015 and reproducing all expected heldout metrics on P016–P030. Verified exact total heldout 28,697 labelled steps, and no test-person label inclusion in threshold tuning.
3. The **separately implemented Rust source parser** read all nine original accelerometer values per sample and original source video-event files, independently checking the 90 trial shapes, 56,668 ordinary steps, 4,131 *valid-in-range* shift annotations and **two anomalous out-of-range shift annotations** (4,133 shift labels total). It checked 135 per-trial paired detection tables satisfy actual Fréchet count bounds and their recorded overlap totals, including wrist/hip 11,411. Rust does **not** independently reimplement the Python detector or manually reannotate video frames. Do not advertise this as two independent sensor estimators.
4. Attached a compact run artifact [`MQR4100-P7-Heldout-Video-Conditional-Step-Risk-Receipts`](https://github.com/WhoSia/MQR/actions/runs/37910379547) artifact ID `11606830311` containing full per-trial test tables, Python/Rust logs, and aggregate structured audit. GitHub Actions artifact digest `sha256:c35a9520201d7197e59585dd224c917372778dc41df73839ebd30f8cafb1c107`.
5. Independently re-downloaded the user Drive P7 archive [source-conditioned analysis code and receipts](https://drive.google.com/file/d/15izchjtNlJ8RrWscpaLHxNqS6f01-oVZ/view); ZIP outer SHA-256 `660a33b22f1d20d8a31d594c0cc8674cd33eb97d64bddfd1ac879d55aacee9de`, 48,405 bytes; all seven archive entries passed integrity verification and the embedded aggregate replay receipt matched P7 results. Exact 31MB primary sensor bytes are already retained and independently verified under P5, and are pointed to in the P7 package rather than duplicated.
6. Same-head MQR-4.100 **P1/P2/P3/P4 regression CI runs #37910379460 / #37910379530 / #37910379477 / #37910379507 all SUCCESS**, as verified after initial court drafting. The separate EDI-P6 CI #37908117703 previously SUCCESS on its own byte-pinned code commit; this court did not re-run a distinct P6 workflow because its path set was unchanged.

**P7 — CLOSED BOUNDED / VIDEO-ANNOTATION-CONDITIONAL SENSOR-ERROR + HELDOUT OPERATIONAL DECISION-LOSS PASS**. Matched operational event-overlap point-identified *only within the observed source/label contract*. **NO PASS:** true latent movement/step truth, independently verified annotation error, sensor independence, parameter-indexed model identification, novelty of existing Fréchet mathematics, or population risk transport. MQR-4.100 official title unchanged, MQR-4.100 as a whole OPEN.


## H. Prior-source next-gate: genuine separate expert reference readings (not yet acquired in P7)

A stronger **next-source candidate**, newly verified from the public provider's data description (not analyzed here), is PhysioNet's [QT Database v1.0.0](https://physionet.org/content/qtdb/1.0.0/), DOI https://doi.org/10.13026/C24K53, citing Laguna et al. (1997). It explicitly provides independent *file records for individual human experts* of the same ECG waveform boundaries: first-pass `.qt1` and `.qt2`, second-pass `.q1c` and `.q2c` (the second annotator only for 11 records), plus automated waveform delineations `.pu`, single-lead versions `.pu0`, `.pu1`. These are **real human annotator-specific files**, stronger adjudicator provenance than a single video-assisted sensor-signal annotation. However, both experts observe the same ECG trace; separate identity/files do NOT prove blinded review, independent error, consensus truth or clinical outcome validity. First check the official `ANNOTATORS` provenance and waveform annotations, then acquire checksum-indexed actual `.q1c/.q2c` originals; match selected beats, measure inter-reader disagreement and derive label-uncertainty rather than choose an arbitrary adjudicator as ground truth. **No P8 or new MQR official title is opened in this court.**
