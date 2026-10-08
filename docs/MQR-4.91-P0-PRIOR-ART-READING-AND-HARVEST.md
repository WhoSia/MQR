# MQR-4.91 P0 — Direct Prior-Art Reading and Cross-Lab Harvest (2026-10-08)

Status: READ-AND-RECONCILE PASS, empirical innovation not yet admitted. Source is **six full PDFs located by exact Drive IDs and opened as original readable content**, not search-snippet paraphrases. All findings conditioned on the original paper population/design and cannot silently generalize.

## A. Source-by-source substantive audit

### Phillips et al. (2009) — Sample selection bias and presence-only distribution models
- Drive ID `1yzmwXwRWdQ7x7v53DPT1Lx3k5MaQa8vc`. DOI `10.1890/07-2153.1`.
- Paper distinguishes observation/selection processes from background data and investigates target-group / biased sample selection for presence-only SDMs. The background/reference point design impacts model evaluation and fitting; neither pooled AUC nor a change after correcting sampling is an invariant biological estimand.
- **Court:** Any claim that choosing background affects AUC is established prior art. Repair compiler must represent (i) source positive sampling process, (ii) training background, (iii) scoring/evaluation negative reference **as distinct objects**, even when grids numerically overlap.
- **Harvest MQR→RITHM:** Administrative-record capture mechanism is not an innocuous denominator; distinguish observed-case enumeration from latent eligible population. This is a methodological analogy only, not empirical evidence about CMS.

### VanDerWal et al. (2009) — Selecting pseudo-absence data...
- Drive ID `18FdcivZtYA0m2uGtgaP8EGCf4dJ1B5-7`. DOI `10.1016/j.ecolmodel.2008.11.010`.
- Directly read Methods: compares **flexible area AUC**, which varies the pseudoabsence background with fitted model background extent, and **fixed area AUC** on about **36,000 one-kilometer grid cells across AWT** with the same reference pseudoabsences for all model fits, to mitigate statistics changing simply because the reference background changed.
- **Strongest novelty falsifier:** fixed-reference normalization already materialized experimentally in 2009. MQR P8's constructed Q union is source-audited sensitivity, not a new normalization procedure.
- **P1 test:** require fixed target positive/negative **AND** fitted predictor version, site mask, feature transform, and selection policy. AUC on common Q alone leaves fold/full, training policy and leakage unresolved.
- **Harvest MQR→C3X:** A shared benchmark position list is the analog of fixed AUC negative reference; paired engine score comparisons still demand identical rules, search budget, context state and source root (analogy, no chess evidence transferred).

### Baker, Maclean & Gaston (2024) — Correcting spatial sampling bias without independent data
- Drive ID `1JcNqdEo4BIYTsucG4vtlhfYNhz9V3SvD`. DOI `10.1111/ddi.13802`.
- Results §3.1 reports **10 original independently tested studies / 13 standardised effect estimates**, pooled mean standardised effect *0.35* with interval *(-0.66, 1.57)*; effect 95% CIs across methods overlap zero. The manuscript itself describes this as **weak support**, not decisive general correction benefit.
- Experimental simulation asks whether internal/spatial CV can identify best corrections in absence of independent data, documents discrepancies between internal CV and independent outcomes. Do not count corrections/estimates as independent biological studies.
- **Harvest MQR→EvoNOMOS:** within-system self-check accuracy is not independently observed downstream correctness; choice of method under shared feedback/data depends on the selection policy. Only use as research design analogy, not empirically generalize ecological numbers to software changes.

### Serov, Koldasbayeva & Zaytsev (2026) — Kernel mean matching under spatial distribution shift
- Drive ID `1QTqBxt4aZHjbNsdgIKut5i81DLpIU8j-`. DOI `10.1038/s41598-026-36740-7`.
- Evaluates NW, density-ratio IW, KMM, classifier-based weighting for spatially structured source→target risk estimation. The paper's stated relative MAPE improvements of **12.3–86.5%** are paper-specific performance claims, not independent replicated measurements under MQR.
- Methods explicitly retain **only classification pairs with AUC-ROC >0.7** in one experimental construction. This is a *selection-conditioned* eligible sample; cannot advertise performance transport to all original examples or claim the threshold universally applies to all experiments in the paper.
- **Genuine methodological rival:** KMM directly optimizes feature-distribution agreement for risk estimation. An evaluation-contract certificate is not a substitute for better weighting; comparisons need matching evaluation targets and selection rules.
- **Harvest MQR→CUBE-REV:** published leaderboards conditional on qualifying screens cannot be naively transported to all attempts/candidates; preserve eligibility and censoring before interpreting conditional success. This is a design analogy; CUBE-REV has independent WCA DNF evidence.

### Bareinboim & Pearl (2013) — Meta-Transportability of Causal Effects: A Formal Approach
- Drive ID `12_XJxLm1fbqWJiKQUC6u2cOrkXijH5qP`. AISTATS, PMLR.
- Abstract and results provide **necessary/sufficient conditions and a complete algorithm** for identified transfer of *causal effects* from heterogeneous experimental sources into a target environment with observational information.
- **Doctrinal correction:** avoid claiming that MQR is inventing general cross-population data fusion or a complete transportability algorithm. Also do not wrongly apply causal-effect transport formula directly to rank-based performance measures, which require explicit score/label/negative-reference constructs and may lack the causal graph assumptions.
- **Harvest MQR→NOMOS:** transfer of authority-dependent attestations across contexts requires a named target and an admissible bridge; this is a conceptual design analogy only and not a demonstrated theory of institutional legitimacy.

