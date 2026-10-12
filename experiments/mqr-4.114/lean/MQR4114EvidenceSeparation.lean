/-!
MQR-4.114 P2-B: evidence non-amplification and independent witness.
Constructed mathematical functions only. Nothing here validates an actual
calibration source, psychological scale, experiment, or novel physical law.
-/
namespace MQR4114P2B

theorem computed_third_channel_does_not_split
    {W O A : Type}
    (observe : W → O) (derived : O → A)
    (world₁ world₂ : W)
    (same : observe world₁ = observe world₂) :
    (observe world₁, derived (observe world₁)) =
    (observe world₂, derived (observe world₂)) := by
  simp [same]

theorem constructed_independent_witness_splits
    {W O R : Type}
    (observe : W → O) (reference : W → R)
    (world₁ world₂ : W)
    (different : reference world₁ ≠ reference world₂) :
    (observe world₁, reference world₁) ≠
    (observe world₂, reference world₂) := by
  intro h
  apply different
  exact congrArg Prod.snd h

theorem postprocessing_cannot_restore_injectivity
    {W O A : Type}
    (observe : W → O) (derived : O → A)
    (world₁ world₂ : W)
    (distinct : world₁ ≠ world₂)
    (same : observe world₁ = observe world₂) :
    ¬ Function.Injective (fun w => (observe w, derived (observe w))) := by
  intro inj
  apply distinct
  exact inj (computed_third_channel_does_not_split observe derived world₁ world₂ same)

def instrument (quantity calibrationBias : Nat) : Nat :=
  quantity + calibrationBias

theorem two_hidden_histories_same_readout :
    instrument 1 0 = instrument 0 1 := by
  decide

def timeDrivenGoal (horizon : Bool) : Bool := horizon
def ageDrivenGoal (age : Bool) : Bool := age

theorem observed_cohort_cannot_split (age : Bool) :
    timeDrivenGoal age = ageDrivenGoal age := by
  rfl

theorem changed_horizon_separates_models (age : Bool) :
    timeDrivenGoal (Bool.not age) ≠ ageDrivenGoal age := by
  cases age <;> decide

end MQR4114P2B
