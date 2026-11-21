# MQR 42 · 기록 03 — PTB 2025 figure-export graph alignment falsifiability

**Input source:** [PTB Original Optical JAWS 2025 ZIP](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view), DOI [10.7795/720.20250210](https://doi.org/10.7795/720.20250210); source ZIP SHA-256 `cdc5cfe15c2d5f81e59515113b78a5eff5abdcffda624849a154cd3ca5836a8c` matched official publisher value in MQR42-R02. Its `fig3b.txt`, `fig3d.txt`, and `fig3f.txt` are **processed plot export tables**, not synchronized digitizer session raw logs. Previous [MQR42-R02 closure analysis](mqr_54_chat42_02_offset_nonidentifiability_and_bridges.md) obtained same-grid 999 rows and `mean(A+B−C) ≈−0.2295063964mV`.

## New holdout sensitivity analysis

Define `e_lag(i)=A(i+lag)+B(i)−C(i)`, restricting all three exports to their common overlapping indices. Fit a constant offset **on the first half of the lagged residual**, and compute RMSE on the untouched second half; this is a *numeric perturbation of exported x indices*, **not a measured instrument time offset**. Original exported time increment is 0.002 ms per sample = **2 µs**.

| Artificial shift in A | Equivalent published-grid displacement | Second-half RMSE after first-half offset fit |
|---|---:|---:|
| −2 rows | −4 µs | 1.507669 mV |
| −1 row | −2 µs | 0.754280 mV |
| 0 | 0 µs | **0.003822 mV = 3.822 µV** |
| +1 row | +2 µs | 0.754040 mV |
| +2 rows | +4 µs | 1.507441 mV |

### Important counterexample: *small residual does not prove a clock*

A simple **linear signal** `A(i)=2i, B(i)=3i, C(i)=5i+0.7` has perfect closure after fitting an offset not only at lag=0 but at lag=±1: the shift adds a constant `±2`, which is *absorbed by the fitted offset*. Thus even the lag sensitivity of the actual PTB exported curve is **a property of that waveform's nonlinearity and processing**, not a general test of co-preparation or physical synchronization. This null counterexample is included in [6 new tests](../language/real/experiments/test_ptb_alignment_sensitivity_v54.py).

### What the experiment needs to resolve

Independent hardware timestamps/clock-phase records and per-channel optical or electrical blocked references measured **before** these three exports; pre-specify which sample corresponds to the same physical preparation and validate *on truly independent acquisitions*. A residual trend sensitive to lag suggests a model choice but does not prove one particular hardware alignment. The new arithmetic test has **no p value, interval, sensor transfer-function calibration, or causal attribution**; its role is to expose precisely how fragile the inference "same graph x coordinate ⇒ same measurement" could be.

[Executable code](../language/real/experiments/ptb_alignment_sensitivity_v54.py) · [6 passing synthetic tests](../language/real/experiments/test_ptb_alignment_sensitivity_v54.py) · [actual source](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view).
