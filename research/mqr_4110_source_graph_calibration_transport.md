# MQR-4.110 — Provenance-Sensitive Calibration Transport & Historical Measurement Warrant: Model-Relative Information Preservation, Cross-Standard Comparability, Source-Graph Reconstruction and Independent Rival Falsification

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
