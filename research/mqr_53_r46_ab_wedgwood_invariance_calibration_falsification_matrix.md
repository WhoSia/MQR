# MQR-5.3 R46-AB — An explicit falsification matrix for Wedgwood's 1782–1786 thermometer

Date 2026-11-05. Research question: *What independent observations would have supported or defeated the transfer of a clay-contraction readout from one manufacturing batch and heat regime to another?* This is a **model-based audit of historical testimony**, not a newly discovered mathematical theorem or a claim to have rerun 18th-century experiments.

## Primary-source status

- Wedgwood 1782, _Philosophical Transactions_ 72:305–326, DOI 10.1098/rstl.1782.0021: **full original scan in Drive**, `17bsv_UoQpzvCtG93tDWAezu52g3GLtZA` (text is only digitization cover, source-image collation incomplete); its 1782 claims known at present through Chang (2004) ch.3 and a contemporaneous 1783 *London Medical Journal* review.
- Wedgwood 1784, _An Attempt to Compare and Connect the Thermometer for Strong Fire ... with the Common Mercurial Ones_, _Philosophical Transactions_ 74:358–384, DOI 10.1098/rstl.1784.0028: **original not in Drive**. Royal Society manuscript L&P/8/79 has 28 manuscript pp + three plates. Note crucial original conversion claims analyzed by Chang.
- Wedgwood 1786, _Additional Observations on Making a Thermometer for Measuring the Higher Degrees of Heat_, DOI 10.1098/rstl.1786.0022: **original not in Drive**. Royal Society catalog of MS L&P/9/1 explicitly identifies 20 manuscript pp, plate. Public-domain 19th-century historic reprint excerpt mentions changed sample formation; this is historical publication-based corroboration, not claimed direct 1786 original page collation.
- Chang 2004 full text _Inventing Temperature_ ch.3 pp.118–155, Drive `1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV`: **directly reread relevant complete textual argument** including the author-described repeated clay contractions and the calibrated 1784 link.

## Distinguish three different empirical invariance claims

`I_1` (repeatability): fixed production recipe b, heating trajectory h and gauge calibration, repeated measurements of shrinkage r agree to claimed tolerance.

`I_2` (preparation transport): after holding an independently known temperature T and heating history h fixed, changing clay recipe or pressing/molding procedure b does **not** change the predicted scale readout beyond acceptable error.

`I_3` (scale extension): a conversion mapping g from contraction to a mercury/Fahrenheit temperature, estimated in a bounded overlap region, remains within tolerance when extrapolated into unknown higher-temperature ranges.

An I1 result does not entail I2 or I3. The 1786 manufacturing correction (per Chang and Royal Society archival descriptions) is evidence that at least naive universal I2 was unsafe; the 1784 conversion's later criticism is evidence the universal I3 was not established. These are distinct forms of error, not one numerical 'Wedgwood accuracy' scalar.

## Formal non-identifiability witness (analytical, wholly synthetic)

Represent the original gauge reading as
`r=f(T,h,b,a)+epsilon`,
where T is the intended high-temperature quantity, h heat-exposure duration/path, b clay composition and forming method, a atmosphere, epsilon observation error.

Suppose all calibration observations lie in an overlap domain `T<=T0`. Two responses
`f_A(T)=T`
and
`f_B(T)=T+c[max(T-T0,0)]^2` (c>0 with appropriate units)
are **identical in the observed overlap domain**, and differ above it. There is no observation in the overlap domain that can adjudicate their relative validity above T0, however many measurements are collected there. The quadratic is a *mathematical countermodel*, **not a factual model of the clay's chemistry**, and c must have inverse-temperature units if the readout is in equivalent temperature units.

Likewise two clay batches `b1,b2` may produce identical `f(T,h0,b1)=f(T,h0,b2)` at one heating duration h0 and diverge at h1; absent h variation, a one-duration cross-comparison does not validate duration independence. This is an inverse-problem and experimental-design observation already broadly within Chang/Tal's theory.

## Empirical discrimination requirements (historical feasibility not asserted)

1. **Replicate** nominally identical clay pieces after controlled shaping, over firing treatments with varied duration and equal independently characterized endpoints. Do not call the same oven dial 'independent temperature truth'.
2. **Bridge** overlapping metal-expansion/other temperatures using *independently calibrated* values and specific uncertainty, while acknowledging those instruments' nonlinear response and high-range limitations.
3. **Change the batch and kiln process** with fixed target standard, rather than transferring readings as though clay species uniquely determines shrinkage.
4. **Reserve a new high-temperature fixed point** or independent measurement for out-of-calibration validation. Agreement at the two calibration anchors alone is not a successful external prediction.
5. Audit the strongest existing Chang (2004), Tal (2019), and Ohnesorge (2022 original pending) methods: If their established recipes already require all five, the contribution is only source-specific research organization and **not MQR philosophical novelty**.

## An actor-time verdict matrix, not success-worship

| Actor time | Evidentially eligible material | Judgments defensible at that time | What to withhold |
|---|---|---|---|
| 1782 | Initial reported high-temperature clay experiments and known low-range mercury limits | Investigate a new instrument with provisional scale | No already-proven universal Fahrenheit conversion |
| 1784 | 1782 construction plus new silver bridge experiments | An explicit but model-dependent preliminary conversion `20*6.5=130 °F/°W` (via Chang) | Extrapolation correctness, independent absolute high-T standard |
| 1786 | Previous pair plus observed dependence on piece forming/mixing, further fixes | Revise manufacturing controls and point anchors | Project backward the later critique as something Wedgwood knew in 1782 |
| 1803 onwards | New rival platinum gauges and eventual calibration critique | Retrospectively revise the numerical conversion | Proof every earlier high-heat experimental *purpose* was irrational |

A historian reconstructing what Wedgwood knew on a given date should never use 1903 discoveries of heat-history dependence as if present in 1782.

## Provisional research verdict

What this improves is the **precision of the historical audit**: three papers, three different invariance questions, materially and temporally bounded evidence. These differences were already largely apparent to Chang, so MQR should **not** claim to surpass Chang on philosophical explanatory novelty. A real contribution would require original 1782/1784/1786 plate-and-table recovery and a **newly independent** contemporaneous cross-calibration result or a robust counterexample to Chang/Tal's best defended account.

Status: direct full 1782 scan present but image text unreadable; 1784 and 1786 missing from Drive; Regnault original present as unreadable image scan. No original high-temperature data replication; no fabricated error bars or real-world measurement predictions; **NOVELTY HOLD**.
