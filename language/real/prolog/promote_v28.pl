:- use_module(library(readutil)).

run(File) :-
 read_file_to_string(File,S,[]),
 split_string(S,"\n","\r",Lines),
 field(Lines,"prior_relation","INCOMPARABLE",Old),
 field(Lines,"new_relation","INCOMPARABLE",New),
 field(Lines,"reason_before","INDEPENDENT_WORLD_CONTACT",RB),
 field(Lines,"reason_after","INDEPENDENT_WORLD_CONTACT",RA),
 flag(Lines,"veto_before",VB), flag(Lines,"veto_after",VA),
 flag(Lines,"reopen",Reopen),
 field(Lines,"scope_before","LOCAL",SB), field(Lines,"scope_after","LOCAL",SA),
 field(Lines,"horizon_before","MEDIUM",HB), field(Lines,"horizon_after","MEDIUM",HA),
 flag(Lines,"cycle_before",CB), flag(Lines,"cycle_after",CA),
 flag(Lines,"lost_option",Lost), flag(Lines,"irreversible_debt",Debt),
 flag(Lines,"provenance_changed",Prov), flag(Lines,"material_history",MF),
 flag(Lines,"chronology_only",Chron), flag(Lines,"event_order_sensitive",Order),
 field(Lines,"same_ancestry","YES",Anc),
 material(MF,Lost,Debt,Prov,Mat),
 transition(Chron,Mat,RB,RA,VB,VA,Reopen,SB,SA,HB,HA,CB,CA,Old,New,T),
 exact(Old,New,SB,SA,HB,HA,RB,RA,VB,VA,CB,CA,Lost,Debt,Prov,E),
 out(T,Old,New,Mat,Order,Lost,Debt,Prov,RB,RA,VB,VA,Reopen,E,Anc).

field(Lines,K,D,V) :-
 atom_string(KA,K),
 (member(Line,Lines), split_string(Line," "," ",[K,V0]), V0 \= "" -> atom_string(VA,V0), atom_string(KA,K), V=VA ; V=D).

flag(Lines,K,true) :- field(Lines,K,'NO',V), memberchk(V,['YES','ACTIVE','PASS']), !.
flag(_,_,false).

material(true,_,_,_,true) :- !.
material(_,true,_,_,true) :- !.
material(_,_,true,_,true) :- !.
material(_,_,_,true,true) :- !.
material(_,_,_,_,false).

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
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,O,N,'RELATION_REVISED') :- O \= N, !.
transition(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,'STABLE').

exact(O,O,S,S,H,H,R,R,V,V,C,C,false,false,false,true) :- !.
exact(_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,false).

word(true,'YES'). word(false,'NO').

out(T,O,N,Mat,Order,Lost,Debt,Prov,RB,RA,VB,VA,Reopen,E,Anc) :-
 word(Mat,MW), ((Mat=true ; Order=true) -> P=true ; P=false), word(P,PW),
 (Order=true -> C='NO' ; C='YES'),
 ((Lost=true ; Debt=true ; Prov=true) -> H='ACTIVE' ; H='INACTIVE'),
 ((Lost=true ; Debt=true) -> L='ACTIVE' ; L='INACTIVE'),
 (RB=RA -> M='NONE' ; atomic_list_concat([RB,'TO',RA],'_',M)),
 (VB=false,VA=true -> VT='ACTIVATED' ; VB=true,VA=false -> VT='RETIRED' ; VT='STABLE'),
 word(Reopen,RW), word(E,EW),
 (RB\=RA,Anc='YES' -> I='NO' ; I='NOT_INFERRED'),
 format("promotion.transition=~w~n",[T]),
 format("promotion.old_relation=~w~n",[O]),
 format("promotion.new_relation=~w~n",[N]),
 format("promotion.history_material=~w~n",[MW]),
 format("promotion.path_sensitive=~w~n",[PW]),
 format("promotion.revision_commutative=~w~n",[C]),
 format("promotion.hysteresis=~w~n",[H]),
 format("promotion.lost_option_debt=~w~n",[L]),
 format("promotion.reason_mutation=~w~n",[M]),
 format("promotion.veto_transition=~w~n",[VT]),
 format("promotion.reopen=~w~n",[RW]),
 format("promotion.exact_restoration=~w~n",[EW]),
 format("promotion.independent_warrant_created=~w~n",[I]),
 writeln("promotion.history_scalarization=OFF"),
 writeln("promotion.universal_historical_meta_utility=NOT_EARNED"),
 writeln("promotion.prtr=CANDIDATE"),
 writeln("promotion.phl=CANDIDATE"),
 writeln("promotion.odr=CANDIDATE"),
 writeln("promotion.rmr=CANDIDATE").
