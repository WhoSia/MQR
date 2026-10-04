import Std

namespace MQR

structure RecoverabilityState where
  exactInverse : Bool
  claimSufficientDecoder : Bool
  posthocPredictor : Bool
  modelIndependent : Bool
  semanticScopePreserved : Bool
  deriving DecidableEq, Repr

def RecoverableAtScope (r : RecoverabilityState) : Bool :=
  r.semanticScopePreserved &&
  r.modelIndependent &&
  (r.exactInverse || r.claimSufficientDecoder)

def posthocOnly : RecoverabilityState :=
  { exactInverse := false, claimSufficientDecoder := false,
    posthocPredictor := true, modelIndependent := false,
    semanticScopePreserved := true }

def sufficientOnly : RecoverabilityState :=
  { exactInverse := false, claimSufficientDecoder := true,
    posthocPredictor := false, modelIndependent := true,
    semanticScopePreserved := true }

theorem posthoc_prediction_does_not_force_recoverability :
    posthocOnly.posthocPredictor = true ∧
    RecoverableAtScope posthocOnly = false := by
  exact ⟨rfl, rfl⟩

theorem raw_invertibility_not_necessary_for_scope_recoverability :
    sufficientOnly.exactInverse = false ∧
    RecoverableAtScope sufficientOnly = true := by
  exact ⟨rfl, rfl⟩

structure ExtensionState where
  provesMore : Bool
  conservativeOnOldLanguage : Bool
  semanticBridge : Bool
  deriving DecidableEq, Repr

def nonconservativeStrong : ExtensionState :=
  { provesMore := true, conservativeOnOldLanguage := false, semanticBridge := false }

def AuthorityRecoverable (e : ExtensionState) : Bool :=
  e.conservativeOnOldLanguage && e.semanticBridge

theorem stronger_formal_system_can_fail_authority_recoverability :
    nonconservativeStrong.provesMore = true ∧
    AuthorityRecoverable nonconservativeStrong = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.posthoc_prediction_does_not_force_recoverability
#print axioms MQR.raw_invertibility_not_necessary_for_scope_recoverability
#print axioms MQR.stronger_formal_system_can_fail_authority_recoverability

end MQR
