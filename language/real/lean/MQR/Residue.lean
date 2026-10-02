import Std

namespace MQR

/-- A declared class has zero internal residue exactly when every relevant probe is tested. -/
def InternalResidueEmpty {Probe : Type} (Relevant Tested : Probe → Prop) : Prop :=
  ∀ p, Relevant p → Tested p

/-- For an explicitly bounded probe index Fin n, complete coverage implies zero internal residue.
    This theorem proves only the closure statement inside the declared class. -/
theorem zeroInternalResidueOfComplete
    {n : Nat}
    (Relevant Tested : Fin n → Prop)
    (coverage : ∀ p, Relevant p → Tested p) :
    InternalResidueEmpty Relevant Tested :=
  coverage

/-- A larger probe language can contain a fresh probe not covered by the old tested predicate.
    This is a syntactic extension theorem, not a claim that nature realizes the fresh probe. -/
inductive Extended (Probe : Type) where
  | old : Probe → Extended Probe
  | fresh : Extended Probe

def liftTested {Probe : Type} (Tested : Probe → Prop) : Extended Probe → Prop
  | .old p => Tested p
  | .fresh => False

theorem extensionContainsUncoveredProbe
    (Probe : Type) (Tested : Probe → Prop) :
    ∃ p : Extended Probe, ¬ liftTested Tested p := by
  refine ⟨Extended.fresh, ?_⟩
  intro h
  exact h

inductive AuthorityStatus where
  | fail
  | hold
  | pass
  deriving DecidableEq, Repr

def AuthorityStatus.rank : AuthorityStatus → Nat
  | .fail => 0
  | .hold => 1
  | .pass => 2

def NoLaunder : AuthorityStatus → AuthorityStatus → Prop
  | .fail, .fail => True
  | .fail, .hold => False
  | .fail, .pass => False
  | .hold, .fail => True
  | .hold, .hold => True
  | .hold, .pass => False
  | .pass, .fail => True
  | .pass, .hold => True
  | .pass, .pass => True

theorem holdMayStayHold : NoLaunder .hold .hold :=
  True.intro

theorem checkedProofCannotRaiseHoldToPass : ¬ NoLaunder .hold .pass :=
  fun h => h

theorem failedPremiseCannotAuthorizeHold : ¬ NoLaunder .fail .hold :=
  fun h => h

#print axioms MQR.zeroInternalResidueOfComplete
#print axioms MQR.extensionContainsUncoveredProbe
#print axioms MQR.checkedProofCannotRaiseHoldToPass

end MQR
