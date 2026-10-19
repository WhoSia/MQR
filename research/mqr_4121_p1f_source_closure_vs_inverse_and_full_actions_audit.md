# MQR-4.121 P1F — Numerically invertible, physically underidentified

2026-10-19. Research state: SOURCE-AND-SYNTHETIC-PASS_BOUNDED; no new physical experiment, no 4.122 promotion.

## A. Original optics sources and their own qualifications

**Zong, Brown, Johnson, Lykke & Ohno (2006)**, Applied Optics 45(6), 1111–1119, https://doi.org/10.1364/AO.45.001111. Owned original: https://drive.google.com/file/d/1EQSG9IXVfB9MpZMRAvHxPou0hAqE2nFo/view . Its Eq.1 builds a spectral stray-light distribution function from monochromatic LSF normalized by in-band intensity and zeroed inside the bandpass. Eq.2 assembles the interpolated response columns D; Eq.4/5 includes additive light from outside the instrument measurement wavelength range (eps_spec). Authors explicitly say **their matrix method cannot determine/correct that off-array term**. With this term negligible, Eq.7–9 gives Y_meas=(I+D)Y_IB and the signal-domain inverse Y_IB=(I+D)^(-1)Y_meas. Eq.10 offers a fixed-point iterative check. This is not an absorbance-domain inverse.

Author instrument and outcome: commercial CCD spectrograph 200–800nm, ~0.6nm pixel sampling, FWHM ~3nm, 15bit ADC, condition number about 1.07. Fig.6 is filtered-lamp broadband source validation; Fig.7 uses a 516nm held-out laser, plus LED applications. The authors report reductions of scattered-light errors to order 1e-5. **No verification of the figure pixel traces here, and no MQR physical replication**. Source-side bandpass filtering was used to restrict off-array light in their validation.

**Zong et al. 2007**, Proc. SPIE 6744 67441L, https://doi.org/10.1117/12.737315, owned https://drive.google.com/file/d/1EPiNdsM1d5HU8z3stXRc0BSWSlp_USIr/view . Spectral line spread and spatial point spread are distinct; off-array and off-field effects have distinct limits. Not to conflate with the separately owned CIE Beijing 2007 publication.

**Travis, Smith, Rasberry & Kramer (2000), NIST SP 260-140**, DOI https://doi.org/10.6028/NIST.SP.260-140, owned https://drive.google.com/file/d/17bhfdoo_8i7etVEY0N2EsZoBKULIJHw8/view .
- Section 2.4: Type A/B uncertainty and replicated, multiple-day observations with >=30 degrees of freedom per nominal absorbance level and certification wavelength.
- Section 4.2.2 / Table 7, visually crosschecked with original NIST PDF (PDF page index 29): certification wavelength nm -> maximum slit width nm: 440->2.2; 465->2.7; 546.1->6.5; 590->5.4; 635->6.0. Those constraints are for the historical visible **neutral density NTRM filter programme**, not universal UV–Vis limits.
- Section 4.2.4 run/intermediate and final record preservation differs from accepting valid rows in the certifier's measurement database. Exclusion of a row from a *valid-data database* does not establish that all evidence of an invalid attempt must disappear.
- Section 4.2.5 condition/protocol changes need review and some requalification. Sections 5.5–5.6 specify comparison tests, and allow blind tests. Filter absorbance certification ≠ certification of the chemical count in methyl-red solutions.

## B. Bounded mathematical result and actual local execution

For in-band intensity t, true spectral stray response D, external/off-array light q, signal noise eta and estimated response Dhat:

y = (I+D)t + q + eta.

The corrected vector using the estimated operator is t_hat=(I+Dhat)^(-1)y. Therefore exactly

t_hat - t = (I+Dhat)^(-1)[(D-Dhat)t + q + eta].

A small numerical condition number limits amplification of KNOWN disturbances; it does not establish that q or D mismatch is absent. If some nonnegative external-light vector q=(I+D)(t1-t2) is physically admissible, two distinct positive true spectra t1 and t2 can create the same y. Such an unrestricted-nuisance example establishes **model-conditional nonidentification**, not realizability of every arbitrary q in a given spectrograph or originality of the linear algebra.

