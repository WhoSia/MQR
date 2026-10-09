# MQR-4.103 — Adaptive Verification, Evidence-Feedback Dependence & Sequential Identifiability

## Internal P2 — Zero-Support Selection, Positive Designs, and Fallible-Reference Identification

**Status: OPEN — exact finite mathematics Python-verified and Rust CI #37948140071 SUCCESS; final P2 source-custody CI and archival closeout pending.** This is **P2 inside 4.103**, not a new MQR version. The model is entirely synthetic; the PhysioNet QTDB source does not contain independently verified third-expert truth.

### Primitive target and observation contract

Fix three units with latent truth `T=(T0,T1,T2) in {0,1}^3`; target finite prevalence `R(T)=(T0+T1+T2)/3`. A stable, error-prone binary reviewer outputs `A_i=T_i xor E_i` when inspected. Let `H` record ordered inspected indices, corresponding `A` values, known conditional selection weights and stop time. At stage one inspect unit 0. At stage two choose one among units 1 and 2, then stop at exactly two inspections.

- **D0 (deterministic)**: if `A0=0`, inspect unit 1; if `A0=1`, inspect unit 2. The nonfavored unit has inclusion probability **0**.
- **D+ (positive randomization)**: given `A0`, choose the favored unit with probability **3/4** and the alternative with probability **1/4**. The first unit has probability 1. All conditional probabilities are known, design-exogenous *given recorded first-stage information*.
- Truthful oracle subcourt: `A=T` (hypothetical); fallible subcourt: `A=T xor E`, with no stochastic independence assumptions and no certified restriction on `E` unless explicitly declared as a counterfactual budget.
- No second-stage outcome is observed for the nonselected unit; one observed sequence does **not** equal the law over all possible sequences. This model always stops after two examinations, so optional stopping is not conflated with adaptive target selection. P1's separate stopped-average experiment is unchanged.

### Result 1 — zero versus positive support

Exhaust all 8 possible fixed `T` vectors under a perfect oracle, recording the entire *probability law over histories*, not merely the realized history.

- D0 yields exactly **4** distinct laws, with **2** truth vectors in every equivalence class. Their population prevalence differs by **1/3**. No statistic of these observable histories can be design-unbiased for the full finite total across both indistinguishable vectors, because their observation laws are identical while their target totals differ.
- D+ yields exactly **8** distinct laws: in this finite stable-oracle model every possible `T` has a distinct full law. This is law-level *structural identification*, not a guarantee that a single realized two-review path point-identifies `T`.
- For example, even under D+, the observed receipt `(A0=1, selected index=2, A2=1, stop=2)` with a perfect oracle permits totals **2 or 3**. Its sharp finite prevalence set is `[2/3,1]` (discrete values `{2/3,1}`). Each endpoint is attained by selecting a different unseen `T1` with the same observed receipt.

### Result 2 — exact Horvitz–Thompson identity under the oracle

Under D+ and truthful labels define `pi_0=1`, and conditional on the observed first label, `pi_favored=3/4`, `pi_alternative=1/4`. With second-stage selection indicator `I_i`, the design-based finite-prevalence estimator is

```text
R_hat = [T0 + I1*T1/pi1 + I2*T2/pi2]/3.
E_D+[R_hat | fixed T] = R(T).
```

For each of **all 8 fixed truth vectors**, exact integer arithmetic computes the expected *total* times 12 as `3*(3*T0+4*Tfav)+(3*T0+12*Talt)=12*(T0+T1+T2)`. This is a finite instance of **existing Horvitz–Thompson design theory (1952)**, not a new general theorem or a true-label empirical result. It neither certifies error-free `A` nor makes the one realized path point-identifying. A stopped or randomly normalized observed average need not share this expectation.

### Result 3 — reference error reinstates an independent failure

For D+ on fallible observed `A`, both latent worlds `(T=000,E=000)` and `(T=111,E=111)` produce stable `A=000` and the **same full probability law over all recorded histories**, but their true prevalences are 0 and 1. Thus positivity only identifies the **reviewer's labels** in the law-level stable-label model. With completely unconstrained `E`, population *truth* is **not identified even in the full observational law**, despite positive probabilities.

