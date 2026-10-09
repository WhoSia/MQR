# MQR-4.100 — P6: Authenticated EDI Original-Byte Recovery, 344-Row Lineage and Decimal-Precision Court

**Official MQR name (unchanged):** *Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport*.

**2026-10-09; internal stage, not a separate research title.** This is a full first-party dataset **source/curation comparison**, *not* a new scientific discovery, independent ecological validation, causal effect, Blackwell ordering, parameter-level identification or cross-protocol risk test.

## 1. Genuinely new source authority relative to P3–P5

At P3 the only available Palmer field record was the previously published **secondary combined** `palmerpenguins/inst/extdata/penguins_raw.csv`. At P4/P5 EDI's new login requirement blocked original files, so the exact 344-row first-party comparison was honestly HOLD.

**The user signed in to the normal EDI Data Portal and downloaded the 3 exact "Full Data Package (Zip)" archives to Research OS `00_INTAKE`**. These files were actually accessed and byte-read, not inferred from filenames/DOIs or reconstructed from secondary row partitions:

| Species | Original EDI package | Original source ZIP SHA-256 | Source CSV | Data rows |
| --- | --- | --- | --- | ---: |
| Adélie | `knb-lter-pal.219.5` | `29771c188cb1274b30f3d356716a3eadfed0954c55bbe5675cb49b10d26c79bd` | `table_219.csv` | 152 |
| Gentoo | `knb-lter-pal.220.5` | `7d141b10500a849c9de7f36c175f424ff929aa951100c0e5c62d50313186ddb9` | `table_220.csv` | 124 |
| Chinstrap | `knb-lter-pal.221.6` | `c83097abfda2489386eedae03e8f3dd8835f655463bd6caf173c2ae271b50b0e` | `table_221.csv` | 68 |

