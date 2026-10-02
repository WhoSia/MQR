:- use_module(library(readutil)).

run(File) :-
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Ls0),
    exclude(blank,Ls0,Ls),
    Ls = ["REALPROMOTE 0.28"|Rest],
    phrase(body([],M),Rest),
    decide(M).

blank(S) :- string_codes(S,Cs), forall(member(C,Cs), char_type(C,space)).
body(A,M) --> ["END"], {dict_create(M,p,A)}.
body(A0,M) --> [Line],
    { split_string(Line," "," ",[K,V]), atom_string(KA,K), atom_string(VA,V) },
    body([KA-VA|A0],M).

v(M,K,D,V) :- (get_dict(K,M,V0) -> V=V0 ; V=D).
yes('YES'). yes('ACTIVE'). yes('PASS').
b(M,K,D,B) :- v(M,K,D,V), (yes(V) -> B=true ; B=false).

decide(M) :-
    v(M,sealed,'PASS','PASS'),
    v(M,lineage,'PASS','PASS'),
    v(M,audit,'PASS','PASS'),
    v(M,prior_relation,'INCOMPARABLE',Old),
    v(M,new_relation,'INCOMPARABLE',New),
    v(M,scope_before,'LOCAL',SB), v(M,scope_after,'LOCAL',SA),
    v(M,horizon_before,'MEDIUM',HB), v(M,horizon_after,'MEDIUM',HA),
    v(M,reason_before,'INDEPENDENT_WORLD_CONTACT',RB),
    v(M,reason_after,'INDEPENDENT_WORLD_CONTACT',RA),
    b(M,veto_before,'OFF',VB), b(M,veto_after,'OFF',VA),
    b(M,cycle_before,'OFF',CB), b(M,cycle_after,'OFF',CA),
    b(M,reopen,'NO',Reopen), b(M,lost_option,'NO',Lost),
    b(M,irreversible_debt,'NO',Debt),
    b(M,provenance_changed,'NO',Prov),
    b(M,material_history,'NO',MF),
    b(M,chronology_only,'NO',Chron),
    b(M,event_order_sensitive,'NO',OrderSensitive),
    b(M,same_ancestry,'YES',SameAnc),
    any_true4(MF,Lost,Debt,Prov,Material),
    transition(Chron,Material,RB,RA,VB,VA,Reopen,SB,SA,HB,HA,CB,CA,Old,New,T),
    exact_restore(Old,New,SB,SA,HB,HA,RB,RA,VB,VA,CB,CA,Lost,Debt,Prov,Exact),
    mutation(RB,RA,Mutation),
    independent_warrant(RB,RA,SameAnc,Independent),
    veto_transition(VB,VA,VT),
    bool_word(Material,MW),
    any_true2(Material,OrderSensitive,Path), bool_word(Path,PW),
    (OrderSensitive=true -> Comm=false ; Comm=true), bool_word(Comm,CW),
    any_true3(Lost,Debt,Prov,Hb), (Hb=true -> H='ACTIVE' ; H='INACTIVE'),
    any_true2(Lost,Debt,Lb), (Lb=true -> LOD='ACTIVE' ; LOD='INACTIVE'),
    bool_word(Reopen,RW), bool_word(Exact,EW),
    format("promotion.transition=~w~n",[T]),
    format("promotion.old_relation=~w~n",[Old]),
    format("promotion.new_relation=~w~n",[New]),
    format("promotion.history_material=~w~n",[MW]),
    format("promotion.path_sensitive=~w~n",[PW]),
    format("promotion.revision_commutative=~w~n",[CW]),
    format("promotion.hysteresis=~w~n",[H]),
    format("promotion.lost_option_debt=~w~n",[LOD]),
    format("promotion.reason_mutation=~w~n",[Mutation]),
    format("promotion.veto_transition=~w~n",[VT]),
    format("promotion.reopen=~w~n",[RW]),
    format("promotion.exact_restoration=~w~n",[EW]),
    format("promotion.independent_warrant_created=~w~n",[Independent]),
    writeln("promotion.history_scalarization=OFF"),
    writeln("promotion.universal_historical_meta_utility=NOT_EARNED"),
    writeln("promotion.prtr=CANDIDATE"),
    writeln("promotion.phl=CANDIDATE"),
    writeln("promotion.odr=CANDIDATE"),
    writeln("promotion.rmr=CANDIDATE").

any_true2(A,B,true) :- (A=true ; B=true), !.\nany_true2(_,_,false).\nany_true3(A,B,C,true) :- (A=true ; B=true ; C=true), !.\nany_true3(_,_,_,false).\nany_true4(A,B,C,D,true) :- (A=true ; B=true ; C=true ; D=true), !.\nany_true4(_,_,_,_,false).\n\nbool_word(true,'YES'). bool_word(false,'NO').

transition(true,false,_,_,_,_,_,_,_,_,_,_,_,_,_,'HISTORY_IRRELEVANT') :- !.
transition(_,_,RB,RA,_,_,_,_,_,_,_,_,_,_,_,'REASON_MUTATED') :- RB \= RA, !.
transition(_,_,_,_,false,true,_,_,_,_,_,_,_,_,_,'VETO_ACTIVATED') :- !.
transition(_,_,_,_,true,false,_,_,_,_,_,_,_,_,_,'VETO_RETIRED') :- !.
transition(_,_,_,_,_,_,true,_,_,_,_,_,_,_,_,'REOPENED') :- !.
transition(_,_,_,_,_,_,_,SB,SA,_,_,_,_,_,_,'SCOPE_REVERSED') :- SB \= SA, !.
transition(_,_,_,_,_,_,_,_,_,HB,HA,_,_,_,_,'HORIZON_REVERSED') :- HB \= HA, !.
transition(_,_,_,_,_,_,_,_,_,_,_,false,true,_,_,'CYCLE_ENTERED') :- !.
transition(_,_,_,_,_,_,_,_,_,_,_,true,false,_,_,'CYCLE_EXITED') :- !.
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,'INCOMPARABLE','DOMINATES','INCOMPARABLE_TO_DOMINATES') :- !.
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,'DOMINATES','INCOMPARABLE','DOMINATES_TO_INCOMPARABLE') :- !.
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,Old,New,'RELATION_REVISED') :- Old \= New, !.
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,'STABLE').

exact_restore(O,O,S,S,H,H,R,R,V,V,C,C,false,false,false,true) :- !.
exact_restore(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,false).

mutation(R,R,'NONE') :- !.
mutation(RB,RA,M) :- atomic_list_concat([RB,'TO',RA],'_',M).

independent_warrant(R,R,_, 'NOT_INFERRED') :- !.
independent_warrant(_,_,true,'NO') :- !.
independent_warrant(_,_,false,'NOT_INFERRED').

veto_transition(false,true,'ACTIVATED') :- !.
veto_transition(true,false,'RETIRED') :- !.
veto_transition(_,_, 'STABLE').
