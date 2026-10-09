import Lean

/-!
MQR-4.96 mathematical logic court. Source erasure cannot
identify a protocol tag even if the observed site and binary
label are known. This is a conditional counterexample to
injectivity of an explicitly defined projection, **not** a
theorem of ecological causation, sampling independence,
correctness of actual GBIF statuses, or calibration transfer.
-/
namespace MQR496

structure TaggedRecord where
  source : Nat
  site : Nat
  observed : Bool
deriving DecidableEq, Repr

def dropSource (r : TaggedRecord) : Nat × Bool :=
  (r.site, r.observed)

def tag (source site : Nat) (observed : Bool) : TaggedRecord :=
  ⟨source, site, observed⟩

theorem different_sources_erase_to_same_observation
    (s t site : Nat) (v : Bool) :
    dropSource (tag s site v) = dropSource (tag t site v) := by
  rfl

theorem different_sources_are_different_records
    (s t site : Nat) (v : Bool) (h : s ≠ t) :
    tag s site v ≠ tag t site v := by
  intro eq
  apply h
  have hs := congrArg TaggedRecord.source eq
  simpa [tag] using hs

theorem dropping_source_is_not_injective :
    ¬ Function.Injective dropSource := by
  intro h
  have eq : tag 1 7 true = tag 2 7 true :=
    h (different_sources_erase_to_same_observation 1 2 7 true)
  have bad : (1 : Nat) = 2 := by
    simpa [tag] using congrArg TaggedRecord.source eq
  exact (by decide : (1 : Nat) ≠ 2) bad

/--
An observation absent from a presence-only list cannot be
conjured into a certified binary non-detection.
-/
theorem positive_only_has_no_recorded_negative
    (xs : List Bool) (allPositive : ∀ x ∈ xs, x = true) :
    false ∉ xs := by
  intro hx
  have contradiction := allPositive false hx
  cases contradiction

/--
A claimed negative record is licensed here only if the
abstract observation contract has a certified survey.
This definition does not model detection probability.
-/
def admissibleNegative (surveyed : Bool) (observed : Bool) : Bool :=
  surveyed && (!observed)

theorem no_negative_receipt_without_survey (observed : Bool) :
    admissibleNegative false observed = false := by
  cases observed <;> rfl

/-!
A *toy* latent detection model: observed detection probability is
occupancy × detection probability, with zero false positives. A single
observed probability cannot recover both components without extra data.
These two concrete interior-boundary parameters are counterexamples to
injectivity. This is standard occupancy-model algebra, not MQR novelty.
-/
def detectionObservation (occupancy detection : Rat) : Rat :=
  occupancy * detection

theorem occupancy_not_identified_from_one_detected_rate :
    (1 / 2 : Rat) ≠ 1 ∧
    detectionObservation (1 / 2) 1 =
      detectionObservation 1 (1 / 2) := by
  decide

end MQR496
