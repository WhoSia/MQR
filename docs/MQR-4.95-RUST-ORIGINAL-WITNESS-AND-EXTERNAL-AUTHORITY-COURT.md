# MQR-4.95 — Rust Original-Source Calibration Court and External-Witness Boundary

**Author-confirmed name:** MQR-4.95 — Independent Calibration Witnesses, Spatially Dependent Sampling & the Identifiability of Informative Target-Risk Bounds.

**Court state 2026-10-09:** `OPEN / RUST NATIVE FINITE-TARGET LABEL-AUDIT PASS / DESIGN-CAPABILITY TEST PASS / EXTERNAL INDEPENDENT CALIBRATION HOLD / POPULATION-SPATIAL INFERENCE HOLD`.

**DO NOT close 4.95 yet:** The title's scientifically demanding external independent-calibration witness is not yet demonstrated. A bounded code success on the same Serov publisher source does not authorize stage-wide completion. This document records P1 empirical + mathematical findings and a falsifiable P2 external-acquisition gate.

## 1. Source, original experiment lineage and epistemic custody

Root original Serov, Koldasbayeva & Zaytsev (2026), Scientific Reports, DOI `10.1038/s41598-026-36740-7`, publisher repo `egorser0v/Importance-reweighting` fixed commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`. Pinned `datasets/species/anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`, independently checked by `git hash-object` on CI before Rust ran. Data shape: 29,543 original rows; 2,905 rows surviving 2013–24, original physical Finland-coordinate and all 19 BIO completeness; 988 unique eligible WEST positions, 411 EAST positions. This count concerns the original frame, not a second study.

**New Rust experiment vs old Python experiment distinction:** P1 crate `experiments/mqr-4.95/` (Cargo std ONLY, zero external Rust packages), uses FNV-1a site dedup and fixed ranking, first 512 WEST original-position records for source FIT, next 64 WEST for source G, first 64 EAST for target P, and a **new** source-only 19-BIO standardized logistic gradient-descent predictor (1000 epochs, learning rate 0.12, ridge penalty .015). It neither claims to match original author's KMM nor the 4.93–4.94 Python sklearn model/target sample. No target Y/label is parsed on the primary source-frame walk: only selected FIT/G source labels are re-read for fitting. **All target probabilities and three audit-site orders** are frozen before parsing the selected target Y in a final pass. The labels nevertheless already existed in the same publisher CSV: this is a **masked-label retrospective audit simulation**, NOT genuinely newly acquired, independently collected or separately attested field measurements.

## 2. Rust implementation and failed-to-successful CI path

Source: `experiments/mqr-4.95/Cargo.toml`, `src/main.rs`, `src/design.rs`. Workflow: `.github/workflows/mqr-4.95-rust-calibration.yml`, permission `contents:read`, never commits. Original data only downloaded into CI working scratch, and summary+CSV+test logs are artifacted; no distribution of entire upstream raw CSV in Drive receipts.

Failure receipts retained in GitHub Actions:
- [37807365453](https://github.com/WhoSia/MQR/actions/runs/37807365453): Rust test-syntax non-leading-zero float literals + ambiguous numeric type; corrected in human-authored commit `f64f6ecd`.
- [37807440227](https://github.com/WhoSia/MQR/actions/runs/37807440227): 4 Rust math tests passed and publisher CSV Git blob hash matched; original CSV header fields are quoted, first hand-parser rejected `bio1`; corrected by quote-stripping and actual header regression.
- [37807652370](https://github.com/WhoSia/MQR/actions/runs/37807652370): quoted-CSV test fixture incorrectly double-escaped; test caught actual fixture error, corrected in commit `a11bc338`.
- [37807748787](https://github.com/WhoSia/MQR/actions/runs/37807748787): successful actual 5-test + original-source Rust court.
- **Final [37808091457](https://github.com/WhoSia/MQR/actions/runs/37808091457) SUCCESS**: 8 Rust tests PASS (including source-root authorization, two adversarial target-label worlds, exact equal-cost width minimization on all small subsets, actual quoted CSV parsing, sampling first/second-order inclusion gate and 4-outcome full-enumeration Horvitz–Thompson design mean). Original Git hash PASS; original-data risk interval execution PASS; publication-level independent witness `HOLD` as required, NOT re-labelled PASS.

No GitHub Actions bot-authored commit; commits use the human account `WhoSia`.

## 3. Measured same-root original-data masked-label acquisition

Finite target = 64 original but freshly hashed Finnish Anemone geographic sites, actual source-model logits fixed before target Y access. The retrospectively fully revealed target positive count was **40/64**, and its realized mean logloss oracle = **0.656484555903**.

Without any target labels, the sharp finite-site label-extrema convex-hull interval was **[0.276758587422, 1.687878538646]**, width **1.411119951224**. The set of realizable fixed-64-site label assignment losses is discrete; endpoints are sharp, and this interval is its convex hull, not an assertion all intermediate losses occur.

At a frozen set of observed site labels A, and unobserved U, let `a_i=-log(1-p_i)`, `b_i=-log(p_i)`; then sharp extrema
`L_A=(Σ_A loss(y_i)+Σ_U min(a_i,b_i))/64`, `H_A=(Σ_A loss(y_i)+Σ_U max(a_i,b_i))/64`;
its exact width `W_A=Σ_U |b_i-a_i|/64`. Opening a site's actual label therefore contracts the envelope by **`|log(p_i/(1-p_i))|/64`**, independent of the revealed 0/1 value. All observed audit intervals contained the final oracle, nested and reached zero at k=64.

| Site labels revealed, k | Fixed hash width | Top-score-width width | Latitude-quartile-balanced top-width |
|---:|---:|---:|---:|
| 0 | 1.411120 | 1.411120 | 1.411120 |
| 4 | 1.352668 | 1.224591 | 1.230871 |
| 8 | 1.226191 | 1.060681 | 1.085319 |
| 16 | 1.047015 | 0.771211 | 0.812694 |
| 32 | 0.733988 | **0.322811** | 0.395757 |
| 64 | 0 | 0 | 0 |

The `top-width` rank uses only p_i, not target labels, and is *exactly optimal under fixed equal-cost observation of k sites for the narrow objective of shrinking the finite-target convex-hull width*, since width is the sum of nonnegative unobserved contributions. A six-site exact exhaustive subset test checks every k and all possible chosen sets; a separate test constructs two unseen-label worlds that agree at known audit sites but attain both allowed endpoints. This optimization is **elementary mathematics, not a new estimation algorithm or source-independent scientific discovery**. In particular it targets high absolute log-odds (often seemingly confident scores), which may increase risk of concentrating observations in one part of geographic or covariate space; latitude-balanced version is a deterministic coverage alternative.

## 4. Design-based estimation is an **orthogonal** authority question

Rust `src/design.rs` distinguishes (1) deterministic top-width, (2) theoretical spatially stratified simple random sampling with one site per 16-site latitude group and (3) two sites per such group. Under the *theoretical* random design, first inclusion probability is `π_i=k/16` within each group, second inclusion is `π_ij=k(k-1)/(16·15)` for distinct sites in the same group and `π_iπ_j` across independent groups. One per group has positive `π_i` but zero within-group `π_ij`; this blocks generic unbiased variance estimation across all pairs. Two per group has positive within-group pair probability. The realized 4.95 selection is deterministic, NOT a randomly drawn realization from those mathematical designs.

Exact 2+2-site strata, one sampled per stratum, enumerates all 4 possible equal-probability draws and checks that average Horvitz–Thompson mean equals actual fixed-population mean. A pair of distinct population loss assignments matches sampled values but disagrees on unobserved values, proving that **design-unbiased estimation in expectation is not point identification after one realized draw**. These are classical sampling principles, not a novel MQR unbiasedness theorem. With zero inclusion probability in deterministic top-k on unsampled sites, such a design cannot support an unbiased HT total for arbitrary finite populations.

Prior work:
- Thompson (2012), *Sampling*, unequal probability, DOI `10.1002/9781118162934.ch6`.
- Aronow & Samii (2013), *Variance estimation for the Horvitz–Thompson estimator*, `https://www150.statcan.gc.ca/n1/pub/12-001-x/2013001/article/11831/section2-eng.htm`.
- `spsurvey` software/background, `https://pmc.ncbi.nlm.nih.gov/articles/PMC9926341/`.
- Roberts et al. (2017), spatial/temporal block CV, DOI `10.1111/ecog.02881`.

