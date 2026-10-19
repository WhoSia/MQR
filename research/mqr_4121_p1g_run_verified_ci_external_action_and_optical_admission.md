# MQR-4.121 P1G — Run-Anchored CI Authority and Optical Source Admission

**2026-10-19 · 4.121 ACTIVE · P1G BOUNDED SYNTHETIC / STATIC AUDIT PASS · PHYSICAL SOURCE HOLD · 4.122 UNPROMOTED**

## 1. Executed GitHub Actions evidence (not only workflow YAML)

Workflow: [mqr-4.121-p1f-audit-and-oob.yml](../.github/workflows/mqr-4.121-p1f-audit-and-oob.yml). GitHub API `actions/runs` and associated `jobs` and **decoded job logs** directly inspected.

| run ID | exact head SHA prefix | result | directly observed boundary |
|---|---|---|---|
| [39196590710](https://github.com/WhoSia/MQR/actions/runs/39196590710) | b5458ba | SUCCESS | initial optical fixture and permission gate |
| [39196779614](https://github.com/WhoSia/MQR/actions/runs/39196779614) | f87a11b | FAILURE | optical fixture passed; authority scanner fixture raised AssertionError; NOT physical-model failure |
| [39196812801](https://github.com/WhoSia/MQR/actions/runs/39196812801) | 2b3d51f | SUCCESS | corrected fixture and authority script |
| [39196835032](https://github.com/WhoSia/MQR/actions/runs/39196835032) | 0cc10c3 | SUCCESS | permission omission/workflow-run ratchets checked |
| [39199535448](https://github.com/WhoSia/MQR/actions/runs/39199535448) | ff8796e | SUCCESS | external Action/source-script inventory scanner |
| [39199844293](https://github.com/WhoSia/MQR/actions/runs/39199844293) | 8a103a9 | SUCCESS | P1G analytic bounded absorption interval test and 11 action-reference detail logging |
| [39200008987](https://github.com/WhoSia/MQR/actions/runs/39200008987) | 47809e6 | SUCCESS | verified checkout SHA pin; optical and authority regression remain passing |

These are seven successive runs found for this workflow, **six SUCCESS and one FAILURE**, within queried repository results as of 2026-10-19. These explicit runs are evidence only for the checked SHA, not proof of success for later README or notebook-only commits. `github-actions[bot]` may publish status/check metadata, but **the research commits and CI workflow are human WhoSia author+committer**.

## 2. External Actions and invoked scripts: bounded inventory, not full security proof

[Source-only inventory tool](../tools/mqr_workflow_transitive_inventory.py) was executed in run 39200008987 with `MQR_TRANSITIVE_AUDIT=PASS_SCOPED`. Current repo has **164 workflow YAML files**. **11 distinct external `uses:` references** because the formerly 10 reference types now include both the pinned new checkout and the remaining v4 checkouts. **163** workflows contain at least one Action without a full 40-character SHA, and **102** distinct explicit repo-root Python/shell command paths were collected with **zero unresolved** among those literal references.

| Reference | workflow count | review |
|---|---:|---|
| `actions/checkout@v4` | 163 | floating major tag, credential persistence defaults require `with: persist-credentials: false` per-use audit |
| `actions/checkout@11d5960a326750d5838078e36cf38b85af677262` | 1 | SHA retrieved from GitHub tag v4 on 2026-10-19, new P1F gate sets `persist-credentials: false` |
| `actions/upload-artifact@v4` | 97 | saves Actions artifact, not a Git source commit; artifact contents may still disclose data |
| `actions/setup-python@v5` | 53 | mutable major tag |
| `dtolnay/rust-toolchain@stable` | 40 | mutable stable ref, install dependencies/network |
| `leanprover/lean-action@38fbc41a8c28c4cbaec22d7f7de508ec2e7c0dd9` | 43 | SHA-pinned, its `action.yml` composite shell runner inspected; nested scripts and all dependencies not yet audited |
| `actions/setup-java@v4` | 7 | mutable major tag |
| `r-lib/actions/setup-r@v2` | 7 | mutable major tag |
| `leanprover/lean-action@v1` | 6 | mutable major tag, separate from pinned copy |
| `r-lib/actions/setup-r-dependencies@v2` | 6 | mutable major tag |
| `actions/download-artifact@v4` | 2 | artifact transfer, not Git source mutation by itself |

The older fixed-tree census (163 workflows, 54 `statuses: write`, 3 missing explicit root permissions, 1 `workflow_run`) remains valid for those unchanged workflows; the new P1F file declares only `contents: read`. No literal `contents: write` or direct YAML `git push` was observed. Representative `mqr-4.44-obligation-constitution-court.yml` explicitly publishes GitHub commit-status records using `GH_TOKEN: github.token` and `gh api POST /statuses/${GITHUB_SHA}`, which is **not read-only** and is **not** a code commit.

### Called-code depth reached
Directly read 16 invoked Python scripts in MQR-4.70/4.71/4.72 and the MQR-4.91 `workflow_run` receiver. Direct Python script writes observed: local result CSV/TSV/JSON generated inside job workspace for Actions artifacts. No direct Git push/commit or HTTP API status-writing instructions were observed in these selected scripts. That does **not** certify their imported dependencies, C++/Lean builds, downloaded tools or arbitrary `uses:` Actions. The pinned Lean action manifest was opened and found to run shell scripts such as `scripts/install_elan.sh`; transitive downloaded scripts were **not** inspected. `actions/checkout@v4` manifest explains default token persistence; this is a potential exposure surface even where the workflow grants no source write. **Status: SOURCE-BATCH SCOPED; total runtime dependency closure HOLD.**

### External pinned Lean Action dependency-depth correction (additional source audit)

The exact pinned `leanprover/lean-action@38fbc41a8c28c4cbaec22d7f7de508ec2e7c0dd9` repository **Git tree was inspected, truncated=false**. Its `action.yml` and **11 `scripts/*.sh` under that SHA** were opened as actual source. The action is a composite runner and the inspected shell files do not contain a literal `git push` or commit-status API call. However, its always-used `scripts/install_elan.sh` fetches `https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh` over HTTPS and pipes the retrieved script to `sh`. Consequently **pinning this Action commit does not pin the recursively downloaded install script**. The optional `scripts/run_nanoda.sh` also includes a remote `https://sh.rustup.rs` shell installer. The specifically inspected workflows 4.70/4.71/4.72 explicitly use `nanoda: false`, so do NOT falsely label the optional nanoda branch executed for them; the common elan installer remains in the action path. `dtolnay/rust-toolchain@stable` is also a floating top-level ref. The real fetched downstream bytes, all Lean toolchains and transitive dependencies were **not** independently hashed or executed in a separate trusted sandbox, and nothing about this source scan establishes successful or malicious source mutations. Review priority: immutable installers/toolchain locks, then branch/path-specific runtime verification before rights removal.

### Concrete next hardening candidate, not an automatic rewrite
4.70, 4.71 and 4.72 declare `statuses: write` but no direct `gh api` status call was seen in their YAML. Remove only after checking third-party actions/nested scripts and observing comparison CI runs; 4.44 legacy status-producing workflows still rely on that permission. Pin remaining floating Actions only with reviewed upstream SHAs and regression verification, not mass replacements.

## 3. Zong original's applicability conditions

Original archived source: [Zong et al. (2006), `Applied Optics` 45(6):1111–1119, DOI 10.1364/AO.45.001111](https://drive.google.com/file/d/1EQSG9IXVfB9MpZMRAvHxPou0hAqE2nFo/view). Text directly examined around eqs (1)–(10) and validation sections. As reported in the **authors' instrument**, CCD-array range 200–800 nm, pixel spacing about 0.6 nm, bandwidth FWHM around 3 nm, 15-bit readout, 80 laser line measurements spaced about 5 nm; Fig. 6 uses a filtered broadband source and Fig. 7 an additional 516-nm laser. Their broadband demonstration uses a filter to suppress out-of-range light before declaring `δ_spec≈0`. These specifications are source-specific, **not requirements every other instrument must match**.

Equation chain:
- Instrument laser-characterized spectral line-spread function → out-of-band-per-pixel spill `d_ij` → `D` with in-band response excluded (eqs 1–3). Interpolation of measured laser wavelengths requires independently assessed fit error.
- Physically measured intensity `y=(I+D)x+q+η` (eqs 4–5); `q` includes signals from incident light **outside the instrument's spectral range**. Zong's method cannot infer `q` from its matrix alone; incident filtering is discussed as a way of making it negligible.
- Only with `q≈0` do eqs 7–9 yield `x=(I+D)^{-1}y`; the correction is **before** absorbance's logarithm and sample/reference ratio.
- Numerical condition number and inversion residual address stability; they do not guarantee the physical forward model includes all significant source components.

**Do not transfer the author's 1024-pixel laser-calibrated correction matrix to the Cary 14H scanned methyl-red curves of Griffiths & Potts (1974).** Different optical/sampling architectures and independently undocumented raw detector signals invalidate direct replay.

### Minimal actual raw-data admission packet, bounded
1. Instrument serial/model, optical geometry, detector pixel/wavelength calibration and slit/LSF/FWHM for the **actual instrument and acquisition date**.
2. Raw **linear** source/blank, reference and sample detector counts **and dark/offset** for the same optical/integration/gain setting; exposure metadata, clipping/saturation flags, instrument nonlinearity and read-noise response.
3. Independent monochromatic laser SLSF scans across the instrument spectral response, per-column normalization and `D` construction, measured/interpolated wavelengths, calibration uncertainties and independent held-out optical validation.
4. Physical filter transmission and independently bounded out-of-range source flux **for sample and reference separately**, including how added filters alter in-range throughput; if bounds absent, `PHYSICAL_IDENTIFICATION_HOLD`.
5. Repeat blocks, blank and reference drift, matrix calibration age/stability and covariance; uncertainty propagation through intensity correction, transmittance ratio and logarithm; reject nonpositive corrected intensity and unresolved spectral-reference mismatch.
6. To infer **chemical species** rather than corrected photon flux: path length, pH, temperature, ionic strength, concentration, dilution/sample-history, optical intervention order and independent chemical-state measurement, ideally held-out sample batches.

NIST [SP 260-140, Travis et al. (2000)](https://drive.google.com/file/d/17bhfdoo_8i7etVEY0N2EsZoBKULIJHw8/view) provides **certification and instrument traceability for visible neutral-density filter NTRMs** (control charts, comparison and blind testing), not a unique chemical-species-count certificate.

## 4. Bounded *analytical* interval, independently checked in Actions

[Executable 2-channel interval fixture](../experiments/mqr-4.121/p1g_bounded_raw_signal_enclosure.py) implements fixed known `M`, bounded `0≤q_j≤Q_j`, `|η_j|≤E_j`, with `v=M^{-1}y` and signed columns of `M^{-1}` to obtain sharp componentwise intensity intervals for **a rectangular admissible perturbation box**. Then for separately bounded sample and reference corrected signals `s^-≤s≤s^+`, `r^-≤r≤r^+` with strict positivity, the absorbance interval is

`A_i ∈ [ -log10(s_i^+/r_i^-), -log10(s_i^-/r_i^+) ]`.

For its constructed sample/reference fixture, `A_1=[1.879822013,2.005042882]` around constructed truth 2.000, `A_2=[.203421446,.205169579]` around truth .20412. See **real Actions run [39199844293](https://github.com/WhoSia/MQR/actions/runs/39199844293)** and post-checkout-pin **[39200008987](https://github.com/WhoSia/MQR/actions/runs/39200008987)**, both SUCCESS, log `MQR_P1G_INTERVAL_FIXTURE=PASS_SYNTHETIC` and `MQR_P1G_REAL_SOURCE_ADMISSION=HOLD`.

This is conditional interval reasoning, not statistical coverage; `M` uncertainty is **not** covered by the P1G fixture, and `Q_j`/noise thresholds are stipulated, not physically measured. Logarithms require **positive bounds**. Chemical-state identifiability still requires independent spectroscopy/chemistry and held-out interventions.

## 5. Philosophical consequence and anti-overclaim

- **Kuhn:** in established normal science, corrections of a standard instrument can be genuine scientific puzzle solutions; a spectral anomaly alone does not announce crisis. Original excerpt: Kuhn *Second Thoughts on Paradigms* resistance defined as V/I versus independently measured on a Wheatstone bridge, giving distinct future intervention implications.
- **Lakatos:** modifying measurement nuisance parameters could be a progressive research-program repair when **independently fixed and predicts held-out observed effects**; post-hoc absorption of the same anomaly with free nuisance parameters may be degenerating. This is our comparative application, not a theorem of either philosopher.
- **MQR:** confidence in algebraic correction is distinct from measurement warrant; measurement warrant is distinct from a scientific claim about chemical ontology, and neither is a universal one-number demarcation judgment.

**What remains HOLD:** original Griffiths & Potts raw detector traces; calibrated actual SLSF `D`, independent out-of-range `q` estimates, experimentally measured noise/throughput; full external Action transitive source/credentials review and exhaustive third-party runtime security; actual methyl-red chemistry assays; 4.122 promotion.
