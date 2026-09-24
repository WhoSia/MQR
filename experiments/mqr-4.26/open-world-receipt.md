# MQR-4.26 — Open-World Rival Closure & Origin-Return Receipt

Status: R_OPEN OPERATIONAL PASS / EXHAUSTIVE CLOSURE REJECTED / ORIGIN RETURN PASS

## Preseal
Commit:
1ed4b9d9f961bff06e0f7c7bfd859e4b96815019

Question:
Can rival-separation R remain operational when no finite rival generator can enumerate all possible future hypotheses?

## Experimental execution
Workflow:
.github/workflows/mqr-4.26-open-world.yml

Run:
35967992728

Commit:
55faa501afba21285650e1e5883bc94ae4f09fa5

### t0 — restricted rival grammar
Evidence:
f(0)=0
f(1)=1

Rival grammar:
finite affine family.

Unique survivor:
f(x)=x.

Within this grammar:
GLOBAL CLAIM = PASS.

Correct label:
UNIQUE_WITHIN_CURRENT_OPEN_WORLD_TEST.

No exhaustive closure claim is licensed.

### t1 — rival grammar expansion
Add quadratic escape rivals:
h_c(x)=x+c*x*(x-1), c != 0.

Every h_c agrees at x=0,1.

Survivors:
affine_1_0 plus quadratic escapes.

Global f(x)=x claim:
HOLD.

Invariant core:
{f(0)=0, f(1)=1}.

Action:
CONTRACT TO CURRENT IDENTIFIED CORE.

### t2 — discriminating world contact
Add admissible observation:
f(2)=2.

Quadratic escape rivals are eliminated.

Within G1:
f(x)=x becomes unique again.

Current R:
PASS.

### t3 — rival grammar re-expansion
Add cubic escape rivals:
h_d(x)=x+d*x*(x-1)*(x-2), d != 0.

They agree at x=0,1,2 and diverge later.

Global f(x)=x claim:
HOLD again.

Invariant core:
{f(0)=0, f(1)=1, f(2)=2}.

Thus:
GENERATOR EXPANSION CAN CONTRACT AUTHORITY.
DISCRIMINATING WORLD CONTACT CAN EXPAND AUTHORITY.
A LATER GENERATOR EXPANSION CAN CONTRACT IT AGAIN.

## Generic finite-evidence escape theorem

Let O be any finite set of observed points and f0 a baseline function.
For c != 0 define:

h_c(x)=f0(x)+c*Product[(x-o), o in O].

For every o in O:
h_c(o)=f0(o).

For generic x* not in O:
h_c(x*) != f0(x*).

For O={0,...,n} and x*=n+1:

h_c(n+1)-f0(n+1)=c*(n+1)! != 0.

CI witnesses:
O={0,1}, x*=2: base=2, rival=4.
O={0,1,2}, x*=3: base=3, rival=9.
O={0,1,2,3}, x*=4: base=4, rival=28.
O={0,1,2,3,4}, x*=5: base=5, rival=125.

Independent Wolfram check:
- each escape polynomial agrees identically on all observed points;
- differences at the next point are 2c, 6c, 24c, 120c.

Therefore:
FINITE EVIDENCE ALONE DOES NOT IDENTIFY AN UNRESTRICTED GLOBAL EXTRAPOLATIVE LAW.

This is not a universal theorem that all scientific law inference fails.
It means extrapolative authority must come from additional independently warranted structural assumptions, intervention geometry, cross-domain transport, or other world-contact beyond finite point fit.

## Operational open-world R

Let:
E_t = admitted evidence/world-contact at time t.
A_t = currently warranted structural assumptions.
Gamma_t = rival-generator portfolio.
S_t = survivors generated under Gamma_t and A_t consistent with E_t.
Scope_t = licensed claim domain.

For claim phi:

R_t(phi)=PASS
iff
every h in S_t entails phi.

Define current invariant authority core:

Q_t = intersection of claim-relevant consequences of all h in S_t.

Scientific authority:

AUTH_t(phi)
=
C_t AND E_t AND P_t AND [phi in Q_t].

But every AUTH_t carries:

