import Std

namespace MQR

structure PanelWitness where
  namedAdjudicators : Nat
  ancestryClasses : Nat
  deriving DecidableEq, Repr

def commonModePanel : PanelWitness :=
  { namedAdjudicators := 3, ancestryClasses := 1 }

theorem adjudicatorCountDoesNotImplyAncestryIndependence :
    commonModePanel.namedAdjudicators = 3 ∧
    commonModePanel.ancestryClasses = 1 := by
  decide

structure SelfCertificationWitness where
  proposerAncestry : Nat
  adjudicatorAncestry : Nat
  independentWitness : Bool
  deriving DecidableEq, Repr

def selfCertificationWitness : SelfCertificationWitness :=
  { proposerAncestry := 7
    adjudicatorAncestry := 7
    independentWitness := false }

theorem selfCertificationAddsNoIndependentWitness :
    selfCertificationWitness.proposerAncestry =
      selfCertificationWitness.adjudicatorAncestry ∧
    selfCertificationWitness.independentWitness = false := by
  decide

inductive MapRelation where
  | exact
  | refine
  | merge
  | overlap
  | disjoint
  | unmapped
  deriving DecidableEq, Repr

def underdeterminedCorrespondence : List MapRelation :=
  [.refine, .overlap]

theorem sameDeclaredSurfaceCanLeaveMultipleRelationsAdmissible :
    underdeterminedCorrespondence.length = 2 ∧
    underdeterminedCorrespondence.contains .refine = true ∧
    underdeterminedCorrespondence.contains .overlap = true := by
  decide

structure ConsensusWitness where
  panelAgreement : Bool
  uniqueWorldCorrespondence : Bool
  deriving DecidableEq, Repr

def consensusWitness : ConsensusWitness :=
  { panelAgreement := true
    uniqueWorldCorrespondence := false }

theorem adjudicatorConsensusDoesNotImplyUniqueWorldCorrespondence :
    consensusWitness.panelAgreement = true ∧
    consensusWitness.uniqueWorldCorrespondence = false := by
  decide

structure StandardWitness where
  standardAgreement : Bool
  truthOracle : Bool
  deriving DecidableEq, Repr

def standardWitness : StandardWitness :=
  { standardAgreement := true
    truthOracle := false }

theorem standardAgreementDoesNotCreateTruthOracle :
    standardWitness.standardAgreement = true ∧
    standardWitness.truthOracle = false := by
  decide

structure MetaCycleWitness where
  cyclePresent : Bool
  independentRootCreated : Bool
  deriving DecidableEq, Repr

def metaCycleWitness : MetaCycleWitness :=
  { cyclePresent := true
    independentRootCreated := false }

theorem cyclicMetaSupportDoesNotCreateIndependentRoot :
    metaCycleWitness.cyclePresent = true ∧
    metaCycleWitness.independentRootCreated = false := by
  decide

structure SeparatorWitness where
  beforeCount : Nat
  afterCount : Nat
  finalCorrespondenceClosed : Bool
  deriving DecidableEq, Repr

def separatorWitness : SeparatorWitness :=
  { beforeCount := 2
    afterCount := 1
    finalCorrespondenceClosed := false }

theorem worldFacingSeparatorCanNarrowWithoutClosingCorrespondence :
    separatorWitness.afterCount < separatorWitness.beforeCount ∧
    separatorWitness.afterCount = 1 ∧
    separatorWitness.finalCorrespondenceClosed = false := by
  decide

structure MetaDebtWitness where
  finiteDependencyGraph : Bool
  unresolvedTerminal : Bool
  finalMetaOracle : Bool
  deriving DecidableEq, Repr

def metaDebtWitness : MetaDebtWitness :=
  { finiteDependencyGraph := true
    unresolvedTerminal := true
    finalMetaOracle := false }

theorem finiteMetaDebtCanRemainExplicitWithoutFinalOracle :
    metaDebtWitness.finiteDependencyGraph = true ∧
    metaDebtWitness.unresolvedTerminal = true ∧
    metaDebtWitness.finalMetaOracle = false := by
  decide

structure TranslationClosureWitness where
  currentAuthorityPass : Bool
  futureTranslationClosed : Bool
  deriving DecidableEq, Repr

def translationClosureWitness : TranslationClosureWitness :=
  { currentAuthorityPass := true
    futureTranslationClosed := false }

theorem currentMappingAuthorityDoesNotImplyFutureTranslationClosure :
    translationClosureWitness.currentAuthorityPass = true ∧
    translationClosureWitness.futureTranslationClosed = false := by
  decide

#print axioms MQR.adjudicatorCountDoesNotImplyAncestryIndependence
#print axioms MQR.selfCertificationAddsNoIndependentWitness
#print axioms MQR.sameDeclaredSurfaceCanLeaveMultipleRelationsAdmissible
#print axioms MQR.adjudicatorConsensusDoesNotImplyUniqueWorldCorrespondence
#print axioms MQR.standardAgreementDoesNotCreateTruthOracle
#print axioms MQR.cyclicMetaSupportDoesNotCreateIndependentRoot
#print axioms MQR.worldFacingSeparatorCanNarrowWithoutClosingCorrespondence
#print axioms MQR.finiteMetaDebtCanRemainExplicitWithoutFinalOracle
#print axioms MQR.currentMappingAuthorityDoesNotImplyFutureTranslationClosure

end MQR
