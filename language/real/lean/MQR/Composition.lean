import Std
import MQR.Transfer

namespace MQR

theorem authorityMeetAssociative
    (a b c : AuthorityStatus) :
    AuthorityStatus.meet (AuthorityStatus.meet a b) c =
      AuthorityStatus.meet a (AuthorityStatus.meet b c) := by
  cases a <;> cases b <;> cases c <;> rfl

theorem authorityMeetPassIdentity
    (a : AuthorityStatus) :
    AuthorityStatus.meet .pass a = a ∧
      AuthorityStatus.meet a .pass = a := by
  cases a <;> decide

theorem noLaunderTransitive
    (a b c : AuthorityStatus)
    (hab : NoLaunder a b)
    (hbc : NoLaunder b c) :
    NoLaunder a c := by
  cases a <;> cases b <;> cases c <;> trivial

structure ThreeStepReceipt where
  firstLocal : Bool
  secondLocal : Bool
  direct : Bool
  deriving DecidableEq, Repr

def adjacentPassDirectFail : ThreeStepReceipt :=
  { firstLocal := true, secondLocal := true, direct := false }

theorem adjacentPassDoesNotEntailDirectPass :
    adjacentPassDirectFail.firstLocal = true ∧
      adjacentPassDirectFail.secondLocal = true ∧
      adjacentPassDirectFail.direct = false := by
  decide

theorem authorityBaselineResetCanHideInflation :
    NoLaunder .pass .pass ∧
      ¬ NoLaunder .hold .pass := by
  constructor
  · trivial
  · exact checkedProofCannotRaiseHoldToPass

theorem localAssumptionsCanBeSeparatelySatisfiableButJointlyInconsistent :
    (∃ x : Bool, x = true) ∧
      (∃ x : Bool, x = false) ∧
      ¬ (∃ x : Bool, x = true ∧ x = false) := by
  refine ⟨⟨true, rfl⟩, ⟨false, rfl⟩, ?_⟩
  rintro ⟨x, hx1, hx2⟩
  cases hx1
  cases hx2

structure DefeatSegment where
  localReachable : Bool
  sourceToFinalReachable : Bool
  deriving DecidableEq, Repr

def localReopenGlobalDisconnect : DefeatSegment :=
  { localReachable := true, sourceToFinalReachable := false }

theorem localDefeatReachabilityDoesNotEntailGlobalDefeatReachability :
    localReopenGlobalDisconnect.localReachable = true ∧
      localReopenGlobalDisconnect.sourceToFinalReachable = false := by
  decide

structure ScopeComposition where
  firstLocalAdmissible : Bool
  secondLocalAdmissible : Bool
  finalInsidePulledBackScope : Bool
  deriving DecidableEq, Repr

def localScopePassGlobalInflation : ScopeComposition :=
  { firstLocalAdmissible := true
    secondLocalAdmissible := true
    finalInsidePulledBackScope := false }

theorem localScopePassDoesNotEntailCompositeScopeAdmissibility :
    localScopePassGlobalInflation.firstLocalAdmissible = true ∧
      localScopePassGlobalInflation.secondLocalAdmissible = true ∧
      localScopePassGlobalInflation.finalInsidePulledBackScope = false := by
  decide

#print axioms MQR.authorityMeetAssociative
#print axioms MQR.authorityMeetPassIdentity
#print axioms MQR.noLaunderTransitive
#print axioms MQR.adjacentPassDoesNotEntailDirectPass
#print axioms MQR.authorityBaselineResetCanHideInflation
#print axioms MQR.localAssumptionsCanBeSeparatelySatisfiableButJointlyInconsistent
#print axioms MQR.localDefeatReachabilityDoesNotEntailGlobalDefeatReachability
#print axioms MQR.localScopePassDoesNotEntailCompositeScopeAdmissibility

end MQR