### Calautti, Livshits, Pieris & Schneider (2024) — Below and Above Why-Provenance for Datalog Queries
- Drive ID `1vUjw6ua-LUe1c6hrFpEx6-sqFLpOnjPr`. DOI `10.1145/3695829`. Original paper explicitly distinguishes ordinary why-provenance, **subset-minimal** witnesses (whyminimal) and multiplicity-aware explanation.
- Their results show data-tractability for a restricted minimal notion and nontrivial complexity for more informative witnesses. In Theorem 3.6, why-multiplicity NR arbitrary Datalog is PSPACE-complete, with distinctions for linear Datalog and other explanation classes.
- **Critical logic distinction:** inclusion-minimal witness != minimum cardinality != least procurement cost != exhaustive search proof. MQR's current four source prerequisites are *candidate obligations*, not a globally minimal acquisition policy.
- **Harvest MQR→NOMOS/EvoNOMOS:** registrar/gate witness dependency can be recorded as a support graph, but don't call a list 'minimal' unless the finite derivation rules and exact minimality predicate are proven.

## B. Proposed P1 experiment and repair contract

Source problem from original Matsui ZIPs + official Maxent Java 3.4.4: original publisher external prediction raster width 191 vs direct whole-environment replay width 715; after coordinate-indexing, **10,057** author-scored cells not paired with valid reprojection scores. Read-only GitHub Actions 37745214684 and 37745501466 failed closed. These are not proof that original projection is fundamentally unrecoverable; they specify a source-missing transformation/mask condition.

Decompose next repair into competing causes (test each, never assert as established):
1. **Grid provenance:** original external output `.asc` may have been cropped or projected using a different raster extent/CRS/resampling mode than the supplied environment. Check `nrows,ncols,xllcorner,yllcorner,cellsize,nodata` for published output and each actual input climate raster; calculate overlap counts both geographic and scored-mask.
2. **Feature contract:** original model lambdas use selected BIO features and specific numeric normalization/clamping/output transform. Pin exact training Maxent version / lambda entries / projection flags and inspect actual logs.
3. **Mask and missingness:** test all input BIO raster valid masks individually, including out-of-bounds and NoData. The `10,057` count is uncovered under the current overlay, **not** necessarily individual missing observations or missing biological labels.
4. **Selection policy:** evaluate whether publisher's external target is selected/cropped for species presence and whether the original Q_unrecorded grid matches externally selected raster cells; avoid selecting new target by test performance.
5. **Replay falsifier:** accept matching fitted-final-score replay only if coordinate equality, comparable output transformation, matched scored-cell coverage and numerical source agreement are independently demonstrated; then apply original four fitted CV models to exactly same externally labelled cells.

## C. Harvest contracts (transfer only as conceptual experiments)

| Harvest ID | Source → target | Portable insight | New target-specific falsifier |
|---|---|---|---|
| H491-01 | MQR → RITHM | denominator and capture mechanism are part of estimand | audit eligible/observed denominators by year and cell before converting a rate |
| H491-02 | MQR → C3X | fixed benchmark reference removes one moving evaluator | test whether root position, engine version, search budget and PV legality are actually matched |
| H491-03 | MQR → EvoNOMOS | internal validation doesn't establish independent field success | separate oracle replay, deployment cohort and downstream independent observation |
| H491-04 | MQR → CUBE-REV | qualification creates conditional estimand | compare threshold-selected and full attempt populations; DNF and selection handling |
| H491-05 | MQR → NOMOS | evidentiary admissibility & repair routes require domain-specific contracts | an acknowledged petition must not be equated to usable remedy; source of authority cannot self-attest |
| H491-06 | MQR → NOMOS/EvoNOMOS | distinguish inclusion-minimal from least-cost witness | construct derivation DAG with more than one minimal set and unequal acquisition cost |

**Transfer governance:** none of H491-01…06 automatically opens or closes another Lab stage, authorizes connector writes, or treats analogy as independent evidence. Follow the corresponding Lab constitution, time-appropriate source and falsifiers. Retain current original Maxent P1 as MQR priority and do not drift into administrative policy instead of statistical/scientific experiments.

## D. P0 novelty and writing judgment

Reject: *We discovered fixed-background AUC normalization*; *AUC reference-change proves spatial CV optimism*; *KMM inferior in all spatial target shifts*; *we introduced minimal why-provenance*; *the finite opposite-world example is a fundamentally new impossibility theorem*.

Keep live: an **executable, source-attested typed score-comparability / repair court**, requiring demonstrable original model replay and dataset-level performance relative to manual audit and prior domain-specific matching procedures. Inability to complete a source replay is an honest result only if exact mismatch is documented as a falsifiable empirical defect with reproducible receipts.

**Next required action:** build metadata-only gridded source matrix including raster extents, transforms, per-band mask coverage, original-vs-replay intersections and source hashes. Do NOT restart AUC or claim P1 PASS until grid and matched score comparison actually succeeds.
