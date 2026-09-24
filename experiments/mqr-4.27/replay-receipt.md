# MQR-4.27 — Historical Authority without Finality Replay Receipt

Status: CROSS-EPOCH REPLAY PASS / R-LANGUAGE v0.1 LIVE

## Preseal
Commit:
352fb3bac4f1c49c5500314e4dd9b9be3469db60

Hindsight firewall:
historical packets are scored only from evidence/method/rivals available at the packet epoch.
Later science enters only through SUCCESSOR_SHOCK and never retroactively raises an earlier TPX.

## R-Language live surface

Language constitution:
language/r/README.md
commit:
de8e2dc8b3522c4db9f05ad1504bc229af4d014b

Compiler:
language/r/rpacket.py
commit:
f869c9079a4d3f594c781391698a6a632751b7ee

Regression tests:
language/r/test_rpacket.py
commit:
60820ab2482f1cd0533fba54c3a7002cfa3555a6

Persistent CI:
.github/workflows/r-language-ci.yml
commit:
79fb361161439192b9feb34fc55a1adc723b811d

CI run:
35980481315

CI verdict:
R_LANGUAGE_V0_1=PASS
GATE_NONCOMPENSATION=PASS
HINDSIGHT_FIREWALL=PASS
OPEN_WORLD_RESIDUE=PASS

## R-Language semantics

Authority gates:
C = constitutional/adjudication legitimacy
E = admissible execution/world-contact
P = provenance/time/auditability
R = open-world rival invariance

Truth-Proximity Profile:
W = world resistance
N = noncommon route strength
I = rival invariance / identification
T = declared-scope transport
D = defeat exposure / corrigibility

Optional:
TPX = geometric_mean(W,N,I,T,D)

TPX is emitted only if C=E=P=R=PASS.

TPX is:
CURRENT_WORLD_CONSTRAINED_PROXIMITY_PROXY

TPX is not:
- P(claim=true)
- metaphysical truth distance
- final-theory similarity
- exhaustive-rival confidence

Every packet retains:
OPEN_WORLD_RESIDUE=true.

## Historical lineage A — Newton / Mercury

### Packet A1 — 1859 residual epoch
Packet:
language/r/examples/newton-mercury-1859.rpacket

Commit:
d3c374785efb7c28291be581b39f975126449f54

Claim:
Newtonian gravitation retains strong scoped authority for major planetary orbital constraints while Mercury's residual perihelion advance remains unresolved.

Important scope:
the packet explicitly excludes treating the Mercury residual as a solved Newtonian consequence.

TPP:
W=1.00
N=0.75
I=0.75
T=0.75
D=0.75

TPX:
0.794418

Band:
SCOPED_REALIST.

Residue:
Mercury perihelion anomaly remains HIGH.

Ontic reserve:
final/exhaustive Newtonian gravitational ontology = HOLD.

### Packet A2 — 1915 GR/Mercury
Packet:
language/r/examples/newton-gr-1915.rpacket

Commit:
3b4d0f4d8f6257d09387faff19f6fb2e77e01821

Claim:
general relativity accounts for Mercury's anomalous perihelion advance while recovering a Newtonian-like regime for weaker gravitational conditions.

TPP:
W=0.75
N=0.50
I=0.75
T=0.50
D=0.75

TPX:
0.637712

Band:
SCOPED_REALIST.

Interpretation:
The 1915 packet scores below the mature scoped 1859 Newtonian packet because later eclipse, pulsar, lensing, gravitational-wave and other evidence is barred by the hindsight firewall.

This is a positive result.

It demonstrates:
BETTER LATER THEORY != AUTOMATICALLY HIGHER HISTORICAL TPX AT FIRST INTRODUCTION.

MQR therefore separates:
- current evidence-backed authority;
- eventual historical survival;
- final truth.

Successor shock:
GR contracts Newtonian final-law authority while preserving a substantial weak-field constraint domain.

Historical authority verdict:
NEWTONIAN SUCCESS WAS NOT VACUOUS MERELY BECAUSE GR WAS FUTURE-UNCONCEIVED.

## Historical lineage B — Antarctic ozone

### Packet B1 — 1985 Halley
Packet:
language/r/examples/ozone-1985.rpacket

Commit:
824baaf9fbbf9d8551c0369f19614d50e41ce51f

Claim:
severe recurring springtime total-column ozone depletion over Halley is a real atmospheric phenomenon.

TPP:
W=0.75
N=0.50
I=0.75
T=0.25
D=0.75

TPX:
0.555161

Band:
LIMITED_SCOPED.

Why limited:
world resistance is already meaningful, but noncommon route strength and spatial transport are still restricted.

Mystery retained:
regional extent and detailed causal chemistry remain open.

### Packet B2 — 1986 regional satellite replay
Packet:
language/r/examples/ozone-1986.rpacket

Commit:
aabb60bda8c1646639a86e9aef93197105872d93

Claim:
the Antarctic spring ozone-hole phenomenon is regional-scale rather than a local Halley-instrument artifact.

TPP:
W=1.00
N=0.75
I=0.75
T=0.75
D=0.75

TPX:
0.794418

Band:
SCOPED_REALIST.

Authority gain:
- noncommon ground/satellite ancestry;
- transport from one station to regional Antarctica;
- local-instrument rival weakened.

Still HOLD:
complete causal chemical ontology.

