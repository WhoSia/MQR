:- use_module(library(readutil)).

severity('NONE',0).
severity('BOUNDED',1).
severity('MATERIAL',2).
severity('FATAL',3).

field(Lines,K,V) :-
    member(Line,Lines),
    split_string(Line," "," ",[K0,V0]),
    K0 = K, !,
    atom_string(V,V0).

need(Lines,K,V) :-
    ( field(Lines,K,V) -> true
    ; format(user_error,"missing required field: ~w~n",[K]), halt(2) ).

need_pass(Lines,K) :-
    need(Lines,K,V),
    ( V='PASS' -> true
    ; format(user_error,"governance gate failed: ~w~n",[K]), halt(2) ).

need_sev(Lines,K,A,N) :-
    need(Lines,K,A),
    ( severity(A,N) -> true
    ; format(user_error,"invalid severity: ~w~n",[K]), halt(2) ).

need_nat(Lines,K,N) :-
    need(Lines,K,A),
    atom_number(A,N),
    N >= 0, !.
need_nat(_,K,_) :-
    format(user_error,"invalid nonnegative integer: ~w~n",[K]), halt(2).

yn(true,'YES').
yn(false,'NO').

run(File) :-
    read_file_to_string(File,S,[]),
    split_string(S,"
","",Lines),
    ( member("REALAPPROX 0.30-CANDIDATE",Lines) -> true
    ; writeln(user_error,'expected REALAPPROX 0.30-CANDIDATE'), halt(2) ),

    need_pass(Lines,"sealed"),
    need_pass(Lines,"lineage"),
    need_pass(Lines,"audit"),
    need(Lines,"scalar_mode",Scalar),
    ( Scalar='OFF' -> true ; writeln(user_error,'scalar_mode must be OFF'), halt(2) ),

    need(Lines,"evidence_kind",Evidence),
    ( memberchk(Evidence,['OBSERVED','PROVED','ENUMERATED','SIMULATED','INFERRED','OPEN']) -> true
    ; writeln(user_error,'invalid evidence_kind'), halt(2) ),

    need_sev(Lines,"loss_sep",LSA,LS),
    need_sev(Lines,"loss_reopen",LRA,LR),
    need_sev(Lines,"loss_prov",LPA,LP),
    need_sev(Lines,"loss_ext",LEA,LE),
    need_sev(Lines,"loss_release",LXA,LX),

    need_sev(Lines,"budget_sep",BSA,BS),
    need_sev(Lines,"budget_reopen",BRA,BR),
    need_sev(Lines,"budget_prov",BPA,BP),
    need_sev(Lines,"budget_ext",BEA,BE),
    need_sev(Lines,"budget_release",BXA,BX),

    need_nat(Lines,"debt_sep",DS),
    need_nat(Lines,"debt_reopen",DR),
    need_nat(Lines,"debt_prov",DP),
    need_nat(Lines,"debt_ext",DE),
    need_nat(Lines,"debt_release",DX),

    need(Lines,"merge_ancestry",Ancestry),

    ( DS>=4 ; DR>=3 ; DP>=2 ; DE>=3 ; DX>=2 -> DebtReexpand=true ; DebtReexpand=false ),
    ( LX=:=3 -> HardForbid=true ; HardForbid=false ),
    ( LR=:=3 ; DebtReexpand=true -> HardReexpand=true ; HardReexpand=false ),
    ( LP=:=3 ; LE=:=3 -> HardReopen=true ; HardReopen=false ),
    ( LS>BS ; LR>BR ; LP>BP ; LE>BE ; LX>BX -> BudgetExceeded=true ; BudgetExceeded=false ),
    ( LS>0 ; LR>0 ; LP>0 ; LE>0 ; LX>0 -> AnyLoss=true ; AnyLoss=false ),

    choose(HardForbid,HardReexpand,HardReopen,BudgetExceeded,AnyLoss,Decision),

    format("approximation.decision=~w~n",[Decision]),
    emit_coord(sep,LSA,BSA,LS,BS),
    emit_coord(reopen,LRA,BRA,LR,BR),
    emit_coord(prov,LPA,BPA,LP,BP),
    emit_coord(ext,LEA,BEA,LE,BE),
    emit_coord(release,LXA,BXA,LX,BX),
    yn(HardForbid,YF), format("approximation.hard_forbid=~w~n",[YF]),
    yn(HardReopen,YR), format("approximation.reopen_required=~w~n",[YR]),
    yn(HardReexpand,YX), format("approximation.reexpand_required=~w~n",[YX]),
    yn(DebtReexpand,YD), format("approximation.debt_reexpand=~w~n",[YD]),
    format("approximation.merge_ancestry=~w~n",[Ancestry]),
    writeln("approximation.scalar_authority=OFF"),
    writeln("approximation.global_loss_score=FORBIDDEN"),
    format("approximation.evidence_kind=~w~n",[Evidence]),
    world_validity(Evidence,W), format("approximation.world_validity=~w~n",[W]),
    writeln("approximation.universal_epistemic_utility=NOT_EARNED"),
    writeln("approximation.realapprox_status=CANDIDATE_UNPROMOTED").

choose(true,_,_,_,_,'FORBID_MERGE') :- !.
choose(_,true,_,_,_,'REEXPAND_REQUIRED') :- !.
choose(_,_,true,_,_,'REOPEN_REQUIRED') :- !.
choose(_,_,_,true,_,'HOLD_INCOMPARABLE') :- !.
choose(_,_,_,_,true,'ACCEPT_WITH_AUDIT') :- !.
choose(_,_,_,_,_,'ACCEPT_LOCAL').

emit_coord(Name,LossA,BudgetA,Loss,Budget) :-
    format("approximation.loss.~w=~w~n",[Name,LossA]),
    format("approximation.budget.~w=~w~n",[Name,BudgetA]),
    ( Loss>Budget -> X=true ; X=false ),
    yn(X,Y),
    format("approximation.budget_exceeded.~w=~w~n",[Name,Y]).

world_validity('SIMULATED','NOT_ESTABLISHED') :- !.
world_validity('OPEN','OPEN') :- !.
world_validity(_,'LIMITED_BY_EVIDENCE_KIND').

:- initialization(main, main).
main(Argv) :-
    ( Argv=[File|_] -> run(File)
    ; writeln(user_error,'usage: swipl -q -f approx_v30.pl -- <packet>'), halt(2) ).
