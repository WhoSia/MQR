import Std

namespace MQR

variable {H T O : Type}

def EqUnder (resp : H → T → O) (family : T → Prop) (x y : H) : Prop :=
  ∀ t, family t → resp x t = resp y t

def FamilySubset (u v : T → Prop) : Prop :=
  ∀ t, u t → v t

theorem larger_family_equivalence_implies_smaller
    (resp : H → T → O)
    (u v : T → Prop)
    (hsub : FamilySubset u v)
    (x y : H)
    (hv : EqUnder resp v x y) :
    EqUnder resp u x y := by
  intro t hut
  exact hv t (hsub t hut)

theorem eqUnder_refl
    (resp : H → T → O) (u : T → Prop) (x : H) :
    EqUnder resp u x x := by
  intro t ht
  rfl

theorem eqUnder_symm
    (resp : H → T → O) (u : T → Prop) (x y : H)
    (hxy : EqUnder resp u x y) :
    EqUnder resp u y x := by
  intro t ht
  exact (hxy t ht).symm

theorem eqUnder_trans
    (resp : H → T → O) (u : T → Prop) (x y z : H)
    (hxy : EqUnder resp u x y)
    (hyz : EqUnder resp u y z) :
    EqUnder resp u x z := by
  intro t ht
  exact (hxy t ht).trans (hyz t ht)

theorem added_distinguishing_test_refines
    (resp : H → T → O)
    (u : T → Prop)
    (v : T)
    (x y : H)
    (hdiff : resp x v ≠ resp y v) :
    ¬ EqUnder resp (fun t => u t ∨ t = v) x y := by
  intro h
  exact hdiff (h v (Or.inr rfl))

theorem added_equal_test_preserves_equivalence
    (resp : H → T → O)
    (u : T → Prop)
    (v : T)
    (x y : H)
    (hu : EqUnder resp u x y)
    (hv : resp x v = resp y v) :
    EqUnder resp (fun t => u t ∨ t = v) x y := by
  intro t ht
  rcases ht with hut | rfl
  · exact hu t hut
  · exact hv

#print axioms MQR.larger_family_equivalence_implies_smaller
#print axioms MQR.eqUnder_refl
#print axioms MQR.eqUnder_symm
#print axioms MQR.eqUnder_trans
#print axioms MQR.added_distinguishing_test_refines
#print axioms MQR.added_equal_test_preserves_equivalence

end MQR
