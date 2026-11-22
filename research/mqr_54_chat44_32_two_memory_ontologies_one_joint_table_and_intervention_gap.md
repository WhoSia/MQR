# MQR 5.4 · MQR 44 · R32 — Two equal test tables, two causal ontologies, different intervention forecasts

**2026-11-22 KST.** Original didactic finite countermodel using exact fractions, executed locally PASS prior to GitHub commit. This is ordinary causal identification / latent-variable measurement underdetermination, not a new theorem and **not** a model fitted to any real cognitive, neurological, clinical or admissions data. Theory version 5.4 OPEN.

## 1. Goal and direct prior art
The 1981 Jacoby/Dallas, 1985 Graf/Schacter and 1990 Roediger studies in R31 show that interpreting different memory-task patterns as unique memory systems is a live scientific inference problem. Feest (2010), Campbell–Fiske (1959) and Kane (2013) already warn that tasks, constructs and mechanism interpretations must be separated. To force MQR's own rationale to face a hostile test, construct two distinct causal models making **exactly the same FULL paired observable distribution**, not just the same marginal success rates, then specify an intervention that separates them. This is an illustrative measurement-identification failure, not a reconstruction of the human memory experiments.

## 2. Model S: one common memory mechanism
Latent H is Bernoulli(1/2). Two task outcomes A and B independently equal H with probability 3/4 each conditional on H; symmetric flips otherwise. Exact full observational distribution:
   p(A,B) = 5/16 for (0,0) and (1,1); 3/16 for (0,1) and (1,0).
Each marginal is 1/2; Cov(A,B)=1/16 and Corr(A,B)=1/4.

## 3. Model M: two independent memory mechanisms, a shared method nuisance
Latents M_A, M_B and C (task/context factor) are mutually independent fair bits. Each test independently chooses with probability 1/2 whether to report its OWN memory bit (M_A for task A, M_B for task B) or the common method factor C. These method-choice random switches are independent. This alternative model also produces **exactly the same four cells** (5/16,3/16,3/16,5/16), marginal means 1/2, and correlation 1/4. Observing a whole infinite population of just the joint A,B table, even with zero measurement error in frequency estimation, cannot distinguish these two specified generative mechanisms.

## 4. A precisely scoped counterfactual that DOES distinguish
Under a hypothetical intervention that fixes H=1 in S (without changing measurement errors), both A and B have probability 3/4 of 1. Under an intervention that fixes **only M_A=1** in M (keeping independent M_B,C and switches unchanged), A has probability 3/4 but B remains 1/2. This separates the two **intervention models**:
   S: do(H=1) -> (P(A=1),P(B=1))=(3/4,3/4)
   M: do(M_A=1) -> (P(A=1),P(B=1))=(3/4,1/2).
But the interventions target differently defined latent variables, so the calculation does not show a physically available uniform manipulation! An experimental researcher must find a justified operational intervention with comparable and independently verified target binding. Without it, the causal comparison remains a theoretical prediction with **untested** intervention evaluability, not a real refutation.

## 5. Critical epistemic consequence
A task correlation, a task dissociation or even a complete joint score table does not automatically identify a unique causal ontology. Stronger measurements, within-person interventions, independent measurement procedures and the explicit causal link from operation to construct are required to discriminate the rival mechanisms.

The counterexample is a severe rival to any MQR implication that 'new executable question -> new uniquely identified scientific object'. It also shows why an observational bridge and an intervention bridge have genuinely separate authority contracts (MQR44 R04, R17–R18): both models can agree on ordinary observable output and nevertheless disagree on the consequences of a justifiably targeted action.

## 6. Exact code and validation scope
[Exact executable](../language/real/experiments/mqr_memory_latent_nonidentifiability_v54.py) enumerates all 2^3 ancestral/noise worlds in S and 2^5 worlds in M with rational probabilities; both full distributions match exactly and the stated do-latent queries differ. Local Python result:
`PASS: matched 4-cell observational distribution; intervention changes both vs only A`.
This code does **not** reproduce Graf–Schacter participants, Jacoby's original experiments, or a clinical amnesia model; no fitted parameters or inferential significance claims are involved.

## 7. Historical test and stopping gate
To apply this diagnostic to original psychological research, first obtain exact original methods and manipulations, identify which task components/memory effects are targeted, check whether control manipulations isolate a unique latent component and exclude confounding/context explanations, and then compare held-out task/encoding results. The same principle should be applied to Faraday/Ampère 1821: observed rotation agreement does not uniquely identify microscopic currents without an operationally discriminating experiment. A bare analogy is insufficient to establish identical historical causal graphs.

**PASS:** exact synthetic observational equivalence and rival interventional predictions; provenance of held scholarship and public original primary bibliographic abstracts. **HOLD:** realistic manipulation of latent states, empirical external validity and novel natural kind. Keep 5.4 OPEN.
