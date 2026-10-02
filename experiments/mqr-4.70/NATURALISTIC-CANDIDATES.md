# MQR-4.70 — Naturalistic Candidate Freeze

Status: **CANDIDATE-SELECTION-FROZEN / OUTCOME-READ-NOT-YET-AUTHORIZED**

## Primary lane — K562 Perturb-seq

Source lineage:
- Replogle et al. 2022 genome-scale Perturb-seq.
- Public processed datasets and SRA metadata.
- K562 genome-wide and essential-scale screens.
- 2025 causal-network analyses provide independent downstream use of the same experimental family.

## Pre-outcome question

Can a predictive state built from a metadata-selected subset of gene perturbations remain coarse, while predeclared held-out perturbations refine distinctions among histories/models that were equivalent under the restricted family?

## Selection rule

The current-family subset must be selected using metadata only:
- perturbation target identity;
- screen membership;
- cell line;
- collection day;
- declared quality/coverage metadata available before response analysis.

Expression-response outcomes may not be used to choose the current family or held-out family.

## Primary comparison

Current family:
a bounded metadata-selected subset of K562 perturbations.

Held-out family:
a disjoint predeclared set of K562 perturbations from the same source experiment.

Readout:
compare the induced model/history equivalence relation under current-only versus current-plus-held-out response features.

## Promotion criterion

Naturalistic contact requires:
1. current-family equivalence classes fixed before held-out response reveal;
2. at least one held-out perturbation that prospectively refines a current class;
3. a null held-out perturbation that leaves at least one class unchanged;
4. result stability under a second metadata-only subset rule;
5. comparison against ordinary identifiability / experimental-design baselines.

## Failure conditions

- outcome-informed subset selection;
- changing the held-out family after response inspection;
- treating any refinement as MQR novelty without baseline comparison;
- claiming genome-wide completeness;
- using one method's learned network as unquestioned ground truth.

## Secondary lane — systems-biology model discrimination

Use published model-discrimination settings where different experimental conditions alter distinguishability of candidate models.

Role:
naturalistic replication of family-relative distinguishability, not primary promotion evidence.

## Exact control lane — active automata learning

Use finite-state test suites as a formal control domain for:
- alternative minimal test families;
- completeness assumptions;
- counterexample discovery;
- family restriction and extension.

This lane carries no naturalistic scientific-world promotion credit.

## Current authority

No naturalistic outcome has been opened in MQR-4.70.

The candidate freeze only authorizes future acquisition and comparison.
