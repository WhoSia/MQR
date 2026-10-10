# MQR-4.110 — Provenance-Sensitive Calibration Transport & Historical Measurement Warrant: Model-Relative Information Preservation, Cross-Standard Comparability, Source-Graph Reconstruction and Independent Rival Falsification

> **P3 SOURCE PAGINATION ERRATUM (2026-10-10):** In earlier 4.107–4.110 entries, the graphical-construction prose and four-glass 250 °C comparison table were incorrectly called *printed pp.240–241*. Actual SHA-pinned original images establish **DjVu index 274 = printed p.238 (prose)** and **DjVu index 275 = printed p.239 (table)**. The published numeric values and 2.95 °C range remain correct. This authoritative source-image finding supersedes all such earlier page-number references, without claiming page-content digitization of curve points.

**Officially opened 2026-10-10.** Main-only, no Actions. OPEN / NEW PHILOSOPHICAL DISTINCTNESS HOLD.

## Changed intervention and actual new primary-source acquisition

Unlike P2 of 4.109 (repeat analysis of the published p241 numeric table), first-party source bytes were actually recovered from the user's Drive original `Regnault (1847) — ... — ORIGINAL SCAN.djvu` (Drive file ID `1yvgpg_U6giXU-zzag7FFctTzQKhnMbLT`). Local file length: **15,049,344 bytes**. SHA-256 computed directly on downloaded bytes: **`00f9dc99fea5af6944c4f19624d945d89ea54a379bf660cb604fc77ba717efed`**. Header begins with `AT&TFORM` + `DJVM`, a DjVu multi-page container. A binary scan finds **824 `FORM....DJVU` page-form signatures** and one `DJVM` root-form signature, consistent with the public Wikisource volume having 824 indexed pages. **This is a bounded structural check, not a full semantic verification**: the current local image tools (PyMuPDF, ImageMagick, ffmpeg) did not decode DjVu; no scan pages including p181, p240, p241 or Plate VIII have been rasterized from *this exact local byte copy*. DjVu renderer/delegate unavailable.

Old converted PDF 361 MiB remains a separate original-preserving derived artifact, Drive ID `1oMK9-9K_f4SIxLkOtZpTzW2Dxhr_6OAe`; raw fetch over 256 MiB blocked. Never replace original DjVu with it.

## P1 research question

For *the same declared measurand and decision target*, is there any historically grounded situation in which transformation `R → G(R) → S(G(R))` conserves a Fisher–Neyman/Blackwell-sufficient numerical statistic yet fails to transmit warranted calibration/reference claims, in a way not already explained by JCGM VIM result-specific traceability, GUM uncertainty covariance, Tal model-mediated coherence, Chang epistemic iteration, or ordinary source criticism?

## Provenance and rival protocol

Regnault 1847 printed p240 reports p241 table derived from experimental readings by Plate VIII graphical constructions. The actual original p181 image read in earlier 4.107 yielded A′ pressure 785.21 vs Chang 2004 secondary Table 2.5 782.21, cause unknown. Printed p241 (air 250°C) reports mercury indicated 253.00/250.05/251.85/251.44 for four glass types, a 2.95°C spread. These are graph-derived published readings; cannot claim individual rows are direct observations.

1. **Fisher–Neyman:** specify `P_θ(R)` and likelihood factorization before claiming sufficiency for historical readings.
2. **Blackwell:** require comparable `θ`-indexed kernels for a *shared measurand*; a chart/table and one thermometry row are not those kernels.
3. **VIM §2.41–2.42:** certified traceability of individual results requires documented reference chain and uncertainty, cannot be inferred from graph convergence.
4. **GUM §§5.2.4–5.2.5:** model glass- and reference-dependent shared correction/covariances; historical uncertainties not yet present.
5. **Tal (2017), §5.4:** reference standards and coherence tests remain theory-laden; simple independently originated instruments do not settle accuracy.
6. **Chang (2004), chs 2,5:** historical Regnault comparisons and epistemic iteration already examined.

