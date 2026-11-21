# MQR 42 · 기록 02 — Additive offset non-identifiability under apparent optical superposition

**Empirical provocation:** [PTB 2025 processed figure exports](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view), fig3b/d/f with 999 shared time coordinates, give `mean(A+B−C) = −0.2295063964 mV`. Training an offset on only first half lowers holdout residual RMS to `3.822 μV`, but **this does not identify which experimental component creates the offset**.

## Minimal structural model

Let latent optical/electrical signals be `s_plus(t),s_minus(t)`, and let each separately acquired channel have an unknown offset `d_p,d_n,d_f`. Observed published channels satisfy:
`A(t)=s_plus(t)+d_p`,
`B(t)=s_minus(t)+d_n`,
`C(t)=s_plus(t)+s_minus(t)+d_f`.
Then `e(t)=A(t)+B(t)-C(t)=d_p+d_n-d_f`, assuming exact waveform superposition and aligned samples. **A constant residual cannot identify any of `d_p,d_n,d_f`**: for every `u,v`, replacing `d_p'=d_p+u`, `d_n'=d_n+v`, `d_f'=d_f+u+v` leaves `e(t)` unchanged. Moreover, with unknown differences in source timing, optical path or export interpolation, the closure equation need not hold physically at all.

The *one-degree fitted residual* is not an independent measured calibration. Lower observed residual after arithmetic fitting makes the formal model plausible **conditionally**, but if the publisher graph exports were already processed to share common axes or reconstruction algorithms, numerical cancellation can be partly a processing identity. Even perfect zero residual is insufficient to identify co-prepared states across two scientific practices.

### Distinguishing experiment
Run blocked/bright reference measurement for each channel, record which physical state is shared and a pre-specified timestamp/joint-pulse mapping, measure the offsets independently, and predict full-wave holdout without refitting any offset. A genuine bridge would **restrict an uncertainty interval** that excludes alternative offset mappings. Without these independent observations the correct confidence state is **STRUCTURAL NONIDENTIFIABILITY**, not 'cancellation measured'.

This is a small identifiability lemma, **not a new universal scientific law**: the novelty for MQR is the transfer of explicit *bridge requirement* into cross-scientific measurement language. It answers a direction-setting question more strongly than bibliographic collation of original physical editions.
