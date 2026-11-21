# MQR 5.4 — MQR 43 · 기록 02: Deterministic-vs-stochastic cancellation and model-class sensitivity

**2026-11-21. Conversation 43, research version 5.4 unchanged.**
**Status:** LOCAL EXACT COUNTEREXAMPLE + 4 NEW TESTS PASS / PHYSICAL APPLICATION HOLD.
**Previous result:** [MQR 43 record01 mixture-span proposition](mqr_54_chat43_01_preparation_mixture_identifiability.md).
**New test:** [test_stochastic_mixture_bridge_v54.py](../language/real/experiments/test_stochastic_mixture_bridge_v54.py).

## 1. Director's objection to a tempting overgeneralization

Record01 found that changing a balanced two-state preparation mixture to p=3/4 exposes its deterministic order disturbance, and that two known linearly independent preparations form a sufficient identification design. A reader might incorrectly infer that **one unbalanced preparation always suffices**. That is true in the special nondegenerate two-state deterministic-output construction, but **false with stochastic native readouts**.

Distinguish three claims:
- **Existential refutation:** one adequately controlled preparation condition where AB and BA differ rules out operational order equality for that setting. This detects an effect without reconstructing latent states or W, but still requires genuine randomization, stable preparation and measurement controls.
- **Pointwise identification:** equal pooled AB/BA distributions permit a general latent-conditional equality inference only under enough independently certified preparation combinations (rank(W)=n for n latent states, invariant conditional kernels).
- **Mechanism attribution:** neither difference nor equality by itself proves measurement back-action rather than selection, latency, reset failure, device drift or mislabeled physical handoff.

## 2. New stochastic negative control

For a single binary joint-result category `u` versus `not-u`, let the conditional probabilities at states 0 and 1 be:

| State | P(u | AB, state) | P(u | BA, state) |
|---|---|---|
| 0 | 3/5 | 1/2 |
| 1 | 1/5 | 1/2 |

With P(state 0)=3/4, both pooled probabilities equal

`P(u|AB)=(3/4)(3/5)+(1/4)(1/5)=1/2`,
`P(u|BA)=(3/4)(1/2)+(1/4)(1/2)=1/2`.

Their binary complementary outcomes also agree, **despite conditional discrepancies** (+1/10 at state 0, −3/10 at state 1). Thus a **nonuniform** mixture itself does not eliminate cancellation for stochastic kernels.

Under a second mixture P(state 0)=1/2, one finds `P(u|AB)=2/5` versus `P(u|BA)=1/2`. The pair of preparation-weight rows (3/4,1/4) and (1/2,1/2) has rank 2, recovering the record01 full-rank criterion.

These are abstract conditional probability distributions over one binary signature; the note does **not** assert a realized physical sequential-measurement instrument that produces these numbers.

## 3. Exact finite enumeration and limits

- The earlier deterministic two-state exhaustive suite checked 4 binary output functions for A, 4 for B, 4 possible A after-state maps, and 4 B maps: **256 total systems**. Of these, 136 show balanced pooled AB/BA agreement; only **100** have actual pointwise equality; **36** hide differences by balanced cancellation. These proportions reflect an artificially uniform enumeration of model descriptions, **not a probability of physical experimental error**.
- Under the single p=3/4 mixture in this same strictly deterministic two-state family, pooled equality occurred in exactly those **100 pointwise-equal** models. This is a restricted combinatorial fact, not the general theorem.
- New independent four-test suite checks one stochastic cancellation at p=3/4, its exposure at p=1/2, malformed probability boundaries, and **256** Bernoulli conditional-probability quadruples on the grid {0,1/3,2/3,1} under two linearly independent mixtures.
- All **4/4 new tests** passed locally; together with record01's **8/8**, this makes **12/12 local tests**. Both original Python files and the new test file have local-versus-GitHub matching Git blob SHA. No whole-repository integration or physical measurement has been run.

## 4. Operational research decision

The structural sufficiency of rank(W)=n is mathematically standard linear inference, closely related to preparation completeness in generalized probabilistic theory and tomography: [PRX Quantum 2, 020302 (2021)](https://doi.org/10.1103/PRXQuantum.2.020302) and [Experimental test of noncontextuality (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4909951/). The contribution here is a **qualified comparison of deterministic and stochastic assumptions** within MQR's cross-science experimental-translation problem, with explicit falsifying tests.

For the next physical-facing design, prioritize a readily testable **difference-producing protocol** before a universal equality certificate: independent repeatable preparation recipes, randomized AB/BA ordering per recipe, native-label joint signatures, and a documented preparation/clock/custody chain. If different native instruments agree at one pooled setting, search for a deliberate preparation perturbation with an independently validated effect rather than claiming conceptual fusion. However, finding another perturbation that changes a prediction is still not yet creating an entirely new conceptual primitive.

**DFS handoff:** seek a cross-lab preparation perturbation that is expressible through each science's own operation vocabulary, without supplying the analyst's common latent state coordinate as a premise. **BFS return:** what new questions become executable once those operations are coupled, beyond improving parameter identification?
