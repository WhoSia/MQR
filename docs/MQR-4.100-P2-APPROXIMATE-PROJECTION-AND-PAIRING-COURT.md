# MQR-4.100 — P2 Research Court (Internal Stage; NOT a New Official Title)

**Official, unchanged:** MQR-4.100 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport.

**Date:** 2026-10-09. **Scope:** finite-experiment mathematical sensitivity, source-matching semantics and elementary counterexamples. No new observational source, ecological field inference, fully formalized Le Cam theorem, universal progress metric or method novelty is claimed.

## 1. Explanandum and four separate operators

P1 defined an *exact* marginal-preserving joint observation J_θ(Y,Z) over a single common parameter set Θ, with projected Y distribution exactly E_θ. P2 asks what survives if projection preservation is not exact and if Y/Z only come from separate (unpaired) sources. Four distinct operators must NOT be conflated:

1. **A genuinely matched extension:** single-individual/visit joint Y,Z records with stable identifiers, event alignment and verified selection/exposure.
2. **An approximate experiment correspondence:** the actual J_θ has its Y marginal within a quantitative tolerance of E_θ on the SAME Θ, event definition and support.
3. **A statistical match/assumed coupling:** only the marginals E_θ(Y), F_θ(Z) are separately observed; a chosen Y–Z joint dependency is NOT identified by those marginals alone.
4. **A model change or a population/protocol transfer:** target θ-domain, nuisance family, sampling frame, event definition or selection process changes; requires its own new map before comparison.

The central research claim is not "additional observation always improves information." It is that the type and provenance of the *comparison map* must be recorded before a mathematical guarantee can even be applied. Similar ideas already exist in statistical matching, Le Cam's deficiency framework and the theory of comparison of experiments. P2 implements only small, unoriginal instances.

## 2. Approximate marginal preservation and its exact mathematical ceiling

Use finite spaces and total variation `TV(P,Q)=1/2 sum_x |P(x)-Q(x)|`, with range [0,1]. Let E_θ be the original observation PMF, J_θ the joint PMF, and `M_θ = proj_Y(J_θ)` its actual Y marginal. For each θ, **as an independent assumption/certificate**, let

`TV(E_θ, M_θ) <= ε_θ`.

Data processing (projecting the joint pair onto Y) plus triangle inequality give for each θ,θ':

`TV(E_θ,E_θ') <= ε_θ + TV(J_θ,J_θ') + ε_θ'`.

