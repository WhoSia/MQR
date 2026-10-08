# MQR-4.94 — Fixed-Predictor Sensitivity Preseal

**Timing:** Retrospective second-stage diagnostic designed **after** the initial five 4.94 results. Not independent blinded confirmation.

**Motivation:** Previous latitude-blocked validation changed both FIT and G. To reduce this confound, hold its FIT512, source-fitted predictor, preprocessing, EAST target P64, source source code/hash and target oracle constant, and change only the source validation G64.

**Far G:** original q50 WEST top-20%-latitude candidate, SHA rank `mqr494-blockG|site`, first64. Replicate previous NW 1.1030750271157368, KMM 0.7958976661740039, target loss oracle 0.89985903200522.

**Near G:** remaining WEST southern site candidates latitude <= WEST-site 65th percentile, excluding fixed FIT; choose first64 with SHA rank `mqr494-blockG-near|site`. Do not use labels/risks in selection. Source labels read only for selected G. Original NW/MCE and KMM_error B=10 calculate new risk against SAME EAST target X. Target labels read only for final oracle check.

Report FIT–G nearest Haversine min, median and proportions within 0.1/1/5km, validation class/year composition, source KMM ESS, risk-estimator errors and any method-winner reversal. Fail instead of relaxing exact frozen rule if infeasible.

This isolates learned-predictor identity, not the causal role of spatial distance: G geography, class mix and year distribution may still differ. One diagnostic only; bounded 4.94 closeout next. Original Serov author file/commit hashes remain unchanged; previous 4.93/4.94 results and HOLD verdicts retained.
