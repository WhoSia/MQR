# MQR 5.4 / chat MQR 41 — Two New User-Held Papers: Alphabet Construction, EXHYTE, and Where Scientific Questions Come From

Date: **2026-11-11 KST**. Provenance: source-grounded, two original PDFs received today, read directly in the authenticated Drive. **Session number MQR 41 is not a research-version number**. Version remains MQR 5.4. No automatic transfer of source authority to global Harvest.

## 0. Intake identity, format, canonical folder

1. **JiongHan Wang and WenChao Huang (2026)**, *An Automated Framework for Input Alphabet Construction in Stateful Protocol Implementation Learning*, **arXiv 2606.23464v1 (22 June 2026)**, manuscript header ASE 2026. Original filename `2606.23464v1.pdf`; verified content title/authors/arXiv identifier; Drive `1g0-2mURv2XL0CPT2OonO0E6emrtBW9sz`. **Renamed** to normalized bibliographic title and **moved** from folder `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16` (00_INTAKE) to `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP` (10_PAPERS), preserving file ID and raw file bytes. Status: PREPRINT SOURCE; do not upgrade to final proceedings without edition comparison.

2. **Md Musaddaqul Hasib et al. (2026)**, *Unifying AI-assisted scientific discovery around exploration, hypothesis generation, and testing*, *Patterns* 7, article **101660**, published 9 October 2026, DOI **10.1016/j.patter.2026.101660**, open access publisher PDF. Original filename `PIIS2666389926001698.pdf`; verified content title/copyright/DOI; Drive `12dDPLmrn9-W-SDkw7SzY-4sN7eUR8BHu`. **Renamed** normalized bibliographic title and **moved** from 00_INTAKE to 10_PAPERS, same ID and bytes. Status: PUBLISHER OPEN-ACCESS REVIEW; its literature synthesis is not a direct primary experiment.

Both are **HELD** now. The three-paper prior-art radar loses these two candidates; Henry et al. (CONCUR 2025), DOI 10.4230/LIPIcs.CONCUR.2025.20, remains a retrieval candidate. The standing three historic complete-source/facsimile gaps remain as before.

## 1. Wang–Huang: direct sections and what their method actually achieves

Directly inspected original first pages and §4.1/4.2; §5.1–5.3; Table 3 and §6.2; Table 4; later method limitations and conclusion. Source `https://drive.google.com/file/d/1g0-2mURv2XL0CPT2OonO0E6emrtBW9sz/view`.

- Problem: active state-machine learning is limited by an **expert-fixed input message alphabet**. A behavior cannot be exposed if triggering input symbols are absent. This is a concrete manifestation of *fixed interrogation grammar*.
- Framework: LLMs derive protocol message-format configuration, structured mutations generate valid and invalid input symbols, mini-batch learning amortizes state-machine inference as the alphabet grows. Distinguish mutation of message symbols from actual invention of physically new measurement operators or scientific quantities.
- Evaluation: authors report **9 implementations of 5 kinds of protocol** (RTSP, FTP, SMTP, TLS 1.3 server/client groupings). Some full-alphabet baselines fail to terminate within their **12-hour** budget; the mini-batch strategy mitigates query cost. Their Table 4 lists ten newly found semantic-bug entries with mixed statuses (fixed, reported, and one CVE-assigned case). This is **authors' reported experimental outcome**, not independently replicated in this project.
- Relevant negative limit **explicitly stated by source**: single-symbol mutation priority may miss bugs requiring interactions among multiple message types (§6.2.1). The MQR41 toy demonstrated independently that a zero-one-step-gain action can be prerequisite for an informative composite word. However, MQR toy is **not evidence the Wang–Huang algorithm suffered such a loss on those benchmarks**. Their diverse-symbol approach addresses some interaction space; overgeneralization would be false.
- Additional methodological issue: the generated alphabet remains constrained by an already interpretable protocol documentation schema and chosen mutation operators. What is *not known to be expressible* by that starting representational regime is not automatically searched.

### Collision and surviving question

Automation of input-alphabet construction and discovery of semantic discrepancies **is prior art**. MQR should not claim to invent it. What remains worth asking: what creates or legitimates the *generative schema* for experiments, and how can independent world-contact expose a variable or mechanism beyond the admitted input grammar?

## 2. Hasib et al.: direct review sections and scope limits

Directly inspected publisher PDF summary, introduction, EXHYTE definitions, source corpus selection, hypothesis/test transitions, discussion and future outlook, including the hypothesis-space scope discussion. Source `https://drive.google.com/file/d/12dDPLmrn9-W-SDkw7SzY-4sN7eUR8BHu/view`.

- EXHYTE = **EXPLORE → HYPOTHESIZE → TEST**, with feedback to previous steps, proposed as an **empirical workflow abstraction** for comparing AI-assisted science systems. Authors **explicitly reject** treating it as a comprehensive universal philosophy of scientific method.
- The original survey mapped **87 papers**, sampled chiefly across **2018–July 2025** (not a corpus exhausting 2026 research) with manually filtered sources. Review publication in October 2026 **must not be confused with a 2026 survey cutoff**. Do not repeat the 87 count as independently reproduced.
- Gap: systems are more mature at retrieving/exploring and generating ideas than at converting hypotheses into feasible **executed, independently evaluable tests**, and recycling results into subsequent inquiry.
- Crucial author-supplied limitation: extant LLM discovery inherits constraints and paradigms implicit in published literature, available data and user-specified targets; a pipeline covering all three stages is not necessarily more scientifically trustworthy than a smaller workflow. This is directly relevant to MQR40's concern about drifting into conventional rather than ambitious questions.
- Their introduction explicitly treats **question formulation, conceptual change, instrument development, and social validation** as partly outside the 3-stage review abstraction. It would be unfair to criticize the authors as if they pretended to solve these issues.

