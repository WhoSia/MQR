# MQR 46 (5.4) — Contact-stabilizer boundary: what establishes cross-science preparation identity?

**Status:** finite conditional result / explicit prior-art boundary / 2026-11-21.
**Root:** [MQR 5.4 constitution](MQR_5_4_OPEN_HORIZON_CONSTITUTION.md), particularly possible sciences, new observables, and open-ended inquiry. **Earlier assumptions:** [MQR 43 bridge](../language/real/experiments/unknown_preparation_bridge_v54.py) and [MQR 42 action alignment](../language/real/experiments/action_alignment_v54.py) presuppose either common outcome semantics or already shared preparations.

## 1. Different operations require different kinds of evidence

Let each science have its own preparation labels P_A,P_B, with |P_A|=|P_B|=n. The model contains (i) independently described local manipulation/accessibility graphs G_A,G_B; (ii) prospective verified physical handoffs h=(p,q); and (iii) an independently **justified relation-preservation hypothesis** R: an actual correspondence must be an isomorphism between these graphs. R is **stronger** than sharing a world: two same-world laboratories may possess different instruments and thus different action menus.

An authenticated **token** handoff alone is insufficient: the physical preparation may alter in transport. A certified contact requires both (1) source/destination token identity and (2) independently justified stability of the specific preparation. Code Boolean flags record **assumptions supplied by external evidence**, not mechanically generated certificates. Matching strings, measured numbers or files do not produce them.

## 2. Conditional stabilizer proposition and proof

Let Iso(G_A,G_B) be graph isomorphisms and C be genuinely certified contacts. Define

\[
\Phi(G_A,G_B;C)=\{\phi\in\mathrm{Iso}(G_A,G_B):\ \phi(p_i)=q_i\ \text{for all }(p_i,q_i)\in C\}.
\]

Without justified relation preservation, use *all* n! bijections instead of Iso. If Iso is nonempty, pick one isomorphism f: then every other isomorphism is uniquely f∘a for an automorphism a of G_A. Consequently |Iso|=|Aut(G_A)|. For compatible contacts, candidates form a coset of the pointwise stabilizer of the contacted A-vertices, with corresponding cardinality. Inconsistent contacts return the empty set, **not a forced best mapping**. This is elementary finite group/graph theory, **not a novel general theorem**.

**Four-state worked witness:** if both practices are the cycle C4, start with 4!=24 arbitrary matches. Assuming R leaves |Aut(C4)|=8. A certified handoff A0↔B0 leaves 2 orientations. A second handoff A2↔B2 (opposite) leaves **2**; instead A1↔B1 (neighbor) leaves **1**. Thus an independently authenticated contact can have zero or one bit of discriminating power depending on which physical object is selected. The result is *conditional* on trusted contact and relation invariance.

**Unresolved case:** if both accessibility graphs are complete K4, all 24 permutations are automorphisms; one certified anchor still leaves 6 candidates. Repeated native readings without new interventions or cross-lab events do not resolve the ambiguity.

## 3. Choosing the next genuinely achievable interaction

Partition the finite candidate set Φ by the hypothetical response q=φ(p) to a new physically certified handoff p∈P_A. Rank p by worst-case survivor count max_q |Φ_q|. Under an *optional uniform prior across the surviving mappings only*, expected survivor size is Σ_q |Φ_q|²/|Φ| and ideal expected information gain is

\[
I(p)=\log_2|\Phi|-\sum_q\frac{|\Phi_q|}{|\Phi|}\log_2|\Phi_q|.
\]

This is a decision heuristic given cost-free, error-free, preparation-stable transfer; **not an observed physical bit count or an objective entropy of the world**. The [code](../language/real/experiments/contact_stabilizer_v54.py) and [13 tests](../language/real/experiments/test_contact_stabilizer_v54.py) include an exhaustive sweep of 64 four-node graphs × 24 B-label permutations = 1,536 graph-pair cases (plus other regression examples).

## 4. Crucial counterexamples

1. **Same world, different available operations:** lab A uses a C4 accessibility graph, lab B a P4 path on the *same possible physical states*. Then enforcing graph isomorphism gives zero candidates even though shared physical preparations might exist. Different action menus ≠ different worlds. R itself needs independent validation, not dogmatic assertion.
2. **Same transported object, different preparation:** transport alters a temperature- or context-sensitive sample, so the material token remains identifiable but the state preparation is not stable. Such an event must not enter the certified contact set without independently checked state preservation.
3. **Same finite mapping, multiple unobserved ontologies:** a unique mapping under a fixed action menu is not unique underlying reality; two theoretical models can agree on all admissible experiments but diverge on future novel interventions.

## 5. How this changes the research question

The original [founder 2026-02-05 essay, directly re-read](mqr_54_mqr46_founder_structure_generativity_audit.md) distinguishes representation from world identity and asks how theories generate possible structures and questions. Our construction addresses the *earlier* stage of establishing what can count as a shared preparation. It does not yet generate new experimental primitives or show that an alien science can independently discover the same graph predicate.

The constructive path is **preparation contact → experimentally justified relation comparison → conditional identification → new action that could falsify that relation**. Do not equate success of graph isomorphism with ontological realism.

**Epistemic classification:** conditional finite operational model and familiar automorphism lemma; implementation and synthetic tests verified, no real authenticated alien-science handoffs observed, scientific/cross-ontology generality OPEN.
