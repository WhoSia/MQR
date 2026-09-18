# MQR-3.179 — First Executable Semantic-Mutant World Contact

## Status
**ACTIVE / CONTRACT-FROZEN / PRIOR-ART-COLLAPSE / EXECUTION-SURFACE-PARTIALLY-RECOVERED / EXECUTION-PENDING / HISTORICAL-NOVELTY-HOLD**

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

### Paired fixture — outcome-blind deterministic construction
Use the pinned POP-TOOLS `Head_BMD` common-variant triplet:
- `test/data/Head_BMD_y_lab.txt.gz`
- `test/data/Head_BMD_yhat_lab.txt.gz`
- `test/data/Head_BMD_yhat_unlab.txt.gz`

At execution time, before any verifier outcome is observed:
1. identify the lexicographically smallest SNP identifier present exactly once in each of the three files whose source alleles are ordinary A/T/G/C values and are source-compatible across the triplet;
2. save the three source rows and their original A1/A2 values in a fixture manifest;
3. duplicate those rows under fresh sentinel SNP id `MQR_QALLELE_001`;
4. preserve all file-specific numeric/statistical fields and set sentinel `A1=N` in all three copies;
5. leave the original rows untouched.

The source-oracle holdout is frozen as:
- ordinary fixture output is unchanged;
- the invalid-sentinel fixture executes under the pinned source;
- `MQR_QALLELE_001` is absent from canonical POP-GWAS output.

The interface-side mutant is equally frozen:
- never modify the pinned POP-TOOLS source;
- copy the three input files to temporary inputs;
- only for `MQR_QALLELE_001`, restore A1 from the pre-mutation fixture manifest;
- pass those temporary files to the same upstream POP-GWAS command.

Thus the mutant launders exactly one presealed scientific-admission boundary and does not invent an arbitrary replacement allele.

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

The reconstruction census is now finer:
- `jmiao24/Paper2AgentBench`: current primary URL/API route is dead (404), although historical indexes preserve the POP-TOOLS adversarial path names;
- `joed3/Paper2AgentBench`: an author-collaborator sibling benchmark repository is live, but inspected current/history trees preserve AlphaGenome materials rather than the missing POP-TOOLS artifact;
- `jmiao24/pop_gwas_agent@ca345e4d0921bdd8dd9ce089518c0b747fe737c2`: a live author-controlled repository explicitly titled **Paper2Agent: POP-TOOLS Demo**, exposing `run_pop_gwas` and `run_pop_rare`;
- the Nature no-tutorial ablation reports four callable tools, whereas this demo exposes two, so identity with the published ablation is **not licensed**.

CRF classification:
**EXACT PUBLISHED ABLATION ROUTE DEAD/UNRECOVERED / AUTHOR-CONTROLLED SIBLING EXECUTION SURFACE LIVE / CANONICAL SOURCE LIVE / CURRENT PAPER2AGENT VERIFIER SPEC LIVE.**

This accessibility recovery is a CRF result, not a q_ALLELE verdict.

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

## 10. Second prior-art kill — context-of-use credibility and assurance cases
A stronger rival family substantially reduces `Def` as an independent novelty candidate.

- **NASA-STD-7009B** explicitly ties model/simulation credibility to intended use, criticality, permissible uses, V&V status, uncertainty, robustness, and reporting of risks/caveats.
- **ASME V&V 40** and regulatory applications explicitly assess whether completed V&V evidence is sufficient for a declared context of use, with required credibility scaled by model influence and decision consequence.
- Parvinian et al. (2019), DOI **10.3389/fphys.2019.00220**, and Kuemmel et al. (2020), DOI **10.1002/psp4.12479**, make this evidence→credibility-for-use relation operational in biomedical/regulatory settings.
- Viceconti et al. (2021), DOI **10.1016/j.ymeth.2020.01.011**, likewise frames verification/validation/uncertainty evidence as licensing or failing to license a model for its context of use.
- Assurance-case traditions already organize a scoped top-level claim through explicit evidence and assumptions.

Therefore MQR may **not** claim novelty for a generic authority-defeat map or for the proposition that evidence/failures alter permissible scientific use.

