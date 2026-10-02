import Std

namespace MQR

structure ScopedContact where
  scientificSplit : Bool
  available : Bool
  permitted : Bool
  resourceOK : Bool
  deriving DecidableEq, Repr

def Executable (q : ScopedContact) : Bool :=
  q.available && q.permitted && q.resourceOK

def ScientificClosureDefeater (q : ScopedContact) : Bool :=
  q.scientificSplit

def ExecutionClosureDefeater (q : ScopedContact) : Bool :=
  q.scientificSplit && Executable q

def blockedScientificSeparator : ScopedContact :=
  { scientificSplit := true, available := true, permitted := false, resourceOK := true }

def unlockedScientificSeparator : ScopedContact :=
  { scientificSplit := true, available := true, permitted := true, resourceOK := true }

theorem scientific_defeater_need_not_be_execution_defeater :
    ScientificClosureDefeater blockedScientificSeparator = true ∧
    ExecutionClosureDefeater blockedScientificSeparator = false := by
  exact ⟨rfl, rfl⟩

theorem permission_unlock_can_change_execution_defeat_without_changing_scientific_defeat :
    ScientificClosureDefeater blockedScientificSeparator =
      ScientificClosureDefeater unlockedScientificSeparator ∧
    ExecutionClosureDefeater blockedScientificSeparator ≠
      ExecutionClosureDefeater unlockedScientificSeparator := by
  exact ⟨rfl, by decide⟩

theorem execution_defeater_implies_scientific_defeater
    (q : ScopedContact)
    (h : ExecutionClosureDefeater q = true) :
    ScientificClosureDefeater q = true := by
  unfold ExecutionClosureDefeater at h
  unfold ScientificClosureDefeater
  exact (Bool.and_eq_true.mp h).1

#print axioms MQR.scientific_defeater_need_not_be_execution_defeater
#print axioms MQR.permission_unlock_can_change_execution_defeat_without_changing_scientific_defeat
#print axioms MQR.execution_defeater_implies_scientific_defeater

end MQR
