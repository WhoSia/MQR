# MQR 5.4 · MQR 43 · 기록 23 — 두 시계가 다시 만날 때: 경로 의존적 고유시간과 물리적으로 새로운 질문

**2026-11-21 · MQR 43 · MQR 5.4 unchanged.**
**Status:** EXACT MINKOWSKI WORLDLINE COMPARISON VERIFIED / HISTORICAL INTERPRETATION SUBJECT TO RIVAL THEORIES / NO NEW EMPIRICAL CLOCK EXPERIMENT.
**Context:** [Record21](mqr_54_chat43_21_galilei_lorentz_minkowski_invariant_question_space.md) derived exact spacetime interval invariance for rational boosts; [record22](mqr_54_chat43_22_masterman_friedman_galison_meta_paradigm_prior_art.md) challenged a simplistic novelty claim against historically prior Kuhnian theories.

## 1. Strengthening the question beyond distant simultaneity

A coordinate statement that distant events are simultaneous can depend on synchronization convention. [The SEP's detailed article on simultaneous conventions](https://plato.stanford.edu/entries/spacetime-convensimul/) stresses that Einstein's 1905 treatment presupposes a choice of how light signals define the times of spatially separated clocks. Therefore **an event-pair thought experiment about simultaneity should not be confused with a directly observed time difference between two clocks that meet at the same event.**

A physically stronger conceptual test asks what ideal clocks *actually accumulate along different spacetime histories* joining a common departure event P and reunion event Q. That problem invites Minkowski's line element / clock hypothesis, not merely a coordinate relabelling.

Let c=1. Define

P=(t,x)=(0,0), R=(5,3), Q=(10,0).

For a straight inertial worldline from P to Q, all coordinate time is spent at spatial position x=0 in the chosen inertial frame. The Minkowski proper time is

τ_direct = sqrt((10-0)^2-(0-0)^2) = 10.

For the two-leg path P→R→Q, with velocities +3/5 and −3/5, the proper times are

τ_PR = sqrt(5²-3²) = 4,
τ_RQ = sqrt(5²-(-3)²) = 4,
τ_via_R = 8.

Thus **the clock readings at the same reunion event can differ by exactly 2 time units** in this idealized flat-spacetime construction. The numbers were independently recomputed using Python Fraction integer arithmetic in the current analysis. No rounding, actual device readout or new experimental observation is involved.

The turnaround R changes velocity instantaneously in this piecewise-inertial idealization, so it should be replaced by a smooth finite-acceleration path for a physically realizable route; a smooth approximation retains a nonzero proper-time difference. The "clock hypothesis" / ideal-clock physical behavior and possible acceleration-specific disturbances must be addressed in any actual experiment.

## 2. An exact general proof without numerical gadgets

In the rest frame of the straight segment between P and Q, parameterize an alternative future-directed timelike path by coordinate time t∈[0,T], with spatial velocity v(t) satisfying |v(t)|<c. In special relativity,

τ[γ] = ∫₀ᵀ sqrt(1-v(t)²/c²) dt ≤ T,

with equality precisely when v(t)=0 almost everywhere. Hence an inertial straight worldline maximizes proper time among such timelike paths between fixed events in flat spacetime. The inequality is an elementary consequence of 0<sqrt(1-v²/c²)≤1; it is not an MQR novel theorem.

In the **standard Newtonian absolute-time ideal-clock assumption**, both paths span the same absolute time T, irrespective of velocity history. This is a genuinely different theoretical answer to a *locally comparable* reunion-clock problem. It goes beyond describing which separated events are simultaneous in one convention. However a specially engineered Newtonian dynamical clock can itself be path-sensitive; one clock comparison alone cannot rule out every possible alternative mechanical clock theory.

## 3. Theory, question, apparatus, and ontological underdetermination

| Level | What physically changes? | Permissible inference |
|---|---|---|
| Coordinate labels only | Represent an event with other numbers | No new predictions/ontology automatically |
| Structural invariants | Adopt Minkowski metric and associated proper-time functional rather than universal Newtonian time | The accepted coordinate-independent questions and constraints change |
| Clock behavior | Specify when physical clocks approximate ideal proper-time indicators | Reunion comparison becomes an experimentally assessable claim with clock/dynamics assumptions |
| Ontology/interpretation | Interpret invariant outcomes as Minkowski spacetime, a dynamical ether-based structure, or another representation | Identical operational outcomes may still underdetermine preferred ontology |

The *historical* Lorentz-versus-Einstein issue is a critical negative control. One cannot use Galilean transformation formulas as a stand-in for Lorentz's actual aether framework: **Lorentz used Lorentz transformations.** The philosophical literature remains contested: [SEP inertial frames](https://plato.stanford.edu/entries/spacetime-iframes/) notes possible empirical indistinguishability, whereas [2014 equivalence argument](https://www.sciencedirect.com/science/article/pii/S1355219814000124) and [2019 non-equivalence study](https://doi.org/10.1093/BJPS/AXZ014) disagree over how to construct/compare the rival theories. We have verified their abstracts and not adjudicated every argument in full texts. In particular, **two equivalent fitted models may explain the same clock result differently**; even a precise reunion-clock difference does not establish the unique metaphysical interpretation of spacetime.

## 4. Historicity: same formula does not equal same practice

For the earliest original texts, use [Einstein's 1905 paper in a declared English translation](https://fourmilab.ch/etexts/einstein/specrel/www/) and [Minkowski's 1908 talk in an openly tagged later translation](https://en.wikisource.org/wiki/Translation:Space_and_Time), with translation status recorded rather than claiming German 1905/1908 original page fidelity.

- **Masterman (1970)** asks how exemplary problem solutions teach a community what to investigate. Reunion-clock calculations can become an exemplar when experimentalists and theorists learn to treat proper time as a physical measurable quantity, but the mere availability of a formula does not show when that actually happened.
- **Friedman (2001)** asks how the constitutive structure of time/measurement changes while rational discourse survives across scientific revolutions. This is already known prior art; MQR must not rebrand it as a new "meta-paradigm theorem."
- **Galison (1999)** asks how theory, instrumentation, engineering and experiment coordinate *locally* without sharing a global ontology. For a real clock experiment, a common operational result may be jointly usable even when parties disagree on its deeper meaning.

The three historical explanations differ in **temporal and social scope** and can coexist. New historical research must check *when particular clock techniques, predictions, and explanatory aims actually entered practice*, not infer real events from formal mathematics alone.

## 5. The sharpened founding thesis and its adversary

**Proposed bounded thesis:** A changed scientific framework can change the set of *physically privileged, discriminating and experimentally actionable questions* even when some of its concepts can be translated into older mathematical languages. A question may be formally expressible yet not treated as a central invariant or useful experiment; later physical practice can make it a key target.

**Hard counterargument:** Any actual clock experiment can in principle be represented in a sufficiently expressive older mathematical notation with extra dynamics. Therefore it may be **methodological organization and explanatory virtues**, not logical expressibility or unique empirical success, that really changed. An advocate of Lorentzian aether could reproduce special-relativistic clock predictions with an added constitutive story. This is not grounds for abandoning the question but a reason not to equate question-space difference with logical inexpressibility or theory's falsification.

**What would count as more than a rhetorical advance?** A specific historical sequence with source-dated (i) initial admissible question/exemplar, (ii) formal derivation and rival explanation, (iii) concrete apparatus or mathematical method enabling a new comparison, (iv) actual experimental adjudication and remaining alternative interpretations. Historical and mathematical claims each require evidence appropriate to the claim. The current paper establishes only the exact physical-theoretical step and a historically bounded question for subsequent DFS.

**Director decision:** This is a meaningful physics-grounded return to MQR's founding concern about generating new questions, not a reason to recast all of MQR as clock calibration. Record21/22/23 form one bounded branch; next BFS should explore a genuinely different structural domain (mathematical proof, electromagnetism, renormalization-group universality, or the history of scientific exemplars). No 5.5 promotion.
