import Lean
/-!
Conditional detectability/occupancy toy courts, not model fitting or real
NAAMP/Swedish provenance verification. Numerators below share denominators:
ψ_A=1/2 p_A=1 versus ψ_B=1 p_B=1/2.
One visit positive probability numerator over 4 is 2 in both worlds;
two-visit BOTH-positive numerator over 8 is 4 vs 2. This illustrates
a sufficient distinction when closure and independent homogeneous
detection hold, not universal statistical identifiability.
-/
namespace MQR497

def oneVisitNumerator (occupancyN detectionN : Nat) : Nat :=
  occupancyN * detectionN

def bothVisitsNumerator (occupancyN detectionN : Nat) : Nat :=
  occupancyN * detectionN * detectionN

theorem two_parameter_worlds_equal_one_visit :
  oneVisitNumerator 1 2 = oneVisitNumerator 2 1 := by decide

theorem two_parameter_worlds_differ_under_two_independent_visits :
  bothVisitsNumerator 1 2 ≠ bothVisitsNumerator 2 1 := by decide

def recordedDetection (occupied detected : Bool) : Bool :=
  occupied && detected

theorem silent_visit_not_latent_absence :
  recordedDetection false true = recordedDetection true false ∧
  false ≠ true := by decide

theorem guaranteed_detection_given_occupied_under_perfect_detector :
  recordedDetection true true = true := by rfl

structure SurveySite where
  station : Nat
  geographicFootprint : Option Nat
  detector : Bool
deriving DecidableEq, Repr

def sourceStrip (r : SurveySite) : Nat × Bool :=
  (r.station, r.detector)

theorem missing_footprint_can_share_record_with_geolocated_footprint :
 sourceStrip ⟨7, none, true⟩ = sourceStrip ⟨7, some 35, true⟩ := by rfl

theorem field_station_id_does_not_identify_coordinate_footprint :
  (⟨7, none, true⟩ : SurveySite) ≠ ⟨7, some 35, true⟩ := by decide

/-- Finite lists of recorder visits cannot conjure an omitted protocol attribute. -/
theorem shared_detection_history_still_lacks_footprint :
 sourceStrip ⟨18, none, false⟩ = sourceStrip ⟨18, some 12, false⟩ := by rfl

end MQR497
