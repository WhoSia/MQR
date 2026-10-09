# MQR-4.102 — Internal P2: Capacity-Constrained Adjudication & Multi-Target Ambiguity Court

**Formal name unchanged:** MQR-4.102 — Adjudication Allocation, Decision-Contrast Identification & Selection-Robust Verification Value.

**New attack (2026-10-09):** The original P1 assumption that any ten selected disagreements can receive independent review is a *counterfactual availability assumption*, not an empirical fact. Introduce audit capacity c_r per ECG record; test how optimal selection changes if only c_r cases per stratum can actually be verified, and if the decision maker has not fixed the target in advance. The cap of three per record is **invented for mathematical stress-testing**, not an observed PhysioNet lab capacity. No independent truth adjudications have been acquired.

Use the exact source-derived 487-row QTDB receipt (SHA-256 `d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842`); 402 first-and-second-reader complete opportunities and 76 disagreements, 85 missing second-reader outputs. Illustrative threshold 440ms remains strictly **nonclinical**.

For n_r observed paired cases in record r, d_r binary disagreements and hypothetical successfully certified s_r≤min(d_r,c_r), the **full width** of the risk-difference identified interval on the paired 402 is
`W_pooled(s)=2 Σ_r (d_r−s_r)/402`.
For equal-record weighting, `W_equal(s)=2 Σ_r (d_r−s_r)/(11 n_r)`.
These are classical finite independent-free-truth sharp endpoints, **conditional on genuine true labels for every selected audit case**, with unknown interval center until labels are observed.

Under capacity constraints, minimizing either width is equivalent to choosing the largest eligible *target-specific* weight for each review. A greedy solution is optimal here because every review is a unit-cost, separable constant-width contribution. Exhaustively enumerate finite models with varying d_r, capacities and budgets to challenge and verify greedy optimality. It is not a general proof of adaptive clinical trial allocation, heterogeneous real audit cost or review error dependence.

### Multi-target robustness

If weights between pooled and equal-record objectives are *unknown* (not Bayesian), let `W_λ=λ W_pooled+(1−λ) W_equal` for λ∈[0,1]. The worst-case width is exactly `max(W_pooled,W_equal)`; the minimax integer allocation for a ten-case budget with artificial cap three per record can be computed by exhaustive enumeration of feasible stratum count vectors. This is an **objective ambiguity** stress test, not an identified population target or realized review value. A lower worst-case width is an *if-independent-truth-were-purchased* statement.

### Strict distinctions and limitations

- Existing P1 unconstrained optimal ten-case selection is a special case. P2 includes finite capacities and compares single-target and minimax objectives.
- Choosing ten cases based on **observed disagreement** does not create true outcome measurements, and none are claimed.
- These strata consist of 11 selected QTDB ECG records with pairwise completion, not a representative future patient population.
- Missing h2 on 85 cases still prevents extending the 402-pair contrast to all 487 source opportunities.
- Peer reviewers may share the same measurement trace, adjudication error, annotation tools and institutional labels. No external certification of reviewer error rates has been acquired.
- Source QT values, annotation identities and PhysioNet authorship all belong to the original producers; no first-party ECG measurement or original theorem is attributed to MQR.

**Executed outcome:** see [GitHub Actions](https://github.com/WhoSia/MQR/actions) after main push; do not mark P2 closed until the new source-pinned code passes. 4.102 remains OPEN regardless. 4.103 is a **next formal title proposal only**, not a version to open without user confirmation.
