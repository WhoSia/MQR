# MQR 5.4 · MQR 44 · Record 06 — Science under constrained information: admission, interview, small networks, and experiment choice

**2026-11-22 KST.** Research program remains **MQR 5.4 OPEN**. Cross-domain comparative synthesis; numerical examples synthetic. Code run witnessed in local Python before GitHub commit (terminal output PASS). Do not equate admissions procedures with scientific research or claim that selected students have any specific traits.

## 1. Question and scope
User asked MQR to consider university admission, small societies and interviews as cases of science flowering under information constraints. The intended analogy is to epistemic mechanisms: limited observations, endogenous selection, bounded time and processing, repeated/fragmentary communication, active experimental design, and the formation of legitimate questions. The project should not turn this into admissions coaching or a claim that evaluating applicants is itself science.

## 2. Literature checked
- **Compensatory selection/collider:** PLOS ONE (2022), 'A compensatory selection effect with standardized tests: Lack of correlation between test scores and success is evidence that test scores are predictive of success', https://doi.org/10.1371/journal.pone.0265459. This is a simulation-based study on selection affecting observed correlations, NOT a universal proof that any test predicts success.
- **Admission interviews:** 2007 meta-analysis of 44 studies https://doi.org/10.1026/0033-3042.58.2.93; reported corrected validities 0.11 unstructured vs 0.21 structured for academic-exam outcome (context and transport require care). 2018 medical-admission meta-analytic review https://pmc.ncbi.nlm.nih.gov/articles/PMC6179055/ reports limited reliability of traditional interviews. Admission-specific predictive outcomes are not identical to the ability to formulate original research questions.
- **Scientific communities:** Kevin J. S. Zollman (2007), 'The Communication Structure of Epistemic Communities', https://doi.org/10.1086/525605; Zollman (2010) transient diversity, https://gwern.net/doc/philosophy/epistemology/2009-zollman.pdf. Limited connection can sometimes prolong theory diversity and improve eventual correctness, at the cost of slower learning, under the particular model assumptions. No blanket recommendation for information suppression.
- **Constrained cognitive resources:** held Lieder & Griffiths (2019), 'Resource-rational analysis', Drive `13wE_bRR3YDk7iRzrNu8GrwwWCDk0yDsu`, directly fetched text, opening abstract/introduction explicitly discusses optimal use of bounded cognition and nonidentifiability of latent mechanism from finite observations.
- **Experimental strategy rival, important NEW 2026 held text:** Dubova, Moskvichev & Zollman (2026), 'Against theory-motivated experimentation: Can random experimental choice lead to better theories?', *Collective Intelligence* 5(1), DOI 10.1177/26339137261421577, Drive `1XI4OoLOa4rrfA26mUPMULBb0ErwrCYrP`. Full text extraction (89,451 chars) available and opening sections directly checked. Its multi-agent model found randomly chosen experiments improved broader model informativeness/prediction vs confirmation/falsification/disagreement-driven policies under modeled conditions; theory-motivated sampling can appear to succeed on endogenous selected samples. This challenges a maxim 'always maximize immediate discriminatory information'. It does NOT prove random experimentation best across all physical sciences, costs or causal objectives.
- **Inquiry psychology:** Wason (1960) original journal 'On the Failure to Eliminate Hypotheses in a Conceptual Task', https://doi.org/10.1080/17470216008416717; contemporary replication/extension and think-in-opposites https://pmc.ncbi.nlm.nih.gov/articles/PMC10219317/. The 2-4-6 hypothesis task is a minimalist laboratory analogue, not evidence that admissions interviews have Wason's objective.

## 3. Exact negative result: selection destroys naive population inference
Let X,Y be *independent* Bernoulli(1/2) toy indicators, and select S=1 if X=1 or Y=1. Unconditionally covariance(X,Y)=0, Var(X)=Var(Y)=1/4.
Among accepted states {(0,1),(1,0),(1,1)}, each has conditional probability 1/3.
Thus E[X|S]=E[Y|S]=2/3; E[XY|S]=1/3; Cov(X,Y|S)=1/3-4/9=-1/9; Var(X|S)=Var(Y|S)=2/9; Pearson Corr(X,Y|S)=**-1/2**.
The negative correlation does NOT show that the two properties causally conflict in the population; it is entirely induced by conditioning on selection. This deliberately simple 'either indicator suffices' rule is not a descriptive model of any actual university's decisions. It should be called a collider example, not an effect size estimate.