Historical lesson:
THE PHENOMENON COULD BE REAL BEFORE ITS MECHANISM WAS FULLY IDENTIFIED.

Historiographic caution:
simplified stories about satellite software automatically deleting the ozone hole are not made load-bearing.
NASA's own history establishes the sequence of ground publication and subsequent satellite regional demonstration; disputed processing details remain residue.

## Historical lineage C — H. pylori

### Packet C1 — 1983/84 early association
Packet:
language/r/examples/hpylori-1983.rpacket

Commit:
cf57a1906b68fe212ed9f3fec41480b22148ed41

Claim:
curved gastric bacteria are reproducibly associated with chronic gastritis and ulcer-linked pathology.

TPP:
W=0.50
N=0.50
I=0.50
T=0.25
D=0.75

TPX:
0.472044

Band:
LIMITED_SCOPED.

Residue:
association is stronger than causal identification.

Live rivals:
- harmless commensal / secondary colonizer;
- acid/stress/lifestyle primary-cause frameworks.

### Packet C2 — causal consolidation
Packet:
language/r/examples/hpylori-causal.rpacket

Commit:
2dc93c9462b064550ea0075bce496ed4065f9524

Claim:
H. pylori infection is a major causal driver of chronic gastritis and peptic ulcer disease, and eradication changes disease course.

TPP:
W=1.00
N=0.75
I=0.75
T=0.75
D=0.75

TPX:
0.794418

Band:
SCOPED_REALIST.

Authority gain:
- culture;
- histology;
- treatment response;
- volunteer/interventional evidence;
- epidemiology.

Residue:
not every infected person develops ulcer disease; host/strain/disease-subtype structure remains live.

Historical lesson:
METHOD CHANGE CAN CREATE A RIVAL THAT PREVIOUS PRACTICE COULD NOT STABLY REALIZE.

## Cross-epoch theorem

The three lineages jointly support:

1. FUTURE-RIVAL IGNORANCE DOES NOT ERASE CURRENT CONSTRAINT AUTHORITY.
2. CURRENT CONSTRAINT AUTHORITY DOES NOT LICENSE FINAL THEORY IDENTITY.
3. SUCCESSOR SHOCK CAN PRESERVE, CONTRACT, OR REINTERPRET PRIOR AUTHORITY.
4. RESIDUE IS LOAD-BEARING:
   - Mercury anomaly;
   - ozone mechanism/extent;
   - H. pylori causality and host heterogeneity.
5. A later theory or method need not make predecessor science fraudulent.
6. A predecessor theory's scoped invariant may remain world-supported after its broader ontology is retired.

Therefore:

SCIENCE CAN KNOW REALITY BEFORE IT KNOWS ITS FUTURE RIVALS,

provided "know reality" means:
earn scoped authority for world-supported constraints,

not:
possess a final exhaustive ontology.

## Mystery-preserving realism

MQR-4.27 explicitly licenses the joint state:

SCOPED_REALIST_AUTHORITY = HIGH
AND
FINAL_ONTOLOGY = HOLD.

This is not weakened realism.

It is the refusal to convert earned local authority into unearned metaphysical closure.

The unknown future rival is represented by:
OPEN_WORLD_RESIDUE,
not by setting all current authority to zero.

## Truth-proximity interpretation

R-Language's TPX is intentionally non-hindsight.

Consequently:
Newton-1859 scoped constraint authority can score higher than GR-1915 at first introduction.

This prevents a historical-survivor fallacy:
"the theory we now think better must have deserved the highest score at every earlier moment."

R-Language instead asks:
what did the world-facing evidence at that moment force?

Thus TPX is a measure of:
EARNED CURRENT REALIST PROXIMITY,

not:
RETROSPECTIVE WINNER SIMILARITY.

## Current doctrine promotion

Root README live-surface update:
3341e31141faaede997b8ecfff05a7e1f30e304f

doctrine/CURRENT.md Generation-IV + R-Language promotion:
9aeffb14735d1fdd97f3dbc3e986ea85c424a2e6

The repository now has an active executable language, not only prose doctrine.

## Verdict

HISTORICAL-CROSS-EPOCH-REPLAY-PASS /
NEWTONIAN-SCOPED-AUTHORITY-PRESERVED-WITH-MERCURY-RESIDUE /
SUCCESSOR-GR-CONTRACTS-FINALITY-WITHOUT-ERASING-ALL-PREDECESSOR-AUTHORITY /
OZONE-1985-PHENOMENON-AUTHORITY-BEFORE-FULL-MECHANISM /
OZONE-NONCOMMON-REGIONAL-CONTACT-RAISES-AUTHORITY /
H-PYLORI-ASSOCIATION-PRECEDES-CAUSAL-CONSOLIDATION /
METHOD-CHANGE-EXPANDS-LIVE-RIVAL-SPACE /
FUTURE-RIVAL-IGNORANCE-NOT-EQUAL-ZERO-KNOWLEDGE /
CURRENT-AUTHORITY-NOT-EQUAL-FINALITY /
MYSTERY-PRESERVING-REALISM-PASS /
R-LANGUAGE-V0.1-LIVE /
TPP-W-N-I-T-D-ACTIVE /
TPX-NONPROBABILISTIC-PROXY-ACTIVE /
HINDSIGHT-FIREWALL-PASS /
OPEN-WORLD-RESIDUE-MANDATORY /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
