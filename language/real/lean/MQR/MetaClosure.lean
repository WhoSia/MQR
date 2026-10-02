import Std

namespace MQR

structure VisibleView where
  currentEnvelope : Nat
  generatorOutput : Nat
  gateState : Nat
  deriving DecidableEq, Repr

structure ContactWorld where
  visible : VisibleView
  hiddenAdmissibleExterior : Bool
  deriving DecidableEq, Repr

def TrueClosure (w : ContactWorld) : Bool :=
  !w.hiddenAdmissibleExterior

def v0 : VisibleView :=
  { currentEnvelope := 0, generatorOutput := 0, gateState := 0 }

def closedWorld : ContactWorld :=
  { visible := v0, hiddenAdmissibleExterior := false }

def openWorld : ContactWorld :=
  { visible := v0, hiddenAdmissibleExterior := true }

theorem same_visible_view_opposite_true_closure :
    closedWorld.visible = openWorld.visible ∧
    TrueClosure closedWorld = true ∧
    TrueClosure openWorld = false := by
  exact ⟨rfl, rfl, rfl⟩

theorem visible_only_certifier_cannot_be_correct_on_both
    (cert : VisibleView → Bool) :
    ¬ (cert closedWorld.visible = TrueClosure closedWorld ∧
       cert openWorld.visible = TrueClosure openWorld) := by
  intro h
  rcases h with ⟨hc, ho⟩
  have htf : true = false := by
    calc
      true = cert closedWorld.visible := hc.symm
      _ = cert openWorld.visible := by rfl
      _ = false := ho
  cases htf

#print axioms MQR.same_visible_view_opposite_true_closure
#print axioms MQR.visible_only_certifier_cannot_be_correct_on_both

end MQR
