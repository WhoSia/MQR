# MQR-4.121 P1F — Full main-workflow authority inventory and physical-model identification boundary

**Audited UTC/KST period:** 2026-10-19. **Reference main tree:** `3f4423ac96d885068fade109776aded76ef1c7ff` (GitHub REST git/trees/main?recursive=1, truncated=false). **Static assessment, not runtime security certification.**

## 1. Workflow census, 163/163 read
All 163 blobs in `.github/workflows` under the fixed tree were enumerated and their source YAML checked in sorted batches (0–31 in preceding turn, 32–162 in current continuation). No fetch errors in those batches.

| Permission/action | Count | Meaning |
|---|---:|---|
| Workflow YAML count | **163** | Complete at fixed tree, not entire Git history |
| `statuses: write` | **54** | Commit status publication permission; **NOT globally read-only** |
| `contents: write` | **0** | No direct workflow declaration |
| Other named `*: write` permissions | **0 detected** | Based on line-oriented static inspection |
| `git commit` / `git push` directly written in YAML | **0 detected** | Nested scripts and external Actions not formally audited |
| Remaining YAML without detected write permission | **109** | Static-only privilege statement |

Observed status-writing cluster: MQR-4.44 to 4.72 legacy workflows (uneven coverage), plus `real-language-proof-ci.yml`. Representative example `mqr-4.44-obligation-constitution-court.yml` uses `GH_TOKEN: github.token` and `gh api --method POST repos/${GITHUB_REPOSITORY}/statuses/${GITHUB_SHA}`; the authenticated mutation writes GitHub **commit status**, not source. The workflow `real-language-proof-ci.yml` also requests this permission. **Three workflows** `mqr-4.70-probe-family.yml`, `mqr-4.71-contact-envelope.yml` and `mqr-4.72-intentional-contact.yml` request `statuses: write` with no direct status-posting command found in their YAML; remove only after checking whether third-party Actions or called scripts require it, not on this static observation alone.

### Distinctions and residual risk
A normal `github-actions[bot]` **status/check actor** must not be mistaken for a bot **author/committer**. Workflow YAML with `contents: read` and `statuses: write` can change repository metadata without changing files. A broad claim 'fully read-only workflows' is false. Conversely `statuses: write` is not evidence that the bot committed code. Direct YAML scan is limited by external `uses:` Actions, code invoked through local Python/Rust/bash, shell expansion, cached credentials, and REST API auth/rulesets. It does **not** replace inspection of jobs at runtime, all contributors and commit histories, or trigger/secret policies.

### Reproducible local helper
[Pure-standard-library static inventory scanner](../tools/mqr_workflow_authority_inventory.py), run `python tools/mqr_workflow_authority_inventory.py .` on checked-out repo. Includes fixture self-tests for `contents: write`, `statuses: write`, direct `git push`, comment filtering and status-post detection. Local fixture test `MQR_WORKFLOW_AUDIT_FIXTURE=PASS`; its scanner result has **not** been claimed as a separate GitHub CI run. No new workflow, branch or bot commit was created for this audit.

## 2. A well-conditioned optical correction may fail to identify a physical in-band spectrum

