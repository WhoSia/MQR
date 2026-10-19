# MQR-4.121 P1I — Source-Authenticated Boundaries, Continuous Matrix Perturbations and Immutable Bootstrap Audit

**2026-10-19. P1I: CODE+RUN VERIFIED (CONDITIONAL/SYNTHETIC); physical source inference HOLD. Distinct from planned MQR-4.122 P0.**

## A. Independent upstream elan release-byte verification actually executed

Prior local-container attempt to download the asset failed because DNS/network access was disabled; no unverifiable local verification is claimed. A new **separate GitHub Actions runner** was configured to fetch the official GitHub release asset, verify the binary SHA-256 using the runner's `sha256sum`, compare with the reviewed GitHub release metadata, stage it in `$RUNNER_TEMP`, and execute *only* `elan-init --version` with an empty/sanitized environment, separate temporary `HOME`, and an eight-second timeout.

- Official upstream tag: **elan v4.2.4**, asset `elan-x86_64-unknown-linux-gnu.tar.gz` (Linux x86-64).
- Independently downloaded artifact digest from GitHub Actions job log: **`42b94d4244e8353142c456ec0e4ca6528fd898a6c604d4059f494e706e431f63`**; matches official GitHub release metadata previously fetched through the authenticated GitHub connector.
- Staged entry: `elan-init`. Smoke output: **`elan-init 4.2.4 (227caca13 2026-08-25)`**. `MQR_P1I_INDEPENDENT_SHA256=PASS`, `MQR_P1I_ELAN_VERSION_SMOKE=PASS_TEMP_ONLY`.
- Actual [run #39206178996 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39206178996) at head `0c6d7bdd060a89d14ed0351de04651ddbc383883`; verified exact step completions AND decoded job log.
- [Read-only one-purpose workflow](../.github/workflows/mqr-4.121-p1i-elan-release-verify.yml) uses **`contents: read`, SHA-pinned checkout, `persist-credentials: false`**. [Fail-closed archive intake](../experiments/mqr-4.121/p1i_elan_archive_admission.py) verifies SHA-256 *before staging*, rejects traversal and nonregular archive members, does not install to global paths.
- Limits: `--version` is NOT an installation or Lean proof build; runner `env -i` + timeout are NOT kernel-enforced network isolation. The selected executable is not a malware assessment; SHA comparison is a byte-identity check against release metadata. `elan/master` bootstrap script and `releases/latest` selectors remain **unreplaced** in old Lean workflows; no Rust/Lean transitive toolchain hash/entire dependency closure certified. MQR `lean-toolchain` remains `leanprover/lean4:v4.34.0`; no production Lean/runtime tool changes were made.

## B. Physical-record acquisition: actual byte + declared-clock + calibration-expiration checks

[P1I raw file integrity and time-bound validator](../experiments/mqr-4.121/p1i_raw_byte_time_calibration_gate.py) extends the existing [P1H structural intake schema](../experiments/mqr-4.121/p1h_instrument_raw_intake.py). Provided a **caller-supplied local `file://` path within an explicit admission root**, the validator verifies:
- SHA-256 over original file bytes (not merely digest format); file must be nonempty and under the declared intake root, and neither symlinks nor parent traversal outside that root are admitted.
- ISO 8601 **timezone-aware** calibration acquisition start/valid-from/valid-until times and sample/reference/sample-dark/reference-dark capture times.
- Calibration window must contain all four capture times; configurable maximum sample/reference/dark span defaults to **120 seconds**; scanning instrument wavelength-channel timestamps must also fall inside both calibrated and matched observation windows.
- Instrument serial/config and raw counts/pH/T metadata still checked under parent structural contract.
- Synthetic fixture rejects changed hashes, expired calibration, out-of-block time, timezone-naive timestamps, invalid start/end ordering and invalid paths; tampered bytes after initially valid manifest are rejected.

CI [#39206021068 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39206021068), `MQR_P1I_RAW_BYTE_AND_TIME_GATES=PASS_SYNTHETIC`. **Crucial**: a syntactically valid and hash-matched file is **not authenticated instrument output**: a fabricated file/manifest can pass; a calibration 'independent' flag is self-declared; instrument clock accuracy, laboratory sign-off, embedded exposure metadata, NIST certificate validity and actual acquisition must be independently corroborated. 120 s is a conservative *example policy*, not a science-wide constant. `MQR_P1I_DEVICE_AUTHENTICITY=HOLD`.

## C. Continuous 3×3 calibration-matrix uncertainty: finite check upgraded to analytic norm enclosure

Original P1H proof-of-concept: (y = Mx+q+\eta) with two optical configurations and two chemical/pH states, 3 synthetic spectral channels. P1I first [tested all 512 corners](../experiments/mqr-4.121/p1i_matrix_uncertainty_rival_grid.py) of independent `±0.002` uncertainties for 9 matrix entries in each optical setting, with `±0.0015` per-channel combined intensity/OOB discrepancy. Corner tests are **not** an enclosure of every continuous possible `M`.

Now [P1I inverse-norm certificate](../experiments/mqr-4.121/p1i_matrix_continuous_norm_certificate.py) proves a **uniform, conservative bound** over all \(\Delta M\) obeying the predeclared \(\|\Delta M\|_\infty\le\varepsilon\). For a fixed center \(M_0\) with inverse \(V=M_0^{-1}\), nominally corrected \(\hat x=V(y-q_0)\), unknown intensity perturbation \(\|\Delta q+\eta\|_\infty\le\delta\), and \(\|V\|_\infty\varepsilon<1\),

\[
\|x-\hat x\|_\infty \le \frac{\|V\|_\infty}{1-\|V\|_\infty\varepsilon}\left(\varepsilon\|\hat x\|_\infty + \delta\right).
\]

This follows from \(x-\hat x=-V(\Delta M x+\Delta q+\eta)\) and \(\|x\|\le\|\hat x\|+\|x-\hat x\|\). Therefore the rectangular intensity enclosure followed by positive-intensity monotone \(-\log_{10}(S/R)\) bounds **every member of the stated continuous matrix box**, not merely its corners. For 3 rows of 3 entries each with \(|\Delta M_{ij}|\le .002\), take \(\varepsilon=.006\) in the infinity norm. This is a mathematical statement *conditional on measured upper bounds being valid*.

Conservative cross-optic intersection of chemical high-minus-low absorbance (Delta A) (constructed two chemical states, not measured methyl red):

| channel (toy) | finite 512-corner enclosure | **continuous analytic norm enclosure** |
|---|---:|---:|
| 450 nm | [+0.103714,+0.130237] | **[+0.102947,+0.130997]** |
| 550 nm | [−0.079623,−0.048639] | **[−0.080732,−0.047542]** |
| 650 nm | [+0.091582,+0.120537] | **[+0.090663,+0.121449]** |

All analytic intervals exclude zero **only for this synthetic scenario**, with exact center matrices independently stipulated and finite nuisance bound. The no-chemistry-change fixture's intervals all include zero. Unbounded pH-dependent `q` still makes chemistry-versus-optics nonidentifiable and raw chemical-species counts remain unestablished. Measured (arepsilon), (delta) and calibration time drift are **not available**.

Run: [#39206409270 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39206409270), head `3b541bd48c1e1a37325f4dec67625c255a94d92f`; decoded job log shows `MQR_P1I_CONTINUOUS_MATRIX_ENCLOSURE=PASS_SYNTHETIC_THEOREM_PREMISES`. Fixed tree/source permissions scanner also passed at this head.

## D. Epistemology: normal science and moving warrant boundaries

This result offers a stronger candidate for the next MQR main question. Stable numerical inverse (instrument calculation) differs from a *certified source-corrected interval*, which differs from identifying a chemical species, which differs from disciplinary reclassification. Independence of optical calibration is not a Boolean label; it must be demonstrated via source provenance, detector physics and held-out interventions. New evidence can tighten/loosen a **set of admissible explanations**, but neither a scalar 'progress score' nor a Kuhnian crisis follows automatically.

Competing explanations remain: D1 legitimate independent instrumental recalibration; D2 chemical-state model expansion; D3 revision of what counts as a stable observable; D4 historical disciplinary change. The Harvest E (empirical evidence), R (research criticism), I (institutional standing) and M (measurement coherence) axes are analyst classifications that can move independently.

**P1I completed as operational/code+source-bounded research; scientific authority only conditional.** Recommend **4.122 P0 OPEN** with formal title *Moving Boundaries of Scientific Warrant: Independent Calibration, Intervention-Relative Identifiability, Normal-Scientific Repair & Historical Borderlands*. No claim 4.121 physically CLOSED or 4.122 mathematical theory established.

## Current risks & next evidence
Verify actual instrument raw-file byte origins (not just hashes); calibrate and measure (arepsilon)/(delta), acquisition clocks, sample/reference drift; test held-out physical interventions; compare independent chemical-state assay; audit upstream Lean/Rust toolchains and security/runtime dependency closure; philosophical close read Kuhn/Lakatos/Laudan/Chang with strict primary-source scope. **No raw methyl-red detector data were acquired.**
