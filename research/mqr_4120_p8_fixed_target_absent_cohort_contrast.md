# MQR-4.120 P8 — Fixed-Target Absent-Cohort Contrast and Selection Inversion

2026-10-17 · finite-population descriptive audit only; **not design-based causal estimation**.

## Exact data and question
MIT JTPA full source (11,204 rows, original earnings/Z in columns 2/3) https://economics.mit.edu/sites/default/files/publications/jtpa.raw ; the separate third-party recid-bearing Han tab https://github.com/chensy123-sys/Additive-IV/blob/main/JTPA/jtpa_han.tab supplies 9,223 retained IDs. The **1,981 absent IDs** are the complement under that conditional copy. Source bytes, author archive correspondence and historical row-exclusion rule remain unverified.

Use fixed outcome 1{earnings > 11,010}, MIT full-cohort earnings median, for *all* groups. No group-level recentering.

Group | Z=0 numerator/denominator | Z=1 numerator/denominator | crude difference
MIT full | 1798/3717 = .4837234329 | 3803/7487 = .5079471083 | +.02422367545
Han retained | 1515/3090 = .4902912621 | 3132/6133 = .5106799283 | +.02038866612
Absent complement | 283/627 = .4513556619 | 671/1354 = .4955686854 | +.04421302349

- Selected-minus-full Z-group crude contrast = **−0.00383500932**, or −0.3835 percentage points.
- At *fixed* outcome definition, absent group's Z=1 vs Z=0 crude contrast is +4.4213 percentage points versus retained +2.0389 percentage points.
- The retained group's conditional Y2 threshold recomputation at 11,187 changes its Z difference to +.02181893592; this is **+0.00143026980** from relabeling, distinct from selection at the fixed cutoff.
- Aggregate label prevalence almost cancels between selection and relabeling as established in the earlier P8 report, but subgroup contrasts need not cancel.

## Epistemological and causal ceiling
This is a real finite-sample descriptive decomposition, not evidence that historical exclusions were based on outcomes, or that missing persons had greater treatment effects. Under post-assignment selection, within-selected Z comparisons need not inherit original randomization. Causal estimand transfer to selected cohorts requires a selection mechanism, potential-outcome assumptions and experimental design reconstruction; no bootstrap/standard errors or Han dynamic-regime partial order were calculated here. MQR 4.101 selective verification, 4.107 evidence production history, 4.109 source-sensitive sufficiency, and 4.119 J1-versus-J2 warrant remain binding.

## Next discriminating tasks
Read author-side Han ZIP using byte-preserving access and its primary supplement, identify actual selection and Census/NCES merger predicate, validate full ID inclusion against a documented code path, audit whether selection occurs before or after Z2. Only then ask causal inference or whether policy ordering changes when target population/outcome cutoff is fixed.

## Verdict
FIXED_CUTOFF_ABSENT_COHORT_COMPARISON_PASS_BOUNDED; TARGET_DEFINITION_CONTROL_PASS_BOUNDED; HISTORICAL_SELECTION_CAUSE_HOLD; SELECTED_RANDOMIZATION_HOLD; ORIGINAL_POLICY_LP_HOLD; AUTHOR_BINARY_CUSTODY_HOLD. Remain MQR 4.120 ACTIVE/P8.
