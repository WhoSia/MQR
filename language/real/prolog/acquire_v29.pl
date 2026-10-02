:- use_module(library(readutil)).

run(File) :-
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    flag(Lines,"myopic_best",Myopic),
    flag(Lines,"option_loss",OptionLoss),
    flag(Lines,"unique_future_separator",Separator),
    flag(Lines,"identifiability_gain",IdGain),
    flag(Lines,"live_claim_relevance",Live),
    flag(Lines,"prior_sensitive",Prior),
    flag(Lines,"model_sensitive",Model),
    flag(Lines,"representation_sensitive",Repr),
    flag(Lines,"sampling_blind_spot",Blind0),
    flag(Lines,"confirmation_loop",Confirm),
    flag(Lines,"generator_closed",GenClosed),
    flag(Lines,"common_mode",Common),
    flag_default_yes(Lines,"reopening_reserve",Reserve),
    flag(Lines,"order_sensitive",Order),
    flag(Lines,"exploration_debt",Debt),
    flag(Lines,"causal_decisive",Causal),
    flag(Lines,"randomization",Random),
    flag(Lines,"hidden_rival",Hidden),
    flag(Lines,"intervention_drift",Drift),
    flag(Lines,"contamination",Contam),
    flag(Lines,"pareto_multiple",Pareto),
    flag(Lines,"destructive",Destructive),
    flag(Lines,"outcome_contingent_loss",OutcomeLoss),
    or3(Blind0,Confirm,GenClosed,Blind),
    and2(OptionLoss,Separator,OptReq),
    choose_state(Destructive,OptReq,Hidden,GenClosed,Debt,Prior,Model,Repr,Pareto,Random,State),
    and2(IdGain,Live,IdLocal),
    or4(Separator,Causal,Hidden,IdLocal,Anticipation),
    output(State,OptReq,Myopic,IdLocal,Order,Blind,Common,Reserve,Hidden,GenClosed,Debt,OutcomeLoss,Random,Pareto,Anticipation,Drift,Contam).

field(Lines,K,D,V) :-
    ( member(Line,Lines),
      split_string(Line," "," ",[K0,V0]),
      K0 = K
    -> atom_string(V,V0)
    ; V = D).

flag(Lines,K,true) :-
    field(Lines,K,'NO',V),
    memberchk(V,['YES','ACTIVE','PASS']),
    !.
flag(_,_,false).

flag_default_yes(Lines,K,false) :-
    field(Lines,K,'YES',V),
    memberchk(V,['NO','OFF','FAIL']),
    !.
flag_default_yes(_,_,true).

and2(true,true,true) :- !.
and2(_,_,false).

or3(true,_,_,true) :- !.
or3(_,true,_,true) :- !.
or3(_,_,true,true) :- !.
or3(_,_,_,false).

or4(true,_,_,_,true) :- !.
or4(_,true,_,_,true) :- !.
or4(_,_,true,_,true) :- !.
or4(_,_,_,true,true) :- !.
or4(_,_,_,_,false).

choose_state(true,true,_,_,_,_,_,_,_,_,'FORBIDDEN_BY_DESTRUCTIVE_CONTRACT') :- !.
choose_state(_,true,_,_,_,_,_,_,_,_,'OPTION_PRESERVE') :- !.
choose_state(_,_,true,_,_,_,_,_,_,_,'REOPEN_REQUIRED') :- !.
choose_state(_,_,_,true,_,_,_,_,_,_,'REOPEN_REQUIRED') :- !.
choose_state(_,_,_,_,true,_,_,_,_,_,'DEBT_CARRY') :- !.
choose_state(_,_,_,_,_,true,_,_,_,_,'HOLD_INCOMPARABLE') :- !.
choose_state(_,_,_,_,_,_,true,_,_,_,'HOLD_INCOMPARABLE') :- !.
choose_state(_,_,_,_,_,_,_,true,_,_,'HOLD_INCOMPARABLE') :- !.
choose_state(_,_,_,_,_,_,_,_,true,_,'HOLD_INCOMPARABLE') :- !.
choose_state(_,_,_,_,_,_,_,_,_,true,'BOUNDED_EXTERIOR_PROBE') :- !.
choose_state(_,_,_,_,_,_,_,_,_,_,'LOCAL_ADMISSIBLE').

word(true,'YES').
word(false,'NO').

output(State,OptReq,Myopic,IdLocal,Order,Blind,Common,Reserve,Hidden,GenClosed,Debt,OutcomeLoss,Random,Pareto,Anticipation,Drift,Contam) :-
    word(OptReq,OptW),
    (Myopic=true,OptReq=true -> MyopicW='NO' ; MyopicW='NOT_DEFEATED'),
    word(IdLocal,IdW),
    (Order=true -> Comm='NO' ; Comm='YES'),
    word(Blind,BlindW),
    (Common=true -> Indep='NO' ; Indep='NOT_DEFEATED'),
    word(Reserve,ReserveW),
    or3(Hidden,GenClosed,Blind,Reopen),
    word(Reopen,ReopenW),
    (Debt=true -> DebtW='ACTIVE' ; DebtW='INACTIVE'),
    word(OutcomeLoss,OutcomeW),
    (Pareto=true -> ParetoW='NO' ; ParetoW='NOT_APPLICABLE'),
    word(Anticipation,AntW),
    (Drift=true -> DriftW='NO' ; DriftW='NOT_DEFEATED'),
    (Contam=true -> BaseW='NO' ; BaseW='NOT_DEFEATED'),
    format("acquisition.selection_state=~w~n",[State]),
    format("acquisition.option_preservation_required=~w~n",[OptW]),
    format("acquisition.myopic_sequence_optimal=~w~n",[MyopicW]),
    format("acquisition.identifiability_local_value=~w~n",[IdW]),
    writeln("acquisition.identifiability_universal_value=NO"),
    format("acquisition.query_order_commutative=~w~n",[Comm]),
    format("acquisition.policy_blind_spot=~w~n",[BlindW]),
    format("acquisition.evidence_independence=~w~n",[Indep]),
    format("acquisition.reopening_reserve_active=~w~n",[ReserveW]),
    format("acquisition.reopening_required=~w~n",[ReopenW]),
    format("acquisition.exploration_debt=~w~n",[DebtW]),
    format("acquisition.outcome_contingent_option_loss=~w~n",[OutcomeW]),
    writeln("acquisition.randomization_oracle=NO"),
    writeln("acquisition.fixed_exploration_universal=NO"),
    format("acquisition.pareto_unique_selector=~w~n",[ParetoW]),
    writeln("acquisition.cost_ratio_universal=NO"),
    format("acquisition.relation_anticipation_material=~w~n",[AntW]),
    format("acquisition.intervention_semantics_stable=~w~n",[DriftW]),
    format("acquisition.baseline_preserved=~w~n",[BaseW]),
    writeln("acquisition.history_scalarization=OFF"),
    writeln("acquisition.universal_expected_epistemic_utility_optimizer=NOT_EARNED"),
    writeln("acquisition.easr=CANDIDATE"),
    writeln("acquisition.raer=CANDIDATE"),
    writeln("acquisition.opr=CANDIDATE"),
    writeln("acquisition.idr=CANDIDATE"),
    writeln("acquisition.arr=CANDIDATE"),
    writeln("acquisition.nedl=CANDIDATE").
