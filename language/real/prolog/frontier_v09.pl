:- use_module(library(readutil)).
:- dynamic query/2, generator/3, rival/3, admit/2, distinguish/3, alias/3.
:- dynamic root/3, obligation/2, separates/2, search/3, grammar_closed/1.
:- dynamic expected_escape/1, expected_off_query/1, expected_common_mode/1.
:- dynamic expected_saturation_mirage/1, expected_rank_before/1, expected_rank_after/1.
:- dynamic packet_id/1, claim_scope/1.

reset_db :-
    retractall(query(_,_)), retractall(generator(_,_,_)), retractall(rival(_,_,_)),
    retractall(admit(_,_)), retractall(distinguish(_,_,_)), retractall(alias(_,_,_)),
    retractall(root(_,_,_)), retractall(obligation(_,_)), retractall(separates(_,_)),
    retractall(search(_,_,_)), retractall(grammar_closed(_)),
    retractall(expected_escape(_)), retractall(expected_off_query(_)),
    retractall(expected_common_mode(_)), retractall(expected_saturation_mirage(_)),
    retractall(expected_rank_before(_)), retractall(expected_rank_after(_)),
    retractall(packet_id(_)), retractall(claim_scope(_)).

atomize(S,A) :- atom_string(A,S).
canon(A,B,X,Y) :- (A @=< B -> X=A,Y=B ; X=B,Y=A).

parse_line(Line) :-
    normalize_space(string(N), Line),
    ( N="" -> true
    ; sub_string(N,0,1,_,"#") -> true
    ; split_string(N," \t"," \t",T),
      (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]), fail)
    ).

parse_tokens(["REALFRONTIER","0.9"]).
parse_tokens(["id",S]) :- atomize(S,A), assertz(packet_id(A)).
parse_tokens(["claim_scope",S]) :- atomize(S,A), assertz(claim_scope(A)).
parse_tokens(["query",Q,K]) :- atomize(Q,AQ), atomize(K,AK), member(AK,['BASE','EXTENSION']), assertz(query(AQ,AK)).
parse_tokens(["generator",G,C,A]) :- atomize(G,AG), atomize(C,AC), atomize(A,AA), assertz(generator(AG,AC,AA)).
parse_tokens(["rival",R,P,G]) :- atomize(R,AR), atomize(P,AP), atomize(G,AG), member(AP,['BASELINE','DISCOVERED']), assertz(rival(AR,AP,AG)).
parse_tokens(["admit",R,S]) :- atomize(R,AR), atomize(S,AS), member(AS,['PASS','HOLD','FAIL']), assertz(admit(AR,AS)).
parse_tokens(["distinguish",Q,A,B]) :- atomize(Q,AQ), atomize(A,AA), atomize(B,AB), canon(AA,AB,X,Y), assertz(distinguish(AQ,X,Y)).
parse_tokens(["alias",Q,A,B]) :- atomize(Q,AQ), atomize(A,AA), atomize(B,AB), canon(AA,AB,X,Y), assertz(alias(AQ,X,Y)).
parse_tokens(["root",R,K,F]) :- atomize(R,AR), atomize(K,AK), atomize(F,AF), member(AK,['EXTERNAL','INTERNAL']), member(AF,['LIVE','STALE','EXPIRED']), assertz(root(AR,AK,AF)).
parse_tokens(["obligation",O,P]) :- atomize(O,AO), atomize(P,AP), member(AP,['BASELINE','DISCOVERED']), assertz(obligation(AO,AP)).
parse_tokens(["separates",R,O]) :- atomize(R,AR), atomize(O,AO), assertz(separates(AR,AO)).
parse_tokens(["search",G,N,O]) :- atomize(G,AG), number_string(AN,N), atomize(O,AO), member(AO,['NEW','NO_NEW']), assertz(search(AG,AN,AO)).
parse_tokens(["grammar","CLOSED"]) :- assertz(grammar_closed(true)).
parse_tokens(["grammar","OPEN"]) :- assertz(grammar_closed(false)).
parse_tokens(["authorize_escape",X]) :- atomize(X,A), assertz(expected_escape(A)).
parse_tokens(["authorize_off_query_escape",X]) :- atomize(X,A), assertz(expected_off_query(A)).
parse_tokens(["authorize_common_mode",X]) :- atomize(X,A), assertz(expected_common_mode(A)).
parse_tokens(["authorize_saturation_mirage",X]) :- atomize(X,A), assertz(expected_saturation_mirage(A)).
parse_tokens(["authorize_rank_before",X]) :- atomize(X,A), assertz(expected_rank_before(A)).
parse_tokens(["authorize_rank_after",X]) :- atomize(X,A), assertz(expected_rank_after(A)).
parse_tokens(["END"]).

load_packet(File) :-
    reset_db,
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    maplist(parse_line,Lines),
    packet_id(_), claim_scope(_),
    query(_,_), generator(_,_,_), rival(_,_,_),
    forall(rival(R,_,G), generator(G,_,_)),
    forall(admit(R,_), rival(R,_,_)),
    forall(distinguish(Q,A,B),(query(Q,_),rival(A,_,_),rival(B,_,_),\+ alias(Q,A,B))),
    forall(alias(Q,A,B),(query(Q,_),rival(A,_,_),rival(B,_,_),\+ distinguish(Q,A,B))),
    forall(separates(R,O),(root(R,_,_),obligation(O,_))),
    forall(search(G,_,_),generator(G,_,_)).

admitted(R,P) :- rival(R,P,_), admit(R,'PASS').

distinguish_pair(Q,A,B) :- canon(A,B,X,Y), distinguish(Q,X,Y).
alias_pair(Q,A,B) :- canon(A,B,X,Y), alias(Q,X,Y).

