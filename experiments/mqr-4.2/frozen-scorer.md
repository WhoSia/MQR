# MQR-4.2 Frozen Scorer

Score each arm output per packet on 0/1/2:

S1 Claim-content fidelity
0 substitutes question; 1 partial; 2 exact.

S2 Role typing
0 conflates roles; 1 implicit; 2 explicit and correct.

S3 Scope typing
0 overgeneralizes; 1 partial; 2 explicit and correct.

S4 Commitment ceiling
0 misses overclaim/underclaim; 1 warns vaguely; 2 identifies exact permissible ceiling.

S5 Qualification fidelity
0 drops uncertainty/caveats; 1 partial; 2 retains relevant qualifications.

S6 Revocation/review semantics
0 absent where relevant; 1 generic; 2 named trigger/transition.

S7 Output usability
0 not actionable; 1 actionable with reconstruction; 2 directly usable claim/scope/caveat correction.

Additional bureaucracy measures:
B1 added required fields;
B2 new substantive assumptions;
B3 whether domain analysis had to be redone;
B4 output word count;
B5 whether output directly changes a claim/scope/caveat.

Primary comparison:
Delta = total_B - total_A.

MQR survival requires:
- positive Delta concentrated in S2/S4/S6/S7;
- no systematic loss in S1/S3/S5;
- B2=0;
- B3=false for most packets;
- anti-overrestriction control V26 must not be incorrectly rejected.

Scorer must be independent of both arm adjudicators for confirmatory use.
