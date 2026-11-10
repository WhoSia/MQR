# MQR 5.4 / MQR 41 — Intervention-Generated Distinctions and the Limits of Cross-Science Translation

Date: 2026-11-10 (KST)  
Status: **THEORETICAL TOY WITNESS / NO EXTERNAL EMPIRICAL CLAIM**  
Research lineage: 5.4 Q1 (measurement and computation), Q2 (possible sciences), Q3 (paradigm genesis).

## Root question

Can a scientist discover world-differences that are invisible to their current observation apparatus, without mistaking an already shared language of interventions for a discovered translation between alien sciences?

## Operational experiment space

Finite world `X={(0,0),(0,1),(1,0),(1,1)}`. States are ordered binary pairs `(x,y)`; first-science sensor `o(x,y)=x`.

For an available family of **known and repeatable action sequences** `W`, define the operational signature `sig_W(s)=(o(w(s)))_{w in W}`, including the empty sequence, and equivalence `s ~_W t iff sig_W(s)=sig_W(t)`. Here a word is executed before observation, and composition order must be fixed in any implementation.

If `W_1 subseteq W_2`, then `~_(W_2) subseteq ~_(W_1)`: adding protocols refines or preserves distinguishability. This is an elementary consequence of equality of the longer signature implying equality of every shorter component, **not a new theorem**.

Three actions: `identity(x,y)=(x,y)`; `toggle_y(x,y)=(x,1-y)`; `swap(x,y)=(y,x)`.

| Experiment family | Number of operational state classes | Observation |
| --- | ---: | --- |
| identity only | 2 | sensor reads only x |
| identity and toggle_y | 2 | intervention changes hidden y but never couples it to x |
| identity and swap | 4 | first observe x, then swap to observe former y |
| identity and swap-after-toggle_y | 4 | indirect protocols still expose y |

Thus **adding more procedures is not sufficient**: procedures must make previously latent distinctions observable. Equivalently, available interventions can expand an effective observation algebra even without changing sensor electronics.

## Reproducible exhaustive enumeration

```python
from itertools import product
states = list(product((0, 1), repeat=2))
obs = lambda s: s[0]
identity = lambda s: s
toggle_y = lambda s: (s[0], 1 - s[1])
swap = lambda s: (s[1], s[0])
conditions = {
    "passive": [identity],
    "toggle_only": [identity, toggle_y],
    "swap": [identity, swap],
    "toggle_then_swap": [identity, lambda s: swap(toggle_y(s))],
}
expected = {"passive": 2, "toggle_only": 2, "swap": 4, "toggle_then_swap": 4}
for label, protocols in conditions.items():
    sig = {s: tuple(obs(f(s)) for f in protocols) for s in states}
    assert len(set(sig.values())) == expected[label], (label, sig)
    print(label, sig)
```

The four expected counts were exhaustively checked locally on 2026-11-10. No physical sensor data were tested.

## Translation obstruction: an identification boundary, not an impossibility of all communication

Suppose science A reports `x` and science B reports `y`. An external analyst may define a swap translation. But if A and B do not yet agree on event correspondence, action identity, clocks, the meaning of an observation, or a common coupling channel, that mathematical swap does not entail **discoverability by the scientists**.

More generally, whenever a permutation `g:X->X` preserves all actually accessible experiment records after relabeling state, observation, and available action descriptions, the transcripts alone cannot distinguish `s` from `g(s)` or uniquely identify the cross-science dictionary. This is a symmetry/gauge ambiguity of the posed inverse problem, not a blanket claim that translation is impossible. Any claimed unique translation must identify a symmetry-breaking witness: a joint intervention, shared reference event, physical coupling, or novel observation that does not simply presuppose the desired mapping.

**Negative control:** If the only jointly witnessed records are marginal frequencies of independent uniform bits, many cross-science alignments fit; even perfect marginal agreement does not identify the referent.  
**Positive candidate:** A jointly constructed device with controlled cross-coupling and a previously frozen discriminating prediction can break some alignments; its success remains conditional on genuinely independent evidence of matched events and coupling.

## Key boundary for MQR's original UV–Vis ambition

A digital conversion `Q:Z->D` cannot by itself distinguish analog states already identified by the upstream map `F:X->Z`: if `F(s)=F(t)`, then `Q(F(s))=Q(F(t))`. In contrast, a new sensor or intervention can change `F` or the set of accessible experiments. Conversely, two states with different analog outputs can still be quantized into the same digital code; finer ADC resolution may split that **quantizer-induced** class, not recover distinctions the physical transduction already erased.

Claim must be scoped to noise model, observables, protocol set, hardware dynamics and reachable preparations. No result about all scientific knowledge or all alien mathematics follows from the four-state demonstration.

## BFS/DFS next branches

1. **BFS-Q1:** derive nested partitions for physical transduction, noise, ADC quantization and active probing; record failure classes (saturation, spectral overlap, drift, nonidentifiable latent variables).
2. **DFS-Q2:** define a two-agent protocol where action labels are initially independently permuted; quantify which joint couplings permit dictionary recovery and which automorphisms remain.
3. **BFS-Q3:** model conceptual novelty as extending the observable/action vocabulary, not merely improving parameter estimates within a fixed one; compare this carefully against historical examples without assuming history obeys a four-state automaton.
4. **Literature:** distinguish this elementary model from classical automata distinguishability, active system identification, observational equivalence/bisimulation, structural identifiability and scientific incommensurability. Novelty is unassessed; scholarship does not depend on novelty alone.

## What changed relative to MQR 40

The intervention witness shows explicitly that **not every intervention splits a hidden state** (toggle-only negative control); it separates an external isomorphism from a discoverable cross-agent translation, and it ties the result back to the founding measurement-versus-logic-circuit question. The primary claims are narrow mathematical consequences and reproducible toy enumeration, not world-facing evidence.

## Missing-source status

No new source bytes obtained during this research unit. Preserve the 2026-11-10 live missing-source registry, including Feest (2025) whole book and Fraenkel (1927) complete lectures, plus the image/edition verification HOLD categories. Do not reclassify held image-only Wedgwood sources as absent.

## Governance

Research contribution can be synthesis or careful reconstruction per doctrine override 2026-10-18. Do not assert empirical PASS, original theorem, comprehensive literature review, or fully identified alien-science translation.
