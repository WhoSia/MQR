# MQR 5.4 · MQR 44 · Record 11 — A precise two-round exploration reserve with an interior optimum

**2026-11-22 KST. Claim:** original synthesis and exact finite toy calculation, not a general optimum for science; MQR 5.4 OPEN.

## 1. Why a fourth calculation is not just repetition
Record07 constructed two **different** tasks on the same four-site experimental menu: closed-world discrimination favors known diagnostic targeting, unseen novelty outside the known diagnostic favors broad search. An honest research program must not just assert 'mix is good'; it should make explicit **under exactly which utilities, horizons and conditions** a mixed policy actually beats both pure policies.

## 2. Two-round policy, completely specified
At each of two steps independently:
- with probability 1-e, exploit the fixed site that certainly discriminates two **specified known hypotheses**;
- with probability e, explore one of four sites selected uniformly.
Two objectives are mutually exclusive *evaluation tasks*, drawn with equal probability. The *known* task succeeds if at least one exploit step occurs. The *novelty* task succeeds if at least one exploration samples the single out-of-target novelty site. We are deliberately not claiming that every exploration fails the known task or every exploitation fails a real discovery; those are simplified assumptions of this synthetic model.

Hence:
```
P_known(success) = 1 - e^2
P_novelty(success) = 1 - (1 - e/4)^2
U(e) = 0.5 P_known + 0.5 P_novelty
     = 1/2 + e/4 - 17 e^2/32, for 0 <= e <= 1.
```
Derivative U'(e)=1/4 - 17e/16; second derivative U''(e)=-17/16<0. Thus the UNIQUE maximizer is **e*=4/17**. Exact outcomes:
- zero exploration e=0: P_known=1, P_novelty=0, U=1/2.
- pure exploration e=1: P_known=0, P_novelty=7/16, U=7/32.
- mixed e=4/17: P_known=273/289, P_novelty=33/289, U=9/17.

The mixed policy has higher weighted success (9/17 > 1/2 > 7/32), but this depends on **two trials, four sites, the assumed 50/50 objective mixture and independent draws**. For a one-step horizon, a linear objective may instead have a boundary optimum. If novelty frequency, search cost, model misspecification or other objective weights change, so does the optimum. Neither a 23.5% exploration budget nor 50/50 evaluation mixture is a justified universal scientific policy.

Exact rational executable `language/real/experiments/mqr_explore_mix_v54.py`, locally run PASS. The script verifies endpoints, optimum, and compares it with 1001 rational points in [0,1]. The closed-form derivative is the more general mathematical proof for this quadratic; grid enumeration is a regression check.

## 3. Philosophical result
Now distinguish:
- **Within-model optimality:** the best experimental choice conditional on a fixed known set of alternatives and evaluation loss.
- **Horizon-relative optimality:** the best plan given a specified time, cost and instrument budget.
- **Model-growth resilience:** an institutional policy preserving the possibility of detecting alternatives not in the currently modeled hypothesis set.
- **Genuinely new concept formation:** historically specific acquisition of observational and inferential distinctions not captured simply by counting visits to predefined sites.

The exact optimum addresses the first three only insofar as the novelty site and objective are explicitly built into a mathematical meta-model; it does NOT solve the fourth. Treating the analyst's externally specified unknown site as historically unanticipated is not justified.

## 4. Main prior-art rival and decisive next test
Source: Dubova, Moskvichev & Zollman (2026), DOI 10.1177/26339137261421577; the full held 2026 paper shows random sampling benefits under their high-dimensional environment and target loss, while conceding adaptive strategies can work under correctly specified priors and that all strategies presuppose a bounded experimental design space. This toy model was designed to **falsify the global random-is-best slogan** while showing an explicitly constrained case of a beneficial mixture; it is not their implementation.

Next genuinely adversarial task: include variable experiment costs, biased site distribution, nonstationary scientific fields, the possibility that exploration creates new *actions* (record09), and countermodels where exploration wastes resources while confirmed theory testing is the correct scientific objective. Require independent historical events before converting toy transition to paradigm-genesis claims.

## 5. Decision
Mathematical exact finite optimum PASS; 1001-point numerical/rational regression PASS; original real scientific exploration fraction or historical causal policy HOLD. This unit is a meaningful negative control for the new framework and earns its own research record, not a version upgrade.