Standalone executable P1F: https://github.com/WhoSia/MQR/blob/main/experiments/mqr-4.121/p1f_outside_range_identifiability_stress.py . Corresponding local NumPy 2.3.5 code executed 2026-10-19, 20,000 Gaussian trials, seed 4121. D=[[0,.015,.002],[.012,0,.008],[.002,.014,0]], t=[.01,.1,.5]. kappa_2(I+D)=1.0354767965. q=[.0008,.0004,.0002] creates first-channel A bias -0.0331735661 AU. Dhat=.8D creates first-channel A bias -0.0207651781 AU. Distinct t2=[.0095,.0995,.4995] and q2=(I+D)(t-t2), which is nonnegative, yield the exact same y. Absolute raw signal noise sigma=1e-5 gives empirical absorbance SD [0.000434796,0.0000431994,0.0000087371] AU for true A=[2,1,0.30103]. Analytic delta-method SD [0.000434424,0.0000434466,0.0000086878] AU agrees to within 7%. **All synthetic**. Repository code was committed; external GitHub CI not run in this turn.

## C. Primary philosophy counter-test

- Kuhn (1970), _Logic of Discovery or Psychology of Research?_, owned https://drive.google.com/file/d/1fB-omnpaQM8WNMqHygya0VtVSlJWJu5d : directly read section distinguishing scientists' normal puzzle-tests premised on existing theory from tests of theory itself.
- Lakatos (1970), _Falsification and Methodology of Scientific Research Programmes_, owned https://drive.google.com/file/d/1f_VM-77p_wFHs50ztNeQ7atInIAaZkNK : directly examined his theoretical and empirical progressive/degenerating problemshift distinctions and novel-fact requirement.
- Laudan (1983), _Demise of the Demarcation Problem_, owned https://drive.google.com/file/d/1ejCLztxLBTCkk5FUeTfi8tJq4NSyWrpa : direct text on insufficiency of general demarcation labels for warrant judgments.
- Chang (2004), _Inventing Temperature_, owned https://drive.google.com/file/d/14Gb6NUlrDzDy3ooOJVTFAavfd6xSb3bi : direct original TOC and body/context on historical fixed points and complementary science.
No claim of fully collated book editions.

**Proposed testable contrast**: when externally laser-characterized D predicts correction of a held-out optical control, that independently constrained repair supports a limited normal-scientific D1 achievement, not identity of chemical species; when chemistry-sensitive residuals survive optical control and independent state measurement, a D2 local theory extension gains evidential footing. A purported D4 Kuhnian revolution would require separate history of disciplinary evaluation changes. Nor does any local repair alone qualify as Lakatosian progressive confirmation: new independently checked predictions matter. Prevent MQR from imposing infinite calibration provenance burdens upon the normal accumulation of science.

## D. Complete 163-file workflow YAML source audit (separate from executing workflows)

Authenticated GitHub tree for main resolved SHA 64f76cf894ff9c4ba00bcb32285e649f3dec2bf4; tree was nontruncated (1590 paths). Exactly 163 .github/workflows/*.yml and *.yaml files were identified. All 163 were individually fetched and scanned in eleven disjoint sorted batches (0–10,10–20,20–36,36–52,52–68,68–84,84–100,100–116,116–132,132–148,148–163), no fetch failures. Literal YAML checks found:
- 0 files with a literal contents: write grant.
- 0 containing literal git push or git commit commands.
- **54 files request statuses: write**, therefore do NOT describe this CI surface as globally read-only.
- 3 without workflow-top-level permissions declaration: mqr-4.59-core.yml, mqr-4.59-repair.yml, mqr-4.73-defeat-capability.yml. Effective default permission is outside this file-level audit.
- 1 workflow_run listener, mqr-4.91-fold-target-interaction.yml, individually inspected: contents: read and actions: read specified.
- Several older workflow checkouts lack an explicit persist-credentials: false.
REST history query authored by github-actions[bot] returned 0 matching commits. Latest P1F authored and committed by WhoSia. These are **scoped facts**: third-party action behavior, all invoked scripts, repo-level token default, earlier revisions, other push syntaxes and externally granted credentials remain security HOLD. No workflow files were changed; Actions execution and success remain unclaimed.

**Next physical gate:** independent calibration source traces, bounded outside-wavelength light, dark/reference/raw signals, same physical sample with independently verified optical interventions, optical detector dynamic range and uncertain nuisance covariance, and independently evaluated chemical model candidates. P1F synthetic reproducibility is not a chemical-species claim or 4.122 promotion.

## Post-write Git tree reconciliation

The GitHub REST comparison 64f76cf894ff9c4ba00bcb32285e649f3dec2bf4...93075ee39a2356af9061160f3835e3dd1cb94d67 reported exactly three changed paths: README.md, experiments/mqr-4.121/p1f_outside_range_identifiability_stress.py, and this research note; **zero .github/workflows changes**. Thus the 163-file YAML source audit at the base Git tree also applies to the YAML file contents at that later README commit. This is not a transitive security validation nor an all-history authorship audit.
