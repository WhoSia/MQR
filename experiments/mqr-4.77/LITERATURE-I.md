# MQR-4.77 — Literature Collision I

Status: **PRIOR-ART ABSORPTION / RESIDUAL NARROWED / PRESEAL UNCHANGED**

## 1. Internal ancestor

MQR-0.4-C/D already owns the first-order claim that latent dependency graphs are generally partially identified, that perturbational response geometry need not identify latent causes, and that finite perturbation diversity cannot be promoted to ontic independence.

Therefore MQR-4.77 does not claim novelty for latent common causes, correlated measurement error, graph non-identifiability, or perturbational signatures.

## 2. Causal graph equivalence classes

Hauser & Bühlmann (2012) and Yang, Katcoff & Uhler (2018) formalize observational/interventional Markov equivalence classes: observational or even interventional data may identify only an equivalence class rather than one unique DAG. Interventions can refine that class.

Sources:
- https://www.jmlr.org/papers/v13/hauser12a.html
- https://proceedings.mlr.press/v80/yang18a.html

Absorption:
- GRAPH_FIT != GRAPH_IDENTIFICATION
- one selected graph is not an identified dependency ontology
- intervention families refine, but do not automatically collapse, graph ambiguity

## 3. Local identification without full-graph recovery

Jaber, Zhang & Bareinboim (2019) develop causal identification directly under graph equivalence classes; Gupta, Childers & Lipton (2023) emphasize that local causal quantities may be identified without globally recovering the entire causal graph.

Sources:
- https://proceedings.mlr.press/v97/jaber19a.html
- https://proceedings.mlr.press/v213/gupta23b.html

Plan-changing consequence:

**FULL DEPENDENCY-GRAPH IDENTIFICATION IS NOT NECESSARY FOR EVERY LOCAL AUTHORITY CLAIM.**

MQR-4.77 therefore tests whether all currently live graph alternatives agree on the claim-relevant cut, not whether every edge in the world has been recovered.

## 4. Latent confounding and proxy / negative-control identification

Proxy-variable and proximal-causal-inference results show that hidden confounding may sometimes be addressed using suitable proxies under explicit rank/completeness assumptions, while negative controls can diagnose hidden bias only under their own validity assumptions.

Sources:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7746017/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/
- https://academic.oup.com/ije/article/55/5/dyag163/8776067

Absorption:
- negative controls are not generic independence certificates;
- a null negative control is not proof that no hidden common mode exists;
- proxy-based identification requires structural assumptions and can identify a target without identifying the entire latent measurement mechanism.

## 5. Metrological traceability

NIST/VIM define metrological traceability through an explicit calibration hierarchy / unbroken calibration chain, with each link contributing uncertainty. Traceability is a property of a measurement result, not automatically of a device or laboratory, and does not itself guarantee fitness for purpose.

Sources:
- https://www.nist.gov/metrology/metrological-traceability
- https://jcgm.bipm.org/vim/en/2.41.html
- https://jcgm.bipm.org/vim/en/2.40.html

Absorption:
- DIFFERENT_INSTRUMENT != DIFFERENT_CALIBRATION_ANCESTRY
- DIFFERENT_LAB != DIFFERENT_REFERENCE_CHAIN
- traceability documentation is ancestry evidence, not a scalar independence score

## 6. Shared preprocessing / leakage

Kapoor & Narayanan et al. show that data collection, sampling and preprocessing can create leakage and spuriously optimistic scientific conclusions across many ML-based fields. Later guidance emphasizes that complex dependency structure can hide such leakage.

Sources:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/
- https://www.nature.com/articles/s41592-024-02362-y

MQR consequence:
- INDEPENDENT_DATASET != INDEPENDENT_ANALYSIS_ANCESTRY
- preprocessing can preserve a common-mode route even when raw observations differ

## 7. Formal mathematics boundary

MQR-4.76 already established:
- independent proof checking != independent formalization;
- checker plurality can strengthen proof-software custody while preserving common formalization ancestry.

4.77 does not claim generic novelty for proof checking or trusted kernels. Its mathematical stress lane asks only whether a proposed break in formalization/encoding ancestry is locally identified or remains compatible with a hidden shared route.

## 8. 2026 latent-confounding update

Recent causal-discovery work continues to characterize interventional equivalence classes in the presence of latent confounding and soft interventions rather than treating one recovered graph as automatically unique.

Source:
- https://proceedings.mlr.press/v306/zhou26s.html

This strengthens the open-world / equivalence-class firewall but is not itself an MQR contribution.

## 9. Surviving MQR-4.77 residue

After absorption, the surviving claim is constitutional and narrower:

> A 4.76 break certificate should carry only the authority shared by all live dependency-graph alternatives on the claim-relevant path. Full graph recovery is unnecessary when those alternatives agree locally; one selected graph is insufficient when they disagree. Targeted separators can refine this authority, and later hidden-common-mode reconstruction can reopen it.

This is not a new causal-discovery algorithm, a new negative-control estimator, a new metrology ontology, or a new proof-verification theory.

## 10. Novelty firewall

No novelty credit for:
- Markov/interventional equivalence classes;
- causal discovery under latent confounding;
- negative controls or proximal causal inference;
- calibration hierarchies / traceability;
- preprocessing leakage taxonomies;
- proof checker / kernel independence.

Candidate MQR residue:
- typed break-identification status on top of 4.76 authority transport;
- graph-equivalence-class-relative cut authority;
- local agreement criterion for authority upgrade without global graph recovery;
- explicit reopening when later ancestry reconstruction crosses the claim-relevant cut.
