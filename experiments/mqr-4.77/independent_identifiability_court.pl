:- use_module(library(readutil)).
die(M):-writeln(user_error,M),halt(2).
yn("YES",true). yn("NO",false).

classify("later_hidden_ancestor_discovered",_,_,_,_,"REOPEN_HIDDEN_COMMON_MODE"):-!.
classify("later_evidence_restores_decisive_shared_path",_,_,_,_,"BREAK_DEFEATED"):-!.
classify(_,false,_,_,_,"LOCALLY_SEPARATED_BREAK"):-!.
classify(_,true,_,_,false,"LOCALLY_SEPARATED_BREAK"):-!.
classify("single_selected_graph_only",true,false,_,true,"UNIDENTIFIED_BREAK"):-!.
classify("negative_control_not_discriminating_graphs",true,false,_,true,"DIAGNOSTIC_BREAK_ONLY"):-!.
classify(_,true,false,_,true,"PARTIALLY_IDENTIFIED_BREAK"):-!.
classify(_,true,true,false,true,"DIAGNOSTIC_BREAK_ONLY"):-!.
classify(S,true,true,true,true,"LOCALLY_SEPARATED_BREAK"):-
 member(S,["independent_raw_data_independent_preprocessing_same_anomaly","independent_reformalization_same_theorem","partial_theorem_correspondence"]),!.
classify(_,true,true,true,true,"ROBUST_SEPARATION_WITHIN_DECLARED_FAMILY").

bump(K,[K-N|Xs],[K-M|Xs]):-M is N+1,!.
bump(K,[X|Xs],[X|Ys]):-bump(K,Xs,Ys).
bump(K,[],[K-1]).

check(Line,state(N0,C0),state(N,C)):-
 split_string(Line,"\t","",T),
 T=[Id,Domain,Scenario,D0,S0,P0,R0,F0,Expected],
 yn(D0,D),yn(S0,S),yn(P0,P),yn(R0,R),yn(F0,F),
 (F=false->true;die("global graph fetish forbidden")),
 classify(Scenario,D,S,P,R,Got),
 format("~w\t~w\t~w\t~w~n",[Id,Domain,Expected,Got]),
 (Got=Expected->true;die("court mismatch")),
 N is N0+1,bump(Got,C0,C).

run(File):-
 read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls0),exclude(=(""),Ls0,[H|Rows]),
 H="id\tdomain\tscenario\tlive_graphs_disagree_on_cut\tseparator_targets_disagreement\tprospective\tclaim_relevant_ambiguity\tfull_graph_needed\texpected_state",
 foldl(check,Rows,state(0,[]),state(N,C)),
 format("MQR477_CASES=~w~n",[N]),format("MQR477_PASS=~w~n",[N]),
 forall(member(K,[ "UNIDENTIFIED_BREAK","DIAGNOSTIC_BREAK_ONLY","PARTIALLY_IDENTIFIED_BREAK",
                   "LOCALLY_SEPARATED_BREAK","ROBUST_SEPARATION_WITHIN_DECLARED_FAMILY",
                   "REOPEN_HIDDEN_COMMON_MODE","BREAK_DEFEATED"]),
        ((member(K-V,C)->true;V=0),format("MQR477_~w=~w~n",[K,V]))),
 writeln("MQR477_FULL_GRAPH_IDENTIFICATION_REQUIRED=NO"),
 writeln("MQR477_SELECTED_GRAPH_LAUNDERING=REJECT"),
 writeln("MQR477_OPEN_WORLD_INDEPENDENCE=REJECT"),
 writeln("MQR477_PROLOG_COURT=PASS").

:- initialization(main,main).
main(Argv):-Argv=[F|_],run(F).