**External authority contract:** a same-Serov-root label can be valid observed data for this exact 64-site finite target while not granting a new external publication root; a different unverified URL cannot grant independent calibration by declaration. The Rust authority test rejects `SamePublisher`, `UnattestedOtherPublisher` and unverified matching/custody/freezing cases. Its mocked `IndependentlyAttested` constructor in a unit test is an authorization *fixture*, not a cryptographically validated real attestation or actually found external dataset.

## 5. Independent potential data source search: no false admission

A next real candidate to investigate is the **Finnish Biodiversity Information Facility (FinBIF)**, `https://info.laji.fi/en/frontpage/spatial-data/spatial-data-services/`, which documents public occurrence access through `api.laji.fi` and provenance including its collection and source datasets (`https://laji.fi/en/about/3120c1`). Another is GBIF occurrence records, `https://www.gbif.org/citation-guidelines`, where actual downloads have citable persistent DOIs and dataset provenance. **Neither has been downloaded or proven independent or label-comparable here.** A repository URL or portal differs from independent observation root. The precise original Anemone taxon must first be verified against Serov's source metadata, rather than guessing from a common name.

**Critical semantic falsifier:** arbitrary presence records do **not** supply independently verified binary absence labels for the same selected 64 positions, years and observation protocols. Coordinates may be coarsened/hidden; a shared original GBIF record or source collector may be duplicated in FinBIF, GBIF and the Serov CSV. Require taxon and taxonomic concept, site tolerance, observation time/effort, detection/non-detection definitions, observer source IDs, source-collection lineage, selection/inclusion probabilities and target-frame correspondence. Failing any required semantic bridge must yield `EXTERNAL_WITNESS_INADMISSIBLE` rather than seemingly narrower bounds.