Suppose **hypothetically and externally** that at most `k` of the 3 reviewer labels disagree with truth. For the *same realized receipt* `A0=1, index2, A2=1`, exact enumeration over all `8 truth x 8 error` assignments yields sharp true-total possibilities:

| Authorized hypothetical error budget | Possible totals | Prevalence range |
|---|---|---|
| `k=0` perfect reviewer | `{2,3}` | `[2/3,1]` |
| `k<=1` independently warranted | `{1,2,3}` | `[1/3,1]` |
| No external certification | `{0,1,2,3}` | `[0,1]` |

With the complete D+ law identifying **A=111**, the hypothetical `k<=1` sharp true totals narrow to `{2,3}`; without a certified bound the totals still range from 0 to 3. Full-law identification and one-history partial identification must not be substituted for one another. All listed bounds are sharp by existence of assignments in exhaustive enumeration, **not continuous population confidence intervals**.

### Stress test — positivity does not control finite-design variance

The same D+ policy and the **same true prevalence** `R(T)=1/3` can produce very different design variances, even with a hypothetical perfect reviewer. Take `T0=0`, so unit 1 is favored (selection probability `3/4`) and unit 2 is the alternative (probability `1/4`).

- World `T=(0,1,0)`: the sole true item is favored; `R_hat=4/9` with probability `3/4`, otherwise 0. Exact expectation `1/3`, design variance **`1/27`**.
- World `T=(0,0,1)`: the sole true item is disfavored; `R_hat=4/3` with probability `1/4`, otherwise 0. Exact expectation `1/3`, design variance **`1/3`**: a **ninefold increase**, even though all inclusion probabilities remain positive and both worlds have identical prevalence.
- For a one-positive-case population with `T0=0`, if the true item's inclusion probability is `q>0`, the HT prevalence estimator equals `1/(3q)` when selected and 0 otherwise. Therefore `E[R_hat]=1/3`, but `Var(R_hat)=(1-q)/(9q)`, diverging as `q` decreases to zero. Values of `R_hat>1` are possible: it is an unbiased *inverse-weighted estimate*, not a realized proportion constrained to the unit interval.

Exact rational arithmetic using independent Python `fractions.Fraction` confirmed the `1/27`, `1/3`, and `(1-q)/(9q)` identities. **This variance stress test is a local analytical supplement, not yet a separately compiled Rust CI variance claim.** It is classical unequal-probability sampling mathematics, not a general MQR novelty claim. It strengthens the method court by separating *support*, *identification*, *unbiasedness*, *precision*, and *truth validity*.

### Prior-art and source audit

- Horvitz, D. G. & Thompson, D. J. (1952), *A Generalization of Sampling Without Replacement from a Finite Universe*, JASA 47(260), 663–685. DOI: https://doi.org/10.1080/01621459.1952.10483446. Original publisher abstract documents unequal-probability design theory; the finite identity here is an application.
- Begg, C. B. & Greenes, R. A. (1983), *Assessment of Diagnostic Tests When Disease Verification Is Subject to Selection Bias*, Biometrics 39(1), 207–215. DOI: https://doi.org/10.2307/2530820. Its verified abstract establishes selection-biased verification as longstanding prior art.
- Heitjan, D. F. & Rubin, D. B. (1991), *Ignorability and Coarse Data*, Annals of Statistics 19(4), 2244–2253. The source abstract formulates conditions on coarsening and ignorability. **Not yet a full-text, line-by-line literature adjudication.**
- Existing original QTDB source: https://physionet.org/content/qtdb/1.0.0/. Prior MQR receipt has 487 selected beat opportunities, 402 complete paired expert decisions, 76 disagreements, 85 incompletes, and **zero independently certified third-reader truths**. These counts are lineage context; they are not used in this synthetic P2 enumeration.

### Executable contract and current scientific disposition

