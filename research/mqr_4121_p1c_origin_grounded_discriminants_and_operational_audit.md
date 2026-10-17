# MQR-4.121 P1C — Origin-grounded discriminants and operational audit (2026-10-18)

**STATUS:** Research design and historical reading PASS_BOUNDED; experimental identification HOLD; no original laboratory data acquired. **Branch:** main. No version promotion.

## 1. Historical source reading: direct archive receipts vs inferred lineage

The following archive files were accessed directly through the connected Research OS Drive. Text extraction returned a readable prefix/selection, **not a complete raw-byte reading**. Do not label the full 1–25 transcript corpus as exhaustively read.

- [MQR 1.md](https://drive.google.com/file/d/190Sh9592ogYTcaYEGtMNksdbqYzDhsTS/view): user's founding Aug 26 question asked whether UV–Vis instruments may be reduced to logic circuits and what it means to validate physical world claims from output data. The **same first conversation** already asks about translation loss, non-isomorphic survival, authority, dissent, institutional resource selection and cites Hasok Chang; these are **early themes, not late intrusions**.
- [MQR 2.md](https://drive.google.com/file/d/1_1YDFRJoutoEYPkKOm6HAuzZJ1AG_JTE/view): 1.10 organization and cross-level individuals; 1.11 global compatibility; 1.12 intervention composition; 1.13 admissibility; 1.14 reference through target transformation; 1.15 reversible output/irreversible genealogy; 1.16 state sufficiency and non-Markovian description. Subsequent versions branch into distributed mechanisms, medicine, institutions and strategic ontology.
- [MQR 3.md](https://drive.google.com/file/d/1q3uSc5IjykFeIIhTzfW9PWC8nBZtbAW_/view): independent-coder acquisition phases prompted **explicit user's objection** that a philosophical project had become occupied with coder procurement; a return-to-philosophy 1.89 was then proposed. This is primary evidence of repeated instrumental inversion.
- [MQR 4.md](https://drive.google.com/file/d/10iNWtFbFHL5VZhndqkhYze2083ETwWkn/view): physical-history example of hidden defeaters, real rival-probe rankings, Euclid prospectivity and genuine no-hindsight commitments; user objected to indefinitely proliferating governance courts, with 'return from the mountain only upon a genuine insight'.
- [MQR 22.md](https://drive.google.com/file/d/1C7eWowb25gtcM0PY7jJzJ0421KF9EjtY/view): user requested natural science, math philosophy, mathematical history, *strong rivals*, and permission to break MQR's own theoretical claims; UV–Vis was explicitly only a founding example, **not a restriction on domains**. Historical Kempe/Heawood and SNO cases remain valuable.
- [MQR 24.md](https://drive.google.com/file/d/1yQiC5QWjb71gUoSCHoqiowjWlWS6Ve02/view): FER full-cohort preprocessing, BayLum comparison, Real Language, transition into 4.113.
- [MQR 25.md](https://drive.google.com/file/d/1GeDsUi3duGHKVaUJ0NW_vrlBIozgdZt0/view): 4.113–4.114 Blackwell/calibration lineage and renewed Kant/reason/authority argument, rooted in measuring instruments and evidential graph; both must survive, without forcing a single reduction.

**Corrective interpretation:** The project did not progress linearly from physical science into unrelated philosophy, then 'return'. It had multiple coexisting explanatory branches since its foundation. Its recurring risk has been replacing original contested questions with procedural gates; the present physical priority is a chosen emphasis, not a denunciation of philosophical research.

## 2. Griffiths & Potts (1974) as a source-grounded discriminator

Canonical PDF: https://drive.google.com/file/d/1-gkuNeS5kqblkpG9Pt2S1MSvQbEAcDvX/view

Original experimental distinction:
- pH scans methyl red, automatically sampled at 1 nm (series A) and manually digitized at 5 nm (series B, smoothing), *not identical underlying samples or matched pH points*.
- Their 3-spectra affine internal-linearity test estimates beta on wavelengths passing a small denominator threshold; the final residual is evaluated across all wavelengths, including excluded beta points.
- Table I gives dilution-uncorrected vs corrected averaged beta-RMS .022 -> .018 and d-RMS .016 -> .011 absorbance units, but do not attribute every change to a specific mechanism without paired original scans.
- Extreme high-pH spectra leave the bulk-range affine family; three chemical species/pseudo-two-species is the authors' chemical **interpretation**, not uniquely identified structural fact. Re-read original figures and numerical tables before digitization claims.
- Temperature series (15.3–73.4 C) has a different intervention, and absorption spectra of endmembers need not remain invariant.

### Three physical hypotheses and discriminants

Let c be dilution-corrected effective concentration, \(\ell\) path length, \(\epsilon(\lambda)\) extinction coefficient, \(w(\lambda)\) bandpass and \(s\) stray-light fraction. Define clean monochromatic transmittance \(T_0(\lambda,c)=10^{-\ell\epsilon(\lambda)c}\).

**H1 chemical equilibrium:** \(T_0(\lambda)=10^{-\ell\sum_j\epsilon_j(\lambda)c_j(pH,T)}\), with non-proportional species profiles and independent equilibrium/spectroscopy checks. Prediction: pH-dependent *shape* persists after independently measured dilution, stray-light and bandpass corrections; a chemical-state proxy (orthogonal spectroscopy or calibrated equilibrium measurements) co-varies. Possible rival: pH changes scattering or instrument baseline.

**H2 optical stray light:** under simplified uniform additive light \(T_s=(T_0+s)/(1+s)\), \(A_s=-\log_{10}T_s\). At high intrinsic absorbance and fixed optical setup \(A_s\to\log_{10}((1+s)/s)\), a saturation tendency. Prediction: at matched chemistry, variations in verified stray-light suppression or attenuation reveal instrument-correlated curvature; independent low-stray-light instrument changes profile. CAUTION: real spectral stray-light has a matrix/kernel, not necessarily a uniform s.

**H3 finite spectral bandpass:** measured intensity \(T_b(c)=\int w(\lambda)10^{-\ell\epsilon(\lambda)c}d\lambda/\int w(\lambda)d\lambda\), \(A_b(c)=-\log_{10}T_b(c)\). For fixed w and c-independent epsilon, curvature satisfies \(A_b''(c)=-(\ln 10)\ell^2\mathrm{Var}_{w,c}(\epsilon)\le 0\). Nonzero variance within bandpass yields concavity even with one chemical species. Prediction: bandwidth dependence stronger where epsilon varies sharply over passband; at narrow bandwidth the artifact tends toward zero, given suitable signal-to-noise.

**Design:** independently calibrate pH and sample concentrations, control ionic strength, temperature, cell/pathlength and blank; collect randomized repeated measurements across pH × concentration × spectral slit width (at least two independently calibrated widths) × validated stray-light regimes, with a stable reference material whose chemistry is not altered by pH intervention. Preserve RAW detector intensities plus dark and reference channels before logarithms, spectra with wavelengths, equipment settings and scan histories. No procurement / instrument allocation assumed available.

**Decision logic:** H1 is favored *conditional on controls* when chemistry-sensitive shape and orthogonal species indicators survive optics variation; H2 when curvature shifts with validated stray-light perturbation; H3 when its bandwidth dependence tracks source-spectrum gradients as specified. Interactions are permitted; 'best rival' must not be forced to be unique. Predeclare model comparison, uncertainty and blocked/unidentifiable regimes rather than only a three-way winner.

## 3. State sufficiency: separate epistemic, physical and claim-relative senses

Let history h, representation z(h), future feasible intervention u and future observation law P(Y|h,u). A claim-relative predictive sufficient representation for a **specified feasible set U** obeys

\[z(h_1)=z(h_2)\Rightarrow P(Y\mid h_1,u)=P(Y\mid h_2,u)\quad\forall u\in U.\]

This is a **formal definition/reconstruction**, not a new theorem or a result established for methyl red. A pair of matched nominal (A,pH,T) endpoints reached by different permissible histories, followed by a fixed multiwavelength perturbation, can *falsify* this sufficiency if future laws differ after controls. Non-difference in finite tests supports only tested U/power. Sethna's return-point memory needs its model-specific dynamical assumptions and cannot certify chemical hysteresis generically.

## 4. Actions and authorship scoped audit

GitHub current README demands MAIN_ONLY, WhoSia author and committer, no actions bot commits, and read-only CI. Verified in previous turn five recent detailed commits have account author=committer=WhoSia.

This turn fetched original YAML for 12 workflows, including legacy 4.57/4.59, 4.80, 4.90, 4.95, 4.100, 4.101, 4.112, 4.114 and Real Language. All 12 explicitly had `permissions: contents: read`; no literal git commit/git push, create-pull-request, or contents: write was found in the **fetched files**. Three historical workflows (.github/workflows/mqr-4.57-lean.yml, mqr-4.59-real-language.yml, mqr-4.57-ecology-proof.yml) additionally have **`statuses: write`**. They are therefore *not globally read-only*, even though the source-content token permission is read-only and no source push was observed. Several do not set `persist-credentials: false` explicitly, despite read-only contents permission. External action and called script behavior, all other workflow files, repository-level defaults and full commit history **NOT FULLY AUDITED**. No automatic bot contribution violation has been shown, but absence is not proven globally.

**Suggested independent future audit:** walk the full workflow tree via authenticated GitHub API; evaluate the permissions at workflow AND job level, reusable workflow calls, pull_request_target, persisted checkout credentials, secrets, external unpinned actions, bot commits and cross-workflow write paths. Treat `statuses: write` as a documented policy exception to either justify or eliminate, not as proof of repository mutation.

## 5. Historiographic self-criticism and review gate

- MQR's early 'courts' and rapid sequential naming are historically real, but label generation is not automatic insight.
- The 1.87/1.89 coder episode and recent 4.120 P8 governance expansion are comparable pattern warnings, not reasons to dismiss institutional epistemology.
- Truth that 'a low-rank spectrum cannot certify a count of chemical species' is compatible with some specific chemical states being identifiable on physically admissible domains. Study both identifiability and nonidentifiability.
- Cite work from other disciplines generously: existing mathematical insight reused rigorously is a contribution when it answers the physical/epistemological question more sharply; do not manufacture novelty or its absence.
- Preserve original GitHub/Notion/Drive boundaries; research P1C is **PROPOSED / DESIGN-READY**, not laboratory PASS and not a promotion to 4.122.

**Next:** original figures with units plus uncertainty and independent negative controls; fully inspect NBS appendices and calibration editions; assess proposed physical protocol against feasible instruments; revisit MQR 5–21 in detail and source-specific counterexamples; finish complete Actions tree and contributors audit.


## 6. P1C synthetic numerical anchor and scoped minimum screening (2026-10-18)

For relative concentration c = 0.5, 1, 2, benchmark ideal absorption A=2c, simplified stray light s=0.01 with A_s=-log10[(10^(-2c)+.01)/1.01], and equal-bin finite bandwidth ε=(1.5,2.5) with A_b=-log10[(10^(-1.5c)+10^(-2.5c))/2].

| Relative c | Ideal A | Stray-light A | Finite-bandwidth A |
|---:|---:|---:|---:|
| 0.5 | 1.000000 | 0.962929 | 0.931699 |
| 1.0 | 2.000000 | 1.703291 | 1.759637 |
| 2.0 | 4.000000 | 2.000000 | 3.296709 |

These values are **constructed mathematics**, not Griffiths–Potts raw data. This construction models optical rival mechanisms only; chemical-equilibrium competition remains conceptually proposed, not quantified by this table. A first two-factor physical **screening** grid of 3 concentrations × 2 independently characterized slit widths × 2 independently validated stray-light regimes = **12 cells**, plus blanks, references, repetitions, random order and sample-history controls; it is *not a theorem of minimal sample count, not a power calculation and not a three-hypothesis identification guarantee*. Independent chemical-state evidence and pH/temperature interventions require additional conditions. Notion research ledger updated 2026-10-18 at https://app.notion.com/p/3fcef561cf9281389fecf57ead3bb348.

**Historical extension:** Directly inspected archival transcripts 6–21 at conversation-question/transition level after the initial P1C filing. Highlights: 4.42 rival-frontier limitations; 4.53 progress scalar skepticism; 4.66 state quotient; 4.69 ancestry nonfungibility; 4.70 intervention-family endogeneity; 4.90–4.100 detection/sampling observational selection. Not a claim of 16 transcripts read word-for-word, nor independent replication of historic science outcomes.
