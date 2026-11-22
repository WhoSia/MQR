# MQR 5.4 · MQR 44 · R41 — Two equally accurate instruments need not be comparable experiments

**2026-11-22 KST.** Exact synthetic conditional result, executed locally PASS. Intentionally undercuts an inappropriate scalar 'apparatus improves, science improves' metric. This is elementary Blackwell/garbling/informativeness theory, **not** an MQR original theorem. MQR 5.4 OPEN.

## 1. Finite four-world demonstration with changed scientific target
Let the state of the world be a pair (X,Y)∈{0,1}², with four states equally likely. Scientific practice P can read **X perfectly** but receives no Y measurement; practice Q reads **Y perfectly** but receives no X measurement. Both are error-free as sensors *for their own declared target*.

For a decision problem requiring X, the best correct-guess probability from P is 1 and from Q is 1/2. For predicting Y the results reverse exactly. These channels are NOT Blackwell ordered relative to the entire (X,Y) state space: Y cannot be obtained as a state-independent random postprocessing of X, since among states sharing X, Y takes different values with certainty; vice versa similarly.

The two scientific interfaces are thus **incomparable** rather than better or worse. If a new technique substitutes a Y sensor for an X sensor, X-related scientific access shrinks even though Y-related access increases. If one retains BOTH raw channels, it can recover either previous question's answer; under the usual no-cost optimal-policy assumptions, the knowledge ability does not shrink.

Exact locally verified code: `language/real/experiments/mqr_incomparable_question_channels_v54.py` prints `PASS: X/Y channels incomparable; target-dependent accuracy 1 vs 1/2 (reversed)`. No real experiment or actual RNA biochemical probability is asserted.

## 2. How this constrains 1950s RNA historical claims
The actual 1958 Hoagland et al. paper (JBC 231:241–257) reports qualitatively that an RNA isolation method's sample condition affects how much labeled signal is observable. The historical Rheinberger account compares RNA recovery with radioactive signal loss. Those are **different experimental targets**. It is legitimate to say optimizing sample yield did not necessarily improve ability to detect the nascent scientific object; it is NOT legitimate to say more informative information somehow injured the same Bayesian decision problem.

Do not infer the RNA experiment channels literally had the 4-state X/Y structure, identical information values or uniform priors. The model merely displays a logically available mechanism of goal-dependent instrument incommensurability.

## 3. A hard caveat on scientific 'question generation'
A theoretically specifiable X or Y state component in our counterexample is imposed by a *later analyst*. Historical scientists sometimes do not yet have language or experimental apparatus for defining the target Y. Consequently this model illustrates target-dependent comparison **once two targets are formally known** but cannot explain ontologically unanticipated question invention. To explain that, need dated actor-level concept construction and material operations, as in Rheinberger/Steinle/Feest. MQR cannot claim fixed-state decision models exhaust scientific openness.

## 4. Scope-bound conclusion
- Blackwell-domination ⇒ for fixed targets/actions/prior/decision rule optimization, no decrease of best expected utility.
- Incomparability ⇒ improvement claims require target-specific evaluation; no single global ordering.
- Changes to materials/experimental process ⇒ state and channel may change, and original data may be irrecoverable.
- Changes to concepts and questions ⇒ the set of possible *decision problems* is itself historically variable; standard fixed-domain results do not automatically order it.

**Next historical discriminator:** identify an actual before/after technique modification, target-dependent measurable signals and loss of recoverability; test alternative explanations (specimen or cohort differences, assay error, changed target, communication effects). One fabricated toy is not a historical finding.

**Status:** exact proof and synthetic code PASS; RNA mapping to X/Y direct archival confirmation HOLD; 5.4 OPEN.
