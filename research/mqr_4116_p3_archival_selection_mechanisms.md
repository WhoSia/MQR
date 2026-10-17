# MQR-4.116 P3 — Archival Selection Mechanisms and Observed Graph Distortion

2026-10-17. Formal finite countermodels; 4.115 and 4.116 OPEN.

A source-level retention variable R determines whether an evidence/citation edge is observable. MCAR: P(R=1|A,Y)=P(R=1); MAR relative to observed authority A: P(R=1|A,Y)=P(R=1|A); MNAR relative to recorded A: retention additionally depends on latent claim-relevant outcome Y. These labels depend on which variables are observed; authority-dependence alone is not MNAR if authority A is fully observed.

A transparent four-cell population has equal P(A,Y)=1/4. For MCAR P(R=1)=1/2; MAR retention 3/4 for A=1, 1/4 for A=0; MNAR retention 3/4 for Y=1, 1/4 for Y=0. The observed rate P(Y=1|R=1) is respectively 1/2, 1/2, 3/4, whereas underlying P(Y=1)=1/2. This is a counterexample to treating selected archives as representative without mechanism assumptions; it is not evidence that Greenberg data are MNAR. Finite rational arithmetic checks located at experiments/mqr-4.116/p3_selection_mechanisms.py.

Research-original question reread from 4.115 P0: experimental method→logical prerequisite directed graph (7 templates, 51 edges in prior model) has degree statistics sensitive to coding granularity, and now source retention adds a second sensitivity. Observed in-degree equals a selection-weighted sum of source-target edges; changing selection alone may change it with the underlying graph fixed. No universal arrow concentration law follows.

Existing Harvest LR-20260905-A W05, K02, K04, C2 reused as historical prompts only. P2 missing certificate and defeater states remain UNKNOWN rather than FALSE. Existing 161-edge Greenberg subset and 7 visually ambiguous row stances not augmented. Physical independence and missingness mechanism identification HOLD.

P4: produce observationally equivalent MCAR/MNAR models with different target warrant states; specify extra retention audits and source-root verification required to separate them. An empirical causal claim requires access to sampling frames, absent-source indicators or justified restrictions, not only reported edges.
