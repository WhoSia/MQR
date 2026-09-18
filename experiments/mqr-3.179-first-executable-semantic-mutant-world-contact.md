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


## 17. Prospective rival prediction — frozen before runtime
Source-level inspection of current Paper2Agent verification doctrine materially changes the expected result.

The current independent verifier is explicitly required to:
- trace every exposed tool to pinned upstream scientific code;
- establish expected behavior by direct upstream execution on the same inputs;
- add meaningful changed inputs and relevant missing/invalid inputs;
- preserve upstream assumptions, defaults, units, and error meaning;
- reject silent repair of scientific inputs;
- inspect wrapper code for altered defaults, ignored parameters, unjustified restrictions, duplicated scientific logic, and other deviations;
- record source-call review, changed-input/error checks, commands/exits, repairs, exclusions, limitations, and production hashes.

Therefore the prospective prediction is now:

**P2A-STRONG-RIVAL PREDICTION:** a faithfully executed current Paper2Agent independent verifier *should* detect the frozen q_ALLELE laundering mutant, because the mutant silently repairs a source-invalid scientific input and diverges from direct upstream behavior on an invalid-input challenge.

This prediction is frozen before any runtime outcome.

### Interpretation discipline
- If Paper2Agent catches q_ALLELE: this is a substantive rival victory, not a null result. CPC loses this single-route distinctness claim.
- If Paper2Agent misses q_ALLELE despite the doctrine above: the result is stronger than merely showing weak reference testing, because the framework expressly claims changed/invalid-input and source-fidelity verification.
- If only `verify_mcp_server.py` passes: no verdict. Runtime acceptance alone is not the strong rival.
- If the verifier repairs the mutant before final acceptance: count as **DETECTED**, because bounded repair is part of the native verification procedure.
- If the verifier excludes/defer the affected tool: count as **DETECTED/REFUSED**, not PASS.
- If execution is blocked by environment/dependency failure: **NO EMPIRICAL VERDICT**.

## 18. MQR-4.0 promotion constitution — presealed
MQR-3.179 may promote directly to **MQR-4.0** only if all four gates below are satisfied. No numerical 3.180–3.999 ladder is required if a genuine generational constitution is earned.

### G4-A — Empirical differential
At least one prospectively frozen challenge must yield:
- ordinary/reference/runtime acceptance PASS;
- mature rival verification PASS or materially insufficient localization;
- MQR challenge-route holdout FAIL;
- with source identity, mutant identity, and verdict path frozen before outcome.

A q_ALLELE miss can satisfy G4-A, but never the whole promotion.

### G4-B — Non-isomorphic route replication
The differential must recur on at least one second challenge route whose failure geometry is not merely another input-validity check.

Acceptable second-route families include, if presealed before observation:
- provenance/common-mode collapse;
- substitute-route loss;
- reconstruction-cost/competence degradation;
- failure/abstention semantic erasure;
- authority-bearing composition that changes route independence.

The two routes must require distinct challenge coordinates in the CRF representation.

### G4-C — Side-by-side reduction defeat
For each promoted differential, explicitly instantiate the strongest relevant existing frameworks:
- robust/full-abstraction or property-preservation machinery;
- counterexample/witness preservation;
- diagnosability/fault localization;
- assurance-case/context-of-use credibility;
- provenance/reproducibility/change-impact analysis.

Promotion requires at least one matched pair where those frameworks, applied with their ordinary native state, do **not** recover the MQR verdict unless they are augmented with the CRF-specific route portfolio variables being claimed as new.

If ordinary composition of existing frameworks yields the same verdict without extra MQR machinery, remain Generation III.

### G4-D — Constitutional compression
The proposed Generation IV object must compress a substantial fraction of the 3.x machinery rather than merely add another audit.

