# MQR 5.4 · MQR 44 · R46 — A little unreliable alignment can destroy identifiability

**2026-11-23 KST** · Exact rational synthetic counterexperiment, script `language/real/experiments/mqr_noisy_pairing_v54.py` executed locally and PASS. This is standard statistics of mislinked records and measurement error; no novelty claim, no actual clinical or laboratory data. MQR 5.4 OPEN.

## 1. Increase complexity by precisely one realistic assumption
R44 supposed matched observations of A and B on the **same unit**. Now suppose a recorded pair is correct with probability p, while an incorrect pairing attaches an **independent unit's** B measurement. Take both A and B individually balanced (P=1/2). The actual joint relationship can be represented by agreement bias
  r=P(A=B)-P(A≠B), so -1≤r≤1.
For correctly paired records, P(A≠B)=(1-r)/2. Random cross-unit mispairing yields parity P(A≠B)=1/2. By total probability,
  q=P(observed A≠observed B) = p(1-r)/2 +(1-p)/2 = (1-pr)/2.

**This exact equation changes the philosophical outcome**: observed paired distributions identify only the PRODUCT pr if both pairing accuracy p and scientific association r are unknown. As a concrete witness, `p=1/2,r=1` (perfect association, unreliable pairing) and `p=1,r=1/2` (weaker association, perfect pairing) both give q=1/4 and, because both marginals remain balanced, the **same complete observed two-by-two table**.

Thus even collecting an unlimited number of mislabeled joint rows cannot in principle distinguish these two situations without independent linkage calibration or additional justified assumptions.

## 2. Positive recovery and fragility
If correct-pairing probability p is **known** from independently established provenance and positive,
  r=(1-2q)/p.
As p→0, the same error in observed q gets multiplied by 2/p in inferred r; uncertainty is amplified. At p=0, every actual r yields q=1/2, so linkage carries no association information.

For the two extreme worlds r=±1, q differs from 1/2 by p/2. With n independent paired records, calibrated p and correctly specified symmetric model, a threshold-at-1/2 binary classifier has Hoeffding one-sided error bound
  Pr(error)≤exp(-n p²/2).
At n=100,p=1/2 the bound is exp(-12.5)≈3.73×10^-6. It is a **bound for this stark model under iid sampling and known p**, not a universal real-data guarantee. If errors correlate, background marginals differ, or mispairing is selective, the formula and bound may fail.

## 3. A fourth level in the thought experiment sequence
R44:
 (i) separate tests ⇒ identical marginals can mask opposite joint structure;
 (ii) paired tests ⇒ exact parity becomes identifiable;
 (iii) full joint statistics ⇒ causal fork and chain remain observationally identical;
 (iv) intervention on A ⇒ differ, assuming a valid target-specific manipulation.

R46 inserts a necessary **evidence-ancestry and linkage-calibration gate** between (ii) and (iii). A nominal shared identifier is not an infallible coupling map. A scientific bridge is therefore not achieved by a bilingual dictionary, instrument shipment or matched spreadsheet alone. We need independent proof the observations belong to the same target *in the sense relevant to the question*.

## 4. Relation to original philosophical sources (not new mathematics)
The concern is consistent with Mitchell's multi-perspective integration (2023), Feest's converging operations, Campbell–Fiske's multitrait-multimethod discriminant validity, and research data provenance theory. In heterogeneous scientific communities, a sample identifier, calibration convention or ontology alignment may require as much justification as the instrument itself. Unlike R17's deterministic quotient, these bridges lose reliability gradually and the lost information may be non-identifiable without an anchor.

## 5. Falsifying and opposing evidence
- If identical paired measurements can be recovered with a separately calibrated p=1, this particular failure disappears (not all theory differences).
- If cross-laboratory shared labels index genuinely different biological individuals / episodes, the 'joint' target is ill-defined; reject the model, don't invent r.
- If random mispairing is replaced by known systematic mispairing that preserves a predictable relation, p alone is insufficient: require the **full pairing kernel**.
- If datasets are independently sampled from non-equivalent populations, observed marginals may not correspond to a single shared world distribution; provenance alone cannot establish exchangeability.

## 6. Exact source status
Script has exact `Fraction` checks for observational equivalence `(p,r)=(1/2,1)` and `(1,1/2)`, p=0 degeneracy, calibrated inverse, and numeric bound. Local PASS. No source PDF acquisition or new 'missing' group. The mechanism is a constructed illustration, not proof of a real case in Faraday, memory, or RNA. MQR 5.4 OPEN.
