# MQR 5.4 · MQR 44 · Record 05 — Exploratory experiment, science in transit, and nonmonotone question genesis

**Date:** 2026-11-22 KST; MQR research version 5.4 remains OPEN. **Source level:** direct reading of held Steinle (1997) and Secord (2004) machine-extracted full-text; historical corroboration from published catalogues/transcriptions, not page-by-page verified holograph manuscripts. Formal example synthetic. No 5.5.

## 0. Why this is a genuine return to the founding question
The user's MQR43 20:09 / 20:19 prompts criticize an assistant drift into local metrological and historical side-projects, **without devaluing rigorous history of science**. They ask for structurally ambitious physics/philosophy of paradigm genesis and a Work-source-acquisition/Chat-research division. The exact root in `research/MQR_5_4_OPEN_HORIZON_CONSTITUTION.md`: how many different sciences could intelligent agents construct facing one resisting world, and how they could bridge those sciences when the next question may not yet be expressible in current terms.

MQR44 records 02–04 distinguished observation, intervention, semantics, and global gluing. This note adds a needed **genetic** dimension: the operation that constructs new legitimate contrasts, not just testing contrasts already in a shared catalogue.

## 1. Direct original scholarship read
**Friedrich Steinle (1997), 'Entering New Fields: Exploratory Uses of Experimentation'**. Held PDF `1rl444ab9HV-Q285EwbPq1QBR2z5g3JcR`. Fetched full 30,035-character extracted text. In abstract/introduction, distinguishes exploratory experimentation where no reliable theory or conceptual framework is yet available, from straightforward theory-testing. His procedural diagnostic is specific: vary many parameters, separate necessary from merely modifying conditions, seek stable regularities, invent useful representations, and construct simple/pure experiments isolating them. Ampère and Faraday are considered as different historical actors. This is **strong prior art** for the insight that scientific questions can be made by exploratory manipulations; MQR should not claim to originate it.

**James A. Secord (2004), 'Knowledge in Transit', Isis 95:654–672**. Held PDF `1Y0N6ke4RCf6iDw7pl9S34jgwcI9VjBYt`. Directly fetched 82,718-character extracted text; abstract foregrounds circulation, movement, translation, transmission, and communicating practices. Secord specifically criticizes localizing knowledge as an end in itself and parochial antiquarianism. This directly disciplines MQR's choice of case selection: source fidelity must support the bigger account of science's movement and uptake, not crowd it out.

**Michael Faraday (1852), 'On the Physical Lines of Magnetic Force'**, primary publication digitization at Wellcome Collection, https://wellcomecollection.org/works/z4rgjue7/items, 1852 catalog/date, original held by Royal College of Surgeons of England; online excerpt displays Faraday distinguishing a merely ideal gravitational force line from a physically independent ray-line and discussing electricity/magnetic force. Separate 1852 work **'On the Physical Character of the Lines of Magnetic Force'** appears in Philosophical Magazine vol. 3 and in `Experimental Researches in Electricity`; these similar titles are NOT interchangeable editions. The Wellcome online page shows a *limited excerpt*, so do not present the two papers as identically full-text verified or infer exact chronology of specific conceptual innovations from this limited access. This is a promising primary-source spine for a historical case, not a completed dated adoption history.

**Kuhn secondary verification**: Stanford Encyclopedia of Philosophy, 'The Incommensurability of Scientific Theories', https://plato.stanford.edu/entries/incommensurability/ §§2.1, 2.3.1. Kuhn's 'Kuhn loss' explicitly involves old legitimate scientific problems becoming obsolete/unscientific, and newly important problems appearing. Late Kuhn's cross-classifying kinds and 'bilingualism, not literal translation' are discussed. The encyclopedia is a secondary philosophical synthesis, not Kuhn's autograph primary text. This negates any naive monotone question-set growth axiom.

## 2. Revision of Question-Generative Reach
Let a historically bounded scientific practice at time t be
  P_t = (L_t, Q_t, I_t, G_t, S_t, E_t),
where Q_t denotes recognized inquiries rather than all sentences logically expressible in L_t. This is a **provisional comparative description**, not an exhaustive ontology.
The earlier naive measure |Q_(t+1)|-|Q_t| is **not invariant** under relabeling and ignores displaced questions. More importantly, exploratory experiment can modify L,Q,I and the ranking of goals jointly. Late Kuhn also permits branching into contemporaneous incommensurable disciplinary descendants. There need not be a single chronological total order of all Q_t.

Proposed diagnostic instead of a scalar:
  GAIN(P_t -> P_u; R) = supported questions newly recognizable/executable, relative to declared relation R;
  LOSS(P_t -> P_u; R) = formerly legitimate questions no longer recognized/executable;
  REFORM(P_t -> P_u; R) = questions retained but with new meaning/proof/operational criterion;
  UNRESOLVED(R) = no justified cross-lexicon identity for the candidate questions.
