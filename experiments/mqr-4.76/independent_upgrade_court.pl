:- use_module(library(readutil)).
die(M):-writeln(user_error,M),halt(2).
yn("YES",true). yn("NO",false).

classify(_,_,_,_,_,true,_,_,"NO_UPGRADE"):-!.
classify(_,"DISJOINT",_,_,_,_,_,_,"NO_UPGRADE"):-!.
classify(_,_,_,_,_,"MERGE",_,_,"MERGE_COLLAPSE"):-!.
classify(_,"REFINE",_,_,_,_,_,_,"SPLIT_REQUIRED"):-!.
classify(_,_,_,_,_,"SPLIT",_,_,"SPLIT_REQUIRED"):-!.
classify(Route,_,false,_,_,_,_,_,
  "DIAGNOSTIC_REPLICATION_ONLY"):- member(Route,["OTHER_LAB_SAME_CALIBRATION","SECOND_PROVER_SAME_ENCODING"]),!.
classify(_,_,false,_,_,_,_,_,"NO_UPGRADE"):-!.
classify(_,_,true,false,_,_,_,_,"NO_UPGRADE"):-!.
classify(Route,_,true,true,false,_,_,_,
  "CROSS_ROUTE_INDEPENDENCE_UPGRADE"):- member(Route,["NEW_INSTRUMENT_FAMILY","DISTINCT_ENCODING_INDEPENDENT_DERIVATION"]),!.
classify(_,_,true,true,_,_,_,_,"LOCAL_AUTHORITY_UPGRADE").

bump(K,[K-N|Xs],[K-M|Xs]):-M is N+1,!.
bump(K,[X|Xs],[X|Ys]):-bump(K,Xs,Ys).
bump(K,[],[K-1]).

run(File):-
 read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls0),exclude(=(""),Ls0,[H|Rows]),
 H="case_id\tdomain\tsource_origin\ttransport_route\tchallenge_correspondence\trelevant_common_mode_broken\tindependent_cut_provenance\tresidual_common_mode\tpostoutcome_tuned\tsplit_merge_state\texpected",
 foldl(check,Rows,state(0,[]),state(N,C)),
 format("MQR476_CASES=~w~n",[N]),format("MQR476_PASS=~w~n",[N]),
 forall(member(K-Label,[
  "LOCAL_AUTHORITY_UPGRADE"-"MQR476_LOCAL",
  "CROSS_ROUTE_INDEPENDENCE_UPGRADE"-"MQR476_CROSS",
  "DIAGNOSTIC_REPLICATION_ONLY"-"MQR476_DIAGNOSTIC",
  "SPLIT_REQUIRED"-"MQR476_SPLIT",
  "MERGE_COLLAPSE"-"MQR476_MERGE",
  "NO_UPGRADE"-"MQR476_NO_UPGRADE"]),
  ((member(K-V,C)->true;V=0),format("~w=~w~n",[Label,V]))),
 writeln("MQR476_ORIGIN_NONLAUNDERING=PASS"),
 writeln("MQR476_PROLOG_CHALLENGE_COURT=PASS").

check(Line,state(N0,C0),state(N,C)):-
 split_string(Line,"\t","",T),T=[Id,Domain,Origin,Route,Corr,B0,P0,R0,Post0,SM,Expected],
 Origin="INTERNAL",yn(B0,B),yn(P0,P),yn(R0,R),yn(Post0,Post),
 classify(Route,Corr,B,P,R,Post,SM,Origin,Got),
 format("~w\t~w\t~w\t~w~n",[Id,Domain,Expected,Got]),
 (Got=Expected->true;die("court mismatch")),
 N is N0+1,bump(Got,C0,C).

:- initialization(main,main).
main(Argv):-Argv=[F|_],run(F).