Minimum requirement:
one compact state object and update rule must jointly recover, as special cases:
- live defeat geometry;
- challenge lineage / successor burden;
- common-mode genealogy;
- translation burden;
- certification/reuse debt where relevant;
- substitute-route topology;
- reopenability / reconstruction frontier;
- typed failure localization;
- refusal/HOLD semantics.

The object must generate at least one new prospective prediction not explicitly baked into its construction.

### Promotion verdicts
- **ALL G4-A/B/C/D PASS → MQR-4.0 AUTHORIZED.**
- **G4-A PASS, B/C/D OPEN → remain MQR-3.179.**
- **G4-A FAIL because Paper2Agent catches q_ALLELE → remain MQR-3.179 and reduce CPC.**
- **Execution unavailable → remain MQR-3.179 / EMPIRICAL HOLD.**
- **Existing frameworks fully recover all tested verdicts → close the CPC branch without Generation IV promotion.**

## 19. Current judgment after verifier-source audit
The current Paper2Agent verifier is a substantially stronger rival than the earlier T0/T1 framing suggested.

Accordingly:
- q_ALLELE is retained unchanged;
- the expected rival outcome is now **DETECTION**;
- a Paper2Agent miss, if observed, becomes more informative;
- no result can authorize MQR-4.0 by itself;
- Generation IV remains **PREAUTHORIZED-BUT-NOT-EARNED** under G4-A/B/C/D.

**CURRENT STATE: ACTIVE / STRONG-RIVAL-PREDICTION-FROZEN / EXECUTION-PENDING / MQR-4.0 GATE-PRESEALED / NO PROMOTION.**


## 20. Verifier-succession audit — historical rival vs current successor
A temporal confound has now been resolved.

### Historical Paper2Agent verifier
The last public Paper2Agent state before the POP-TOOLS demo date is represented by:
- `jmiao24/Paper2Agent@cbcd5dfd2324fde298758c8092b1d96059567290` (2025-12-15);
- the same verifier constitution remains in `e573687e15f345e3f375cd0851373d588e436be3` (2026-02-10).

Its `test-verifier-improver` explicitly requires:
- “Test exactly what the tutorial demonstrates — no more, no less”;
- exact tutorial examples verbatim;
- “No Exploration”;
- “Do not write assertions beyond what the tutorial demonstrates”;
- no mock/synthetic test cases.

The Nature paper's own pipeline description is aligned with this historical constitution: the verifier creates per-function tests using the tutorial's example data as ground truth and removes tools that repeatedly fail those tests.

Because q_ALLELE is intentionally a **new synthetic invalid-input challenge** not present in the tutorial example set, it lies outside the historical verifier's authorized challenge envelope.

This does **not** prove a runtime mutant would necessarily pass historical Paper2Agent; it proves only:
**q_ALLELE was not a required or authorized test under the historical verifier constitution.**

### Current successor verifier
The current strong verifier documents were introduced in commit:
`61bdd684eb2d8ce57355d0ee0072393cb700f539` on **2026-09-16**.

They newly require:
- direct upstream execution;
- meaningful changed inputs;
- relevant missing/invalid inputs;
- detection of ignored inputs and changed defaults;
- preservation of upstream assumptions/defaults/units/error meaning;
- rejection of silent scientific-input repair;
- source-reuse and wrapper-quality review.

Therefore q_ALLELE is now inside the successor verifier's declared challenge envelope.

### Challenge-envelope succession
Define the authorized challenge envelope of verifier version V_t as:
`E(V_t)={q : q is licensed/required by V_t's verification constitution}`.

For the frozen q_ALLELE:
`q_ALLELE ∉ E(V_historical)`
while
`q_ALLELE ∈ E(V_2026-09-16+)`.

Thus:
`E(V_historical) ⊊ E(V_successor)`
for at least this observed challenge coordinate.

This is an externally observed **challenge-space expansion** in a real scientific-agentification method.

## 21. No-Retroactive-Rival-Strengthening rule
MQR must not conflate historical and present distinctness.

