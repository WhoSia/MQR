# MQR-5.3 R46-D — A historical negative-control matrix, ex-ante inquiry, and nonidentification

Date 2026-11-05. Historical primary evidence: Zamecnik & Keller (1954), *Relation Between Phosphate Energy Donors and Incorporation of Labeled Amino Acids into Proteins*, Journal of Biological Chemistry 209:337–354, Research OS Drive ID `1FJx6ghWM3QF4wpmQQlAdgDZcZxJlxp6n`, Table I printed p.340, narrative pp.339–341.

## One actual experimental choice, not a fictional historical funding decision

The paper uses a gentle homogenizer and evaluates preservation of cell-free radioactive leucine incorporation under energy-supporting conditions. The authors cite Bucher's separate cholesterol-incorporation work as a prior stimulus. This is evidence of a historically **stated methodological reason** to try gentler homogenization, not a quantified claim that it had the highest expected utility among every laboratory option. The paper was received 1954-01-27; that is a manuscript receipt date, *not* an exact date on which each flask was run.

## Directly transcribed Table I conditions and outcome

| Flask | Homogenization seconds | Pestle–tube gap, mm | Nicotinamide (0.01 M) | Hemolysate (0.1 mL) | Leucine incorporation cpm/mg protein |
| --- | ---: | ---: | --- | --- | ---: |
| 1 | 15 | 0.6 | no | no | 8 |
| 2 | 15 | 0.6 | yes | no | 64 |
| 3 | 15 | 0.6 | yes | yes | 0.8 |
| 4 | 120 | 0.4 | no | no | 9 |
| 5 | 120 | 0.4 | yes | no | 21 |

`Flask 3`'s nicotinamide setting is read in context of the original narration identifying nicotinamide omission in flasks 1/4 and hemolysate addition in flask 3. Verify column layout visually before declaring independently figure-verified. Readout: counts/minute per mg of washed protein; single reported conditions, not a sample of replicate population means. No uncertainty estimates or confidence intervals are inferable from this table alone.

Observed *descriptive* contrasts:
- 2 minus 1 = +56 cpm/mg: nicotinamide-associated contrast at 15 seconds, 0.6 mm, with no hemolysate.
- 3 minus 2 = -63.2 cpm/mg: hemolysate-associated contrast at the same short homogenization/nicotinamide settings.
- 5 minus 4 = +12 cpm/mg: nicotinamide-associated contrast at 120 seconds, 0.4 mm.
- 5 minus 2 = -43 cpm/mg, BUT both duration and gap changed, so *neither factor's independent causal effect* is identified by that comparison.
- Apparent difference-in-differences for nicotinamide contrasts: (21−9)−(64−8)=−44 cpm/mg. This is a purely tabular conditional-interaction summary between two **bundled homogenization regimes** and nicotinamide; it is not a separately identified interaction for duration alone or for pestle gap alone. No sampling variance provided.

Important experimentally reported qualification: with alternative phosphate-energy donors (phosphocreatine, PPA, 3-PGA) the authors find that an intact glycolytic system was no longer required and that more complete versus incomplete homogenization made little difference (Table II). Hence failure in one assay regime is *not* global failure of a research line, nor a universal property of homogenization. A strong negative-control result may instead motivate a change of experimental mediation.

## A strong conceptual counterexample to naive progress claims

1. Higher observed readout ≠ mechanism confirmed.
2. Lower readout ≠ research direction disproved.
3. A poorly discriminating assay may be worth pursuing if it reveals which mediating conditions are indispensable, but this is a possible ex-ante reason—not a historical decision theorem.
4. Controls and successful alternative energy sources changed the *inferential target* from generic labelled incorporation to the biochemical conditions supporting that readout.
5. To attribute causes to independent manipulations one must first check intervention equivalence and co-varying factors. Table I's strong-homogenization comparison changes both seconds and gap; Table II changes energy support. Raw counts do not directly identify peptide bond synthesis.
6. Neither the actual resource cost nor contemporaneous ranking of unchosen programs has been recovered. Therefore **pursuit permissibility** may be discussed conditionally, but **comparative pursuit priority** is HOLD.

## Philosophical assessment of precisely this episode

Dewey (1938) p.108–109: an indeterminate problem is institutionally formed through inquiry; choosing the problem makes experimental information relevant. Fits the progressive construction of the problem but does not automatically endorse each specific tube setting.

Feest (2012) pp.167–189: the experimental definition/procedure may serve as a tool in building concepts and theories. Analogical transfer from cognitive psychology to biochemical fractionation is interpretive, not a direct verdict from Feest.

Chang (2012) §5.1.5: preservation of alternative inquiry and intensive resource allocation are distinct. Table II's viable alternative energy routes help illustrate option plurality, not a claim about actual funding priority.

Kitcher (1993), Scientific Practice section 'Significant Questions and Accepted Statements': scientific practice includes significant problems and accepted statements and criteria. Neither Table I nor its later outcome establishes the project's significance ranking relative to other feasible 1954 laboratory programs.

Lari (2024): a goal-relative methodological criticism is not the same argument as meta-level criticism of the goals of a discipline. Here the tests remain predominantly within the shared goal of explaining protein synthesis; there is insufficient evidence of a meta-level goal change.

**Verdict:** This historical case supports a meaningful *within-program* negative/control comparison, not a documented case of an irrational research program, rejected revolution, or direct contradiction among these philosophers. Historical ex-ante choices and a separate truly failed research program remain further source tasks.

## Counterfactual data requirement

To disentangle duration and gap, need (at minimum) the missing regimes 15 s/0.4 mm and 120 s/0.6 mm under matched medium, response, and source samples, plus independent repeats/uncertainty and preparation-equivalence justification. Observed 2×2 designs on two bundled settings do not identify separately the two causal effects. We will not impute missing cells.

## Originality kill gate

If the account of problem formation, instrumental mediation, uncertainty and priorities can be exhaustively assembled from Dewey + Feest + Chang + Kitcher + causal experimental-design theory, record **PRIOR ART SUFFICIENT**. A new theory must add a specific discriminating explanation on an independently held-out historical case, not merely supply new labels.

Next R46-E: historical competing strategies rather than internal low-readout only; primary evidence of a genuinely abandoned research program and contemporary decision commentary. Keep historical test separate from theory promotion.

No PDF bytes altered, no new wet-lab work or numerical digitization claimed.
