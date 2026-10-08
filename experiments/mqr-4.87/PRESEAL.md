# MQR-4.87 — Real Lang P1: Typed Warrant Court
Status: PROTOTYPE / INTERPRETATION COURT / NO NEW THEOREM CLAIM

Input is a dictionary with polynomial terms, sources with generation-family identifiers,
shared upstream components, credential validity, scopes, independently provided permission
for requested use, a policy threshold, and known compromised components.
Evidence interpretation is restricted to singleton source monomials. Higher-degree terms
are NOT taken as independent observational sources. A coefficient, duplicate derivation,
or source raised to a power never creates independent evidence on its own.
Each source must have valid credentials and allowed scope. Known compromised upstream
components defeat the current source pending reassessment and trigger exposed-source review.
Surviving singleton sources are counted by independently attested generation families.
At least k distinct families plus valid permission: AUTHORIZED_FOR_USE.
Permission denied: DENIED_SCOPE (not evidence falsity).
Defect-exposed eligible sources reduce count below k: HOLD_SHARED_DEFECT.
Otherwise: HOLD_INSUFFICIENT. Missing metadata is unknown, never silently valid.

Frozen cases: T1 distinct p+q -> authorized; T2 same family -> insufficient;
T3 shared known defect -> defect hold; T4 scope-denied -> denied;
T5 repeated p squared -> insufficient; T6 invalid credential -> insufficient;
T7 policy k=1 -> authorized; T8 same polynomial, distinct metadata -> distinct verdict;
T9 duplicate path -> insufficient; T10 missing metadata -> insufficient and unknown flag.

This is a synthetic pedagogical MQR interpreter, not a new mathematical theorem,
not a theorem of Green et al. (2007), and not empirically validated scientific authority.
Prior art boundary: provenance polynomial semantics (Green et al. 2007),
distributed authorization (Li et al. 2003; Abadi et al. 1993),
local-global gluing (Abramsky and Brandenburger 2011).
4.86 stays OPEN / hosted validation HOLD. No predecessor closure is inferred.
Next: executable typed judgments, then tests, then real-world evidence and policy revisions.