Source: [Zong et al. (2006), Applied Optics 45(6) 1111–1119, DOI 10.1364/AO.45.001111](https://drive.google.com/file/d/1EQSG9IXVfB9MpZMRAvHxPou0hAqE2nFo/view). The authors' original Eqs (4)–(5) include stray contributions `δ_spec` originating *outside the spectral range*; the text directly after Eq (5) says their method cannot quantify/correct that part and discusses filtering incoming radiation. Only **assuming δ_spec=0** do Eqs (7)–(9) yield the in-band recovery `Ymeas = (I + D) YIB`, `YIB=(I+D)^(-1)Ymeas`. Authors' empirically validated CCD performance is their result, not independently replicated in MQR.

Our exact conceptual extension: if the measured vector obeys `y=Mx+δ`, `M` is nonsingular but `δ` unknown, then `x=M^{-1}(y-δ)` spans a *set*, not an identified point, for allowable δ. Near-unit condition number of M does **not** cure this failure of the forward model's uniqueness.

**Synthetic executed test**, [self-checking standard-library Python](../experiments/mqr-4.121/p1f_oob_identifiability.py): `M=((.98,.02),(.01,.99))`, true `x=(.01,.5)`, `δ=(.003,0)`, observed `y=(.0228,.4951)`. If δ is falsely set to zero, invertible M gives alternative positive `x'=(.0130618557,.4999690722)`: both worlds produce exactly the same y. First-channel absorbance `-log10 x1`: actual constructed 2.000000 vs zero-δ reconstruction 1.883995; signed bias -0.116005 AU. `cond_∞(M)=1.041237`: stable inversion, wrong physical recovery.

With calibration weights `a∈{.018,.020,.022}`, `b∈{.009,.010,.011}`, OOB components `δ1∈{0,.0015,.003}`, `δ2∈{0,.00025}`, and signed channel noise `±.0001`, **216 grid cases** give a first-channel absorbance range `[1.848598967,2.051488928]`. This is a discrete scenario **grid**, not a continuous sharp bound, confidence interval, statistical power result, measurement observation, or traceable instrument performance.

### Additional feasible discriminant
Use an independent *out-of-range* suppression/filter intervention with independently characterized filter throughput and unchanged chemical preparation, check matched raw intensities and reference scans, and use independent source characterization to constrain δ. If the filter changes both δ and in-band transfer function, do not attribute the signal change solely to δ. Preserve detector dynamic-range and wavelength response constraints.

## 3. NIST certification is type- and procedure-specific, not truth of chemical ontology

[Travis et al., NIST SP 260-140 (2000)](https://drive.google.com/file/d/17bhfdoo_8i7etVEY0N2EsZoBKULIJHw8/view), abstract and contents; section 4 certification/protocol, section 5 traceability, section 5.4 control charts, 5.5 annual transmittance-scale comparisons, 5.6 blind testing, 5.7 data+metadata reporting. The spectrophotometric NTRM certification process provides instrument/absorbance scale assurance at declared conditions, not identification of a methyl-red chemical species count. Its instrument parameters are protocol-specific; do not transplant the NIST table's photometric uncertainty or stray-light ratio as measured noise of our toy data.

## 4. Kuhn/Lakatos contact, strongest competing philosophical readings

[Kuhn *Second Thoughts on Paradigms* (1974 reprint)](https://drive.google.com/file/d/1-jK0eaCXH_RvXRvFgrUCXMO_Yh8GLyiy/view) gives a striking explicit **Ohm's law** counterexample: defining resistance as V/I versus independently measuring it with a Wheatstone bridge can make the same law tautological or empirically informative; higher-voltage intervention disambiguates the practices. This is direct owned text and a closer historical predecessor to MQR's 'same representation, different future intervention' problem. The 1977 *Essential Tension* image scan still needs independent page collation.

[Lakatos (1970) original](https://drive.google.com/file/d/1f_VM-77p_wFHs50ztNeQ7atInIAaZkNK/view), section 2(c), defines theory-series appraisal through progressive/degenerating problemshifts and corroborated novel empirical content. Our **interpretation**, not an author claim: an independently premeasured spectral stray-light matrix which predicts held-out spectral corrections is a stronger *progressive* repair candidate than tuning residual coefficients on the tested methyl-red spectrum. The mere persistence of a spectral anomaly alone is insufficient for a blanket Kuhnian revolution verdict. Historic E/R/I/M Harvest axes remain analyst axes, not authoritative Kuhnian categories.

### Status
**MQR-4.121 ACTIVE**, P1F physical-identification bound `PASS_BOUNDED_SYNTHETIC`, source and workflow static authority `PASS_SCOPED`; original methyl-red scan/raw intensity, physical instrument calibration, fully inspected third-party actions/scripts, Kuhn full image collation, independent human evaluation and **4.122 promotion HOLD**.
