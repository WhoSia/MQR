# MQR-4.120 P4 — Provenance Mutation, Missing Edges and Contestable Authority

2026-10-17. ACTIVE P4, **constructed finite contract only**.

## Why P3 was not enough
P3 classified common ancestors and separate declared ancestry, but a missing authority edge could make the appeal court look independent. Deleting a recorded dependency cannot constitute positive evidence of real independence. P4 conditions its checks on a separately supplied *expected edge registry*.

## Reproducible test
[Dependency-free Python P4 fixtures](../experiments/mqr-4.120/p4_provenance_mutation.py) construct eight cases: shared ancestry; registered shared edge deleted; separately declared genealogy under stipulated mandate; missing mandate; appeal outside its contestable scope; empty receipt; unregistered extra edge; cyclic delegation. Local Python execution: eight expected classifications matched. A registry mismatch yields HOLD instead of an apparently stronger separation verdict.

## Source and authority limits
The registry is **stipulated** and independently supplied in these examples, not independently attested. If the registry and observed edge list share a deletion or are manipulated together, this checker need not detect it. A nonempty receipt token is merely schema evidence; no underlying document was fetched or authenticated. A 'verified mandate' flag is hypothetical, and 'appeal can hear scope' is only a boolean assumption. Thus CONDITIONAL_STRUCTURAL_SEPARATION is emphatically **not** real independence or normative legitimacy.

Shared ancestry itself does not defeat a legitimately authorized independent review function; a defensible appellate procedure may be within the same overall institution. Independence is claim-, function-, challenge-, and source-indexed, not a disjoint-graph score.

## P5 proposal
Develop a witness for appeal capacity: whether the review body can actually reopen the excluded question, require custody evidence and revise the rule. Test the limitation that an internally consistent authority registry cannot authenticate its own completeness; bring independent evidence and adversarial challenge over time. Preserve dissent and authority scope without universal final closure.

## Inherited outstanding work
Greenberg seven unresolved rows, CCQM physical calibration chain, 4.118 Kuhn/H-MQR Harvest candidates, 4.119 R0/R+/E human evaluation NOT RUN. Synthetic regression PASS does not settle any source-grounded scientific or institutional question. MAIN_ONLY; never bot-authored commits.
