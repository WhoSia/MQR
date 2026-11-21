# MQR 5.4 · MQR 44 · Record 22 — Institutional competition may increase risky inquiry yet lower expected epistemic return

**2026-11-22 KST.** Critical negative-control research unit using original source comparison and an exact synthetic payoff game (run in local Python, PASS). Not an empirical admissions, journal or scientific-policy estimate. MQR 5.4 OPEN.

## 1. Newly inspected relevant empirical/formal literature (with edition verification)
- **Avin**, *Centralized Funding and Epistemic Exploration*, final journal **BJPS 70(3), September 2019, pp.629–656**, DOI 10.1093/bjps/axx059, publisher https://academic.oup.com/bjps/article-abstract/70/3/629/4675327 . A held 2017 copyright/2018 advance-manuscript is available Drive `1h7KkdSpY_0WBL9tdaYb01oBVQYG_2JkG`, directly read. Earlier R21 noted final publication date unresolved: it is now verified as **2019 issue**. Under modeled *large epistemic landscapes*, some random grant allocation can outperform peer review; context matters.
- **Gross & Bergstrom**, 'How competition propels scientific risk-taking', dated Sep 9 2025 in held manuscript `1aneV_8fwwVnu0lWtCcJUyF_v_z6QZpWI`, arXiv https://arxiv.org/abs/2509.06718 ; formal competition can increase high-risk project uptake, countering naive 'institutional selectivity always conservatizes' slogans. No final journal venue assumed.
- **Gross & Bergstrom (2024)**, *Rationalizing risk aversion in science: Why incentives to work hard clash with incentives to take risks*, *PLOS Biology* 22, DOI 10.1371/journal.pbio.3002750, https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002750 . Distinct paper and mechanism; avoid merging with 2025 preprint.
- **Gross & Bergstrom** *Why ex post peer review encourages high-risk research while ex ante review discourages it*, PubMed https://pubmed.ncbi.nlm.nih.gov/34921115/. Its framing itself shows that **timing and target of evaluation** can change incentive direction; specific mechanisms require full reading before claiming strong derivations.

## 2. A small theorem-like countermodel to another simplistic MQR slogan
Consider one investigator choosing:
- **Safe:** certain epistemic yield score 1.
- **Risky:** yield score 3 with probability 1/4, else 0, thus expected epistemic yield = 3/4, *less than safe*.
An external fixed comparator has score 2, and a tournament reward prize V>0 goes only to a researcher who exceeds this comparator. Safe never exceeds 2. Risky exceeds it with probability 1/4. If investigator's objective is own expected epistemic yield PLUS prize value:
  U_safe(V)=1,
  U_risky(V)=3/4+V/4.
The investigator favors risky iff V>1, is indifferent at V=1, and favors safe iff V<1.

At prize V=2, the investigator rationally chooses risky, with utility 5/4 versus safe's 1; however the expected epistemic yield falls from 1 to 3/4. **Risk-taking, apparent individual success incentives and expected collective knowledge cannot be equated.** This reverses any simplistic proposal 'more risky research means more expected world knowledge'. The game is a deliberately stark construction with a fixed rival benchmark, no individual effort, no learning spillovers, no real prize monetary conversion and no empirical parameter estimates.

Exact rational code `language/real/experiments/mqr_institutional_risk_selection_v54.py`, locally executed PASS. No claim of replicating any paper's actual contest equilibrium.

## 3. Precise relevance to MQR's limited-information science
The user's link between admission interviews, small societies and science can be valid only at a careful **epistemic selection** abstraction:
  SELECTION_PERSON -> which agents can participate,
  SELECTION_QUESTION -> which projects are funded/recognized,
  SELECTION_EVIDENCE -> which experimental outcomes are sampled/publicized.

A competition can increase risky research proposals yet not increase the creation of new questions, independent observations, model accuracy or eventual generalizability. 'Novelty' may be an evaluation label, not a physical new observable. Even an open evaluation process may reward attention-grabbing false positives.

Conversely some competitive incentives may really prevent excessive conformity and produce transformative discoveries. We need actual counterfactual outcome data, not global institutional morality stories.

## 4. Dual evaluation principle and its possible failure
**Research conjecture:** when assessing whether an institution permits 'science to flourish' under constraints, report two distinct outcomes:
(A) contemporaneous personal/institutional payoff relative to its explicit selection rule;
(B) independent epistemic benefit (discriminating observations, replicable new methods, accepted valid conceptual distinctions, domain-general predictive competence).
These can diverge. A third axis concerns distributive fairness and social legitimacy; it cannot be reduced to the scientific truth measure. The two-axis evaluation is familiar to incentives research and decision theory; MQR's potential usefulness is integrating it with historical question invention, not priority of a universal theorem.

Strong objections:
- Some social epistemic value is created by risky projects' option value and method innovation even when the immediate average yield is lower; our one-shot toy omits this.
- A fixed 2-point rival is an artificial tournament; symmetric multi-agent equilibrium, selection into contests and effort choice are crucial in actual Gross/Bergstrom models.
- 'Expected knowledge yield' is itself not a universal scalar validated by empirical science; this thought experiment uses a declared numerical reward.
- Without pre-registered real institutional outcome measures, this is at best a boundary-case illustration.

## 5. Source-backed decision
Institutional scarcity can simultaneously *support* risky novel attempts and *distort* which outcomes appear prestigious. Restrict claims to each institutional design, not 'competitive societies are scientifically superior' or its inverse. Next differentiating study: historical/multilaboratory case with dated method invention, truly distinct underlying evidence ancestries and documented dissemination to outsiders. Faraday–Hachette–Ampère 1821 letters currently give apparatus transfer and physical reproduction, not quantified population/contest incentives.

**Status:** source cross-read + publisher date verification PASS; one-shot exact calculation PASS; real-world incentive causal effect HOLD; MQR 5.4 OPEN.
