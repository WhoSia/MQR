import Std
import MQR.Residue

namespace MQR

def worldPredA (w : Bool) : Bool := w
def worldPredB (w : Bool) : Bool := !w
def sharedFormalStatement : Bool := true

theorem sameFormalStatementCanAliasDifferentWorldPredicates :
    sharedFormalStatement = true ∧
      worldPredA true = true ∧
      worldPredB true = false := by
  decide

def worldSupported : Bool → Bool
  | false => true
  | true => false

def formalStatementCovers (_ : Bool) : Bool := true

theorem formalScopeCanStrictlyExceedWorldSupport :
    formalStatementCovers true = true ∧
      worldSupported true = false := by
  decide

structure FineAncestry where
  surfacePass : Bool
  measurementPass : Bool
  calibrationPass : Bool
  deriving DecidableEq, Repr

def ancestryGood : FineAncestry :=
  { surfacePass := true, measurementPass := true, calibrationPass := true }

def ancestryHiddenHold : FineAncestry :=
  { surfacePass := true, measurementPass := true, calibrationPass := false }

def coarseCompile (a : FineAncestry) : Bool := a.surfacePass

def fineWorldPass (a : FineAncestry) : Bool :=
  a.surfacePass && a.measurementPass && a.calibrationPass

theorem coarseCompilationCanEraseAuthorityChangingAncestor :
    coarseCompile ancestryGood = coarseCompile ancestryHiddenHold ∧
      fineWorldPass ancestryGood = true ∧
      fineWorldPass ancestryHiddenHold = false := by
  decide

structure DefeatMetadata where
  reopenableLabel : Bool
  successorReachable : Bool
  deriving DecidableEq, Repr

def defeatMirage : DefeatMetadata :=
  { reopenableLabel := true, successorReachable := false }

theorem nominalReopenabilityDoesNotEntailDefeatReachability :
    defeatMirage.reopenableLabel = true ∧
      defeatMirage.successorReachable = false := by
  decide

def selfCertifiedBridge (bridgeAdequate : Bool) : Bool := bridgeAdequate

theorem bridgeSelfCertificationAddsNoIndependentConstraint :
    selfCertifiedBridge true = true ∧
      selfCertifiedBridge false = false := by
  decide

inductive FormalCustody where
  | notApplicable
  | pass
  deriving DecidableEq, Repr

structure ScientificClaim where
  worldAuthority : Bool
  formalCustody : FormalCustody
  deriving DecidableEq, Repr

def directMeasurementClaim : ScientificClaim :=
  { worldAuthority := true, formalCustody := .notApplicable }

theorem scientificAuthorityNeedNotRequireFormalCustody :
    directMeasurementClaim.worldAuthority = true ∧
      directMeasurementClaim.formalCustody = .notApplicable := by
  decide

def AuthorityStatus.meet : AuthorityStatus → AuthorityStatus → AuthorityStatus
  | .fail, _ => .fail
  | .hold, .fail => .fail
  | .hold, .hold => .hold
  | .hold, .pass => .hold
  | .pass, x => x

theorem transferMeetCannotRaiseWorldAuthority
    (world bridge : AuthorityStatus) :
    NoLaunder world (AuthorityStatus.meet world bridge) := by
  cases world <;> cases bridge <;> trivial

#print axioms MQR.transferMeetCannotRaiseWorldAuthority
#print axioms MQR.sameFormalStatementCanAliasDifferentWorldPredicates
#print axioms MQR.formalScopeCanStrictlyExceedWorldSupport
#print axioms MQR.coarseCompilationCanEraseAuthorityChangingAncestor
#print axioms MQR.nominalReopenabilityDoesNotEntailDefeatReachability
#print axioms MQR.bridgeSelfCertificationAddsNoIndependentConstraint
#print axioms MQR.scientificAuthorityNeedNotRequireFormalCustody

end MQR
