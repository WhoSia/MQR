# MQR 5.4 — MQR 42: The Genesis of Scientific Questions, Exploratory Protocols, and Model Failure as a Resource

Date: 2026-11-10 (KST). Status: SOURCE-BOUND HISTORICAL SYNTHESIS + EXACT FINITE ENUMERATION / NO EMPIRICAL CERTIFICATION. This is a same-version continuation of MQR 5.4; not a new version.

## 0. Origin and methodological guard

From MQR 40 closing directives, the project must not relapse into endless critique of Wedgwood, Regnault, or Chang: there are several ambitious founding questions, including the conversion of UV–Vis observations to circuits, possible alien sciences, paradigm-genesis, and the emergence of concepts not yet expressible. Depth must return to breadth (DFS/BFS). Here the selected DFS is **how scientific questions become materially possible**, not merely how already-formulated problems are solved. Its origin is linked to the user's earliest HWPX 'explanation to structure generation' problem.

## 1. Direct source reading: Maxwell's modeling choices are not an algorithmic theorem

Nersessian (2008), *Creating Scientific Concepts*, MIT Press, held full-text searchable scan in Drive: https://drive.google.com/file/d/168Yv277pBhy--iQrNjhMWbYcFhVx3_KR/view ; DOI https://doi.org/10.7551/mitpress/7967.001.0001 . Directly inspected Chapter 2 discussion around printed pp. 23, 30 and 45 onward, especially §2.2 Model 2 idle-wheel and §2.2.3 Model 3 elastic-vortex models; also Ch. 1 and excerpts of Ch. 5. Nersessian argues Maxwell's dynamically simulated vortex models generated internal mechanical failures: adjacent vortices' contact and friction raised a jamming problem; mechanical 'idle wheels' were repurposed as intermediaries, subsequently with translational motion to model current; subsequently vortex elasticity enabled modeling electrostatics. This was neither a predetermined dictionary translation from mechanics to electrodynamics nor a simple accumulation of instrument readouts. Historical accuracy ceiling: interpretation through Nersessian's historical reconstruction; Maxwell's own unseen draft candidates are not recoverable, and in Nersessian's discussion his archive is incomplete. The fluid vortices and idle wheels are heuristic historical scaffolding, **not accepted contemporary subatomic machinery**.

Haueis, 'Exploratory Concept Formation and Tool Development in Neuroscience', author accepted manuscript held Drive https://drive.google.com/file/d/1EqY18HPcrti7CF30nGnc4KS0EV67NbEh/view ; DOI https://doi.org/10.1017/psa.2022.79 . Inspected §2 Table 1, passages on 'default mode' emerging via oxygen extraction fraction baseline/previous PET apparatus, §3 tool-concept cycles and §5 conclusion. The new choice of baseline and tool-analysis combination helps make a different research agenda possible, showing the relevant process need not be the invention of an entirely new sensor. Reference remains tentative; exploratory usefulness ≠ universal ontological proof.

Steinle's exploratory experimentation is direct priority prior art: https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/entering-new-fields-exploratory-uses-of-experimentation/A1BF59B7198F4C380D3B5F1FAEFF9241 . Read publisher abstract and SEP scientific method, https://plato.stanford.edu/entries/scientific-method/ ; the ability to experiment when the conceptual framework is not yet developed is prior art, not MQR novelty. Need obtain original full paper if genuinely load-bearing, and resolve 1997 original date vs online host posting; do not call publisher abstract deep reading.

Nersessian's account of Maxwell is also synthesized in a later article: https://pmc.ncbi.nlm.nih.gov/articles/PMC9127582/ (heuristic levels and model revisions); source is a secondary comparison, not independent historical verification.

## 2. Finite countermodel: operation-created experimental predicates

Define a modeler's full state space X={0,1}^3 with state (x,y,z). Initially an investigator has one sensor O(x,y,z)=x, and can only construct O-observable predicates. The observational equivalence relation with admissible protocols W is

    s ≈_W t  iff  O(w(s))=O(w(t)) for each w∈W.

The corresponding observable Boolean algebra consists of all unions of ≈_W classes. If there are k finite classes it has exactly 2^k predicates. The number k is NOT the number of predicates, an important dimensional distinction.

Admit these manipulations:
- F_x toggles x: (x,y,z)↦(1-x,y,z), informative only about already observed x;
- F_y toggles hidden y without coupling to sensor: (x,y,z)↦(x,1-y,z), cannot reveal y;
- S_xy swaps x and y, reveals y by measuring x afterwards;
- S_xz swaps x and z, reveals z by measuring x afterwards.

Each protocol is a word over available manipulations, followed by O. Include the empty word. For horizon h, W_h contains words of length ≤h.

**Actual local Python standard-library exhaustive enumeration** over all eight states and all words up to depth 3, with assertions and negative controls:

