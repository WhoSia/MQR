# MQR-4.7 — Outcome-Blind Representation Separator, Frozen Rival Predictions, Held-Out Engineering World-Contact, Differential Failure Localization & Whether a New Observation Can Expand Realist Authority without Historical Hindsight

## 0. Execution design
MQR-4.7 attempts the strongest available form of outcome-blindness without a new physical apparatus.

A specific held-out engineering record was selected:
- UIUC Low-Speed Airfoil Tests;
- Eppler E387 airfoil;
- low-Reynolds-number wind-tunnel polar data.

A preseal was committed **before opening the selected held-out polar values**:
- GitHub preseal commit: \`9be65f8e5fcc64efa3ecc002e9b195426b42d8e7\`.

This run therefore has procedural tool-sequence blindness with respect to the specific held-out record.

Limitation:
the adjudicating model is pretrained and E387 is a known airfoil, so pristine ignorance of all latent background knowledge cannot be guaranteed.

Thus:
- TOOL-SEQUENCE HELD-OUT = YES.
- EXTERNAL EVALUATOR BLINDNESS = NO.
- NEW PHYSICAL EXPERIMENT = NO.

## 1. Frozen rivals

### Rival A — linear attached-flow representation
Frozen form:

\[
C_L(\alpha)=a(\alpha-\alpha_0)
\]

with approximately constant lift slope extrapolated into the held-out range.

Frozen prediction:
- \(C_L\) continues approximately linearly with increasing \(\alpha\);
- no sharp stall-induced saturation/drop;
- no mechanism-specific sharp drag escalation.

### Rival B — viscous/separation-sensitive representation
Includes:
- Reynolds-sensitive boundary layer;
- transition/separation;
- finite stall onset;
- strong nonlinear drag growth near/post stall.

Frozen prediction:
- low-angle \(C_L\) can mimic Rival A;
- high-angle \(C_L\) departs materially from indefinite linear extrapolation;
- \(C_D\) rises strongly as separation grows.

## 2. Frozen separator
Strong B win if the held-out record shows, relative to the low-angle trend:

1. lift ceases approximately linear continuation in the high-angle regime; and
2. drag rises strongly in the same regime.

Weak B win if only one condition is clear.

A survives if neither occurs.

No threshold changes are allowed after reveal.

## 3. Held-out reveal
After the preseal was committed, the E387 experimental record was opened.

Selig & McGranahan (2004) report that:
- UIUC and NASA LTPT lift data agree well over the normal unstalled range;
- in the stalled regime, especially for \(\alpha>12^\circ\), the behavior departs from that unstalled trend;
- at \(Re=200{,}000\) and above, agreement is excellent up to stall and then the stalled regime becomes distinct.

The published E387 lift curves show:
- an approximately linear unstalled region;
- \(C_L\) reaching a maximum around the low-1.2 range;
- flattening and decline beyond roughly the low-teens angle range rather than indefinite linear continuation.

The drag polar in the same published dataset shows:
- low drag in the normal unstalled region;
- large movement toward higher \(C_D\) on the high-angle/high-lift edge of the polar;
- nontrivial low-Re separation-bubble structure and strong nonlinear drag behavior.

The paper explicitly attributes major low-Re behavior to laminar separation bubbles and discusses stall/unsteady effects beyond the unstalled range.

## 4. Frozen-rival verdict
### Rival A
Fails.

The held-out record does not preserve approximately linear \(C_L\) growth through the separator region.

The high-angle regime produces:
- lift saturation/decline;
- materially nonlinear drag behavior.

These were excluded from Rival A by construction.

### Rival B
Survives.

The revealed behavior matches the frozen qualitative prediction:
- low-angle quasi-linearity;
- high-angle stall/nonlinearity;
- separation-linked drag growth.

Verdict:

\[
\boxed{\text{HELD-OUT DIFFERENTIAL = STRONG B WIN}}
\]

within the tested low-Re E387 regime.

## 5. Failure localization
The result does **not** show that every viscous model is correct.

It localizes the failure of Rival A to omitted structure needed for the high-angle regime:

- finite separation/stall;
- Reynolds-sensitive boundary-layer behavior;
- nonlinear drag growth;
- transition/separation-bubble dynamics.

The failed claim is therefore not:
> "linear lift theory is useless."

It is:
> "a low-angle linear attached-flow representation can be extrapolated through the held-out high-angle regime without additional separation-sensitive structure."

That extrapolation is defeated.

## 6. Authority update
### Before reveal
Authority ceiling:

**SCOPED AUTHORITY — LOW-ANGLE LIFT TREND ONLY.**

Both rivals were allowed to survive in the baseline envelope.

### After reveal
Authority can expand to:

**SCOPED / PROVISIONALLY-REALIST — SEPARATION-SENSITIVE HIGH-ANGLE STRUCTURE IS LOAD-BEARING IN THE TESTED LOW-RE REGIME.**

The realist credit is localized to the existence and engineering relevance of nonlinear viscous/separation structure.

It does not extend automatically to:
- one exact turbulence model;
- one exact transition model;
- one exact separation-bubble parametrization;
- all Reynolds numbers;
- all airfoils.

## 7. Why this is stronger than MQR-4.6
MQR-4.6 replayed a historically known loading-coil success.

MQR-4.7 freezes:
- target;
- rival forms;
- separator;
- win conditions;

before opening the specific held-out experimental result in the execution sequence.

Therefore it adds a genuine procedural asymmetry:

\[
\text{freeze}
\rightarrow
\text{reveal}
\rightarrow
\text{adjudicate}
\]

rather than:

\[
\text{known result}
\rightarrow
\text{retrospective reconstruction}.
\]

This is epistemically stronger.

## 8. Why it is still not fully blind
The stronger claim remains unavailable because:
- the model may contain latent training knowledge about E387 or low-Re airfoil stall;
- the same adjudicator selected the target, wrote the preseal and read the reveal;
- no isolated independent scorer exists.

Thus:

\[
\boxed{
\text{tool-sequence outcome blindness}
\neq
\text{external evaluator blindness}
}
\]

MQR must preserve that distinction.

## 9. Differential failure and realist authority
MQR-4.7 gives a clean Generation-IV authority transition:

\[
[R_A,R_B]_{\Omega_0}
\rightarrow
R_B\text{-compatible survivor set in }\Omega_1.
\]

The new observation does not "prove viscous aerodynamics."

It refines the intervention/observation equivalence class by defeating the reduced rival in a regime where their predictions diverged.

That is exactly the kind of authority expansion MQR-4.5 required.

## 10. Engineering significance
The relevant engineering gain is not philosophical.

If a designer extrapolated the linear attached-flow representation into the stall regime, they would misrepresent:
- maximum attainable lift;
- margin to stall;
- high-angle drag;
- operating-envelope safety/performance.

The held-out record therefore changes actual design-relevant claim ceilings.

This is not mere semantic relabeling.

## 11. World-contact status
The revealed UIUC/LTPT record is external material evidence from physical wind-tunnel experiments.

Therefore:

**HELD-OUT ENGINEERING WORLD-CONTACT = YES.**

But:
- the experiment itself was historical;
- it was not newly commissioned by MQR;
- MQR supplied the frozen rival comparison, not the physical data generation.

## 12. Anti-overreach
Do not infer:

\[
\text{Rival B wins}
\Rightarrow
\text{all nonlinear/viscous representations are equally warranted}.
\]

The only licensed expansion is:

\[
\boxed{
\text{some separation-sensitive viscous structure is necessary for the tested high-angle regime}
}
\]

with the exact model class still open to further discrimination.

## 13. Generation-IV consequence
MQR-4.7 is the first Generation-IV stage in this branch to satisfy, within one execution sequence:

1. baseline-equivalent rival setup;
2. frozen differential prediction;
3. held-out external engineering evidence;
4. reveal after preseal;
5. post-reveal authority update;
6. explicit limitation of the strengthened claim.

That is enough to close the retrospective-only gap left by MQR-4.6.

It is not enough to claim fully independent blinding.

## 14. Next pressure
The remaining methodological weakness is latent evaluator knowledge.

A stronger successor should therefore use:
- an obscure/public data slice selected by a separate compiler;
- rival predictions generated without access to the held-out identifier/outcome;
- independent scoring after reveal;
or
- a truly new public/live engineering measurement generated after freeze.

The purpose is not to add more airfoil cases.
It is to attack **evaluator-side leakage**.

## 15. Verdict
**PASS-TOOL-SEQUENCE-OUTCOME-BLIND-SEPARATOR / PRESEAL-COMMIT-BEFORE-REVEAL / E387-HELD-OUT-WIND-TUNNEL-WORLD-CONTACT / LINEAR-ATTACHED-FLOW-RIVAL-DEFEATED / VISCOUS-SEPARATION-SENSITIVE-RIVAL-SURVIVES / DIFFERENTIAL-FAILURE-LOCALIZED-TO-HIGH-ANGLE-SEPARATION-STRUCTURE / AUTHORITY-EXPANDS-BEYOND-LOW-ANGLE-SHARED-TREND / EXACT-VISCOUS-ONTOLOGY-NOT-PROMOTED / DESIGN-RELEVANT-CLAIM-CEILING-CHANGED / EXTERNAL-EVALUATOR-BLINDNESS-NOT-CLAIMED / LATENT-MODEL-MEMORY-LEAKAGE-OPEN / GENERATION-IV-CONTINUES.**
