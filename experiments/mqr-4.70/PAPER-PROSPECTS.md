# MQR-4.70 — Publication Claim Matrix

Status: **DRAFT / CLAIMS NOT YET EARNED**

## Candidate titles

1. **When Is a Scientific State Minimal? Intervention-Relative Predictive Quotients, Exterior Separators, and the Constitution of Scientific Tests**
2. **Minimal Relative to Which Experiments? Scientific State Compression under Open Intervention Families**

## Central question

A predictive state is minimal only relative to a set of future tests.

What authority does that minimality have when the test set is incomplete, selected by the current model, costly, restricted, historically generated, or nontransportable across domains?

## Formal results to pursue

A. **Family-refinement monotonicity**  
For fixed response semantics, U subseteq V implies P(V) refines P(U).  
Expected status: elementary baseline.

B. **Separating-hypergraph characterization**  
A family distinguishes a required history pair iff it intersects that pair's separator set. A family realizes a declared target distinction set iff it intersects every required separator set.  
Expected status: classical combinatorial baseline.

C. **Minimal-family nonuniqueness**  
Distinct incomparable minimal families can induce the same predictive partition.  
Expected status: finite constructive result.

D. **Endogenous self-sealing countermodel**  
A family selector conditioned only on the current quotient may preserve that quotient even though a frozen admissible exterior separator would refine it.  
Potential value: a precise connection between test selection and self-confirming scientific state compression.

E. **Transport-preservation condition**  
Cross-domain intervention transport preserves a source partition only when the transport preserves the relevant pairwise separation relation over the declared history correspondence.

F. **Open-world minimality ceiling**  
Finite family-relative minimality does not entail minimality over an open class of future interventions without an independently warranted closure condition.

## Naturalistic program

Potential domains:
- causal intervention design;
- systems-biology experiment design;
- adaptive scientific protocols;
- computational workflow audit;
- active automata learning as an exact control domain.

A strong study should prefer depth over domain count:
- one formal control domain with exact ground truth;
- two scientific domains with genuine intervention constraints;
- one cross-domain transport demonstration.

## Figure plan

Figure 1 — Family-to-partition map: U0 subset U1 subset U2 mapped to predictive partitions.

Figure 2 — Separator hypergraph: history-pair distinction obligations and alternative minimal intervention families.

Figure 3 — Endogenous selector: current quotient -> selected family -> no refinement, versus frozen exterior separator -> refinement.

Figure 4 — Cross-domain transport square: one separation-preserving case and one distinction-losing case.

Figure 5 — Authority ceiling:
LOCAL FAMILY-RELATIVE MINIMALITY -> FINITE-UNIVERSE MINIMALITY -> OPEN-WORLD HOLD.

## Claim discipline

The study must not present the following as novel:
- partition refinement under added tests;
- hitting-set or set-cover reduction;
- active experimental design;
- predictive-state or causal-state construction;
- generic path dependence.

Potentially distinctive contribution:
- a unified constitutional analysis of how scientific state compression inherits limits from the admitted intervention family;
- prospective endogenous-selection countermodels;
- separation-preserving transport conditions;
- authority ceilings that separate finite test completeness from open scientific sufficiency;
- executable receipts that keep family-relative sufficiency separate from world validity.

## Required quality bar

Publication-ready status requires:
- independent implementations;
- finite proofs without outcome fitting;
- current literature comparison;
- naturalistic cases with source-level receipts;
- ablations showing which claims reduce to established baselines;
- explicit negative results alongside positive results.

A baseline-absorbed outcome remains scientifically useful if it identifies a sharp formal boundary that transfers beyond MQR.
