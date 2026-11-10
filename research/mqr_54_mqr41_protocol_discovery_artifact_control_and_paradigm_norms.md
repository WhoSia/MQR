# MQR 5.4 / Chat MQR 41 — Protocol Search, Artifact Confounding, and Question-Generating Sciences

**Canonical labels:** CHAT SESSION = **MQR 41** (the number denotes the conversation, not a research stage). RESEARCH VERSION = **MQR 5.4**. Subprojects in this chat do not increment the chat number. The previously mistakenly labeled `mqr42_...` paths were replaced with `mqr41_...`; the history remains accessible in Git. No MQR 42 session has occurred.

**Status:** executable synthetic comparison (pass), source-grounded conceptual comparison (bounded), physical-world validation (hold), universal science-of-science theory (hold).

## 1. What is genuinely being asked?

MQR 40 ending calls for broad curiosity: not another incremental claim about one old thermometer, but the question of how radically different sciences, instruments, mathematical languages and even criteria for a *question* can arise. The key progression is:

1. A given fixed experimental alphabet can make some physical distinctions observable.
2. A scientist may select candidate experiments from a **supplied** design grammar.
3. A scientist might invent a new design grammar or concept — this is a much stronger problem.
4. A community may decide whether the split warrants a new natural kind, an explanatory concept or only a useful operational category — stronger still.

Do **not** collapse (2) into (3) or (4).

## 2. Experiment: finite-menu protocol discovery with artifact control

States X={0,1}^3, one baseline sensor O(x,y,z)=x. Candidate black-box experimental protocols are `flip_x`, `flip_y`, `swap_xy`, `swap_xz`, and an `artifact` channel. The first four are exact modeled physical actions; the last is a confounded readout that returns y in the first data session and z in an independently repeated session (a deliberately contrived nuisance-channel failure). We assume eight known, reproducibly preparable states — a strong laboratory advantage, **not** a discovered external ontology.

For each candidate `a` the algorithm examines the number of equivalence classes induced by `(O(s),O(a(s)))`, and checks the *per-state* signatures under two sessions before accepting it. Information gain measured as added class count is a heuristic, not a unique information-theoretic optimality claim. A greedy acquisition strategy selects validated candidates until no further stable refinement is achieved.

The executable is `experiments/mqr-5.4/mqr41_protocol_candidate_discovery_and_artifact_control.py` and was run directly under Python. Observed transcript:

```text
selected: ['swap_xz', 'swap_xy']
protocol transcript:
  ('artifact', 2, 'REJECT: session-unstable artifact')
  ('swap_xz', 2, 'ACCEPT')
  ('swap_xy', 4, 'ACCEPT')
final observable Boolean predicates: 256
PASS: baseline 2 -> validated 4 -> 8, artifact rejected
```

- Both `swap_xy` and `swap_xz` reveal different latent bits and together split eight states.
- `flip_x` and `flip_y` are no-gain negative controls.
- The artifact seems to improve classification from 2 to 4 both on training and on retest **if one checks only class counts**. Per-state signatures change between sessions, hence it fails replication.
- A first code assertion failed, NOT because the result was wrong, but because greedy selection saturated the partitions before it happened to audit `artifact`; correction added a separate *candidate-wide* stability audit before selection. After correction all assertions passed. A complete audit is thus more informative than merely testing the final selected subset.
- For `k` observational equivalence classes the Boolean algebra of stable observable predicates has `2^k` members. For k=8 this is 256, **not** 256 physically validated kinds.

### Hidden circularity

The data generator and validator are given the true states, exact actions and paired specimen identities. This privileges the simulated scientist with an oracle. Matching the same physical entity across interventions is a nontrivial step in real laboratories and in alien-science contact. The algorithm is a small controlled **finite-menu active experimental design** demonstration, not concept invention from nothing.

### Next-level negative controls

A more serious test should deliberately break state re-preparation, permute specimen identity between sessions, add instrument-dependent common-mode drift, and introduce an out-of-distribution latent state; measure false category promotions rather than merely class counts. Distinguish passing a session repeat from independent measurement channel confirmation.

## 3. Canonical mathematical boundary: finite data vs unconceived protocols

For any finite set of experimental histories H, two possible scientific models can agree on every history in H and differ on an untested admissible history h*. This elementary underdetermination construction requires a hypothesis universe capable of varying on h*; it does not show that no particular finite-state known-class system is learnable. It does show that **the data from H alone cannot warrant universal completeness over all not-yet-imagined protocols.** Avoid calling this a newly proved theorem.

