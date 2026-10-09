# MQR-4.101 — P1 Internal Court: Fallible-Reference Truth Risk and Selective Coverage

**Not an additional formal research title.** Official name: *MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability.* P1 **CLOSED BOUNDED / real derived-source binary annotations and elementary mathematical risk interval exhaustively checked; true reference error and target population still HOLD**. MQR-4.100 P8 original-source custody and complete-pair disagreement court remain CLOSED BOUNDED, not magically replaced.

## 1. Source and comparison

Use the exact 487-row `p8_per_beat.csv` emitted from authentic first-party PhysioNet QTDB v1.0.0 original files and independently archived as part of P8. Source artifact: [MQR 4.100 P8 original and receipts in Drive](https://drive.google.com/file/d/1_0oF1hlmi1u7W2Jravjt7QjuiyZ4qTjR/view) and [P8 source hash CI](https://github.com/WhoSia/MQR/actions/runs/37914228677). Exact P8 derived CSV SHA-256: `d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842`. No record gets an invented QT value; 402 paired full QT intervals and 85 unmatched/incomplete opportunities from 11 selected recordings. `q1c` and `q2c` are distinct expert annotations, not certified independent errors or a clinical truth standard. Source document: [PhysioNet QTDB](https://physionet.org/content/qtdb/1.0.0/), DOI 10.13026/C24K53; original source is ODC-By v1.0. The derived CSV is separately pinned for deterministic proof-contract regression; it is **NOT itself a fresh 77-file publisher download**.

Define binary decisions `h_i(c)=1[QT_{1i}≥c]` and fallible proxy reference `a_i(c)=1[QT_{2i}≥c]` where both QT values were measured. Probe `c ∈ {400,420,440,460,480} ms` deliberately as a **nonclinical discretization sensitivity**; none is validated as a disease diagnosis threshold. Target = only the same 487 reference-beat opportunities.

## 2. Real observed disagreement, by arbitrary cutoff

| Source-conditioned artificial QT cutoff | Paired complete | Reader-1 vs Reader-2 different | Observed paired disagreement | k=0 pooled true-risk bound **only if reader 2 perfect on observed** |
| --- | ---: | ---: | ---: | ---: |
| 400ms | 402 | 88 | 21.89% | [88,173]/487 = [18.07%,35.52%] |
| 420ms | 402 | 76 | 18.91% | [76,161]/487 = [15.61%,33.06%] |
| 440ms | 402 | 76 | 18.91% | [76,161]/487 = [15.61%,33.06%] |
| 460ms | 402 | 66 | 16.42% | [66,151]/487 = [13.55%,31.01%] |
| 480ms | 402 | 42 | 10.45% | [42,127]/487 = [8.62%,26.08%] |

**Distinct event definitions:** there happen to be 88 pairs with a **continuous absolute QT difference ≥40ms** in P8 and also 88 pairs whose **binary 400ms labels cross the threshold** here. The 88 events are not assumed identical: these are different indicator functions. No medical inference follows.

## 3. Sharp identification contract and sensitivity

For a prediction h for all n cases, fallible reference A on exactly m cases, source-observed e mismatches, and an **additional known external upper bound k on wrong observed reference labels**, any potential truth vector T consistent with that certificate satisfies

`L=max(0,e−k)/n`, `U=[e+min(k,m−e)+(n−m)]/n`.

- Among e currently disagreed labels, up to k may be wrong and correcting them can reduce h's errors by at most min(k,e). On the m−e currently agreed labels, up to min(k,m−e) could be jointly wrong. Every unobserved truth can disagree with h at most once.
- The lower endpoint is **attained** by flipping min(k,e) currently disagreed reference labels to h and completing unobserved T=h; the upper endpoint is **attained** by flipping min(k,m−e) currently agreed reference labels against h and completing every missing T≠h. For each k both constructions keep the observed decisions and the available two-expert reports exactly fixed. This is elementary sharpness by construction (known partial-identification algebra, not a new theorem).
- If no external error certificate exists, k=m is feasible and the bounds are **[0,1] for true h-vs-T risk**, regardless of apparent reviewer consensus. Under the unverified condition “reader 2 perfect on all its 402 observed labels,” the k=0 [15.61%,33.06%] example at cutoff 440 is an *assumption-conditional sensitivity interval*, not a measurement of actual clinical risk.
- Under a **hypothetical externally validated** k=10 mistake budget at cutoff 440, `[66,171]/487 = [13.55%,35.11%]`; P8 did not supply such a certificate. The two human annotators' observed agreement does not identify k.
- A true clinical target, even the existence of a single unambiguous “QT truth,” and an externally representative population are NOT established by binary thresholding one lab's chosen annotations.

Brute-force tests of all finite binary truth completions for each observed pattern and candidate classifier through n≤5 cover **39,190 exact cases**, validating endpoint attainability. An independent Rust finite-model test checks n≤6 and a separate Rust receipt reader checks all 55 record × cutoff rows. Passing code tests only verifies this declared proof-contract, not original novelty or externally assessed T.

## 4. Reference selection and target weighting actually matter

The original 487 selected beats are unevenly distributed between 11 recordings, and `q2c` coverage is highly nonuniform. Equal weight to each ECG recording is a **different finite functional** from pooled beat weight.

At cutoff 440 under k=0, **beat-pooled** risk sensitivity range is `[0.15606, 0.33060]` while **equal-record weighted** range is `[0.20069, 0.29202]`. Neither is a confidence interval or transport to real patients. No information determines which target weights should be used for future patients. A nonrandom set of 11 records with q2c access cannot be silently promoted to a distribution over the full 105-record QTDB, much less a hospital population.

## 5. Negative controls, limits, future proof obligations

1. **Truth-construction counterexample:** Fix absolutely every observed `(h,reader1,reader2,S)` and set latent T=h on all 487. Then true risk 0. Alternatively set T=1−h on all 487; true risk 1. Both worlds have exactly the **same observed annotations and selection pattern**, because no link to T was assumed. Statistical source-linked paired judges do **not** remove this nonidentifiability.
2. **Not independent:** two independently identified experts read the same ECG, often with shared fiducials/annotation instructions; statistical independence and blinded assessment were **not verified**. Never estimate a missing external k from an independence assumption not checked.
3. **No causal adjudication story:** the source says which cases have 2nd-pass annotation, not why. Missing at random, physician-level confidence, or selective review policies are not established.
4. **No risk ranking from two overlapping intervals:** even two hypothetical bounded marginal loss intervals do not by themselves establish a robust preference unless all admissible worlds yield the ordering; strictly nonoverlapping intervals are sufficient but not necessary.
5. **Prior art:** label misclassification bounds (Manski and related work), selective labels, imperfect reference-standard diagnostic performance, and exact binary Hamming counting predate MQR. P1 is a clean example tying selection + false adjudication + risk to real author-separated source files, not an original theorem.

Follow-ups: source-authentic third review, traceable independent error-certification, and a specified target population/decision loss. Do NOT claim P1 answers unknown latent QT truth or medical accuracy. The older MQR 6 historical chat exists at https://chatgpt.com/g/g-p-6a8e7e61cb3c8191b6afc475b21a5d82-mqr/c/6aa77eff-25d0-83ee-9ff7-0fc88cc6efc8 ; the failed export is not evidence that the original chat disappeared.

## 6. Executed independent CI and failure provenance

- **Actual GitHub CI [#37917143944](https://github.com/WhoSia/MQR/actions/runs/37917143944): SUCCESS**, running on human-authored implementation commit `6c063cfff67805554e99c57d5d89d5fbf3d066f0`. Python verifies exact known-P8 487-row CSV SHA-256, re-computes 400/420/440/460/480 threshold-disagreement totals, and brute-forces **39,190** small finite truth-completion test cases for endpoint sharpness. Rust separately checks its n≤6 finite truth models and the actual **55** selected-record × cutoff receipt rows. No new expert judgement or full publisher ECG download occurred in this P1 CI; source ancestry remains the checksum-verified P8 corpus.
- **First CI [#37916855181](https://github.com/WhoSia/MQR/actions/runs/37916855181): FAILED** in Rust because the receipt test accidentally initialized all five expected cutoff keys as 400. Python and Rust theorem tests already passed. The program was repaired with distinct expected 400/420/440/460/480 keys, and **the second full CI passed**. Failure remains visible; it does not prove the original physical observations wrong.
- Successful run's artifact **11610685413**, `MQR4101-P1-Selectively-Observed-Fallible-Reference-Risk-Receipt` (artifact outer ZIP SHA-256 `8c60347ca5ec8079413df83d1130f7711adc44ff43139662bf6c53bc895e4ed2`) retains computed JSON/CSV and Python/Rust execution logs.
- Drive canonical source-replay package: [MQR4101-P1-Founding-Source-Math-and-Replay.zip](https://drive.google.com/file/d/1bWi8UR0P2N5_p2z657hJYLIPX_bS92Sb/view) under `MQR/02_ANALYSIS_SAFE`. Official charter [Drive `00_GOVERNANCE`](https://drive.google.com/file/d/1GRKLOswau8lFNCtbF5iuEKSPw_p1APeb/view) and P1 court [Drive `03_REPORTS_COURTS`](https://drive.google.com/file/d/1V9eUWgFouBjwQlnm7rSgZfx5dg4qsgwX/view). Original P8 human annotation source remains a separate full original-source archive; the P1 package carries derived rows and their provenance, not another reference truth.

**P1 CLOSED BOUNDED:** real reference-disagreement source conditionality plus known sharp *hypothetical external-k* error bounds established; **external k certificate, latent true QT, general population risk and accuracy ranking HOLD**. MQR-4.101 overall OPEN; title unchanged.

