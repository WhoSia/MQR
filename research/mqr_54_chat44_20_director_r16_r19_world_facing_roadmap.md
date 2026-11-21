# MQR 5.4 — MQR44 R20 | Director checkpoint: physical structural disputes as question generators

Date 2026-11-21 KST. Evidence-typed research decision, not a phase upgrade.

## What was achieved

1. [R16 primary protein experimental table](mqr_54_chat44_16_primary_refmac5_five_protein_success_and_failure.md): Rinaldelli et al. 2014 five REFMAC5 X-ray/NMR joint refinements, independent arithmetic on AUTHOR'S published summary (not a raw data rerun). [Executable script](../experiments/mqr-5.4/mqr44_r16_published_refmac5_table.py): five of five NMR Q_RDC values improve; three joint results below authors' .2 heuristic; two above, with one borderline. Eight local exact assertions PASS.
2. [R17 original PDB metadata](mqr_54_chat44_17_pdb_chain_specimen_and_refinement_identity_gate.md): PDB 3NHE is a USP2a–ubiquitin complex, not a standalone purified ubiquitin crystal. 1EXR is calcium-bound calmodulin. Neither full deposited model and publication's refined target can be equated without specific chain/residue/preparation mapping. Direct mmCIF download was blocked, no new source bytes downloaded.
3. [R18 published data multi-objective audit](mqr_54_chat44_18_real_refinement_pareto_non_dominance_and_tolerances.md): Q_RDC falls in all five but R_free rises slightly. No before/after strict Pareto dominance on those two objectives. Arbitrarily changing the NMR tolerance from .200 to .202 changes the binary label of the 0.201 calmodulin–DAPk case; this is an artificial sensitivity check, not published empirical calibration. [Code](../experiments/mqr-5.4/mqr44_r18_refinement_pareto_and_threshold.py) run locally.
4. [R19 cross-domain return](mqr_54_chat44_19_cortical_bone_stem_cells_real_science_bfs.md): Gustafsson et al. 2020 cortical bone micro-CT-oriented mesoscale XFEM predicted qualitative parallel/perpendicular osteon crack-path trend as reported in the experimenters' abstract. Fagan 2016 stem-cell model/experimental collaboration failed under divergent norms of adequate explanation, per her abstract. Neither raw meshes nor full Fagan article was independently reprocessed.

## Scientific conclusion and rival challenge

Disagreement can generate new, scientifically answerable questions only when an independently supported residual is distinguished from uncorrected sensor, sample, geometric and model/weighting artifacts. A successful unified model is one possible outcome, not the definition of rational cooperation. The actual authors already proposed the complementary refinement strategy and its failure limit; MQR does not claim to have discovered this mechanism or new biophysical data.

### Prospective next physical source gate

Use deposited 1EXR calmodulin for a negative control and 1IGD GB3 as a positive control because the published five-protein case varies in joint compatibility. Before raw-replay claims: retrieve original diffraction structure factors/R-free flags, exact measured RDC/PCS source arrays, chain/residue mapping, conditions/calcium/peptide status, software version and full weight geometry protocol, with source bytes/hashes and independently frozen outcome criteria. Run crystal-only and joint trials, weights ablations and a non-single-structure alternative; compare the SAME primary-source fit metrics. If source bytes inaccessible, do not extract fabricated raw values from chart images. Retain HOLD.

### Open horizon

Return to the founding question: can two science practices use contact with the same world to learn when their concepts apply to truly different physical regimes, without being forced to adopt one complete theory/dictionary? Also explicitly compare why mesoscopic engineering mathematics can be effective for crack propagation targets and why differing goals may make shared stem-cell explanation unratifiable. These are independent branches of MQR 5.4, not a reduction to protein chemistry.

**Authority:** Published experimental Table 1 arithmetic verified; independent primary raw/world measurement not executed. Official 17 historical mixed source groups unchanged, new 2014 article and 2016/2020 originals are additional bounded intake radar only. MQR 5.4 OPEN. Novelty HOLD; no Harvest promotion; no Drive files moved.
