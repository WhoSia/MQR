# MQR-4.115 P1-R6 — Contextual Proof Congruence and Harvest Backflow

2026-10-14. Formal work continuation after P1-R5. MQR-4.115 OPEN.

Let C be the typed free path category of the provenance graph. A context-indexed admissible proof structure P(c,k) contains only derivations satisfying authenticated source lineage, claim scope, dependency independence and defeater obligations. An equivalence ~ of proof objects must (i) relate only parallel proofs with the same contextual conclusion; (ii) preserve admissibility in both directions; (iii) preserve externally authenticated source-root and defeater obligations; (iv) be a *congruence* under every defined pre- and post-composition of admissible proofs: f~g implies h∘f~h∘g and f∘j~g∘j wherever well typed and admissible.

If these conditions hold, composition [g]∘[f]=[g∘f] is well-defined in the quotient proof category. Proof: substitute equivalent representatives one argument at a time and invoke congruence twice. This is a standard quotient-category construction, not a claim of original categorical novelty.

If a representation map between the valid quotient proof categories is conclusion/context-preserving, sound on valid classes and essentially surjective on each fixed claim's admissible proof classes (ordinary surjective sets suffice), it preserves existence of a proof in both directions. This is conditional and does not establish independence certification for original Greenberg citations.

Counterexample: two proofs f and g with identical citation target but distinct source-root identifiers need not be equivalent. An extension h that checks independent ancestry can admit h∘f and reject h∘g. If a proposed ~ identifies f~g, it violates admissibility stability under postcomposition; the putative quotient is unsound. Another counterexample: directional fault detection A=>B (Kuhn K02) does not imply B=>A, so symmetrizing the preorder can identify genuinely distinct tests and violate proof obligations.

Harvest bridge: existing Harvest_LR-20260905-A W05 (reused holdout not fresh independent validation), K02 (asymmetric fault-detection implication), K04 (logical sensitivity vs real-world causal claims) and C2 (the original Harvest author's cross-paper question). This is a lineage link to already harvested interpretations, not a new Harvest fragment or independent external corroboration. From Research OS intake/Harvest P13, the model discrepancy and discriminating experimental designs remain method candidates, not evidence for authority causality.

Greenberg original supplementary PDF Drive ID 1N7iO3C15_dCjANtX0FLxPAWqTKE5NzJN. Current P1-R5 limited certified 161 transcribed edges, 45 targets; seven column-ambiguous rows excluded, no physical independence witnesses. New P1-R6 is theoretical and has no new citation extraction or executable CI in this commit.

NEXT: Find a minimal non-congruent equivalence counterexample with a small typed category, separate 'transport preserving existence' from 'transport preserving evidence strength', and visually resolve Greenberg Table 4 ambiguous column alignment before changing empirical edge totals.
