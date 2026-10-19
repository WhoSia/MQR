# MQR-4.121 P1H — Immutable-Bootstrap Candidate, Raw Optical Intake Contract, and Cross-Intervention Identifiability

**2026-10-19 · ACTIVE / P1H SOURCE_AND_SYNTHETIC_CI_PASS_BOUNDED / PHYSICAL_INPUT_HOLD / 4.122 UNPROMOTED**

This report must be read alongside [P1G run-verified optical-source admission](mqr_4121_p1g_run_verified_ci_external_action_and_optical_admission.md), the [MQR original history](mqr_4121_p1c_origin_grounded_discriminants_and_operational_audit.md), and the Global Harvest calibration-warrant fragment. It does **not** constitute laboratory validation, complete system reproducibility, or a new scientific law.

## 1. Pinability of external installation: three distinct levels

Directly fetched the `leanprover/lean-action` source at pinned Git SHA `38fbc41a8c28c4cbaec22d7f7de508ec2e7c0dd9`. Its `scripts/install_elan.sh` invokes `https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh`. GitHub refs show the `leanprover/elan` master head at observation as `9605b24b08cf68b78dce0014b6fa01be1f8e2cee`. A URL using this 40-character commit *can* freeze the bootstrap script source. But this script itself downloads `https://github.com/leanprover/elan/releases/latest/download/elan-${arch}.tar.gz`, so **script source pinning does not freeze installer binary bytes**.

GitHub releases/latest at inspection returned **elan v4.2.4**. The asset `elan-x86_64-unknown-linux-gnu.tar.gz` has GitHub-supplied digest **`sha256:42b94d4244e8353142c456ec0e4ca6528fd898a6c604d4059f494e706e431f63`**. The corresponding version-specific candidate is `https://github.com/leanprover/elan/releases/download/v4.2.4/elan-x86_64-unknown-linux-gnu.tar.gz`. This is an **official metadata assertion; no independent binary download or hash calculation was performed**. The MQR Lean `language/real/lean/lean-toolchain` currently specifies `leanprover/lean4:v4.34.0`. Freeze of that toolchain version is not proof that its installation provenance or Lake/Rust ancillary dependencies are identical.

Separately, `dtolnay/rust-toolchain@stable` is a mutable tag/branch-like upstream selector; source ref resolution at inspection gave `b725eda525362e7cf34af9a7243cac1e3f01a7ec`. This SHA could freeze the **Action** code, but not the dynamically installed Rust toolchain payload. `lean-action` optional nanoda runner may bootstrap from `sh.rustup.rs`; checked legacy 4.70–4.72 workflows specify `nanoda: false` so that specific optional branch was not activated by their manifest. Do not treat these candidate URLs as authenticated binaries until digest is independently checked.

Read-only candidate machine ledger: [P1H bootstrap pin candidates](mqr_4121_p1h_bootstrap_pin_candidates.json). Source metadata (refs+releases) and [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use) corroborate full-SHA pinning as meaningful for Actions themselves, **not transitive bootstrap closure**. **No historical Lean workflow modified**; migration would require Linux binary digest verification, independent build test and before/after CI runs. The 163 remaining workflows with floating Action references, status-write exceptions and undefined effective root token privileges are still active audit items.

## 2. Machine-readable raw-intensity acquisition contract

Executable structural validator: [`experiments/mqr-4.121/p1h_instrument_raw_intake.py`](../experiments/mqr-4.121/p1h_instrument_raw_intake.py). `--example` prints a complete explicitly labeled **synthetic** manifest, `--validate manifest.json` structurally checks an incoming record, and default invocation performs seven acceptance/rejection fixtures.

Required major groups:
- `schema_version=MQR-4.121-P1H/1`, `provenance.kind=synthetic|physical`; no promotion to reality based on typed label.
- Instrument serial/model, `array` vs `scanning` response architecture, strictly ordered wavelength channels, `raw_linear_detector_counts` units, and explicit linear/saturation ceiling.
- Independent monochromatic line-spread calibration per instrument and optical setup: nonnegative pilot response matrix with strict diagonal dominance, independently acquired status and evidence URI; **separate** per-channel sample OOB and reference OOB upper bounds and absolute noise bound. Positivity/convergence requirements are intentionally more restrictive than general invertibility: this is a conservative **pilot gate**, not a universal spectrometer theorem.
- Per-record sample and reference **raw counts and dark frames separately**, optical configuration and calibration ID, sample ID/history, block, randomized order index, temperature, pH, concentration and integration. For sequential scanning instruments: per-channel sample/reference acquisition timestamps (needed to assess source drift).
- Physical records require original raw data URI and 64-character SHA-256 representation. Importantly **the script currently checks shape, not external file bytes or authority**. `STRUCTURAL_PASS_PROVENANCE_UNVERIFIED` cannot be relabeled `PHYSICAL_VERIFIED` without independent file fetching, hash verification, instrument logs and calibration provenance.