## 5A. New original-paper provenance discovery — GBIF candidate shares an upstream root

After P1 closed as a code court, **the original Serov article's Methods were re-read against the published underlying data citations**. Serov et al. (2026), original source [Scientific Reports article](https://www.nature.com/articles/s41598-026-36740-7), under 'Plant occurrence', explicitly says the Finnish plant occurrences from 2000–2024 were **primarily obtained from the Global Biodiversity Information Facility (GBIF)**. It identifies three taxa *Tussilago farfara L.*, **Anemone nemorosa L.** and *Caltha palustris L.*. The bibliography pins its **Anemone nemorosa GBIF occurrence download** to `https://www.gbif.org/occurrence/download/0031144-240626123714530` (accessed 20 July 2024). This original-paper evidence establishes the correct taxon without conjecture and shows a **known upstream GBIF dependence**.

**Consequent evidence-authority correction:** Querying GBIF for *Anemone nemorosa* or re-downloading **the same original 2024 source snapshot** is NOT independent external calibration; it can be a new HTTP/file container of the *same underlying occurrence observations*. A newer GBIF download is not automatically independent either. FinBIF is not presumed independent simply because it is another institution: source records may be contributed to GBIF by FinBIF or its collections, and matching record IDs or source-collection lineage must be audited. Distinct web portals, DOIs, or datasets can all reflect common occurrence ancestry. A fully genuine additional witness requires new independently collected observation units, an independently corroborated detection/non-detection protocol, a source-publication/collection record-ID audit, exact taxon *Anemone nemorosa*, date/site/effort alignment and defensible binary target labels. The original article states its data contained presence and absence records, but this does not itself establish that an arbitrary *external* opportunistic species record supplies a true observed non-detection (0).

**New P2 discriminant:** First fetch original GBIF download/constituent dataset lineage (`0031144-240626123714530`) and check it against any prospective FinBIF source/record keys before promoting independence. If it is merely identical or derived data, record `SOURCE_ROOT_COLLISION`. Direct original GBIF downloadable metadata endpoint was not accessed through available public fetch in this court; only the article's explicit citation was verified. No independent external field calibration is admitted. This provenance result **narrows candidate search** even while 4.95 stays OPEN.

