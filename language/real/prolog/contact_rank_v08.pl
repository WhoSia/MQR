:- use_module(library(readutil)).
:- dynamic root/4, obligation/1, separates/2, expected_rank/1, expected_unique/1, expected_exchange/1.
reset_db :- retractall(root(_,_,_,_)),retractall(obligation(_)),retractall(separates(_,_)),retractall(expected_rank(_)),retractall(expected_unique(_)),retractall(expected_exchange(_)).
atomize(S,A):-atom_string(A,S).
parse_line(Line):-normalize_space(string(N),Line),(N=""->true;(sub_string(N,0,1,_,"#")->true;(split_string(N," \t"," \t",T),(parse_tokens(T)->true;(format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]),fail))))).
parse_tokens([]).
parse_tokens(["REALCONTACTRANK","0.8"]).
parse_tokens(["id"|_]).
parse_tokens(["claim_scope"|_]).
parse_tokens(["frontier"|_]).
parse_tokens(["query_class"|_]).
parse_tokens(["END"]).
parse_tokens(["root",RS,KS,FS]):-atomize(RS,R),atomize(KS,K),atomize(FS,F),assertz(root(R,K,F,1)).
parse_tokens(["cost",RS,CS]):-atomize(RS,R),number_string(C,CS),retract(root(R,K,F,_)),assertz(root(R,K,F,C)).
parse_tokens(["obligation",OS]):-atomize(OS,O),assertz(obligation(O)).
parse_tokens(["separates",RS,OS]):-atomize(RS,R),atomize(OS,O),assertz(separates(R,O)).
parse_tokens(["authorize_rank",X]):-atomize(X,A),assertz(expected_rank(A)).
parse_tokens(["authorize_unique",X]):-atomize(X,A),assertz(expected_unique(A)).
parse_tokens(["authorize_exchange",X]):-atomize(X,A),assertz(expected_exchange(A)).
load_packet(File):-reset_db,read_file_to_string(File,S,[]),split_string(S,"\n","\r",Lines),maplist(parse_line,Lines).
eligible_roots(Rs):-findall(R,root(R,'EXTERNAL','LIVE',_),R0),sort(R0,Rs).
choose(0,_,[]).
choose(K,[H|T],[H|R]):-K>0,K1 is K-1,choose(K1,T,R).
choose(K,[_|T],R):-K>0,choose(K,T,R).
covers(B):-forall(obligation(O),once((member(R,B),separates(R,O)))).
minimum_bases(Bases):-eligible_roots(Rs),length(Rs,N),between(0,N,K),findall(B,(choose(K,Rs,B),covers(B)),Bs0),Bs0\=[],sort(Bs0,Bases),!.
basis_cost(B,C):-findall(X,(member(R,B),root(R,_,_,X)),Xs),sum_list(Xs,C).
replace_one(B,A,X,R):-select(A,B,T),sort([X|T],R).
exchange_status([], 'UNAVAILABLE').
exchange_status([_], 'VACUOUS').
exchange_status(Bases,'FAIL'):-member(B1,Bases),member(B2,Bases),B1\=B2,member(A,B1),\+ member(A,B2),\+ (member(X,B2),\+ member(X,B1),replace_one(B1,A,X,R),member(R,Bases)),!.
exchange_status(_, 'PASS').
analysis(Min,Count,Unique,Exchange,CMin,CMax,Bases):-minimum_bases(Bases),!,Bases=[First|_],length(First,Min),length(Bases,Count),(Count=:=1->Unique='YES';Unique='NO'),exchange_status(Bases,Exchange),findall(C,(member(B,Bases),basis_cost(B,C)),Cs),min_list(Cs,CMin),max_list(Cs,CMax).
analysis('UNCOVERED',0,'NO','UNAVAILABLE','UNAVAILABLE','UNAVAILABLE',[]).
check_expected(Min,U,X):- (expected_rank(E)->term_to_atom(Min,A),(A=E->true;fail);true),(expected_unique(EU)->EU=U;true),(expected_exchange(EX)->EX=X;true).
basis_atom(B,A):-atomic_list_concat(B,'+',A).
print_bases([]):-writeln('rank.minimum_bases=').
print_bases(B):-maplist(basis_atom,B,A),atomic_list_concat(A,';',J),format('rank.minimum_bases=~w~n',[J]).
must_stage(Tag,Goal):- (call(Goal)->true;(format(user_error,'PROLOG_STAGE_FAIL=~w~n',[Tag]),fail)).
run(File):-must_stage(load_packet,load_packet(File)),must_stage(analysis,analysis(M,C,U,X,Cmin,Cmax,B)),(M='UNCOVERED'->Cov='FAIL';Cov='PASS'),format('rank.coverage_complete=~w~n',[Cov]),format('rank.minimum=~w~n',[M]),format('rank.basis_count=~w~n',[C]),format('rank.unique=~w~n',[U]),format('rank.exchange_property=~w~n',[X]),format('rank.minimum_basis_cost_min=~w~n',[Cmin]),format('rank.minimum_basis_cost_max=~w~n',[Cmax]),print_bases(B),must_stage(check_expected,check_expected(M,U,X)).
