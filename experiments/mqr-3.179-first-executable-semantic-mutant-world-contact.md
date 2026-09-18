# MQR-3.179 — First Executable Semantic-Mutant World Contact

## Status
**ACTIVE / CONTRACT-FROZEN / PRIOR-ART-COLLAPSE / CHALLENGE-ROUTE-ACCESS DEGRADED / EXECUTION-PENDING / HISTORICAL-NOVELTY-HOLD**

This stage remains **MQR-3.179**. No R1/R2/substage numbering is authorized.

## 1. Frozen source identities
- Paper2Agent: `jmiao24/Paper2Agent@8c2d059165ef8cdcb70dbea76655b9c2b55b38e6`
- POP-TOOLS: `qlu-lab/POP-TOOLS@f1db4032b7ffe3d65cc03c314ee06da07ac9bd50`
- POP-TOOLS common-variant entry point: `POP-GWAS.py`
- Source boundary implementation: `utils.py::_read_z -> _merge_match_a1a2 -> AllelesOperations._invalid_snps/filter_snps`

## 2. Primary frozen challenge: q_ALLELE
The primary semantic mutant is no longer a generic “boundary test”. It is a source-backed scientific-admission boundary.

### Source contract
For the common-variant POP-GWAS path (`rare=False`), POP-TOOLS removes rows when allele fields fail the source's admitted A/T/G/C structure or cross-input allele-compatibility conditions before the scientific estimate is produced.

### Challenge function
`F_q = <D, ΔA, E, Def, S>`

- **D** — admissible biallelic GWAS row vs row outside the admitted allele alphabet/matching relation.
- **ΔA** — inject one otherwise-valid row into all three GWAS inputs, preserving its SNP identity across inputs, but set one allele token to `N`.
- **E** — canonical POP-TOOLS must remove the injected row before inference; the injected SNP must not appear in output and the relevant removal accounting must reflect the exclusion.
- **Def** — if a compiled paper-agent interface instead silently normalizes/coerces the invalid allele and returns an ordinary inferential result for the injected SNP, challenge-function transport fails.
- **S** — common-variant POP-GWAS only. No automatic claim about POP-RARE/burden paths.

### Paired fixture
Start from a known-valid POP-TOOLS quantitative-trait fixture. Copy one valid row into each of the three input files, assign a fresh SNP identifier, retain ordinary numeric fields, and alter one allele field to `N`.

The baseline/source oracle is therefore:
1. original fixture remains unchanged;
2. injected-invalid fixture executes;
3. injected SNP is excluded from canonical output.

## 3. Mutant semantics
The mutant must alter **only the compiled/interface-side handling of the frozen boundary**, not the original source oracle.

Allowed semantic mutation:
- before invoking the upstream scientific path, silently map the single frozen invalid allele token to an admitted allele or otherwise launder the row into the admitted domain;
- preserve tool signature, valid-input behavior, reference fixture outputs, and ordinary packaging/runtime behavior.

Forbidden:
- changing the source oracle after observing verifier behavior;
- moving to a different boundary if Paper2Agent catches q_ALLELE;
- adding post-outcome holdouts;
- mutating output files directly;
- substituting a different repository.

## 4. Frozen execution order
1. materialize baseline Paper2Agent MCP from the pinned POP-TOOLS source;
2. run native Paper2Agent verification;
3. preserve all baseline verifier reports and hashes;
4. inject the single q_ALLELE semantic mutant;
5. rerun the **same** native verifier without revealing mutant location;
6. run the independently frozen q_ALLELE challenge holdout;
7. record T0 / T1 / native P2A verification / CPC holdout;
8. do not repair before verdict;
9. run provenance lane separately;
10. stop.

## 5. Detection matrix
| Lane | Baseline | q_ALLELE mutant |
|---|---|---|
| T0 package/runtime | PASS required | PASS required |
| T1 reference fixture | PASS required | PASS required |
| Native Paper2Agent verifier | PASS required | empirical |
| Frozen q_ALLELE holdout | PASS required | FAIL required |

