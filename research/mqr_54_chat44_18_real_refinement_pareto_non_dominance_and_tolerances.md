# MQR 5.4 · MQR44 R18 — No scalar score laundering in five real joint refinements

Date 2026-11-21 KST. This unit extends [R16](mqr_54_chat44_16_primary_refmac5_five_protein_success_and_failure.md) and the [publisher's original Rinaldelli et al. 2014 Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/#T1), DOI 10.1107/S1399004713034160. **Provenance:** exact calculations use rounded results published by the experimental authors; no original structural/nuclear-magnetic input files, uncertainty intervals, or fresh molecular refinement were obtained.

## The counterintuitive result

Across the *same five actual scientific systems*, every joint refinement improves the NMR restraint fit Q_RDC, **but every one also slightly worsens R_free**:

| PDB crystal source | Q_RDC before → after | R_free before → after | Strict Pareto dominance in (Q_RDC, R_free)? |
|---|---|---|---|
| 3SHI | .414→.160 | .264→.267 | Neither dominates |
| 3NHE | .360→.121 | .158→.160 | Neither dominates |
| 1IGD | .146→.081 | .132→.134 | Neither dominates |
| 1EXR | .398→.308 | .142→.147 | Neither dominates |
| 1YR5 | .540→.201 | .304→.307 | Neither dominates |

The trade-off is expected when adding NMR restraints, and *does not* mean the refinement failed: authors appropriately assess whether X-ray and geometric fidelity are **preserved within a scientifically acceptable tolerance** while the NMR fit improves. But there is **no objective, unweighted single 'progress score'** whose increase is proved by the numbers alone. If the goal were strictly minimizing R_free, all five additions would worsen that indicator. If the goal were decreasing Q_RDC while bounding R_free increases to tolerance, some are useful.

The code [mqr44_r18_refinement_pareto_and_threshold.py](../experiments/mqr-5.4/mqr44_r18_refinement_pareto_and_threshold.py) was executed locally with Decimal exact inputs. It asserts non-dominance for all five, sign changes, and sensitivity: authors' roughly Q_RDC<.20 heuristic yields **3/5**; permissive .202 would yield **4/5**, because peptide-bound CaM reaches .201. Therefore near-cutoff categorization depends on declared acceptance tolerance, but free CaM at .308 is not close to .20. **Do not apply cutoff .202 to the authors' actual claim**, it is a methodological stress test only.

## Important source logic

1. Q_RDC is primarily an in-sample NMR restraint fit; R_free is a held-out X-ray reflection diagnostic. These do **not** have equal epistemic meaning or comparable units; their signs alone are not equivalent evidence streams.
2. The author adjusts geometric restraints and weighting; too-flexible structures can artificially fit disparate observations while losing chemistry. The geometric parameters in the published Table 2 must be consulted before declaring any case 'successful'.
3. The failure to produce one adequate structure for CaM is **scientifically informative** about crystal-versus-solution regimes, conditional on trusted measurements and known methodological artifacts; not every difference proves true biological dynamics.
4. Different protein systems do not share one natural experimental uncertainty distribution, so 5/5 is **not** a random representative scientific success rate.

## Philosophy return

The strongest MQR outcome is not 'we discovered a universal score' but the exact separation:
- **preservation of established X-ray evidence** at acceptable target-dependent tolerances;
- **new NMR evidence compatibility** that may succeed or fail;
- **productive rejection** of a premature single-structure ontology, potentially opening new conformational questions.

The foundational 'why does mathematics work in engineering?' question is thereby illuminated: model fitting is not enough; geometry, physical preparation, domain-appropriate invariants, and held-out independent evidence determine usable scientific representations. This is a concrete mathematical-scientific counterpart to Mitchell's 2020 philosophy and earlier MQR non-scalar Pareto doctrine, not an independent mathematical theorem.

**Stop:** Do not tweak more thresholds absent physical calibration. Obtain original NMR/diffraction data and a before/after validation target, or backtrack to a different empirical example.

**Status:** published author-data arithmetic PASS; direct raw-data replay HOLD; classifying .201 as universally 'true identical' REJECTED; original theory novelty HOLD; MQR 5.4 OPEN; official 17 heterogeneous missing groups unchanged.
