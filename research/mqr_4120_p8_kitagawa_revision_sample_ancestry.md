# MQR-4.120 P8 — Historical JTPA Sample-Size Revision in Kitagawa–Tetenov

2026-10-17. Source-document comparison, not code-level selection replication.

## Source distinction
An earlier Kitagawa–Tetenov *Who Should Be Treated?* manuscript explicitly uses JTPA 11,204 adults aged 22+. Source: https://discovery.ucl.ac.uk/1522145/1/Kitagawa_Who_should_be_treated_Working-paper_May17.pdf . A later revision in the Bristol university repository explicitly states an empirical sample of **9,223 observations with available years of education and pre-program earnings** from the adult JTPA cohort. Source: https://research-information.bris.ac.uk/files/137721118/Who_should_be_treated_Kitagawa_Tetenov.pdf . Both are versions of the Kitagawa–Tetenov empirical welfare maximization research lineage. Another independent 2022 Byambadalai JTPA study reports exactly 9,223, 6,133 assigned and 3,090 controls and cites following Kitagawa–Tetenov 2018 for its inclusion conventions.

## Relevance to previous MIT–Han comparison
MIT original public jtpa.raw contained 11,204 records; a later third-party copy of jtpa_han.tab carries 9,223 unique MIT recids, all joined exactly with source earnings, Z, D and sex and aligned with the Zenodo reconstructed CSV. The difference is precisely 1,981 recids. The historical revision supplies a **published selection-rationale candidate: availability of education and preprogram earnings**, strongly preferred for investigation over the prior unsupported speculation that Han's Census/NCES school-density join first removed 1,981 persons.

## Warrant and falsification gate
The revised paper's inclusion rationale does not establish which precise 1,981 MIT record IDs were excluded by which missing-value flags or data transformations, because the MIT archival 19-column file does not itself expose all original education/pre-program earnings fields needed for an unambiguous complete-case filter. Do not claim that exclusions were reproduced. Independently confirm author replication code, missingness conventions and row-level correspondence. Historical manuscript versions need to be attributed accurately (earlier manuscript versus later revision, not necessarily a single fixed edition). Author binary archive authenticity and full preprocessing history remain HOLD.

## Original MQR philosophical continuity
MQR 4.101 selection-relative targets, 4.107 production histories, 4.109 provenance-sensitive sufficiency and 4.119 contestable standards. Research record count agreement establishes no causal assignment-effect transport; keep 4.89's pre-existing nonidentification and 4.113's experiment-order restrictions intact. 4.120 ACTIVE/P8. This is historical source genealogy, not a new universal theorem.
