# MQR 5.4 · MQR 44 · Record 07 — Experiment choice under an open hypothesis horizon

**2026-11-22 KST.** TYPE: Source-grounded adversarial synthesis + exact mathematical counterexample; theory version 5.4 OPEN. This is not a replication of any article and not a claim of original active-learning discovery.

## 1. Critical rereading of Dubova, Moskvichev & Zollman (2026)
Directly fetched 89,451-character text of the *Collective Intelligence* 5(1) article, DOI 10.1177/26339137261421577 (held Drive PDF: `1XI4OoLOa4rrfA26mUPMULBb0ErwrCYrP`). Journal first online publication 2026-02-16. Main modeling architecture: a family of high-dimensional ground-truth environments defined as mixtures of multivariate Gaussian distributions; agents choose experiments, construct reduced-dimensional representations and learn from others. Experimental strategies include confirmation, falsification, disagreement, novelty and random sampling. Distinguishes *perceived* model success on gathered data from *actual* generalization to independently assessed ground-truth observations.

Read beyond abstract:
- Experiment 1: 9,060 completed simulations (2 incomplete) across context parameters, not a real-world randomized field trial.
- Experiment 2: novelty strategy after only one random observation; reported 4,191 completed simulations, 129 incomplete, random advantage emerges with sample accumulation.
- Experiment 3: initial pretraining 10/50/100 observations; 8,906 completed simulations, 166 incomplete, relative ranking not reversed by their pretraining.
- Experiment 4: dependent/independent variable roles separated in one dimension; relative results broadly persist, with important differences in strategy pair rankings.
- Experiment 5: changed task to predict hidden observation dimensions rather than reconstruct input; **random and novelty driven strategies both outperformed the other strategies**, so it is inaccurate to claim strict domination by random in all objectives.
- Authors expressly acknowledge that random sampling itself depends on selecting a bounded experimental space and is not intrinsically bias-free. Adaptive sampling can outperform under well-specified structure; universal 'random is best' is unwarranted.

This source is strong *prior art and adversarial challenge*, not proof of a universal experimental policy.

## 2. An analytic demonstration of why neither policy universally dominates
Let there be exactly four experiment sites. A pair of *known candidate theories* gives different deterministic outputs at one diagnostic site, identical outputs elsewhere. With one experiment, targeting that known site identifies which candidate theory obtains with probability 1. Uniform random site selection succeeds with probability 1/4; with n independent choices probability of visiting the site at least once is 1-(3/4)^n. Thus targeted design is better at the *specified closed-world identification objective*.

Now fix a different open-world objective: an unanticipated novelty resides at a site OUTSIDE the fixed target site. A policy always repeating the target cannot see it, while a uniform random policy sees its site within n rounds with probability 1-(3/4)^n. The two objectives are explicitly distinct, and novelty's location is conditioned to lie outside the target. This is neither a universal victory for random search nor an empirical claim about scientific practice.

At n=4, random hit probability = 175/256. In contrast targeted known-hypothesis discrimination = 1 and targeted out-of-target novelty detection = 0. This creates a toy tradeoff **caused by different objective/coverage specifications**, not by computational complexity or human irrationality.

Executable exact-fraction regression: [`mqr_inquiry_frontier_v54.py`](../language/real/experiments/mqr_inquiry_frontier_v54.py), locally run in Python with PASS prior to GitHub commit. Code tests 1<=n<=8 and checks boundaries. Code includes shared-evidence and partition calculations as reusable companion material for next records.

## 3. Proposed MQR advance: epistemic objective drift and horizon reserves
Distinguish four uncertainty kinds:
1. State uncertainty within an accepted model.
2. Model uncertainty among explicitly listed alternatives.
3. **Domain coverage uncertainty**: unmeasured regions under existing observational dimensions.
4. **Concept-space incompleteness**: entirely missing observational variables, intervention types or explanatory aims.

Conventional information gain typically addresses 1–2 and can be adapted to 3 with models of it. A fixed finite query-language cannot simply attach a validated prior over every unknown future concept in 4. The language must distinguish a resource *policy for admitting new observations/actions* from a claim to enumerate all possible novel questions.

A candidate constrained policy: under fixed budget B allocate B_test to declared competitors, B_cover to pre-registered representational coverage and B_meta to tool/variable invention and out-of-model anomaly review. These are governance knobs, not numerical defaults validated by MQR. Compare policies on BOTH held-out domain generalization and newly discovered testable contrasts, not on in-sample likelihood alone.

## 4. Adversarial test and next decision
A rival might show that robust Bayesian experimental design with misspecification or optimal design over the full domain already captures all of this. That is a real threat to novelty but not to value of rigorous synthesis (MQR doctrine 2026-10-18). The proposed open-horizon category earns distinct explanatory work only if **actual changes of observable/action repertoire** can be sourced and prospectively predicted rather than scored retrospectively.

Test program: log dated Steinle/Faraday exploratory experimental menus; compare against Kuhn loss and period-specific instrument abilities; use 2026 simulations as bounded external model comparison. Historical primaries still required before claiming exact priority.

**Status:** Exact finite synthetic algebra PASS; direct 2026 source reread PASS at section-level; complete replication, population generalizability, historical case explanation HOLD. No 5.5 promotion.
