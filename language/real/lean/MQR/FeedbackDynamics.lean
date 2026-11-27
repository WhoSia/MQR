import MQR.ScientificStateQuotient

namespace MQR.FeedbackDynamics

/-- Boolean state, Boolean intervention, identity observation, known reset false. -/
structure World where
  off0 : Bool
  on0 : Bool
  off1 : Bool
  on1 : Bool
  deriving DecidableEq, Repr

def step (w : World) (state policy : Bool) : Bool :=
  if state then (if policy then w.on1 else w.off1)
  else (if policy then w.on0 else w.off0)

def asSystem (w : World) : MQR.AuthoritySystem Bool Bool Bool :=
  { label := id, step := step w }

def endpoint (w : World) (state : Bool) (word : List Bool) : Bool :=
  MQR.run (asSystem w) state word

theorem endpoint_congr (w v : World)
    (h : ∀ s p, step w s p = step v s p)
    (s : Bool) (word : List Bool) :
    endpoint w s word = endpoint v s word := by
  induction word generalizing s with
  | nil => rfl
  | cons p ps ih =>
      change endpoint w (step w s p) ps = endpoint v (step v s p) ps
      rw [h s p]
      exact ih _

theorem endpoint_dead (w : World) (h : ∀ p, step w false p = false)
    (word : List Bool) : endpoint w false word = false := by
  induction word with
  | nil => rfl
  | cons p ps ih =>
      change endpoint w (step w false p) ps = false
      rw [h p]
      exact ih

/-- For this fully observed two-state family, words of length at most two
    suffice to establish equality of all finite reset experiments. -/
theorem two_steps_complete (w v : World)
    (h0 : ∀ p, step w false p = step v false p)
    (h2 : ∀ p q, step w (step w false p) q = step v (step v false p) q)
    (word : List Bool) :
    endpoint w false word = endpoint v false word := by
  by_cases reach : ∃ p : Bool, step w false p = true
  · obtain ⟨p, hp⟩ := reach
    have hpv : step v false p = true := (h0 p).symm.trans hp
    have h1 : ∀ q, step w true q = step v true q := by
      intro q
      simpa only [hp, hpv] using h2 p q
    apply endpoint_congr w v
    intro s q
    cases s with
    | false => exact h0 q
    | true => exact h1 q
  · have hw : ∀ p, step w false p = false := by
      intro p
      cases hp : step w false p with
      | false => rfl
      | true => exact False.elim (reach ⟨p, hp⟩)
    have hv : ∀ p, step v false p = false := fun p => (h0 p).symm.trans (hw p)
    exact (endpoint_dead w hw word).trans (endpoint_dead v hv word).symm

def reversible : World := ⟨false, true, false, true⟩
def persistent : World := ⟨false, true, true, true⟩

theorem fixed_endpoint (w : World) (s p : Bool)
    (h : step w s p = s) (n : Nat) :
    endpoint w s (List.replicate n p) = s := by
  induction n with
  | zero => rfl
  | succ n ih =>
      simp only [List.replicate_succ]
      change endpoint w (step w s p) (List.replicate n p) = s
      rw [h]
      exact ih

theorem constant_policy_agreement (p : Bool) (n : Nat) :
    endpoint reversible false (List.replicate n p) =
      endpoint persistent false (List.replicate n p) := by
  cases p with
  | false =>
      exact (fixed_endpoint reversible false false rfl n).trans
        (fixed_endpoint persistent false false rfl n).symm
  | true =>
      cases n with
      | zero => rfl
      | succ n =>
          simp only [List.replicate_succ]
          change endpoint reversible true (List.replicate n true) =
            endpoint persistent true (List.replicate n true)
          exact (fixed_endpoint reversible true true rfl n).trans
            (fixed_endpoint persistent true true rfl n).symm

theorem withdrawal_separates :
    endpoint reversible false [true, false] ≠
      endpoint persistent false [true, false] := by decide

theorem unreachable_rows_do_not_identify (w v : World)
    (hw : ∀ p, step w false p = false)
    (hv : ∀ p, step v false p = false)
    (word : List Bool) :
    endpoint w false word = endpoint v false word :=
  (endpoint_dead w hw word).trans (endpoint_dead v hv word).symm

#print axioms two_steps_complete
#print axioms constant_policy_agreement
#print axioms withdrawal_separates
#print axioms unreachable_rows_do_not_identify

end MQR.FeedbackDynamics
