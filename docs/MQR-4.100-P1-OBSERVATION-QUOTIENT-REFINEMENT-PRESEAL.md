# MQR-4.100-P1 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport

Date: 2026-10-09. The user has **authorized the official title and P1 work**, but has not authorized scientific closure of MQR-4.99. P1 is a scoped **known-mathematics / finite-countermodel** court, not an original theorem, an empirical discovery, or a successor that retroactively resolves outstanding ecological limitations.

## 0. Explanandum lock and historical non-repetition

Explanandum: Given a parameterized observation experiment E and a proposed additional measurement Z, what EXACTLY changes in (i) indistinguishability of parameters, (ii) identified target functions, (iii) decision informativeness, (iv) dependence on measurement assumptions, and (v) justified target/protocol transport?

Historical receipts, which may not be superseded without a new defeating witness:
- MQR-4.53: Blackwell experiment comparison is only a **local partial order**, never a universal scientific-progress scalar; Fisher–Rao is local. Reference: `experiments/mqr-4.53/FINAL-SEAL.md`.
- MQR-4.76: origin-independent authority is not earned by repeated computation; later authority requires a relevant dependency cut with provenance. Reference: `experiments/mqr-4.76/FINAL-SEAL.md`.
- MQR-4.78: separator success does not certify separator-generator completeness; the finite target family must be independently warranted. Reference: `experiments/mqr-4.78/FINAL-SEAL.md`.
- MQR-4.84: do not impose a global total ranking on otherwise scoped admissible comparisons. Reference: `experiments/mqr-4.84/FINAL-SEAL.md`.
- MQR-4.99: P2 reproduced **existing published source bookkeeping** and P3 tested hand-transcribed behavioral aggregate arithmetic, without new independent calibration. This is a cautionary case, NOT field confirmation of the formal structure below.

**Novelty firewall:** Statistical experiment kernels, Blackwell garbling/order, identified sets, Fréchet bounds, stochastic data processing, and elementary quotient refinement are established mathematics; the present elementary proofs and finite regression fixtures are not advertised as new theorems. See Blackwell (1953), DOI https://doi.org/10.1214/aoms/1177729032; Torgersen (1991), *Comparison of Statistical Experiments* DOI https://doi.org/10.1017/CBO9780511666353.007; Manski (2003), *Partial Identification of Probability Distributions* DOI https://doi.org/10.1007/b97478; and statistical-matching/Frechet prior art, DOI https://doi.org/10.1080/03610926.2015.1010005.

## 1. Fixed-type definitions and a strictly conditional refinement lemma

Let Θ be a common, **fixed** parameter set, Ω_Y and Ω_Z finite observable outcome sets, E: Θ→Δ(Ω_Y) a fixed old experiment, and J: Θ→Δ(Ω_Y×Ω_Z) a joint **paired** auxiliary-measurement experiment. Demand a known **projection conservation certificate** for EVERY θ and y:

`E(θ)(y) = Σ_z J(θ)(y,z)`.

Define θ ~E θ' iff E(θ)=E(θ') as complete distributions; likewise θ ~J θ' iff J(θ)=J(θ'). The kernel partition / observation quotient Θ / ~E is representation-relative.

**Elementary lemma:** ∀ θ,θ', θ~Jθ' ⇒ θ~Eθ' by applying the marginal map. Therefore ~J ⊆ ~E. Strict refinement holds iff some θ~Eθ' but θ is NOT ~J θ'. It is **not** automatic merely because Z has new columns or more readings. A user-supplied scientific claim that J conserves E requires actual measurement correspondence, not an ex post label.

For any target function g: Θ→G, say g is identifiable under E iff `θ~Eθ' ⇒ g(θ)=g(θ')`. If identifiable before a valid fixed-domain joint extension, it remains so after extension. A strictly smaller equivalence kernel need NOT change identifiability of a particular g, and does not measure any universal progress.

**Formal scope:** Lean 4 checks the general set/function projection theorem and target preservation, where Old/New are arbitrary mathematical objects (in particular complete probability laws). Rust checks finite PMF row normalization, projection conservation and concrete distinguishability; the Lean file is NOT a machine-checked measure-theoretic Blackwell theorem.

## 2. Negative controls that force the distinction

**N1 — Duplicate measurement (no quotient change).** Let θ∈{0,1}; Y|0 Bernoulli(0.4) and Y|1 Bernoulli(0.6). Appending Z=Y produces a larger *paired* observation but no new equivalence separation; Bayes classification success under the uniform θ prior stays 0.6.