For a rival method R with versioned verification constitutions:
- historical comparison at time t uses `R_t`;
- present irreducibility uses the strongest current successor `R_now`;
- later successor absorption may defeat a **current** novelty claim;
- later successor absorption must not be projected backward to claim that the earlier rival already possessed that challenge capacity.

Formally, if:
`q ∉ E(R_t)` and `q ∈ E(R_{t+1})`,
then successor absorption updates present reduction status but does not rewrite the historical challenge envelope.

This is a fairness/lineage rule, not itself a novelty claim.

### Consequence for MQR-3.179
q_ALLELE changes role:
- **historical lane:** challenge-envelope succession witness;
- **current lane:** strong-rival positive control / compliance probe;
- **not sufficient:** current MQR-vs-Paper2Agent discriminant.

Therefore even if the current successor detects q_ALLELE, the result is scientifically useful: it confirms successor absorption and reduces CPC on this axis.

## 22. Raw demo baseline is not a current-rival baseline
The author-controlled `jmiao24/pop_gwas_agent@ca345e4d...` predates the 2026-09-16 verifier strengthening and is not compliant with the current verifier contract in at least two visible ways:
1. upstream failures are returned as ordinary `{"success": false, ...}` data instead of MCP tool errors;
2. the current verifier's preferred `message/reference/artifacts` output contract is not the demo's native return structure.

Therefore a fair current-rival experiment cannot use the untouched January demo as “Paper2Agent-current PASS”.

The admissible current-rival baseline must be:
1. regenerated or repaired under the current successor verifier;
2. independently verified to PASS;
3. hashed/frozen;
4. only then receive the q_ALLELE mutant.

The January demo remains a provenance/sibling execution surface, not the final current-rival baseline.

## 23. Generation-IV consequence
The verifier-succession result does **not** satisfy G4-A.

Reason:
- there is a documented constitutional difference between historical and successor verifier challenge envelopes;
- there is not yet an empirical current-rival PASS vs MQR-holdout differential.

Accordingly:
**G4-A = OPEN, not PASS.**
**MQR-4.0 remains NOT AUTHORIZED.**

What has been earned is narrower:
**REAL-WORLD SUCCESSOR-CHALLENGE-ENVELOPE EXPANSION OBSERVED / TEMPORAL RIVAL INDEXING REQUIRED / q_ALLELE DOWNGRADED TO CURRENT-RIVAL POSITIVE CONTROL.**

## 24. Updated state
**ACTIVE / VERIFIER-SUCCESSION-WITNESS / HISTORICAL-ENVELOPE-NARROWER / CURRENT-SUCCESSOR-ABSORPTION / RAW-DEMO-NONCOMPLIANT-WITH-CURRENT-VERIFIER / CURRENT-BASELINE-REGENERATION-REQUIRED / G4-A-OPEN / HISTORICAL-NOVELTY-HOLD.**


## 25. Delivery-custody audit — co-location is not challenge preservation
The first delivery-level CRF candidate was deliberately attacked before promotion.

Current Paper2Agent delivery rules intentionally separate:
- the **runtime package** delivered to the user;
- the **development/verification evidence** retained outside that package.

The delivered ZIP must contain the verified runtime, pinned runtime requirements, relevant scientific implementation/provenance or fixed-version installation instructions, and `USAGE.md` with scope and validation limits.

By default the ZIP omits:
- examples;
- test fixtures;
- test suites;
- notebooks;
- reports;
- agent records;
- environments;
- intermediate outputs.

However delivery validation is not evidence-free. Paper2Agent requires:
- ZIP SHA-256;
- packaged file/hash inventory outside the package;
- independent verification of the extracted ZIP;
- source-backed acceptance evidence kept outside the ZIP;
- `reports/delivery-validation.json` tied to the exact archive hash;
- completion hashes linking the final ZIP and delivery report.

