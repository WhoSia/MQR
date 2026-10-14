# MQR-4.114 P2-I — Retrospectoscope Access, Historical SRM Certificate Version, and Original Calibration-Custody Gate

**2026-10-14; OPEN / documentary PASS_BOUNDED; raw-dataset acquisition HOLD.** Inherits [P2-H](mqr_4114_p2h_source_typed_calibration_ancestry_matrix.md). This is not a new physical intervention or a new inference about any laboratory's actual error covariance.

## Official publication and original-vs-compiled boundary

- NIST 2024 [Reference Manual](https://www.nist.gov/publications/ccqmretrospectoscope-reference-manual-detailed-reference-ccqmretrospectoscope-suite-0), DOI [10.6028/NIST.IR.8478e2024](https://doi.org/10.6028/NIST.IR.8478e2024): explicitly identifies the public version as a **curated database of publicly accessible studies** and distinguishes NIST's master database, which also holds confidential pilot-study records and provisionally curated reports under review. It does **not** establish public accessibility of confidential master data, original participant submission workbooks, or instrument-level signals.
- NIST 2024 [Quick Start](https://www.nist.gov/publications/ccqmretrospectoscope-quick-start-beginners-guide-data-analysis-system-visualizing-0) describes the September 2024 workbook as compiled measurement-comparison results and visualization/analysis tools, not injection files or original institution laboratory notebooks.
- NIST dataset [PDR DOI 10.18434/mds2-2952](https://doi.org/10.18434/mds2-2952) lists a public `.xlsm` URL `https://data.nist.gov/od/ds/mds2-2952/CCQM_Retrospectoscope_Public_20240901.xlsm`. **New direct tool access attempts on 2026-10-14 failed**: web binary open inaccessible; container HTTP request failed during DNS resolution; therefore **no workbook byte, SHA-256, sheet name, K11.2 inclusion, or row is claimed verified in this session.** Do not execute VBA/macros. The website publication link exists independently of local reachability.

## Historical 917c certification facts

- [NIST official 917c archived CoA](https://tsapps.nist.gov/srmext/certificates/archives/917c.pdf), original institutional PDF, 2 pages re-checked on 2026-10-14. Current archived document **issue 2020-06-22**, certified D-glucose **mass fraction purity 99.7% ± 0.3 percentage points expanded (k=2)**, conditional nominal expiry 2026-05-01. Explicit history: 2009-06-30 first issue; 2013-11-21 extended validity and editorial changes; 2016-02-10 editorial; 2020-06-22 update. None of this supplies original **2009 or 2013 certificate bytes** or documents **which exact certificate revision/physical SRM unit** was in the possession of HSA, INMETRO, LNE, or NMIJ during CCQM work.
- Distinguish the purity-certified **chemical SRM 917c** from the distributed **serum comparison material**. Certificate identity is a source-node; historical institution-specific use requires separate custody evidence. Shared catalogue label does not prove shared physical bottle, common error, or error independence.

## Source-typed unresolved request matrix

| Proposed document or observation | Public status now | What a successful original would add | Does it independently identify physical reference truth? |
|---|---|---|---|
| September 2024 Retrospectoscope .xlsm | Public stable URL/official manual; local bytes inaccessible | Cross-check curated published study coverage, K11.2 rows if included | **No**. Later derived summary |
| 2009/2013 original NIST 917c CoA revisions | Revision events authenticated in 2020 CoA; original document bytes HOLD | Historically time-matched value/uncertainty and effective wording | **No**; per-institute material use unknown |
| Per-participant original 2012–2013 Reporting Forms | Historical existence supported by BIPM Appendix B/D screenshots; accessible raw files HOLD | Original row-level uncertainty input provenance, calibration identity, calculation detail | Not alone |
| Instrument detector response / per-injection original traces | Accessibility unverified | Measurement-operation repeatability and calculation traceability | Not automatically |
| Actual label, certificate copy, date, working reference solution records, uncertainty sensitivities | No institution-specific originals inspected | Graph edges linking each institution to reference ancestry | Not necessarily |
| Independent certified same-serum measured value | Not verified | Break some common-calibration gauge indeterminacy if independent traceability and measurand matching demonstrated | Potentially, conditional on genuine independence |

## Access strategy and negative assertions

First attempt **nonexecuting, read-only** access to the published NIST workbook via official PDR. If reached: record HTTP URL/redirect, byte length, SHA-256 and ZIP entry inventory, then identify workbook sheet names in a parser that never runs macros, and test whether K11.2 appears. Avoid proprietary/confidential master data. For historical certificate revisions or original submitted forms, the [NIST SRM archive](https://shop.nist.gov/ccrz__CCPage?pageKey=SRMArchive) and [BIPM KCDB](https://www.bipm.org/kcdb/) describe institution-administered records access channels. No correspondence was sent and no privileged data access obtained.

**Identification frontier:** conditional model `Y_i=theta+b_i+a_i Z+epsilon_i` still cannot identify `Cov(e_i,e_j)` from published marginal `u_i`. Access to **compilation rows alone** does not resolve ancestry. Even per-injection data without historically matched calibration records cannot establish metrological independence. Evidence acquisition alters mathematical admissibility only if new independently witnessed source edges or observations are actually produced.

**Scientific verdict:** `P2I_PUBLICATION_SCOPE_VERIFIED / HISTORICAL_917C_COA_RECHECK_PASS / PUBLIC_WORKBOOK_BYTES_ACCESS_HOLD / INSTITUTION_FORM_AND_PHYSICAL_REFERENCE_HOLD`. No P3/P4, no Real Lang 0.44 promotion.
