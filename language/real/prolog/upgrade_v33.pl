:- use_module(library(readutil)).
origin("INTERNAL"). origin("EXTERNAL"). origin("MIXED"). origin("UNKNOWN").
corr("EXACT"). corr("REFINE"). corr("MERGE"). corr("OVERLAP"). corr("DISJOINT").
contact("MEASUREMENT"). contact("RAW_DATA"). contact("ANALYSIS"). contact("SEMANTIC"). contact("PROOF"). contact("MODEL"). contact("NONE").
sm("NONE"). sm("SPLIT"). sm("MERGE").
state("NO_UPGRADE"). state("DIAGNOSTIC_REPLICATION_ONLY"). state("LOCAL_AUTHORITY_UPGRADE").
state("CROSS_ROUTE_INDEPENDENCE_UPGRADE"). state("SPLIT_REQUIRED"). state("MERGE_COLLAPSE"). state("REOPEN").
effect("BREAK"). effect("PRESERVE"). effect("REPLACE"). effect("UNRESOLVED"). effect("NEW").
yn("YES",true). yn("NO",false).
die(M):-writeln(user_error,M),halt(2).
explicit(V):-V\="",V\="OPEN",V\="NA".
field(L,K,V):-member(X,L),split_string(X," "," ",[K,V]),!.
need(L,K,V):-field(L,K,V),!;format(string(M),"missing required field: ~w",[K]),die(M).
parse_dep(Line,d(N,E,P)):-split_string(Line," "," ",["dependency",N,E,P]),effect(E),
 ((member(E,["BREAK","REPLACE","NEW"]))->explicit(P);true).
count_break(Ds,N):-include(is_break,Ds,X),length(X,N).
is_break(d(_,"BREAK",_)).
emit([], _).
emit([d(N,E,P)|Xs],I):-format("upgrade.dependency.~w=~w:~w:~w~n",[I,N,E,P]),J is I+1,emit(Xs,J).

run(File):-
 read_file_to_string(File,S,[]),split_string(S,"\n","\r",Raw),exclude(=(""),Raw,L),
 member("REALUPGRADE 0.33-CANDIDATE",L),member("END",L),
 need(L,"sealed","PASS"),
 forall(member(K,["id","source_challenge_hash","claim_scope_hash","source_dependency_graph_hash","witness_route","witness_provenance_hash","certificate_version"]),
   (need(L,K,V),(explicit(V)->true;die("required token must be explicit")))),
 need(L,"origin",O),origin(O),need(L,"correspondence",C),corr(C),
 need(L,"postoutcome_tuned",P0),yn(P0,Post),need(L,"contact_kind",Contact),contact(Contact),
 need(L,"split_merge",SM),sm(SM),need(L,"residual_common_mode",R0),yn(R0,Residual),
 need(L,"authority_state",State),state(State),
 need(L,"reopen_on_ancestry_revision","YES"),
 findall(D,(member(X,L),sub_string(X,0,11,_,"dependency "),parse_dep(X,D)),Ds),count_break(Ds,B),
 ((member(State,["LOCAL_AUTHORITY_UPGRADE","CROSS_ROUTE_INDEPENDENCE_UPGRADE"]))->
    (C\="DISJOINT",Post=false,B>0);true),
 (State="CROSS_ROUTE_INDEPENDENCE_UPGRADE"->Residual=false,Contact\="NONE";true),
 (State="SPLIT_REQUIRED"->(SM="SPLIT";member(C,["REFINE","OVERLAP"]));true),
 (State="MERGE_COLLAPSE"->SM="MERGE";true),
 need(L,"id",Id),
 format("upgrade.id=~w~n",[Id]),format("upgrade.origin=~w~n",[O]),format("upgrade.correspondence=~w~n",[C]),
 format("upgrade.contact_kind=~w~n",[Contact]),format("upgrade.split_merge=~w~n",[SM]),
 format("upgrade.residual_common_mode=~w~n",[R0]),format("upgrade.postoutcome_tuned=~w~n",[P0]),
 format("upgrade.authority_state=~w~n",[State]),format("upgrade.break_count=~w~n",[B]),length(Ds,ND),format("upgrade.dependency_count=~w~n",[ND]),
 writeln("upgrade.original_independence_rewritten=NO"),writeln("upgrade.independence_scalar=OFF"),
 writeln("upgrade.reopen_on_ancestry_revision=YES"),writeln("upgrade.status=CANDIDATE_UNPROMOTED"),emit(Ds,0).
:- initialization(main,main).
main(Argv):- (Argv=[F|_]->(run(F)->true;die("packet authority relation not earned"));die("usage: upgrade_v33.pl <packet>")).
