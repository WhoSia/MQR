# MQR-4.34 — Fresh Relational World-Contact Receipt

Status: THREE FRESH ENGINEERING RELATION TYPES EXECUTED / OPERATIONAL DIFFERENTIATION PASS / EXTERNAL IDENTIFICATION HOLD

## Constitution

Primary preseal:

`16c0d474...`

The relation grammar, authority map, promotion rule, falsifiers and anti-retrofitting rule were frozen before TKN/TOML calibration and before fresh behavioral reveal.

Fresh relation receipts were then compiled before behavior under commit lineage ending at:

`e8a6a733bf0b84f1f2473a7d8a3c44f6b9e4b5e0`

No relation retyping occurred after reveal.

## REGEX-001 — R1 strict domain extension

Lineage: ENGINEERING_DEVELOPMENT

Regimes:
- A = regex 1.9.6
- B = regex 1.10.6
- C = regex 1.12.3

Frozen relation: `R1_STRICT_DOMAIN_EXTENSION`

Frozen authority: `A1_EXTENSION_REQUIRES_FRESH_CONTACT`

Canonical run: `36136627752`

Bridge adjudication:

```text
A_TO_B=TRANSPORT_PASS
B_TO_C=TRANSPORT_PASS
COMPOSITION_CANDIDATE=YES
RELATION=R1_STRICT_DOMAIN_EXTENSION
AUTHORITY=A1_EXTENSION_REQUIRES_FRESH_CONTACT
MEDIATED_DIRECT_PREDICTION=NOT_LICENSED
DIRECT_BURDEN=FRESH_EXTENSION_CONTACT_REQUIRED
```

Independent direct adjudication:

```text
DIRECT_A_TO_C=TRANSPORT_PASS
FRESH_EXTENSION_CONTACT=PASS
RELATION_RETYPE=FORBIDDEN
AUTHORITY_REMAINS=A1_EXTENSION_REQUIRES_FRESH_CONTACT
REGEX_001_FRESH_RELATION_STRESS=PASS
```

The strict-extension relation did not predict direct failure. It predicted that adjacent transport could not license the extension without fresh direct contact. Fresh contact happened to pass. The authority state survives without retrospective upgrade to R0/A0.

## SJSON-001 — R0 same-generator holdout

Lineage: ENGINEERING_DEVELOPMENT

Regimes:
- A = serde_json 1.0.140
- B = serde_json 1.0.145
- C = serde_json 1.0.151

Frozen relation: `R0_SAME_GENERATOR_HOLDOUT`

Frozen authority: `A0_HOLDOUT_SUPPORT_ADMISSIBLE`

Canonical run: `36138267446`

Bridge adjudication before direct reveal:

```text
A_TO_B=TRANSPORT_PASS
B_TO_C=TRANSPORT_PASS
RELATION=R0_SAME_GENERATOR_HOLDOUT
AUTHORITY=A0_HOLDOUT_SUPPORT_ADMISSIBLE
MEDIATED_DIRECT_PREDICTION=TRANSPORT_PASS
```

Independent direct adjudication:

```text
DIRECT_A_TO_C=TRANSPORT_PASS
MEDIATED_PREDICTION_ADJUDICATION=CONFIRMED
RELATION_RETYPE=FORBIDDEN
AUTHORITY_REMAINS=A0_HOLDOUT_SUPPORT_ADMISSIBLE
SJSON_001_FRESH_RELATION_STRESS=PASS
```

This is one fresh confirmation that a presealed same-generator heldout relation can license a mediated direct PASS prediction and survive independent direct adjudication.

It is not enough to satisfy the promotion rule, which requires at least two fresh R0 cases and six fresh external cases overall.

## UNORM-001 — R2 successor refinement

Lineage: ENGINEERING_DEVELOPMENT

Regimes:
- A = unicode-normalization 0.1.22
- B = unicode-normalization 0.1.23
- C = unicode-normalization 0.1.24

Frozen relation: `R2_SUCCESSOR_REFINEMENT`

Frozen authority: `A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED`

Canonical run: `36138297347`

Bridge adjudication before successor-only direct reveal:

```text
A_TO_B_COARSE=TRANSPORT_PASS
B_TO_C_COARSE=TRANSPORT_PASS
RELATION=R2_SUCCESSOR_REFINEMENT
AUTHORITY=A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED
COARSE_MEDIATED_SUPPORT=ADMISSIBLE_IF_CANDIDATE
SUCCESSOR_ONLY_DIRECT_PREDICTION=NOT_LICENSED
DIRECT_BURDEN=FRESH_SUCCESSOR_CONTACT_REQUIRED
```

Independent successor-only direct adjudication:

```text
DIRECT_SUCCESSOR_A_TO_C=TRANSPORT_DIVERGENCE
QUOTIENT_INDEXED_INTERPRETATION=COARSE_PRESERVATION_WITH_SUCCESSOR_DIVERGENCE
RELATION_RETYPE=FORBIDDEN
AUTHORITY_REMAINS=A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED
UNORM_001_FRESH_RELATION_STRESS=PASS
```

