import Lean

/-!
MQR-4.95: A tiny abstract theorem court distinguishing target-matched
observations from different-frame field data. This uses NATURAL-number
uncertainty contributions, NOT a proof of arbitrary floating-point
log-loss computations or ecological transfer. No sorry, no new axiom.
-/
namespace MQR495

/-- Sum of as-yet-unobserved nonnegative uncertainty contributions. -/
def residualWidth (unknown : List Nat) : Nat := unknown.sum

structure ExternalReceipt where
  frameKey : Nat
  observedBinary : Bool
deriving Repr

/--
A receipt contracts the given target risk's admissible width only if
its frame is the target AND a matched binary observation is admitted.
Outside target-frame evidence is valid for its own study, not the
unobserved labels of this target.
-/
def auditStep (target : Nat) (width : Nat) (rest : List Nat)
    (receipt : ExternalReceipt) : List Nat :=
  if receipt.frameKey = target ∧ receipt.observedBinary = true then
    rest
  else
    width :: rest

theorem unmatched_frame_keeps_target_uncertainty
    (target width : Nat) (rest : List Nat) (r : ExternalReceipt)
    (h : r.frameKey ≠ target) :
    residualWidth (auditStep target width rest r) =
      residualWidth (width :: rest) := by
  simp [auditStep, h]

theorem missing_binary_label_keeps_target_uncertainty
    (target width : Nat) (rest : List Nat) (r : ExternalReceipt)
    (h : r.observedBinary = false) :
    residualWidth (auditStep target width rest r) =
      residualWidth (width :: rest) := by
  simp [auditStep, h]

theorem matched_observation_removes_exact_contribution
    (target width : Nat) (rest : List Nat) (r : ExternalReceipt)
    (hFrame : r.frameKey = target)
    (hBinary : r.observedBinary = true) :
    residualWidth (width :: rest) =
      width + residualWidth (auditStep target width rest r) := by
  simp [auditStep, hFrame, hBinary, residualWidth]

def worldLossLow (observed unknownLow : Nat) : Nat := observed + unknownLow
def worldLossHigh (observed unknownHigh : Nat) : Nat := observed + unknownHigh

/-- Observational equality on the audited part does not identify unseen loss. -/
theorem distinct_unknown_label_worlds_same_observed_data
    (observed unknownLow unknownHigh : Nat)
    (h : unknownLow ≠ unknownHigh) :
    worldLossLow observed unknownLow ≠
      worldLossHigh observed unknownHigh := by
  intro eq
  have same : unknownLow = unknownHigh := Nat.add_left_cancel eq
  exact h same

theorem audited_every_site_zero_residual :
    residualWidth ([] : List Nat) = 0 := by
  rfl

end MQR495
