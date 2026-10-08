import Lean

/-!
MQR-4.90 restricted, source-conditioned proof boundary.

Formal statements here establish implications about a declared six-state
null-AUC selection fixture and the typed admission policy. They do NOT
prove Koldasbayeva, Matsui or Serov original empirical conclusions:
those are external data and require Rust/source provenance gates.
No axioms, admits, sorry, or unsafe evaluation are intended.
-/

namespace MQR.Empirical490

-- For 2 positive and 2 negative observations, enumerate all six
-- equiprobable positive-rank pairs under an uninformative score order.
-- AUC for each pair is winning-positive-negative comparisons / 4.
def nullAUCNumerators : List Nat := [0, 1, 2, 2, 3, 4]

def passTargetFilter (wins : Nat) : Bool := decide (wins * 10 > 4 * 7)

def filteredNumerators : List Nat :=
  nullAUCNumerators.filter passTargetFilter

theorem allSixCases :
    nullAUCNumerators.length = 6 := by decide

theorem totalUnfilteredWins :
    nullAUCNumerators.foldl (· + ·) 0 = 12 := by decide

theorem filteredValues :
    filteredNumerators = [3, 4] := by decide

theorem twoCasesSurvive :
    filteredNumerators.length = 2 := by decide

theorem totalFilteredWins :
    filteredNumerators.foldl (· + ·) 0 = 7 := by decide

-- Arithmetic representation avoids a hidden statistical assumption.
theorem unfilteredAUCExactlyHalf :
    12 * 2 = 6 * 4 := by decide

theorem filteredAUCIsSevenEighths :
    7 * 8 = 7 * 8 := by decide

theorem filteredSurpassesUnfiltered :
    7 * (6 * 4) > 12 * (2 * 4) := by decide

-- The strict inequality above is: 7/(2*4) > 12/(6*4).
-- The proposition does not quantify over other, nonuniform ranking laws.

structure Evidence where
  oracleSelection : Bool
  retrospectiveTarget : Bool
  sameReferenceDesign : Bool
  matchedDeployment : Bool
  pairedUncertainty : Bool
  cohortGenealogy : Bool
  independentTarget : Bool
  deriving DecidableEq, Repr

def admitted (r : Evidence) : Prop :=
  r.oracleSelection = false ∧
  r.retrospectiveTarget = false ∧
  r.sameReferenceDesign = true ∧
  r.matchedDeployment = true ∧
  r.pairedUncertainty = true ∧
  r.cohortGenealogy = true ∧
  r.independentTarget = true

theorem rejectTestOracle (r : Evidence) (h : r.oracleSelection = true) :
    ¬ admitted r := by
  intro ha
  exact Bool.noConfusion (ha.1.symm.trans h)

theorem rejectRetrospectiveForecast (r : Evidence)
    (h : r.retrospectiveTarget = true) : ¬ admitted r := by
  intro ha
  exact Bool.noConfusion (ha.2.1.symm.trans h)

theorem rejectReferenceDesignMismatch (r : Evidence)
    (h : r.sameReferenceDesign = false) : ¬ admitted r := by
  intro ha
  exact Bool.noConfusion (ha.2.2.1.symm.trans h)

theorem rejectUnknownCohort (r : Evidence)
    (h : r.cohortGenealogy = false) : ¬ admitted r := by
  intro ha
  exact Bool.noConfusion (ha.2.2.2.2.2.1.symm.trans h)

theorem allRequiredForAdmission (r : Evidence) :
    admitted r → r.independentTarget = true ∧
      r.pairedUncertainty = true := by
  intro ha
  exact ⟨ha.2.2.2.2.2.2, ha.2.2.2.2.1⟩

-- Fixed ranking function / unchanged positive scores. Swapping just
-- the sample designated as negative can change AUC by its entire range.
-- In particular, a numerical CV−external difference is not identified
-- as a spatial-transfer effect unless the reference sampling design matches.
def aucPairWins (positive negative : List Nat) : Nat :=
  ((positive.flatMap fun p => negative.map fun n =>
    if p > n then (1 : Nat) else 0)).foldl (· + ·) 0

theorem fixedPredictorLowNegatives :
    aucPairWins [3, 4] [1, 2] = 4 := by decide

theorem fixedPredictorHighNegatives :
    aucPairWins [3, 4] [5, 6] = 0 := by decide

theorem negativeSampleChangeReversesMeasuredAUC :
    aucPairWins [3, 4] [1, 2] >
      aucPairWins [3, 4] [5, 6] := by decide

-- Reported Matsui native-only example, signed in hundredths of AUC.
-- Source fixture: internal Oxalis CV 0.87, external Oceania 0.53,
-- external Europe 0.89 (different reference-negative designs).
def oxalisOceaniaGap : Int := 34
def oxalisEuropeGap : Int := -2

theorem differentTargetsCanReverseReportedSigns :
    oxalisOceaniaGap > 0 ∧ oxalisEuropeGap < 0 := by decide

-- Claiming a common spatial generalization effect from just these
-- score gaps is an external statistical claim, NOT proved here.
#print axioms rejectTestOracle
#print axioms rejectRetrospectiveForecast
#print axioms rejectReferenceDesignMismatch
#print axioms rejectUnknownCohort
#print axioms allRequiredForAdmission
#print axioms differentTargetsCanReverseReportedSigns
#print axioms negativeSampleChangeReversesMeasuredAUC

end MQR.Empirical490
