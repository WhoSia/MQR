import Std

namespace MQR

structure CapabilityState where
  oldA : Bool
  oldB : Bool
  newC : Bool
  oldDistinctionRecoverable : Bool
  independentSupport : Bool
  deriving DecidableEq, Repr

def LocalDominates (s : CapabilityState) : Bool :=
  s.oldA && s.oldB && s.oldDistinctionRecoverable && s.independentSupport

def strictGood : CapabilityState :=
  { oldA := true, oldB := true, newC := true,
    oldDistinctionRecoverable := true, independentSupport := true }

def hiddenLoss : CapabilityState :=
  { oldA := false, oldB := true, newC := true,
    oldDistinctionRecoverable := false, independentSupport := true }

theorem novel_channel_does_not_compensate_old_loss :
    hiddenLoss.newC = true ∧ LocalDominates hiddenLoss = false := by
  exact ⟨rfl, rfl⟩

theorem strict_local_dominance_requires_old_recoverability :
    LocalDominates strictGood = true ∧
    strictGood.oldDistinctionRecoverable = true := by
  exact ⟨rfl, rfl⟩

structure TraceabilityState where
  traceable : Bool
  purposeAdequate : Bool
  independentFailureExposure : Bool
  deriving DecidableEq, Repr

def traceOnly : TraceabilityState :=
  { traceable := true, purposeAdequate := false, independentFailureExposure := false }

def CapabilityCertified (t : TraceabilityState) : Bool :=
  t.traceable && t.purposeAdequate && t.independentFailureExposure

theorem traceability_alone_does_not_force_capability_dominance :
    traceOnly.traceable = true ∧ CapabilityCertified traceOnly = false := by
  exact ⟨rfl, rfl⟩

structure MathTransportState where
  provesMore : Bool
  oldObligationsRecoverable : Bool
  semanticBridge : Bool
  deriving DecidableEq, Repr

def strongerSyntaxLostSemantics : MathTransportState :=
  { provesMore := true, oldObligationsRecoverable := false, semanticBridge := false }

def MathAuthorityDominates (m : MathTransportState) : Bool :=
  m.oldObligationsRecoverable && m.semanticBridge

theorem proving_more_does_not_force_authority_dominance :
    strongerSyntaxLostSemantics.provesMore = true ∧
    MathAuthorityDominates strongerSyntaxLostSemantics = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.novel_channel_does_not_compensate_old_loss
#print axioms MQR.strict_local_dominance_requires_old_recoverability
#print axioms MQR.traceability_alone_does_not_force_capability_dominance
#print axioms MQR.proving_more_does_not_force_authority_dominance

end MQR
