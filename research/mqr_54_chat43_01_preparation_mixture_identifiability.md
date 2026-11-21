# MQR 5.4 — MQR 43 · 기록 01: Preparation-mixture stress tests for pooled order agreement

**Date:** 2026-11-21. **Conversation:** MQR 43. **Research version:** MQR 5.4, unchanged.
**Status:** EXACT FINITE MODEL / 8 LOCAL TESTS PASS / 256 TWO-STATE CONFIGURATIONS ENUMERATED / PHYSICAL BRIDGE HOLD.
**Executable:** [model](../language/real/experiments/preparation_mixture_bridge_v54.py) and [regression suite](../language/real/experiments/test_preparation_mixture_bridge_v54.py).
**Predecessors:** [MQR 42 · record06 sequential-contact criterion](mqr_54_chat42_06_sequential_contact_and_order_effects.md) and [unpaired native catalogs](mqr_54_chat42_06_unpaired_native_observables.md).

## 1. Question and scope

Two laboratories report native AB and BA sequential outputs, with each record normalized into the coordinate order (A result, B result). If the **pooled output distributions** agree after randomizing order, does that establish that the order of measurement is operationally irrelevant **for each original preparation**? **No.** A change in preparation composition can reveal conditional order effects completely hidden by a balanced preparation ensemble.

This differs from the previous record06 pointwise criterion: record06 compared two outputs **on the same analyzer-named state**. Actual repeated runs are often compared by distributions across independently prepared items. Mixture matching does not automatically recover pointwise comparison.

## 2. Exact two-state construction

Use S={0,1}, native output maps a(s)=b(s)=s, and both after-measurement state maps m_A(s)=m_B(s)=1-s. Define R_AB(s)=(a(s), b(m_A(s))) and R_BA(s)=(a(m_B(s)), b(s)).

| Initial state | AB | BA |
|---|---|---|
| 0 | (0,1) | (1,0) |
| 1 | (1,0) | (0,1) |

For the preparation mixture P(s=0)=p, P(s=1)=1-p, the two distributions on the joint native result alphabet are reversed, hence

`TV(P_AB,P_BA) = |2p-1|`.

At **p=1/2**, TV=0 although R_AB(s) differs from R_BA(s) at both states; at **p=3/4**, TV=1/2. A separate non-disturbing rival with a(s)=s, b(s)=1-s and identity after-state maps reproduces **both** order distributions at p=1/2 while preserving pointwise equality. This rival would be discriminated by additional condition-specific native calibration; equivalence is asserted only for the stated pooled balanced records, not for all conceivable experiments.

Thus unchanged pooled AB/BA proportions can be a cancellation artifact, not a physical non-disturbance receipt. Modulating the **known composition of preparations**, if feasible and certified, is a potential discriminating intervention.

## 3. Finite mixture-span proposition

Let there be n analyst-specified latent preparation states and q possible normalized joint native outputs. For each initial state s and signature y, define the order-specific probability difference

`D[s,y] = P(y | s, AB) - P(y | s, BA)`.

Each chosen preparation condition j has known, order-independent weights W[j,s] over the same states. Assumptions: preparation identity and weights are grounded; the within-state AB/BA kernels remain invariant across conditions; native outputs are comparable in their own alphabets; and no condition-specific sorting, loss or selection changes the effective mixture.

Then the observed difference matrix satisfies **Delta = W D**.

- If `rank(W)=n` and `Delta=0` exactly, then `D=0`, since W has a left inverse. Thus every constituent state has equal **conditional joint-output distributions** under the two orders.
- If `rank(W)<n`, equality of mixtures alone cannot generally identify the per-state difference: nonzero columns D in the nullspace of W may cancel. The concrete balanced two-state construction witnesses this possibility.
- The proposition does not say that `rank(W)=n` is necessary for every particular state-machine instance; one may already know conditional equality on other grounds. It is a general linear-identification sufficient condition without adding further restrictions to D.
- Even when `D=0`, hidden state changes can persist (as shown by record06). This result is neither latent ontological identity nor a physical nondemolition proof.

For n=2, rows (1/2,1/2) and (3/4,1/4) have rank 2. The example's zero TV in the first condition and nonzero TV in the second make conditional equality fail. A repeated (1/2,1/2) row has rank 1 and does not improve identification.

## 4. Execution and error boundaries

The local Python `unittest` suite passed **8/8**. It checks exact rational TV, pooled-equivalent rival mechanisms, a preparation bias grid, full-rank and rank-deficient probes, malformed dimensions and invalid weights, and **all 256 deterministic two-state combinations** of two binary readout maps and two arbitrary endomorphisms (4 × 4 × 4 × 4). Within that enumeration, order agreement under both linearly independent mixtures is equivalent to pointwise output equality. It is an exhaustive *finite regression*, not an empirical generalization.

Invalid state indices, transitions, orders, or nonprobability weights fail with ValueError. Calculations do not mutate experiment state or use floating-point thresholds. No randomized physical experiment, whole-repository test run, or stochastic confidence-interval estimation has been performed in this record.

## 5. Prior art, precise contribution, and new physical discriminant

Existing work on *generalized probabilistic theories* and measurement tomography already identifies completeness of preparation sets and linear inversion as central to operational inference. See [Experimentally Bounding Deviations From Quantum Theory in the Landscape of Generalized Probabilistic Theories (2021)](https://doi.org/10.1103/PRXQuantum.2.020302) and [An experimental test of noncontextuality without unphysical idealizations (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4909951/). Their arguments should be read for the exact operational assumptions; the elementary W-rank proposition is **not claimed as new tomography or quantum physics**. The [Feest & Steinle (2012) held source](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view) supports studying investigative practices that develop the relevant operational categories; it does not empirically validate this finite model.

MQR-specific contribution type: **conceptual transfer + explicit negative-control construction + finite verified design criterion** joining record06's order-effects problem to a minimal way of experimentally changing its identifiability. This remains at the level of analyst-given state identities, not genuine self-generated alien-science primitives.

Prospective physical test, not yet performed:
1. Define at least two externally verified preparation protocols changing proportions of independent repeats while leaving the conditional measurement kernels stable; preserve native output labels.
2. Randomize AB versus BA *within each preparation setting*. Include reset, lag/drift, reference and loss diagnostics; compare empirical joint distributions conditioned on the setting, not only pooled across settings.
3. Predeclare a rival that predicts pooled agreement at a balanced mixture but measurable divergence when the mixture shifts, plus a stable competitor and its prediction. Specify statistical power and uncertainty before judging the outcome.
4. If the shift reveals divergence, audit preparation-induced instrument drift, sample mismatch and selection before attributing an effect to measurement back-action. If results remain compatible, report only the tested operational bound, not full physical equivalence.

**Cross-science caution:** neither lab is guaranteed to know the latent weights W or to realize a common mixture knob. If calibration of W itself requires a shared framework, the sufficient-rank statement is a *conditional experiment-design insight*, not a solved bridge/bootstrap problem. An accessible output-only perturbation with an independently validated preparation certificate is the next substantial MQR 5.4 challenge.

## 6. Director's return to founding question

This is useful if it makes a previously invisible route for the world to disagree with a proposed translation. The next DFS should ask which native *operations* can produce reliable mixture shifts without an analyst-provided common latent state list. A separate BFS should examine how such operational success changes the category of a scientific **question**, not merely its statistical precision. Keep MQR 5.4's seven frontiers open; do not turn a rank check into a universal paradigm-generation theory.
