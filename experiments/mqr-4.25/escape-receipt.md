# MQR-4.25 — Minimal-Basis Adversarial Escape Search Receipt

Status: C–E–P NOT STABLE UNDER DELIBERATELY UNMODELED THREATS / SUCCESSOR DIMENSION ADMITTED

## Preseal
Commit:
7f3ac13ea5e41dec68365c8ef4b882a3704724b3

Frozen successor-dimension admission:
D1 concrete C=E=P=PASS counterexample;
D2 promotion should nevertheless HOLD;
D3 defect not reducible to C/E/P without semantic distortion;
D4 prospective operationalization;
D5 blocks counterexample while preserving valid cases;
D6 not merely another credential/provider/notary/identity lane.

## Adversarial threat census
1. Source-origin corruption with intact provenance
Classification:
ABSORBED_BY_E.
Reason:
A receipt is not an admissible world-contact receipt if the measured source is known to be corrupted relative to the declared measurement semantics.

2. Calibration / measurement-validity drift
Classification:
ABSORBED_BY_E when the instrument no longer validly measures the declared observable.
If the measurement is valid but the construct-level inference exceeds what the observable identifies, classification moves to R below.

3. Construct mismatch / semantic aliasing
Classification:
ABSORBED_BY_C when claim/observation ontology or scope is misconstituted.
GENUINE RISK TO R when multiple substantively distinct constructs remain observationally equivalent under a correctly constituted claim.

4. Adversarial environment manipulation
Classification:
ABSORBED_BY_E when it invalidates the authorized execution regime.
ABSORBED_BY_C when the promoted claim exceeds the authorized regime.

5. Collusion / common-mode dependence among nominally independent authorities
Classification:
ABSORBED_BY_C or P because independence/auditability is not genuinely satisfied.

6. Cryptographic trust-root compromise
Classification:
ABSORBED_BY_P.

7. Claim-scope laundering
Classification:
ABSORBED_BY_C and/or P because the promoted claim is not the constitutionally bound/auditable claim.

8. Causal overreach from non-causal world-contact
Classification:
GENUINE RISK TO R if C/E/P genuinely pass but observations do not identify the causal claim.

9. Hidden selection/censoring
Classification:
ABSORBED_BY_E if the execution/sample is inadmissible under the frozen sampling contract.
May induce R-failure when selection leaves multiple incompatible population claims observationally equivalent.

10. Evaluator incentives / nominal independence with substantive dependence
Classification:
ABSORBED_BY_C when constitutional independence is not genuine.

11. Underspecification / observational equivalence / omitted live rival
Classification:
GENUINE_OUT_OF_BASIS_CANDIDATE.

## Literature anchors
D'Amour et al., JMLR, "Underspecification Presents Challenges for Credibility in Modern Machine Learning":
multiple predictors can satisfy the same validation criterion yet behave differently in deployment; identical validation success does not uniquely determine the relevant behavior.

Dennis et al., "Errors in Statistical Inference Under Model Misspecification":
if compared models are misspecified, standard inferential procedures can produce misleading conclusions even as sample size grows.

Kline & Tamer, Annual Review of Economics, "Recent Developments in Partial Identification":
identification asks what can logically be learned from data plus assumptions; observationally equivalent parameter values cannot be distinguished by the observed data.

These support treating inferential identification as distinct from mere procedural provenance or execution integrity.

## Concrete out-of-basis counterexample
Workflow:
.github/workflows/mqr-4.25-counterexample.yml

Run:
35966976279

Commit:
56a1bab6072580ef56659872d446f0fb1dea6922

Claim domain:
x in {0,1,2}

Hypotheses:
H1(x)=x
H2(x)=1-x
H3(x)=x for x in {0,1}, H3(2)=0

Observed:
x=0 -> y=0
x=1 -> y=1

Frozen state:
C=PASS.
Independent constitutional authority genuinely approved H1-vs-H2 protocol and the broad claim domain.

E=PASS.
Authorized world-contact was executed correctly.
Observed outcomes match H1 and exclude H2.

P=PASS.
Assume complete, immutable provenance/time chain.

But:
H3 also matches every observation.
H1 and H3 diverge inside the authorized claim domain at x=2:
H1(2)=2
H3(2)=0

Machine output:
C=1 E=1 P=1 R=0
H1_FITS=True
H2_FITS=False
H3_FITS=True
CEP_PROMOTE=True
CEP_R_PROMOTE=False