**N2 — Pairing is essential (strict only with joint data).** For θ=0, P(Y,Z) assigns probability 1/2 to (0,0) and (1,1). For θ=1, assign probability 1/2 to (0,1) and (1,0). Both experiments' Y and Z **separate marginals are fair coins in both θ**, so two independently published unpaired marginal datasets cannot distinguish θ. Matched joint observations distinguish θ perfectly through the dependence structure. The fictitious matching operation itself is an unearned source claim.

**N3 — Strict Blackwell decision gain without any change of quotient.** The old Y already has distinct laws (.6/.4 vs .4/.6) for θ=0/1, and appending a perfect θ-revealing Z preserves the original marginal while making uniform-prior state classification accuracy rise 0.6→1.0. BOTH kernels already have discrete classes {0},{1}; therefore strict improvement in a decision problem does NOT require strict kernel refinement. Quotient ordering is weaker than Blackwell informativeness (and no scalar progress is promoted).

**N4 — Nuisance/model expansion is not an auxiliary-channel refinement.** Old Y=θ identifies θ. In a *different model* with parameter (θ,η) and Y=θ XOR η, (0,0) and (1,1) have the same observation but different θ. This is not a failure of the projection lemma: the parameter space and θ-wise old experiment were changed, and the marginal-conservation certificate does not exist.

**N5 — Assumption narrowing ≠ new evidence.** An uninformative Y with admissible θ∈{0,1} cannot identify θ. Declaring θ=0 admissible and θ=1 inadmissible trivializes identification without collecting Z; this can be a legitimate externally warranted restriction, but it is not a measurement information gain.

**N6 — Target-relative gain.** θ∈{A,B,C}; initial experiment groups A,B and separates C. The target g(A)=g(B)=0 and g(C)=1 is already identified. A matched Z can separate A from B and strictly refine the full parameter quotient without improving the identified status of this g.

**N7 — Cross-protocol type mismatch.** Source E_S distinguishes its θ labels; target E_T has identical PMFs for those labels. Merely reusing symbol names does not transport the identifying property. Required: explicit population/parameter correspondence, loss/outcome meaning, known or warranted measurement kernels, selection/positivity and validation/uncertainty account. Target risk identification is a different claim again.

## 3. Gates and no-overclaim mechanism

Gate | Required object | P1 judgment
--- | --- | ---
G0 source ancestry | cited established theory and MQR lineage | PASS as background, not discovery
G1 fixed-domain projection | θ-indexed marginal-conservation witness | mathematical local theorem only
G2 strictness | explicit witness distinguished by joint but not old | CONDITIONAL; N2 yes, N1/N3 no
G3 pairing | recorded same-individual joint labels, not merely two marginal lists | N2 math fixture; field warrant HOLD
G4 nuisance and changed assumptions | typed map and model-version comparison | N4/N5 prevent laundering
G5 target function | explicit g and equivalence classes | N6 preserves honest scoped inference
G6 cross-protocol and risk | population bridge + outcome/loss correspondence + uncertainty | HOLD
G7 independent source | original external measurement with adequate claim-relevant dependence cut | HOLD
G8 implementation | Rust/Lean regression success on GitHub exact commit | PENDING at first authored commit

A projection certificate makes J **at least as informative as E** for decisions on the exact same Θ, since the receiver can discard Z. Strict quotient refinement is neither equivalent to strict Blackwell dominance nor necessary for stricter Bayes risk in a particular decision problem. The category-theoretic word 'morphism' does not itself generate epistemic authority. Neither more sensors nor more source files constitute independent scientific evidence without a corresponding dependency cut.

P1 can close in a narrow executable-math sense after tests pass. **Do not close MQR-4.100 as a scientific method discovery**; investigate in P2 whether realistic paired auxiliary sensors and target outcomes exist, and how uncertain/approximate kernel correspondences constrain conclusions (possible Le Cam deficiency sensitivity, not automatic theorem novelty).

## 4. Reproducibility

- Rust library: `experiments/mqr-4.100/src/lib.rs` (7 finite model/negative-control tests).
- Lean source: `experiments/mqr-4.100/lean/Mqr4100Refinement.lean` (no sorry/axiom; fixed-type projection and formal scopes).
- Dedicated read-only CI: `.github/workflows/mqr-4.100-p1-refinement.yml`. All GitHub commits must be human WhoSia authored; GitHub Actions can compute/upload artifacts but may not author commits. MAIN_ONLY. No deletions of historical code in P1.
