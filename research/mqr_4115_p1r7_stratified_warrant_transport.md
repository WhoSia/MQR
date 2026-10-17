# MQR-4.115 P1-R7 — Stratified Warrant Preservation Under Proof Quotient

2026-10-17. Extends [P1-R6](mqr_4115_p1r6_contextual_proof_congruence.md) and recovers Notion ledger lag. **Bounded formal stage; no new empirical independent witness.**

## Three judgment layers
- J0(c): at least one undefeated eligible evidence witness exists.
- J1(c): at least two eligible witnesses possess distinct **certified** lineage roots and an independently verified independence certificate. A distinct root ID is at most a necessary proxy, not a sufficient scientific witness of independence.
- J2(c,k): J1 holds and admissible witnesses meet a context-specific strength threshold and defeat checks; the toy implementation uses threshold >=2.

The toy program `experiments/mqr-4.115/p1r7_witness_judgments.py` uses `a.root != b.root` as a **toy stand-in**, not external certification. The finite tests demonstrate representation split, weaker evidence, defeat, and harmless syntactic duplication. Five checks executed locally and passed. No remote CI or human-certified physical source independence.

## Countermodel results
original J0/J1_proxy/J2_proxy = 1/1/1
split_same_root = 1/0/0
independent_weak = 1/1/0
defeated = 1/0/0
syntax_duplicates = 1/1/1

## Proposed proof-class condition
For category C of evidence derivations and congruence ~ on admissible parallel arrows, form C/~ only if all composition and context/defeater/lineage obligations are respected. To preserve J0, a sound transport and reflection of inhabited proof classes suffices (surjectivity is stronger). To preserve J1/J2, transport must additionally reflect and preserve certified independence hyperedges, source-ancestry provenance, strength predicates at each threshold and defeater eligibility. A full bijection of raw graph nodes is unnecessary, but proof-class congruence alone does not certify these enriched structures.

Mathematical lemma: any translation inducing equivalences on the sets of all eligible proof-class combinations **with the extra independence and strength annotations** preserves J0/J1/J2. This is a conditional transport lemma by witness selection, not a discovery of categorical novelty, nor proof that empirical calibration/citation roots are independent. Distinct labels are not certified independent evidence.

## Harvest status
Reuses prior `Harvest_LR-20260905-A` W05 (holdout reuse), K02 (directional detection implication), K04 (logic vs causal influence), C2 (prior cross-source hypothesis); no new Harvest fragments or counts. For Greenberg (2009) source, the bounded earlier 161 edge citation subset, 45 cited targets, 7 ambiguous rows and original PDF remain unchanged. No new Table 4 visual-row certification claimed.

## Ledger
P1-R5 and R6 were saved to GitHub but not synced to Notion owing to synchronous write blocks. A later minimal **asynchronous** Notion content insertion and exact targeted update both reached `succeeded` and were re-fetched. Use small async inserts with task polling and re-read instead of confusing acceptance with completion.