Therefore:
**EVIDENCE NOT CO-LOCATED WITH THE EXECUTABLE ≠ CHALLENGE ROUTE DESTROYED.**

A challenge route can remain live through an externally bound evidence object.

## 26. Challenge Custody Tuple — provisional CRF refinement
For each challenge route r, replace the binary “inside package / outside package” criterion with a custody tuple:

`C(r)=<L,B,A,R,P>`

where:
- **L — Locator:** where the evidence/replay materials reside;
- **B — Binding:** how strongly those materials are cryptographically/version-identically tied to the exact artifact under judgment;
- **A — Accessibility:** whether an independent recipient can actually obtain them;
- **R — Retention:** whether the route persists over the relevant time horizon rather than only in an ephemeral builder workspace;
- **P — Replay sufficiency:** whether the retained material is enough to reconstruct the intended challenge rather than merely prove that “some validation happened”.

Provisional states:
- **LIVE-LOCAL** — challenge materials travel with the artifact and are replay-sufficient;
- **LIVE-EXTERNAL** — materials are external but strongly bound, accessible, retained, and replay-sufficient;
- **BOUND-BUT-INACCESSIBLE** — identity is preserved but recipient challenge reconstruction is unavailable;
- **ACCESSIBLE-BUT-UNBOUND** — evidence exists but cannot be reliably tied to the judged artifact;
- **EPHEMERAL** — builder-side evidence existed but retention is not established;
- **DEAD** — no adequate challenge route remains.

This is a CRF bookkeeping refinement, **not a novelty claim**.

## 27. Paper2Agent delivery classification
Paper2Agent-current supplies strong machinery for **B**:
- final ZIP hash;
- file/hash inventory;
- delivery-report hash;
- completion evidence tied to the verified production revision.

It also supplies a process for **P** inside the builder workspace:
- source-backed acceptance evidence;
- changed-input/error cases;
- independent verifier reports;
- delivery-validation records.

But recipient-side **A** and long-horizon **R** are not guaranteed merely by successful generation:
- detailed workspace evidence is not shipped by default;
- the final response links detailed evidence only when useful;
- evidence retained only in a private/ephemeral workspace can therefore become unreconstructable to a later independent recipient.

Thus the correct MQR verdict is not “Paper2Agent destroys challenge evidence”. It is:
**PAPER2AGENT SUPPORTS EXTERNAL CHALLENGE CUSTODY, BUT RECIPIENT REOPENABILITY DEPENDS ON ACCESS/RETENTION POLICY BEYOND THE RUNTIME ZIP.**

## 28. Prior-art reduction of custody residue
This custody distinction is already strongly anticipated by:
- SLSA-style external provenance attestations;
- in-toto-style artifact/step attestations;
- Workflow Run RO-Crate and related workflow provenance;
- assurance-case evidence stores;
- archival reproducibility packages.

Therefore “keep verification evidence externally but cryptographically bind it to the artifact” is not MQR novelty.

The only remaining MQR-specific question is whether **challenge-route replay sufficiency and authority role** require richer typed state than generic provenance/attestation provides.

This remains open and must be tested, not presumed.

## 29. Successor-custody synthesis
The Paper2Agent encounter now yields two concrete reductions and one retained MQR function:

1. **Historical verifier weakness cannot be projected onto the current successor.**
2. **Externalized verification evidence cannot be equated with lost challenge custody.**
3. MQR's remaining role, if any, is to ask whether the surviving external evidence preserves the *specific defeat route and authority consequence*, not merely artifact identity and execution provenance.

This further narrows CPC from “preserve semantics/provenance/tests” to:
**preserve the reconstructable, typed defeat route needed for a scoped authority judgment.**

## 30. Promotion impact
Neither verifier succession nor delivery custody satisfies MQR-4.0 promotion.

Current gate state:
- **G4-A:** OPEN;
- **G4-B:** OPEN;
- **G4-C:** currently under strong reduction;
- **G4-D:** NOT CONSTITUTED.

