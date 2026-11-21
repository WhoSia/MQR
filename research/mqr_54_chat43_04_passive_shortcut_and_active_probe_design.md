# MQR 5.4 — MQR 43 · 기록 04: Passive shortcut, active intervention necessity and finite query budget

**2026-11-21.** Conversation MQR 43, program version MQR 5.4.
**Status:** TWO COMPETING DESIGNS TESTED / 7 LOCAL TESTS PASS / REAL CONTACT AND INDEPENDENT OPERATOR SEMANTICS HOLD.
**Code:** [query optimizer](../language/real/experiments/native_bridge_query_design_v54.py) and [regression tests](../language/real/experiments/test_native_bridge_query_design_v54.py). Local tested bytes have identical Git blob hashes to GitHub copies. Previous conditional model: [record03](mqr_54_chat43_03_native_action_composition_and_bridge_symmetry.md).

## 1. An attack on the supposed necessity of joint actions

Record03 found that combining independently named A and B actions could reveal an A-native outcome unavailable from A's original recipe and action repertoire. But a **simpler experimental route** exists in its original three-state example.

If B's native readout (x,y,y) may be applied to an **authenticated A-prepared token**, then run two crossed *readout* queries:

1. A:seed → B:read (no primitive action, one physical contact).
2. A:seed → A:turn → B:read (one primitive action, a second independently prepared physical contact).

The signatures across the six possible hidden alignments fall into **three operational classes of size two**. No B:shift action is required to identify these classes. The optimal two-probe primitive action count is one under this particular cost model. Thus **cross-laboratory contact and paired readout can be enough**; one must not claim that action composition is *necessary* without excluding a simpler passive witness.

This shortcut is only available after genuine authenticated contact. Merely juxtaposing A-only and B-only historical catalogs does not give B's readout for the *A-prepared* token; record06 of MQR 42 already established that matching cannot be assumed.

## 2. Sensor-ablation adversary

Keep B's native action g=(1 2) but change its modeled readout to a **single constant opaque outcome**. B's existing sensor then tells us nothing about its latent state, even after a handoff. This is a deliberately weak instrument; B's ability to enact its native state-changing action remains an **analyst assumption**, not an independently observed physical fact.

With this constant B readout:
- Both passive crossed B-readout queries return the same symbol under **all six** alignments; no hypothesis class is separated.
- But A:seed → B:shift → A:read and A:seed → A:turn → B:shift → A:read generate respective A-native signatures (low,high), (high,low) or (low,low) across the three operational alignment classes, **each still of size two**.
- The B operation adds useful power only because A's sensor can read a consequence of B's otherwise opaque action. This is an example of **intervention/readout complementarity**, not evidence that an alien society has independently discovered an ontology.

The two query words contain respectively one and two primitive actions, so **three primitive actions total**. An exhaustive search over candidate A-final-readout words of length ≤3 and two-query choices shows that **no pair with action count below three** distinguishes all three classes. One A-binary outcome cannot distinguish three classes in a single run. The optimization counts neither repeated preparations, physical transfer, drift controls, randomization, nor independent action certification. It is not a physical cost estimate.

## 3. Why the residual factor of two persists

For both scenarios, the source of irreducible ambiguity is B's internal automorphism swapping native states 1 and 2 while preserving its action g, native recipes, and (both the coarse and constant) B sensor. Thus **π and π∘h remain operationally indistinguishable** under the allowed apparatus. The experiment can select a working operational translation *class*, not unique hidden-state labels. This is a representation-level obstruction, not proof that two worlds exist.

## 4. Acceptance ladder and next research split

| Level | What would justify it | This model |
|---|---|---|
| Native-only logs | Separate self-contained records | Yes (synthetic) |
| Crossed readout | Independently certified transfer of A-prepared material to B | Assumed only |
| Mixed action protocol | Same-token custody, relevant preparation stability, repeatable reset and execution of B action on transferred token | Assumed only |
| New executable question | A mixed word outside both old action grammars with independently measured differentiated output | Formal possibility only |
| Newly generated scientific concept | Independent native-agent problem formulation, nontrivial expressibility shift and novel world-facing consequences | Not shown |

This follows MQR's [MQR 42 handoff preregistration](mqr_54_chat42_04_physical_handoff_preregistration_and_falsifiers.md). No fictitious material, native sensor, experimental shift or signed transfer receipt is created by a Boolean flag.

## 5. Prior art and director's return

Active automata learning treats black-box interaction as action/observation queries and compares candidate models by falsifying experiments: [AALpy](https://doi.org/10.1007/s11334-022-00449-3). The experimental reset and reliable step interface are themselves prerequisites, not outputs of that algorithm. Gate-set tomography's gauge freedom provides a useful conceptual reminder that operational data need not select a unique representation: [Blume-Kohout et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5330857/). For the problem of how *new scientific categories* arise rather than merely more queries, return to [Feest & Steinle (2012), held original source](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view) and the project's 2026-02-05 founder manuscript.

**Director verdict:** A new operator word can *conditionally* widen experimental ability, but it may be unnecessary if existing cross-lab sensors suffice, and it cannot by itself establish conceptual genesis. The next valuable test would give the two agents **local models only**, let them choose discriminating native queries without disclosing π, and require a certified transfer procedure producing **held-out predictions**. Prevent an oracle from silently leaking the common state mapping. Run a separate BFS on how successful problem-creation differs from conventional model identification rather than promoting a trivial semigroup result into a new philosophy of science.
