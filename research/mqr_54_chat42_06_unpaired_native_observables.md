# MQR 5.4 — MQR 42 · 기록 06: No joint observable from unmatched native outcomes

**2026-11-21; new finite no-go witness.** Source code: [unpaired native catalog model](../language/real/experiments/unpaired_native_readouts_v54.py); [seven regression/exhaustion tests](../language/real/experiments/test_unpaired_native_readouts_v54.py). Both files were run locally as part of a **15/15** test run jointly with the 8 sequential-contact tests; exact local Git blob hashes equaled those of repository files. The result is a finite identifiability counterexample, **not** a new theorem in statistical data integration or a demonstrated physical inter-lab bridge.

## The missing premise in the apparently positive complementary-native-readout result

[The paired sequential analysis](mqr_54_chat42_06_sequential_contact_and_order_effects.md) showed two distinct native observational partitions can intersect in a finer joint partition when applied to the **same physical preparations**. But **which records belong to the same preparations?** If independent native scientists have no authenticated cross-lab token identifiers, even the joint *number* of distinguishable preparations may not be inferred.

Let A have four individually inventoried specimens with native readouts (a,a,b,b) and B four with (x,x,y,y); only their **native** specimen labels and readout symbols are known. The analyst posits both inventories can be put into a bijection, but no particular pairing is externally warranted. There are 4!=24 possible pairings. The full joint outputs, ordered by A specimen, are (o_A(i),o_B(φ(i))). **For exactly 8 pairings**, the two nonempty joint signature classes are just the existing A categories, **while for exactly 16 pairings** there are four distinct joint signatures (a,x),(a,y),(b,x),(b,y). The same two native records therefore support *incompatible conclusions about the resolution of a joint experiment*.

### Why 8 versus 16, independently of code

The 2+2 local readout split can be fully matched by mapping the two A blocks onto the two B blocks either in the same order or swapped: 2! ways to map blocks ×2! internal permutations in each ×2! = **8** possible bijections with only two joint cells. Any other bijection distributes two members of each A block over both B classes, yielding all four joint signature cells: 4!−8=**16**. Hence a proof without relying solely on the program.

### Certified physical contacts change which joint conclusion is identifiable

| Externally certified contact(s) | Pairing candidates | Joint class-count possibilities |
|---|---:|---|
| None | 24 | 2 for 8 hypotheses; 4 for 16 |
| A0→B0 | 6 | 2 for 2; 4 for 4 |
| A0→B0 and A1→B1 | 2 | 2 for both |
| A0→B0 and A1→B2 | 2 | 4 for both |
| A0→B0 and A2→B2 | 2 | One predicts 2, the other 4 |

The 2-anchor cases are particularly instructive: **the joint number of distinct outcomes can be uniquely established before the entire one-to-one specimen map is known**. This is a relative *task-specific identification*: knowing the exact world state correspondence is sometimes stronger than what an experimental decision needs. Conversely, one or even two poorly chosen anchors can leave the *joint observable* unidentified.

**No empirical contacts were made in this work.** Anchors are analyst-supplied *already verified* identities. They must never be inferred merely because two spreadsheets share identical timestamps, approximate values, or translated category names. In reality state inventories can differ in cardinality and be nonbijective, which the present model deliberately excludes.

## Prior art rather than misplaced general novelty

This is an instance of the well-established **statistical matching / data fusion problem**: marginals of two variables observed in separate datasets do not uniquely identify their joint distribution without a bridge, additional assumptions or genuinely paired observations. See [*Partial identification in the statistical matching problem* (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5423529/); [*Integrating rather than collecting: statistical matching in the data flood era* (2023)](https://link.springer.com/article/10.1007/s00362-023-01468-3); and [Endres & Augustin (2016), *Statistical Matching of Discrete Data by Bayesian Networks*](https://proceedings.mlr.press/v52/endres16.html). Our enumeration is a small exact deterministic illustration with **named specimen correspondence** rather than a population-level statistical joint law: do not claim the two problems are literally mathematically identical in all respects, only that the underlying missing pairing/association is structurally analogous.

## Research-director implications

The MQR ambition should be sharper than 'two labs with different terms can share data':
1. **The target fact may be smaller than the full translator**. Decide whether the scientific question requires joint outcome counts, a specific causal intervention, or a complete specimen correspondence before collecting more contacts.
2. **The world-contact certificate is what matters**, not number of shared English words, matching graph diagrams, or row-level data parity. Some contact choices resolve the target property but not the map; others are useless despite multiple apparent matches.
3. **Measurement disturbance adds a second independent threat.** Even when every specimen is externally paired, [sequence AB/BA](mqr_54_chat42_06_sequential_contact_and_order_effects.md) can change what those paired outputs mean. Thus cross-science fusion has at least two separate gates: *matching the same preparation* and *validating the effects of measurement order*.
4. **Concept invention is a third, harder gate.** Identifying a joint partition by certified paired observations is not yet a new concept grammar, a newly executable experiment, or an argument for a unique hidden ontology.

**Status:** EXACT FINITE UNPAIRED-READOUT COUNTERMODEL / CROSS-LAB AUTHENTICATION NOT ESTABLISHED / PHYSICAL SENSING OPEN. Do not invent an experimental scientific encounter from a toy bijection.
