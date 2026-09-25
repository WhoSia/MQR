import Std
import MQR.Composition
namespace MQR
def definitionalEndpoint (x : Bool) : Bool := !x
theorem definitionalEndpointCarriesNoIndependentBooleanDegree (x y : Bool) (h : x = y) : definitionalEndpoint x = definitionalEndpoint y := by cases h; rfl
structure InternalCoherenceOnly where pathOne : Bool; pathTwo : Bool; commute : Bool; externalRoot : Bool deriving DecidableEq, Repr
def closedCoherenceLoop : InternalCoherenceOnly := {pathOne:=true,pathTwo:=true,commute:=true,externalRoot:=false}
theorem internalCoherenceDoesNotCreateExternalWorldAnchor : closedCoherenceLoop.pathOne=true ∧ closedCoherenceLoop.pathTwo=true ∧ closedCoherenceLoop.commute=true ∧ closedCoherenceLoop.externalRoot=false := by decide
def basisPathA (q : Bool) : Bool := q
def basisPathB (_ : Bool) : Bool := false
theorem agreementOnCheckedBasisDoesNotEntailGlobalAgreement : basisPathA false = basisPathB false ∧ basisPathA true ≠ basisPathB true := by decide
structure CommonModePaths where pathAgreement : Bool; sharedRootAdequate : Bool deriving DecidableEq, Repr
def commonModeAgreement : CommonModePaths := {pathAgreement:=true,sharedRootAdequate:=false}
theorem pathAgreementDoesNotEntailIndependentWorldContact : commonModeAgreement.pathAgreement=true ∧ commonModeAgreement.sharedRootAdequate=false := by decide
def observedEq (f g : Bool → Bool) : Prop := f false = g false
def preNot (f : Bool → Bool) : Bool → Bool := fun x => f (!x)
theorem endpointAgreementNeedNotBeCongruentUnderExtension : observedEq basisPathA basisPathB ∧ ¬ observedEq (preNot basisPathA) (preNot basisPathB) := by constructor <;> decide
structure FaceCertificate where checkedFace : Bool; untestedFace : Bool deriving DecidableEq, Repr
def finiteFaceOnly : FaceCertificate := {checkedFace:=true,untestedFace:=false}
theorem checkedFaceDoesNotEntailHigherCoherence : finiteFaceOnly.checkedFace=true ∧ finiteFaceOnly.untestedFace=false := by decide
inductive Freshness where | expired | stale | live deriving DecidableEq, Repr
def Freshness.rank : Freshness → Nat | .expired=>0 | .stale=>1 | .live=>2
def Freshness.meet : Freshness → Freshness → Freshness | .expired,_=>.expired | .stale,.expired=>.expired | .stale,.stale=>.stale | .stale,.live=>.stale | .live,x=>x
theorem compositionCannotRefreshRootFreshness (root bridge : Freshness) : (Freshness.meet root bridge).rank ≤ root.rank := by cases root <;> cases bridge <;> decide
structure TwoNodeCycle where zeroToOne : Bool; oneToZero : Bool; zeroExternal : Bool; oneExternal : Bool deriving DecidableEq, Repr
def unanchoredCycle : TwoNodeCycle := {zeroToOne:=true,oneToZero:=true,zeroExternal:=false,oneExternal:=false}
theorem cyclicJustificationDoesNotEntailExteriority : unanchoredCycle.zeroToOne=true ∧ unanchoredCycle.oneToZero=true ∧ unanchoredCycle.zeroExternal=false ∧ unanchoredCycle.oneExternal=false := by decide
structure DirectComposedConflict where composedPass : Bool; directPass : Bool deriving DecidableEq, Repr
def directComposedConflict : DirectComposedConflict := {composedPass:=true,directPass:=false}
theorem directConflictEstablishesDisagreementNotDirectInfallibility : directComposedConflict.composedPass=true ∧ directComposedConflict.directPass=false := by decide
theorem exactInternalDeterminacyStillRequiresAnExternalPremise (worldPremise : Bool) : worldPremise=true → definitionalEndpoint worldPremise=false := by intro h; cases h; decide
#print axioms MQR.definitionalEndpointCarriesNoIndependentBooleanDegree
#print axioms MQR.internalCoherenceDoesNotCreateExternalWorldAnchor
#print axioms MQR.agreementOnCheckedBasisDoesNotEntailGlobalAgreement
#print axioms MQR.pathAgreementDoesNotEntailIndependentWorldContact
#print axioms MQR.endpointAgreementNeedNotBeCongruentUnderExtension
#print axioms MQR.checkedFaceDoesNotEntailHigherCoherence
#print axioms MQR.compositionCannotRefreshRootFreshness
#print axioms MQR.cyclicJustificationDoesNotEntailExteriority
#print axioms MQR.directConflictEstablishesDisagreementNotDirectInfallibility
#print axioms MQR.exactInternalDeterminacyStillRequiresAnExternalPremise
end MQR
