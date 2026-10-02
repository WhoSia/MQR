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

evidence_kind('OBSERVED').
evidence_kind('PROVED').
evidence_kind('ENUMERATED').
evidence_kind('SIMULATED').
evidence_kind('INFERRED').
evidence_kind('OPEN').

context('EXPLORATORY').
context('AUDIT').
context('PUBLIC_RELEASE').
context('CROSS_DOMAIN').

yn(true,'YES').
yn(false,'NO').

run(File) :-
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    ( member("REALLOSS 0.30-CANDIDATE",Lines) -> true
    ; writeln(user_error,'expected REALLOSS 0.30-CANDIDATE'), halt(2) ),

    need_pass(Lines,"sealed"),
    need_pass(Lines,"lineage"),
    need_pass(Lines,"audit"),
    need(Lines,"scalar_mode",Scalar),
    ( Scalar='OFF' -> true ; writeln(user_error,'scalar_mode must be OFF'), halt(2) ),

    need(Lines,"evidence_kind",Evidence),
    need(Lines,"warrant_kind",WKind),
    ( evidence_kind(Evidence), evidence_kind(WKind) -> true
    ; writeln(user_error,'invalid evidence kind'), halt(2) ),

    need(Lines,"context",Context),
    ( context(Context) -> true ; writeln(user_error,'invalid context'), halt(2) ),

    need_sev(Lines,"loss_sep",LSA,LS),
    need_sev(Lines,"loss_reopen",LRA,LR),
    need_sev(Lines,"loss_prov",LPA,LP),
    need_sev(Lines,"loss_ext",LEA,LE),
    need_sev(Lines,"loss_release",LXA,LX),
    need_sev(Lines,"ceiling_sep",BSA,BS),
    need_sev(Lines,"ceiling_reopen",BRA,BR),
    need_sev(Lines,"ceiling_prov",BPA,BP),
    need_sev(Lines,"ceiling_ext",BEA,BE),
    need_sev(Lines,"ceiling_release",BXA,BX),

    need(Lines,"warrant_source",WSource),
    need(Lines,"warrant_defeaters",WDef),
    need(Lines,"horizon",Horizon),
    need(Lines,"expiry",Expiry),
    ( WKind \= 'OPEN', WSource \= 'OPEN', WDef \= 'OPEN', Horizon \= 'OPEN', Expiry \= 'OPEN'
      -> WComplete=true ; WComplete=false ),

    need(Lines,"transport_valid",Transport),
    ( Transport='PASS' -> TransportValid=true ; TransportValid=false ),
    need(Lines,"reopening_trigger",RT0),
    ( RT0='YES' -> Reopening=true ; Reopening=false ),
    need(Lines,"revision_requested",RR0),
    ( RR0='YES' -> RevReq=true ; RevReq=false ),
    need(Lines,"revision_authorized",RA0),
    ( RA0='YES' -> RevAuth=true ; RevAuth=false ),
    need(Lines,"revision_trigger",RevTrigger),
    ( RevReq=true, RevAuth=true,
      \+ memberchk(RevTrigger,['OBSERVED_SCOPE_CHANGE','OBSERVED_REOPENING_EVENT','PREDECLARED_EXPIRY'])
      -> writeln(user_error,'revision authorization lacks admitted trigger'), halt(2)
      ; true ),

    need(Lines,"merge_ancestry",Ancestry),
    ( LS>BS ; LR>BR ; LP>BP ; LE>BE ; LX>BX -> BudgetExceeded=true ; BudgetExceeded=false ),
    ( LS>0 ; LR>0 ; LP>0 ; LE>0 ; LX>0 -> AnyLoss=true ; AnyLoss=false ),

    choose(WComplete,Context,TransportValid,RevReq,RevAuth,LX,Reopening,LR,LP,LE,BudgetExceeded,AnyLoss,Decision),

    format("loss_contract.decision=~w~n",[Decision]),
    format("loss_contract.context=~w~n",[Context]),
    format("loss_contract.horizon=~w~n",[Horizon]),
    format("loss_contract.warrant.kind=~w~n",[WKind]),
    format("loss_contract.warrant.source=~w~n",[WSource]),
    format("loss_contract.warrant.defeaters=~w~n",[WDef]),
    yn(WComplete,YWC), format("loss_contract.warrant.complete=~w~n",[YWC]),
    emit_coord(sep,LSA,BSA,LS,BS),
    emit_coord(reopen,LRA,BRA,LR,BR),
    emit_coord(prov,LPA,BPA,LP,BP),
    emit_coord(ext,LEA,BEA,LE,BE),
    emit_coord(release,LXA,BXA,LX,BX),
    yn(Reopening,YR), format("loss_contract.reopening_trigger=~w~n",[YR]),
    yn(TransportValid,YT), format("loss_contract.transport_valid=~w~n",[YT]),
    yn(RevReq,YQ), format("loss_contract.revision_requested=~w~n",[YQ]),
    yn(RevAuth,YA), format("loss_contract.revision_authorized=~w~n",[YA]),
    format("loss_contract.revision_trigger=~w~n",[RevTrigger]),
    format("loss_contract.expiry=~w~n",[Expiry]),
    format("loss_contract.merge_ancestry=~w~n",[Ancestry]),
    writeln("loss_contract.scalar_authority=OFF"),
    writeln("loss_contract.global_loss_score=FORBIDDEN"),
    writeln("loss_contract.cross_domain_severity_equality=NOT_ASSUMED"),
    format("loss_contract.evidence_kind=~w~n",[Evidence]),
    world_validity(Evidence,W), format("loss_contract.world_validity=~w~n",[W]),
    writeln("loss_contract.authority_reducibility=NOT_ESTABLISHED_BY_REPRESENTATION"),
    writeln("loss_contract.status=CANDIDATE_UNPROMOTED").