### Collision and surviving question

The whole 'Explore–Hypothesize–Test–Feedback' loop is established and cannot be MQR novelty. However a workflow loop can be operationally *closed* while the space of interrogations/questions admissible to it is structurally *closed*. This is a scope distinction, not yet a new theorem.

## 3. Four-level inquiry map (proposed research organizer, not a universal science formalism)

Define a scoped inquiry state I=(V,A,O,N;H), where V is currently meaningful variable/concept vocabulary, A is feasible experiment operations (possibly compositional), O is instrument response mapping, N is the plural collection of domain/community evaluation norms, and H is the historical experiment/evidence trace. The semicolon flags H as the evidence record rather than an intrinsic physical world variable.

Distinguish four transitions:

- **T0 (within-grammar inference)**: with fixed V,A,O,N, test rival hypotheses and update H.
- **T1 (compositional extension)**: with fixed *primitive* alphabet A, construct a new experiment word via closure under composition. Recombination can gain information even when primitive atomic information gain is zero.
- **T2 (grammar development)**: add new physical action templates or instrument modes, modify V or O with a tested interface; e.g., mutation strategies in Wang–Huang are an automated, *schema-constrained* T2, not total ex nihilo discovery.
- **T3 (norms/concept authority)**: revise which results count as evidence, which emerging variables deserve referential standing, which experiments count as legitimate, and which projects count as fruitful. This is the 'paradigm of paradigms' frontier. T3 need not always follow T2, and community adoption is not itself a truth maker.

This taxonomy is purpose-built for MQR discussion, collides with many established methods (experimental exploration, Kuhnian conceptual shift, active automata learning, research programs); not a new fundamental ontology or unique way to partition scientific practice.

### Precise MQR41 failure witness

Previous `mqr41_compositional_protocol_search.py`: state s=(x,y,z), sensor x, adjacent swaps S_xy and S_yz. S_yz alone has zero gain; the sequence S_yz followed by S_xy reveals z. Immediate-gratification myopic action selection reaches only 4 classes, 2-step composition reaches 8. **This is T1, not T2.** Avoid incorrectly using it as proof of genuine experiment invention. Prior work in active automata/plan synthesis and observability already owns its formal structure.

### Stronger external validation design

A meaningful real-world benchmark should provide:
- explicit instrument resource limits (allowed probes, time/energy, calibration drift) and a held-out repertoire of potential new apparatus couplings;
- independently pre-registered evidence categories: 'novel symbol within known grammar', 'novel composite protocol', 'genuinely new apparatus mode', 'new concept with independent referential support', or 'artifact';
- false discovery tests across device, batch, and researcher, not just a retest that shares calibration ancestry;
- comparison against grammar-constrained active learning, budgeted experimental design, EXHYTE-style closed-loop, and opportunistic random experiment/recombination;
- a separate historical case study (Faraday/Steinle or electro-optical instrument development) to check whether the taxonomy captures actual conceptual and material change, including social criteria.

**No genuine novel physical-world test has been run in this turn**. Scope remains conceptual and computational.

## 4. MQR origin, DFS/BFS and Harvest provenance

Restore questions across UV–Vis / reduction-to-circuit, possible alien sciences with distinct measurement vocabularies, criteria that constitute paradigms, 'questions one did not know one could ask', and why mathematics persists in engineering. This new pair should **not** shift MQR into merely a paper about automated protocol testing or into a generic LLM agent workflow taxonomy.

Existing MQR global Harvest [LR-20260916-B](https://app.notion.com/p/3ddef561cf9281f1975bd07b6883ab8f), [LR-20260916-C](https://app.notion.com/p/3ddef561cf9281ed8085cca1290f447f), and [LR-20260928-D](https://app.notion.com/p/3e9ef561cf928109956eedd9c52ac300) already cover Steinle exploratory work and 'operational split ≠ natural kind'. Neither Wang–Huang nor EXHYTE gives general authority to infer physical ontology from a refined class partition. Potential reusable Harvest backflow is **SOURCE-SPECIFIC**: schema-limited alphabet expansion, and workflow-loop completeness versus question-space openness. No global Harvest fragment or receipt claimed by this local note.

## 5. Next experimental decision / stopping condition

The next useful **DFS** is not another longer toy action path; it is either a real optical/chemical instrument case with explicit causal controls or a genuinely coupled unknown-state interface that cannot assume identical initial states. Before any novelty claim, reopen relevant held historical original instrument reports and compare rival interpretations. **BFS return** to Q3: the legitimacy of a new type of observation changes with experimental practice, historical institutions and counterevidence, not solely increasing number of distinguishable model states.

Preserve two papers' original source IDs and exact versions. GitHub writes through user-owned connector only (commit author and committer `WhoSia`, never `GitHub-Actions[bot]`). Live source ledger reclassified exactly these two from 'PROSPECT' to 'HELD'; Henry et al. (2025) remains a **provisional acquisition target**, and pre-existing historical missing-source items remain.

### Status
- Completed: 2 held files identified by bytes/readback, renamed & moved, relevant source sections directly read, prior-art claims sharpened, missing source registry corrected.
- Remaining: other original user-requested broad research frontiers, independent replication of paper's findings, real instrument validation, optional complete page-by-page deep reading.
- User action: none required.
