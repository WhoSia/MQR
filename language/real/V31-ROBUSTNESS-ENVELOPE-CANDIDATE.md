# REALENVELOPE 0.31-CANDIDATE — Robustness-Envelope Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED / MQR-4.74**

REALENVELOPE does not choose an optimal uncertainty set.

It records and mechanically audits the authority conditions of a declared robustness-envelope certificate.

## Header

```text
REALENVELOPE 0.31-CANDIDATE
id <token>
sealed PASS
claim_scope_hash <token>
obligation_family_hash <token>
envelope_id <token>
envelope_version <token>
parent_certificate <token|NONE>
admissibility_rule_hash <token>
revision_rule_hash <token>
evidence_kind <OBSERVED|PROVED|ENUMERATED|SIMULATED|INFERRED|OPEN>
completeness_claim RELATIVE_ONLY
open_world_complete OFF
...
END
```

## Perturbation rows

```text
perturbation <id> <generator> <coherent> <relevant> <independent> <realizability> <permission> <scope_preserved> <action>
```

Generators:
- THEORY
- RIVAL
- ANOMALY
- INSTRUMENT
- DOMAIN_GRAMMAR
- EXTERNAL
- COUNTERMODEL
- FRAMEWORK_EXTENSION
- PROOF_OBLIGATION
- POSTOUTCOME
- LABEL_ONLY

Boolean fields use YES / NO.

Realizability:
- AVAILABLE
- CURRENTLY_UNREALIZABLE
- IMPOSSIBLE_IN_PRINCIPLE
- NOT_APPLICABLE

Permission:
- PERMITTED
- BLOCKED
- NOT_APPLICABLE

Actions:
- ADMIT_NEW_FAILURE
- ADMIT_SCIENTIFIC_DEBT
- REJECT_INCOHERENT
- REJECT_IRRELEVANT
- HOLD_POSTOUTCOME
- HOLD_SCOPE_DRIFT
- SPLIT_PARENT
- MERGE_CHILDREN
- HOLD_UNEARNED
- NO_NEW_FAILURE

## Transition receipts

```text
transition <EXPAND|SPLIT|MERGE|TRANSPORT> <source> <target> <receipt>
```

Receipt must be explicit and not OPEN.

## Mechanical boundaries

The compiler rejects:
- `open_world_complete != OFF`;
- `completeness_claim != RELATIVE_ONLY`;
- an admitted failure with incoherent or irrelevant perturbation;
- post-outcome perturbation promoted as prospective authority;
- scope-changing perturbation treated as same-scope defeat;
- impossible-in-principle perturbation admitted as executable scientific debt;
- split/merge without a transition receipt;
- BLOCKED execution treated as scientific irrelevance.

The compiler emits:
- envelope version identity;
- perturbation census by authority class;
- whether successor authority is reopened;
- whether the prior certificate remains historically valid at its old declared envelope;
- explicit open-world ceiling.

## Authority semantics

```text
LATER_ADMISSIBLE_EXPANSION_CAN_REOPEN_SUCCESSOR_AUTHORITY
AND
PRIOR_SCOPED_CERTIFICATE_CAN_REMAIN_HISTORICALLY_VALID
```

These statements are compatible.

REALENVELOPE does not infer:
- optimal envelope choice;
- probability that the envelope is complete;
- global robustness;
- truth distance;
- universal perturbation severity;
- open-world closure.

## Promotion status

`REALACQUIRE 0.29` remains the latest promoted syntax.

`REALWARRANT 0.30-CANDIDATE` remains development-only.

`REALENVELOPE 0.31-CANDIDATE` is development-only until an independent promotion stage explicitly earns otherwise.
