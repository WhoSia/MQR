# MQR 46 — Four-preparation exhaustive contact census and the reference-class trap

**Source of numbers:** [exact executable enumeration](../language/real/experiments/graph_contact_census_v54.py), [independent permutation-oracle tests](../language/real/experiments/test_graph_contact_census_v54.py) and [model](../language/real/experiments/contact_stabilizer_v54.py). Local Python tests: **16 MQR46 tests passed** including the extra census tests and 64 graph ×24 re-labeling assertions. Source and test blob IDs were independently compared between locally executed bytes and the GitHub main branch. The experiment is synthetic combinatorics, **not** sampled data about real scientific communities.

Each of 4 vertices has a fixed unique label; an undirected loop-free edge is the locally available manipulation between two preparations. There are six possible edges, hence 2^6=64 **labeled graphs**. For each graph G the first possible cross-lab mappings under *assumed structural invariance* are Aut(G). The minimum number of **perfect independently certified preparation anchors** sufficient to kill every non-identity automorphism is the pointwise stabilizer base size b(G).

## Exact labeled four-graph census

| Automorphism count (candidate mappings) | Labeled graphs (of 64) | Minimum verified anchors |
|---:|---:|---:|
| 2 | 36 | 1 |
| 4 | 12 | 2 |
| 6 | 8 | 2 |
| 8 | 6 | 2 |
| 24 | 2 | 3 |
| **Total** | **64** | |

There are zero asymmetric graphs with only four vertices (no |Aut|=1 case). Across these 64 *labeled graphs*, minimum anchors: one for **36**, two for **26**, three for **2**; the equally weighted-labeled average is (36+52+6)/64=**94/64=1.46875**. These anchors are theoretical **best subsets** of the observed states, not the number of human transfer attempts or the expected cost under noisy/biased measurements.

**Independent oracle:** The tests separately enumerate all 4!=24 permutations for each edge mask and then all subsets of fixed vertices; this agrees with the original model's counts. The two independent algorithm paths reduce but cannot eliminate implementation or definition risks.

## A deeper metascientific finding: “typical” depends on equivalence and measure

The 64 graphs include repeated *isomorphic* configurations. A graph with automorphism group size a has 4!/a =24/a distinct labeled copies. Dividing the labeled counts by those orbit sizes shows **11 nonisomorphic graph types**:

| Automorphism count | Nonisomorphic graph types | Minimum anchors |
|---:|---:|---:|
| 2 | 3 | 1 |
| 4 | 2 | 2 |
| 6 | 2 | 2 |
| 8 | 2 | 2 |
| 24 | 2 | 3 |
| **Total** | **11** | |

Under an *equal weight on 11 isomorphism classes*, the average minimum contact base size is (3×1+6×2+2×3)/11=**21/11 ≈ 1.90909**, instead of **1.46875** under a uniform weight over labeled graph objects.

This is a fully transparent instance of a serious MQR principle: **what looks typical changes when the state space is quotiented by representational equivalence and a different measure is placed on the quotient.** The two means answer **different questions** and neither is an empirical frequency of scientific practices or a probability that two alien sciences will find their vocabulary in two exchanges.

Avoid claiming this as a novel theorem: orbit-stabilizer and graph automorphism enumeration are familiar mathematics. The contribution is a checked, interpretably bounded example of why a “random possible science” or a “representative model” must specify its encoding, equivalence class and measure.

## Physical and philosophical limits

- The cardinality and anchor calculations depend on graph preservation; two sciences sharing one world can have **nonisomorphic** local practice structures when their action menus differ.
- Certified physical transfer is **much stronger** than a common spreadsheet ID. Stability of preparation state must be independently checked.
- Graph edges are defined by the analyst; no automated detection of a common experimental relation is accomplished.
- A unique finite graph alignment does not imply identical hidden ontology, causal explanation or future action grammar.

### Next constructive target

Build a *source-backed action invention model*: initially nonisomorphic G_A/G_B because A and B have different devices. Let an authenticated material encounter change what B can **physically construct or perform**, and check a new out-of-menu prediction against a held-out physical reference. The desired result would be a **new executable distinction** rather than a better bijection of a fixed graph.

References to actual historical concept co-formation: [Feest & Steinle (2012)](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view), Feest chapter on exploratory experiments and concept/theory construction; [Clement (1988)](https://drive.google.com/file/d/1X_EeNfK7g5ablkwQweNpyU_Jhy0uIxTk/view). Their evidence does not establish the mathematical census or its interpretation; both are **MQR analytical reconstructions**.

**Scientific classification:** exhaustive finite enumeration supported by two local code paths; zero measurements of natural sciences sampled, no claim of universal translation.
