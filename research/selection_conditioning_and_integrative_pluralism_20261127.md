# MQR 5.4 — Selection-conditioned scientific evidence and limits of integrative pluralism

2026-11-27 | MQR 5.4 OPEN | no artificial sequential research numbering

## Executed source audit

The existing Drive archive contains the exact historical 2024 GBIF ZIP, SHA256 5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836. Local Python read all 29,543 records, grouped the 14,651 Spring records by authentic FinBIF Document URI, and reproduced the 2,272-document contingency from the previous cycle. Script [finbif_selection_audit_20261127.py](../language/real/experiments/finbif_selection_audit_20261127.py) local git hash-object and GitHub blob both bd5e7f8c5a90c6563a3e20915d242a09fdde0bae. This is actual execution with exact source and matching committed code, not new field data or whole-repository CI.

Here A denotes a noninterval PRESENT candidate first observation, B an interval PRESENT candidate weekend observation. These are operational categories, not certified field visits or native form meanings.

| Year | both | A only | B only | neither |
|---|---:|---:|---:|---:|
|2013|83|112|21|0|
|2014|84|96|34|0|
|2015|33|59|32|0|
|2016|97|128|33|0|
|2017|37|63|22|0|
|2018|53|96|27|0|
|2019|40|124|29|0|
|2020|94|161|97|8|
|2021|51|108|29|0|
|2022|50|66|10|0|
|2023|43|86|35|0|
|2024|30|79|22|0|
|total|695|1178|391|8|

All eight double-negative documents occurred in 2020 and had five interval-coded records. All twelve annual strata show negative cross-product contrast. Stratifying by number of interval rows gives six negative, three uninformative strata; jointly by year and number of interval rows gives 54 negative and 24 uninformative, zero positive among 78 strata. Mantel–Haenszel descriptive odds ratios: year .0104780666, slots .0104297506, both .0102589900, aggregate .0120712639. These are not adjusted causal effects, and the slot count may itself be downstream of reporting mode and selection.

## Exact alternative: selection alone

For strictly positive underlying cell masses q_ab and selection probabilities s_ab, conditional odds ratio OR_selected = OR_population times s11*s00/(s10*s01). The observed cells (695,1178,391,8) can be reproduced exactly from an independent hypothetical population with unnormalized masses (695,1178,391,1178*391/695), selecting all but the 00 cell with probability 1, and selecting the 00 cell with probability 8/(1178*391/695) = .0120712639. The hypothetical mass 662.730935 is NOT a real count of missing documents or an estimate of the actual inclusion mechanism. More generally for any strictly positive target distribution q and observed p, choose positive k <= min_i q_i/p_i and s_i=k*p_i/q_i. Then q_i*s_i/sum(q*s)=p_i exactly. This is elementary selection non-identification, not a new mathematical theorem. The exact rational construction is checked in the executed script. See Cole et al. (2010), https://doi.org/10.1093/ije/dyp334 and Elwert & Winship (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC6089543/.

The source's actual selection mechanism is unverified. Taxon filtering, producer form inclusion/defaults, participation, actual flowering, and export conversion remain alternatives. The historical source's complete original form denominator, actual effort and generation rule remain necessary. Do not present the eight observed double negatives as evidence a particular participant did or did not survey. No new source-level native records obtained this cycle.

## Comparative Q2/Q4/Q5/Q6 research: when integration is admissible

Read the actual held text of Mitchell (2023), The landscape of integrative pluralism, pp.262–263, 285–287, https://doi.org/10.1387/theoria.25273, Drive 1Ps_Ki9rIuDa-SY2zyb3jRoz3tY-a18RS. She describes partial and perspectival representation and compatible explanations that may target different aspects, and her example of joint X-ray/NMR refinement explicitly conditions integration on reliable detection of the target. Correct systematic discrepancies, compare feasible structure ensembles; a compatible overlap can narrow the set, while incompatible constraints need not. The crystallized and solution protein need not be in identical physical states. Her text is not an assertion that agreement unconditionally establishes truth.

Read the actual held text of Deulofeu & Suárez (2023), pp.314–315 conclusion, https://doi.org/10.1387/theoria.23871, Drive 1bgd9vw84e3tZ80MEGBPmonjg0xUk-Kb_. Their criticism distinguishes epistemic incompatibility/goal dependence and cases of allegedly higher-level causation without lower-level explanatory role. They reject integration as a universally desirable or achievable research goal while valuing the approach in its domain. The metaphysical claim is their argument, not an empirically settled result.

Primary structural biology bibliographic cross-check: Carlon et al. (2016), https://doi.org/10.1021/jacs.5b11598 (JACS 138, 1601–1610); public abstract reports protein–RNA complex joint refinement and compatibility within experimental uncertainty. Rinaldelli et al. (2014), https://journals.iucr.org/d/issues/2014/04/00/dz5299/; indexed text differentiates small changes and larger conformational changes, but direct full-text fetch failed (cache miss). No primary raw data, structural model or exact fit statistics reproduced. These references correct/clarify older R98 bibliographic ambiguity without pretending to have audited that entire old dossier.

MQR synthesis: before intersecting constraints C_A and C_B, specify target equivalence or a warranted target transport map, sampling/selection mechanisms, uncertainty and representation. If both are valid confidence sets for the SAME parameter theta with respective failure bounds alpha,beta, then the union bound gives P(theta in C_A intersect C_B) >= 1-alpha-beta, without requiring independence. Merely overlapping sets cannot guarantee correctness, and this bound does not apply if they are not valid confidence sets for the same target. This is a standard mathematical consequence, not a new experimental law. FinBIF is a concrete contrast: matching occurrenceStatus fields does not establish matching observational targets or comparable selection. The physical bridge remains open. The current doctrine permits legitimate cited synthesis, reconstruction and clarification as valuable scholarship; novelty is not an absolute veto.

## Scored research management and decisions

See [priority and evidence ledger](data/decision_priority_and_selection_lira_20261127.json), 10 tasks, 11 decisions. P=.25V+.30D+.20F+.15I+.10K. Declared planning ratings, not calibrated probabilities. Retrospective completed-task scoring marked as such. Highest eligible next task is cross-case structural biology primary refinement comparison P=.9055; Maxwell source-image and units .8325; 4.97 heldout revisits .762. Original historical source form/event bridge P=.787 HOLD access; independent LIRA raters P=.736 HOLD; extra binary toy P=.462 DEFER. For all 32 extreme combinations of independent +/-20% weight multipliers, renormalized, structural biology ranks first among these ready tasks, which reflects only declared scores and candidate set. No automatic version promotion. All seven founding questions remain protected.

Current shared 00_MISSING_LITERATURE.txt read back via Drive; 56 continuous numbered entries, newer than the old local 50-entry attachment and earlier 53-entry report. No write this cycle. Two principal philosophy texts already owned; primary protein papers only bibliographically checked here. Do not overwrite another project's shared edits; no duplicate missing list. Reassess exact custody and register genuinely needed absent texts in existing TXT during next source acquisition.

Status: exact source analysis PASS scoped; actual selection mechanism HOLD; general cross-science reference bridge HOLD; historical equation-image parity HOLD; new independent field validation absent; 5.4 OPEN.