### Fatal interpretation
- If native Paper2Agent verification catches q_ALLELE, credit the rival and reduce CPC on this axis.
- CPC retains a software-level operational residue only if the mutant passes T0/T1 and native P2A verification but fails the presealed q_ALLELE holdout.
- Either outcome is **not** yet a philosophical novelty result.

## 6. Challenge-Reconstruction Frontier finding
The previously public `jmiao24/Paper2AgentBench` repository was indexed with an `eval/adversarial_repos/POP-TOOLS_i{1-4}` structure and published as the benchmark home for the Nature work, but the current GitHub API returns 404 for the repository.

This is recorded as:
**PUBLISHED ROUTE HISTORICALLY VISIBLE / CURRENT PRIMARY BENCHMARK ROUTE DEGRADED-OR-DEAD / PAPER+SUPPLEMENT SUBSTITUTE ROUTE LIVE.**

This accessibility fact is a CRF observation, not a substitute q_ALLELE verdict.

## 7. Prior-art collapse
The following components are explicitly removed from MQR novelty:

### Mutation-testing protocol itself
Shulepov (2026), *Mutation Testing for Reproducibility Safeguards in Machine Learning Research Software: An Empirical Study*, arXiv:2608.27100.
Frozen artifact DOI: **10.5281/zenodo.22126120**.
It prospectively freezes repository revisions, mutation candidates, and validation workflows before outcomes, then tests reproducibility-relevant mutations. This directly defeats novelty claims based on freeze→mutate→same-validator alone.

### Property-specific mutants
Bartocci et al. (2023), *Property-Based Mutation Testing*.
DOI: **10.1109/ICST57152.2023.00029**.
This defeats novelty claims based merely on selecting mutants because they can violate a specified requirement/property.

### Metamorphic testing
Lin, Simon & Niu, *Exploratory Metamorphic Testing for Scientific Software*.
DOI: **10.1109/MCSE.2018.2880577**.
This defeats generic novelty claims for changed-input relational oracles in scientific software.

### Executable provenance
Leo et al. (2024), *Recording provenance of workflow runs with RO-Crate*.
DOI: **10.1371/journal.pone.0309210**.
Workflow Run RO-Crate profile DOI: **10.5281/zenodo.12159311**.
SLSA v1.2 likewise supplies verifiable software provenance/attestation machinery.
Therefore `RECORDED PROVENANCE != AUTHENTICATED PROVENANCE` is not itself an MQR novelty claim.

## 8. Narrow surviving candidate
The surviving candidate is **epistemically typed challenge-function transport**, not mutation testing.

A compiled interface preserves q only when it preserves enough of
`F_q=<D,ΔA,E,Def,S>`
for the same adverse intervention to remain capable of changing the same scoped scientific authority judgment.

The strongest candidate difference from ordinary requirement-aware mutation testing is **Def**, the authority-defeat map:
- not merely whether a software property was violated;
- but whether the violated distinction changes what scientific inference is licensed, refused, localized, or reopened.

This candidate remains under prior-art attack.

## 9. Residual Challenge Basis — provisional reverse import
Research OS disagreement-preservation work suggests a useful compression:
define `B_q` as the minimal distinction set that must survive compilation so that q's defeat decision remains invariant within declared tolerance.

This is **PROVISIONAL / NOT NOVELTY-BEARING**.
It is useful only if it produces a smaller executable contract than full semantic equivalence while preserving the same defeat decision.

## 10. Evidence still missing
No q_ALLELE baseline/mutant Paper2Agent run has been executed in this stage.
No native verifier verdict is recorded.
No CPC survival claim is licensed.

## 11. Current judgment
**DO NOT INCREMENT THE MQR NUMBER.**
Continue inside MQR-3.179 until the frozen q_ALLELE execution yields a native-verifier verdict or the executable route is demonstrated unrecoverable under bounded reconstruction effort.

If the route remains unavailable, close 3.179 as an accessibility/world-contact failure rather than fabricating execution.
