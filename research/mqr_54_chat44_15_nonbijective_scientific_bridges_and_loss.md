# MQR 5.4 · MQR 44 · Record 15 — Nonbijective bridges: when a lossy translation is still scientifically legitimate

**2026-11-22 KST.** Exact finite synthetic result, code locally executed and passed after fixing an initial test implementation bug; MQR 5.4 OPEN. This corrects the misleading assumption in record10 that a foreign scientific language must admit a one-to-one outcome dictionary.

## 1. Formal example
Source scientific language L_A distinguishes equiprobable values A={0,1,2}, target interface L_B distinguishes B={left,right}. Assume the desired target marginal is p(left)=2/3, p(right)=1/3 and a *deterministic total* outcome map f:A->B. Three possible coarsening maps fit this marginal: the single source state mapping to right can be 0,1, or 2. By themselves, the two marginal datasets do not identify which three-to-two map is the actual correspondence. One validated anchor 0->left reduces possible maps to two; two distinct validated anchors 0->left and 1->left leave one. Contradictory anchors requiring all three source states to be left leave zero maps under the target marginal.

For each admitted map, conditional H(A|B)=2/3 bits because the two-to-one category retains two equiprobable source distinctions within an event of probability 2/3. This is strictly positive information loss despite successful exact prediction of B through f. The number is **exact** in this two-and-one cardinality model, not a general quantum/information-theory law.

Local verified code: `language/real/experiments/mqr_nonbijective_bridges_v54.py`, PASS string: 'PASS nonbijective: 3->2->1 candidate coarsenings, H(A|B)=2/3 bits'. The first local test incorrectly compared floating logarithms for exact equality; it failed and was repaired by a correct exact rational formula for the specific fiber sizes **before commit**. This test debugging is an engineering verification, not theoretical evidence.

## 2. What counts as success?
If scientists only seek to predict the target coarse observable B, f can be an **adequate operational translation**, even though it is not invertible and fails to convey all source distinctions. If they seek to distinguish all three A classes or to transfer interventions acting differently within the size-two fiber, f alone is insufficient. If different interventions distinguish states collapsed by B, the recipient may require (i) a finer local measurement, (ii) a context-indexed translation, or (iii) a state-dependent probabilistic kernel, not necessarily a global bijection.

Consequently MQR's translation criterion must be **goal-, intervention-, and scope-relative**:
```
BridgeContract := (
 source_linguistic_types, target_linguistic_types,
 candidate_mappings, anchored_joint_events,
 operations_to_preserve, hypotheses_to_distinguish,
 resolution_scope, evidence_provenance,
 losses_and_nonidentifiabilities, excluded_claims
)
```
The legitimate epistemic state is **identified set of candidate bridges**, not necessarily a single winning map. This aligns with earlier MQR typed transport and identified-set policies, but must not misstate a toy deterministic function as a demonstrated translation of genuinely alien ontology.

## 3. Adversarial counterexamples and prior art
- A bijection is often impossible if native category cardinalities differ; that alone does **not** prove Kuhnian incommensurability.
- A coarse map can be decision-sufficient for one operational purpose while scientifically inadequate for another. Decision theory's Blackwell comparison and statistical sufficiency are important predecessors, not mere decorative citations.
- Distinct surface names may refer to nearly identical phenomena; conversely same names can hide different experimental distinctions. Algebraic isomorphism does not force semantic equivalence.
- If actual category frequencies are not uniform or scientifically stationary, a map that appeared identified in a small sample need not be unique outside its support.
- If target categories are fuzzy/probabilistic, deterministic map family is misspecified.
- Conflicting anchors do not authorize hiding the data; show NO FITTING MAP and revisit assumptions, measurement or category definitions.

## 4. Relation to Faraday's historical record
The 12 September 1821 Faraday letter confirms that the old attraction/repulsion categories were reinterpreted by rotational motion (see R14), **not** that Faraday performed a literal mathematical 3->2 coarsening. The formal example is an illustrative diagnostic of concept alignment; its transfer to early electrodynamics requires reconstructing actual experimental distinctions and mapping contracts from dated sources.

## 5. Next strong gate
Compare coarsenings under a set of **interventions**. Show a concrete example in which f preserves predictions on the passive observation domain but fails after an action that separates source states within a fiber. Then ask whether a context-aware partial interface, rather than a universal dictionary, resolves the problem. Compare against the social diffusion of apparatus in R14 without conflating observed letter delivery with actual recipient scientific uptake.

**Decision:** mathematically scoped nonbijective bridge result PASS; historical causal / semantic application HOLD. Source registry counts unchanged; no 5.5 promotion.
