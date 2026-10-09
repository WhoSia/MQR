# MQR-4.102 — Adjudication Allocation, Decision-Contrast Identification & Selection-Robust Verification Value

**Formal question opening, 2026-10-09. Research status OPEN.** This version is an organic successor question to, *not forced completion or replacement of*, **MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability**, which remains OPEN. No standalone "P3" research title is minted. GitHub main-only and human commit attribution are retained.

## 1. Why a new formal version, and why not an arbitrary P suffix?

The cross-Lab canonical [Flowing Versioning, Question Migration & Continuous Genealogy](https://app.notion.com/p/3f4ef561cf92818da4d4d92bc949ca15) states that a version records a **moving primitive question**; open a successor upon a change of its object, contradiction, or intervention target, without requiring predecessor closure. [CUBE-REV 0.17](https://app.notion.com/p/3f4ef561cf92811e8da1dde0478bfd1e) explicitly applied it while CUBE-REV 0.16 remained OPEN. The older [Generation ≠ Version](https://app.notion.com/p/3c4ef561cf92813b9204c3346f453820) further distinguishes numbered versions from changes of scientific generation. The shared Research OS doctrine treats version count as **not** information gain.

- **MQR origin:** scientific observations and measured quantities do not inherit philosophical meaning, identity or authority merely from formal encoding; the question is what finite observation and intervention actually distinguish.
- **4.36–4.53:** tested restrictions on universal scalar progress; narrowed survivals include Fisher–Rao and Blackwell in appropriate, non-universal contracts, and 4.53 closed the scalar-progress overreach.
- **4.90–4.99:** source- and population-dependent identifiability/risk; effort, zero truncation, occupancy vs detection and correct origin data become consequential. Archived code and independent repository tests are *reproducibility conditions*, not novel science.
- **4.100:** how actual auxiliary observation channels refine observational equivalence; EDI/Penguin, UCI sensors, Clemson and PhysioNet QTDB established source lineage and empirical paired observations **only under their operational definitions**.
- **4.101:** criteria by which *fallible, selectively supplied reference labels* could license absolute error-risk claims. Actual 487 selected QTDB beat opportunities, only 402 pairs, with 76 artificial-threshold disagreements. No external truth certificate; true risk still [0,1].
- **4.102 new object:** **finite budget of external adjudications as an intervention**. For a declared loss functional, which observed cases should be independently reviewed to shrink the *identified set* fastest, and how do different target weights and nonrandom selection change the audit's value? This is scientifically distinct from merely tightening another 4.101 error cap.

Explicit inheritance edge: 4.101 supplies fallible labels and no-truth authority firewall; 4.102 changes **which observations to obtain** and **which risk contrast to identify**. Does NOT claim a new generation, new mathematical theorem, completed 4.101, or actual third-expert review.

## 2. Same original source and exact target restriction

Use **exactly** \`experiments/mqr-4.101/p8_publisher_verified_487beat_receipt.csv\`, SHA-256 \`d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842\`, derived from prior actual [PhysioNet QTDB](https://physionet.org/content/qtdb/1.0.0/) human-reader files, audited in MQR-4.100 P8 and MQR-4.101. 11 source ECG records, 487 first-expert selected beats; **402** selected beats have both expert QT measurements, **85 do not**. Nonclinical illustrative decision threshold **440ms** (NOT medical recommendation).

On **only the 402 complete pairs**, define observed two binary decisions \`h1_i=1[qt1>=440]\` and \`h2_i=1[qt2>=440]\`; their observed disagreement indicator \`d_i\` is known. Ground truth \`T_i\` is **completely unobserved**. Source-observed agreement = **326**, disagreement = **76**. Missing second reader is concentrated in \`sel102\` (83 of the 85 absent) and \`sel213\` (2 absent); no evidence justifies missing-at-random or transport beyond these selected source beats.

**Do not conflate these targets:**
- **Absolute finite error** \`R_T(h1)=402^-1 Σ 1[h1_i ≠ T_i]\` on selected complete pairs.
- **Paired finite decision contrast** \`Δ_T=R_T(h1)-R_T(h2)\` on **the same 402 pairs**.
- A contrast on all **487** is **not a defined observable policy comparison**, because second-reader predictions do not exist for 85 cases. If one defines a hypothetical extension \`h2^ext\` there, disclose it separately; assigning values does not make them original expert observations.
- Source empirical quantities are NOT calibrated future-patient risks, causal intervention effects or clinician accuracy. Selected records are not a representative random population.

## 3. Established elementary sharp mathematics: why disagreement targets are special

Let \`D={i:h1_i≠h2_i}\` have 76 elements, \`G\` have 326. For \`i∈G\`, \`1[h1_i≠T_i]-1[h2_i≠T_i]=0\` **for any T**. For each \`i∈D\`, the difference is \`+1\` or \`−1\`, independently free unless actual third-party truth certificates impose additional restrictions.

Thus the sharp finite range:
\`Δ_T∈[-76/402,+76/402]=[-18.9055,+18.9055] percentage points\`.
For absolute risk, \`R_T(h1)∈[0,1]\` with no truth evidence. Observed agreement, independent annotator identities, or the code's validation status do not narrow it.

**Hypothetical ten genuine external truth checks**: If exactly \`s\` of 76 disagreements are verified and their **actually observed** signed contribution is \`S_s\`, then
\`Δ_T∈[(S_s−(76−s))/402,(S_s+(76−s))/402]\`.
These endpoints are sharp. In particular, ten \`D\` verifications imply identified-set **full width 132/402=32.836%p**, versus original \`152/402=37.811%p\`; center \`S_10/402\` is **not known** and is NOT fabricated. Ten \`G\` verifications imply no contraction in **this contrast**. Ten independent truly verified \`T\` labels anywhere reduce the absolute-risk uncertainty width only from \`402/402\` to \`392/402\` unless additional true-world constraints exist. No such independent validation has actually occurred.

**Uniform ten from 402 without replacement:** exact expected observed disagreement count \`E[s_D]=10·76/402=1.8905472637\`. Expected contrast interval width \`(152−2 E[s_D])/402≈36.870%p\`, conditional on eventual fully accurate reviews and source-fixed selection; this is mathematical design expectation, NOT an unbiased population-risk estimate and not an enacted random audit.

**Fallible third-party review:** if \`s\` observed disagreement cases were additionally reviewed, their recorded signed contrast \`S\` contains \`p\` positive and \`n\` negative signs, and an independently authenticated review-error cap \`k\` existed, sharp bounds are
\`[(S−2min(k,p)−(76−s))/402,(S+2min(k,n)+(76−s))/402]\`.
When \`k\` is not certified, reviewer outputs do not have authority to shrink the true identified set. No such error cap or true review sign has been acquired.

The arithmetic follows classic finite Hamming-label comparisons. The present contribution is **a source-grounded choice-of-information target and negative evidence-accounting audit**, NOT an original identification theorem.

## 4. Why source selection changes the apparent value of one adjudication

Observed discordances by actual first-party ECG record (target = *complete pairs only*):

| Record | Paired beats | Discordant | Second-reader incomplete |
|---|---:|---:|---:|
| sel100 | 30 | 0 | 0 |
| sel102 | 2 | 0 | 83 |
| sel103 | 30 | 4 | 0 |
| sel114 | 50 | 9 | 0 |
| sel116 | 50 | 0 | 0 |
| sel117 | 30 | 13 | 0 |
| sel123 | 30 | 9 | 0 |
| sel213 | 69 | 3 | 2 |
| sel221 | 30 | 3 | 0 |
| sel223 | 31 | 26 | 0 |
| sel230 | 50 | 9 | 0 |
| **Total** | **402** | **76** | **85** |

\`sel223\` contributes 26/76 paired binary disagreements; \`sel102\` contributes zero such discordances despite 83 missing second-reader labels. This *observed selection pattern* motivates contrasting two audit targets, **not a causal diagnosis of why labels were absent**.

- **Beat-pooled Δ** gives every one of the 76 discordances equal full-width benefit \`2/402\` of truth adjudication, wherever located. Any 10 discordances are equivalent for the *set width*.
- **Equal-record Δ** (each of 11 records has 1/11 weight; each observed pair within a record 1/n_r) gives reviewed discordance in record r full-width benefit \`2/(11 n_r)\`. Initial equal-record bound is \`[-0.2008049641,+0.2008049641]\`; selecting ten disagreements from 30-pair records contracts its total width by \`2/33≈0.0606061\`, vs the 31-pair or 50/69-pair records yielding different values. A strictly count-based method that always starts with sel223 because it has most disagreements need not optimize equal-record-weighted identification value.
- Neither beat-pooled nor equal-record weighting transports 11 selected ECG records to all 105 QTDB records, let alone patients; their unit, selection and intended loss differ.

The ideal objective here is **worst-case identification-set width conditional on actually certified truth**, not realized Bayes improvement, predictive accuracy, clinical utility, a prospective active-learning experiment, or value-of-information in dollar units. A two-annotator disagreement is a rational selection cue only **for this contrast**; for absolute error risk, direct third-party information targets all cases equally absent other restrictions.

## 5. Falsification and research obligations

1. **Correctness:** verify every actual row, original 487-byte source hash, record strata and two labels with independent Python/Rust reading; brute-force small finite binary worlds for claimed sharp endpoints. The two implementations share one original source; this is reproducibility, not independent ground-truth corroboration.
2. **Selection robustness:** retain per-record n_r and observed disagreement; report separately matched-pair-only target and 487 source-opportunity target with unknown h2 actions, and withhold MAR assumptions without data.
3. **Decision comparison versus absolute risk:** never use observed proxy disagreement as evidence of true clinical error; never relabel one reader as infallible.
4. **Future world contact:** legitimately independently review prechosen discordant and matched concordant subsets while keeping reviewers blind where possible, verifying sampling strata and independent source and output; no review is claimed here. Retrospective selection based on observed disagreements must be acknowledged.
5. **Genealogy:** 4.101 remains OPEN and owns fallible-reference error certification and selective adjudication; 4.102 owns the distinct new **verification-allocation** scientific question. No cosmetic CI fix or substage name is a separate version.

**Current execution status at first writing:** exact finite mathematical/source target specified; GitHub Action result NOT YET WITNESSED. Therefore \`FORMAL_ALLOCATION_PRESEAL\` and \`WORLD_TRUTH=HOLD\`. 4.102 is officially OPEN, not scientifically closed.
