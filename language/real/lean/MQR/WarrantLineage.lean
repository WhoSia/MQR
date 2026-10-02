import Std

namespace MQR

inductive AuthorityOutcome where
  | stable
  | holdReauthorize
  | reopenRequired
  | holdReasonReconstitute
  deriving DecidableEq, Repr

structure FrozenHistory where
  authorization : Nat
  provenance : Nat
  defeater : Nat
  revision : Nat
  deriving DecidableEq, Repr

def ExtensionalState (_h : FrozenHistory) : Nat := 0

def FourAxisState (h : FrozenHistory) : Nat × Nat × Nat × Nat :=
  (h.authorization, h.provenance, h.defeater, h.revision)

def FutureSignature (h : FrozenHistory) : Nat × Nat × Nat × Nat :=
  (h.authorization % 3, h.provenance % 2, h.defeater % 2, h.revision % 3)

def PredictivelyEquivalent (a b : FrozenHistory) : Prop :=
  FutureSignature a = FutureSignature b

theorem extensional_state_can_be_equal_while_future_signature_differs :
    ∃ a b : FrozenHistory,
      ExtensionalState a = ExtensionalState b ∧
      FutureSignature a ≠ FutureSignature b := by
  refine ⟨
    { authorization := 0, provenance := 0, defeater := 0, revision := 0 },
    { authorization := 1, provenance := 0, defeater := 0, revision := 0 },
    rfl, ?_⟩
  decide

theorem predictive_equivalence_is_reflexive (a : FrozenHistory) :
    PredictivelyEquivalent a a := by
  rfl

theorem predictive_equivalence_is_symmetric (a b : FrozenHistory) :
    PredictivelyEquivalent a b → PredictivelyEquivalent b a := by
  intro h
  exact h.symm

theorem predictive_equivalence_is_transitive (a b c : FrozenHistory) :
    PredictivelyEquivalent a b →
    PredictivelyEquivalent b c →
    PredictivelyEquivalent a c := by
  intro hab hbc
  exact hab.trans hbc

theorem four_axis_identity_implies_predictive_equivalence (a b : FrozenHistory)
    (h : a = b) :
    PredictivelyEquivalent a b := by
  subst b
  rfl

theorem predictive_equivalence_does_not_imply_history_identity :
    ∃ a b : FrozenHistory,
      PredictivelyEquivalent a b ∧
      a ≠ b := by
  refine ⟨
    { authorization := 0, provenance := 0, defeater := 0, revision := 0 },
    { authorization := 3, provenance := 2, defeater := 2, revision := 3 },
    ?_, ?_⟩
  · rfl
  · decide

theorem predictive_equivalence_does_not_imply_four_axis_identity :
    ∃ a b : FrozenHistory,
      PredictivelyEquivalent a b ∧
      FourAxisState a ≠ FourAxisState b := by
  refine ⟨
    { authorization := 0, provenance := 0, defeater := 0, revision := 0 },
    { authorization := 3, provenance := 2, defeater := 2, revision := 3 },
    ?_, ?_⟩
  · rfl
  · decide

#print axioms MQR.extensional_state_can_be_equal_while_future_signature_differs
#print axioms MQR.predictive_equivalence_is_reflexive
#print axioms MQR.predictive_equivalence_is_symmetric
#print axioms MQR.predictive_equivalence_is_transitive
#print axioms MQR.four_axis_identity_implies_predictive_equivalence
#print axioms MQR.predictive_equivalence_does_not_imply_history_identity
#print axioms MQR.predictive_equivalence_does_not_imply_four_axis_identity

end MQR
