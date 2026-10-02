import Std

namespace MQR

structure ContactState where
  currentEnvelope : Nat
  rivalGenerator : Bool
  instrumentGenerator : Bool
  externalGenerator : Bool
  techUnlocked : Bool
  budgetHigh : Bool
  ethicsOpen : Bool
  revisionState : Nat
  ancestryLabel : Nat
  deriving DecidableEq, Repr

def RivalAdmission (s : ContactState) : Bool :=
  s.rivalGenerator

def InstrumentAdmission (s : ContactState) : Bool :=
  s.instrumentGenerator && s.techUnlocked

def ExternalBudgetAdmission (s : ContactState) : Bool :=
  s.externalGenerator && s.budgetHigh

def ExternalEthicsAdmission (s : ContactState) : Bool :=
  s.externalGenerator && s.ethicsOpen

def FutureSignature (s : ContactState) : Bool × Bool × Bool × Bool :=
  (RivalAdmission s, InstrumentAdmission s, ExternalBudgetAdmission s, ExternalEthicsAdmission s)

def OperationalState (s : ContactState) :
    Nat × Bool × Bool × Bool × Bool × Bool × Bool × Nat :=
  (s.currentEnvelope, s.rivalGenerator, s.instrumentGenerator, s.externalGenerator,
   s.techUnlocked, s.budgetHigh, s.ethicsOpen, s.revisionState)

theorem same_current_envelope_can_have_different_future_contact :
    ∃ a b : ContactState,
      a.currentEnvelope = b.currentEnvelope ∧
      FutureSignature a ≠ FutureSignature b := by
  refine ⟨
    { currentEnvelope := 0, rivalGenerator := false, instrumentGenerator := false,
      externalGenerator := false, techUnlocked := false, budgetHigh := false,
      ethicsOpen := false, revisionState := 0, ancestryLabel := 10 },
    { currentEnvelope := 0, rivalGenerator := true, instrumentGenerator := true,
      externalGenerator := true, techUnlocked := false, budgetHigh := false,
      ethicsOpen := false, revisionState := 0, ancestryLabel := 20 },
    rfl, ?_⟩
  decide

theorem operational_identity_implies_future_identity
    (a b : ContactState)
    (h : OperationalState a = OperationalState b) :
    FutureSignature a = FutureSignature b := by
  cases a
  cases b
  simp [OperationalState] at h
  rcases h with ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  rfl

theorem ancestry_label_need_not_change_future :
    ∃ a b : ContactState,
      a.ancestryLabel ≠ b.ancestryLabel ∧
      OperationalState a = OperationalState b ∧
      FutureSignature a = FutureSignature b := by
  refine ⟨
    { currentEnvelope := 0, rivalGenerator := true, instrumentGenerator := true,
      externalGenerator := true, techUnlocked := false, budgetHigh := false,
      ethicsOpen := false, revisionState := 0, ancestryLabel := 1 },
    { currentEnvelope := 0, rivalGenerator := true, instrumentGenerator := true,
      externalGenerator := true, techUnlocked := false, budgetHigh := false,
      ethicsOpen := false, revisionState := 0, ancestryLabel := 2 },
    ?_, rfl, rfl⟩
  decide

#print axioms MQR.same_current_envelope_can_have_different_future_contact
#print axioms MQR.operational_identity_implies_future_identity
#print axioms MQR.ancestry_label_need_not_change_future

end MQR