Generation IV remains **NOT EARNED**.

## 31. Updated state
**ACTIVE / HISTORICAL-vs-SUCCESSOR-RIVAL-SEPARATED / q_ALLELE-CURRENT-POSITIVE-CONTROL / EXTERNAL-CHALLENGE-CUSTODY-ADOPTED / COLOCATION-CRITERION-REJECTED / CPC-RESIDUE-FURTHER-NARROWED / G4-A-OPEN / NO-4.0-PROMOTION.**


## 32. Research-OS backflow — custody tuple withdrawn as redundant
Cross-Lab retrieval found that the provisional Challenge Custody Tuple `C(r)=<L,B,A,R,P>` does not earn a new MQR object.

### Reduction to existing MQR
MQR-3.13 already represents custody topology through:
- `I` byte/content integrity;
- `P` temporal priority/pre-outcome commitment;
- `A` continued availability;
- `D` discoverability/linkability;
- `S` semantic adequacy;
- `R` replay/reconstruction capacity;
- `X` adversarial reach.

MQR-3.10 already defines the authority object as:
`(terminal summary, provenance reserve)`
and explicitly requires a challenge-generative reserve rather than archival maximalism.

The provisional tuple therefore maps approximately as:
- Locator → `D`;
- Binding → `I/P` plus source identity;
- Accessibility/Retention → `A`;
- Replay sufficiency → `S/R/X`.

FMS-4.2 independently adds the organizational-custody warning:
**distributed custody ≠ distributed accessibility; ownership map ≠ repair map.**

### Verdict
**CHALLENGE-CUSTODY-TUPLE = REDUNDANT VIEW / NO NEW PRIMITIVE / ABSORB INTO MQR-3.10 + MQR-3.13.**

The Paper2Agent delivery case is therefore best treated as a new positive external witness for already-existing MQR custody doctrine:
- runtime artifact and defeat-preservation reserve may be separate;
- equivalence depends on reachable defeat topology, not co-location;
- cryptographic binding alone is insufficient without availability, semantics, replay and adversarial reach.

## 33. Information-gain reassessment of q_ALLELE runtime
Research OS 2.4.4 requires frontier compression, authority separation, minimal world contact, and stopping when further work mainly improves machinery without reducing the live uncertainty.

After the verifier-succession audit:
- historical verifier: q_ALLELE lies outside its authorized challenge envelope;
- current successor verifier: q_ALLELE lies inside its explicit changed/invalid-input and silent-repair envelope;
- raw January demo: not a compliant current-rival baseline;
- current verifier should detect/repair/refuse the mutant if implemented faithfully.

Therefore the expected information value of a q_ALLELE runtime is now asymmetric.

### What runtime can still answer
It can test **implementation compliance**:
does the current Paper2Agent successor actually operationalize its stronger written verifier doctrine on this concrete mutant?

### What runtime can no longer answer by itself
It cannot establish CPC philosophical distinctness:
- detection confirms rival absorption;
- a miss exposes a verifier implementation gap, but still does not establish CRF novelty;
- either branch leaves G4-B/C/D untouched.

### Resource decision
q_ALLELE runtime is reclassified:
**OPTIONAL HIGH-QUALITY COMPLIANCE WORLD-CONTACT / NOT REQUIRED FOR CURRENT NOVELTY ADJUDICATION.**

This is not cancellation of the frozen experiment. The packet remains executable and may be run later without redesign.
It is a decision that scarce execution effort should not be spent merely to confirm a low-discrimination positive control when a stronger current-rival matched pair has not yet been found.

## 34. Successor-hard discriminant requirement
The next informative object inside MQR-3.179 is now a matched pair `(A,B)` satisfying all of:

