# MQR-4.120 P8 — Population-Relative Outcome Definition under Sample Selection

2026-10-17. Full-text observed-data comparison; **a new bounded MQR measurement/selection result**, NOT identified causal selection mechanism or policy effect.

## Concrete sources and computation
MIT original jtpa.raw, 11,204 rows × 19 fields, earnings in column 2: https://economics.mit.edu/sites/default/files/publications/jtpa.raw . Third-party retained Han tabulation, 9,223 rows with unique MIT recid, earnings column 4: https://github.com/chensy123-sys/Additive-IV/blob/main/JTPA/jtpa_han.tab . The same 9,223 earnings and shared covariates exactly match Zenodo jtpa.csv according to earlier P8 cross-audit, but official Han binary ZIP is not verified.

Compute the usual finite sample median of earnings in both populations:
- MIT full-source median (11,204): **USD 11,010**; both central sorted order statistics are 11,010.
- Reconstructed analytic cohort median (9,223): **USD 11,187**.
- Difference: USD **177**.
- On the *same 9,223 retained units*, construct two binary outcomes: 1{earnings > 11,187} and 1{earnings > 11,010}. These disagree for exactly **36 retained observations**, with no change whatsoever to their recorded earnings. Count is computed from full parsed records.

This is a concrete finite observation that an endogenously **population-referenced binary outcome is not invariant under sample selection**. In mathematical form, if P_S is the selected empirical distribution and T(P) is its median, the derived label L(y;P)=1{y>T(P)} depends on P as well as y. A sample-selection operator S may change T(P), and hence L(y;P), even for y belonging to both samples. No counterfactual or statistical significance is implied.

## Non-commutativity formulation
Let B_P denote labeling all rows relative to population P's median and R_S denote row restriction to S. Comparing R_S B_P (labels computed using full P, then restrict) against B_{R_S P} R_S (restrict, then derive labels using subset's median) yields **36 differing labels** for the real JTPA records in this case. The operators fail to commute on this dataset. This is a well-known target/measurement-dependence fact, **not a claimed novel general theorem**; the empirical instantiation and explicit provenance-aware scope are the added value.

## Original MQR intellectual lineage
- Measurement quotient: numeric observations are not the same object as target-specific judgments built by a map.
- MQR-3.100 and 4.53: informativeness/ordering depends on measurand/target; reject universal scalar progress.
- 4.101: selective verification and fallible reference class shifts a decision target.
- 4.107 and 4.109: the retained statistic and the generation history differ; source authority isn't established by fit.
- 4.113: Blackwell information order pertains to specified experiment/target, not historical calibration and authority.
- 4.119–4.120: J1 validity under an evaluative rule does not certify J2 legitimacy of selecting that rule/target population.
- 4.89 pre-existing rational Bernoulli SCM nonidentification not duplicated.

## Warrant boundary
The fact of a 36-label difference does NOT show which 1,981 source records Han's original code excluded or why; it does not prove selection-induced treatment effect bias or changed causal policy ordering. A fair comparison of policy effects requires consistent outcome definitions and target populations. Han's actual dynamic-regime LP is not implemented. The codebook/quantile tie convention and third-party copy remain custody-limited.

## Next falsification
Verify official Han file bytes; recover direct dataset construction/row inclusion predicate; compare restricted full-source and selected-sample estimands at identical outcome thresholds *before* studying the effect of recalibration of those thresholds. If policy-ordering is studied, recompute the original study's LP using its official assumptions and document every redefinition.

## Decision
FULL_VS_SELECTED_MEDIAN_DIFFERENCE_PASS_BOUNDED / SAME_UNITS_36_LABEL_CHANGE_PASS_BOUNDED / SAMPLE_SELECT_AND_RELABEL_NONCOMMUTE_OBSERVED / SOURCE_SELECTION_REASON_HOLD / HAN_ORIGINAL_CAUSAL_POLICY_ORDER_HOLD. Remain 4.120 ACTIVE/P8 and preserve all inherited Greenberg, CCQM, Harvest, 4.119 real assessor and original ZIP integrity HOLDs.