Provider package pages: [219.5](https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.219.5), [220.5](https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.220.5), [221.6](https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.221.6). DOI sources are independently cited in Horst et al. (2022), [The R Journal](https://journal.r-project.org/articles/RJ-2022-020/). EDI provider's license is CC0 1.0 per package metadata.

Each original ZIP passes CRC and contains **exactly five** items: `table_###.csv`, `knb-lter-pal.###.version.xml` (EML original package ID), text metadata, XML quality report, and `manifest.txt`. Metadata package ID, manifest file listings, all ZIP and CSV hashes were checked. **There was no cryptographic publisher signature**; trustworthy source handling is established by the user's authenticated first-party access plus byte-preserving chain and metadata consistency, not by an invented signature.

**Secondary target pinned:** `allisonhorst/palmerpenguins` commit `8957207b78d6ccd1b4654a9dd9c9041b657478ab`, `inst/extdata/penguins_raw.csv` (344 rows, 17 columns), SHA-256 `144f623143c9360fd77322a4f86acb06dc198814dbd2669724c63e6457b907bd`. Already held as original-byte archive from P3. These source bundles and target all contain publicly published observational records, not MQR-collected new birds.

## 2. Reconciliation with a declared *source-specific* rule

**Matching unit:** `(studyName, Individual ID)` because it uniquely identifies rows in **this pinned table**. `(studyName, Sample Number)` has 124 collisions and is *not* a valid global row key. Adding Species to the sample-number key distinguishes all 344. Uniqueness in the source files does not establish band-marked identity or longitudinal independence of biological birds.

Original concat order Adélie→Gentoo→Chinstrap matches **the complete combined CSV row order** for all 344 rows. Each original source CSV has the **same 17 columns in the same order** as the secondary combined source.

| Fixed comparison | Actual result |
| --- | ---: |
| Original and combined table records | 344 and 344 |
| Matched exact row keys | 344 |
| Source-only / secondary-only keys | 0 / 0 |
| Duplicate keys on `studyName + Individual ID` | 0 |
| Compared cells | 344 × 17 = **5,848** |
| Source/secondary strings **exactly identical** | **5,360** |
| Source/secondary strings different | **488** |
| Differences explained by blank / `NA` / whitespace / decimal-notation normalization | **483** |
| Numeric values with extra very-low-order combined digits | **5** |
| Remaining substantive disagreement **after original-EDI-reported-decimal-precision quantization** | **0** |

The 5 isotope cell **strings and exact decimal values are not equal**, but quantizing the secondary string back to the original EDI source's reported decimal exponent gives that original value in every case:

| Species / keyed row | Source field | Exact source text → combined text |
| --- | --- | --- |
| Adélie / PAL0809 N46A1 | Delta 13 C | `-26.69543` → `-26.695430000000002` |
| Adélie / PAL0809 N49A2 | Delta 15 N | `8.39459` → `8.3945900000000009` |
| Gentoo / PAL0910 N13A1 | Delta 15 N | `8.23468` → `8.2346800000000009` |
| Chinstrap / PAL0910 N98A1 | Delta 15 N | `9.26715` → `9.2671500000000009` |
| Chinstrap / PAL0910 N98A2 | Delta 15 N | `9.70465` → `9.7046500000000009` |

Difference size is `9×10^-16` in four cells, `2×10^-15` in one. These are **consistent with binary floating-point serialization**, but the precise underlying transformation code was **not** independently recovered. Do **not** claim literal 5,848/5,848 exact string or real-number equality. The appropriate statement is "no field content changes detected *at the source's original reported precision with explicit missing-value normalization*." The 488 cell-by-cell string differences and 344 original-to-secondary row indices are supplied as separate unmodified witness tables.

## 3. Independent prior-P3 computation replay from the recovered original source

The same explicitly documented P3 retrospective nearest-class-centroid experiment was repeated on source **directly assembled from the EDI originals** (not by copying secondary classifier outputs). Complete bill + flipper pairs: 342; first two study seasons training: 223; last season evaluation: 119. Bill-only 83/119 correctly classified; bill+flipper 113/119; 32 former errors corrected, 2 former correct predictions lost. It exactly reproduces the former secondary-combined result.

What this **DOES** establish: the specific morphometric inputs and source/target years used for P3 are directly traceable to their three EDI versioned tables at original reported precision.

What this **DOES NOT** establish: globally unique animals across seasons, independence of the model's two physical measurements, externally adjudicated species truth, fair prospective prediction, new statistical information order, or transportable ecological inference. It is *data/implementation lineage*.

## 4. Reproducibility and custody

Canonical complete original+secondary+receipt ZIP on Drive:
[**MQR4100-P6-EDI2195-2205-2216-Originals-344Row-Audit.zip**](https://drive.google.com/file/d/1xk4vV_QZlfWqvLEfcSvLQ-WkpgMRweof/view),
`MQR/01_SOURCE_ACCRUAL_RAW`, **77,425 bytes**, SHA-256 `70b4a6b8adfd024cbc53539a540649188df9108b101445609f2f7728793fe16d`. A new Drive download verified this outer SHA, ZIP CRC, and all three nested original-source ZIP hashes. It contains original 3 ZIPs, pinned secondary combined CSV, unmodified audit script, 344-row map, full 488-cell change listing, 5 precision exceptions, JSON receipt, execution log and replay instructions. Re-extracting the ZIP and running the script in a clean temporary directory actually PASSed.

A strictly byte-pinned independent audit implementation:
`experiments/mqr-4.100/p6_edi_reconcile.py` (Python Decimal/CSV and EML metadata; old no-file `p4_edi_reconcile.py` is a historical failed gate, **not** a replacement). Three original open-license ZIPs are mirrored byte-for-byte in `experiments/mqr-4.100/sources/edi-v5v5v6/` with the **original Git blob IDs verified**. A separate Rust parser cross-checks row keys and normalized 17-column comparisons in `experiments/mqr-4.100/src/bin/p6_edi_court.rs`. The repository receipt `experiments/mqr-4.100/receipts/p6_edi_audit.json` captures all source hashes and classifications. The full GitHub CI reruns against **those exact original ZIPs** and the separately fetched SHA-pinned secondary CSV, not fabricated surrogate/rewritten source tables. A successful CI certifies deterministic reproduction in a second environment; multiple languages share the **same evidence ancestry**.

**Version scope:** only 219.5, 220.5 and 221.6 vs one pinned `palmerpenguins` combined file. Prior P4/P5 access holds are historically true at those dates; *the source-access portion is now superseded by this P6 recovery*. Everything beyond source lineage stays scoped HOLD.

## 5. Scientific and governance verdict

- **PASS, bounded:** authenticated first-party EDI source-byte acquisition, package/version/EML validation, all 344 record links, all 5,848 cell comparison with transparent 488 text differences, fixed source-report precision handling, source-preserving Drive archive, EDI-based repetition of P3 sample and prediction counts.
- **NOT passed:** re-running the original creators' end-to-end cleaning scripts as a causal reconstruction; verifying banded biological identity, physical sensor independence, latent parameter kernels, new point identification, improved externally transported risk, proof of a novel theorem.
- **No new MQR official name:** this work belongs to 4.100 as an internal stage. No automatic 4.101. No bot-authored commits.
- **Possible next substantive work:** search for *actual observed mechanism changes* on a controlled measurement regime; test variable-specific source schema transformations as explicit provenance maps; independently adjudicated sensor-reference measurements with target population units. The stage's source-permission blocker has been resolved, but the science problem remains.

**At initial commit:** local original ZIP + 344-row replay + Drive verified; GitHub full external CI to be adjudicated before final stage closure.
