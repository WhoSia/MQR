:- use_module(library(readutil)).
evidence("OBSERVED"). evidence("PROVED"). evidence("ENUMERATED"). evidence("SIMULATED"). evidence("INFERRED"). evidence("OPEN").
relation("COMMON_MODE_HOLD"). relation("INDEPENDENT_CHALLENGE"). relation("ROUTE_DIVERSE_LOCAL").
relation("AUTHORITY_UPGRADED"). relation("BENIGN_SHARED_INFRASTRUCTURE"). relation("NO_CLOSURE_FROM_SEARCH_FAILURE").
yn("YES",true). yn("NO",false).
die(M):-writeln(user_error,M),halt(2).
field(L,K,V):-member(X,L),split_string(X," "," ",[K,V]),!.
need(L,K,V):-field(L,K,V),!;format(string(M),"missing required field: ~w",[K]),die(M).
explicit(V):-V\="",V\="OPEN".

parse_g(Line,g(Id,F,A,T,W,P,N,R,B)):-
 split_string(Line," "," ",["generator",Id,F,A,T0,W0,P0,N0,R0,B0]),
 yn(T0,T),yn(W0,W),yn(P0,P),yn(N0,N),yn(R0,R),yn(B0,B).
parse_p(Line,p(A,B,SA,SI,RD,Rel)):-
 split_string(Line," "," ",["pair",A,B,SA0,SI0,RD0,Rel]),relation(Rel),
 yn(SA0,SA),yn(SI0,SI),yn(RD0,RD).

gid(Gs,Id,g(Id,F,A,T,W,P,N,R,B)):-member(g(Id,F,A,T,W,P,N,R,B),Gs).

audit_pair(Gs,p(A,B,SA,SI,RD,Rel)):-
 gid(Gs,A,GA),gid(Gs,B,GB),
 GA=g(_,_,_,_,WA,PA,_,RA,BA),GB=g(_,_,_,_,WB,PB,_,RB,BB),
 ( Rel="COMMON_MODE_HOLD" -> SA=true
 ; Rel="INDEPENDENT_CHALLENGE" -> SA=false,RD=true,(WA=true;WB=true),PA=false,PB=false,RA=true,RB=true
 ; Rel="ROUTE_DIVERSE_LOCAL" -> SA=false,RD=true,RA=true,RB=true
 ; Rel="AUTHORITY_UPGRADED" -> SA=false,RD=true,(WA=true;WB=true),PA=false,PB=false
 ; Rel="BENIGN_SHARED_INFRASTRUCTURE" -> SA=false,SI=true
 ; Rel="NO_CLOSURE_FROM_SEARCH_FAILURE" -> (BA=true;BB=true)
 ).

count_rel(Ps,R,N):-include(has_rel(R),Ps,X),length(X,N).
has_rel(R,p(_,_,_,_,_,R)).
count_post(Gs,N):-include(post_g,Gs,X),length(X,N).
post_g(g(_,_,_,_,_,true,_,_,_)).
count_novel_irrelevant(Gs,N):-include(ni_g,Gs,X),length(X,N).
ni_g(g(_,_,_,_,_,_,true,false,_)).

emit_g([], _).
emit_g([g(Id,F,A,T,W,P,N,R,B)|Xs],I):-
 (T=true->TS="YES";TS="NO"),(W=true->WS="YES";WS="NO"),(P=true->PS="YES";PS="NO"),(N=true->NS="YES";NS="NO"),(R=true->RS="YES";RS="NO"),(B=true->BS="YES";BS="NO"),
 format("challenge.generator.~w=~w:~w:~w:~w:~w:~w:~w:~w:~w~n",[I,Id,F,A,TS,WS,PS,NS,RS,BS]),J is I+1,emit_g(Xs,J).
emit_p([], _).
emit_p([p(A,B,SA,SI,RD,R)|Xs],I):-
 (SA=true->SAS="YES";SAS="NO"),(SI=true->SIS="YES";SIS="NO"),(RD=true->RDS="YES";RDS="NO"),
 format("challenge.pair.~w=~w:~w:~w:~w:~w:~w~n",[I,A,B,SAS,SIS,RDS,R]),J is I+1,emit_p(Xs,J).

run(File):-
 read_file_to_string(File,S,[]),split_string(S,"\n","\r",Raw),exclude(=(""),Raw,L),
 (member("REALCHALLENGE 0.32-CANDIDATE",L)->true;die("expected REALCHALLENGE 0.32-CANDIDATE")),
 (member("END",L)->true;die("missing END")),
 need(L,"sealed",Seal),(Seal="PASS"->true;die("sealed must be PASS")),
 forall(member(K,["claim_scope_hash","challenge_family_hash","portfolio_id","admissibility_rule_hash","dependency_rule_hash"]),
   (need(L,K,V),(explicit(V)->true;format(string(M),"~w must be explicit",[K]),die(M)))),
 need(L,"evidence_kind",E),(evidence(E)->true;die("invalid evidence_kind")),
 need(L,"completeness_claim",CC),(CC="RELATIVE_ONLY"->true;die("completeness_claim must be RELATIVE_ONLY")),
 need(L,"open_world_complete",OW),(OW="OFF"->true;die("open_world_complete must be OFF")),
 findall(G,(member(X,L),sub_string(X,0,10,_,"generator "),parse_g(X,G)),Gs),
 findall(P,(member(X,L),sub_string(X,0,5,_,"pair "),parse_p(X,P)),Ps),
 forall(member(P,Ps),(audit_pair(Gs,P)->true;die("pair authority relation not earned"))),
 need(L,"portfolio_id",PID),length(Gs,NG),length(Ps,NP),
 count_rel(Ps,"COMMON_MODE_HOLD",CM),count_rel(Ps,"INDEPENDENT_CHALLENGE",IC),count_rel(Ps,"AUTHORITY_UPGRADED",AU),count_rel(Ps,"NO_CLOSURE_FROM_SEARCH_FAILURE",NC),
 count_post(Gs,PG),count_novel_irrelevant(Gs,NI),
 format("challenge.portfolio_id=~w~n",[PID]),format("challenge.generator_count=~w~n",[NG]),format("challenge.pair_count=~w~n",[NP]),
 format("challenge.common_mode_count=~w~n",[CM]),format("challenge.independent_count=~w~n",[IC]),format("challenge.authority_upgrade_count=~w~n",[AU]),format("challenge.no_closure_count=~w~n",[NC]),
 format("challenge.postoutcome_generator_count=~w~n",[PG]),format("challenge.novel_irrelevant_count=~w~n",[NI]),
 writeln("challenge.novelty_is_independence=NO"),writeln("challenge.algorithm_diversity_is_assumption_diversity=NO"),
 writeln("challenge.shared_infrastructure_is_automatic_dependence=NO"),writeln("challenge.bounded_search_failure_is_counterexample_absence=NO"),
 writeln("challenge.portfolio_diversity_is_generator_completeness=NO"),writeln("challenge.postoutcome_tuning_is_prospective_authority=NO"),
 writeln("challenge.completeness_claim=RELATIVE_ONLY"),writeln("challenge.open_world_complete=OFF"),
 format("challenge.evidence_kind=~w~n",[E]),writeln("challenge.status=CANDIDATE_UNPROMOTED"),
 emit_g(Gs,0),emit_p(Ps,0).
:- initialization(main,main).
main(Argv):- (Argv=[F|_]->run(F);die("usage: challenge_v32.pl <packet>")).
