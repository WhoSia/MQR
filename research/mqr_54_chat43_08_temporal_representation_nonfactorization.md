# MQR 5.4 — MQR 43 · record08: A new scientific question need not add new sensor bits

**2026-11-21; conversation MQR 43; research version MQR 5.4.**
**Status:** FINITE EXACT NONFACTORISATION PROPOSITION AND NEGATIVE CONTROL / EIGHT NEW LOCAL TESTS PASSED / NOT AN ACTUAL CAT REPRODUCTION.
**Executable:** [time-resolved representation model](../language/real/experiments/temporal_representation_v54.py) and [eight unit tests](../language/real/experiments/test_temporal_representation_v54.py). Locally tested Git blob SHAs `44fd029ace95752d7f32d0871de5e9a796d7f677` and `ec29f1996e5a94085882884db701de1afeaf8e17` match GitHub readback. On the local MQR 43 experiment set, `python -m unittest discover -p 'test_*v54.py' -q` returned **43/43 tests passing**. Not a whole-repository suite or real-world instrument test.

## 1. The exact distinction

There are at least three different events that should not be merged:

1. **New acquisition**: an instrument actually retains a physical time-varying signal that was not previously available from its exported observations.
2. **New representation**: an already retained raw trace is processed into a new derived statistic and visualization, perhaps with a new scientific use.
3. **New concept or inquiry**: investigators use the new representation to revise significant questions, causal models, apparatus designs or experimental practices, and expose the revision to worldly tests.

The second does not imply the first. The third neither follows automatically from the first nor requires genuinely new digital sensor bits. In particular, a fixed deterministic transformation of a retained raw trace cannot increase Shannon information about a target variable (data-processing inequality under its usual probabilistic assumptions). Yet a new derived representation can make a previously *unused or inexpressible within a restricted query language* relational question operationally useful.

## 2. Concrete restricted-language example

For an abstract 4-channel, 4-time-bin system, allow one observed event per bin. A raw record is a sequence `R=(c_1,c_2,c_3,c_4)` with each `c_t in {0,1,2,3}`. Its old exported summary is the four-component per-channel event-count vector `H(R)`, completely discarding the event time order. The revised time-resolved statistic `T(R)` is the sequence of the count-weighted channel positions at each time bin. This is a pedagogical **centroid trajectory analogous in spirit** to Nersessian's reported center-of-activity trajectory; it does not duplicate the real CAT algorithm, MEA geometry, physical parameters or recordings.

Take `R=(0,1,2,3)` and `R'=(0,2,1,3)`. Then

- `H(R)=H(R')=(1,1,1,1)`, so **no function whatsoever of H** can tell these records apart;
- `T(R)=(0,1,2,3)` and `T(R')=(0,2,1,3)`, so the time-ordered question 'did the apparent activity center move monotonically across channels?' has different answers.

**Formal proposition (elementary):** no function `g` on the old summary alphabet can satisfy `T=g∘H` for every valid raw record. Proof: the displayed two records have equal H but unequal T. By contrast, T is a deterministic function of the full raw trace R, so T adds **no new raw data information** when R is already retained. This is **relative expressibility**, not invention of an absolutely noncomputable primitive.

For 4 one-hot time bins and 4 channels, there are `4^4=256` raw event sequences. Their old summaries occupy only `C(7,3)=35` integer-composition classes. The number of unordered pairs of *distinct* raw sequences collapsing to the same summary is exactly **1230**, independently enumerated. For example the all-distinct-channel summary contains 4!=24 sequences. The underlying counts across all histogram types are 4 singleton cells, 12 cells of size 4, 6 cells of size 6, 12 cells of size 12, and one cell of size 24; consequently total unordered collisions are 12·6 + 6·15 + 12·66 + 276 = **1230**.

## 3. Two negative controls

**Negative A — the new trajectory also discards information.** Two different 3-channel, two-time-bin raw arrays `((1,0,1),(0,2,0))` and `((0,2,0),(1,0,1))` both have center trajectory `(1,1)` despite different channel activations. Thus identical centroid positions do not identify the underlying participating sensors, neural events, flows or causal mechanisms. A moving centroid, too, cannot alone establish actual transport of the *same* physical entity.

**Negative B — inaccessible raw time structure.** When only H was saved and the actual time-resolved instrument data were never acquired or retained, computing T from H is **impossible in general**. A new instrument or separately acquired evidence is needed. When full R was retained all along, a new representation may make a powerful investigative question practical but **does not add measurement bits**. The code makes these provenance cases explicit, without treating a Boolean flag as evidence of physically new acquisition.

An empty time bin is recorded as undefined (`None`) rather than producing a fabricated center, and irregular channel geometry is accepted only when explicitly specified.

## 4. Crucial historical restraint and source interpretation

The historical [Nersessian (2012) case, directly inspected in the held Feest–Steinle book](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view) describes **MEAscope representations that already had per-channel activity over time**; her claim is not that the original apparatus had access only to the four-number histogram H constructed here. The computational model exposed network-wide motion and visualization and the center-of-activity trajectory developed as an investigative concept. See [record07's documented historical sequence and rivals](mqr_54_chat43_07_nersessian_cat_historical_concept_genesis.md) and [Nersessian and Chandrasekharan's authored account](https://sites.cc.gatech.edu/aimosaic/faculty/nersessian/papers/hybridanalogies.pdf).

The present H/T contrast is a **minimal counterexample to a philosophical claim about representations**, not a reconstructed experiment on real neuronal networks. The mathematical nonfactorization fact is trivial once the maps are defined; its relevance is clarifying when a newly defined observable is genuinely unavailable in an old *released data language*, while retaining skepticism about strong ontological inference.

## 5. A research director's forward test

This comparative construction distinguishes **measurement capacity** (what was ever physically recorded) from **expressible research tasks** (what questions a group could and did pose) and **validated conceptual change** (what new constructs endured physical tests or supported interventions). Follow-up historical coding should locate actual chronological evidence for shifts in questions and the status of “bursts as signal” from original journals/lab records where possible, not merely count new variable names.

Two hard rivals remain: a richer old representation may already encode the allegedly new distinction, and an entirely different physical process may produce the same centroid trajectory. Hence **a new feature does not suffice to certify a new kind of scientific individual**.

**Decision:** Preserve this as a mathematics–scientific-practice bridge inside MQR 5.4, but do not turn it into a universal theorem about every scientific paradigm. Continue BFS with a separate historical episode involving the *displacement* rather than mere addition of a useful concept (Friedrich Steinle's magnetic pole/lines-of-force history is the next held-source candidate).
