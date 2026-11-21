# MQR 5.4 · MQR 44 · Record 08 — A small epistemic community: signal count is not evidence count

**Date:** 2026-11-22 KST. Phase 5.4 OPEN. Claim class: exact Bayesian toy demonstration + primary paper comparison; not evidence about particular student groups, institutions, or actual researchers.

## 1. Problem and prior art
The user's prompt asks for epistemically meaningful analogies among small societies, interviews and science under limited information. A scientific community's reports are sometimes correlated through shared original sources, imitation, reputation and institutional selection. The canonical relevant prior art includes:
- Zollman (2007), 'The Communication Structure of Epistemic Communities', *Philosophy of Science* 74(5), 574–587. https://doi.org/10.1086/525605; distinguishes communication structure from speed/reliability of convergence.
- Zollman (2010), 'The Epistemic Benefit of Transient Diversity', *Erkenntnis* 72, 17–35, https://doi.org/10.1007/s10670-009-9194-6 (check edition/pagination before direct quote). Transient rather than permanent diversity is important.
- Secord (2004), 'Knowledge in Transit', *Isis* 95(4), 654–672, previously fetched held PDF `1Y0N6ke4RCf6iDw7pl9S34jgwcI9VjBYt`. Knowledge circulation should be understood as an actual process, not a mere duplication of stored propositions.
- MQR doctrine 4.X: evidential **noncommon failure ancestry** matters more than nominal count of instruments/reports.

## 2. Exact Bayesian demonstration: four reports from one origin
Hidden binary proposition H with equal priors. One source reports the truth correctly with reliability p=3/4, errors symmetrically. Its positive report yields posterior P(H=1|+) = 3/4. Now four agents forward precisely the SAME source report; forwarded signals have one stochastic ancestor. Correct posterior, conditional on observing four identical forwarded + signals with known shared origin, stays **3/4**.

If an analyst wrongly treats those forwarded messages as four conditionally independent measurements of reliability 3/4, likelihood ratio is (3)^4 = 81, giving false posterior **81/82 = 0.987804878...**.

The false confidence error is 81/82 - 3/4 = 39/164 (~0.2378). This is algebra, not a measured bias in human groups. Under *genuinely independent* measurement errors, posterior 81/82 is in fact correct. The counterexample attacks a violated ancestry assumption, not Bayesian inference.

Exact-fraction `correlated_reports_posteriors` in [code](../language/real/experiments/mqr_inquiry_frontier_v54.py), with [7 locally executed regressions](../language/real/experiments/test_mqr_inquiry_frontier_v54.py), including n=1,4,8.

## 3. Counterargument: independence is not the only route to information
Even when each observer consults one common source, independent checks of different predictions can multiply information if their conditional errors are not perfectly correlated. Conversely differently titled papers may all descend from the same flawed experiment or a shared miscalibration. Therefore:
- The count of *people, messages or distinct author names* is not the number of independent information sources.
- Independence must be typed at the proposition, failure mechanism, protocol, dataset and reference-standard levels.
- More connections can be helpful when the transmitted item is a new independent test; sparse connections can be harmful when refutations are delayed.
- 'Dense communities are bad' and 'isolation promotes genius' are unsupported simplifications.

## 4. Structural link to question-genesis
A community's epistemic structure is not only a graph G of who forwards data to whom. It also contains a graph of **which experiment or question a report makes feasible**. For instance, distribution of an instrument calibration procedure may create new *shared experiments* even if it adds no independent observation. That kind of communication changes the repertoire I and recognized questions Q; it cannot be scored merely by effective sample size.

We propose two different network layers:
- E-layer: ancestral evidence production and transmission; provenance and error conditional dependence.
- Q-layer: diffusion of skills, experimental procedures, question templates, and admissibility standards.

The same edge can be redundant for E but generative for Q. Conversely transmission of a high-confidence answer without its procedure can produce apparent evidence convergence while shrinking Q-layer exploration. This is the central falsifiable comparative hypothesis, not a theorem of epistemic network science.

## 5. Strong rival and proposed empirical checks
A rival social-network epistemology model already carrying distinct information and method-diffusion edges might explain all proposed phenomena. If so MQR contributes integration with possible-sciences bridge contracts, not discovery of a new mechanism.
For historical validation:
1. Trace two independently dated scientific communications back to their data ancestry.
2. Log whether the message transmitted a new *result*, an executable *method*, or a changed *problem standard*.
3. Before viewing later outcomes, predict which recipients gained new testable questions and which received merely copied evidence.
4. Compare with a rival model using only group connectivity or raw report count.
5. Establish negative cases: valid open communication with independent evidence improved inquiry; sparse dialogue preserved a false line of work.

**Status:** exact posterior example PASS and 7 code tests locally PASS; source-specific historical network case and causal claims HOLD. Keep MQR 5.4.
