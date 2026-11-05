# MQR-5.3 R46-V — Same data is not necessarily the same question: adversarial many-analyst papers

Date: 2026-11-05. All five papers below held as full Research OS PDFs; direct textual examination of three new contributions, original Breznau et al (2022), and correction (2024). Numerical figures not independently image-verified. No universal verdict on social science, sociological effects, or effect heterogeneity.

## Intake custody

Three fresh direct 00_INTAKE arrivals discovered after Stephenson (1956) was moved. Original 00 parent `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16`, destination `10_PAPERS` parent `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP`:
- Maya B. Mathur, Christian Covington & Tyler J. VanderWeele (2023), 'Variation across analysts in statistical significance, yet consistently small effect sizes', *PNAS* **120(3):e2218957120**, DOI `10.1073/pnas.2218957120`, Drive `1_f5TrM-tonVpl9k7kDswgCHlQ23VBgrA`, 118179 B. Metadata-only move+rename completed.
- Katrin Auspurg & Josef Brüderl (2024), 'Toward a more credible assessment of the credibility of science by many-analyst studies', *PNAS* **121(38):e2404035121**, DOI `10.1073/pnas.2404035121`, Drive `1s95yC7Rkxp52GK1BpiQzdL_00a4FWlFE`, 341123 B. Metadata-only move+rename completed.
- Per Engzell (2023), 'A universe of uncertainty hiding in plain sight', *PNAS* **120(2):e2218530120**, DOI `10.1073/pnas.2218530120`, Drive `1VpL2sCk2gRSlKVlrGwzoTm5UWW-DgIxp`, 111962 B. Already moved by another concurrent operation when this process rechecked; we did **metadata-only rename** in its confirmed 10_PAPERS parent, no redundant move.

Previously held:
- Nate Breznau et al (2022), 'Observing many researchers using the same data and hypothesis reveals a hidden universe of uncertainty', *PNAS* **119(44):e2203150119**, DOI `10.1073/pnas.2203150119`, Drive `1lsyHjglet1NaXlOf2EYfNPtW92jU5aYK`. Direct original abstract and research framing inspected.
- Breznau et al (2024), 'Correction for Observing many researchers...', *PNAS* **121(26):e2410677121**, DOI `10.1073/pnas.2410677121`, Drive `1NSkJ1yxy8vZ4EUP6SwD5BQa3mbe5_G4z`. **Corrects original Figure 1**, published June 20 2024; corrected graphical data not digitized. If invoking the figure, use corrected version not uncorrected 2022 screenshot.

## Direct cross-paper conflict in how to interpret output variation

### Original Breznau et al (2022)

73 teams, 161 researchers, same observational dataset and a broadly stated hypothesis concerning immigration and public support for social policies. They report dispersion in effect directions, significance and subjective interpretations, and that coded researcher decisions explained little of variance in results. They conceptualize this as an often hidden analytic-choice uncertainty; claims must remain attached to specific models, outcomes and estimates. The 2024 correction requires using the corrected Fig.1 if quantitatively reproducing it.

### Engzell (2023)

Argues the 'same hypothesis' encompasses multiple **operational targets** (different immigration and policy-support indicators, countries, within-/between-country contrasts and model specifications), i.e. teams sometimes estimate *different quantities*. Within-team specification variation must be separated from between-team variation; a number of apparently discordant results may reflect heterogeneous research questions, rather than arbitrary analyst disagreement on an unchanged estimand. Notes that one team found inadequate measurement and stopped rather than falsely claiming a causal assessment. This is directly source-grounded, not a newly invented MQR criticism.

### Mathur, Covington & VanderWeele (2023)

Distinguish statistical significance categories from substantively meaningful estimate sizes. In the Breznau collection, their letter reports **90% standardized point estimates in [-0.037, +0.037]**, and a meta-analytic model giving **90% of inferred population effects in approximately [-0.014, +0.014]**. These are **their reanalyses of Breznau results**, not newly recoded estimates by this project. The latter interval is model-dependent, not a nonparametric guaranteed effect range. Mixed significance signs can coexist with small effect magnitudes.

### Auspurg & Brüderl (2024)

Emphasize three distinct failure modes in many-analyst studies: (1) distinguish sources of variation (sampling uncertainty, discretionary choices and substantive estimand heterogeneity), (2) consider incentives and selection in participating analyst teams, (3) meta-analyze using comparable effect metrics and appropriate precision/heterogeneity structure. They warn about pooling incompatible estimands and misreading statistical significance variation. This is a **strong existing methodology**, not a model deficit newly discovered by MQR.

## Is this a genuine same-question contradiction?

The original's interpretation 'significant variation in research findings' and critiques 'small point estimates' are **not logically contradictory** absent a fixed meaning for 'variation' (spread in p-value classes vs actual effect-size heterogeneity vs within-team model choice). The critique does, however, directly contest how strongly the original results should support an inference about reliability of published science.

The historically real opposing judgments are about the **interpretation and methodological validity of a metaresearch design**, not about the causal claim that immigration decreases policy support. Do not take sides on that distinct empirical/political hypothesis from these methodological papers.

Before comparing analysts, register an estimand or target tuple:
`(population, exposure, outcome, intervention/conditioning regime, unit, measurement, target estimand, time)`.
One dataset and one English-language hypothesis can contain several incompatible estimands. Sample size by itself does not repair this.

## R46-T bridge: target transport

Stephenson (1956) demonstrated operational sample-label observations even when a different *specific viral-product* endpoint was negative. The many-analyst letters similarly challenge promotion of the same broad descriptor ('same hypothesis') into an identical fine-grained target. These are **analogies about claim-scope**, not proof that tissue fractionation and social-data estimand selection have the same causal mechanism.

**NOVELTY REJECTION:** The mismatch between fixed observed data and different targets was already explicit in Engzell 2023, Mathur 2023, Auspurg & Brüderl 2024 and historical prior art in Feest/Rheinberger. Merely applying a target-typing scheme adds no original philosophy. A new framework would need a pre-specified counterexample to these strong baseline methods in a genuinely new setting.

## Source handling / no overclaims

This is a reader's adversarial text comparison, not reproduction of Breznau's 1,253 models, individual 73 team data, the Mathur numerical meta-analysis, or the corrected 2024 Fig.1. The available numerical claims above are explicitly *published author's figures*, not this project's calculations. No SHA-256 audit or replacement of original PDF bytes performed.

Next R46-W: operationalize the precise same-target comparison using a source matrix with observed measurement, estimand, evidence origin, timestamp and independent controls. Validate against these prior accounts; if already sufficient, mark R46 prior-art kill gate and concentrate the remaining problem on conditions in which target continuity is itself empirically testable.
