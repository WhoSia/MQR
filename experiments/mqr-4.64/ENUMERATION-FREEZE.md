# MQR-4.64 — Finite Binding-Surface Enumeration Freeze

Status: **FROZEN BEFORE EXECUTABLE REVEAL**

## Purpose

Avoid hand-selecting a few favorable witness worlds.

The primary executable study exhaustively enumerates a small finite class of action systems and derives binding/redundancy from the action/reachability structure.

## Finite world grammar

Each world contains exactly 3 currently feasible actions `a0,a1,a2`.

Each action has:
- immediate utility `u ∈ {0,1,2}`;
- cost `c ∈ {0,1}`;
- separator-retention mask over two future separators `S={s0,s1}`: one of `00,01,10,11`;
- reopening-retention bit `r ∈ {0,1}`;
- ancestry class `g ∈ {0,1}`;
- exterior-access bit `x ∈ {0,1}`.

World-level flags:
- action effects irreversible: `irr ∈ {0,1}`;
- separator substitutability: `sub ∈ {0,1}`;
- reopening later material: `reopen_live ∈ {0,1}`;
- independent ancestry route material: `anc_live ∈ {0,1}`;
- exterior route material: `ext_live ∈ {0,1}`.

To keep enumeration finite but nontrivial, action feature tuples are drawn from a fixed catalog of 16 representative action types spanning:
- high/medium/low immediate value;
- full/partial/no separator retention;
- reopen/no-reopen;
- ancestry class 0/1;
- exterior yes/no.

Worlds enumerate unordered triples with replacement from the 16-action catalog × the 5 binary world flags.

## Baseline families

1. **MYOPIC**: maximize `u-c`, deterministic index tie-break.
2. **LOOKAHEAD**: maximize `u-c + 1.0*|effective separators| + 0.5*reopening_live*r`.
3. **CONSTRAINED**: LOOKAHEAD plus minimum one effective future separator when irreversible and any separator is preservable.
4. **DIVERSITY**: MYOPIC plus preference for ancestry/exterior diversity only when those declared world flags are live.

These are stylized baselines, not claimed exact implementations of cited algorithms.

## Typed constraints

- **OPR**: when irreversible, require at least one effective future separator if any action can preserve one.
- **ARR**: when `reopen_live=1`, require `r=1` if any such action exists.
- **EAI**: when `anc_live=1`, if prior ancestry class is 0, require class 1 when available.
- **EXTERIOR**: when `ext_live=1`, require `x=1` when available.
- **NEDL**: over a frozen two-step extension, reject first actions that leave zero effective separators for step 2 when a preserving action exists.

Substitutability rule:
when `sub=1`, separator masks `01`, `10`, and `11` all count as retaining the same effective future discriminatory capability; destroying one named separator is not option loss if the other survives.

Reversible rule:
when `irr=0`, OPR/NEDL separator-loss constraints release because the action does not remove future access.

## Derived quantities

For every world × baseline × typed constraint:
- baseline feasible set;
- constrained feasible set;
- set difference;
- chosen baseline action;
- chosen constrained action;
- effective future separator set;
- reopening bit;
- ancestry/exterior state;
- immediate utility/cost;
- action disagreement;
- reachability disagreement.

## Frozen classification implementation

- no typed activation => DIAGNOSTIC_ONLY;
- typed activation but baseline chosen action always allowed and same reachability => REDUNDANT_CONSTRAINT;
- typed changes formal feasible set, but baseline family independently chooses behaviorally equivalent action/reachability => BASELINE_ABSORBED;
- typed changes chosen action and future material reachability, non-oracular => BINDING_LOCAL;
- typed binds in both irreversible-separator and at least one structurally different live-axis family under ≥2 baseline families => BINDING_STRUCTURAL candidate;
- typed binds but reduces immediate utility by ≥1 with no future material reachability gain => OVERCONSTRAINING;
- no ORACLE_DEPENDENT case can be promoted from this finite grammar because all activation variables are explicit state; separate frozen oracle-trap witnesses test rejection.

## Minimality test

For every BINDING_LOCAL witness, remove each live world flag/constraint condition one at a time.
A witness is minimal only if at least one such removal destroys binding and no proper action-subset containing baseline+constrained choices still witnesses the same reachability loss.

## Frozen controls

Named structural controls are generated from the same grammar and checked:
- reversible release;
- substitutable-separator release;
- baseline absorption;
- slack constraint;
- overconstraint;
- oracle trap (separate explicit fixture);
- ancestry binding;
- reopening binding;
- exterior binding;
- two-step debt binding.

No post-reveal action catalog, weights, thresholds, or classification rule changes.
