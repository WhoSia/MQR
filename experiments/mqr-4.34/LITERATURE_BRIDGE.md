# MQR-4.34 — Literature Bridge

Status: CONCEPTUAL ANCHOR / NO EMPIRICAL PROMOTION CREDIT

This note records literature that constrains interpretation of MQR-4.34. None of these sources supplies fresh case credit.

## 1. Pearl & Bareinboim — transportability requires explicit domain-difference structure

Judea Pearl and Elias Bareinboim, “Transportability of Causal and Statistical Relations: A Formal Approach,” AAAI 2011.

DOI: 10.1609/aaai.v25i1.7861

Drive copy already present:
`Pearl & Bareinboim (2011) — Transportability of Causal and Statistical Relations - A Formal Approach.pdf`

Relevant constraint:

Transportability is not licensed by generic similarity between environments. Their selection-diagram framework represents where mechanisms differ and asks what additional observations/experiments license transfer.

MQR-4.34 is not a causal-transportability theorem and does not import selection diagrams. The useful structural lesson is narrower:

> authority to transport a claim should depend on an explicit representation of how source and target domains differ, not on a scalar similarity/support flag alone.

That is the role played here by bridge→direct relation typing.

## 2. Tal — measurement authority is model-mediated relation, not raw indication

Eran Tal, “Calibration: Modelling the Measurement Process,” Studies in History and Philosophy of Science 65–66 (2017), 33–45.

DOI: 10.1016/j.shpsa.2017.09.001

Drive copy already present:
`Tal (2017) — Calibration - Modelling the Measurement Process.pdf`

Relevant constraint:

Tal treats calibration as constructing and testing models that establish a reliable relation between indications and outcomes. Measurement authority is therefore mediated by a tested measurement-process model rather than read directly from an instrument indication.

MQR-4.34 uses this as a philosophical constraint on the word “support”:

> an observed PASS is not itself a portable support quantity; the inferential relation that makes the PASS evidentially relevant must also survive scrutiny.

## 3. Cousot & Cousot — coarse abstraction can preserve information without licensing refined claims

Patrick Cousot and Radhia Cousot, “Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints,” POPL 1977.

Drive copy already present:
`Cousot & Cousot (1977) — Abstract Interpretation - A Unified Lattice Model for Static Analysis of Programs.pdf`

Relevant constraint:

Abstract interpretation formalizes how a coarser semantic universe can soundly summarize selected properties of a more concrete one while discarding distinctions that the abstraction does not represent.

MQR-4.34 does not claim that its R2 relation is a Galois connection or an abstract-interpretation theorem.

The useful structural analogy is:

> preservation after forgetting distinctions licenses claims only at the preserved quotient unless a separate argument recovers authority over the refined distinctions.

This is exactly the burden encoded prospectively in `R2_SUCCESSOR_REFINEMENT`.

## 4. Unicode normalization — a concrete refinement world

Unicode Standard Annex #15, “Unicode Normalization Forms,” and the Unicode 16.0 normalization documentation provide the engineering basis for UNORM-001.

The Unicode normalization stability policy states, roughly, that normalization results remain stable across versions when the string contains only characters assigned in both versions. It also explicitly warns that strings containing characters unassigned in an older version can normalize differently under a future version.

Unicode 16.0 introduced new characters with normalization behavior that created novel implementation-relevant cases, while retaining the normalization algorithm itself.

This makes UNORM-001 a particularly clean refinement stress:
- the old/common assigned-character bridge can remain stable;
- successor-only distinctions can become behavior-bearing;
- therefore coarse preservation need not license claims on the newly resolved domain.

MQR-4.34 presealed the relation before executing the direct packet, so this literature is an interpretation anchor rather than a posthoc retyping device.

## 5. What MQR adds

The literature above supplies three different pieces:
- formal domain-difference representation;
- model-mediated measurement authority;
- quotient/refinement discipline.

MQR-4.34 combines them into a prospective experimental question:

```text
Given adjacent bridge transport,
what relation maps bridge support into the direct domain,
and what authority is licensed before the direct outcome is known?
```

The object of measurement is therefore not merely a case-level support bit.

A candidate relational object is:

```text
R = (domain_map, component_map, quotient_map, state_map, endpoint_map)
```

with authority assigned by a frozen relation classifier.

The stage deliberately stops short of claiming that this tuple is a final ontology of support.

Fresh external promotion remains governed entirely by the presealed 4.34 rule.
