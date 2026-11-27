import MQR.ScientificStateQuotient

namespace MQR.PartialObservation

inductive Phase where
  | zero | one | two
  deriving DecidableEq, Repr

def next (persistent : Bool) (s : Phase) (p : Bool) : Phase :=
  if p then
    match s with
    | .zero => .one
    | .one => .two
    | .two => if persistent then .one else .zero
  else .zero

def coarseLabel : Phase → Bool
  | .two => true
  | _ => false

def system (persistent : Bool) : MQR.AuthoritySystem Phase Bool Bool :=
  { label := coarseLabel, step := next persistent }

def stateAfter (persistent : Bool) (word : List Bool) : Phase :=
  MQR.run (system persistent) .zero word

def observed (persistent : Bool) (word : List Bool) : Bool :=
  coarseLabel (stateAfter persistent word)

theorem state_agreement_zero :
    stateAfter false [] = stateAfter true [] := rfl

theorem state_agreement_one (p : Bool) :
    stateAfter false [p] = stateAfter true [p] := by
  cases p <;> rfl

theorem state_agreement_two (p q : Bool) :
    stateAfter false [p,q] = stateAfter true [p,q] := by
  cases p <;> cases q <;> rfl

theorem coarse_agreement_three (p q r : Bool) :
    observed false [p,q,r] = observed true [p,q,r] := by
  cases p <;> cases q <;> cases r <;> rfl

theorem coarse_separator_four :
    observed false [true,true,true,true] ≠ observed true [true,true,true,true] := by
  decide

theorem fine_separator_three :
    stateAfter false [true,true,true] ≠ stateAfter true [true,true,true] := by
  decide

/-- A common deterministic state sensor cannot reveal a difference before
    the states themselves differ; this does not cover history-aware sensors. -/
theorem any_state_sensor_agrees_two {O : Type} (sensor : Phase → O) (p q : Bool) :
    sensor (stateAfter false [p,q]) = sensor (stateAfter true [p,q]) :=
  congrArg sensor (state_agreement_two p q)

/-- A refined sensor preserves old distinctions if the old observation
    factors through it. No converse is assumed. -/
theorem refinement_preserves_distinction {S O L : Type}
    (fine : S → O) (forget : O → L) (s t : S)
    (h : forget (fine s) ≠ forget (fine t)) : fine s ≠ fine t := by
  intro eq
  exact h (congrArg forget eq)

#print axioms state_agreement_two
#print axioms coarse_agreement_three
#print axioms coarse_separator_four
#print axioms fine_separator_three
#print axioms any_state_sensor_agrees_two
#print axioms refinement_preserves_distinction

end MQR.PartialObservation
