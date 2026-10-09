import Lean

/-!
MQR-4.100-P1: logical scope of observation-quotient refinement.
Elementary general-function propositions, not a new statistical theorem.
The observation objects may themselves be probability-law vectors.
The theorem requires law-preserving projection at EACH theta.
-/
namespace MQR4100

def ObsEq {Θ O : Type} (experiment : Θ → O) (a b : Θ) : Prop :=
  experiment a = experiment b

theorem projection_implies_observation_refinement
    {Θ Old New : Type}
    (old : Θ → Old) (joint : Θ → New) (project : New → Old)
    (compatible : ∀ t, project (joint t) = old t)
    {a b : Θ}
    (h : ObsEq joint a b) :
    ObsEq old a b := by
  dsimp [ObsEq] at h ⊢
  calc
    old a = project (joint a) := (compatible a).symm
    _ = project (joint b) := congrArg project h
    _ = old b := compatible b

theorem target_identification_preserved_under_projection
    {Θ Old New Target : Type}
    (old : Θ → Old) (joint : Θ → New) (project : New → Old)
    (compatible : ∀ t, project (joint t) = old t)
    (target : Θ → Target)
    (alreadyIdentified : ∀ a b, ObsEq old a b → target a = target b) :
    ∀ a b, ObsEq joint a b → target a = target b := by
  intro a b eq
  exact alreadyIdentified a b
    (projection_implies_observation_refinement old joint project compatible eq)

/- Model enlargement is NOT appending an observation with compatible marginal law.
   Different theta / nuisance values can share relaxed signals. -/
def relaxedObservation (p : Bool × Bool) : Bool := p.1 != p.2
def latentTarget (p : Bool × Bool) : Bool := p.1

theorem model_expansion_can_destroy_old_target_identification :
    relaxedObservation (false, false) = relaxedObservation (true, true) ∧
    latentTarget (false, false) ≠ latentTarget (true, true) := by
  decide

def duplicated (b : Bool) : Bool × Bool := (b, b)
theorem duplicate_does_not_split_fibers (a b : Bool) :
    duplicated a = duplicated b ↔ a = b := by
  constructor
  · intro h
    exact congrArg Prod.fst h
  · intro h
    rw [h]

def flatExperiment (_ : Bool) : Unit := ()
theorem flat_experiment_cannot_identify_full_boolean_target :
    ObsEq flatExperiment false true ∧ (false : Bool) ≠ true := by
  decide

end MQR4100
