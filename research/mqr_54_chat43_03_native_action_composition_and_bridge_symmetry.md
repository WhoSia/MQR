# MQR 5.4 — MQR 43 · 기록 03: Native action composition and residual bridge symmetry

**2026-11-21.** Conversation MQR 43; research program remains **MQR 5.4**.
**Status:** FINITE CONDITIONAL L2 POSSIBILITY / EXTERNAL PHYSICAL HANDOFF HOLD / L3 CONCEPT GENESIS HOLD.
**Executable:** [model](../language/real/experiments/native_composition_bootstrap_v54.py) and [8 local tests](../language/real/experiments/test_native_composition_bootstrap_v54.py); both source files' Git blobs matched the actual locally executed bytes.

## 1. The restored question and the model's limited scope

The founding MQR question is how distinct sciences with incompatible basic vocabularies might develop new questions after actual contact with one world. This note addresses only whether two independently named actions can generate a new observable experiment without an upfront shared state *dictionary*. It does not construct a new scientific ontology.

For proof only, an analyst posits S={0,1,2}. Lab A prepares native recipe A:seed in state 0, operates f=(0 1), and reads (low,low,high). Lab B operates g=(1 2) in B-local coordinates and reads (x,y,y). B can prepare either native B:clear at B-local 0 or native B:mixed symmetrically over local 1 and 2. Neither lab is given the analyst's state names or the other lab's action labels. A hypothetical common-token handoff has six possible B-to-A hidden alignments π.

An analyst predicts shared-token experiments by transporting B's native operation as g_π=π∘g∘π^{-1}. Under the identity alignment, A-only words cannot leave {0,1} from recipe A:seed and therefore always produce low. However:

| Shared-token word, A-native final readout | Result under π=id |
|---|---|
| A:turn, then B:shift | high |
| B:shift, then A:turn | low |

Both mixed transformations are absent from either single-lab monoid {id,f} and {id,g}; the generated joint monoid has six distinct transformations rather than two. This is **conditional newly executable action-word and outcome growth** (formal L2 possibility), not a demonstrated experiment.

## 2. Every native-only record remains compatible with six bridges

No local-only A or B experiment depends on π: native preparation and action words are evaluated entirely in native coordinates. The difference concerns actual common-token contact. Two proposed cross-action probes produce these exact predictions:

| (A:turn→B:shift, B:shift→A:turn), A-native readouts | Compatible alignments |
|---|---:|
| (high,low) | 2 |
| (low,high) | 2 |
| (low,low) | 2 |

The final class has **no effective new action**: the translated B action equals A's f and the combined monoid remains size 2. Therefore simply connecting two nominally distinct laboratories does not guarantee an increase in experimental power.

The irreducible factor of two has an exact symmetry explanation. The B-local permutation h=(1 2) commutes with g, preserves B's sensor output partition, and preserves both B preparations (clear and symmetric mixed). Hence π and π∘h induce exactly the same transported B action, readout and preparation distributions. **Every** allowed joint experiment has the same outcome under these paired alignments, not just the finite word samples. Exhaustive code checks all words of length at most five as regression; the underlying symmetry gives the unrestricted proof.

Thus six hypothesized absolute state-label mappings reduce at best to **three operational equivalence classes**, each containing two mappings. The residual distinction is analogous to representational gauge redundancy; it is not itself evidence of competing realities.

## 3. Evidential and conceptual gates

The code's transfer receipt flags represent analyst-provided assertions that the same token was authenticated, its relevant preparation survived, and reset worked. A positive Boolean flag does **not** constitute a real physical certificate. With any false flag the modeled result is withheld. A physical L2 claim needs witnessed cross-laboratory action execution, repeatable new outcomes and rival-dependent prospective tests. There is no such physical receipt yet.

The action symbols and candidate translations are assigned by the analyst. This only makes a mixed question *formally expressible*; it does not establish L3 self-generated concepts, an intrinsically superior ontology, or genuine alien-science communication. The experiment must also survive the **passive-readout shortcut** evaluated in [record04](mqr_54_chat43_04_passive_shortcut_and_active_probe_design.md).

## 4. Prior art and research-director ruling

- [AALpy active automata learning](https://doi.org/10.1007/s11334-022-00449-3): black-box action-word input/output queries, resets and falsifying counterexamples are established techniques.
- [Blume-Kohout et al. (2017), gate-set tomography](https://pmc.ncbi.nlm.nih.gov/articles/PMC5330857/): operational reconstruction need not fix a unique representation, a related gauge caution but **not** a proof of this particular example.
- [Feest and Steinle (2012), Scientific Concepts and Investigative Practice](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view): the interaction of concepts and investigative practice is prior philosophical context.

**MQR contribution type:** narrow synthesis, finite counterexample and no-go, and a testable protocol hypothesis; **not** first discovery of active learning, group symmetry or concept creation. The 5.4 founding program remains open. The next question is whether the actors can independently construct the discriminating action words and authenticate the handoff without borrowing the analyst's hidden coordination.
