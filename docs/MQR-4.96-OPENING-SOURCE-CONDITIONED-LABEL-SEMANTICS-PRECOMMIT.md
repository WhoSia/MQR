# MQR-4.96 — Observation-Process Confounding, Source-Conditioned Label Semantics & Calibratability Under Provenance Shift

**Title proposed and opened 2026-10-09 under explicit user instruction to hand off immediately after 4.95 bounded closeout.** Await user confirmation of the final long-form name; do not retroactively claim the user chose this wording.

**Status:** OPEN / SCIENTIFIC QUESTION + SOURCE-CONTRACT PRECOMMIT / NO 4.96 EMPIRICAL CLAIM YET.

## 0. What changed scientifically

MQR-4.95 has closed with **actual 2024 historic** raw GBIF and original Serov CSV recovered and stored in Drive, not merely an archive URL or CI logs. Rust verified every one of **29,543 row-ordinal corresponding** binary labels `ABSENT→0`, `PRESENT→1`, same numeric coordinates/year (after formatting normalization), 27 original source dataset UUIDs. The original CSV lacks all `gbifID/datasetKey/occurrenceID` keys and has 3,031 same-lat/lon/year/label tied groups comprising 15,938 rows; ID reconstruction needs the preserved *original row ordering*, not an independently keyed join. Original author GBIF-to-feature ETL is not published in the pinned tree.

**Material new evidence:** original 2024 **11,165 of 11,166 negative labels** come from **one publisher observation campaign** (Finnish Nature League Spring monitoring; that source also supplies 3,486 positives). All other 26 publisher sources combined supply one negative and 14,891 positives, including 9,686 Kastikka positives and zero Kastikka negatives. Thus the binary response mixes observation protocols, geography, survey effort and publisher origin. It is FALSE to presume homogeneous negatives sampled independently across all source subpopulations.

This is a substantive **observational provenance / measurement semantics / positivity** problem, not a reason to add another near-identical Serov geographical holdout.

## 1. Explanandum

**Can target-risk estimation and conditional-label transport be identified when the event `Y=0` is almost entirely supplied by one collection protocol, while much of `Y=1` comes from other collection processes?**

Formally, `R_Q(f)=E_Q[ℓ(f(X),Y)]` is a target-risk estimand only once `Y` has a specified **detection protocol and sampling event**, not just a shared string field. The observation `Y=0` under a checklisted survey with known effort is not necessarily an equivalent measurement to nonappearance in a presence-only archive. Let `S` denote actual original field-collection source/protocol; preserve source source/root IDs. Require positivity/overlap, explicit detection and sampling semantics, and a defendable bridge before `P_Q(Y|X,S)` can be transported.

## 2. Honest baseline and competing hypotheses

H1: Source identity or field sampling protocol predicts label strongly beyond location, year and BIO features. This can represent *recording/selection mechanism*, ecological site differences, or confounding; source-predictive accuracy alone never proves causal shortcut learning.

H2: Conditioning or stratifying on actual source reveals **class support failure**: in 2024 original, Kastikka has zero recorded negative; a source-conditional binary risk for that source is not point-identified under arbitrary counterfactual label mechanism. It may be identifiable for *observed label distribution within that archive*, but that is not population ecological absence without an observation mechanism.

H3: A genuinely protocol-matched independent survey collecting explicit detected/non-detected labels can improve semantic transport or calibrate risk **only after** unit, taxon, effort, spatial correspondence and mechanism invariance are audited. Swedish NFI is a real independent 2-class ecological field survey but **not** matched to the 64 Finnish target locations. It may serve an explicitly new Swedish-domain contact, not be silently inserted as Finland calibration.

Rival explanation: Finnish Nature League and Kastikka may sample different habitat/years/locations/taxa checklist, so a source-label association need not be measurement bias in the underlying ecological phenomenon. Distinguish known `occurrenceStatus` coding from latent true occupancy and variable detection.

## 3. Executable Rust + Lean next gate

Use the **actual frozen original source archive** already preserved:
- Drive raw original [GBIF 2024 ZIP + author CSV + notebook + SHA](https://drive.google.com/file/d/1OBJ7DJqNKUH5-GgMX5I10xlyr6erVj3v/view);
- full [29,543 gbifID→presence positional reconstructed table, 27-source status breakdown](https://drive.google.com/file/d/1VzoJYfMnp17cDBKXD3MPLRyJ0-w4YHNy/view);
- bound scientific predecessor [MQR-4.95 final court](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.95-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md).

First 4.96 material task: Rust exact publisher-source × field-label counts, positive/negative support, and heldout contrast on the **original provenance joined** data; predeclare comparator with location/year controls, measure separability without interpreting source coefficient causally, and explicitly preserve source-correlation and event cluster. Lean 4 scope theorem should prove non-injectivity of source-ID-erasing row projection under duplicate visible records, and/or the exact insufficiency of source-conditioned class observations for hypothetical non-detection events when no matching protocol receipt exists. The proof is conditional mathematical syntax, not ecological correctness or missing finite-data creation. Make a bounded full comparative study, then stop at empirical court.

No generational inflation: each new MQR version must resolve a distinct empirical/mathematical obstacle, preserve earlier inconclusive findings, and produce new falsifiable contact with the world. `4.95 CLOSED`, `4.96 OPEN`. No 4.97 without new PI direction.

## 4. Governance and authority

ONE Notion MQR canonical root page `3c8ef561cf92815693b6-fcf6de9955f7`, append 4.95 final and 4.96 precommit as sections. Do not create separate MQR Lab DB rows or displace historic subpages. Main-branch `WhoSia` human-authored commits only; Actions `contents:read`, no bot author/push/tag. Source archives kept in existing `02_ANALYSIS_SAFE` Drive; no duplicate raw re-downloads merely to multiply artifacts.
