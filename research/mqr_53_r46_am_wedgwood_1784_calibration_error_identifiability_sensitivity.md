# MQR-5.3 R46-AM — Wedgwood 1784 silver-bridge calibration: assumptions, sensitivity, and contemporaneous tests

2026-11-09 KST. **Primary 1784 original image scan HELD but full image-text parity NOT accomplished**. Historical numerical detail from held Chang (2004) ch.3 pp.118–141, Drive 1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV, and Chaldecott (1975) Cambridge full original PDF DOI 10.1017/S0007087400013674 verified via web text; web PDF screenshot tool attempted and cache-missed. Do not present as independently verified extraction of Wedgwood 1784 page images.

## Computation check

Silver intermediary low endpoints spring water 50°F and boiling water 212°F; silver gauge 8 divisions: 162/8 = **20.25 °F/°S**. Historical 'boiling mercury' 600°F and same silver 27.5 divisions from 50°F: (600−50)/27.5 = **20 °F/°S**. Wedgwood treated the proximity as adequate support for using 20. Modern reference given by Chaldecott is ~675°F for boiling mercury, which would change that particular historical line to (675−50)/27.5=**22.7273 °F/°S** if all other conditions were unchanged: ~13.636% larger than 20. Do NOT apply as physical correction to all 1784 observations, since silver itself, mercury boiling setup and intermediate ceramic gauge were not independently characterized.

High bridge measured (W=2.25, S=66) and (W=6.25, S=92). ΔS/ΔW=26/4=6.5 S/W. With historical 20 F/S, slope β=130 F/W. Historical anchor T(2.25)=50+66×20=1,370°F => intercept α=1,370−2.25×130=**1,077.5°F**, so quoted affine mapping T(F)=1,077.5+130 W. For W=160 the rule yields 21,877.5°F, approximately as in Chang table 3.1. These are *reported historical extrapolations*, not actual modern furnace temperatures. Range between two bridge anchors 4 W; 160−6.25=153.75 W beyond right anchor = **38.4375×** calibration interval. Numerical slope error δβ (F/W) at W=160 vs 6.25 anchor produces δT=153.75 δβ. 1% of 130 as a hypothetical slope error (1.3 F/W) would create ~**199.875°F** difference at 160 W; this is a pure illustrative sensitivity, not historically observed uncertainty.

## Four separable assumptions

A1 LOW SILVER measurement comparability: mercury anchor and silver gauge expansion, including mercury saturation pressure and cup/gauge expansion.

A2 HIGH silver-to-clay comparison: same local furnace conditions, temperatures at both indicators and duration/batch history; silver gauge gives apparent *differential* expansion (silver minus ceramic gauge), not silver's pure material coefficient.

A3 MODELS: affine interpolation/extrapolation of silver expansion and clay shrinkage, not established by two paired points alone.

A4 MATERIALLY STABLE: firing duration and initial/final thermal history; batches/atmosphere/clay type same response. The 1782 heat-duration test Wedgwood used +3 min at low-red and +5 min full heat in his own unstable furnace as evidence; modern material response includes heat-work dependence. Chaldecott 1975 p.5 (online PDF), Chang 2004 p.120.

## Historical evidence and asymmetries

Chaldecott p.8–9 argues that Wedgwood could not have known several errors in his period: contemporary reference ~600 not 675°F for boiling mercury, temperature-variable silver expansion, clay shrinkage nonlinear and firing-duration dependent, and possible reuse of fired clay in the second temperature comparison. The last is explicitly only a *possibility* in Chaldecott, not proved original practice. Temperatures and data from later analyses cannot fairly become 1784-known refuters without mediation. 1786 Wedgwood article directly addresses standard clay manufacturing variance and fixed-point repair: **do not collapse material comparability into algebraic calibration**.

## MQR originality check

Chang ch.3 already argues the most important failure modes and the rational historical context; Ohnesorge 2022 covers alternative independent operations and error-source control; Shapin 1994 the sociability of credible experimental testimony; Moxham & Fyfe 2018 the publication/accuracy distinction. Therefore discovery of 'two-point extrapolation fragile' is elementary mathematics, **not new historiography or MQR novel framework**. Strong discriminating future question: Were the intermediate silver-gauge physical artifacts and clay-piece dwell histories sufficiently stable under procedures available in 1784 to allow a *limited but worthwhile* quantitative extrapolation despite knowing absolute temperatures were not confirmed? Need original notebook & 1784 plate comparisons, not model speculation.

## Sources

- Chang 2004 held Drive 1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV, pp.123–128, especially notes 33/34 on p.125.

- Chaldecott 1975, Josiah Wedgwood (1730–95)—Scientist, BJHS 8(1):1–16, DOI https://doi.org/10.1017/S0007087400013674 full publisher PDF https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D1F1C821024D2B6AC186DDCA224F561A/S0007087400013674a.pdf/josiah_wedgwood_173095_scientist.pdf, primary cited editor analysis pp.7–9.

- Royal Society 1784 MS L&P/8/79/1 28pp read May 13 https://catalogues.royalsociety.org/CalmView/Record.aspx?id=L%26P%2F8%2F79%2F1&src=CalmView.Catalog, three plates (manuscript), print DOI 10.1098/rstl.1784.0028 held Drive 1fwIwmTTB80vyjqHnW-o0lNXYRNaTy2oy.