import Std

namespace MQR.FeedbackIdentification

/-- Restricted deterministic factorial model. These are coefficients of
    the observation contrast, not empirically established mechanisms. -/
structure World where
  drift : Nat
  response : Nat
  bias : Nat
  interaction : Nat
  deriving DecidableEq, Repr

def observed (w : World) (policy standard : Bool) : Nat :=
  w.drift + (if policy then w.response else 0) +
    (if standard then w.bias else 0) +
    (if policy && standard then w.interaction else 0)

def deploymentWorld : World := ⟨0, 1, 0, 0⟩
def calibrationWorld : World := ⟨0, 0, 1, 0⟩

theorem two_cells_do_not_identify_response :
    observed deploymentWorld false false =
      observed calibrationWorld false false ∧
    observed deploymentWorld true true =
      observed calibrationWorld true true ∧
    deploymentWorld.response ≠ calibrationWorld.response := by
  decide

theorem three_cells_identify_main_effects (w v : World)
    (h00 : observed w false false = observed v false false)
    (h10 : observed w true false = observed v true false)
    (h01 : observed w false true = observed v false true) :
    w.drift = v.drift ∧ w.response = v.response ∧ w.bias = v.bias := by
  have hd : w.drift = v.drift := by simpa [observed] using h00
  have hr : w.response = v.response := by
    have h : w.drift + w.response = v.drift + v.response := by
      simpa [observed] using h10
    rw [← hd] at h
    exact Nat.add_left_cancel h
  have hb : w.bias = v.bias := by
    have h : w.drift + w.bias = v.drift + v.bias := by
      simpa [observed] using h01
    rw [← hd] at h
    exact Nat.add_left_cancel h
  exact ⟨hd, hr, hb⟩

def zeroWorld : World := ⟨0, 0, 0, 0⟩
def interactionWorld : World := ⟨0, 0, 0, 1⟩

theorem three_cells_do_not_identify_interaction :
    observed zeroWorld false false = observed interactionWorld false false ∧
    observed zeroWorld true false = observed interactionWorld true false ∧
    observed zeroWorld false true = observed interactionWorld false true ∧
    observed zeroWorld true true ≠ observed interactionWorld true true := by
  decide

theorem four_cells_identify_coefficients (w v : World)
    (h00 : observed w false false = observed v false false)
    (h10 : observed w true false = observed v true false)
    (h01 : observed w false true = observed v false true)
    (h11 : observed w true true = observed v true true) :
    w.drift = v.drift ∧ w.response = v.response ∧
    w.bias = v.bias ∧ w.interaction = v.interaction := by
  obtain ⟨hd, hr, hb⟩ := three_cells_identify_main_effects w v h00 h10 h01
  have hi : w.interaction = v.interaction := by
    have h : w.drift + w.response + w.bias + w.interaction =
        v.drift + v.response + v.bias + v.interaction := by
      simpa [observed] using h11
    rw [← hd, ← hr, ← hb] at h
    exact Nat.add_left_cancel h
  exact ⟨hd, hr, hb, hi⟩

#print axioms two_cells_do_not_identify_response
#print axioms three_cells_identify_main_effects
#print axioms three_cells_do_not_identify_interaction
#print axioms four_cells_identify_coefficients

end MQR.FeedbackIdentification
