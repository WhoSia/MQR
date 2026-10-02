:- use_module(library(readutil)).
run(File) :-
 read_file_to_string(File,S,[]), split_string(S,"\n","\r",Ls0), exclude(blank,Ls0,Ls),
 phrase(packet(M),Ls), decide(M,D,R,V),
 v(M,relation,'INCOMPARABLE',Rel),
 format("promotion.relation=~w~n",[Rel]),
 format("promotion.veto=~w~n",[V]),
 format("promotion.decision=~w~n",[D]),
 format("promotion.reason=~w~n",[R]),
 writeln("promotion.scalar_aggregation=OFF"),
 writeln("promotion.weighted_sum_universal=REJECT"),
 writeln("promotion.lexicographic_universal=REJECT"),
 writeln("promotion.pareto_selector=REJECT"),
 writeln("promotion.universal_meta_utility=NOT_EARNED"),
 writeln("promotion.prcr=CANDIDATE"),
 writeln("promotion.rag=CANDIDATE"),
 writeln("promotion.hrs=CANDIDATE").
blank(S):-string_codes(S,Cs),forall(member(C,Cs),char_type(C,space)).
packet(M) --> ["REALPROMOTE 0.27"], body([],M).
body(A,M) --> ["END"], {dict_create(M,p,A)}.
body(A0,M) --> [Line], {split_string(Line," "," ",[K,V]),atom_string(KA,K),atom_string(VA,V)}, body([KA-VA|A0],M).
v(M,K,D,V):- (get_dict(K,M,V0)->V=V0;V=D).
decide(M,'HOLD','GOVERNANCE','INACTIVE'):-v(M,sealed,'PASS',S),v(M,lineage,'PASS',L),v(M,audit,'PASS',A),(S\='PASS';L\='PASS';A\='PASS'),!.
decide(M,'HOLD','ANCESTRY_COLLAPSE_REQUIRED','INACTIVE'):-v(M,duplicate_ancestry,'NO',D),v(M,common_mode,'NO',C),(D='YES';C='YES'),!.
decide(M,'HOLD','LOCAL_VETO_ACTIVE','ACTIVE'):-v(M,veto,'OFF','ACTIVE'),v(M,fatal,'NO','YES'),v(M,scope,'LOCAL',S),v(M,veto_scope,'LOCAL',S),v(M,horizon,'MEDIUM',H),v(M,veto_horizon,'MEDIUM',H),!.
decide(M,'PROMOTE','LOCAL_DOMINANCE','INACTIVE'):-v(M,relation,'INCOMPARABLE','DOMINATES'),!.
decide(M,'HOLD','LOCAL_DEFEAT','INACTIVE'):-v(M,relation,'INCOMPARABLE','DEFEATS_UNDER_SCOPE'),!.
decide(_,'HOLD','INCOMPARABLE','INACTIVE').