Thus:
C∧E∧P can authorize an over-strong claim even though the claim is not identified.

## D1–D6 adjudication
D1 concrete C=E=P=PASS counterexample:
PASS.

D2 promotion should HOLD:
PASS.
The evidence licenses at most the observational equivalence class containing H1 and H3, not unique H1 authority over the full claim domain.

D3 non-reducibility:
PASS-NARROW.
- C answers who/what has authority to constitute and alter the protocol; it does not guarantee that the protocol point-identifies the scientific claim.
- E answers whether admissible world-contact occurred; it does not guarantee uniqueness of the explanation.
- P answers whether the evidence chain is auditable; it does not guarantee inferential separability.
Folding point-identification into C, E, or P would materially expand their frozen role semantics.

D4 prospective operationalization:
PASS.
A separate rival-separation gate was implemented.

D5 block counterexample while preserve valid cases:
PASS.

D6 not credential lane:
PASS.

## Operational R gate
Successor dimension:
R = claim-level rival separation / inferential identifiability.

Workflow:
.github/workflows/mqr-4.25-rival-gate.yml

Run:
35967088598

Commit:
b33eb0240ddff2c15bbc4c571ffda097d928938b

Case A:
observations {0:0,1:1}

Survivors:
H1,H3

Divergence:
H3 differs from H1 at x=2.

R:
HOLD.

Required contraction:
identified set = {H1,H3}.

Case B:
additional admissible world-contact x=2 -> y=2.

Survivors:
H1 only.

R:
PASS.

Machine receipts:
ambiguous_case_blocks=PASS
hidden_rival_found=PASS
identified_case_passes=PASS
hidden_rival_removed_by_new_world_contact=PASS
valid_prior_case_preserved=PASS
R_OPERATIONALIZATION=PASS

Thus R is not merely a veto label.
It is a prospective executable gate that contracts claims to the identified set or demands discriminating world-contact.

## External adversarial review
Factagora/Agora deep research independently judged that, with C/E/P genuinely passing, inferential non-identifiability is best treated as a distinct substantive identification/rival-separation requirement rather than as procedural failure.

However its returned source list contained several weak/off-topic items.
Therefore the external adjudication is retained only as diagnostic support, not as primary evidence.

Primary evidential support is:
- the presealed formal counterexample;
- executable rival-separation gate;
- high-quality underspecification/model-misspecification/partial-identification literature.

## Successor constitution
MQR-4.24 remains correct relative to the frozen three-variable authority language used there.

MQR-4.25 shows that this language omitted a scientifically independent failure mode.

Therefore:
C–E–P MINIMALITY = LOCALLY VALID BUT NOT ADVERSARIALLY STABLE.

Successor authority basis:
{C,E,P,R}

Successor law:
PROMOTE := C AND E AND P AND R

where R requires that the promoted claim be invariant across the surviving admissible rival/identified set, or else be contracted to that identified set until additional discriminating world-contact is obtained.

## Scope limit
R does not imply exhaustive enumeration of every logically possible hypothesis.
Its operational scope is relative to:
- the declared claim domain;
- the admissible rival generator/class;
- the available adversarial rival search;
- explicit identified-set semantics.

A future stage may attack R itself with rival-generator incompleteness.

## Verdict
ADVERSARIAL-ESCAPE-SEARCH-PASS /
MOST-THREAT-FAMILIES-ABSORBED-BY-CEP /
OUT-OF-BASIS-COUNTEREXAMPLE-FOUND /
C-PASS-E-PASS-P-PASS-R-FAIL-CONSTRUCTED /
INFERENTIAL-NONIDENTIFIABILITY-NOT-REDUCIBLE-TO-CEP-WITHOUT-SEMANTIC-DISTORTION /
RIVAL-SEPARATION-GATE-OPERATIONALIZED /
AMBIGUOUS-CLAIM-CONTRACTED-TO-IDENTIFIED-SET /
ADDITIONAL-WORLD-CONTACT-RESTORES-R /
D1-D6-SUCCESSOR-ADMISSION-PASS /
SUCCESSOR-DIMENSION-R-ADMITTED /
C-E-P-MINIMALITY-LOCALLY-VALID-BUT-NOT-ADVERSARIALLY-STABLE /
SUCCESSOR-BASIS-EQUALS-C-E-P-R /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
