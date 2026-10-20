import Lean

/-!
MQR-4.122 P6 exact finite-support quadrature witness, NOT the continuous
uniform-ball model and NOT an actual BEST detector.

Two equally weighted source atoms at s=-1 and s=+1; three equal-capacity
detector cells at x=2,3,4 (arbitrary distance units). Their inverse-square
weights are (5/9,5/32,17/225) after averaging over the two source atoms.
For k=pi/2, sin²(k*|x-s|)=1 on odd distances and 0 on even distances.
The suppressed weights are therefore (5/9,0,17/225), evaluated exactly.
The theorem concerns this finite quadrature; it does NOT formalize an
analytic sine identity, continuous 3D integration or actual gallium masks.
-/

namespace MQR4122P6

structure Occupancy where
  near : Rat
  middle : Rat
  far : Rat
  deriving Repr, DecidableEq

def volume (q : Occupancy) : Rat := q.near + q.middle + q.far

def baseline (q : Occupancy) : Rat :=
  (5 / 9 : Rat) * q.near +
  (5 / 32 : Rat) * q.middle +
  (17 / 225 : Rat) * q.far

def oscillation (q : Occupancy) : Rat :=
  baseline q - (1 / 2 : Rat) *
  ((5 / 9 : Rat) * q.near + (17 / 225 : Rat) * q.far)

def hNear : Rat := (5 / 32 : Rat) - (17 / 225 : Rat)
def hMiddle : Rat := (17 / 225 : Rat) - (5 / 9 : Rat)
def hFar : Rat := (5 / 9 : Rat) - (5 / 32 : Rat)

def plus : Occupancy :=
  ⟨(1 / 2 : Rat) + hNear / 4,
   (1 / 2 : Rat) + hMiddle / 4,
   (1 / 2 : Rat) + hFar / 4⟩

def minus : Occupancy :=
  ⟨(1 / 2 : Rat) - hNear / 4,
   (1 / 2 : Rat) - hMiddle / 4,
   (1 / 2 : Rat) - hFar / 4⟩

theorem distinct_geometries : plus ≠ minus := by decide
theorem same_volume : volume plus = volume minus := by decide
theorem same_no_oscillation_response :
    baseline plus = baseline minus := by decide
theorem oscillation_difference_exact :
    oscillation plus - oscillation minus = (-3 / 160 : Rat) := by decide
theorem oscillation_distinguishes :
    oscillation plus ≠ oscillation minus := by decide

theorem valid_occupancies :
    (0 : Rat) ≤ plus.near ∧ plus.near ≤ 1 ∧
    (0 : Rat) ≤ plus.middle ∧ plus.middle ≤ 1 ∧
    (0 : Rat) ≤ plus.far ∧ plus.far ≤ 1 ∧
    (0 : Rat) ≤ minus.near ∧ minus.near ≤ 1 ∧
    (0 : Rat) ≤ minus.middle ∧ minus.middle ≤ 1 ∧
    (0 : Rat) ≤ minus.far ∧ minus.far ≤ 1 := by decide

theorem extra_independent_channel_separates
    {W Obs Extra : Type} (observe : W → Obs) (extra : W → Extra)
    (a b : W) (different : extra a ≠ extra b) :
    (observe a, extra a) ≠ (observe b, extra b) := by
  intro h
  exact different (congrArg Prod.snd h)

theorem witness_cannot_be_erased_by_same_baseline :
    (volume plus, baseline plus, oscillation plus) ≠
    (volume minus, baseline minus, oscillation minus) := by
  intro h
  exact oscillation_distinguishes (congrArg (fun p => p.2.2) h)

end MQR4122P6