### Revised residue
The candidate is now narrower:
**challenge-authority transport across epistemic compilation**.

Let source object `A` induce a scoped licensing relation `L_A(q,e,u)`, where evidence/challenge state `e` licenses use/claim `u` for target `q`. For compiler `K:A→I`, a challenge-preserving compilation requires a typed bridge `τ` such that, over a declared challenge basis `B_q`,

`L_A(q,e,u) = L_I(τ(q),τ(e),τ(u))`

within declared tolerance and scope.

The novelty candidate, if any, is **preservation of the credibility/licensing relation through compilation/interface transformation**, not the licensing relation itself.

### Next fatal rival
This residue must now be attacked against:
- assurance-case transformation/refinement;
- requirements traceability under model transformation;
- certified compilation;
- proof-carrying code;
- refinement/bisimulation preserving safety or proof obligations;
- semantics-preserving API/interface transformation.

If those literatures already preserve claim–evidence/use judgments under transformation in an equivalent form, CPC distinctness contracts again.

Harvest receipt:
`Literature Harvest LR-20260918-MQR-CPC — Context-of-Use Credibility, Assurance Cases, Permissible-Use Mapping & Challenge-Authority Transport`
Notion page: `3dfef561-cf92-817f-87b5-c69c32cfa339`.

## 11. Third prior-art kill — formal semantic preservation, witnesses, and diagnosability
The revised challenge-authority transport candidate also faces strong reduction.

- Full abstraction already preserves and reflects contextual equivalence.
- Robust property preservation in secure compilation already asks whether source-level trace/hyperproperties survive arbitrary adversarial target contexts.
- Counterexample-preserving reduction explicitly treats a counterexample set as the object to preserve under transformation.
- Verification-witness work treats independently checkable violation witnesses as first-class artifacts and can minimize them by fault-localization relevance.
- Abstraction-based diagnosability asks whether a projection retains the ability to detect and isolate faults.
- ACCESS/ATTEST-style assurance engineering tracks claims/evidence across evolving system artifacts and supports change-impact reassessment.

Therefore MQR may not claim novelty for:
1. preserving/reflection of hostile contextual distinctions;
2. preservation against arbitrary adversarial contexts;
3. preservation of counterexample sets;
4. minimal failure witnesses;
5. diagnosability/localization under abstraction;
6. claim-evidence traceability under system evolution.

### CRF-transport compositional residue
The candidate must now move from one property/counterexample/witness to a typed **portfolio of scientific challenge routes**.

For source artifact A and claim q:
`CRF_A(q)={r_j}`,
where each route records at least:
- trigger/intervention;
- witness/data/material;
- reconstruction path;
- semantic fidelity;
- common-mode ancestry / noncommonness;
- required competence/environment;
- reconstruction cost/time;
- localization power;
- authority role;
- substitute-route / replaceability structure.

For compiler `K:A→I`, a provisional route map is:
`τ_R:CRF_A(q)→CRF_I(K(q)) ∪ {JUSTIFIED-RETIREMENT, LICENSED-SUBSTITUTE}`.

A CPC/CRF transport claim requires:
1. every load-bearing source challenge receives an explicit target fate;
2. no challenge disappears through silent quotienting;
3. scoped defeat/licensing judgments commute over transported outcomes;
4. relevant noncommonness is not silently collapsed;
5. substitute routes are counted as substitutions, not identical preservation;
6. degradation in reconstruction cost/competence remains visible.

### Strong limitation
This is **not yet a novelty claim**. It may be only a composition of secure compilation, diagnosability, verification witnesses, assurance-case evolution, provenance/dependency analysis, and cost-aware reproducibility.

The distinctness question is now:
> Does joint CRF transport over scientific-authority roles yield a verdict or prediction that those mature frameworks, applied side-by-side, do not already yield?

### q_ALLELE scope correction
The frozen q_ALLELE experiment tests only a narrow CRF slice:
- adverse-trigger expressibility;
- source-backed semantic boundary;
- observable exclusion/failure;
- elementary localization.

It does not test noncommonness, substitute-route topology, long-term reconstruction cost, competence decay, or multi-route frontier preservation. Therefore even a q_ALLELE CPC win cannot promote the full CRF-transport thesis.

