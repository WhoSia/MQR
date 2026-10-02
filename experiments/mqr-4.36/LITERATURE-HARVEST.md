# MQR-4.36 — Literature Harvest: Rubenstein et al. (2017)

Source:
Rubenstein, Weichwald, Bongers, Mooij, Janzing, Grosse-Wentrup & Schölkopf (2017), *Causal Consistency of Structural Equation Models*.

Canonical Drive title:
`Rubenstein et al. (2017) — Causal Consistency of Structural Equation Models.pdf`

## Load-bearing result

An exact transformation between SEMs is not merely a state-variable map.

The paper requires:
- a transformation `tau : X -> Y`;
- a surjective map between intervention sets;
- preservation of the intervention partial order;
- equality between the transformed source interventional distribution and the target interventional distribution for every admitted intervention.

The intervention order matters because it records which interventions can be composed without undoing earlier intervention structure.

## Formal positive control

The paper proves transitivity of exact transformations.

If:
- Y is an exact transformation of X;
- Z is an exact transformation of Y;

then Z is an exact composite transformation of X.

The composite proof uses the fact that the intervention maps compose while remaining surjective and order-preserving, together with the exact interventional-distribution equalities.

## MQR consequence

This is a positive control against the slogan:

```text
COMPOSITION IS NEVER WARRANTED
```

That slogan is false.

Under sufficiently explicit structural conditions, composition can be formally licensed.

But the theorem does not imply:

```text
A real scientific bridge has satisfied those conditions merely because its formal encoding has.
```

MQR therefore separates:

```text
FORMAL COMPOSITION THEOREM
from
EMPIRICAL ENTITLEMENT TO ITS PREMISES
```

## Cholesterol counterexample lesson

The paper's historical cholesterol example shows why a macro variable can fail as a causal variable when different lower-level interventions collapse to the same macro value while having different downstream effects.

For MQR this is a concrete version of:

```text
SAME OBSERVATIONAL / AGGREGATE VALUE
!=
SAME INTERVENTIONAL MEANING
```

A quotient that merges intervention-distinct states can destroy causal transport even when it appears descriptively compact.

## Relation to MQR-4.36

The paper strengthens three 4.36 commitments.

1. **Probe/intervention class must be explicit.**
   A formal composition result is indexed by the intervention family it preserves.

2. **Composition can be proved conditionally.**
   Lean may correctly certify a theorem that composes formally specified maps.

3. **World entitlement remains external to theoremhood.**
   Whether the actual scientific system realizes the required intervention correspondence remains a world/model claim.

Therefore Rubenstein et al. supports the positive half of the MQR proof-assistant boundary:

```text
STRONG FORMAL CONDITIONS
CAN EARN
FORMAL COMPOSITION
```

while MQR-4.36 preserves the negative half:

```text
FORMAL COMPOSITION
DOES NOT BY ITSELF EARN
WORLD-LEVEL PREMISE TRUTH
```

## Harvest status

Canonical paper processed from 00_INTAKE to the MQR paper collection.

Used for conceptual/formal constraint only.

Zero fresh-case promotion credit.
