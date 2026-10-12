# MQR-4.114 P2-F — Institution-Level Data and Reference-Ancestry Audit: Source Available versus Source Missing

**State 2026-10-12:** MQR-4.114 OPEN, P2-F documentary original-source audit **PASS_BOUNDED**, independently certified calibration error covariance **HOLD**, causal source attribution **HOLD**. This is inside P2; P3/P4 not authorized. Previous P2-E Rust 20/20 CI remains the last CI-verified executable physical comparison. **A proposed P2-F GitHub native Rust upload was blocked by the safety checker; no new executable, tests or CI success may be claimed for P2-F.** Exploratory matrix calculations below were conducted privately as mathematical sensitivity, not independently source-certified.

## Original documents actually examined and custody

A. [Official 2018 BIPM report](https://www.bipm.org/documents/20126/44596658/CCQM-K11.2_and_12.2.pdf/1e39817b-940d-09a5-d098-651f65a2ab27), original DOI `10.1088/0026-1394/55/1A/08012`, **70 pages**. Methods and results tables 4–7, Appendix A tables A2/A3, **Appendix B pages 35–50: screenshots of participants' Analytical Information Excel worksheet**, and analogous creatinine Appendix D pages 56–70. This confirms **actual participant-reported numerical calibration inputs and within-institution uncertainty budgets are indeed partially included**, stronger than saying only combined institute means are accessible. The public report does **not** provide access to every original per-injection chromatogram or a machine-readable copy of each *Reporting Form* workbook, nor a verified cross-institution covariance matrix. These underlying institutional archives **may exist**, but were not found attached to the original BIPM report, public KCDB comparison entry or NIST article record. We cannot claim none ever existed.
B. [NIST SRM 917c official *archived* certificate](https://tsapps.nist.gov/srmext/certificates/archives/917c.pdf), 2 pages, explicit **D-glucose certified mass-purity 99.7% ±0.3 percentage points expanded uncertainty, k=2**. The viewed version was **issued June 22, 2020**, with conditional certification expiration **May 1, 2026**, and revision history **original June 30, 2009; November 2013; February 2016; June 2020**. **This 2020 revision does not certify the exact content of 2012 participating institutes' contemporaneous certificate holdings**. The 2009 original and 2013 revision as actually held by each institute were not obtained. The expired-in-2026 archived certificate is appropriate historical evidence, not a current license for use.
C. [NIST official FAQ](https://www.nist.gov/srm/faqs) clarifies that **SRM identifiers need not include any extra lot number**; when no separate lot or serial is on the certificate, the SRM numeric/suffix identifier is the official identity and the laboratory sample label must match. Therefore P2-E's earlier phrasing "missing lot number" was excessively strong. The genuine missing evidence is each institution's original physical source identifier and label match, certificate revision effective at measurement, calibration solution records, purity uncertainty propagation, actual shared source effects and uncertain covariance. Never invent a per-vial lot number.
D. NIST issued a **different successor SRM 917d** and corresponding independent high-purity certification literature in 2023, including qNMR-based metrology. It is a **different later reference material/issue** and cannot retrospectively validate original 2012 CCQM sample or share the original 917c material identity. Prior sample certification SRM 965c also does not back-link to these original measurements.

**User Drive status:** specific 2018 CCQM report PDF, 2020 NIST 917c certificate, 2023 917d documents or original spreadsheets were not identified in current user Google Drive intake or targeted search as user-controlled archived PDFs. They were read directly from official public sources. Do not invent Drive file IDs or migration/readback.

## Actually source-reported intra-institution numerical inputs

The official BIPM **Appendix B p. 37 (PDF P36)** presents HSA's sample-level uncertainty budget from its Reporting Form, including (approximately, small rounding):
- `C_Z`, calibration standard solution concentration, **1410.8 µg/g**, standard uncertainty **3.9210 µg/g** (relative **0.278%**) and variance contribution **28.3%**.
- `R'_M`, converted calibration response variable, value **0.7436**, standard uncertainty **0.0023**, variance contribution **34.4%**.
- Other variance share terms include specimen mass 0.9%, labelled-standard mass 0.8%, method precision 12.9%, ion-pair 4.4%, extraction 3.7%, and derivatization 14.7%. The sum **100.1%** is normal reporting roundoff.
- The printed contribution-squared sum is approximately **36.4045 (µg/g)^2**, corresponding to about **6.0336 µg/g** within the *specific HSA vial-level example*; this is **not** HSA's combined participant institute standard uncertainty **0.004 mg/g** used in P2-E. Do not interchange vial budget and institute combined uncertainty.
- Other participating institutions disclose selected input numbers, measurement equations, and uncertainty descriptions in Appendix B, e.g. CENAM's source-reported calibration concentrations and sample instrument response factors. These are **partly reconstructed input-variable summaries, not injection-level raw data**.

**Crucial inference firewall:** **28.3% of HSA's local uncertainty variance is NOT a 28.3% cross-laboratory covariance**, nor evidence all SRM 917c users shared identical bottles, certificate errors or calibration-stock preparation. The published original data give no directly certified `Cov(e_i,e_j)` for independent institutions.

## Calibration ancestry original-source cross-check

P2-E listed seven `NIST SRM 917c` source-catalog mentions including post-discordance reference laboratories, across GC and LC-MS. Of the **nine original** K11.2 participant institutes, the four unambiguous named **917c** sources are **HSA, INMETRO, LNE, NMIJ**; exclude NIST/KRISS/PTB from original main cohort because they are reference/late additions and retain **VNIIM source-conflict HOLD**: original Appendix A2 gives **917a** while A3 lists **917c**. Mere catalogue reuse cannot identify physical shared impurity content, covariance or universal drift.

The NIST 2020 archived certification source concerns **chemical purity of D-glucose**, not a certified glucose concentration on the actual serum pool (original SRM1951b's certified property was cholesterol, not glucose). These are separate reference objects and must remain different graph node types.

## Retrospective covariance sensitivity (explicitly hypothetical, not a prereg test)

Reference P2-E results previously inspected and known: nine original participants, source reported means `y_i` and standard uncertainties `u_i`, weighted mean **1.1570068137 mg/g**, `Q0=22.120695703`, critical chi-square df8 at alpha0.01 **20.09023503**. *Assumption sensitivity only*, no extra physical measurement or inferred actual covariance:

Let `s_i=1` for the four original SRM 917c catalogue users and `0` otherwise. Posit a perfectly shared additive random reference factor of hypothetical standard uncertainty τ *among these four* while preserving each source-reported marginal `u_i` by reducing its residual independent variance appropriately:
`Sigma(τ)=diag(u_i^2−τ^2 s_i)+τ^2 s s^T`.

This is positive definite when `τ<min_{s_i=1}u_i`. Set an **illustrative scale**, not an empirical 2012 uncertainty, from the archived 2020 certificate's expanded purity interval and the P2-E weighted mean: `tau_ref = 1.1570068137 × 0.3/(2 × 99.7) ≈0.0017407324 mg/g`. This makes a *perfectly common standard-value uncertainty* assumption that has **not** been documented across labs; users must not interpret its value as a measured bias, a certified 2012 correlation, or a fresh test. Source HSA's full calibrant u=0.278% includes more than the certificate's apparent 0.150% purity share.

Numerical GLS `Q = min_theta (y−theta1)^T Sigma^-1 (y−theta1)` for fixed prespecified sensitivity multipliers (from an **after-P2-E exploratory plan**, not an outcome-blind preregistration):
- τ=0: **Q≈22.120696**.
- τ=tau_ref: **Q≈23.464935**.
- τ=2 tau_ref: **Q≈29.644004**.

Thus **under that particular hypothesized catalogue-sharing covariance family**, introducing positive uncertainty correlation does not rescue the 1% strict compatibility threshold: in these cases Q increases. This is neither a fitted empirical interlab covariance nor a proof correlated error cannot exist; changing correlation structure, error-variance assumptions, group membership and true material behavior could produce different consequences. A *uniform common additive bias* shifts fitted location without changing the between-institution Q at all, and is not identifiable separately from unknown true analyte quantity from one common sample.

The only affirmative source-grounded statement is **shared-source *catalogue labels* and detailed local uncertainty ingredients are partially known**. Full source material lot/issue actual use, cross-institute `Cov`, original raw detector traces, and causal source of 2018 discordance remain NOT IDENTIFIED / HOLD. No causal discovery, no Real Lang release.

## Exact evidence gaps and bounded continuation

Ask the NIST CCQM original coordinators/BIPM KCDB archivists, if they are willing to provide:
1. Original 2012–2013 **Analytical Information** workbook and machine-readable **vial-level original submission forms** (the PDF only pictures them), plus explicitly selected per-injection isotope-response data or calibration-point tables **with shared-material ID/time and units**. Separate historical submitted spreadsheets from any later corrected files.
2. For each source-labeled SRM 917c original institution, **contemporaneous original certificate revision and physical bottle/issue identification** (additional lot only where one was actually assigned), analytical calibration-solution preparation record and calibrated response/impurity purity standard uncertainty mapping. For labs using other standards, analogous provenance.
3. An actual **between-laboratory cross-covariance matrix or joint uncertainty propagation** for shared certification components, documenting underlying common random calibration input(s), sensitivities, dates/versions and whether the same material and control CRM were used. Non-availability should be recorded, never guessed from percentages.
4. Original same-material **separately referenced standard** and independent physical reference measurements or plausible witnessed intervention, clearly distinguishing previous/post-discordance reference-lab recruitment. If missing, the original report's unexplained results cannot be uniquely repaired from documents.

No external email was sent or request initiated; this is the precise documentary access contract for user approval if desired.

**Current result:** P2-F source audit PASS_BOUNDED, *common additive offset alone explains source heterogeneity* REFUTED CONDITIONAL in an old algebraic sense; hypothesized shared-certificate covariance gives sensitivity values only; actual covariance, actual common bias and physical independent reference **HOLD**. The original P2-E 20/20 GitHub Rust CI is still the last source-tested success. A new P2-F code upload was blocked by a safety check, and this audit **does not** claim new code execution or CI PASS.
