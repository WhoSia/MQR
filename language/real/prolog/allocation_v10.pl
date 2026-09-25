:- use_module(library(readutil)).
:- dynamic lane/6, obligation/3, allocation/3, outcome/3.
:- dynamic packet_id/1, claim_scope/1, budget/1, horizon/1, reserve/1.
:- dynamic normative_prior/1, normative_utility/1, history_signature/1, policy/1.
:- dynamic witness_escape_lane/1.
:- dynamic expected_acrr/1, expected_starvation/1, expected_debt/1.
:- dynamic expected_escape_reallocation/1, expected_common_mode/1.
:- dynamic seen_header/0, seen_end/0.

reset_db :-
    retractall(lane(_,_,_,_,_,_)), retractall(obligation(_,_,_)),
    retractall(allocation(_,_,_)), retractall(outcome(_,_,_)),
    retractall(packet_id(_)), retractall(claim_scope(_)), retractall(budget(_)),
    retractall(horizon(_)), retractall(reserve(_)),
    retractall(normative_prior(_)), retractall(normative_utility(_)),
    retractall(history_signature(_)), retractall(policy(_)),
    retractall(witness_escape_lane(_)),
    retractall(expected_acrr(_)), retractall(expected_starvation(_)),
    retractall(expected_debt(_)), retractall(expected_escape_reallocation(_)),
    retractall(expected_common_mode(_)), retractall(seen_header), retractall(seen_end).

atomize(S,A) :- atom_string(A,S).

parse_line(Line) :-
    normalize_space(string(N), Line),
    ( N="" -> true
    ; sub_string(N,0,1,_,"#") -> true
    ; seen_end -> true
    ; split_string(N," \t"," \t",T),
      ( T=["REALALLOCATE","0.10"] ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]), fail)
      ; seen_header ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]), fail)
      ; format(user_error,'PROLOG_HEADER_REQUIRED line=~s~n',[Line]), fail
      )
    ).

parse_tokens(["REALALLOCATE","0.10"]) :- assertz(seen_header).
parse_tokens(["id",S]) :- atomize(S,A), assertz(packet_id(A)).
parse_tokens(["claim_scope",S]) :- atomize(S,A), assertz(claim_scope(A)).
parse_tokens(["budget",S]) :- number_string(N,S), N>=0, assertz(budget(N)).
parse_tokens(["horizon",S]) :- number_string(N,S), N>=0, assertz(horizon(N)).
parse_tokens(["lane",I,A,C,M,R,K]) :-
    atomize(I,AI), atomize(A,AA), number_string(N,C), N>0,
    atomize(M,AM), member(AM,['MANDATORY','OPTIONAL']),
    atomize(R,AR), member(AR,['REOPENING','EXPLOITATION']),
    atomize(K,AK), member(AK,['GENERATOR','QUERY','REPRESENTATION','INSTRUMENT','RESIDUAL','EXTERNAL_CASE']),
    \+ lane(AI,_,_,_,_,_), assertz(lane(AI,AA,N,AM,AR,AK)).
parse_tokens(["obligation",I,L,D]) :-
    atomize(I,AI), atomize(L,AL), number_string(N,D), N>0,
    \+ obligation(AI,_,_), assertz(obligation(AI,AL,N)).
parse_tokens(["allocate",S,L,U]) :-
    number_string(NS,S), atomize(L,AL), number_string(NU,U), NS>0, NU>=0,
    assertz(allocation(NS,AL,NU)).
parse_tokens(["outcome",S,L,O]) :-
    number_string(NS,S), atomize(L,AL), atomize(O,AO), NS>0,
    member(AO,['NEW','NO_NEW','ESCAPE','NA']), assertz(outcome(NS,AL,AO)).
parse_tokens(["reserve",S]) :- number_string(N,S), N>=0, assertz(reserve(N)).
parse_tokens(["normative_prior",S]) :-
    atomize(S,A), member(A,['NONE','DECLARED']), assertz(normative_prior(A)).
parse_tokens(["normative_utility",S]) :-
    atomize(S,A), member(A,['NONE','DECLARED']), assertz(normative_utility(A)).
