# MQR-5.3 R32 — Predictive accessibility is not evidential independence

Date: 2026-11-03. **Status:** analytic counterexample and executable candidate only; no physical evidence, no novelty priority, no completed CI verification.

## 0. Investigative question

**When does a new representation make an existing scientific distinction easier to infer, and when do additional instruments actually contribute independent evidence?** These are different claims. A stronger prediction or greater agreement can be generated without new information about the world.

This study links two intentionally separate mechanisms:
- **computational accessibility** under a restricted hypothesis family;
- **measurement validity** under latent dependence between instruments.

It does not assert that these two mathematical models exhaust Chang's historical epistemic iteration or Rheinberger's experimental systems.

## 1. Prior literature, read against the claims

- **Dennett (1991), *Real Patterns*, pp. 27–51**, [Drive copy](https://drive.google.com/file/d/1XJVMaxU0Dtqmm8dhJwAp-pNSG0vXn76D/view): connects pattern claims to useful prediction and economical description. Our parity example tests a computationally restricted predictor, **not** a refutation of Dennett or a complete definition of real patterns.
- **Chang (2004), *Inventing Temperature*, ch. 5, especially pp. 224–231**, [Drive copy](https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view): provisional standards can be refined and corrected through epistemic iteration without an infallible starting point. This does **not** imply convergence or guarantee shared error removal.
- **Tal (2017), *Calibration: Modelling the Measurement Process***, [Drive copy](https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view): calibration is modelling, prediction, testing and revision; standards help but are not universally necessary. Our construction identifies which independence assumptions must be tested rather than attributing this equation to Tal.
- **Rheinberger (1997), *Toward a History of Epistemic Things*, ch. 2**, [Drive copy](https://drive.google.com/file/d/1DDrn0i1jOZ79tx8VxftIgQmdTrNH4tr8/view): epistemic things are objects of inquiry that remain indeterminate and are manipulated under technical conditions. Laboratory intervention cannot always be treated as adding a variable to an unchanged dataset.
- **Nersessian (2006), *Model-Based Reasoning in Distributed Cognitive Systems*, pp. 699–709**, [Drive copy](https://drive.google.com/file/d/1yFjWFI0fLVfyoeQ4cu3idJ039mZ5bEn5/view): physical modelling systems are simultaneously representations and engineered devices with their own constraints; construction may alter the experiment. This is a reason to separate feature construction from physical measurement.

Only the cited passages/sections were revisited during this pass; do not record complete-book rereading.

## 2. Proposition A — same Shannon information, different restricted learnability

Let A,B be independent Bernoulli(1/2), W=A XOR B. An existing raw measurement is R=(A,B); its deterministic enrichment is Z=(A,B,A XOR B).

Since W=f(R) and Z=g(R) with R included in Z,
I(W;R)=I(W;Z)=H(W)=1 bit.
No new physical observation is made by appending the parity feature.

Consider affine threshold predictors h(a,b)=1[beta_0+beta_1 a+beta_2 b >=0] with the four pairs equally likely. They **cannot** represent XOR exactly:

For h(0,0)=0, beta_0<0. For both h(1,0)=1 and h(0,1)=1, beta_0+beta_1>=0 and beta_0+beta_2>=0. Thus beta_0+beta_1+beta_2 >= -beta_0 >0, contradicting h(1,1)=0. The best possible uniform accuracy is 3/4 (e.g. OR). An affine threshold predictor over Z can set h=1[parity - 1/2 >=0] and obtain accuracy 1.

Hence a representation can improve the **accessibility of a question to a restricted hypothesis class** without increasing Shannon information. This is an established kind of feature engineering, not an invention of a new information law. It does not show generalization under arbitrary model selection.

## 3. Proposition B — a new noisy observation adds information

Suppose the old interface reports only A; W=A XOR B is independent of A, so I(W;A)=0. A new sensor reports C=B XOR E, with E independent Bernoulli(eta), 0<=eta<=1/2, and A,B fair and mutually independent. Then
I(W;A,C)=1-h_2(eta),
where h_2(eta)=-eta log2 eta-(1-eta) log2(1-eta). For eta=0.1 this is 0.5310044064 bits and the Bayes-optimal parity estimate has accuracy 0.9. The information gain here depends on a **new measured channel** C, not on a deterministic re-encoding of A.

This statement assumes a calibrated channel and independence. If eta is unknown, its inferential interpretation is correspondingly weaker.

## 4. Proposition C — two perfectly agreeing sensors may provide no calibration

Let C_1=B XOR E_1 and C_2=B XOR E_2. If E_1,E_2 are mutually independent, iid Bernoulli(eta), and independent of B, then
d=P(C_1 != C_2)=2 eta(1-eta).
With 0<=eta<=1/2 this can be inverted:
eta=(1-sqrt(1-2d))/2.
For eta=0.1, d=0.18, which identifies eta *within this model* from an indefinitely large sample. No ground-truth B is needed for this particular parameter because independence is built into the model.

Now replace E_1,E_2 by the **same** latent error E, with P(E=1)=0.1. Then C_1=C_2 always: d=0. For fair, unobserved B, the entire observable joint distribution is
P(C_1=0,C_2=0)=P(C_1=1,C_2=1)=1/2,
the same as two perfect sensors (eta=0). Thus no sample size of C_1,C_2 alone can distinguish these worlds. Applying the independent-error inversion would incorrectly report eta_hat=0 despite the true 0.1 shared error.

The comparison does not apply if a trusted reference B is actually observed: then errors can be estimated directly. The independent model is a conditional theorem, and the shared-error world is an adversarial violation of its assumptions.

## 5. Critical counterarguments and failure boundaries

1. **Three sensors could be better.** Yes, if their conditional dependence structure has been independently justified. Adding an exact copy of one defective sensor provides no new identification: C_3=C_1 leaves the observed law unchanged.
2. **What if good performance is only a representational artifact?** Then independently held-out experimental tasks should fail to show improvement; distinguish prediction on generated features from new target information.
3. **Does iteration itself solve shared error?** No. Applying the same calibration procedure repeatedly does not create external constraints. A different preparation, trusted reference, or physically independent measurement route may help, but must be audited for shared upstream causes.
4. **Is the common-error mechanism realistic?** It is a mathematical possibility, not evidence that any historical instrument exhibited exactly this XOR mechanism. Possible material examples (sample preparation, common reference bath, shared power calibration) are hypotheses for archival testing.
5. **Could identical experimental outputs simply share a genuine signal?** Yes. The counterexample shows *non-entailment* of correctness from agreement, not that actual agreement is worthless.

## 6. Prospective research design / question ledger

**Q32.1:** What independent intervention can test the independence of calibration errors while holding the measurand stable? Candidate: cross different preparation routes P1/P2 with sensing technologies D1/D2, with blinded reference controls; check whether residual error covariance persists. An untested shared upstream reference still leaves ambiguity.

**Q32.2:** Can a decision-relevant quantity be identifiable despite absolute parameter nonidentifiability? Determine whether a claim is invariant over the model's observational equivalence class; compare MQR R2.

**Q32.3:** What is genuinely produced during concept formation: a new feature of existing data, a new experimental operation, or a new empirical referent? Compare Chang ch. 5, Rheinberger ch. 2, and Nersessian's model systems without assuming equivalence.

**Q32.4 (adversarial):** Can standard misspecification-robust design or system identification anticipate all of these examples? If yes, MQR gains an explanatory comparison, not a new technique; explicitly log this negative result.

## 7. Executable evidence and custody

Synthetic script: `language/real/experiments/mqr53_r32_representation.py`. Regression script: `language/real/experiments/test_mqr53_r32_representation.py`. Suggested local execution:

```bash
cd language/real/experiments
python -m unittest -v test_mqr53_r32_representation.py
```

The proof is algebraic; the finite coefficient grid in the test is only an illustrative regression witness. The tests were authored in GitHub; external runtime/CI success must be established separately. Do not use GitHub Actions bot contributions. This file is a research note rather than a claim of publication novelty.

**Immediate next experiment:** construct a small 2-by-2 preparation-by-sensor interaction with a *known* shared and independent error decomposition; show precisely which covariance contrasts estimate which bias components, and produce an opposing pair of observationally equivalent mechanisms.
