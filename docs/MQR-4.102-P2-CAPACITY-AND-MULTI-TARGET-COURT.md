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

## Actual execution (CI verified)

[GitHub Actions #37938142064](https://github.com/WhoSia/MQR/actions/runs/37938142064) **SUCCESS**, at source commit `5416b43cb478d32e77512cbb1a6b1bfc9218b3bc`. The source-derived 487-row SHA-256 was checked, the script reproduced 402 paired and 76 disagreement labels, and **3,888 exhaustively enumerated small finite allocation problems** agreed with the claimed greedy single-target optimizer. The ten-case capacity-constrained table follows (all hypothetical reviews; no truth acquired):

| Target | Original interval full width | Width after hypothetical ten reviews, cap 3/record | Allocation of ten |
| --- | ---: | ---: | --- |
| Beat-pooled decision difference | `76/201` ≈ 0.3781 | `22/67` ≈ 0.32836 | sel103 3, sel114 3, sel117 3, sel123 1 |
| Equal-record decision difference | `236237/588225` ≈ 0.40162 | `200587/588225` ≈ 0.34100 | sel103 3, sel117 3, sel123 3, sel221 1 |

The equal-record objective has many tied optimal allocations (all chosen 30-pair record cases have equal benefit until available counts are used). **In the present ten-review source/cap contract, minimizing the worst of the pooled and equal-record widths is degenerate**: equal-record width dominates the worst-case objective at its optimum. A minimax score of `200587/588225` was found (one tie-optimal allocation sel103 1, sel117 3, sel123 3, sel221 3); this does NOT demonstrate an independently nontrivial two-target tradeoff or validate robustness for all cost specifications.

The capacity-three restriction, reviewer availability and all review outcomes are mathematical assumptions. No actual adjudications were purchased or performed. Selection based on nonrandom source-observed disagreements has no population-generalization guarantee. **P2 CLOSED BOUNDED for pinned-source allocation arithmetic and finite counterexample tests only; 4.102 OPEN; scientific independent adjudication HOLD.**

### Next falsification

An actual new objective conflict requires genuinely competing target weights or heterogeneous review costs under an explicit target-population measure, not simply writing “minimax” over two targets when one dominates. Changing eligibility due to a fallible selection mechanism also requires measured eligibility. Re-evaluate with a three-way independently justified conflict before claiming general robust optimization.

**4.103 is a proposed next formal scientific question only; do not open without the user's decision.**