1. **Current Paper2Agent equivalence:** the strongest current verifier, runtime acceptance, source-reuse checks, changed/invalid-input tests and delivery validation classify A and B identically.
2. **Mature-framework equivalence:** provenance/assurance/full-abstraction/diagnosability machinery, applied in ordinary form, also does not already separate A and B.
3. **MQR divergence:** a pre-existing MQR coordinate—preferably defeat-route noncommonness, substitute topology, or replay-authority role—classifies A and B differently.
4. **Authority relevance:** that difference changes a scoped scientific licensing/refusal/reopenability judgment rather than merely archive convenience.
5. **Prospective testability:** the divergence can be frozen and world-contacted without defining the MQR coordinate after seeing the result.

Until such a pair exists:
**NO CURRENT-RIVAL DISTINCTNESS TEST IS READY.**

## 35. Generation-IV gate update
The Paper2Agent encounter has produced valuable external contact, but it currently reduces rather than expands MQR.

- **G4-A:** OPEN — no current-rival empirical differential.
- **G4-B:** OPEN — no non-isomorphic replicated differential.
- **G4-C:** NEGATIVE PRESSURE — mature rivals absorb most CPC components.
- **G4-D:** NOT CONSTITUTED — existing MQR-3.x custody/provenance machinery already absorbs the latest candidate.

Therefore:
**MQR-4.0 PROMOTION NOT JUSTIFIED.**

## 36. Current judgment
MQR-3.179 remains the correct number.

Its present result is:
**SUCCESSOR ABSORPTION + INTERNAL REDUCTION, NOT GENERATIONAL BREAK.**

The scientifically justified continuation is not another easy mutant. It is a successor-hard matched-pair search under the five conditions above.

## 37. Updated state
**ACTIVE / q_ALLELE-OPTIONAL-COMPLIANCE-WORLD-CONTACT / HISTORICAL-VERIFIER-ENVELOPE-WITNESS / CURRENT-SUCCESSOR-ABSORPTION / CHALLENGE-CUSTODY-TUPLE-WITHDRAWN-AS-REDUNDANT / MQR-3.10+3.13-REUSED / SUCCESSOR-HARD-MATCHED-PAIR-REQUIRED / G4-A-OPEN / NO-4.0.**


## 38. Closure
MQR-3.179 now closes.

### Why closure is justified
The stage's original question was whether a first executable semantic-mutant probe could show that challenge-preserving compilation adds something beyond ordinary runtime/reference validation.

The answer is no longer a simple empirical yes/no:
1. mutation/provenance/metamorphic/property-specific testing prior art absorbed most of the original novelty surface;
2. context-of-use credibility and assurance cases absorbed the generic authority-defeat mapping;
3. full abstraction, robust property preservation, counterexample/witness preservation and diagnosability absorbed generic semantic/challenge preservation;
4. Paper2Agent's own verifier evolved from tutorial-only validation to changed/invalid-input and source-fidelity verification, directly absorbing q_ALLELE into the current rival;
5. q_ALLELE is therefore a historical challenge-envelope witness and current-rival positive control, not the decisive current distinctness test;
6. the provisional custody tuple was redundant with MQR-3.8/3.10/3.13 and was withdrawn.

### Final verdict
**PASS-REDUCTION / FIRST-WORLD-CONTACT-CONSTITUTION-REVISED / SUCCESSOR-ABSORPTION-WITNESS / CPC-BROAD-NOVELTY-REJECTED / q_ALLELE-POSITIVE-CONTROL / MQR-3.10+3.13-REUSED / CURRENT-DISTINCTNESS-UNRESOLVED / GENERATION-IV-NOT-EARNED.**

### Carry-forward invariant
The only scientifically justified continuation is a new problem:
find a **successor-hard matched pair** that the strongest current rival and mature adjacent frameworks classify alike, but a pre-existing MQR defeat-route coordinate prospectively separates in an authority-relevant way.

That is no longer the same experiment. It becomes MQR-3.180.


