# MQR-4.120 P8 — Eligibility Predicate versus Available Source Fields

2026-10-17 — DOCUMENTARY ELIGIBILITY CONDITION CONFIRMED; ROWWISE HISTORICAL FILTER NOT REPRODUCED.

## Primary documentary evidence and genealogy
The later Kitagawa–Tetenov *Who Should Be Treated?* manuscript, archived at https://tetenov.com/Who_should_be_treated_Kitagawa_Tetenov.pdf, explicitly defines the National JTPA empirical sample as **9,223 observations with available years of education and pre-program earnings**, among adults aged at least 22 in the prior JTPA evaluations. This is a direct historical sample-selection description, not an inferred rule from imputation fractions. The May 2017 working draft discusses an 11,204-person adult source sample; the November 2017 revision and subsequent published lineage use the restricted cohort. Publication-date claims about individual PDFs must be tied to their explicit version labels; website crawl recency is not manuscript dating.

## Data-plane dependency and non-identification
MIT AAI2002 jtpa.raw, previously exhaustively parsed, is a 11,204 × 19 original-analysis numeric file with recid in col1; documented earnings/assignment/receipt/sex and imputed indicator covariates. It is not itself a documented complete-case dump of the unmodified raw schooling and pre-program earnings variables for all 11,204 applicants. The later third-party jtpa_han.tab contains edu/prevearn only on the 9,223 *retained* recids. Thus, from this pair alone, the historical availability indicators on **the 1,981 excluded IDs are missing**: one cannot evaluate the proposed complete-case predicate independently on the excluded records. The zero unmatched join of retained IDs does not fix this missing-source-field problem.

Let R_i denote whether an adult MIT record is selected. The documentary candidate is R_i = 1{education_i observed AND pre_earnings_i observed} under the full input system's missingness coding and eligibility. The available retained-only dataset tells us education_i/pre_earnings_i values when R_i=1, but not which constituent predicate failed for R_i=0. Many missingness-pattern assignments on the 1,981 excluded records are observationally compatible with the same final R vector. An exact recid deletion list is therefore not, by itself, a proof of a historical deletion algorithm. This is an instance of the MQR observation-quotient and 4.107/4.109 history/provenance distinction, with 4.101 selection-relative target qualification.

## Adversarial guards
- MIT col10 wkless13 imputation footprint is a strongly associated baseline indicator, **not** a documented missingness flag for education or pre-program earnings. The existing simple col10 exclusion hypothesis has already been falsified.
- Identical N=9,223 and assignment/compliance margins in other works corroborate shared cohort convention but do not certify authorship or row-level derivation.
- The two-stage selection-and-outcome-threshold decomposition in other P8 notes is descriptive and does not confer ITT/LATE identification after restricting an experimental cohort.
- Exact treatment-rule welfare rankings and Han partial-order LP are not replicated; scientific-appeal J2 issues cannot be inferred from these policy data.

## Required next empirical witness
Acquire an upstream JTPA individual-level source that has original recid plus unmodified adult/education/pre-program-earnings availability flags for **all 11,204 candidates**, or author-side preprocessing script that constructs them; apply its declared predicate, compare both retained and excluded ID sets exactly, and record any residual exceptions. Without this additional input, this history is source-supported at the **verbal eligibility-description level only**.

VERDICT: ORIGINAL_ELIGIBILITY_DESCRIPTION_SOURCE_VERIFIED / FILTER_INPUT_COVERAGE_HOLD / 1981_ID_PREDICATE_REPRODUCTION_HOLD / AUTHOR_ARCHIVE_BYTES_HOLD. MQR-4.120 ACTIVE/P8; all inherited source and assessor HOLDs preserved.