Consequently, if the joint observations become EXACTLY indistinguishable, `J_θ = J_θ'`, the old experiment's states can remain distinguishable but by at most `ε_θ + ε_θ'`. Therefore *approximate* conservation does NOT imply exact refinement of equivalence classes. If `TV(E_θ,E_θ') > ε_θ + ε_θ'`, then J_θ and J_θ' must differ. All inequalities are classical, not a new theorem.

**Sharp coefficient witness:** Let E_0 = (.6,.4), E_1 = (.4,.6), while J_0 = J_1 has old-variable marginal (.5,.5) (the added auxiliary coordinate may be deterministic). Then each ε=.1, TV(E_0,E_1)=.2, and TV(J_0,J_1)=0. The *two-error* bound is achieved with equality and P1 strict quotient implication no longer applies. A margin .2 does not overcome two .1 errors.

**Finite target-specific robustness:** Given a target function `g: Θ→G` over a finite Θ, define

`γ_g(E) = min_{g(θ) ≠ g(θ')} TV(E_θ,E_θ')`, if differing-target pairs exist.

If `γ_g(E) > 2ε` for a verified uniform sup bound ε, then each cross-g joint pair is still separated by at least `γ_g(E)-2ε > 0`. It is a **sufficient finite-model margin condition**, not a guarantee from data. A margin zero does not imply g is intrinsically meaningless or universally unidentifiable (in infinite spaces, an infimum may be zero without exact equality). It only removes this particular *uniform robustness* certificate.

## 3. Decision risk is a separate estimand

Because projection of J approximates E in total variation, for each old procedure `d(Y)` and loss `L(θ,d) ∈ [0,1]`, the same decision rule applied to projected J has risk distortion at most ε_θ. Thus, **under the common parameter/loss contract and actual sup-θ ε bound**, the optimal risk under the full joint observation J is no worse than the old optimal risk under E plus ε for the same Bayes prior / bounded loss. More formally, `R*_J ≤ R*_E + ε`. For any fixed old procedure, the pointwise risk comparison holds; applying it to near-optimal old rules proves Bayes/minimax variants under the usual assumptions.

This is a **one-sided** comparison; it does not establish Le Cam equivalence, a two-sided risk bound, or an unconditional global information order. Le Cam deficiency optimizes over postprocessing kernels, while the explicitly supplied projection above is only ONE candidate kernel and its uniform TV error is merely a bound on ONE direction of deficiency.

**Tight finite witness:** Source E_0=(1,0), E_1=(0,1); projected J_0=(.9,.1), J_1=(.1,.9). Under a balanced θ prior with 0–1 misclassification loss, old risk 0, new risk .1, equal to ε=.1. No statistical estimation from observations took place: all distributions are constructed.

## 4. Coupling provenance and non-identifiability from unpaired marginals

For binary Y,Z with known success probabilities `pY,pZ`, the overlap `p11=P(Y=1,Z=1)` is only constrained by the **sharp Fréchet bounds**:

`max(0,pY+pZ-1) ≤ p11 ≤ min(pY,pZ)`.

With pY=pZ=.5 these allow **every** p11 in [0,.5]. The perfectly correlated joint (.5,0,0,.5) and perfectly anticorrelated joint (0,.5,.5,0), in [00,01,10,11] order, share both marginals and yet have total variation 1 as joint distributions. The joint may distinguish θ while separate unpaired datasets cannot. This is not evidence the pairing exists in nature; it shows which information is absent until paired original records or separately justified restrictions are supplied. Nelsen et al. (2004), DOI https://doi.org/10.1016/j.jmva.2003.09.002; Conti, Marella & Scanu (2013), DOI https://doi.org/10.1016/j.csda.2013.07.004.

**Selection negative control:** The old unconditional distribution of Y is (.5,.5) in both θ=0,1; suppose a retained matched cohort selects only Y=θ. Its *conditional retained-sample* law reveals θ, but the old Y marginal no longer matches. Calling it a freely added independent signal under the original protocol would be an invalid inference unless source/target selection and model correspondence are justified. Selection itself may carry information; the error is **silently treating a conditional sampled observation as a marginal-conserving extension**, not declaring all selected datasets devoid of information.

## 5. Field/source authority, P1/4.99 continuity and audit ladder

The MQR-4.99 Oregon/eBird studies used different schemes/selection protocols; an eBird checklist and a distance-recorded Robin are not automatically the *same bird in a calibrated pair*. The original Diefenbach marked-sparrow report publishes behavioral aggregates but MQR does not hold its raw timed bird-by-bird observation logs. Existing materials therefore do **not** provide the paired microdata needed to validate a real J_θ or to estimate `sup_θ TV(E_θ,proj(J_θ))`. No measured ε is supplied; inserting an arbitrary ε from a toy test would be source laundering.

**P2 evidence gates:**
- **Mathematics:** finite PMF TV, its triangle/data-processing inequality and Fréchet coupling intervals; prior art, no novelty.
- **Formal proof:** Lean checks only elementary natural-number *coordinate discrepancy* and 2x2 count inequalities. Lean does **not** prove the full general TV inequality, Le Cam deficiency or Bayesian risk bound.
- **Executable:** Rust checks eight constructed PMF tests, source-selection failure, Fréchet extremizers and one-sided Bayes-risk example.
- **Empirical:** joint-matched microdata, target risk and external q-denominator **HOLD**.
- **Lineage:** P1 exact marginal theorem stays local to same Θ; 4.53 prohibits universal progress scalar, 4.76 prohibits independence laundering, 4.78 prohibits self-certified generator completeness, 4.84 preserves non-totalizable comparisons, 4.99 field calibration remains on HOLD.

**Next meaningful work:** record a protocol-level joint-matching certificate with original unit IDs and selection/retention mechanism; bound marginal discrepancy empirically (with sampling uncertainty) and test target-relative decision regret. If no such source is available, do not convert ε and toy risk numbers into an ecological/scientific result.

**Status at initial commit:** P2 OPEN, finite-mathematics CI pending. Final P2 verdict must be updated from the actual run, not assumed.