OPEN_WORLD_RESIDUE = ACTIVE.

R_t therefore means:
current adversarially tested claim invariance.

It never means:
all possible future rivals have been eliminated.

## Authority dynamics

Holding evidence/assumptions fixed:

Gamma_t subset Gamma_{t+1}
implies
S_t subset-or-equal S_{t+1}

and therefore the invariant authority core can only contract or remain unchanged:

Q_{t+1} subset-or-equal Q_t.

By contrast, adding discriminating world-contact while holding the rival grammar fixed can eliminate survivors and therefore refine/expand the invariant authority core.

Hence:

RIVAL-GENERATOR EXPANSION -> AUTHORITY CONTRACTION OR STASIS.
DISCRIMINATING WORLD-CONTACT -> AUTHORITY EXPANSION OR STASIS.

This is the core open-world dynamic.

## Why exhaustive hypothesis enumeration is unnecessary

R need not solve:
"Have we imagined every possible theory?"

That question is operationally impossible in an open world.

Instead R asks:
"What is the strongest claim invariant across the current surviving rivals after multiple independent mechanisms for generating attacks, with future rival space explicitly left open?"

Required generator pressure includes:
- parameter/basis mutation;
- structural/grammar mutation;
- assumption relaxation;
- diagonal escape against unobserved consequences;
- historically imported successor patterns when available.

A single generator never earns exhaustive language.

## Identified-set closure

The word closure is now typed.

CURRENT IDENTIFIED-SET CLOSURE:
allowed.

GLOBAL HYPOTHESIS EXHAUSTIVENESS:
HOLD.

If a later rival violates phi:
- old receipt remains historically true as AUTH_t(phi | Gamma_t,A_t,Scope_t);
- current authority for phi is revoked or contracted;
- no retroactive history rewriting;
- no claim that the predecessor was "never scientific";
- no claim that the successor proves every predecessor commitment false.

This is SUCCESSOR-VULNERABLE REALIST AUTHORITY.

## Stanford/PUA pressure without overclaiming

Stanford's historical problem of unconceived alternatives is philosophically contested.
MQR-4.26 does not require the stronger inductive thesis that serious unconceived alternatives are probably present for every current theory.

The weaker result is enough:
finite current rival search cannot logically establish exhaustive rival closure.

The generic escape construction supplies that result directly for unrestricted extrapolation.

Therefore:
PUA PRESSURE BLOCKS FINALITY,
but does not force global skepticism.

## Historical root mirrors

### Mercury / Newton / successor gravity
Newtonian celestial mechanics possessed vast successful constraint authority while Mercury retained an anomalous perihelion residue.
Le Verrier's Vulcan represented one available repair/rival route.
General relativity later supplied a different gravitational framework accounting for the residual precession.

MQR reading:
strong authority can coexist with unresolved residue;
successor theory can transform scope without making all predecessor success unreal.

### Antarctic ozone
British Antarctic Survey ground measurements produced the 1985 ozone-hole report.
Satellite systems also contained extreme Antarctic behavior, but recognition/publication followed a different route.
Historical accounts disagree on the exact role of automated flagging/fill-value processing, so that detail is not treated as settled fact here.

MQR reading:
world-contact can exist while inquiry architecture controls whether surprise becomes an admissible scientific object.
The historiographic disagreement itself belongs in the residue ledger.

### H. pylori
Spiral gastric bacteria had historical precedents.
Shorter culture routines repeatedly failed.
A longer incubation interval produced successful culture, and later intervention/replication changed the causal status of H. pylori in gastritis and ulcer disease.

MQR reading:
a hypothesis can be absent from effective rival space because method grammar prevents its stable empirical realization.
Changing technique changes the space of live science.

## Canonical literature/corpus return

MQR internal canonical sources re-read:
- Generation I — Measurement Quotient Foundation:
  regime-mediated distinction, dependency-resolved world resistance, scoped authority with ontic reserve, recursive corrigibility.
- MQR-1.10-A/D:
  nonexclusive reality;
  lookup-table global law rejection;
  global implementation requires independent modal/exclusion excess;
  governing-vs-Humean and simulation hypotheses remain HOLD when empirically equivalent.
