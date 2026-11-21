# MQR 5.4 — MQR 43 · 기록 05: Alignment-blind active protocol selection and held-out operational prediction

**2026-11-21, conversation MQR 43; research version MQR 5.4 remains open.**
**Status:** EXACT SIMULATOR-BOUND ACTIVE LEARNING / 8 NEW LOCAL TESTS PASS / PHYSICAL ORACLE, SELF-GENERATED CONCEPTS AND INDEPENDENT PREDICTION HOLD.
**Code:** [active learner](../language/real/experiments/native_bridge_active_learner_v54.py), [eight tests](../language/real/experiments/test_native_bridge_active_learner_v54.py). The executed local file blobs match GitHub copies. Predecessors: [record03](mqr_54_chat43_03_native_action_composition_and_bridge_symmetry.md) and [record04](mqr_54_chat43_04_passive_shortcut_and_active_probe_design.md).

## 1. The remaining complaint: an omniscient analyst chose the decisive probe

Records03–04 exhibited conditional joint action gain and optimal short probes by exhaustively comparing all six hidden alignment models. But those were **selected by an analyst who knew the candidate worlds**. A more serious prospective procedure must choose the next native action word without reading the simulator's *actual* alignment and update its beliefs only after an admitted common-token output is returned.

This experiment adds a strict model/oracle interface, while acknowledging that the candidate library, action alphabet, initial recipes, and readout semantics are still explicitly provided by the analyst. It is therefore **hypothesis selection**, not automatic discovery of an alien language or a new conceptual primitive.

## 2. Frozen candidate family and query policy

The learner begins with six B-to-A permutation hypotheses. Its candidate probe menu consists of all finite native words of length at most 3 using A:turn and B:shift, with an A-native or B-native final readout. At each step it computes each query's predicted output **for the surviving candidates only** and chooses a query with the smallest maximum predicted candidate bucket; ties favor fewer primitive actions. The predicted buckets are calculated **before** requesting the hidden oracle's response.

A separate simulator oracle privately contains the actual alignment and returns **native outcome symbols**, never hidden state indices or an actual permutation. The learner keeps only a ledger of query word, reader, returned native symbol, candidate count before and after. It must not execute without an externally supplied token/preparation/reset receipt; these flags are modeled assertions, not fabricated physical authentication.

For the original B sensor (x,y,y), the selected first query is **A:seed → B:read**; when this leaves four candidates a second **A:turn → B:read** reduces them to two. For the constant-output B sensor ablation, the first query becomes **B:shift → A:read** and, when required, the second **A:turn → B:shift → A:read**. This is the exact passive/active distinction from record04, obtained **without revealing the true alignment before query selection**.

## 3. Results and decisive incompleteness

- For all six possible hidden alignments and either B sensor configuration (12 simulated worlds), learning terminates after at most two queries with **two surviving permutation hypotheses**. That residue is exact and cannot be eliminated by further words under the frozen apparatus, because π and π∘h are operationally equivalent.
- A previously unused three-action word B:shift → A:turn → B:shift is predicted identically by each surviving pair. It is tested against the **same synthetic oracle**, and the exact predictions agree for all 12 simulated worlds. This is a *simulator held-out consistency check*, **not** independent experimental confirmation or a prospective real-world validation.
- Model-class failure is handled transactionally: an output that no surviving hypothesis predicts raises a visible error without changing candidates or ledger. A repeated query, malformed probe, mismatched sensor exposure, unverified token handoff, unstable preparation, or failed reset similarly fails closed.
- The test suite verifies **8/8** additional tests for hidden-oracle separation, both sensor modes, held-out non-reuse, valid-but-unpredicted native output, failure after state, and gate checks. **Cumulative MQR 43 local tests through this record: 35/35** (previous 12 + record03 8 + record04 7 + record05 8). This does **not** represent whole-Real-Lang/whole-repository integration.

## 4. Why this is not L3 concept creation

The learner may discover a **new mixed query word in the union of two native action alphabets**, but the analyst has already defined the alphabets, candidate alignments, output types and truth simulator. There is no internal creation of a new scientific quantity, no learning of unknown operators from scratch, no proof that native researchers themselves formulated the question, and no physical communication channel.

A staged claim hierarchy is therefore mandatory:

1. **Computational:** an algorithm can choose a finite discrimination query without peeking at the hidden oracle alignment — **PASS LOCAL**.
2. **Operational contact:** actual labs can authenticate identical material/preparation and exercise both native actions with controlled order — **HOLD**.
3. **Prospective model learning:** a genuinely independent device can yield an untrained native outcome on a preregistered held-out query — **HOLD**.
4. **Concept/problem genesis:** the new experimental operation forces a nontrivial extension of the researchers' own conceptual language, with a world-facing consequence not contained in the old language — **HOLD**.

## 5. Strong prior art and intellectual direction

Query-based active automata learning already separates a learner from a black-box system under test, uses action-word output queries, reset semantics and counterexample-driven hypothesis refinement. The especially relevant reference is [AALpy: an active automata learning library (2022)](https://doi.org/10.1007/s11334-022-00449-3), whose actual implementation is far broader than this three-state model. [Gate-set tomography](https://pmc.ncbi.nlm.nih.gov/articles/PMC5330857/) supplies an independent example of representation/gauge ambiguity; no novelty is claimed for that idea.

The MQR-specific value is **epistemic scope control**: replacing an unjustified absolute translation claim with a typed operational class and a reproducible, failure-aware native-query sequence. Consistent with [the 5.4 open-horizon constitution](MQR_5_4_OPEN_HORIZON_CONSTITUTION.md), the next DFS must find a *world-facing instrument* whose new action can be certified rather than hand-supplied, while the next BFS should study scientific *question formation* through [Feest and Steinle's held 2012 source](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view) and the February 2026 founder manuscript. New mathematics is not the prerequisite; a richer genuinely testable question is.

**No automatic promotion:** MQR conversation 43 is not MQR research version 5.5, nor evidence of L3. Preserve this as a reproducible conditional candidate for further research.