These are **typed research decisions**, not validated counts. If semantic counterpart R is unknown, do not quietly label every source question as either lost or retained.

Exploration should be modelled not only by a set of present questions, but via a **question-producing policy** F mapping admissible histories of observations, interventions and exemplars to candidate revisions of P. Multiple incompatible F may fit the same current empirical record. A robust test must find historical traces of what was *actually invented or abandoned*, not merely mathematically writable post hoc.

## 3. The alien-science bootstrap trap: no paired observations => no justified joint bridge
A hidden-world illustration with four equiprobable states w∈{0,1,2,3}, two binary devices:
  A(w)=floor(w/2); B(w)=w mod 2.
A alone partitions the worlds into {0,1}/{2,3}; B alone into {0,2}/{1,3}; the paired (A,B) signature discriminates all four. This is an intentionally *analyst-supplied ground truth*, not something agents learn simply by separately observing their own unpaired samples.

The unpaired empirical results p_A(0)=p_A(1)=p_B(0)=p_B(1)=1/2 admit an entire **coupling family**:
  p(0,0)=p(1,1)=t,
  p(0,1)=p(1,0)=1/2-t, 0<=t<=1/2.
At t=0 variables are anti-correlated; at t=1/4 they are independent; at t=1/2 they are perfectly correlated. The separate marginal data cannot choose among these couplings. Identical marginal distributions thus do **not** identify the actual observational pairing.

[Executable exact rational check](../language/real/experiments/mqr_unpaired_bridge_identifiability_v54.py) enumerates partitions and validates three different exact couplings with identical marginals. Treat it as an elementary known coupling/identification point; no claim of novel statistical discovery.

Operational lesson: a would-be translator requires access to **shared events, controlled synchronized co-measurement, jointly interpretable interventions, or another independently justified alignment**, rather than quietly supplying a deity's common hidden world index. Realizing a shared experiment itself may require a bridge and presents a bootstrap problem. But this example does NOT prove translation is impossible: paired measurement or other knowledge can solve the posed finite problem.

## 4. Proposed far-reaching research thesis, falsification and source gate
**Thesis (research conjecture, not theorem):** possible-sciences comparability requires studying both (i) the typed structure of partially shared questions/operations and (ii) the dynamically learned procedures by which those questions/operations arise, migrate, and may be abandoned.

Historical predictions:
- A documented exploratory program should show changes in the *space of available distinctions* BEFORE a fully articulated target theory, not just retroactive logical expressibility (Steinle candidate).
- A research vocabulary can grow in some directions and lose old puzzles in others, rather than monotone additive accumulation (Kuhn loss candidate).
- The dissemination/translation of techniques should affect uptake of concepts across laboratories or disciplinary groups, even where a theory's equations remain fixed (Secord candidate).
- For possible alien sciences, lack of paired world-contact may block identification despite matching marginal statistics; explicit shared-action bootstrap may alter that conclusion (toy illustration).

Strong objections:
1. Steinle + Secord + late Kuhn may already explain virtually everything claimed here; then MQR's contribution is a clear synthesis with independently tested bridge contracts, not a new philosophical mechanism.
2. Historical chronologies may reveal that the allegedly 'new' experimental question was already explicit before an alleged conceptual turning point.
3. The toy two-sensor comparison grants a common latent world only to the external analyst; actual practical agents have no guarantee even that ontology.
4. A symbolic question-set or finite partition model does not capture the full phenomenology of historical instrument skill or tacit knowledge.

## 5. Next steps
A. Read and compare Faraday's two differently titled 1852 works at reliable edition/page granularity, with earlier 1821/1831 context, rather than project the later field formalism backward.
B. Consult Steinle (2016) and Gooding when possible for historical verification; note that Steinle (2002) Drive fetch returned **empty extracted text**, not proof of a missing PDF or its content.
C. Use Kuhn's original sources rather than exclusively SEP in a prospective dated conceptual-change case.
D. Freeze before/after questions and experimental capabilities; separately score GAIN, LOSS, REFORM and UNSPECIFIABLE. Maintain source provenance per claim.
E. Run committed exact tests in a proper local/CI environment; no CI is claimed from writing the file.

**Decision:** the unpaired-coupling result is mathematically verified by analytical derivation; the full Python file was committed but its execution has not yet been witnessed. Direct reading of Steinle 1997 and Secord 2004 accomplished; historical experiment/primary Faraday chronology verification remains HOLD. MQR 5.4 OPEN. Do not allow another finite partition toy to displace the historical and structural founding problem.
