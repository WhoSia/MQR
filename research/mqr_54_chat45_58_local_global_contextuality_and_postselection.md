# MQR 5.4 · Chat 45 · R58 — Locally compatible measurement contexts without a global joint model

**2026-11-23 KST; R57 continuation. Status: OPEN / SYNTHETIC EXACT / HISTORICAL PRIOR ART.**
Code: [mqr45_r58_contextuality_exact.py](../language/real/experiments/mqr45_r58_contextuality_exact.py). A matching algorithm was executed in Python and passed all assertions; the GitHub file was committed directly through authenticated user credentials (not GitHub Actions).

## Mathematical object (standard CHSH/PR-box witness)
For settings x,y∈{0,1}, outcomes a,b∈{−1,+1}, define p(a,b|x,y)=1/2 when ab=(−1)^(xy) and 0 otherwise. All four context-level distributions are normalized. Local marginals are uniform and do not depend on the remote setting (no-signalling), so pairs agree on their *overlaps*. Their correlations are E00=E01=E10=+1, E11=−1; S=E00+E01+E10−E11=4.

For any global deterministic assignment (a0,a1,b0,b1) there are exactly two values per variable and the CHSH value is ±2. More directly, imposing all four PR support constraints gives +1 from multiplying squared variable products on the left but −1 on the right. Hence **no global joint probability distribution** over fixed, setting-independent outcomes can extend all four PR pair tables. Convex mixtures of such global deterministic assignments still satisfy |S|≤2. Code exhaustively checks 16 assignments.

This is a *strong contextuality* witness, not an observed quantum experiment. The PR box reaches an algebraic/no-signalling upper bound 4 and exceeds the quantum Tsirelson bound 2√2. The original framework is Bell/CHSH, the superquantum-box comparator is Popescu–Rohrlich (1994), and the global-section language is Abramsky–Brandenburger (2011), directly read in held Drive PDF `1QMYaqy7naNJj43-M9zbBMZJ2AaVv5I2y`. MQR has **not** proved any new theorem here.

## Research consequence distinct from MQR44 R44–R48
Earlier MQR44 asked whether two marginal datasets can be joined at the specimen level, under reliable linkage and nondisturbing measurement. Here *each compatible measurement context has a perfect, already joint distribution*, yet an encompassing counterfactual joint distribution need not exist. The obstacle is not missing pairing IDs. The additional question is whether local measurement-context data admit a single noncontextual/global realization; the relevant mathematical structure, not merely sensor quality, defines a new experimental contrast.

## Incremental noise
Let q_eta=(1−eta)PR + eta×uniform, eta∈[0,1]. Then S(q_eta)=4(1−eta). Exact tests at eta=0,1/4,1/2,3/4,1 pass. Local bound violation occurs iff eta<1/2. **Exceeding CHSH 2 does not by itself certify quantum realizability**; at eta=0 the PR model is not quantum. Likewise, passing CHSH 2 is not a unique physical explanation.

## Adversarial postselection counterexample
Uniformly sample the 16 classical deterministic global assignments: unfiltered E_xy=0, S=0. Retain an event in each chosen setting context only if its observed product ab equals the PR target (−1)^(xy). Exactly 8 of 16 assignments survive per context; their conditional pair tables become exactly PR and S=4, with balanced marginals. Thus a **joint settings-and-outcomes dependent retrospective selection** can manufacture the full pattern in an underlying local table. This filter requires access to both outcomes and settings: it is deliberately *not claimed to be an implementable independent local detector rule*, nor a model of a particular real Bell experiment. It does show that sample selection and coincidence protocols are constitutive assumptions of an inference. Settings-INDEPENDENT filtering of global hidden assignments preserves the |S|≤2 bound.

## Literature/gates
Bell (1964) DOI 10.1103/PhysicsPhysiqueFizika.1.195; CHSH (1969) DOI 10.1103/PhysRevLett.23.880; Freedman–Clauser (1972) DOI 10.1103/PhysRevLett.28.938; Popescu & Rohrlich (1994), *Foundations of Physics* 24:379–385; Abramsky & Brandenburger (2011), arXiv:1102.0264, held readable PDF. **Citation-genealogy transfer none; no new Harvest number.**

**Verdict:** R58 is a severe exact comparator of what mathematics can make askable, *not* sufficient proof of physical novelty, history of actors' questions, or an original philosophy of nonlocality. AUTHORITY TRANSFERRED = NONE.