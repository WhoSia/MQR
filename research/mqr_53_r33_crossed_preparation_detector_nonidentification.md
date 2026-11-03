# MQR-5.3 R33 — A crossed experiment can expose differential errors without identifying a common bias

**2026-11-03 · Constructed counterexample · no empirical measurements or originality priority.**

## Question

Does crossing two specimen preparation routes with two detectors solve the shared-error problem of R32? **Only partly:** a factorial experiment can identify contrasts in the additive model, but cannot recover the absolute measurand from readings alone.

## Model and derivation

Let i,j in {1,2}, and suppose the noiseless expected reading is

`m_ij = theta + g + u_i + v_j + kappa*s_i*t_j`,

where `theta` is the desired measurand, `g` a shared additive bias, `u_i` route-specific bias, `v_j` detector-specific bias, `s=(-1,+1)`, `t=(-1,+1)`, and `kappa` a nonadditive interaction. Actual observations are `Y_ijr = m_ij + epsilon_ijr` for replicate r. **Assumption:** preparation changes do not themselves change the intended measurand; that hypothesis needs physical controls.

Four useful statistics of the expected matrix are:

- grand mean `M=(m11+m12+m21+m22)/4 = theta+g+mean(u)+mean(v)`;
- route contrast `R=(m11+m12-m21-m22)/2 = u1-u2`;
- detector contrast `D=(m11+m21-m12-m22)/2 = v1-v2`;
- interaction contrast `J=m11-m12-m21+m22 = 4*kappa`.

The equations follow by algebra; they are not a new theorem. With replicated noisy measurements, the sample contrasts estimate these population quantities with uncertainty determined by noise and dependence.

For every real t, replacing `(theta,g)` by `(theta+t,g-t)` leaves all four readings unchanged. This **gauge symmetry** is unaffected by sample size or randomization within the existing four cells. Imposing `u1+u2=v1+v2=0` merely chooses a parameterization of relative effects; it does not justify `g=0`. A reference specimen with independently known quantity or an independently warranted physical model is required to pin down the absolute scale; any transfer to a different specimen additionally assumes stable calibration relations.

## Concrete adversarial pair

Take `theta=10, g=2, u=(-1,+1), v=(-0.5,+0.5), kappa=0`. Then the expected matrix is

```
            detector 1    detector 2
prep 1          10.5          11.5
prep 2          12.5          13.5
```

Its mean is 12, route contrast -2, detector contrast -1, interaction 0. The **same matrix** arises from `theta=11, g=1`. Thus crossing the factors exposes variation without certifying the measured absolute value. If `kappa=0.4`, the interaction contrast becomes 1.6, which can flag nonadditivity; it cannot establish whether the cause is instrument interaction or preparation-induced physical changes without further controls.

## Adversarial literature connection

R7 already argued that crossed preparations and detectors cannot eliminate all upstream biases. R33 **formalizes one small instance**, rather than claiming a fresh discovery. Tal (2017) supplies the calibration-as-tested-model framework; Chang (2004) cautions against treating historically contingent reference points as incontestable; Rheinberger (1997) and Nersessian (2006) caution that changing preparation or apparatus may change the material phenomenon and not merely the indicator. These are comparative interpretations of existing works, not numerical assertions about historic temperature or biochemical data.

## Prospective physical/historical falsification design

1. Choose two independently prepared but measurand-stable reference specimens (or document why this is physically impossible), two detector principles, randomized ordering and blinded replicates.
2. Predefine the four contrasts and a noise/dependence model; test the interaction contrast against measurement uncertainty.
3. Add an external reference or independently derived invariant to address the grand-mean gauge ambiguity. **Record the possibility that this reference shares the same source of error.**
4. Repeat in an out-of-domain temperature or assay regime; assess whether the inferred differential structure transports or fails.
5. If conventional factorial design, random-effects metrology or system identification already supplies the sufficient framework, classify the MQR contribution as a philosophical/operational synthesis rather than novelty.

## Files and execution gate

- `language/real/experiments/mqr53_r33_crossed_measurement.py`
- `language/real/experiments/test_mqr53_r33_crossed_measurement.py`

Run locally: `cd language/real/experiments && python -m unittest -v test_mqr53_r33_crossed_measurement.py`. Algebraic entries were independently hand/computationally checked; full submitted Python regression execution/CI receipt still unverified.

**Next genuine question:** Can we define a *minimal independently informative intervention* in a specific historical temperature-scale controversy, with explicit rival predictions before consulting the observed outcome? Compare Chang ch. 1 (boiling vs steam point), Tal's model-based calibration, and relevant primary experimental records. Do not retrospectively manufacture a prospective test.
