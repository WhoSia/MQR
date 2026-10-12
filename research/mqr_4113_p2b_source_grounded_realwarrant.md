# MQR-4.113 P2-B — Published Agreement, RealWarrant and the Limit of Ontic Inference

**2026-10-12 KST. Verdict:** PUBLISHED SOURCE CONTACT + RUST AGREEMENT CALCULATION PASS_BOUNDED; individually paired raw readings, complete calibration genealogy, population transport, independently validated physical measurand equality and method novelty HOLD. MQR-4.113 OPEN, MQR-4.112 independently OPEN.

## Four actual user-owned original sources inspected and normalized

- [Le Cam & Yang (1990), Asymptotics in Statistics: Some Basic Concepts, first edition](https://drive.google.com/file/d/1mo3DcwGCDKg1lSbZT_6QDOKy5qbMSzVt/view) — original book prints whole-book DOI 10.1007/978-1-4684-0377-0. Its chapters 1–2 cover comparison of risks and experiments, deficiencies, distances, likelihood ratios and Blackwell representation. This **1990 first edition** is NOT the separate 2000 second edition (10.1007/978-1-4612-1166-2).
- [van Fraassen (2008), Scientific Representation: Paradoxes of Perspective](https://drive.google.com/file/d/1d03xQ2zj3yc5lQBvB0j0DvCq9pL6ADVi/view) — Part II chapters 4–7 distinguish instrumentation, coordination, physical correlate and information in measurement. Serious philosophical prior art, not a validation of a new MQR ontology.
- [Cox (2002), The Evaluation of Key Comparison Data](https://drive.google.com/file/d/1WXB6QuyfdoevCVNxtZQAGyyGihYZ1riu/view) — original pp.589–595: Procedure A uses uncertainty-weighted mean and statistical consistency checks; B can replace failed A with more robust reference choices. Condition 2 requires participant measurements to be independent; mutual dependence or drifting travelling standards fall outside the simple conditions. The key-comparison reference value is not a universal reference truth.
- [Bland & Altman (1986), Statistical Methods for Assessing Agreement Between Two Methods of Clinical Measurement](https://drive.google.com/file/d/1HyV_DwLEOoNSHWPah_NUHh9_NKHBxzEe/view) — original pp.307–310: Wright versus mini-Wright peak-flow meters, reported correlation 0.94, mean difference −2.1 L/min, standard deviation of differences 38.8 L/min. Original authors say their convenience sample **illustrates statistical method and is not instrument comparability evidence**. Individually paired raw readings were not reproduced into the executable fixture.

All four were moved from 00_INTAKE into canonical 11_BOOKS (two books) and 10_PAPERS (two articles). Drive ID and size were preserved and metadata read back; source-title normalization uses em dash between author/year and title, and ASCII hyphen within compound title. Unrelated intake CSVs and non-MQR PDFs were not touched.

## P2-B original-reported-data engineering

Source [native Rust typed packet and tests](../experiments/mqr-4.113/p2b_realwarrant_source_agreement.rs); [published summary fixture](../experiments/mqr-4.113/fixtures/p2b_bland_altman_1986.real); [read-only Actions #38198630871 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38198630871) at exact tested source HEAD 857b24dfaa3c17f883b92dd7e59c6f3dda84576d. Ten Rust tests PASS; no Python runtime and no automated commit. This is a new Rust REALWARRANT 0.44-P2-CANDIDATE auxiliary surface, **not** language promotion.

From published aggregate difference data, a conventional *nominal Gaussian model* gives −2.1 ± 1.96×38.8 = [−78.148, 73.948] L/min. The paper's ±2 SD rounding would give [−79.7,75.5] L/min. These values are **recalculated from reported summary**, not a reanalysis of source paired subjects, not a true physical range or valid population CI by fiat. Assumptions (distribution, sampling, stability, repeatability, legitimate clinical tolerance and common calibration sources) must be checked separately.

The parser represents (1) source/report metadata, (2) empirical-summary model, (3) declared physical quantity and apparatus operation, (4) external calibration ancestry and (5) the epistemic authority ceiling. Source DOI and Drive file ID are **pointers**, not proof of byte-identical or externally credible experiments. Rejected cases include missing source pointer, synthetic measurement disguised as published, nonfinite or malformed moments, duplicate fields and self-declared independent certification. Even r=1 cannot compel physical equivalence.

## Why Real Lang matters beyond a formal ontology

Epistemology: describe which observational data, decisions and assumptions support a *scoped scientific assertion* and which rivals remain indistinguishable. Blackwell experiment ordering measures relative stochastic information **conditional on the shared state model**; it is not a total order of justified natural-world claims.

Ontology: specify physical apparatus, actual sample, measurand, unit, reference standard, operation and intervention as **hypothesized real referents** distinct from label strings and probability kernels. True identity of those referents is determined by independent physical coordination, not by a well-typed declaration or hash pointer.

Practical engineering: build a compiler of *falsification obligations and missing witnesses* before implementing a verdict-giving ontology. An executable model that cannot distinguish an untested label from a verified physical anchor must output HOLD, not claim it proved a philosophical theorem. The user can improve the program with externally audited witness evidence rather than just increasing language versions.

Rival priority: Le Cam/Blackwell (statistical experimental equivalence), Cox/JCGM (metrological comparison and dependent standards), Bland–Altman (agreement vs correlation), van Fraassen/Tal/Chang (physical coordination and historical calibration) are **existing explanations**. MQR's real advance requires an independent discriminating physical observation; synthetic data and ontological vocabulary do not suffice.

**4.113 P2 scientific disposition:** bounded source-contact and software validation complete; empirically validated same-measurand operation, independently traced error and historical 4.112 full FER source remain HOLD. A P3 solely extending toy theory is not warranted; no P4 or later P-stage planned.

## MQR-4.114 exact-title proposal only — NOT OPENED

**MQR-4.114 — Intervention-Identified Measurands & Calibration-Ancestry Ambiguity: Physical Reference Perturbations, Correlated-Error Rival Models, Source-Indexed Cross-Instrument Validation & Typed Ontological Warrant**

Distinct future problem: whereas 4.113 tests how representations and stochastic comparisons affect measurement warrant, 4.114 would require a **prospectively specified physical perturbation** distinguishing shared calibration root, instrument-specific error, and true shared-measurand response using held-out source-grounded observations. Its formal opening needs user approval. MQR-4.112 remains an independent original-FER source-history problem.

## Drive-not-found bibliography candidates (search, not a universal absence proof)

1. Le Cam & Yang (2000), Asymptotics in Statistics: Some Basic Concepts, SECOND EDITION, whole-book DOI 10.1007/978-1-4612-1166-2; differs from held 1990 edition.
2. Bland & Altman (1999), Measuring Agreement in Method Comparison Studies, DOI 10.1177/096228029900800204 (also indexed as 10.1191/096228099673819272).
3. Bendix Carstensen (2010), Comparing Clinical Measurement Methods: A Practical Guide, whole-book DOI 10.1002/9780470683019.
4. Passing & Bablok (1983), A New Biometrical Procedure for Testing the Equality of Measurements from Two Different Analytical Methods. Application of Linear Regression Procedures for Method Comparison Studies in Clinical Chemistry, Part I, DOI 10.1515/cclm.1983.21.11.709.

No unverified PDF download link or chapter DOI is substituted for an original book DOI; actual PDFs for these recommendations were not ingested.
