# MQR-4.35 — Literature Bridge

All literature has zero forcing/fresh case credit. It constrains interpretation only.

## Miyake (2013) — black-box measurement and underdetermination

Teru Miyake, *Underdetermination, Black Boxes, and Measurement*, Philosophy of Science 80(5):697–708. DOI: `10.1086/673729`.

Drive copy was read during 4.35. Miyake's Kepler discussion is especially relevant: observational equivalence at one evidential coordinate need not be permanent, because a new measured variable can refine the evidential partition. But such refinement is not free; it depends on enabling assumptions whose justification becomes part of the epistemic problem.

MQR translation: a receipt collision is not answered by declaring one rival unreal. It motivates a new prospective measurement coordinate only when that coordinate is independently operationalized and exposed to defeat.

## Beauchemin & Staley (2026) — usefulness, uncertainty and sensitivity

Pierre-Hugues Beauchemin & Kent W. Staley, *How uncertainty and underdetermination allow measurement to produce useful results*, Measurement 267:120330. DOI: `10.1016/j.measurement.2026.120330`.

Drive preprint was read during 4.35. Their 'problem of usefulness' concerns how results produced under specific conditions can legitimately function as evidence in broader future inquiries. Their account makes sensitivity and uncertainty part of managing this transport problem rather than treating uncertainty only as a defect.

MQR translation: `SENSITIVITY_SCOPE` is not an ornamental seventh coordinate. It represents a prospective attempt to state the boundary over which an evidential result remains useful. 4.35 still does not import their account as a proof of NU3.

## Rischel & Weichwald (2021) — compositional abstraction error

Eigil F. Rischel & Sebastian Weichwald, *Compositional Abstraction Error and a Category of Causal Models*, UAI 2021, PMLR 161:1013–1023. Open proceedings record: PMLR 161.

The Drive copy was read during 4.35. The paper gives an especially sharp analogue to MQR's bridge-direct problem. It argues that abstraction error should be compositional and exhibits a case where two individually small KL-divergence abstraction steps (reported as 0.22 and 0.39) do not control the overall abstraction error, which is reported as 1.52. Their framework then builds a compositional error notion with an appropriate bound.

MQR translation: good adjacent transformations do not, by themselves, license a direct composite claim. What matters is whether the error/support notion itself is compositional under the relevant maps and interventions.

The same paper emphasizes that intervention implementation can be ambiguous and should be made explicit. This independently motivates the presealed `INTERVENTION_ALIGNMENT` coordinate, but does not establish that the coordinate is sufficient.

## Rubenstein et al. (2017) — exact transformations

Paul K. Rubenstein et al., *Causal Consistency of Structural Equation Models*, UAI 2017, arXiv `1707.00819`.

Their exact-transformation framework formalizes consistency between causal models at different levels by requiring agreement of interventional predictions under an explicit transformation. Exact transformations compose under their conditions.

MQR translation: composition can be a theorem when the transformation structure is strong enough. MQR-4.35 therefore should not infer that composition is generically impossible; it asks which empirically warranted structure is sufficient to license it in a given court.

## Statistical sufficiency analogy and limit

Classical statistical sufficiency says, roughly, that a statistic is sufficient for a parameter when the data contain no additional parameter-relevant information once the statistic is known; the Fisher–Neyman factorization criterion gives a standard characterization in dominated statistical models.

MQR borrows only the information-preserving reduction intuition. `MU` and `NUk` are not claimed to be sufficient statistics in the classical probabilistic sense. MQR's finite deterministic factorization condition is explicitly target- and probe-relative.

## Underdetermination and open-world residue

Contemporary philosophy of science distinguishes transient/local underdetermination from stronger claims of permanent empirical equivalence. The relevant lesson for MQR is that an apparent equivalence at the current observational partition can be defeated by new experiments, instruments, variables or auxiliary knowledge; conversely, a current absence of rivals does not prove that the representational space has been exhausted.

MQR-4.35 therefore treats `OPEN_WORLD_RESIDUE` as constitutive: it blocks the illicit move from finite collision-free performance to universal sufficiency, while still permitting representations to earn local, prospective authority.
