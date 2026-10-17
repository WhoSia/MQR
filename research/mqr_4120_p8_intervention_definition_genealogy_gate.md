# MQR-4.120 P8 — Intervention Definition, Compliance and the Evidence-Transport Gate

2026-10-17. ACTIVE P8 / PRIOR-ART AND EMPIRICAL DESIGN GATE. No new theorem or empirical causal estimate.

## Why this is NOT another Bernoulli fixture
The P7 Bernoulli observational equivalence reproduces an established MQR-4.89 pattern, where causal nonidentification was already bridged to 4.87 source-family adjudication. MQR-4.107 also documented Lindsey (1997) Bernoulli stopping-rule selection, MQR-4.111 distinguished pre-intervention state from measurement-created response, and MQR-4.113 separated stochastic experiment comparability from physical measurand warrant. Repeating the toy examples or counting another checklist PASS is not sufficient scientific progress.

## Actual P8 target: treatment definition and transportation across three levels
Define assignment/issuance Z, implementation D, and outcome Y with source-indexed timestamps, units, and eligibility. Z=1 (order issued) must not be silently translated to D=1 (measure taken). A remedial order may be issued without compliance; implementation may occur without a recorded order; partial and heterogeneous implementations may violate treatment consistency. Neither an observed post-remedy outcome nor an independent receipt identifies Y(1)-Y(0).

Distinguish:
- **Intention-to-treat estimand:** E[Y | do(Z=1)] - E[Y | do(Z=0)] in a well-defined assignment regime, if identifiable.
- **Effect of actually implemented remedy:** E[Y | do(D=1)] - E[Y | do(D=0)] for a specified implementation, not generally obtained by conditioning on observed compliers.
- **Local complier effect under valid IV assumptions:** can require exclusion, monotonicity, relevance, and independent assignment; no such conditions have been verified for MQR.
- **Procedural legitimacy and material consequences:** J2 concerns mandate and contestability; a causal estimate, even if valid, cannot alone prove that a process is normatively legitimate.

## Source-typed evidence contract (to execute, not to pretend)
Per candidate real-world study collect: unit and target population; assignment/order process; intervention version, start time, intensity; implementation receipts and independent provenance; outcome definition and timestamps; denominators, censoring and selection; competing causes and co-interventions; eligibility and complaint scope; sources for institutional authority and appeal powers; proposed causal design with its failure modes. Label each item SOURCE-VERIFIED / DERIVED / ASSUMED / UNAVAILABLE. Keep treatment positivity and interference questions explicit when applicable.

## Rivals and falsifiers
R1: assignment and treatment coincide under verified enforcement: the two estimands may align; do not force a distinction.
R2: noncompliance makes naive as-treated comparison differ due to selection: conditioning on D requires separate assumptions.
R3: no independently authenticated implementation receipt: outcome-only causal warrant remains HOLD.
R4: policy change alters reporting without changing underlying outcome: measurement invariance and original MQR source lineage are decisive.
R5: legitimate appellate repair shares an institutional ancestor: graph disjointness is not a mandatory condition for J2.
R6: evidence shows correction happened but not outcome change; count implementation without attributing effect.

## Genealogy audit references
- [MQR-4.89 original exact rational causal bridge](../experiments/mqr-4.89/causal_nonidentifiability_bridge.py) and [4.87 Real Lang](../experiments/mqr-4.87/real_lang_p1.py).
- [4.101 fallible standard and sharpness charter](../docs/MQR-4.101-CHARTER.md).
- [4.107 evidential-history and stopping-rule rival](mqr_4107_evidential_history_equivalence.md).
- [4.109 sufficiency versus calibration authority](mqr_4109_provenance_sensitive_sufficiency.md).
- [4.111 measurement-created states and retrodiction](mqr_4111_irreversible_retrodiction.md).
- [4.113 stochastic experiment comparison](mqr_4113_p1_stochastic_channel_comparison.md).
- [4.120 P7 limited reapplication](mqr_4120_p7_causal_nonidentification.md).

## P8 verdict and stopping discipline
CONTRACT-OPEN / DATA-HOLD. No user-supplied or source-audited real remedy panel identified, no defensible causal intervention definition, no independent effect study evaluated in this phase. Therefore there is deliberately **no eighth synthetic PASS**, no claimed causal result, no new Lean/Rust reimplementation, and no transition to 4.121. Only begin empirical estimates after authentic sources are inspected and a design exposes a discrimination unavailable to older MQR.

Inherited Greenberg seven-row ambiguity, CCQM historical calibration and covariance, 4.118 Kuhn/Harvest candidates, and 4.119 R0/R+/E actual assessor comparison remain OPEN/HOLD.
