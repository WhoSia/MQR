# MQR-4.120 P3 — Authority-Ancestry and Contestable Appeal

2026-10-17. ACTIVE P3; **finite constructed contract**, not proof of institutional legitimacy.

## Research move
4.119 P4–P5 and 4.120 P0–P2 distinguished conditional J1 evidential validity from J2 authority to select/revise its rubric. This step asks whether an apparently independent appellate court is genealogically separate from the initial court and whether the appeal route can receive a complaint against its own admissibility rules.

Represent authority lineage as a directed graph G, with an edge x -> y indicating that x claims delegated authorization from y. An ancestor overlap of initial court C and appeal court A is a **dependency warning**, not proof that the appellate decision is corrupt or illegitimate. No overlap in the declared graph is also **not** proof of independence: the graph can omit undeclared dependence.

## Bounded executable counterexamples
[Six synthetic authority-ancestry tests](../experiments/mqr-4.120/p3_authority_ancestry.py) distinguish same authority ancestor, different panels with the same office upstream, distinct ancestry without verified independent mandate, distinct ancestry under stipulated external mandate, cyclic delegation, and missing nodes. Each returns a conservative classification rather than PASS for actual independence.

Local execution of six checks: PASS for the specified synthetic expected classifications; this does not verify source completeness, real delegation, legitimate scope, an effective appeal, or substantive correctness.

## Critical boundaries
- Shared ancestors warrant scrutiny but cannot independently defeat a legally or scientifically legitimate delegation.
- Separate nodes or separate human reviewers do not prove independent authority.
- An independently claimed root is a stipulation here. Real-world external mandate needs source-linked evidence and contestable scope.
- A recursion stopping rule can be *locally warranted* by a source-verified mandate, challengeability, review-scope adequacy and explicit reopening; it is not universal final closure.
- The current graph checker does **not** implement the appeal's capacity to hear a challenge to its own rules, nor does it verify actual documentary provenance. This remains P4.
- Preserving dissent is required even when review is procedurally valid; dissent is not automatically substantively correct.

## P4 research direction
Add provenance receipts for each delegation edge, representation of excluded questions, and actual remedial powers of appellate bodies. Use an adversarial source mutation to check whether the court incorrectly upgrades independence on a missing edge. Include a legitimate shared-ancestor appellate arrangement as a counterexample to overly strict disjointness rules.

## Inherited HOLD
Greenberg unresolved seven-row ambiguity, CCQM custody/calibration independence, 4.118 Harvest candidates, 4.119 R0/R+/E unperformed comparison, no actual assessor independence demonstrated. No scientific or normative closure certified.
