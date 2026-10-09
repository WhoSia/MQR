# MQR-4.103 — Adaptive Verification, Evidence-Feedback Dependence & Sequential Identifiability

**FORMAL VERSION OPEN, 2026-10-09.** The name is a research question, **not** evidence of a novel theorem. MQR-4.102 remains OPEN with P2 CLOSED BOUNDED; it is not silently closed or renamed.

## P1: exact finite adversarial court

Move from a fixed allocation to a sequential policy. Three binary *latent* truths (T=(T_0,T_1,T_2)). First inspect (T_0). The next inspection is (T_1) if (T_0=0) and (T_2) if (T_0=1); stop at two examinations. All examinations in this mathematical court are **assumed perfect**; no QTDB third-party truth is actually available.

The complete recorded evidence is the first outcome, the second **selected index** and value, and stop time. There are eight possible latent truth vectors, but only four distinct evidence histories. Each observed history admits exactly two worlds differing in the **uninspected** bit; their finite-population true positive fraction (R(T)=(T_0+T_1+T_2)/3) differs by exactly (1/3). The full deterministic decision rule is known in both worlds. Therefore **selection-rule transparency does not, by itself, point-identify the full-population parameter**.

This is *not* a proof that adaptive selection necessarily causes bias. If the scientific target is only the first case's truth, it is perfectly observed; if inspection covers all relevant cases, its finite target becomes known. If stochastic sampling uses known strictly positive probabilities for every eligible case and sufficiently justified truthful outcome measurement, design-aware unbiased estimators may be available even with adaptive sampling. Realized sample-path identifiability, design-unbiasedness, and point identification of a superpopulation distribution are different claims.

## Separate optional stopping counterexample

Let independent fair (X_1,X_2\in\{0,1\}) be equally likely, stop after the first sample if (X_1=1); otherwise observe two. Exactly enumerate four two-coin worlds. The expected **naive stopped sample mean** is (5/8\), even though each observation's mean is (1/2). The expected stopped **centered sum** (\sum_{i\le\tau}(X_i-1/2)) remains zero. This illustrates why optional stopping does not imply every stopped statistic is invalid and why one cannot replace martingale/valid-stopping conditions with the phrase “sequential data are biased.”

The example isolates **result-dependent stopping** from item-specific adaptive allocation; it does **not** involve uncertain expert labels. A separate scenario with known allocation, missing independent adjudications, or verification positivity failures can fail for different reasons.

## Identification ledger and lineage

- **Selection-history known:** observed index, first and second outcomes, stopping time.
- **Verification oracle:** purely hypothetical correct binary truth readout; no real clinical validation.
- **Nonidentification mechanism:** one of three units receives zero realized inspection under the chosen observed history. Even perfect accuracy on selected units cannot fill the missing value without additional assumptions.
- **Optional-stopping mechanism:** sample denominator `tau` depends on the observed first result; the stopped average is not the same estimand as the original per-draw mean in expectation.
- **Measured source:** these are exhaustive **synthetic finite models** and must not be attributed to QTDB raw ECG or real adjudicators.
- **Novelty and source limitations:** finite selective verification, inverse-probability correction under positivity, missing-not-at-random observations and optional-stopping martingales have extensive prior literature. Novel theorem status: **NO CLAIM**. Literature audit to compare selective verification and sequential clinical adjudication remains OPEN.
- **4.102 reuse:** prior real QTDB receipt was 487 selected beats, 402 complete two-expert comparisons, 76 disagreements, 85 incomplete pairs; the supposed capacity 3 per record and third-party audits 10 were hypothetical. Do **not** quietly use them as realized third-expert truth, and do not call the P1 toy model an empirical QTDB validation.

**Execution contract:** `experiments/mqr-4.103/src/main.rs` exhaustive eight worlds and four optional-stop histories; no dependencies. `.github/workflows/mqr-4.103-p1-sequential.yml` must show actual success before P1 CLOSED BOUNDED. README records the formal title and OPEN/HOLD limits.