This is the strongest fresh relational result of MQR-4.34.

The same lineage supports both:
1. preserved adjacent transport on the frozen coarse bridge quotient; and
2. direct divergence on a presealed successor-only refinement packet.

Therefore a scalar label such as `domain_covered=true/false` would erase a scientifically relevant distinction. Support authority must be indexed by the map between bridge and direct domains.

This does not mean refinement always produces divergence. It means coarse support does not by itself license claims on newly resolved successor distinctions.

## Cross-case operational differentiation

The three fresh cases were pretyped as three different relations and generated three different authority commitments:

```text
SJSON-001 -> R0 -> mediated direct PASS licensed -> direct PASS
REGEX-001 -> R1 -> mediated direct prediction not licensed -> fresh direct PASS required
UNORM-001 -> R2 -> coarse support licensed only on quotient -> successor direct divergence
```

The distinction is operational, not merely terminological. The relation label changes what evidence is required before direct reveal and what a later direct result is allowed to mean.

## Inherited collision calibration

TKN-001 and TOML-D1 were used only after the new relation grammar was frozen.

Zero-credit mapping:

```text
TKN-001 -> R0_SAME_GENERATOR_HOLDOUT
TOML-D1 -> R1_STRICT_DOMAIN_EXTENSION
```

Core run: `36136324912`

Machine result:

```text
DIAGNOSTIC_INHERITED_SEPARATION=PASS
FRESH_PROMOTION_CREDIT=ZERO
```

This shows that the new relation grammar can separate the old collision, but that fact earns no promotion credit and was not used to alter the grammar.

## Forcing and adversarial controls

Core run: `36136324912`

Passed:
- six forcing relations F0-F5;
- Rust/C++ exact concordance;
- decoy invariance attack;
- relation-changing intervention sensitivity;
- inherited collision separation;
- pre-behavior fresh relation compilation.

Machine summary:

```text
MQR434_FORCING_WORLDS=PASS
MQR434_RUST_CPP_CONCORDANCE=PASS
MQR434_DECOY_INVARIANCE=PASS
MQR434_RELATION_INTERVENTION_SENSITIVITY=PASS
MQR434_EXTERNAL_PROMOTION=STRUCTURALLY_HOLD
```

## Exact promotion ceiling

The presealed promotion rule requires all of:
1. F0-F5 forcing worlds classify exactly;
2. Rust canonical implementation and independent reference implementation agree byte-for-byte;
3. at least 6 fresh admitted external cases;
4. at least 2 lineage kinds;
5. at least 3 ENGINEERING_DEVELOPMENT cases;
6. at least 2 independently admitted RESEARCH_LAB cases;
7. at least 2 fresh R0 SAME_GENERATOR_HOLDOUT cases;
8. at least 1 fresh R1 STRICT_DOMAIN_EXTENSION case;
9. at least 1 fresh R2 SUCCESSOR_REFINEMENT or R3 CONSTITUTIVE_COMPONENT_SHIFT case;
10. zero authority-state collisions for an identical frozen relational receipt;
11. zero post-direct retyping;
12. decoy/irrelevant metadata attack changes zero relation receipts;
13. at least one relation-changing intervention changes the receipt in the frozen expected direction.

Observed fresh corpus:
- 3 admitted external cases, not 6;
- 1 lineage kind, ENGINEERING_DEVELOPMENT, not 2;
- 3 ENGINEERING_DEVELOPMENT cases, satisfying item 5;
- 0 independently admitted RESEARCH_LAB cases, not 2;
- 1 fresh R0 case, not 2;
- 1 fresh R1 case;
- 1 fresh R2 case;
- zero post-direct retyping observed.

Therefore the exact presealed verdict is:

```text
RELATIONAL_SUPPORT_GEOMETRY_EXTERNAL_IDENTIFICATION = HOLD
```

regardless of the favorable engineering pattern.

## Strongest earned result

The stage does not earn a general support-domain law or external identification.

It earns:

```text
RELATIONAL_SUPPORT_GEOMETRY_OPERATIONALIZED = PASS
THREE_FRESH_RELATION_TYPES_WORLD_CONTACT = PASS
R0_MEDIATED_PREDICTION = FRESHLY_CONFIRMED_ONCE
R1_FRESH_CONTACT_BURDEN = OPERATIONALLY_RESPECTED
R2_QUOTIENT_INDEXING = FRESHLY_VINDICATED_BY_SUCCESSOR_DIVERGENCE
INHERITED_TKN_TOML_COLLISION = SEPARATED_ZERO_CREDIT
RELATIONAL_SUPPORT_GEOMETRY_EXTERNAL_IDENTIFICATION = HOLD
```

The decisive conceptual update is that support authority attaches to a relation between observational domains, not to a Boolean property of a triangle.