### First falsification gates
- BYTE_SOURCE: PASS_BOUNDED (actual 15MB primary DjVu downloaded, SHA and coarse container signatures checked).
- DJVU_PAGE_COUNT: **824 CANDIDATE FROM FORM SIGNATURES**, formal directory/page order and render check not yet performed.
- P181_P240_P241_PLATEVIII_IMAGE_FROM_LOCAL_BYTES: HOLD due missing decoding.
- HISTORICAL_RAW_OBSERVATION_POINTS, FIT ALGORITHM and uncertainty budgets: HOLD.
- SAME-TARGET NOVEL MQR VERDICT: HOLD, absent direct rival divergence; do not promote a numerical result or document handling to philosophical novelty.

## Next source experiment

Decode DjVu with a verified compatible tool without modifying primary bytes; obtain page index 215 (printed p181), 274–275 (printed p240–241), 820 (Plate VIII), compare byte-linked rendered crops to the online originals, and distinguish printing/text transcription from original experimental raw records. Test whether plate permits recovery of interpolation method and classification of raw experiment points; no artificial interpolated values. Audit original Regnault independent apparatus measurements and glass-specific calibration reference descriptions before promoting an historical measurement-warrant theorem.

Related court: [4.109](mqr_4109_provenance_sensitive_sufficiency.md). Main README should stay compact, no bloated historical paragraphs.

## P2 — Source image and Rust-first maintenance court

Actual original DjVu is present locally and its 15,049,344-byte SHA-256 remains `00f9dc99fea5af6944c4f19624d945d89ea54a379bf660cb604fc77ba717efed`. Local command checks found no `ddjvu`, `djvused`, `djvutxt`, or DjVu decoding delegate; attempts to provision a decoder in this execution environment did not complete. Therefore **NO page image was extracted from this exact DjVu** at P2, and p181 / p240 / p241 / Plate VIII original-page image comparison must remain HOLD. Previously confirmed public online scans must not be passed off as freshly rasterized local primary-source pages. Container signature `DJVU` count (824) is structural, not full semantic validation. The inferential status of the original raw experimental observation dots on Plate VIII remains unknown. P2 adds zero new original graph measurements.

Rust-first implementation: [`experiments/mqr-4.110/src/main.rs`](../experiments/mqr-4.110/src/main.rs) and dependency-free [Cargo.toml](../experiments/mqr-4.110/Cargo.toml) replicate the **published, graph-derived** p241 T=250°C four-glass table with integers of hundredths of a degree (253.00, 250.05, 251.85, 251.44), proving only max numerical spread 2.95°C and never claiming modern traceability. This moves canonical new arithmetic from Python to Rust. Narrow workflow [mqr-4.110-regnault-rust.yml](../.github/workflows/mqr-4.110-regnault-rust.yml) was committed once (commit `fb4bad7c56c35b7822b5fff0753aaf921482951e`) after two implementation commits, instead of dispatching repeated CI runs. **CI outcome has not been independently verified**: do not label GitHub Actions SUCCESS merely because workflow file exists; likewise local Cargo tests were not run because Rust binaries are absent in the local environment.