Harvest receipt:
`Literature Harvest LR-20260918-MQR-FMT — Full Abstraction, Robust Property Preservation, Counterexample/Witness Preservation, Diagnosability & CRF-Transport Reduction`
Notion page: `3dfef561-cf92-81de-aa23-c2c71efa492c`.

## 12. Evidence still missing
No q_ALLELE baseline/mutant Paper2Agent run has been executed in this stage.
No native verifier verdict is recorded.
No CPC survival claim is licensed.

## 12. Current judgment
**DO NOT INCREMENT THE MQR NUMBER.**
Continue inside MQR-3.179 until the frozen q_ALLELE execution yields a native-verifier verdict or the executable route is demonstrated unrecoverable under bounded reconstruction effort.

If the route remains unavailable, close 3.179 as an accessibility/world-contact failure rather than fabricating execution.


## 15. Execution-surface recovery and double-pin constitution
A real POP-TOOLS paper-agent implementation is now recoverable without pretending that it is the exact Nature ablation artifact.

### Live interface
`jmiao24/pop_gwas_agent@ca345e4d0921bdd8dd9ce089518c0b747fe737c2`
was created by Jiacheng Miao and describes itself as a **Paper2Agent: POP-TOOLS Demo**. Its MCP wrapper exposes:
- `run_pop_gwas`;
- `run_pop_rare`.

The wrapper is thin: it forwards user-supplied file paths to the upstream POP-TOOLS CLI through `subprocess.run`. It does not itself reinterpret A1/A2 content before the call. Static inspection therefore supports:
**BASELINE WRAPPER STRUCTURALLY PRESERVES q_ALLELE INPUT PASS-THROUGH.**
This is not yet a runtime verdict.

### Identity caveat
The demo README tells users to clone `jmiao24/POP-TOOLS` separately and does not pin a commit. That fork's current main is `34fe4ff45532577f810502b2b5aebc68679cf878`, while the canonical qlu-lab source used by this stage is pinned later at `f1db4032b7ffe3d65cc03c314ee06da07ac9bd50`.

Therefore the executable world-contact pair is constitutionally double-pinned:
1. interface: `jmiao24/pop_gwas_agent@ca345e4d0921bdd8dd9ce089518c0b747fe737c2`;
2. scientific source: `qlu-lab/POP-TOOLS@f1db4032b7ffe3d65cc03c314ee06da07ac9bd50`.

No unpinned clone is admissible evidence for MQR-3.179.

### Native-verifier clarification
The current Paper2Agent semantic verifier is not merely `verify_mcp_server.py`. Runtime acceptance checks package/tool execution, whereas the independent verifier agent is instructed to inspect direct upstream execution, changed inputs/defaults, invalid inputs, upstream failures, and source reuse.

Therefore the fatal comparison must use the same **current Paper2Agent verifier doctrine/agent procedure** on baseline and mutant. Passing only the standalone runtime helper cannot count as “native Paper2Agent verifier PASS.”

### Incidental source-defect localization
Static inspection also found that pinned `POP-GWAS.py` defines `--ovp/--sample-overlap` with `action="store_true", default=True`. Omitting the flag therefore does not create an effective false branch. The public wrapper's apparent `ovp=False` path can inherit this source behavior.

This is recorded only as a localization calibration:
**SOURCE-DEFECT INHERITANCE ≠ COMPILATION DISTORTION.**
It does not replace q_ALLELE and cannot be promoted as a new mutant after the preseal.

## 16. Current executable packet state
- source boundary contract: **FROZEN**
- deterministic fixture rule: **FROZEN**
- interface commit: **FROZEN**
- source commit: **FROZEN**
- baseline wrapper static pass-through audit: **PASS**
- exact Nature 4-tool artifact identity: **UNRESOLVED**
- baseline runtime: **NOT RUN**
- mutant runtime: **NOT RUN**
- current Paper2Agent semantic-verifier verdict: **OPEN**
- frozen CPC holdout verdict: **OPEN**

**EMPIRICAL PROMOTION REMAINS HOLD.**
