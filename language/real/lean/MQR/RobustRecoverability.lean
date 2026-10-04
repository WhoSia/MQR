import Std

namespace MQR

structure RobustRecovery where
  nominalRecovery : Bool
  perturbationStable : Bool
  independentSeparator : Bool
  semanticBridge : Bool
  addsNew : Bool
  deriving DecidableEq, Repr

def RobustlyRecoverable (r : RobustRecovery) : Bool :=
  r.nominalRecovery &&
  r.perturbationStable &&
  r.independentSeparator &&
  r.semanticBridge

def nominalFragile : RobustRecovery :=
  { nominalRecovery := true, perturbationStable := false,
    independentSeparator := true, semanticBridge := true, addsNew := true }

def robustGain : RobustRecovery :=
  { nominalRecovery := true, perturbationStable := true,
    independentSeparator := true, semanticBridge := true, addsNew := true }

def selfModelOnly : RobustRecovery :=
  { nominalRecovery := true, perturbationStable := false,
    independentSeparator := false, semanticBridge := true, addsNew := false }

theorem nominal_recovery_does_not_force_robust_recovery :
    nominalFragile.nominalRecovery = true ∧
    RobustlyRecoverable nominalFragile = false := by
  exact ⟨rfl, rfl⟩

theorem perturbation_stable_separator_can_support_local_robust_recovery :
    RobustlyRecoverable robustGain = true ∧ robustGain.addsNew = true := by
  exact ⟨rfl, rfl⟩

theorem successor_self_model_is_not_independent_recovery :
    selfModelOnly.nominalRecovery = true ∧
    selfModelOnly.independentSeparator = false ∧
    RobustlyRecoverable selfModelOnly = false := by
  exact ⟨rfl, rfl, rfl⟩

structure MathRobustTransport where
  provesMore : Bool
  conservativeOnInheritedFamily : Bool
  semanticBackTranslation : Bool
  deriving DecidableEq, Repr

def nonconservativeGain : MathRobustTransport :=
  { provesMore := true, conservativeOnInheritedFamily := false,
    semanticBackTranslation := false }

def RobustMathInheritance (m : MathRobustTransport) : Bool :=
  m.conservativeOnInheritedFamily && m.semanticBackTranslation

theorem nonconservative_gain_does_not_force_robust_math_inheritance :
    nonconservativeGain.provesMore = true ∧
    RobustMathInheritance nonconservativeGain = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.nominal_recovery_does_not_force_robust_recovery
#print axioms MQR.perturbation_stable_separator_can_support_local_robust_recovery
#print axioms MQR.successor_self_model_is_not_independent_recovery
#print axioms MQR.nonconservative_gain_does_not_force_robust_math_inheritance

end MQR
