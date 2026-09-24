# R-Language / R-Packet v0.1

R-Language is MQR's active event-to-authority language.

It takes an incoming scientific event, claim, experiment, anomaly, historical receipt, or successor shock and compiles it into a **scoped realist-authority packet**.

Its central question is deliberately not:

> "What percentage true is this theory?"

Instead:

> "Given the world-contact, rival pressure, provenance, scope and live routes to defeat that currently exist, how much realist authority has this particular claim earned, and what remains unresolved?"

## Why this is not a truth meter

MQR rejects a primitive scalar distance to metaphysical Truth.

R-Language therefore outputs three things together:

1. **Authority Gate**
   - C = constitutional / adjudication legitimacy
   - E = admissible world-contact / execution
   - P = provenance / time / auditability
   - R = open-world rival invariance

2. **Truth-Proximity Profile (TPP)**
   - W = world resistance / intervention-exclusion strength
   - N = noncommon evidence-route strength
   - I = current rival-invariance / identification strength
   - T = transport across the declared scope
   - D = live defeat exposure / corrigibility

3. **Residue**
   - adverse observations
   - surviving rivals
   - generator limitations
   - scope debt
   - ontic/metaphysical reserve
   - successor vulnerability

The optional scalar:

TPX = geometric_mean(W,N,I,T,D)

is a **current world-constrained proximity proxy**, not:
- P(claim=true)
- Bayesian posterior probability
- metaphysical distance to final truth
- proof that no unconceived rival exists.

If any of C/E/P/R is not PASS, TPX is NA.

## Axis rubric

Use quarter-step scoring by default: 0, .25, .50, .75, 1.00.
Finer values require an explicit calibration receipt.

### W — World resistance
- 0.00: no discriminating world-contact
- 0.25: descriptive fit only
- 0.50: replicated effect, mainly same route
- 0.75: intervention/exclusion or strong independent prediction
- 1.00: repeated noncommon world-contact with direct failure exposure

### N — Noncommon route strength
- 0.00: one evidence lineage
- 0.25: repetitions sharing the same load-bearing ancestry
- 0.50: partially independent routes
- 0.75: multiple materially noncommon routes
- 1.00: several independent failure families converge

### I — Rival invariance / identification
- 0.00: major live rivals disagree on the claim
- 0.25: broad observational equivalence remains
- 0.50: narrowed identified set, claim still partly rival-sensitive
- 0.75: claim invariant across diverse current generators
- 1.00: strong current invariance under targeted adversarial generation

Even I=1.00 retains OPEN_WORLD_RESIDUE.

### T — Scope transport
- 0.00: claim exceeds observed jurisdiction
- 0.25: one narrow context
- 0.50: multiple nearby contexts
- 0.75: cross-regime transport at declared scope
- 1.00: broad declared-scope transport with explicit bridges

### D — Defeat exposure
- 0.00: immunized / no reachable defeater
- 0.25: defeaters named but weakly reachable
- 0.50: live prospective failure route
- 0.75: multiple prospective routes including noncommon challenge
- 1.00: strong challenge ecology plus representation/rival-generator escape

## Authority bands

Bands are display summaries of TPX, not new epistemic primitives.

- [0.00,0.40): FRAGILE_SCOPED
- [0.40,0.60): LIMITED_SCOPED
- [0.60,0.80): SCOPED_REALIST
- [0.80,1.00]: STRONG_SCOPED_REALIST

No band is emitted if any gate is not PASS.

## R-Packet grammar

Each non-comment line is one command.

```text
RPACKET 0.1
id "packet-id"
epoch "historical or current epoch"
claim CONSTRAINT "claim text"
scope "licensed scope"

gate C PASS
gate E PASS
gate P PASS
gate R PASS

axis W 0.75 "why"
axis N 0.50 "why"
axis I 0.75 "why"
axis T 0.50 "why"
axis D 0.75 "why"

generator STRUCTURAL "rival generator description"
rival SURVIVING "live rival"
residue MODERATE "adverse residue"
ontic HOLD "what is still metaphysically underdetermined"
successor VULNERABLE
shock "later epoch" CONTRACT "later successor changes scope"
source "source/provenance pointer"
END
```

Comments start with `#`.

## Hindsight firewall

Historical packets must be compiled from contemporaneously available evidence.

Later information may only enter through `shock` lines.

A successor may:
- PRESERVE
- CONTRACT
- REINTERPRET
- EXPAND_RIVAL_SPACE
- RETIRE

It may not silently raise an earlier TPX.

## Open-world semantics

A PASS on R means:

> this claim is invariant across the currently surviving adversarially generated rivals at the declared scope.

It does not mean:

> every possible rival has been enumerated.

Every compiled packet therefore carries:
`open_world_residue=true`.

## Interpreter

```bash
python language/r/rpacket.py language/r/examples/newton-mercury-1859.rpacket
```

The interpreter emits canonical JSON suitable for:
- Git receipts
- Notion writeback
- later successor replay
- comparison across historical epochs
- automated validation

## Design rule

R-Language is allowed to compress bookkeeping.

It is not allowed to compress away mystery.