## 4. Exact positive example: a small query can discriminate more than many redundant queries
Take three toy rules all fitting seed triple (2,4,6):
 H1: strictly increasing numbers;
 H2: arithmetic progression;
 H3: all three numbers even.
A binary feedback response about (2,4,6) is YES for all => zero information about which hypothesis is intended. (3,5,8) yields YES only for H1, making a 1-to-2 partition. With equal priors, its expected information gain is binary entropy h2(1/3)=**0.918295834... bits**. Asking a novel query is not itself a proof of the true rule: we assume one of three listed hypotheses is guaranteed, truthful feedback and equal prior probabilities. Removing those assumptions changes the calculation.
This is the well-known Wason-type inquiry setting, not a unique MQR discovery. The toy demonstrates information *conditional on explicitly declared alternatives*. A globally unanticipated hypothesis can make a prior question-design optimum myopic.

Code [exact example](../language/real/experiments/mqr_sparse_information_selection_v54.py) was executed in the local Python runtime and returned `PASS: exact collider correlation -1/2; rule-query info 0 vs 0.9183 bits` before GitHub commit.

## 5. Small epistemic society: diversity, transmission, epistemic independence
A tightly connected group with repeated messages has many reports but not necessarily independent evidence lineages. If several people forward one original observation, nominal report count multiplies without multiplying underlying evidential independence.
A sparsely linked group may retain competing models longer but miss valid corrections and coordinate less effectively. The old heuristic 'more information sharing always improves group knowledge' is thus neither guaranteed nor simply inverted.
Zollman's results depend on agents' learning rules, payoffs, network topology, and periods. The real MQR problem is to characterize **when communication permits construction and criticism of new question classes, versus when it freezes the community's vocabulary or accelerates valid convergence**. Need model of question invention in addition to fixed-arm bandit models.

## 6. Distinctions to preserve
(1) Predictive selection of applicants ≠ experimental inference ≠ conceptual invention; analogous epistemic gates, distinct social/ethical objectives.
(2) Reliable scoring ≠ valid measurement of latent research ability ≠ fair treatment; interview structure improves certain kinds of validity in studies but may restrain open-ended question emergence.
(3) Individual bounded rationality ≠ collective rationality; outcomes depend on communication institutions.
(4) Information gain *within a fixed set of hypotheses* ≠ question-generating reach in a changing hypothesis space.
(5) Statistical independence of reports ≠ independence of observation ancestry, particularly under common sources, reputation cascades and algorithmic aggregation.
(6) The Dubova et al. result directly challenges simplistic 'maximize immediate discriminatory information' even when experiments are available.

## 7. Research design, rival explanations, phase status
Four candidate case families:
- Structured versus open exploratory interview: criterion validity, procedural comparability, inventive question counts; avoid real people and high-stakes interventions without consent; possible simulations/archival studies.
- Historical scientific society: document dated independent observations, transmission routes, rival persistence and changed experiment menus; neither romanticize isolation nor assume infinite information.
- Exploratory science (Steinle 1997) versus fixed question testing (Wason 1960 / resource-rational experiments); classify what changes in L,Q,I rather than only posterior updates.
- Admission selection: build separate inference about applicant population vs observed selected pool, with explicit selection diagram. Cross-check against 2022 PLOS paper.

Propose a **resource-bounded question-generation protocol**: reserve exploration budget for queries not optimized solely against current favored hypotheses, separately log discrimination vs domain coverage, use an independent evaluation domain to expose selection-induced apparent success, and allow question retirement/reform (Kuhn loss). This is a testable workflow hypothesis rather than verified general method.

Critical rival: all useful outcomes may be explained by existing statistical selection, active learning, social network epistemology, and resource-rational cognition. If so, MQR's contribution is a careful integrative comparative structure; no exclusive new meta-law.

**Decision:** a legitimate ambitious new branch under seven-frontier constitution; not a stage upgrade. Research claims tied to exact cited sources and bounded models. Next: inspect exact methods/parameter regimes in held 2026 Dubova et al., and develop negative-control simulations where random query selection performs worse than targeted design; this can falsify overgeneralization.
