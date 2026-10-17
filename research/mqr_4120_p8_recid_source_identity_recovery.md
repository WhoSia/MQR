# MQR-4.120 P8 — Original Record-ID Recovery Through a Third-Party Han Tabulation

2026-10-17. **MAJOR BOUNDED DATA-LINEAGE RESULT**: full 9,223-row record-ID mapping to the MIT original and exact 1,981-record absent-ID set, **conditional on a third-party copy** of jtpa_han.tab. No official ZIP byte authentication or explanation of why rows were excluded.

## Sources actually opened
1. MIT original archival plain text: https://economics.mit.edu/sites/default/files/publications/jtpa.raw — 11,204 records, 19 whitespace-delimited fields; original first column is recid. Original MIT MATLAB source defines col2=earnings, col3=randomized assignment Z2, col4=training received D2, col5=sex.
2. Third-party GitHub text copy: https://github.com/chensy123-sys/Additive-IV/blob/main/JTPA/jtpa_han.tab — header: recid, D2, Z2, earnings, prevearn, edu, n_hs2, n_hs2_abv, sex; 9,223 data records. The repository is a later study, **NOT an author-signed or official Han release**.
3. Zenodo public reconstructed jtpa.csv, https://zenodo.org/records/18836198/files/jtpa.csv?download=1 — 9,223 data records with fields sex, n_hs2, Z1, edu, D1, prevearn, Y1, Z2, D2, earnings, Y2.
4. Han official ZIP https://sukjinhan.github.io/Han23_Replication_Files.zip has visible filename jtpa_han.tab, but actual binary bytes were not obtainable through the runtime; the third-party file **has not** been authenticated as identical to the one inside the author's ZIP.

## Executed exact full-text comparisons (without raw-byte hashes)
Parsed complete publicly retrieved MIT and third-party text sources. MIT recid values indexed to original row positions. For each of the 9,223 third-party jtpa_han.tab rows:
- recid lookup in MIT: 9,223 of 9,223 found, **zero absent**.
- recid values unique in the third-party tabulation: 9,223 of 9,223 distinct.
- MIT's values of (earnings, Z2, D2, sex) at the recovered ID equal the tabulation's values for **all 9,223 records**, zero mismatches.
- MIT source row positions strictly increase in tabulation order; zero ordering violations.
The difference of source MIT recid set and tabulated recid set contains **exactly 1,981 IDs**. Thus conditional on correctness of this third-party tabulation, the previously 15 ambiguous zero-earnings quadruple matches now have a *determinate MIT original ID* through recid; the earlier fiber/HOLD is superseded in this conditioned setting.

## Independent comparison to Zenodo reconstructed CSV
For all 9,223 rows in identical order, compared seven fields:
- Zenodo (earnings,Z2,D2,sex,prevearn,edu,n_hs2)
- third-party tab (earnings,Z2,D2,sex,prevearn,edu,n_hs2).
All **9,223/9,223 match**, with **zero mismatches**. This provides strong observational correspondence to the Zenodo release and helps transport the recovered recid through the tabulation. No independent cryptographic authenticity or original-transformation script proof follows.

## Cohort decomposition (checked earlier against the same MIT source)
Full MIT 11,204: Z=0 n=3,717 mean earnings USD 15,040.5036; Z=1 n=7,487 mean USD 16,199.9370.
Included 9,223: Z=0 n=3,090 mean USD 15,310.5201; Z=1 n=6,133 mean USD 16,487.4927.
Absent 1,981: Z=0 n=627 mean USD 13,709.8006; Z=1 n=1,354 mean USD 14,897.4409.
These are descriptive comparisons, not a causal selection-bias or design-based ITT result. The 1,981 IDs are recoverable from the set difference and **not yet attributed to particular exclusion/merge/missingness reasons**.

## Intellectual genealogy and scientific ceiling
The distinction between a unique row key and observable-equivalence class is exactly the MQR origin's quotient/latent-identity problem. Earlier 4.101 insisted on authentic source/target constraints before estimating under selective verification; 4.107 and 4.109 separated output identity from historical source authority, and 4.113 separated statistical-equivalence evidence from independent physical warrant. P8 has concretely reduced a finite **identification fiber** by observing a new variable (recid), rather than adding another Bernoulli synthetic example. Nonetheless a third-party copy plus full column consistency is not independent authorization or archival proof (4.119 J1/J2 distinction).

## Remaining discriminating tasks
Retrieve Han's official ZIP bytes intact, compare the archived jtpa_han.tab against the third-party copy bytewise or on canonical parsed records and locate code/docs giving explicit 11,204->9,223 exclusion/merge criterion; read original source for educational density and population construction. Raw ZIP custody, hash validation, exact exclusion predicate, original quantile IV or Han dynamic ordering replication, actual appeals/remedy consequences and inherited Greenberg/CCQM/Harvest/evaluator HOLD are **not cleared**.

## Verdict
RECID_9223_UNIQUE_AND_MIT_FULL_JOIN_PASS_BOUNDED; SEVEN_FIELD_ZENODO_MATCH_PASS_BOUNDED; ABSENT_MIT_ID_SET_1981_RECOVERED_CONDITIONALLY; OFFICIAL_HAN_ZIP_AUTHENTICATION_HOLD; EXCLUSION_REASON_HOLD; CAUSAL_INFERENCE_HOLD. MQR-4.120 ACTIVE / P8. No premature P9.
