# REALPROMOTE 0.27 — Promotion-Reason Conflict Constitution

Status: **PROMOTED LIVE / MQR-4.60 QUALIFIED**

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

Live receipts:
- **PRCR — Promotion-Reason Conflict Receipt**
- **RAG — Reason-Ancestry Graph**
- **HRS — Horizon/Scope Receipt**

A HOLD outcome is allowed when reasons are valid but unresolved.

## Cumulative integration guard

The v0.27 packet family is registered in cumulative Real-Language CI and excluded from the generic v0.2/v0.3 parser lane. Final-seal commits are also explicit cumulative-CI triggers.

## First qualifying reveal

The first fully qualifying dedicated head is:

~~~text
head = e9e259c54fc9006ce5d79ba012b82f5a18874be8
run = 36951219127

MQR-4.60/Court = SUCCESS
MQR-4.60/Real-Language = SUCCESS
MQR-4.60/Lean = SUCCESS
MQR-4.60/Lean-Integration = SUCCESS
~~~

The frozen 16-case court passed without post-reveal mutation. Rust and independent Prolog agreed on the representative conflict packets. The Lean conflict boundary and aggregate MQR import both passed.

Cumulative Real-Language integration also passed after registering the v0.27 packet family in the cumulative parser guard (run 36951150367, predecessor integration head 6abe0c5ac635818c2d250400f489ca02e43fcb38).

## Earned boundary

~~~text
PAIRWISE DOMINANCE != TOTAL ORDER
PARETO NONDOMINATION != UNIQUE PROMOTION
LOCAL VETO != UNIVERSAL PRIORITY
MORE REASONS != MORE WARRANT
DUPLICATED REASONS != INDEPENDENT WARRANT
HORIZON CHANGE MAY REVERSE LOCAL ADMISSIBILITY
INCOMPARABILITY = LEGITIMATE HOLD
UNIVERSAL PROMOTION META-UTILITY = NOT EARNED
~~~

This does not claim that no scalar, lexicographic, outranking or veto method can ever be useful. It denies their unlicensed promotion to a universal scientific-constitutional decision rule.
