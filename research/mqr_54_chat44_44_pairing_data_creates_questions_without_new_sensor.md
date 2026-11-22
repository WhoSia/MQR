# MQR 5.4 · MQR 44 · R44 — Pairing experimental records creates a new testable question; pairing alone does not establish causality

**2026-11-23 KST** · High-priority exact MQR thought experiment, tested locally using Python standard library and `fractions.Fraction`: `PASS: unpaired rank=3, paired rank=4, parity unidentifiable before pairing; causal intervention still needed`. MQR 5.4 OPEN.

## 1. The invention that matters is not a better sensor: it is a linkage capability
World has two binary quantities A and B on each unit, four possible (A,B) states. Two communities separately study **A** and **B** on randomly sampled but **unpaired** units, and each can measure its own variable perfectly.

Possible worlds:
- W+ : P(0,0)=P(1,1)=1/2; A and B agree on every unit.
- W− : P(0,1)=P(1,0)=1/2; A and B disagree on every unit.

Both communities see exactly **P(A=1)=P(B=1)=1/2** in either world; the two full collections of unpaired marginal measurements remain observationally indistinguishable under any sample size (assuming independent random samples and no metadata that implicitly pairs units).

**New capability:** retain reliable common specimen IDs, paired measurements and stable provenance so each unit has both A and B. Now the test `P(A XOR B=1)` distinguishes W+: 0 and W−:1. Importantly, no novel sensor or unknown physical variable was added; instead **measurement records became combinable across experimental practices**. This is a positive counterexample to simplistic 'new scientific questions always require a new physical sensor'.

## 2. The space of identifiable linear questions actually changes dimension
Order four joint states as (0,0),(0,1),(1,0),(1,1). Prior to pairing, available linear expectations are functions of normalization, A-marginal and B-marginal:
  (1,1,1,1); 1[A=1]=(0,0,1,1); 1[B=1]=(0,1,0,1).
Their exact rank over Q is **3**. The parity function 1[A≠B]=(0,1,1,0) is not in that span, and adding it raises exact rank to **4**. Paired data resolve four elementary joint outcomes (subject to normalization), so can estimate every function of (A,B), including parity.

Do not misunderstand rank=3 as 'three independent degrees of freedom in a normalized probability table': normalization is a linear constraint with fixed value 1, so **two free marginal parameters** remain before pairing; the four-cell distribution has **three free parameters** after pairing. The third added parameter is their association. Measurable *function span* rank increases 3→4.

The proof of nonidentification is not just dimension counting: W+ and W− are exact observational counterexamples with equal marginals and opposite parity. The exact rank calculation is a consistency check.

## 3. The second level: full paired observation is still insufficient to identify causality
Now fix the joint observational law W+ (A=B=U where U fair), and compare two causal models:
- F (fork): U→A and U→B independently through deterministic copying; `do(A=1)` leaves B fair.
- C (chain): U→A→B, B copies A; `do(A=1)` makes B=1 with certainty.

Both agree on the **entire paired joint distribution**. Under a well-defined intervention only on A, they predict `P(B=1|do(A=1))=1/2` versus `1`. Thus pairing upgrades question access from marginals to association, **not** automatically to causal-direction discovery. Only an actual selective and validly bound intervention (or other identifying assumptions) can separate these causal models. No human experimentation is requested or performed.

## 4. A bounded possibility for plural sciences
Imagine an A-specialist community and a B-specialist community with distinct instruments and vocabularies. They need **not** first obtain a bijective dictionary between all concepts. A common specimen indexing/measurement provenance practice can produce jointly accessible relational questions, and comparison of coupled outcomes may create a new question that neither isolated evidential archive could answer.

But *being newly answerable* does **not** mean the parity question was logically inexpressible to all researchers before pairing: a mathematician with both variable names could write it beforehand. We therefore must differentiate:
- **logical expressibility**: the question has a grammatical meaning;
- **empirical identifiability**: available experimental distributions determine the answer;
- **historical accessibility**: agents actually possessed instruments, labels, methods and coordination to run it;
- **causal authority**: intervention assumptions are justified.

MQR's experimentally meaningful claim is the second/third; it must not illegitimately substitute the fourth or stronger metaphysical novelty.

## 5. Research tradition and rival
This is *not* a new mathematical result. It is elementary identifiability of contingency tables and conventional causal-graph interventional identification. It also resembles source-aware multi-instrument data integration. The philosophical value is making an 'epistemic bridge' conditional on **pairing/provenance** instead of merely sharing reports. A strong rival is that existing causal/measurement statistics and data integration theory suffice entirely. If no additional historical prediction comes from MQR, treat this as clarified integration, not priority for a new general theory.

## 6. Exact status and implementation
- Source: `language/real/experiments/mqr_pairing_questions_v54.py`, 4-state exact model, Gaussian elimination over rationals, observational source identity, fork/chain causal intervention countercase.
- Local code PASS, exact assertions. No new material acquisition. No automatic assignment of actual Faraday, implicit memory or RNA states to these four abstract worlds.
- Next: test **measurement alignment uncertainty**, sample selection and unequal costs. Or seek historical multi-instrument datasets where paired IDs make a genuinely new result possible, with independent empirical documentation.
