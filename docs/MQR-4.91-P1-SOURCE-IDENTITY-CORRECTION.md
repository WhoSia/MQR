# MQR-4.91 — P1 Source-Identity Correction and Replay Audit
**Date:** 2026-10-08. **Status:** SOURCE IDENTITY ERROR CONFIRMED; PROPER EXTERNAL REPLAY PENDING. This is an explicit factual amendment to MQR-4.90's past failed execution, not an overwrite of that historical run.

## Observed measurement, not hypothesis

Read-only run 37775803581 CI PASS: source eight climate BIO input grids identical geometric metadata/masks; independently projected original final model did execute. Run 37776111431 CI PASS: the **wrongly selected** original archive output `.../Oxalis_latifolia.asc` spans x=-124.5..-29.0, y=-55.5..49.0 with 191x209 cells and 10,057 valid points. Java projection of source climate `Oxalis_latifolia_Oceania` spans x=-178.5..179.0, y=-55.0..-9.5 with 715x91 cells and 2,931 valid. Shared valid pairs 0; 6,683 publisher valid points outside replay bounds and 3,374 within geographic extent but no replay value. Therefore old 10,057 number is NOT a model-output discrepancy on matched cells.

Publisher archive inventory run 37776427465 CI PASS reports **two separately named ASC outputs inside the same 56_predictions/Oxalis_latifolia_America-Oceania directory**:
- `Oxalis_latifolia.asc` = native/base model map, geographic bounds empirically American.
- `Oxalis_latifolia_オセアニア.asc` = separately named Oceania target prediction map, **proper candidate for replay**.
- A `_オセアニア_clamping.asc` and `_オセアニア_novel.asc` also exist and are ancillary, not the predictive score raster. These source facts were unknown when 4.90 was closed.

## Correction of inference

Historical GitHub Actions 37745214684 and 37745501466 REALLY failed. Yet treating the first filename in the directory as the intended out-of-region target raster was a **researcher file-selection error**. It is incorrect to call these failures evidence of author's published Maxent map not reproducing, or of inherent missing data. Correct comparability reference must select the tagged target map and validate transformation/extent first.

## Reproduction fork

Independent P1.3 script `experiments/mqr-4.91/p13_corrected_published_target_projection.py` corrects published ASC reference to `Oxalis_latifolia_オセアニア.asc` under original archive path while retaining original source and jar checks, fail-closed Maxent exact numeric grid compare and only then four fold model projection. Workflow `.github/workflows/mqr-4.91-p13-corrected-projection.yml`; CI 37776623731 is the check authority. Do not call PASS before completion. If numeric replay fails, inspect Maxent output formats/clamping/config; new properly paired mask, not the previous zero-overlap original file, must ground all interpretations.

## Scientific lesson and Harvest

Typed `ModelFitOutput` vs `GeographicTargetProjection` file naming is an empirically demonstrated distinct input type, not merely a bookkeeping convention. A directory's label does not prove file identity; source artifact filename, native domain, geographic extents, and tag-specific output semantics must be checked. This is a concrete experimental motivation for source-backed contract checker and for testing whether it reduces manual misclassification. This does NOT establish generic provably optimal repair certification or broad performance claims. Inherited 4.90 CLOSED status unchanged; 4.91 corrects the historical interpretation.
