:- dynamic seen_header/0,seen_end/0,rid/1,source_cutoff/1,mapping/1,claim/1,
 probe/1,use_mode/1,live_obligation/1,criterion/1,break_kind/1,projection/1,
 granularity/1,stop_window/1,historical_action/1.

reset_all:-
 retractall(seen_header),retractall(seen_end),retractall(rid(_)),
 retractall(source_cutoff(_)),retractall(mapping(_)),retractall(claim(_)),
 retractall(probe(_)),retractall(use_mode(_)),retractall(live_obligation(_)),
 retractall(criterion(_)),retractall(break_kind(_)),retractall(projection(_)),
 retractall(granularity(_)),retractall(stop_window(_)),retractall(historical_action(_)).

run(File):-reset_all,setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),maplist(parse_line,Lines),validate,emit.

parse_line(Line):-normalize_space(string(N),Line),
 (N=""->true;sub_string(N,0,1,_,"#")->true;seen_end->fail;
  split_string(N," \t"," \t",T),
  (\+seen_header->(T=["REALTRACE","0.19"]->assertz(seen_header);fail);parse_tokens(T))).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["source_cutoff",X]):- \+ source_cutoff(_),assertz(source_cutoff(X)),!.
parse_tokens(["mapping",X]):- \+ mapping(_),member(X,["EXACT","BOUNDED","PROXY","UNKNOWN"]),assertz(mapping(X)),!.
parse_tokens(["claim",X]):- \+ claim(_),member(X,["OPEN","RESTRICTED","FROZEN"]),assertz(claim(X)),!.
parse_tokens(["probe",X]):- \+ probe(_),member(X,["ACTIVE","PAUSED","HANDOFF","ARCHIVED"]),assertz(probe(X)),!.
parse_tokens(["use",X]):- \+ use_mode(_),member(X,["NONE","PROVISIONAL","AUTHORIZED"]),assertz(use_mode(X)),!.
parse_tokens(["live_obligation",X]):- \+ live_obligation(_),member(X,["CLEAR","LIVE","BOUNDED","UNKNOWN"]),assertz(live_obligation(X)),!.
parse_tokens(["criterion",X]):- \+ criterion(_),member(X,["AGREE","DISAGREE","UNKNOWN"]),assertz(criterion(X)),!.
parse_tokens(["break",X]):- \+ break_kind(_),member(X,["NONE","WORLD_CONTACT","DECISION_CONTRACT","PATH_CONFLICT"]),assertz(break_kind(X)),!.
parse_tokens(["projection",X]):- \+ projection(_),member(X,["UNIQUE","MULTI_MODE","NONE"]),assertz(projection(X)),!.
parse_tokens(["granularity",X]):- \+ granularity(_),member(X,["REGULAR","IRREGULAR","UNKNOWN"]),assertz(granularity(X)),!.
parse_tokens(["stop_window",X]):- \+ stop_window(_),member(X,["IDENTIFIED","INTERVAL","LEFT_CENSORED","RIGHT_CENSORED","NONIDENTIFIABLE"]),assertz(stop_window(X)),!.
parse_tokens(["historical_action",X]):- \+ historical_action(_),member(X,["CONTINUE_PROBING","CLAIM_FREEZE","PROVISIONAL_USE","ARCHIVE","HANDOFF","REOPEN"]),assertz(historical_action(X)),!.
parse_tokens(_):-fail.

validate:-seen_header,seen_end,rid(_),source_cutoff(_),mapping(_),claim(_),probe(_),use_mode(_),
 live_obligation(_),criterion(_),break_kind(_),projection(_),granularity(_),stop_window(_),historical_action(_).

admission:-mapping(M),member(M,["EXACT","BOUNDED"]),live_obligation(L),L \= "UNKNOWN",criterion(C),C \= "UNKNOWN".
projection_loss:-projection(P),P \= "UNIQUE".
reopen_required:-break_kind(B),B \= "NONE".
point_window:-stop_window("IDENTIFIED").
yn(G,"YES"):-call(G),!. yn(_,"NO").

emit:-
 source_cutoff(S),mapping(M),claim(C),probe(P),use_mode(U),live_obligation(L),criterion(K),
 break_kind(B),projection(R),granularity(G),stop_window(W),historical_action(H),
 yn(admission,A),yn(projection_loss,PL),yn(reopen_required,RR),yn(point_window,PW),
 (G="IRREGULAR"->Lag="REJECT";Lag="NOT_ESTABLISHED"),
 format("trace.source_cutoff=~w~n",[S]),format("trace.mapping=~w~n",[M]),
 format("trace.claim_mode=~w~n",[C]),format("trace.probe_mode=~w~n",[P]),
 format("trace.use_mode=~w~n",[U]),format("trace.live_obligation=~w~n",[L]),
 format("trace.criterion=~w~n",[K]),format("trace.break=~w~n",[B]),
 format("trace.projection=~w~n",[R]),format("trace.granularity=~w~n",[G]),
 format("trace.stop_window=~w~n",[W]),format("trace.historical_action=~w~n",[H]),
 format("trace.naturalistic_admission=~w~n",[A]),
 format("trace.binary_projection_loss=~w~n",[PL]),
 format("trace.reopen_required=~w~n",[RR]),
 format("trace.fixed_event_lag_transport=~w~n",[Lag]),
 format("trace.point_window_identified=~w~n",[PW]),
 writeln("trace.unique_stop_time_inferred=NO"),
 writeln("trace.historical_action_truth_oracle=NO"),
 writeln("trace.naturalistic_retuning_lambda=NO"),
 writeln("trace.prospective_external_validation=NO"),
 writeln("trace.popperian_master_semantics=REJECT"),
 writeln("trace.world_contact_negative_only=NO"),
 writeln("trace.guidance_mode=MODE_RELATIVE_REOPENABLE_AUTHORITY").