- P1 source remains `experiments/mqr-4.103/src/main.rs`. New bounded P2 implementation is `experiments/mqr-4.103/src/p2.rs`, imported into the same Rust executable. Five new Rust unit tests cover support classes, 8/8 exact conditional design expectations, single-history partial identification, hypothetical error-budget sharpness, and reviewer-error observational equivalence.
- An independent Python enumeration reproduced four versus eight laws, the `[2,3]`, `[1,3]`, `[0,3]` one-history totals, and the HT identities. **P2 Rust source CI #37948140071 SUCCESS, 8/8 unit tests; independent full run-log verification complete.** Never label a commit itself CI SUCCESS.
- Claims held: genuinely accurate clinical reviewer; external 1-error certificate; newly acquired QTDB third expert; original survey design/inclusion probabilities for QTDB; population transfer; novelty of inverse-probability methods; general sequential optional-stopping theorem.

**P2 remains OPEN pending full-source custody workflow and archival readback. Internal Rust finite mathematics has been verified in actual CI; full-world empirical truth and transport still HOLD. MQR-4.103 remains OPEN.**

### First actual CI and Drive run-log receipt

- Actual [GitHub Actions #37948140071 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/37948140071), code commit `d49a95fdcd6dae13e6234db95421689530603f84`. Logs verify 8/8 Rust unit tests (three P1, five P2) and all P2 markers.
- The first-run ZIP contains `p1-run.log` with **both P1 and P2 stdout**, although its early workflow artifact name still mentions P1. CRC and observed stdout verified locally.
- GitHub artifact SHA-256 `b368ced802a21a513393c46c7873d2c8459bf8462096197746bd58ec9de4b1fe`; 539 bytes. Preserved in [Drive MQR/02_ANALYSIS_SAFE](https://drive.google.com/file/d/1tOk5CwjaktBaXACAeq-soFBWbuf6X6up/view) and re-downloaded with matching SHA-256 and ZIP integrity.
- [Separate full-P2 source-custody workflow #37948743557](https://github.com/WhoSia/MQR/actions/runs/37948743557) includes `p2.rs`, both court documents, `main.rs`, Cargo manifest, workflow, README, commit receipt and SHA-256 manifest; this *separate run must still be checked* for success and Drive transfer before P2 bounded closeout.


### P2 final bounded scientific disposition and Flowing successor edge

**P2 CLOSED BOUNDED — synthetic finite-design mathematics, executable reproducibility and source custody. Overall MQR-4.103 remains OPEN.** [Final full-source GitHub Actions #37948743557](https://github.com/WhoSia/MQR/actions/runs/37948743557) **SUCCESS** at human-authored source commit `a9b677029014aad4d44cc007e6d24f0f7c699528`: 8/8 Rust unit tests, both P1/P2 stdout markers, complete source-custody step and upload-artifact steps succeeded. Its immutable GitHub outer artifact has SHA-256 `4d9ff80190dfe072e434ab73b93f302c446ea6290472ea95351b2cc0c14a3077`, 31,650 bytes, and is [preserved in existing Drive MQR/02_ANALYSIS_SAFE](https://drive.google.com/file/d/1cRwlurkKp1u3RDOfJY7gbv6hEBEO5Ej2/view). After Drive re-download, both outer and nested ZIP had no CRC errors; inner custody lists Cargo.toml, both P1/P2 court documents, README, SHA256SUMS, commit.txt, main.rs, p2.rs, and the workflow file. P2's later variance paragraph was added *after* this source-commit and does not inherit this workflow's frozen proof/receipt.

**Inherited scientific HOLD:** there are zero independently certified QTDB third-expert truth reviews, no independently warranted error budget, no measured sequential prospective policy, no validated clinical decision-risk improvement, no evidence of novelty for HT/verification-bias/optional-stopping results, and no cross-population transfer. P2 has not identified actual QTDB truth simply by counting or obtaining positive sampling weights.

**Flowing Versioning decision:** the next primitive question should move from *what a fixed adaptive verification design can identify assuming a given truth/error certificate* to *how an actual verification protocol might earn, allocate, and independently audit fallible truth certificates while controlling selection and drift*. This changes the **object of intervention** from inclusion probabilities and formal identified sets to real validation witnesses, certificate provenance, and verification protocol. This is a **successor naming proposal only**, not opening 4.104, and it must preserve all 4.103 external-truth HOLDs.