- MQR-3.30:
  original explanandum is world vs inquiry architecture;
  rival vocabulary itself must remain defeatable.
- MQR-3.76:
  current rival victory does not exhaust unconceived successors;
  realist authority is temporally earned, quotient-scoped and successor-vulnerable.

Drive corpus actively reused:
- Laudan (1981), A Confutation of Convergent Realism;
- van Fraassen, The Scientific Image;
- Research OS 2026-09-10 philosophy/history survey covering Stanford-style unconceived alternatives, incommensurability, structural realism and phlogiston;
- Worrall structural realism remains in canonical genealogy.

External methodological anchors:
- D'Amour et al., JMLR, underspecification;
- Kline & Tamer, partial identification;
- Stanford, Exceeding Our Grasp;
- historical literature on Mercury, Antarctic ozone and H. pylori.

## Return to the global-law question

MQR-1.10 asked why a law fitting every known case is not automatically a real global law.

MQR-4.26 supplies a constructive reason:
for finite observations, infinitely many structured escape rivals can agree on all known points while diverging elsewhere.

Therefore:

FINITE FIT != GLOBAL LAW.
CURRENT UNIQUE MODEL != EXHAUSTIVE LAW.
SUCCESS != FINAL ONTOLOGY.

A global-law candidate gains authority only through nontrivial additional structure that itself survives:
- independent specification;
- novel exclusion;
- cross-domain transport;
- prospective risk;
- rival-generation pressure;
- successor vulnerability.

This is the old "modal excess" requirement returned in operational form.

## Mystery and authority

MQR does not treat mystery as a temporary embarrassment that must be erased before science can know anything.

Science may have:
- strong authority over a constraint;
- unresolved ontology behind that constraint;
- open future rivals;
- unknown deeper realizers;
all at once.

This preserves the founding distinction:

IGNORANCE BEYOND THE IDENTIFIED CORE
does not imply
VACUOUS TRUTH INSIDE THE IDENTIFIED CORE.

Nor does:
CURRENT AUTHORITY
imply
FINAL METAPHYSICAL CLOSURE.

## Constitutional result

MQR-4.25's fourth dimension R survives the incompleteness attack, but only after mutation:

R -> R_open.

No fifth authority dimension is required.

Generation-IV authority law remains:

AUTH_t(phi)=C_t AND E_t AND P_t AND R_open,t(phi)

with mandatory:
OPEN_WORLD_RESIDUE,
SCOPE,
RIVAL-GENERATOR PROVENANCE,
SUCCESSOR-VULNERABILITY.

## Verdict

RIVAL-GENERATOR-INCOMPLETENESS-ATTACK-PASS /
RESTRICTED-GRAMMAR-UNIQUENESS-SHOWN-FRAGILE /
GENERATOR-EXPANSION-CONTRACTS-AUTHORITY /
DISCRIMINATING-WORLD-CONTACT-EXPANDS-AUTHORITY /
GENERIC-FINITE-EVIDENCE-DIAGONAL-ESCAPE-PASS /
ABSOLUTE-RIVAL-CLOSURE-FROM-FINITE-SEARCH-REJECT /
R-OPEN-OPERATIONALIZATION-PASS /
CURRENT-IDENTIFIED-SET-CLOSURE-PASS /
GLOBAL-HYPOTHESIS-EXHAUSTIVENESS-HOLD /
OPEN-WORLD-RESIDUE-ACTIVE /
SUCCESSOR-VULNERABILITY-ACTIVE /
PUA-PRESSURE-WITHOUT-GLOBAL-SKEPTICISM /
FINITE-FIT-NOT-GLOBAL-LAW /
ORIGIN-WORLD-VS-ARCHITECTURE-QUESTION-RESTORED /
NONEXCLUSIVE-REALITY-AND-MODAL-EXCESS-INHERITED /
MYSTERY-RETAINED-AS-RESIDUE /
NO-FIFTH-AUTHORITY-DIMENSION /
SUCCESSOR-BASIS-REMAINS-C-E-P-R-OPEN /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
