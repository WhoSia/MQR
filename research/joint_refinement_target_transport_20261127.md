# MQR 5.4 — Joint refinement, target transport, and structural disagreement
2026-11-27 | conversation MQR 46 | 5.4 OPEN

## Continuity and source scope
Prior prospective decision P=.9055 for structural biology, from research/selection_conditioning_and_integrative_pluralism_20261127.md (3efb76ea). Previous two commits verified WhoSia author/committer. Current doctrine read, including E/C/G/L and P. Prior-art genealogy: Notion MQR-0.35-B (https://app.notion.com/p/3c9ef561cf92818e8a9bf38ed23ebe44): Mitchell, Darden–Maull, Galison, partial structures already constrain novelty. Integration without reduction and productive bridges are not inventions of MQR.

## Published empirical evidence, not independent experimental replication
Rinaldelli et al. (2014), Acta Cryst D70 958–967, DOI 10.1107/S1399004713034160, full HTML https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/ — directly read methods, Tables 1–2, results and discussion. Exact work not found in bounded Drive title/author search; public full text is accessible, custody still unconfirmed. Publisher PDF link https://journals.iucr.org/d/issues/2014/04/00/dz5299/dz5299.pdf (not byte-acquired here). Authors combine X-ray data with long-range solution NMR restraints; weights empirically adjusted, including monitoring free R and geometry. Selected mobile residues excluded for cMMP1; ubiquitin flexible tail excluded. These are explicit scope limits. Supplement has protocol, coordinates and data (DOI 10.1107/S1399004713034160/dz5299sup2.zip); not downloaded/reexecuted.

Table 1 selected values, transcribed from HTML and descriptive differences computed with integer thousandths:
|system|Q_RDC X only|Q joint|R_free X only|R_free joint|backbone RMSD Å|
|---|---:|---:|---:|---:|---:|
|cMMP1|.414|.160|.264|.267|.039|
|Ub|.360|.121|.158|.160|.060|
|GB3|.146|.081|.132|.134|.022|
|CaM|.398|.308|.142|.147|.028|
|CaM-DAPk|.540|.201|.304|.307|.121|

Absolute Q decreases .254/.239/.065/.090/.339; R_free increases .003/.002/.002/.005/.003. All improve Q, only three meet the authors' typical strict Q<.2 threshold, CaM-DAPk borderline. At strict thresholds .15/.18/.20/.202/.25/.31 the counts are 2/3/3/4/4/5. This is retrospective descriptive sensitivity, not a validated threshold. The boundary crossing near .201 is why binary classification alone is inadequate. The largest Q improvement belongs to a borderline case. The R_free values were used for empirical weight selection, so they do not constitute an untouched outer validation set for this comparison. A small backbone RMSD (CaM .028 Å) is not evidence of fit to both observations.

Carlon et al. (2016), DOI 10.1021/jacs.5b11598, https://pubmed.ncbi.nlm.nih.gov/26761154/ — abstract checked only; reported preservation of overall domain arrangement and binding interfaces in protein-protein-RNA complex. Exact paper not found in bounded Drive search; no full-text validation asserted. Carlon et al. 2019 DOI 10.1007/s10858-018-0212-3 and 2020 complementarity DOI 10.1016/j.yjsbx.2020.100019 identified, not fully read due to access challenge.

## Reconstruction
A joint optimizer selects a representation, not an ontology. Distinguish same molecular identity, same environmental state, compatible predicted measurements, preserved component, and unique structural representation. A constrained common model can succeed even when the underlying solution is an ensemble; mismatch may reflect genuine regime-specific geometry, forward-model error, dynamics, selection or constraints. Thus neither agreement nor mismatch alone establishes target identity. Compare model classes H_shared: theta_X=theta_N, H_transport: theta_N=T(theta_X,z), H_distinct: separate parameters. Estimate on training restraints; reserve genuinely unused restraints or independent modality predictions for outer validation. Compare complexity and uncertainty, and avoid tuning the outer validation set. A bridge can be productive when it predicts which components preserve structure and which transform under an environmental change. This is a research hypothesis and standard constrained modeling synthesis, not novel theorem or tested cross-science law.

## LIRA (retrospective declared judgments, not probabilities)
E published Table 1 .98; methods/weight selection .96; Carlon abstract .75; prior-art genealogy .88; local arithmetic .99.
Claim C/G/L: all five Q reductions .99/.18/.82; three strict threshold successes .99/.15/.80; common target identity follows from Q improvement .03/.02/.04; R_free not an untouched outer test in this protocol .95/.35/.89; regime-dependent transport as a discriminating research question .88/.40/.95; MQR novelty over Mitchell established .10/.08/.10. Version promotion .04.
Next candidates (V,D,F,I,K; P): supplement data custody and reproduction (.94,.93,.65,.90,.70; .8455, HOLD until access + program/runtime); Maxwell source-image/units use previous .8325 (READY subject to source access); theory comparison against Darden–Maull (.96,.88,.86,.85,.88; .8925, READY if held original available); extra toy model (.55,.40,.95,.25,.80; .5600, DEFER). These new judgments are planning ratings after this source reading; candidate access gates need rechecking. No automatic novelty veto.

## Custody and limits
No raw structural experiment run; no newly acquired PDF; HTML body was read, not PDF image parity. Shared missing TXT latest readback contained 60 entries, not 56. No overwrite attempted because a safe raw-byte replacement reference and concurrency check have not been established. No duplicate registry created. Tool discovery and minimal descriptive calculation used; performance optimization not material for five rows. Maintain previous FinBIF source HOLD and all founding branches.
