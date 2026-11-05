# MQR-5.3 R46-A — Historical Discrimination Before Meta-Theory

Date: 2026-11-05. Status: RESEARCH DESIGN / HISTORICAL VERDICT HOLD / NOVELTY HOLD.

## Decision

Do not publish a new theory of 'meta-paradigm' or treat existing scientific-philosophical traditions as simple decision rules. First test whether historically grounded rivals *actually disagree* about one clearly fixed episode and one fixed question.

Distinguish three question types:
- **Pursuit**: whether it was rational, given available means and uncertainties *at the time*, to invest in a problem or exploratory intervention.
- **Acceptance**: whether independent available evidence justified a particular claim.
- **Progress**: whether the episode expanded reliable explanatory, experimental, or conceptual capacities (relative to a specified baseline).

These are not automatically scalar or commensurable. A pursuit verdict does not imply acceptance; success does not retroactively establish rational pursuit.

## Primary candidate: 1952–1955 in-vitro protein-synthesis investigations

Use the R40/R45 reading lineage: Siekevitz (1952), Zamecnik/Keller (1954), Hoagland (1955), and Rheinberger's later reconstruction. The candidate is *not* assumed to be a single revolution. The actual source collation must fix dates, feasible experimental alternatives, uncertainty at time of decision, prior accepted results, and retrospective reinterpretations.

Questions:
1. Before a mechanism had been established, were fractionation and alternate assay arrangements rational pursuits? Why, using only contemporary evidence?
2. Which observations supported which narrower molecular claim, and which hypotheses remained underdetermined?
3. Did a novel preparation, assay, or response pattern change the research target or merely improve access to an already specified one?
4. Are later standards being imposed retroactively on earlier actions?

## Rivals and adversarial tests

Relevant interpretive traditions: Dewey on the indeterminate situation/problem articulation; Chang on epistemic iteration and plural alternatives; Kuhn on puzzle/problem formation; Kitcher on significant scientific questions; Longino on critical interaction; Feest on exploratory operational concepts; Brigandt on goals and conceptual change; Haueis on tool-dependent conceptual formation.

**Non-negotiable:** no function in the Python prototype is assigned to any of these thinkers. A philosophical position requires an actual primary-text argument with edition/page, context and an independently reviewed interpretation before constructing a verdict. Rival positions may share a verdict for different reasons: then compare explanations, not just decisions.

## Falsification gates

- H1: At least two source-grounded interpretive positions produce a genuine conflicting *determinate* verdict for the same question, episode and time-relative evidence. If no conflict, DISCRIMINABILITY FAIL, not success by relabeling.
- H2: The discrepancy is not due to unnoticed differences in available information, standards of success or the meaning of 'problem'. If it is, repair operationalization before interpretation.
- H3: A proposed MQR synthesis explains the case better than the strongest prior art without fictitious historical quantities or post-hoc weight tuning. If it does not, PRIOR-ART SUBSUMED.
- H4: A held-out second historical episode challenges the synthesis. If it only fits the discovery case, GENERALIZATION HOLD.
- H5: Physical/scientific historical original and modern philosophical reconstruction receive separate provenance. Neither is an independent empirical experiment by the present researcher.

## Computational witness

`language/real/experiments/mqr53_r46_verdicts.py` enumerates Boolean synthetic conditions to locate incompatible determinate verdicts. The demonstration uses invented toy rivals: feasible AND new-question versus feasible AND independent-support. Exactly 2 of 8 total assignments disagree. This only checks **a formal discriminator's behavior**. It says nothing about Dewey, Chang, or a historical episode.

UNKNOWN is explicitly excluded from disagreements. Verdicts from distinct questions are rejected. The interface is bounded to 16 Boolean axes, without continuous, temporal, or multi-valued historical representations.

## Research / Real Lang separation

This is a Python experiment under Real Lang's research directory, **not** a new Real Lang grammar feature, Rust compiler implementation, executable semantics, or language release. It is potentially useful for future typed epistemic workflows, but the next step is historical validation, not syntax promotion.

## Source and custody status

Historical arguments in preceding MQR-5.3 R40–R45 reports are leads, not re-collated source-level evidence for this R46 episode. No new raw PDF or statistical history data were created. GitHub stores the computational/research artifact; Notion R46 semantic synchronization and Drive artifact custody must be separately verified, never inferred from a GitHub commit.

## Next

R46-B: primary historical chronology and event-by-event quotation ledger; R46-C: full-strength rival arguments with explicit comparability tests; R46-D: negative cases and independent second episode; only then return to macro-theory.
