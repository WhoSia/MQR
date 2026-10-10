# MQR-4.112 — Primary Source Custody and Original-Data Acquisition

Formal OPEN. Source status recorded 2026-10-11 KST. This ledger does not assert access to original data absent from custody.

## FER real OSL source and source software

- Guérin et al. (2021) DOI https://doi.org/10.5194/gchron-3-229-2021 official original ZIP https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip ; exact ZIP SHA256 25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228. Contains 49 selected grain keys each FER1 and FER3; not full initially recorded physical cohort. Both official R Luminescence and independent Python decoded the same 166600 channels, whole-byte-parity PASS.
- BayLum 2021-11-11 historical R source exact commit https://github.com/crp2a/BayLum/blob/2c267b63c2b7017cae1e141d0969eb0765ad2500/R/Generate_DataFile.R ; Git blob SHA1 5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8; version 0.2.1.9000-5. This is a contemporaneous source snapshot, not yet proven the article authors' precise locally installed revision. P1 source comparisons bridge two historical reader API differences, no numerical dose or L/T formula modifications.
- P1 actual historic vs modern source-input comparison: LT and sLT differing at index locations 147/343 FER1 and 294/294 FER3; all ITimes, regenerated dose, environmental/lab dose rates, selected J and K arrays agree. The legacy number of original records per grain differs because the modern function excludes terminal SAR cycles, which alone does not imply fitted K disagreement. Per-grain row-order normalization is essential before claiming physical discrepancy.
- SOURCE-KEY ORDER WITNESS: local original FER3 DiscPos.csv matches the exact BIN 49 unique (position,grain) set but NONE of the 49 occupies the same acquisition-order position; original CSV first two grain IDs appear at BIN acquisition positions 30 and 43 (one-based). FER1 DiscPos.csv matches original BIN acquisition order 49/49. Positional LT/sLT differences may therefore reflect row permutations; P1 source-key alignment is separately under CI validation.

## Real independently measured archaeological radiocarbon witnesses

- Guérin et al. (2015) DOI https://doi.org/10.1016/j.jas.2015.01.019 , original manuscript searchable Table 1 https://files01.core.ac.uk/download/pdf/43249736.pdf associates original FER3 OSL with layer 5b and radiocarbon sample IDs S-EVA-26506, S-EVA-26507 and S-EVA-26508; layer 6 S-EVA-26510 corresponds to FER2 and MUST NOT be joined as FER3 age.
- Talamo et al. (2020), DOI https://doi.org/10.1002/jqs.3236 , Table 3 maps sample S-EVA-26506 to MAMS-16381 43370±300 radiocarbon BP; 26507 to MAMS-16371 42150±660 BP; 26508 to MAMS-16372 42370±680 BP. Excluded layer6 S-EVA-26510 maps to MAMS-16373 37380±390 BP. These are UNCALIBRATED BP, not interchangeable with 2021 source calibrated 44.4–47.3 ka. The 2015 PDF table's rendered image could not be verified due public retrieval error; text-indexed primary Table 1 is corroborated by the later source.
- Common layer 5b does not imply the bone and OSL grain are the same specimen, nor establish independent full geochronological inference. Primary AMS lab original receipt and IntCal scheme remain to acquire. The 2021 pedagogical Rmd C14age 43400±400 is not a substitute for the three actual 2015 specimens.

## Costas 2012 actual GWD + independent photo/GPR age fit — originals NOT LOCATED

- Original study DOI https://doi.org/10.1016/j.quageo.2012.03.007 and AWI article accession https://epic.awi.de/id/eprint/25988/ ; first-party thesis https://ediss.sub.uni-hamburg.de/handle/ediss/5374 . Already preserved PDFs contain aggregate sample summaries, map and first-party 2012 recovery histogram, NOT raw aliquot data.
- Current targeted user Drive search GWD / BINX / Costas did not find verified original GWD-0...245 aliquot files or independent geospatial fit matrices. External targeted repository searches likewise failed to identify a source-matched public dataset. Do not label any nearby Sylt photo-index SHP as the used 1925–2003 georegistered rasters.
- Proposed author/custodian evidence request (DRAFT ONLY, NOT SENT): (1) original GWD aliquot BIN/BINX and SAR L/T test dose reader records with source sample/grain/aliquot IDs, natural vs separate bleaching assay custody and selection screens; (2) 1925 map and 1936,1944,1958,1965,1988,1998,2003 historical orthophotos and 2009 baseline image, original GIS registration control point uncertainty, exclusions and coordinate transforms; (3) GWD-08 GPR original trace, picks, propagation velocity assumptions and profile/sample depth join; (4) regression design matrix, fit residual/covariance and version history; (5) permission/licence and accession or secure read-only research access.

## Admission

Source-matched selected FER original signal bytes PASS. Source historical versus current preprocessing positional equality FAIL_BOUNDED, source ID alignment PENDING. Real FER3 layer5b published specimen IDs PASS_BOUNDED (original manuscript text only). Original Costas actual aliquot/GPR/GIS fit access HOLD. Transport invariance and new MQR law HOLD until aligned held-out physical test.