## 5B. Rust original-GBIF-record source-lineage gate, current final CI

Following the article's original GBIF download disclosure, Rust source `experiments/mqr-4.95/src/provenance.rs` was added and wired into `main.rs`. This is an explicit typed **source collision** gate, not a secret new data source. It pins `Anemone nemorosa L.` and the Serov original paper's exact original [GBIF download 0031144-240626123714530](https://www.gbif.org/occurrence/download/0031144-240626123714530). The finite fixture court distinguishes:
- same original GBIF download under any portal name → `ReusedOriginalDownload`;
- different download with overlapping original occurrence record ID → `OverlappingObservationId`;
- different taxon → `TaxonMismatch`;
- wrong original target-frame site/time/effort protocol → `TargetFrameMismatch`;
- no verified observed non-detection/absence → `BinaryNegativeObservationMissing`;
- unknown occurrence ancestry or only a new URL → `SourceAncestryUnresolved`;
- at best, a fully **hypothetically asserted**, duplicate-free, taxon- and protocol-matched specimen may be `CandidateForExternalHumanAuditOnly`, **NOT automatically verified independent calibration**.

Final [CI 37809168246](https://github.com/WhoSia/MQR/actions/runs/37809168246) SUCCESS: **13 Rust unit tests PASS**, original CSV Git blob and original-data same-root label audit PASS; original GBIF parent record source-collision test PASS; original-data finite target risk numbers unchanged from first success. The implemented evidence-type tests use mocked synthetic manifest IDs and do not demonstrate a real GBIF data fetch, live independent metadata audit or actual independent observer record. It is a **falsifier for obvious source-root aliasing**, not positive certification of observation independence.

Final derived ZIP source/artifact receipt in original Drive `02_ANALYSIS_SAFE`: [MQR495-Rust-GBIF-Ancestry-and-Target-Witness-Final.zip](https://drive.google.com/file/d/1vqbO4kcSAAiQrP1ksrBh4_U7hUsJWQFz/view) (3,261 bytes). Previous same-stage result receipt `1vqbO4kcSAAiQrP1ksrBh4_U7hUsJWQFz` supersedes neither historical failing CI logs nor first P1 receipt `198s1pn9cUlQxfDvoO68rjpNmiYuQqcNh`; retain both because the first run captured the P1 state before ancestry patch.

## 6. Current scientific verdict and continuation trigger

**PASS:** real pinned original source, Rust-native model and 64-site label-masking audit, exact finite-label risk bounds and observable contraction, deterministic site-budget mathematical optimum, adversarial world counterexample, Rust type-level claim-scope tests, mathematical pairwise-inclusion and Horvitz–Thompson micro-fixtures, continuous CI/Drive artifact provenance.

**HOLD:** independently acquired external Serov-target positive *and negative* calibration observations, independent publication/source roots, true probability sampled realized field observations, design-based randomization with coverage guarantees, spatial correlation-informed inference, target population risk identification, general adaptive observation design superiority or new mathematical theorem.

**Status: 4.95 remains OPEN**, because the user's question includes independently grounded external calibration, not merely same-source labels deliberately masked then re-read. The next gate is source-authoritative taxon and collection/observation provenance audit, then independent source matching feasibility or a documented impossibility on a fixed target cohort. Avoid endless shallow repeats and do not open 4.96 merely because this Rust code is finished.

**Canonical custody:** Notion MQR one Labs row, page `3c8ef561cf92815693b6fcf6de9955f7`, all 4.95 content as successive sections. CI final run `37808091457`, resulting zip artifact `11563557852`, Drive `02_ANALYSIS_SAFE` result file `198s1pn9cUlQxfDvoO68rjpNmiYuQqcNh`, metadata-verified ZIP 3,031 bytes (logs and bounded derived CSV; no raw full publisher dataset). Previous failing CI logs and correction commits remain recorded.
