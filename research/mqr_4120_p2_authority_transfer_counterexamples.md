# MQR-4.120 P2 — Dual-Ledger Authority-Transfer Counterexamples

2026-10-17. ACTIVE P2, BOUNDED FINITE CONTRACT.

## Inherited frame
P1 separated J1 (claim-relative evidential warrant under a stipulated rubric) from J2 (authorization, contestability and scope of that rubric). P2 tests *illicit transfers of warrant*, not legitimacy itself. This continues the historical MQR concern that replicated software decisions or shared-source witnesses cannot establish independent world contact.

## Executable
[Dependency-free Python finite checker](../experiments/mqr-4.120/p2_dual_ledger_contract.py) defines eight constructed contract cases: four valid records (DC1–DC4) and four deliberate invariant violations. DC1 admits bounded formula-level PASS while custody J2 stays HOLD; DC2 preserves unresolved empirical alternatives; DC3 preserves an excluded challenge, and DC4 tests a possible nonconflict. Deliberate violations are traceability PASS without custody, empirical PASS with unresolved discriminator, J2 self-authorization by majority with no appeals route, and dissent whose alternative question was erased.

The test establishes only consistency with hardcoded documentation rules, not a theorem about real institutions or experiments. The records are synthetic and the status values are stipulated; PASS does not prove actual J1 correctness or J2 authority. Distinct records are not independent world observations. The checker does not assess honesty of underlying source metadata, independence of authorization, or sufficiency of contested appeals. Future runs in GitHub CI must be separately verified before CI SUCCESS is reported.

## Formal limitation
The relation J1(e,c|r) and J2(r,a|s) does not support an unconditional rule J1 PASS => J2 PASS. Nor does J2 HOLD imply J1 FAIL. This is a type/non-entailment design constraint illustrated by constructed countermodels, not a general scientific discovery. J2 PASS in a synthetic example uses an assumed external remit, not a verified independent mandate.

## P3 direction
Make the authority-ancestry graph explicit, identifying shared-origin appeals panels and inherited exclusions; examine when an independent contestation route exists without infinite regress. Carry Greenberg, CCQM and prior Kuhn/Harvest HOLDs forward.