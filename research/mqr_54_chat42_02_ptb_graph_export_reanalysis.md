# MQR 42 · 기록 02 — PTB optical-JAWS published graph-export readout

**Original source:** [Kraus et al. (2025) Measurement Data for “Parallelization of the optical pulse-drive for AC Josephson voltage standards”](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view), [DOI 10.7795/720.20250210](https://doi.org/10.7795/720.20250210); official ZIP SHA-256 `cdc5cfe15c2d5f81e59515113b78a5eff5abdcffda624849a154cd3ca5836a8c`, byte verified. The archived README states **12 tables exported from Origin for publication figures** — these are processed graph values, **not the full ADC acquisition stream**. Sampling rate 500 kSa/s and 50,000 samples per spectrum are manufacturer/reporting parameters, not evidence that all underlying samples are in this archive.

## Exact bounded numerical inspection

The text members `fig3b.txt`, `fig3d.txt`, `fig3f.txt` have columns `t [ms], V [mV]`, 999 rows each, shared exported time grid 0.002–1.998 ms, 0.002 ms increments. Positive, negative and full sine RMS of **these published export windows** respectively: **59.9811301, 60.2753964, 85.0338225 mV**. Positive export includes a small nonzero baseline; `fig3d` negative has approximately -0.23 mV baseline; `fig3f` full sine has about -0.23263 mV mean. No claim of absolute voltage-standard uncertainty can follow from window RMS.

We tested algebraic closure `e(t) = V_positive(t) + V_negative(t) - V_full(t)` on common **published x coordinates**. **n=999**; mean **-0.2295063964 mV**, raw RMS **0.2295383517 mV**, residual population SD **0.0038300035 mV**. Training a single constant correction `offset = -0.2293283567 mV` on first 499 records produces second-half mean **-0.22968408 mV** and second-half RMS residual **0.0038220474 mV (3.822 µV)**. Second-half worst |residual−training offset| **0.01207164 mV (12.072 µV)**.

**Meaning:** the exported waveforms approximately satisfy a linear combination **up to a common fitted offset**. This is a computational diagnostic and candidate model, not proof that separate runs share a physically fixed offset or that the mean is a measured optical dark reference. This is why we use half-window holdout and preserve raw uncorrected closure alongside fitted correction.

The archive also has `fig6a+b.txt` with 2101 plotted time rows, from 0 to 2100 seconds. One of its converted time channels spans 0–35 min; its amplitudes are different columns and units than the optical 2 ms windows. Do **not** mix graph x axes into a long raw acquisition or infer an experimental drift mechanism from figure export alone. The two 1000 Hz fundamental FFT/voltage outputs in other tables are independent figure products, not independent instruments.

## Necessary prospective falsification

For actual common-preparation inference, obtain same-run raw ADC positive/negative/full channel IDs, independent dark/reference readings, time sync, software processing parameters and separate timestamps. A physically measured dark reference (not a fitted arithmetic offset), blinded held-out sessions, and branch-specific uncertainty propagation can then distinguish electronic offset, optical attenuation, synchronization mismatch, or graph reprocessing artifacts. In the current archive these are unavailable.

[Executable readout](../language/real/experiments/ptb_oa_graph_checks_v54.py) · [unit tests](../language/real/experiments/test_ptb_oa_graph_checks_v54.py). The exercise probes whether the **source-and-reference bridge** is identifiable, not simply whether three files share the same string key.