current_query_separation :-
    \+ (admitted(A,'BASELINE'), admitted(B,'BASELINE'), A @< B,
        \+ (query(Q,'BASE'), distinguish_pair(Q,A,B))).

off_query_escape :-
    admitted(D,'DISCOVERED'),
    findall(B,admitted(B,'BASELINE'),Bs), Bs \= [],
    findall(Q,query(Q,'BASE'),BQs), BQs \= [],
    forall(member(B,Bs), forall(member(Q,BQs), alias_pair(Q,D,B))),
    admitted(B2,'BASELINE'), query(Q2,'EXTENSION'), distinguish_pair(Q2,D,B2), !.

generator_stats(GCount,ACount,Common) :-
    findall(G,(admitted(R,_),rival(R,_,G)),Gs0), sort(Gs0,Gs),
    length(Gs,GCount),
    findall(A,(member(G,Gs),generator(G,_,A)),As0), sort(As0,As),
    length(As,ACount),
    (GCount > 1, ACount < GCount -> Common='YES' ; Common='NO').

saturation_mirage :-
    search(G1,N1,'NO_NEW'), N1 > 0, generator(G1,_,A1),
    search(G2,N2,'NEW'), N2 > 0, generator(G2,_,A2),
    A1 \= A2, !.

generator_relative_saturation :-
    search(_,_,_),
    \+ (search(_,N,O), (N =:= 0 ; O \= 'NO_NEW')).

eligible_roots(Rs) :-
    findall(R,root(R,'EXTERNAL','LIVE'),R0), sort(R0,Rs).

phase_obligations(false,Os) :-
    findall(O,obligation(O,'BASELINE'),O0), sort(O0,Os).
phase_obligations(true,Os) :-
    findall(O,obligation(O,_),O0), sort(O0,Os).

choose(0,_,[]).
choose(K,[H|T],[H|R]) :- K>0, K1 is K-1, choose(K1,T,R).
choose(K,[_|T],R) :- K>0, choose(K,T,R).

covers(_,[]).
covers(B,[O|Os]) :- member(R,B), separates(R,O), !, covers(B,Os).

minimum_rank(Include,Rank) :-
    phase_obligations(Include,Os),
    ( Os=[] -> Rank=0
    ; eligible_roots(Rs), length(Rs,N),
      between(0,N,K), choose(K,Rs,B), covers(B,Os), !, Rank=K
    ), !.
minimum_rank(_, 'UNCOVERED').

yes(Goal,'YES') :- call(Goal), !.
yes(_,'NO').

check_expected(Escape,OffQ,Common,Sat,Before,After) :-
    (expected_escape(X)->X=Escape;true),
    (expected_off_query(X)->X=OffQ;true),
    (expected_common_mode(X)->X=Common;true),
    (expected_saturation_mirage(X)->X=Sat;true),
    (expected_rank_before(X)->term_to_atom(Before,A),X=A;true),
    (expected_rank_after(X)->term_to_atom(After,A),X=A;true).

run(File) :-
    load_packet(File),
    findall(R,admitted(R,'BASELINE'),B0), sort(B0,B), length(B,BC),
    findall(R,admitted(R,'DISCOVERED'),D0), sort(D0,D), length(D,DC),
    append(B,D,All0), sort(All0,All), length(All,AC),
    atomic_list_concat(All,'+',AllAtom),
    generator_stats(GC,GAC,Common),
    yes(current_query_separation,QCur),
    (D=[]->Escape='NO';Escape='YES'),
    yes(off_query_escape,OffQ),
    yes(saturation_mirage,SatMirage),
    yes(generator_relative_saturation,Sat),
    (grammar_closed(true)->Grammar='YES';Grammar='NO'),
    minimum_rank(false,Before),
    minimum_rank(true,After),
    (Escape='YES',Before==After->Stable='YES';Stable='NO'),
    ((number(Before),number(After),After>Before)->Inc='YES';Inc='NO'),
    format('frontier.baseline_rival_count=~w~n',[BC]),
    format('frontier.discovered_rival_count=~w~n',[DC]),
    format('frontier.admitted_rival_count=~w~n',[AC]),
    format('frontier.admitted_rivals=~w~n',[AllAtom]),
    format('frontier.generator_count=~w~n',[GC]),
    format('frontier.generator_ancestry_count=~w~n',[GAC]),
    format('frontier.generator_common_mode_detected=~w~n',[Common]),
    format('frontier.query_separates_current=~w~n',[QCur]),
    format('frontier.escape_detected=~w~n',[Escape]),
    format('frontier.off_query_escape=~w~n',[OffQ]),
    format('frontier.saturation_mirage=~w~n',[SatMirage]),
    format('frontier.generator_relative_saturation=~w~n',[Sat]),
    format('frontier.grammar_closed=~w~n',[Grammar]),
    format('frontier.fcr_before=~w~n',[Before]),
    format('frontier.fcr_after=~w~n',[After]),
    format('frontier.stable_rank_escape=~w~n',[Stable]),
    format('frontier.rank_increasing_escape=~w~n',[Inc]),
    writeln('frontier.world_complete=NO'),
    writeln('frontier.discovery_value_scalar=OFF'),
    writeln('frontier.fcr_guidance_scope=CONDITIONAL'),
    writeln('frontier.generator_independence_inferred=NO'),
    writeln('frontier.query_language_complete_inferred=NO'),
    writeln('frontier.admission_rule_complete_inferred=NO'),
    writeln('frontier.search_count_implies_completeness=NO'),
    check_expected(Escape,OffQ,Common,SatMirage,Before,After).
