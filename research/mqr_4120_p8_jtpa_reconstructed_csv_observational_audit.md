# MQR-4.120 P8 — JTPA Reconstructed CSV Observational Audit

2026-10-17. SOURCE TEXT READ / DESCRIPTIVE COMPUTATION PASS_BOUNDED / RAW CHECKSUM HOLD / CAUSAL IDENTIFICATION HOLD.

## Source and extraction
Zenodo dataset DOI 10.5281/zenodo.18836198, public record: https://zenodo.org/records/18836198 ; CSV URL https://zenodo.org/records/18836198/files/jtpa.csv?download=1 .
Zenodo describes 9,224 × 11 and displays MD5 1be2247cff05b2e6791ee330462bc181. The public CSV text was retrieved in full via a third-party page extraction service (265,170 characters) and parsed in memory; 9,224 CSV lines inclusive of header, **9,223 observations**, 11 columns, and zero empty/malformed cells by the performed simple parse. Thus apparent metadata row count may include header, but metadata convention has not been verified. Direct source file bytes and MD5 have **not** been authenticated; extraction text may not byte-match the published CSV. No original raw file is claimed archived.

## Exact descriptive results on extracted text
- Z2=0: n=3,090; D2=1: 43; training uptake 0.013915857605; earnings mean USD 15,310.5200647; sample variance 268,708,174.7035.
- Z2=1: n=6,133; D2=1: 4,015; training uptake 0.654655144301; earnings mean USD 16,487.4927442; sample variance 302,433,187.8058.
- Z×D cells: (0,0)=3,047; (0,1)=43; (1,0)=2,118; (1,1)=4,015.
- Unadjusted mean earnings difference, assigned minus unassigned = **USD 1,176.9726794**.
- Simple independent-unit Welch SE = **USD 369.1517483**; normal 95% interval **USD [453.4353,1,900.5101]**. This does not adjust for clusters, stratification, weights or data transformations.
- Uptake-rate first-stage difference = **0.6407392867** (64.0739 percentage points).
- Raw ratio ITT/first stage = **1,836.8979457 USD**. This is only an arithmetic Wald ratio, **not a certified LATE**.

## Reproducibility envelope and known limitations
These values were recomputed by programmatically parsing the entire retrieved CSV text and calculating group sample means/variances; the execution was not the original study's code. A direct byte-level SHA/MD5 verification and saved untouched CSV are still unavailable. The public resource describes a **reconstructed** analytic dataset from JTPA and auxiliary high-school-density sources; it is not certified as unmodified original JTPA data. The Zenodo description's DAG includes the malformed self-loop D2 <-> D2; its stated 'Known Graph' must not be treated as independently established causal identification.

Assignment Z2 is described as randomized by the public data dictionary, but randomization unit, balance checks, attrition, analytic weights, clustering, transformations and eligibility exclusions have not been independently audited. Means are descriptive conditional on Z2. The 95% interval assumes independent units and a normal approximation; it is **not** a design-correct inference certificate. The Wald ratio cannot be interpreted causally without justified exclusion, monotonicity, relevance, independence, well-defined treatment and appropriate population specification.

## Scientific scope veto
Real JTPA training assignment Z, actual receipt D and post-program earnings Y are a useful real-world example of incomplete compliance, but are not institutional complaint adjudication or scientific remedy. They do not validate J2 authority, an appeal system or consequences of scientific corrections. The historical MQR 4.89 Bernoulli nonidentification, 4.101 fallible standards, 4.107 acquisition history, 4.111 state-changing measurements, 4.113–4.114 source and instrument genealogy all remain applicable.

## Further adjudication
1. Acquire literal public bytes; verify MD5 and row count and preserve DOI/version/license with a first-party receipt.
2. Read Han 2024 and Abadie–Angrist–Imbens 2002 original methods; identify transformations, sample-selection denominators, experimental design, standard-error treatment and outcome definition.
3. Check baseline balance using pre-program variables, but never infer randomized validity from a balance test alone.
4. Attempt design-aware ITT only after the above, and a LATE interpretation only with documented IV assumptions.
5. Independently locate real appellate-remedy interventions for any transport to the full 4.120 question.

## Retained holds
CCQM physical calibration, Greenberg seven ambiguous observations, 4.118 Harvest primary-source custody, 4.119 R0/R+/E human assessments. 4.120 remains ACTIVE / P8 rather than promoting to P9 from a raw descriptive comparison.
