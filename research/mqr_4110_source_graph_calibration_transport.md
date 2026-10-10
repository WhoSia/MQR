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