parse_tokens(["history_signature",S]) :- atomize(S,A), assertz(history_signature(A)).
parse_tokens(["policy",S]) :- atomize(S,A), assertz(policy(A)).
parse_tokens(["witness_escape_lane",S]) :- atomize(S,A), assertz(witness_escape_lane(A)).
parse_tokens(["authorize_acrr",S]) :- atomize(S,A), assertz(expected_acrr(A)).
parse_tokens(["authorize_starvation",S]) :- atomize(S,A), assertz(expected_starvation(A)).
parse_tokens(["authorize_debt",S]) :- atomize(S,A), assertz(expected_debt(A)).
parse_tokens(["authorize_escape_reallocation",S]) :- atomize(S,A), assertz(expected_escape_reallocation(A)).
parse_tokens(["authorize_common_mode",S]) :- atomize(S,A), assertz(expected_common_mode(A)).
parse_tokens(["END"]) :- assertz(seen_end).

load_packet(File) :-
    reset_db,
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    maplist(parse_line,Lines),
    seen_header, seen_end,
    packet_id(_), claim_scope(_), budget(_), horizon(_), reserve(_), lane(_,_,_,_,_,_),
    normative_prior(_), normative_utility(_), history_signature(_), policy(_), witness_escape_lane(W),
    \+ (obligation(_,L,_), \+ lane(L,_,_,'MANDATORY',_,_)),
    \+ (allocation(_,L,_), \+ lane(L,_,_,_,_,_)),
    \+ (allocation(S,_,_), horizon(H), S>H),
    \+ (outcome(_,L,_), \+ lane(L,_,_,_,_,_)),
    \+ (outcome(S,_,_), horizon(H), S>H),
    (W='NONE';lane(W,_,_,_,_,_)).

sum_allocated(T) :-
    findall(U,allocation(_,_,U),Us), sum_list(Us,T).

spend_until(L,Due,T) :-
    findall(U,(allocation(S,L,U),S=<Due),Us), sum_list(Us,T).

role_spend(Role,T) :-
    findall(U,(allocation(_,L,U),lane(L,_,_,_,Role,_)),Us), sum_list(Us,T).

debt_item(I,K) :-
    obligation(I,L,D), horizon(H), D=<H,
    lane(L,_,Cost,'MANDATORY',_,K),
    spend_until(L,D,T), T<Cost.

debt_items(Items,Classes) :-
    findall(X,(debt_item(I,K),atomic_list_concat([I,'@',K],X)),Xs), sort(Xs,Items),
    findall(K,debt_item(_,K),Ks), sort(Ks,Classes).

yes(true,'YES') :- !.
yes(_,'NO').

acrr(true) :-
    reserve(R), R>0, lane(_,_,Cost,_, 'REOPENING',_), Cost=<R, !.
acrr(false).

common_mode(true) :-
    findall(L,lane(L,_,_,_,_,_),Ls0), sort(Ls0,Ls), length(Ls,N), N>1,
    findall(A,lane(_,A,_,_,_,_),As0), sort(As0,As), length(As,M), M<N, !.
common_mode(false).

check_expected(ACRR,Starve,Debt,Escape,Common) :-
    (expected_acrr(X)->X=ACRR;true),
    (expected_starvation(X)->X=Starve;true),
    (expected_debt(X)->atom_number(X,Debt);true),
    (expected_escape_reallocation(X)->X=Escape;true),
    (expected_common_mode(X)->X=Common;true).

join_or_none([], 'NONE').
join_or_none(Xs, A) :- Xs\=[], atomic_list_concat(Xs,'+',A).