Retired one obsolete one-off script only: historical [`experiments/mqr_4109/p2_regnault_same_target_court.py`](https://github.com/WhoSia/MQR/blob/57ba26aed5b26f6e39b6da1959b3fb8feb8474c2/experiments/mqr_4109/p2_regnault_same_target_court.py) with blob `7bbce363725b0d25a95a66e9c0aff2ab647e15e7` was archived to [Drive Markdown](https://drive.google.com/file/d/199mFVqJAn19rvRBVySGlNTTLp1LRrIJf/view) in 90_README_HISTORY — MQR and downloaded archive was checked to contain source normalized for whitespace. **Exact byte reconstruction is available from pinned Git blob, not the reflowed Docs-export archive**. After archiving and updating the 4.109 research ledger, deleted obsolete GitHub path on main at commit `98d457d8afe7d895bc0650e75492c48cb6127d89`. This has not undergone exhaustive reverse workflow dependency audit; only a scoped successor exists, so further deletions are blocked until an actual dependency inventory and archived backups are verified.

Scientific competitor adjudication unchanged: existing Fisher–Neyman, Blackwell, JCGM VIM/GUM, Tal and Chang explain numerical comparison versus warranted calibration, and 4.110 has not identified a separate same-measurand novel judgment. **Novelty HOLD, page raster HOLD, executable CI status pending independent confirmation.**

## P3 — SOURCE-NATIVE SIX-PAGE IMAGE COURT and retirement CI (2026-10-10)

### Direct byte-attested facsimile: decisive new evidence
The original 15,049,344-byte DjVu file fetched earlier from Drive has SHA-256 `00f9dc99fea5af6944c4f19624d945d89ea54a379bf660cb604fc77ba717efed`. On an isolated GitHub Actions Ubuntu runner we downloaded the Wikimedia public original, **verified it had the exact same SHA-256**, installed DjVuLibre, and verified `djvused -e n == 824`. We then decoded original DjVu indices **215, 266, 274, 275, 356, 820** with `ddjvu` and generated PNGs. GitHub Actions [#38033207087 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38033207087), workflow `.github/workflows/mqr-4.110-djvu-native-render.yml`. First attempt [#38033148770 FAILED](https://github.com/WhoSia/MQR/actions/runs/38033148770) due to erroneous `ddjvu -help` exit-code assertion AFTER apt successfully installed the tools; fixed by `command -v ddjvu` and reran success. Do not hide the failed attempt.

Native six-page rendered ZIP SHA-256 `8594ae3615c83d479d0a1b421052860751d7dcacf0d5d07c636249df7bddd728`; GitHub artifact ID **11662747642**. Its actual bytes were uploaded to Drive [RENDER DERIVATIVE ZIP](https://drive.google.com/file/d/1wz3A8v6HtEna4TBYFB_aWH6bkinz7Ilj/view) in 11_SOURCES and downloaded again; ZIP byte identity and ZIP CRC/integrity successfully checked. The original DjVu and the separate large PDF are **unchanged**.

### Verified page images — source image, NOT web transcript
| Original DjVu index | Visible printed page | Established content |
|--:|--:|---|
| 215 | **181** | Air-thermometer comparison A/A′: A′ H0 at 95.57 °C visibly **785.21 mmHg**, whereas Chang 2004 Table 2.5 gives **782.21**; cause remains unknown. |
| 266 | **230** | Four individual experimental columns: mercury T values **363.39, 361.54, 363.33, 363.09** °C; corresponding air x **358.46, 357.48, 359.27, 358.68** °C; differences **4.93, 4.06, 4.06, 4.41** °C. These are reported experiment-level records, not sampled rows from the graph-derived 10-degree summary. |
| 274 | **238**, *not* 240 | Regnault explicitly states comparative table derived from carefully made graphic constructions on immediate observations, located on Plate VIII. Abscissa difference: 10 °C air thermometer per horizontal division; ordinate: mercury-air difference (t−T), 1 °C per vertical division. Mentions the 100 °C fixed point and possible sub-100 differences which are difficult to resolve accurately. |
| 275 | **239**, *not* 241 | Printed four-glass synthetic-free reported 10-degree table. At air T=250 °C: Choisy crystal **253.00**, ordinary glass #5 **250.05**, green glass #10 **251.85**, Swedish glass #11 **251.44** °C. The previously reported 2.95 °C spread remains numerically correct. |
| 356 | **320** | Regnault describes mechanically marking small crosses for measured coordinates on copper plate himself and constructing Plate VIII mercury-expansion curve. Its described abscissa uses air-thermometer degrees and ordinate is *absolute mercury expansion*, an **additional quantity distinct from the p.238 prose's mercury-minus-air difference**. Distinguish curves/axes before matching dots with summary table. |
| 820 | **Plate VIII engraving** | Landscape multi-curve plotted plate with graph paper, lines and fine marks. Native image rendered **3766×1951 px**; curves visible but individual crosses and axis labels not safely readable/assigned to unique numerical observations without validated registration and contrast/coordinate calibration. **Do not digitize unsupported curves or claim reconstructed experimental data.** |

### Same-target rival re-evaluation
P.230 reports the four separate high-temperature experimental columns at slightly **different** air thermometry x values, so they must NOT be treated as four simultaneous observations at one identical state (nor as repeat measurements with known uncertainty). P.239 holds a grid-normalized, graph-constructed cross-material comparison. P.320 identifies hand-placed measured crosses yet uses an *absolute mercury-expansion* ordinate; p.238 describes *mercury-air temperature difference*. Their reference to the same Plate VIII is not a license to identify two distinct ordinate quantities or reverse-engineer an interpolating function without reading actual panel/axis attribution. This is concrete, source-image-grounded provenance segmentation, but fully compatible with Chang's temperature-scale historiography and Tal's calibration models, plus GUM/VIM requirements. Fisher–Neyman/Blackwell require statistical kernels not supplied by these observations. **NEW HISTORICAL SOURCE IMAGE PASS_BOUNDED; NOVEL SAME-TARGET THEORY STILL HOLD.**

### Development CI and retirement custody
- Original dependency-free Rust arithmetic [Actions #38031726173 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38031726173): unit tests 2 passed, exact execution output marker and log artifact verified.
- Read-only Rust [retirement-audit code](../tools/mqr-retirement-audit.rs): scanned **1234 tracked files, 791 text source files** across active tree; original 7 scoped 4.107–4.109 Python candidates all had **zero direct operational/workflow references**, with document links on some. GitHub Actions [#38032842985 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38032842985), tests 2 passed, report audited. Follow-up [#38033014840 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38033014840) after explicit archive-state guard change. This is **static source-ref scanning only**, not proof of absence of dynamic execution or all semantic research uses. No auto-delete.
- One low-reference, historical *synthetic* Python coefficient-identifiability toy `experiments/mqr_4107/calibration_model_misspecification.py` (original blob SHA `46b9819a3af6f251cde5902d4af197de74783b4f`) was preserved on Drive [retired source Markdown](https://drive.google.com/file/d/1Q5EGGj74dLfxxC3sOj2yE3Ni2_Z9ydjd/view) under **MQR — Git Branch & Retired Code Archives**, re-downloaded and verified that whitespace-normalized original source and blob ID appear; Git preserves byte-exact original. File was then **deleted from main** at commit `2ef84267161df4c03e56200a6b3fded6c3ec71df`. Rust auditor now recognizes archived absence. Other six candidates remain in Git and receive no blanket deletion clearance.

### Status update
DJVU_ORIGINAL_SHA_MATCH PASS; DIR_PAGE_COUNT PASS 824; PAGE_215_266_274_275_356_820 RENDER_PASS; PDF_DERIVATIVE_PAGE_COMPLETENESS still HOLD (no 361MB PDF audit); DIRECT_RECORD_VS_GRAPH_TABLE_CLASSIFICATION PASS for the quoted source distinction; INDIVIDUAL_PLATE_CROSS_COORDINATE_RECONSTRUCTION HOLD; HISTORICAL_MEASUREMENT_UNCERTAINTY_CERTIFICATION HOLD; MQR_ORIGINAL_SAME_TARGET_VERDICT HOLD. GitHub Actions used in a deliberately scoped manner (including repair), no new heavyweight generalized CI.


## P4 — Direction tournament: irreversible histories versus static traceability (2026-10-10)

**Scientific status: MQR-4.110 remains OPEN / DISTINCTNESS HOLD.** This P4 is a Research-OS return-to-origin / direction-selection audit, not an experimental validation or the opening of MQR-4.111. No new physical observations, plate coordinates, or independent metrological certificates were produced.

### Compression of the live 4.110 debts

1. **Historical source recovery:** Regnault (1847) original DjVu source SHA-256 \`00f9dc99fea5af6944c4f19624d945d89ea54a379bf660cb604fc77ba717efed\`, 824 pages, six native-rendered images PASS as P3; printed p.238 is the graph-construction description, printed p.239 the four-glass normalized table; printed p.230 contains separate individual experimental columns at nonidentical reference temperatures. Plate VIII individual points/interpolation and historical covariance remain HOLD.
2. **Fixed-experiment statistical sufficiency vs metrological warrant:** a declared experiment kernel and fixed target are necessary for invoking Fisher–Neyman/Blackwell. Source graphs, calibration-chain uncertainties and historical quantity individuation are already handled substantially by VIM/GUM, Tal (2017, 2019), Chang (2004). No distinct MQR judgment demonstrated.
3. **Return to the physical world:** what can be known about the original specimen's state when observation or reference intervention itself changes the specimen and return to the old physical state cannot be independently established?

### Four-way research-direction tournament

| Candidate | Potential contribution | Strongest defeating objection | P4 disposition |
|---|---|---|---|
| A. More Plate VIII digitization | Better source scholarship and raw/derived distinctions | Marginal same-target theoretical discrimination; cannot infer experimental origin of unlabeled crosses by drawing a better curve | Archive as **bounded historical work**, do not block mainline |
| B. Another provenance/traceability abstraction | Formal bookkeeping and calibrational consistency | VIM/GUM/Tal/Chang and existing 4.107–4.110 already explain the target; risks recursive refinement | **ABSORB / no new mainline version** |
| C. Dynamic observation quotient | Makes future interventions explicit | Control-theoretic observability, behavioral equivalence, epsilon-transducers and causal abstraction already cover the theorem; MQR-4.106 already developed measurement-action state transitions | **NON-NOVEL formal fixture**, no novelty PASS |
| D. Irreversible physical return and historically unrecoverable pre-intervention state | Changes the explanandum to original-state retrodiction under state-altering evidence acquisition; forces new source- and experiment-level discriminators | Potential outcomes, experimental design, latent-state identification and model-based measurement may fully reduce it | **WINNER AS RESEARCH QUESTION ONLY**; novelty and experimental evidence HOLD |

### Exact miniature: present-output equivalence does not imply active-state equivalence

Let \(S=\{0,1\}^2\), \(s=(q,m)\), \(O(q,m)=m\), and a hypothetical intervention \(C\) act as \(F_C(q,m)=(q,q)\). States \(a=(0,0)\), \(b=(1,0)\) satisfy \(O(a)=O(b)=0\), but \(O(F_C(a))=0\) and \(O(F_C(b))=1\). In this fully specified four-state synthetic system, the observation-only partition has two classes (by \(m\)); the partition induced by observing before and after \(C\) has four (by \((m,q)\)). The intervention modifies the system; the toy is not evidence about Regnault's actual glass.

In a deterministic total transition system with unconstrained finite input words, define \(s\equiv_U t\) iff all admissible output histories under every word in \(U^*\) coincide. It is the greatest transition-invariant equivalence contained in \(\ker O\): right-invariance follows by prefixing an input; any transition-invariant relation inside \(\ker O\) implies equality of future outputs by induction. **This is standard behavioral/state-minimization mathematics, not a novel MQR theorem.** Importantly, destructiveness, protocol-dependent feasibility and partial transitions invalidate an unqualified use of \(U^*\); physical admissibility must be specified before quotient claims.

### Stronger destructive-retrodiction falsifier: two worlds, same observable law

Take a *single permitted irreversible probe* \(C\), non-informative pre-probe reading \(Y_0=0\), and post-probe \(Y_1\in\{0,1\}\).

- World A (**pre-existing susceptibility**): \(Q\sim\mathrm{Bernoulli}(1/2)\); the probe reveals it, \(Y_1=Q\).
- World B (**probe-created variation**): \(Q=0\) for every original specimen; the probe produces independent \(Z\sim\mathrm{Bernoulli}(1/2)\), \(Y_1=Z\).

Both worlds give exactly \(P(Y_0=0,Y_1=0)=P(Y_0=0,Y_1=1)=1/2\), including for arbitrarily many independent specimens exposed solely to the same probe. Yet \(P(Q=1)\) is \(1/2\) in A and \(0\) in B. Thus these observations cannot identify the original-state claim; an *independently justified pre-probe marker*, a discriminating intervention family, validated structural assumptions, or further source traces are needed. This is a synthetic identification counterexample already anticipated by causal inference and measurement theory—not a new universal impossibility theorem.

**Critical distinction:** discovering a post-probe difference does not by itself establish that the difference already existed before the probe. Conversely, randomized matched specimens can identify certain population-level intervention contrasts under design assumptions, but cannot recover a particular destroyed specimen's unobserved individual counterfactual.

### Primary-source rivalry and historical limits

- [Chang (2004), *Inventing Temperature*, user's full Drive original](https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view): ch.2 reports that same-glass samples with different thermal treatments followed different expansion laws, citing Regnault (1847) p.165. This is **Chang's historical report**, not direct inspection of Regnault p.165 in this P4; Regnault P3 images do not establish a within-specimen before/after treatment experiment.
- [Tal (2017), full original in Drive](https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view): calibration models and predictive coherence already address much more than fixed numeric correction.
- [Tal (2019), full original in Drive](https://drive.google.com/file/d/1dm4Oea-l6BVMEuZGTwe-OeUp05gYTzrA/view): discrimination between systematic measurement error and differing quantities has fundamental underdetermination; MQR may not award itself ontology solely from a state-quoitent.
- [Barnett & Crutchfield (2015), full original in Drive](https://drive.google.com/file/d/1enuIYvv7dF4B1r59nCcGQmdO8mthCCwO/view): minimal predictive states for input-output stochastic processes.
- [Geiger et al. (2025), full original JMLR in Drive](https://drive.google.com/file/d/1dkkczKfLgmHL8YPwKWrKunEdCbAel6hK/view): intervention-preserving causal abstraction.
- Nelson W. Taylor (1944), *Aging Thermometers*, DOI 10.1111/j.1151-2916.1944.tb09124.x: only publisher abstract inspected in this P4; **Drive 미확보(색인 검색 기준); 직접 PDF 미확인**. Treat as an experiment-design lead, not primary full-text support.

### Non-ceremonial RAVEL verdict and physical discriminators

1. **Internal ancestral attack:** MQR-4.106 already represents a measurement as (readout, state transition) and gives order-sensitive back-action examples. Do not rebrand that result as 4.111.
2. **External mathematical attack:** dynamic quotients and intervention models are existing theories; finite synthetic PASS adds no originality. Reject a new universal theorem based on the four-state example.
3. **Historical attack:** Regnault pp.230/238/239 and Plate VIII are not a sample-indexed longitudinal history; no retrospective claim about a given specimen's exact pre-treatment glass state.
4. **Prospective scientific experiment specification:** using institutionally supervised, already calibrated apparatus, compare matched sample cohorts with a predeclared intervention versus sham, independent reference checks before/after, source-registered specimens, and a prospective recovery check. Test whether an independently validated pre-intervention feature predicts post-intervention shift beyond what a probe-created-change model predicts. No experiment conducted or physical effect measured in P4.
5. **Decision gate:** if standard causal experimental-design/observability theories already explain every legitimate prediction, retire MQR-specific novelty and retain only the physical application; if an explicit shared-target rival-divergent prediction survives and new source evidence supports it, return for a stronger 4.111 stage.

### Proposed only — MQR-4.111, NOT OPENED

**MQR-4.111 — When Measurement Changes the World It Tests: Irreversible Experimental Histories, Pre-Intervention State Identifiability, Reset Witnesses & the Limits of Scientific Retrodiction**

The primitive target is **the scientifically defensible reconstruction of an original physical state from evidence produced by interventions that may make that state unrecoverable**, separating instrument response, probe-created change, source-selected histories and the conditions under which an actual return/reset claim can be established.

**P4 conclusion:** Direction D wins as an *ambitious falsifiable question*; 4.110 stays **OPEN / DISTINCTNESS HOLD**. No new executable experiment, data collection, automatic code retirement, 4.111 creation or new CI workflow is implied by this document.
