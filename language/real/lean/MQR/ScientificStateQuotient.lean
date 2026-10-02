import Std

namespace MQR

universe u v w

/-- Deterministic labeled transition system used as the formal boundary of MQR-4.66. -/
structure AuthoritySystem (S : Type u) (E : Type v) (L : Type w) where
  label : S → L
  step : S → E → S

def run
    {S : Type u} {E : Type v} {L : Type w}
    (M : AuthoritySystem S E L) : S → List E → S
  | s, [] => s
  | s, e :: es => run M (M.step s e) es

/--
A relation is label-respecting and transition-congruent when related states
have equal current labels and remain related after every event.
-/
structure StableAuthorityRelation
    {S : Type u} {E : Type v} {L : Type w}
    (M : AuthoritySystem S E L) (R : S → S → Prop) where
  label_eq : ∀ {s t}, R s t → M.label s = M.label t
  step_closed : ∀ {s t}, R s t → ∀ e, R (M.step s e) (M.step t e)

/--
Stable authority equivalence preserves relatedness after every finite event word.
-/
theorem stableRelationPreservesRun
    {S : Type u} {E : Type v} {L : Type w}
    (M : AuthoritySystem S E L) (R : S → S → Prop)
    (hR : StableAuthorityRelation M R)
    {s t : S} (hst : R s t) :
    ∀ es : List E, R (run M s es) (run M t es) := by
  intro es
  induction es generalizing s t with
  | nil =>
      simpa [run] using hst
  | cons e es ih =>
      simp [run]
      exact ih (hR.step_closed hst e)

/--
Consequently, stable authority equivalence preserves labels after every finite continuation.
This is the formal Q4 soundness boundary; it does not assert that the chosen label is a
complete scientific description.
-/
theorem stableRelationPreservesFiniteTraceLabels
    {S : Type u} {E : Type v} {L : Type w}
    (M : AuthoritySystem S E L) (R : S → S → Prop)
    (hR : StableAuthorityRelation M R)
    {s t : S} (hst : R s t) :
    ∀ es : List E, M.label (run M s es) = M.label (run M t es) := by
  intro es
  exact hR.label_eq (stableRelationPreservesRun M R hR hst es)

/--
If a candidate relation merges two states whose labels differ after some continuation,
then that relation cannot satisfy the stable authority conditions.
-/
theorem distinguishingContinuationRefutesStability
    {S : Type u} {E : Type v} {L : Type w}
    (M : AuthoritySystem S E L) (R : S → S → Prop)
    {s t : S} (hst : R s t)
    (es : List E)
    (hne : M.label (run M s es) ≠ M.label (run M t es)) :
    ¬ StableAuthorityRelation M R := by
  intro hStable
  exact hne (stableRelationPreservesFiniteTraceLabels M R hStable hst es)

#print axioms MQR.stableRelationPreservesRun
#print axioms MQR.stableRelationPreservesFiniteTraceLabels
#print axioms MQR.distinguishingContinuationRefutesStability

end MQR