choose(false,_,_,_,_,_,_,_,_,_,_,_,'HOLD_WARRANT_OPEN') :- !.
choose(true,'CROSS_DOMAIN',false,_,_,_,_,_,_,_,_,_,'HOLD_TRANSPORT') :- !.
choose(true,_,_,true,true,_,_,_,_,_,_,_,'REVISION_AUTHORIZED') :- !.
choose(true,_,_,true,false,_,_,_,_,_,_,_,'REVISION_FORBIDDEN') :- !.
choose(true,_,_,false,_,3,_,_,_,_,_,_,'FORBID_MERGE') :- !.
choose(true,_,_,false,_,_,true,_,_,_,_,_,'REEXPAND_REQUIRED') :- !.
choose(true,_,_,false,_,_,false,3,_,_,_,_,'REEXPAND_REQUIRED') :- !.
choose(true,_,_,false,_,_,false,_,3,_,_,_,'REOPEN_REQUIRED') :- !.
choose(true,_,_,false,_,_,false,_,_,3,_,_,'REOPEN_REQUIRED') :- !.
choose(true,_,_,false,_,_,false,_,_,_,true,_,'HOLD_CONTEXT_CEILING') :- !.
choose(true,_,_,false,_,_,false,_,_,_,false,true,'ACCEPT_WITH_AUDIT') :- !.
choose(_,_,_,_,_,_,_,_,_,_,_,_,'ACCEPT_LOCAL').

emit_coord(Name,LossA,BudgetA,Loss,Budget) :-
    format("loss_contract.loss.~w=~w~n",[Name,LossA]),
    format("loss_contract.ceiling.~w=~w~n",[Name,BudgetA]),
    ( Loss>Budget -> X=true ; X=false ),
    yn(X,Y),
    format("loss_contract.ceiling_exceeded.~w=~w~n",[Name,Y]).

world_validity('SIMULATED','NOT_ESTABLISHED') :- !.
world_validity('OPEN','OPEN') :- !.
world_validity(_,'LIMITED_BY_EVIDENCE_KIND').

:- initialization(main, main).
main(Argv) :-
    ( Argv=[File|_] -> run(File)
    ; writeln(user_error,'usage: swipl -q -f loss_contract_v30.pl -- <packet>'), halt(2) ).
