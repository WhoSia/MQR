import Std

namespace MQR.IrreversibleInquiry

inductive Hypothesis where
  | zero | one | two
  deriving DecidableEq, Repr

def signature (w : Hypothesis) (p : Bool) : Bool :=
  match w with
  | .zero => false
  | .one => p
  | .two => !p

def oneShotTrace (w : Hypothesis) : List Bool → List Bool
  | [] => []
  | p :: ps => signature w p :: List.replicate ps.length false

theorem pairwise_separable (w v : Hypothesis) (h : w ≠ v) :
    ∃ p : Bool, signature w p ≠ signature v p := by
  cases w <;> cases v <;>
    first | exact False.elim (h rfl)
          | exact ⟨false, by decide⟩
          | exact ⟨true, by decide⟩

theorem each_first_test_loses_a_pair (p : Bool) :
    ∃ w v : Hypothesis, w ≠ v ∧ signature w p = signature v p := by
  cases p with
  | false => exact ⟨.zero, .one, by decide, rfl⟩
  | true => exact ⟨.zero, .two, by decide, rfl⟩

theorem each_first_test_loses_a_pair_forever (p : Bool) :
    ∃ w v : Hypothesis, w ≠ v ∧
      ∀ suffix : List Bool, oneShotTrace w (p :: suffix) =
        oneShotTrace v (p :: suffix) := by
  obtain ⟨w, v, hne, heq⟩ := each_first_test_loses_a_pair p
  exact ⟨w, v, hne, fun suffix => congrArg
    (fun b => b :: List.replicate suffix.length false) heq⟩

inductive Inquiry where
  | guess (w : Hypothesis)
  | test (p : Bool) (zero one : Inquiry)

def afterSpent : Inquiry → Hypothesis
  | .guess h => h
  | .test _ z _ => afterSpent z

def diagnose (w : Hypothesis) : Inquiry → Hypothesis
  | .guess h => h
  | .test p z o => afterSpent (if signature w p then o else z)

theorem no_global_adaptive_strategy :
    ¬ ∃ t : Inquiry, ∀ w : Hypothesis, diagnose w t = w := by
  intro hex
  obtain ⟨t, h⟩ := hex
  cases t with
  | guess w =>
      cases w with
      | zero => exact (by decide : Hypothesis.zero ≠ Hypothesis.one) (h .one)
      | one => exact (by decide : Hypothesis.one ≠ Hypothesis.zero) (h .zero)
      | two => exact (by decide : Hypothesis.two ≠ Hypothesis.zero) (h .zero)
  | test p z o =>
      obtain ⟨w,v,hne,heq⟩ := each_first_test_loses_a_pair p
      have same : diagnose w (.test p z o) = diagnose v (.test p z o) := by
        simp only [diagnose, heq]
      exact hne ((h w).symm.trans (same.trans (h v)))

inductive Action where
  | split | left | right
  deriving DecidableEq, Repr

def secondRead (w : Bool × Bool) (a : Action) : Bool :=
  match a with
  | .split => false
  | .left => !w.1 && w.2
  | .right => w.1 && w.2

def fourTrace (w : Bool × Bool) : List Action → List Bool
  | [] => []
  | .split :: [] => [w.1]
  | .split :: a :: ps => w.1 :: secondRead w a :: List.replicate ps.length false
  | _ :: ps => false :: List.replicate ps.length false

def adaptiveRead (w : Bool × Bool) : Bool × Bool :=
  let g := w.1
  (g, secondRead w (if g then .right else .left))

theorem adaptive_four_identifies (w : Bool × Bool) : adaptiveRead w = w := by
  obtain ⟨g,b⟩ := w
  cases g <;> cases b <;> rfl

theorem no_fixed_word_identifies_four (word : List Action) :
    ∃ w v : Bool × Bool, w ≠ v ∧ fourTrace w word = fourTrace v word := by
  cases word with
  | nil => exact ⟨(false,false), (false,true), by decide, rfl⟩
  | cons a ps =>
      cases a with
      | left => exact ⟨(false,false), (false,true), by decide, rfl⟩
      | right => exact ⟨(false,false), (false,true), by decide, rfl⟩
      | split =>
          cases ps with
          | nil => exact ⟨(false,false), (false,true), by decide, rfl⟩
          | cons b rest =>
              cases b with
              | split => exact ⟨(false,false), (false,true), by decide, rfl⟩
              | left => exact ⟨(true,false), (true,true), by decide, rfl⟩
              | right => exact ⟨(false,false), (false,true), by decide, rfl⟩

#print axioms pairwise_separable
#print axioms each_first_test_loses_a_pair_forever
#print axioms no_global_adaptive_strategy
#print axioms adaptive_four_identifies
#print axioms no_fixed_word_identifies_four

end MQR.IrreversibleInquiry