| Available operations | k(h=0) | k(h=1) | k(h=2) | |Boolean algebra| at h=2 |
|---|---:|---:|---:|---:|
| None | 2 | 2 | 2 | 4 |
| F_x only (negative control) | 2 | 2 | 2 | 4 |
| F_y only (negative control) | 2 | 2 | 2 | 4 |
| S_xy only | 2 | 4 | 4 | 16 |
| S_xz only | 2 | 4 | 4 | 16 |
| S_xy and S_xz | 2 | 8 | 8 | 256 |

The original coding expectation for the joint-swaps h=1 result was incorrectly 4: the first actual run stopped at the assert and revealed that both one-step interventions reveal y and z separately, so k(1)=8. **The expected value was corrected to 8; the final test passed.** This failed-prediction-to-correction is part of the research record. No new mathematical theorem is claimed.

Reproducible program: `experiments/mqr-5.4/mqr42_question_algebra_growth.py`. Note that 2^8=256 predicate choices, not 8 or 16. Counts represent model-observable unions of equivalence classes, not scientifically legitimate natural-kind categories.

## 3. Hidden assumptions — crucial failure modes

1. **Repeatably prepared state**: obtaining O(s), O(S_xy(s)) and O(S_xz(s)) in separate trials assumes that the initial state s can be re-prepared, or that the before/after relation can be independently identified. If irreversibly changing a unique specimen prevents repetition, the tuple of outputs isn't directly observable.
2. **Correct intervention semantics**: S_xy and S_xz are assumed to act exactly as written; empirical action uncertainty may destroy these class splits.
3. **Fixed external ontology**: the experimenter-author knows (x,y,z) before the fictional investigator. The code **does not construct, search or invent an unknown operator**; it measures consequences after operations are granted.
4. **Noise and calibration**: binary output is exact; no noise, state drift, or correlated error. No inference that physical UV–Vis can measure any arbitrary latent property by 'swapping' it into a digitizer.
5. **Question-meaning versus predicate expressibility**: logical enumerability of subsets is not successful concept creation, reference stabilization, causal explanation or natural kind discovery.
6. **Transferring authority**: a philosophy of neuroscience source is a conceptual comparator, not direct evidence for physical alien science, and the Boolean algebra theorem is known mathematics.

## 4. The new high-value research question

**Can a scientific community, without already knowing the state variables, discover or design a material intervention that exposes a previously unobservable distinction—and then validate that the associated concept refers to something real rather than being an instrument artifact?**

The candidate staged cycle is:

- Notice an internal failure, anomaly or unhelpful classification (e.g., mechanical jamming in the imagined Maxwell model, unexpected baseline behavior in a neuroscience study).
- Recombine available analogical or instrumental resources into candidate experimental operations.
- Obtain differentiated signatures and perform independent controls.
- Reconstruct the conceptual vocabulary and its referential commitments.
- Expand the space of questions and check downstream explanatory, predictive and technological use.
- Admit that a controlled split can be merely apparatus-specific; require new independent contact before realism.

This is a **research program**, not proof that such a process always succeeds or is unique. It refines the MQR 40 objective rather than reducing it to a metrology audit.

## 5. Cross-Lab, Harvest, and next BFS/DFS

Existing MQR-Harvest Backflow Bridge https://app.notion.com/p/3d5ef561cf928132a2ecc02734f1b885 and origin-preserving global Harvest genealogy https://app.notion.com/p/3d2ef561cf92811d86e7eeb4f5756b1c are already recorded. Distinct reusable donor fragments here: (A) model failure as constructive design pressure (Nersessian Maxwell case, with primary/historiographic limits); (B) measurement baseline or analysis protocol as generator of concepts (Haueis neuroscience). Cross-lab reuse is only with original locators, explicit analogy flags, no transfer of empirical warrant. Not creating a duplicate global fragment or claiming a provenance-ledger update merely by writing a local research note.

Next DFS: define a 'protocol-discovery' benchmark where the scientist is not told the correct swap operations, and negative controls include misleading artifacts and nonrepeatable state. Explicitly distinguish search over a given operator grammar from inventing a grammar.

Next BFS: return to MQR's 'paradigm of paradigms' question — can standards for legitimate observables and trustworthy explanations themselves change as tool vocabularies expand? Compare Kuhn, Nersessian and contemporary scientific practice; do not confuse the formal generated Boolean algebra with a self-certifying scientific paradigm.

Source missing/verification ledger re-opened at https://github.com/WhoSia/MQR/blob/main/research/MQR_LIVE_MISSING_SOURCES_REGISTRY.md ; unchanged from 2026-11-10. Feest 2025 complete monograph (intro-only), Fraenkel 1927 first edition, autograph Fraenkel→Brouwer facsimile remain on hold. Steinle exploratory experimentation full source is a **new targeted acquisition candidate** pending Drive dedup search before adding to missing ledger. No new Drive downloads, moves or renames this turn.

## 6. Governance, no-bot and completion state

Actual local exhaustive run PASS after a documented corrected expectation. Authenticated user GitHub direct writes only, no `GitHub-Actions[bot]` author or committer. Empirical generalization HOLD; literature original publication locator audit partial; exploratory-protocol model does not create truly novel physical measurements.
