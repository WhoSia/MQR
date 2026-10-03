import Std

namespace MQR

structure Inquiry where
  fullTargetSpecified : Bool
  structuredDirectedness : Bool
  reproducibleContact : Bool
  defeatRoute : Bool
  deriving DecidableEq, Repr

def LegitimateExploratory (q : Inquiry) : Bool :=
  q.structuredDirectedness && q.reproducibleContact && q.defeatRoute

def exploratoryWitness : Inquiry :=
  {
    fullTargetSpecified := false
    structuredDirectedness := true
    reproducibleContact := true
    defeatRoute := true
  }

theorem full_target_specification_not_necessary_for_legitimate_exploration :
    exploratoryWitness.fullTargetSpecified = false ∧
    LegitimateExploratory exploratoryWitness = true := by
  exact ⟨rfl, rfl⟩

structure MathAuthorityState where
  theoremLabel : Nat
  framework : Nat
  semanticTruth : Bool
  checkedProof : Bool
  deriving DecidableEq, Repr

def SameLabel (a b : MathAuthorityState) : Bool :=
  a.theoremLabel == b.theoremLabel

def fA : MathAuthorityState :=
  { theoremLabel := 7, framework := 1, semanticTruth := true, checkedProof := true }

def fB : MathAuthorityState :=
  { theoremLabel := 7, framework := 2, semanticTruth := false, checkedProof := false }

theorem same_theorem_label_does_not_force_same_semantic_truth :
    SameLabel fA fB = true ∧
    fA.semanticTruth ≠ fB.semanticTruth := by
  exact ⟨rfl, by decide⟩

structure ReliabilityCase where
  testedTheoryControlsReliability : Bool
  independentCheck : Bool
  deriving DecidableEq, Repr

def CircularityHold (r : ReliabilityCase) : Bool :=
  r.testedTheoryControlsReliability && !r.independentCheck

def selfGated : ReliabilityCase :=
  { testedTheoryControlsReliability := true, independentCheck := false }

theorem theory_self_gated_reliability_is_flagged :
    CircularityHold selfGated = true := by
  rfl

#print axioms MQR.full_target_specification_not_necessary_for_legitimate_exploration
#print axioms MQR.same_theorem_label_does_not_force_same_semantic_truth
#print axioms MQR.theory_self_gated_reliability_is_flagged

end MQR
