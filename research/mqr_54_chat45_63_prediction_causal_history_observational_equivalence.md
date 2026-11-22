# MQR 5.4 · Chat45 R63 — Same theory/experiment chronology, different causal histories

**2026-11-23 KST; exact synthetic SCM; distinct from R62 historical evidence.** No historical empirical data are estimated and no novel causal theorem claimed.

## Historical inference under challenge
Suppose the chronology records a theory's prediction P, an experimenter's research action A, a matching observation D, and an interpretation I. Even if theory and observation fit, it does not follow that P caused A. That historical claim concerns the **counterfactual**: if the prediction had not been published/communicated, would the scientist have performed the same research action?

## Two binary causal models
Let exogenous U~Bernoulli(1/2). Variables P,A,D,I are binary; P=U, D=A, I=P*D. Two models differ only in the equation for A:
- **Guided model G:** A=P; P is an actual cause of action.
- **Shared-context model H:** A=U; U (common environment, problem salience, institutions, or techniques) explains why theoretical prediction and experimental action covary, without P causing A.

Both models generate exactly the same **observational** joint distribution:
- (P,A,D,I)=(0,0,0,0) with probability 1/2
- (P,A,D,I)=(1,1,1,1) with probability 1/2.

However, under an idealized `do(P=1)`, model G yields E[A]=1 while model H yields E[A]=1/2. The causal contrast E[A|do(P=1)]−E[A|do(P=0)] is **1** in G and **0** in H. The probabilistic calculation is exact and was independently rechecked with fractions, but committed Python source itself has no full CI receipt this session: [source](../language/real/experiments/mqr45_r63_prediction_discovery_causal_equivalence.py).

This is an illustrative **observational equivalence / causal non-identification** construction already within standard structural causal model theory; NOT an original principle, nor a reconstruction of a literal historical intervention that could be performed on Dirac/Anderson.

## Link to R62 and scope discipline
- Dirac (1928 equation, 1931 anti-electron interpretation) preceded Anderson's 1932 identification of positively charged electron-mass tracks. Anderson himself described his discovery as accidental and not caused by the prediction; review [APS Physics history](https://physics.aps.org/story/v17/st5) and [NAS mediated testimony](https://www.nationalacademies.org/read/10371/chapter/4).
- Thus actual history gives independent testimony to favor an unguided *research-action* pathway despite retrospective predictive fit, but does NOT quantitatively fit either synthetic model above.
- Maxwell/Hertz and Bell/CHSH/Freedman–Clauser may reflect more explicitly theory-guided experimental design. Their documentary chain must be judged independently, not inferred from chronology alone.

## Strongest falsifier of MQR's excessive claims
A putatively "mathematics-generated" empirical discovery that scientists would have made under unchanged practical research policies and apparatus even without seeing the prediction fails the **direct-guidance** claim. It may still pass **theoretical anticipation** and **later confirmation**. These are distinct epistemic achievements.

## Required historical protocol
Do not use the same 'successful prediction' citation to prove all of: interpretation of a formalism, formulation of a target experiment, experimenter's prior awareness, causal dependence of design on theory, laboratory observation, and later community identification. Record each as a distinct evidentiary witness with date and source.

**Result:** conditional methodological synthesis, no experimentally demonstrated novel MQR theory. 5.4 OPEN. AUTHORITY TRANSFERRED NONE.