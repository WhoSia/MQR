# MQR-4.80 — Court Freeze Repair Receipt

Status: **PRE-RESULT STRUCTURAL REPAIR / SCIENTIFIC CRITERION UNCHANGED**

The first frozen table encoded N3 and M3 with identical observable coordinates but different expected states:
- N3 = UNION_LAUNDERING
- M3 = OBLIGATION_INVENTION

That made the Court under-specified.

Repair:
- add explicit `union_claim` coordinate;
- N3: union_claim=1, invent_joint=0;
- M3: union_claim=0, invent_joint=1;
- keep all previously frozen authority boundaries unchanged.

Interpretation:
- **UNION_LAUNDERING** = existing locally warranted targets are simply unioned and the union is treated as jointly warranted.
- **OBLIGATION_INVENTION** = composition creates a new obligation not inherited from either local constitution.

No scientific outcome was changed. The repair only makes the frozen distinctions representable.

Repaired freeze commit:
`df1c191df9bbe6d5698efd9cc685ee3ac474981b`

Aligned canonical evaluator:
`aabcbfc723ab0e113992ef99f1a0fa2e9d6d735a`
