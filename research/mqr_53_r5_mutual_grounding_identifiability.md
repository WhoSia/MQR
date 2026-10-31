# MQR-5.3 R5: Mutual grounding and identifiability

2026-10-31. Independent analysis of Chang (2004), *Inventing Temperature*, ch. 2–3, and Tal (2017), *Calibration: Modelling the Measurement Process*.

## Verified in Chang (not yet checked against the historical primary original)
- Table 2.4: at air-thermometer 350 C, mercury Choisy-le-Roi=360.50 C, ordinary glass=354.00 C, between-instrument gap=6.50 C.
- Table 2.5: air thermometers A−A′ temperatures = [0,.17,-.02,-.04,.22,.29] C, maximum absolute difference 0.29 C; MAE 0.12333 C; RMS 0.16503 C over six observations, without uncertainty estimates.
- Table 2.6: air vs sulfur dioxide [0,.46,1.21,1.57,1.73,2.09,2.95] C, systematically increasing differences.
- Table 3.1 historical Wedgwood conversions: 160 W=21877 F furnace; 130 W=17977 F cast iron; 32 W=5237 F gold; 28 W=4717 F silver. Not current physical temperature values.
- Table 3.2 compares clay, mercury, metal, ice, water, air, cooling pyrometry (pp.130–132). Multicolumn text extraction misaligns data; further visual source-page validation mandatory before quoting arbitrary pairwise cells.
- Chapter 3, pp.155–158, mutual grounding: historical convergence among imperfect methods without infallible single standard. Not a proof that every agreement is reliable.

## Counterexample I: common-mode bias (constructive, not Chang/Tal theorem)
Measurements y_i(x)=T(x)+b_i(x)+c(x)+epsilon_i(x) with known error laws. For any function h(x), define T'(x)=T(x)+h(x), c'(x)=c(x)-h(x). Then joint observational distributions remain unchanged. Pairwise differences cancel c but do not identify T. An independent physical anchor, quantitative restrictions on c, or interventions yielding an identifiable full-rank design are required to break this gauge freedom. Even many independent conditional-noise measurements do not cancel shared systematic bias.

## Counterexample II: overlap-only extensions
Let overlap D0=[0,1], extended D1=[0,2]. Two candidate scale laws f_1(x)=x, f_2(x)=x+k(max(x-1,0))^2 share all values on D0 and differ for x>1 whenever k!=0. Agreement within D0, however precise, cannot identify k. Tests outside overlap, model assumptions, or other independent physical links are necessary. This is an existence counterexample to sufficiency of overlap alone, not to Chang's broader dynamic strategy.

## Sufficient conditions in a restricted linear model
If y = H theta + epsilon and H is known, measurements identify theta iff H has full column rank (in the usual linear-Gaussian known-error law model). Connected pairwise difference comparisons identify only relative offsets because their incidence matrix has a constant-vector nullspace. One valid absolute anchor removes that gauge for a connected graph; if the anchor is biased, correctness does not follow. Predictive checks under intervention and model misspecification remain necessary. This is elementary linear identification, not new priority.

## Chang vs Tal
Chang focuses on historically progressive but fallible coherence, and the construction of standards for expanded empirical domains; Tal frames calibration as measurement-process modelling, prediction, testing and mutual coherence. Convergence can contribute empirical constraints if tests and error modes are informative. Neither supplies an automatic guarantee of absolute truth; shared bias, observational equivalence and extrapolation remain live objections.

## Provenance and status
Chang Drive file `1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV`, Tal `1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2`, transcript MQR 36 `15T62LwCSxzyioz8jIohE8FNHnfm2oi-B`. Notion master `40aef561cf928165977af8e05ffc1b4f`; Drive master `1rSArpBZ9GvYLkJrI5j3oEu6o-cdGobpi0xzmVj7SiH8`.

Missing original-source audits to verify Drive possession: Regnault (1847), Wedgwood (1784), De Luc (1772). Not yet proven absent. This is research documentation only, no Real Lang code updates. No github-actions[bot] authorship authorized.
