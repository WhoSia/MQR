# REALPROMOTE 0.27 — Promotion-Reason Conflict Constitution

Status: **CANDIDATE / MQR-4.60 / PRESEALED**

REALPROMOTE 0.27 extends v0.26 without replacing it.

It represents conflict among typed promotion reasons using local relations rather than a universal score.

Core relation surface:

~~~text
DOMINATES
VETOES
INCOMPARABLE
DEFEATS_UNDER_SCOPE
~~~

Canonical guardrails:

~~~text
WEIGHTED_SUM_AS_UNIVERSAL_ANSWER = REJECT
LEXICOGRAPHIC_ORDER_AS_UNIVERSAL_ANSWER = REJECT
PARETO_FRONTIER_AS_DECISION_PROCEDURE = REJECT
LOCAL_VETO_AS_UNIVERSAL_PRIORITY = REJECT
DUPLICATE_REASON_COUNTING = REJECT
INCOMPARABILITY = LEGITIMATE
HORIZON/SCOPE REVERSAL = EXPLICIT
UNIVERSAL_PROMOTION_META_UTILITY = NOT_EARNED
~~~

Candidate receipts:
- PRCR — Promotion-Reason Conflict Receipt
- RAG — Reason-Ancestry Graph
- HRS — Horizon/Scope Receipt

A HOLD outcome is allowed when reasons are valid but unresolved.

## Cumulative integration guard

The v0.27 packet family is registered in cumulative Real-Language CI and excluded from the generic v0.2/v0.3 parser lane. Final-seal commits are also explicit cumulative-CI triggers.
