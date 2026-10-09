# MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability

**Official formal MQR-4.101 title. Confirmed by user 2026-10-09.** The title is *the generation's* name; P0/P1/P2 etc. are internal audit stages, **never separate formal research titles**. GitHub `main` is the sole live branch; use a human WhoSia commit attribution, do not assign bot-authored commits. Existing MQR-4.100 P8 is CLOSED BOUNDED for original annotator provenance and a missing-pair disagreement bound. Do not retroactively convert that into source-independent accuracy or full 4.100 theory closure.

## Primitive object and target

Let a finite index set `i ∈ {1,...,n}` represent a **declared target population** (initially the 487 selected QTDB reference beat opportunities across 11 available recordings). Fix a binary decision rule `h_i ∈ {0,1}`, two separately reported imperfect standards `A_i,B_i ∈ {0,1}` where available, a label-selection variable `S_i ∈ {0,1}`, and latent target truth `T_i ∈ {0,1}`. Their observational meaning, origin, shared dependencies and sampling must be specified. A continuous QT interval may be converted into **an artificial threshold probe**, not a clinical decision or known disease state. Define the finite **true 0–1 error** `R_T(h)=n^{-1} Σ 1[h_i != T_i]`. This is not an estimated population Bayes risk.

This generation asks: which auxiliary measurements, external error certificates, adjudication designs and target-population restrictions actually shrink `I(R_T(h)|O,assumptions)`? Which apparently plausible assumptions (e.g. two humans, agreement rate, separate annotation filenames, duplicate annotations, convenience sampling, nominally independent devices) do *not* identify it? What happens to risk comparisons when selective adjudication and errors share latent causes?

## Separation gates

1. **Observation gate:** first-party SHA-pinned raw files, per-annotator identity and record selection, complete vs incomplete pairing; no invented reference for a missing beat.
2. **Reference authority gate:** independent expert identity ≠ independent measurement errors ≠ validated true labels. Model the externally certified *number* `k` of fallible-reference mistakes explicitly; a hypothetical `k` may be used for sensitivity but must not be fitted from inter-annotator agreement alone.
3. **Sharpness gate:** produce attainability constructions, not merely an inequality; exhaustive discrete checks and (when economical) Lean for any claimed abstract theorem.
4. **Decision gate:** declare the event, the action `h`, bounded loss, whether it is hypothetical or deployable, the target unit/weights and each unknown reference-label location. A deterministic source-conditioned disagreement is not an externally established true error.
5. **Transport gate:** give the matching population/sampling/selection conditions. Source-weighted and equal-record-weighted fixed-set quantities differ even before transporting to new patients or recording sites.
6. **Novelty gate:** partial-identification bounds and imperfect gold-standard problems are well-established (Manski and related literature). A PASS can certify an honest audit without claiming a new theorem or new medical data.

## Initial P1 court (open at charter, close only on CI)

For `m` observed fallible reference labels, `e` observed disagreements against `h`, and **externally certified** at most `k` wrong reference labels among `m`, the sharp finite count bounds are

`max(0,e-k) ≤ Σ 1[h_i != T_i] ≤ e+min(k,m-e)+(n-m)`.

The two endpoints are simultaneously attainable by flipping the admissible labels in observed disagreements/agreements, and completing every missing truth label to agree/disagree with `h` as needed. For `k=m` (no external certificate) this interval is `[0,n]`, even if the observed standards are two differently named experts. The result is an elementary finite Hamming-count identity, **not an original theorem**.

Applied only as a probe to the previously verified QTDB P8 selected-beat CSV (`n=487,m=402`, cutoff 440ms, `e=76`): k=0 gives `[76,161]/487`; a *hypothetical* k=10 gives `[66,171]/487`; unconstrained k=402 gives `[0,487]/487`. This quantifies the **additional assumption** required for a numerical true-error bound, rather than pretending the dataset supplies that assumption.

## Research direction after P1

- **P2:** joint dependence/conditional class bounds from actual paired fallible references, explicitly accounting for selection. Compare adversarially dependent errors to *externally validated* conditional error budgets (if obtained); no unearned conditional independence.
- **P3:** causal/selection-aware adjudication acquisition design: what minimum new independent verification sample would contract a prespecified loss identification set? Stress selective review and records that are missing because of adjudicator workload or protocol rather than missing at random.
- **P4:** principled source-vs-target transport contract with explicit population weights, covariate support, loss semantics, and selection mechanism. Seek falsification before claims of generality.

## Status

**MQR-4.101 OPEN.** P1 empirical source is an **existing P8 audited-derived receipt**, not new raw labels. Mathematical sensitivity and full execution CI need adjudication. No verified independent truth, true risk improvement or clinical finding yet.