run(File) :-
    load_packet(File),
    budget(B), horizon(H), reserve(R),
    sum_allocated(T), Committed is T+R,
    (Committed=<B->BudgetOk='YES';BudgetOk='NO'),
    findall(L,lane(L,_,_,_,_,_),Ls0), sort(Ls0,Ls), length(Ls,LaneCount),
    findall(L,lane(L,_,_,'MANDATORY',_,_),Ms0), sort(Ms0,Ms), length(Ms,MandatoryCount),
    findall(A,lane(_,A,_,_,_,_),As0), sort(As0,As), length(As,AncestryCount),
    common_mode(CMB), yes(CMB,Common),
    (R>0->Nominal='YES';Nominal='NO'),
    acrr(ACRRB), yes(ACRRB,ACRR),
    (ACRR='YES'->ReserveState='LIVE';Nominal='YES'->ReserveState='NOMINAL_ONLY';ReserveState='ABSENT'),
    debt_items(Debts,DebtClasses), length(Debts,DebtCount),
    (DebtCount>0->Starve='YES';Starve='NO'),
    join_or_none(Debts,DebtAtom), join_or_none(DebtClasses,DebtClassAtom),
    role_spend('EXPLOITATION',ExploitSpend), role_spend('REOPENING',ReopenSpend),
    (Starve='YES',ExploitSpend>0,ReopenSpend=:=0->ExplorationStarved='YES';ExplorationStarved='NO'),
    findall(1,outcome(_,_, 'NEW'),NewXs), length(NewXs,NewCount),
    policy(Policy),
    (Policy='GREEDY_YIELD',NewCount>0,ExplorationStarved='YES'->Greedy='YES';Greedy='NO'),
    (outcome(_,_, 'ESCAPE')->Escape='YES';Escape='NO'),
    normative_prior(Prior), normative_utility(Utility),
    (Prior='DECLARED',Utility='DECLARED'->OptScope='DECLARED_MODEL_ONLY';OptScope='NOT_AUTHORIZED'),
    (BudgetOk='YES',Starve='NO',ACRR='YES'->Envelope='YES';Envelope='NO'),
    format('allocation.budget=~w~n',[B]),
    format('allocation.horizon=~w~n',[H]),
    format('allocation.total_allocated=~w~n',[T]),
    format('allocation.reserve_units=~w~n',[R]),
    format('allocation.budget_valid=~w~n',[BudgetOk]),
    format('allocation.lane_count=~w~n',[LaneCount]),
    format('allocation.mandatory_lane_count=~w~n',[MandatoryCount]),
    format('allocation.ancestry_count=~w~n',[AncestryCount]),
    format('allocation.common_mode_detected=~w~n',[Common]),
    format('allocation.nominal_reserve=~w~n',[Nominal]),
    format('allocation.activation_capable_reserve=~w~n',[ACRR]),
    format('allocation.reserve_state=~w~n',[ReserveState]),
    format('allocation.starvation_detected=~w~n',[Starve]),
    format('allocation.exploration_debt_count=~w~n',[DebtCount]),
    format('allocation.exploration_debt_items=~w~n',[DebtAtom]),
    format('allocation.exploration_debt_classes=~w~n',[DebtClassAtom]),
    writeln('allocation.debt_scalar_default=OFF'),
    writeln('allocation.opportunity_cost_mode=VECTOR'),
    format('allocation.exploitation_spend=~w~n',[ExploitSpend]),
    format('allocation.reopening_spend=~w~n',[ReopenSpend]),
    format('allocation.exploration_starved=~w~n',[ExplorationStarved]),
    format('allocation.greedy_yield_starvation_witness=~w~n',[Greedy]),
    format('allocation.escape_detected=~w~n',[Escape]),
    format('allocation.escape_reallocation_required=~w~n',[Escape]),
    writeln('allocation.reopen_on_escape=YES'),
    format('allocation.normative_prior=~w~n',[Prior]),
    format('allocation.normative_utility=~w~n',[Utility]),
    writeln('allocation.hidden_prior_inferred=NO'),
    writeln('allocation.hidden_utility_inferred=NO'),
    writeln('allocation.expected_discovery_value_inferred=NO'),
    writeln('allocation.unique_optimum_authorized=NO'),
    writeln('allocation.universal_next_action=UNIDENTIFIED'),
    format('allocation.local_optimizer_scope=~w~n',[OptScope]),
    writeln('allocation.guidance_mode=SET_VALUED_CONTRACT_RELATIVE'),
    format('allocation.admissible_envelope=~w~n',[Envelope]),
    writeln('allocation.randomization_epistemic_oracle=NO'),
    writeln('allocation.policy_path_provenance=REQUIRED'),
    writeln('allocation.world_optimum_identified=NO'),
    writeln('allocation.world_frontier_complete=NO'),
    writeln('allocation.stopping_rule=FORBIDDEN'),
    check_expected(ACRR,Starve,DebtCount,Escape,Common).