## 38. Novelty-defeat literature byte-custody closure
All literature objects that materially defeated or narrowed CPC/CRF novelty claims in MQR-3.179 have now been ingested into the canonical Research OS custody structure.

### 10_PAPERS — Canonical Literature Commons
Canonicalized and moved:
- Shulepov (2026), *Mutation Testing for Reproducibility Safeguards in Machine Learning Research Software: An Empirical Study* — arXiv 2608.27100v1.
- Bartocci et al. (2023), *Property-Based Mutation Testing* — arXiv 2301.13615v1.
- Lin, Simon & Niu (2020), *Exploratory Metamorphic Testing for Scientific Software*.
- Leo et al. (2024), *Recording Provenance of Workflow Runs with RO-Crate*.
- Abate, Busi & Tsampas (2020), *Fully Abstract and Robust Compilation and How to Reconcile the Two, Abstractly* — arXiv 2006.14969v4.
- Abate et al. (2018), *Journey Beyond Full Abstraction: Exploring Robust Property Preservation for Secure Compilation* — arXiv 1807.04603v6.
- Liu et al. (2013), *Counterexample-Preserving Reduction for Symbolic Model Checking* — arXiv 1301.3299v1.
- Beyer, Kettl & Lemberger (2024), *Fault Localization on Verification Witnesses*.
- Wei et al. (2024), *ACCESS: Assurance Case Centric Engineering of Safety-Critical Systems*.
- Muram & Javed (2023), *ATTEST: Automating the Review and Update of Assurance Case Arguments*.
- Almeida, Iacob & van Eck (2007), *Requirements Traceability in Model-Driven Development: Applying Model and Transformation Conformance*.
- Parvinian et al. (2019), *Credibility Evidence for Computational Patient Models Used in the Development of Physiological Closed-Loop Controlled Devices for Critical Care Medicine*.
- Kuemmel et al. (2020), *Consideration of a Credibility Assessment Framework in Model-Informed Drug Development*.
- Viceconti et al. (2021), *In Silico Trials: Verification, Validation and Uncertainty Quantification of Predictive Models Used in the Regulatory Evaluation of Biomedical Products*.

### 20_NON_PAPER_SOURCES
Canonicalized and moved:
- Shulepov (2026), *MLReproMutate v0.1.0* reproduction artifact ZIP.
- NASA (2024), *NASA-STD-7009B — Standard for Models and Simulations*.
- NASA (2026), *NASA-HDBK-7009B — Handbook for Models and Simulations*.
- NASA-HDBK-7009B worksheet.
- NASA-STD-7009A and historical NASA-STD-7009 reference versions.
- NASA-STD-7009A requirements/recommendations lifecycle worksheet.

### Custody verdict
**NOVELTY-DEFEAT LITERATURE BYTE-CUSTODY = COMPLETE FOR THE CURRENT 3.179 PRIOR-ART ATTACK SET.**

This closes the gap between literature-based novelty reduction and actual source-byte custody. The prior-art defeat is no longer metadata/abstract-only for the current canonical set.

The remaining item in 00_INTAKE, `knight1986.pdf`, is unrelated to this MQR-3.179 acquisition batch and was intentionally left untouched.

## 39. MQR-3.179 stopping rule
MQR-3.179 now has one remaining substantive task:
**attempt one successor-hard matched-pair construction under the already frozen five-condition requirement.**

If no non-reducible pair is found after a focused attempt:
- close MQR-3.179 as **SUCCESSOR ABSORPTION / CPC DISTINCTNESS NOT EARNED / PRIOR-ART CUSTODY COMPLETE**;
- proceed to MQR-3.180 rather than prolonging the current stage through additional ad hoc mutants.

If a qualifying pair is found:
- preseal it prospectively inside 3.179;
- execute only the minimum world-contact needed to adjudicate that pair;
- then close 3.179 before opening the next stage.

No further concept invention is authorized inside 3.179 unless forced by a concrete matched-pair failure that existing 3.x machinery cannot represent.