This contract disallows substituting wavelength-averaged absorbance or a digitized historical figure for linear detector counts, and disallows silent acceptance when OOB bounds/calibration independence are unspecified. Required *second-stage* (currently not implemented) checks: actual acquisition UTC timestamps, dark/ref drift, exposure and gain differences, saturation margins, in-band filter throughput, laser/LSF interpolation holdouts, instrument-specific covariance, effective spectral bandpass, path length, independent chemical-state assay, and history conditioning. Reject claims of end-to-end reproducibility until those checks exist.

## 3. Independent calibration changes what is *conditionally* distinguishable

Self-testing synthetic cross-factor experiment: [`p1h_cross_intervention_rivals.py`](../experiments/mqr-4.121/p1h_cross_intervention_rivals.py). It uses **2 pH-conditioned sample states × 2 separately calibrated optical configurations × 3 wavelength channels**, with independent calibration matrices `M_wide,M_narrow`, preset sample and reference extra-light terms `q`, source/reference corrected before logarithm, and rectangular `±0.001` per-channel absolute-intensity perturbation bounds.

The chemical-shift *toy* transmittance templates are `T_low=(.72,.44,.60)` and `T_high=(.55,.51,.47)`, not methyl-red extinctions, not observed spectra. Resulting `ΔA=A_high−A_low` and the intersection of conservative optical-setting-specific Δ intervals:

| wavelength index (toy nm) | intended chemical ΔA | interval after the two optical settings |
|---|---:|---:|
| 450 | +0.116970 AU | [+0.114688,+0.119252] |
| 550 | −0.064117 AU | [−0.066849,−0.061386] |
| 650 | +0.106053 AU | [+0.103517,+0.108590] |

All three intervals exclude zero **conditional on the given independently fixed M and q, perturbed-intensity error bounds, and the physical interpretation of the two states**. The separate optical-only fixture has fixed chemical transmittance across pH and a zero difference inside every interval. Comparing only low-pH under `wide` against high-pH under `narrow` without calibration produces spurious toy differences `(-.000226,+.003637,+.000371)` AU despite unchanged chemistry.

Crucial stronger countermodel: with pH-dependent *unbounded and unmeasured* additive optical contributions, a fixed underlying transmittance can generate **exactly the same entire synthetic observation array** as the chemical-shift fixture. Therefore observational discrimination is achieved only relative to the *declared, independently evidenced bound on optical nuisance*, not globally or by declaring a 3-species chemical ontology. Output marker: `MQR_P1H_UNBOUNDED_PH_DEPENDENT_OOB=NONIDENTIFIABLE`.

There are important limits: the code assumes exact calibration matrices, fixed sample and reference illuminations, and rectangular deterministic bounds; it does not propagate uncertainty in laser-calibrated `M`, optical throughput correlation, interference/scattering or chemical mixing, nor calculate power or a familywise confidence statement. Its toy signal-based contrast need not represent the actual spectrometer's attainable configurations or real pH interventions.

## 4. GitHub actual execution, exact boundary

[GitHub Actions run #39202854699](https://github.com/WhoSia/MQR/actions/runs/39202854699) on commit `19918d2673cf20789bd016f5d6467614c45dd5c9`: read actual job and decoded log; **completed SUCCESS**. `MQR_P1H_INTAKE_SCHEMA=PASS_SYNTHETIC`, `MQR_P1H_RIVAL_CROSS_INTERVENTION=PASS_SYNTHETIC`, `MQR_P1H_DEPENDENCY_PIN_LEDGER=PASS_ADVISORY`, legacy P1F/P1G optical checks and source-only workflow authority scanner all PASS. **`MQR_P1H_EXTERNAL_FILE_AUTHENTICATION=HOLD`**, **`MQR_P1H_REAL_CHEMICAL_SPECIES_COUNT=HOLD`**. No new branch, no bot commit, no instrument measurements.

## 5. Philosophical result versus instrumentation premise

Normal science's legitimate local measurement repair (Kuhn) and an empirically progressive theory/problemshift (Lakatos) are not automatically identical. **External independent calibration is an inferential separator only if it constrains the same nuisance pathways that could imitate the scientific target claim**. A fixed matrix `M` by itself does not rule out pH-dependent `q`; a calibration that is fit using the very chemical anomaly under dispute is less independently constraining than a laser+filter/optical-control calibration with prespecified validation. This suggests a target-conditional scientific *frontier of warrant*, not a universal demarcation law, Kuhnian revolution, proof of unique species count or monotone MQR progress scalar.

**Promotions:** MQR-4.121 ACTIVE / P1H SOURCE_PLUS_SYNTHETIC_RUN_PASS_BOUNDED; instrument/raw-source and full bootstrap closure HOLD; 4.122 UNPROMOTED.
