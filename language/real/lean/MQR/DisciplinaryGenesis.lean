import Std

namespace MQR.DisciplinaryGenesis

/-- A deliberately small causal witness, not a historical data model.
    Context supplies method availability in the observed regime. -/
inductive Explanation
  | methodMediated
  | commonContext
  deriving DecidableEq, Repr

def outcome (e : Explanation) (context readiness method : Bool) : Bool :=
  match e with
  | .methodMediated => method && readiness
  | .commonContext => context && readiness

def factual (e : Explanation) (context readiness : Bool) : Bool :=
  outcome e context readiness context

theorem equal_observations (context readiness : Bool) :
    factual .methodMediated context readiness =
      factual .commonContext context readiness := by
  rfl

theorem factual_success_implies_method (e : Explanation) (u r : Bool)
    (h : factual e u r = true) : u = true := by
  cases e <;> cases u <;> cases r <;> simp [factual, outcome] at *

theorem same_observations_different_withdrawal :
    (∀ u r, factual .methodMediated u r = factual .commonContext u r) ∧
    outcome .methodMediated true true false = false ∧
    outcome .commonContext true true false = true := by
  exact ⟨equal_observations, rfl, rfl⟩

/-- A method may fail to produce a field when complementary readiness is absent. -/
theorem method_not_sufficient :
    outcome .methodMediated true false true = false := rfl

/-- A specific method may be dispensable even if at least one method
    from a specified family is required. -/
def familyOutcome (a b ready : Bool) : Bool := (a || b) && ready

theorem family_requirement_not_token_requirement :
    (∀ ready, familyOutcome false false ready = false) ∧
    familyOutcome false true true = true ∧
    familyOutcome true false true = true := by
  exact ⟨fun _ => rfl, rfl, rfl⟩

#print axioms equal_observations
#print axioms factual_success_implies_method
#print axioms same_observations_different_withdrawal
#print axioms method_not_sufficient
#print axioms family_requirement_not_token_requirement

end MQR.DisciplinaryGenesis