This is where the 'paradigm of paradigms' question begins: rules for deciding *which* protocols are meaningful, admissible, informative and concept-generating may themselves change, so a fixed experiment alphabet cannot settle the epistemology of its own expansion.

## 4. Directly read historical + computational prior art

- **Dana Angluin (1987), 'Learning Regular Sets from Queries and Counterexamples', _Information and Computation_ 75:87–106.** Drive https://drive.google.com/file/d/1X3W7YC5QKwN2MDWnplPlU8f0GBxuod68/view ; direct reading of abstract, introduction and observation-table/closed-consistent passages. L* uses membership and equivalence queries to a *minimally adequate teacher*; the teacher's counterexamples and a given input alphabet are major assumptions. This kills any novelty for 'learn a finite automaton via experiments'; scientific concept genesis is not solved merely by running L*.
- **Jürgen Schmidhuber (2013), 'PowerPlay: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem', _Frontiers in Psychology_ 4:313, DOI 10.3389/fpsyg.2013.00313.** Drive https://drive.google.com/file/d/1u16bbVxiSAJG2WQslJRe-cnC-ESAvhjQ/view ; direct abstract and paper passages. Inventing new computable tasks and altering an existing solver is already prominent prior art; 'AI generates its own tasks' is not automatically an MQR original claim. However an internally generated computational task need not correspond to a newly stabilized empirical referent in the world.
- **Friedrich Steinle (1997), 'Entering New Fields: Exploratory Uses of Experimentation'.** Existing Drive https://drive.google.com/file/d/1rl444ab9HV-Q285EwbPq1QBR2z5g3JcR/view ; original pp. S65–S74. Exploration without a prior mature conceptual framework, flexible apparatus, parameter variations, and new classifications are old, important results.
- **Steinle (2016), _Exploratory Experiments: Ampère, Faraday, and the Origins of Electrodynamics_.** Existing Drive https://drive.google.com/file/d/1-kviuErWDAEJMRlcbACBX7FbLR55hV1G/view ; introduction and Ch. 7 passage reading; full book held, not cover-to-cover read in this session.
- **Nersessian (2008), _Creating Scientific Concepts_** and **Haueis (2023), 'Exploratory Concept Formation and Tool Development in Neuroscience'** already source-checked in earlier MQR 41 units. Their sources retain their separate historical and philosophical authority.

Relevant public comparisons: https://link.springer.com/article/10.1007/s10817-018-9486-0 (active automata learning) and https://plato.stanford.edu/entries/scientific-method/ (exploratory experimental practices). Not substitutes for held full-text sources.

## 5. Existing MQR / Harvest prior-art collision

Previously documented [LR-20260916-B](https://app.notion.com/p/3ddef561cf9281f1975bd07b6883ab8f) and [LR-20260916-C](https://app.notion.com/p/3ddef561cf9281ed8085cca1290f447f) already identify exploratory category creation, intervention choice, and **operational split ≠ natural kind**. This MQR 41 unit adds an intentionally bad session-dependent artifact channel and a source-level computational-learning comparison; it does not warrant a duplicate global Harvest fragment or claiming the old arguments were discovered today.

## 6. BFS: How the norms of explanation themselves change

The most promising next extension is a *plural* test with separate verdicts:
- **Reproducible distinction:** independent session/same-state observational stability.
- **Cross-instrument stability:** independent apparatus/measurement mechanism, with common-mode dependence audited.
- **Explanatory and referential standing:** external interventions, successful new predictions, ability to distinguish instrument artifacts from target properties, and the scope of the concept's usefulness.
- **Historical and institutional uptake:** changes in which experiments and explanations are admissible and what the community treats as problems — observational success by itself does not settle this.

These are **diagnostic dimensions**, not a universal, sequential C0→C3 certification algorithm. A natural kind and an interventionally useful engineering class may both legitimately emerge with different kinds of warrant. This preserves original MQR's broad 'paradigm of paradigms' question without prematurely declaring all science reducible to one formal machine.

## 7. Archive and provenance

The standing [MQR missing-source registry](https://github.com/WhoSia/MQR/blob/main/research/MQR_LIVE_MISSING_SOURCES_REGISTRY.md) was reopened. Feest (2025) complete book remains intro-only; Fraenkel (1927) original edition and the Fraenkel–Brouwer autograph facsimile remain unverified. **Angluin (1987), Schmidhuber (2013), Steinle (1997 and 2016) are already held in Drive**; do not add them to the missing list. No Drive file moved or renamed in this subunit.

Direct authenticated GitHub connector commits only. Commit author and committer must be inspected to avoid `GitHub-Actions[bot]` contributors.
