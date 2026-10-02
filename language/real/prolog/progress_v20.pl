:- dynamic seen_header/0,seen_end/0,rid/1,chart/1,inert_checkpoint/1,
 evidence_batching/1,parameter_recode/1,obligation_partition/1,path_loop/1,
 path_order/1,local_structure/1,magnitude_transport/1,continuation_value/1,reopening/1.

reset_all:-
 retractall(seen_header),retractall(seen_end),retractall(rid(_)),retractall(chart(_)),
 retractall(inert_checkpoint(_)),retractall(evidence_batching(_)),retractall(parameter_recode(_)),
 retractall(obligation_partition(_)),retractall(path_loop(_)),retractall(path_order(_)),
 retractall(local_structure(_)),retractall(magnitude_transport(_)),
 retractall(continuation_value(_)),retractall(reopening(_)).

run(File):-reset_all,setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),maplist(parse_line,Lines),validate,emit.

parse_line(Line):-normalize_space(string(N),Line),
 (N=""->true;sub_string(N,0,1,_,"#")->true;seen_end->fail;
  split_string(N," \t"," \t",T),
  (\+ seen_header->(T=["REALPROGRESS","0.20"]->assertz(seen_header);fail);parse_tokens(T))).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["chart",X]):- \+ chart(_),member(X,["STATISTICAL","EXPERIMENT","OBLIGATION","CAUSAL","MODE","OTHER"]),assertz(chart(X)),!.
parse_tokens(["inert_checkpoint",X]):- \+ inert_checkpoint(_),member(X,["QUOTIENT","MATERIAL"]),assertz(inert_checkpoint(X)),!.
parse_tokens(["evidence_batching",X]):- \+ evidence_batching(_),member(X,["QUOTIENT","MATERIAL"]),assertz(evidence_batching(X)),!.
parse_tokens(["parameter_recode",X]):- \+ parameter_recode(_),member(X,["QUOTIENT","MATERIAL"]),assertz(parameter_recode(X)),!.
parse_tokens(["obligation_partition",X]):- \+ obligation_partition(_),member(X,["QUOTIENT","MATERIAL"]),assertz(obligation_partition(X)),!.
parse_tokens(["path_loop",X]):- \+ path_loop(_),member(X,["QUOTIENT","MATERIAL"]),assertz(path_loop(X)),!.
parse_tokens(["path_order",X]):- \+ path_order(_),member(X,["COMMUTATIVE","NONCOMMUTATIVE","UNKNOWN"]),assertz(path_order(X)),!.
parse_tokens(["local_structure",X]):- \+ local_structure(_),member(X,["METRIC","PARTIAL_ORDER","PREORDER","ADMISSIBLE_REGION","NONE"]),assertz(local_structure(X)),!.
parse_tokens(["magnitude_transport",X]):- \+ magnitude_transport(_),member(X,["LICENSED","UNLICENSED"]),assertz(magnitude_transport(X)),!.
parse_tokens(["continuation_value",X]):- \+ continuation_value(_),member(X,["SEPARATE","COLLAPSED"]),assertz(continuation_value(X)),!.
parse_tokens(["reopening",X]):- \+ reopening(_),member(X,["ACTIVE","INACTIVE"]),assertz(reopening(X)),!.
parse_tokens(_):-fail.

validate:-seen_header,seen_end,rid(_),chart(_),inert_checkpoint(_),evidence_batching(_),
 parameter_recode(_),obligation_partition(_),path_loop(_),path_order(_),local_structure(_),
 magnitude_transport(_),continuation_value(_),reopening(_).

quotient_complete:-inert_checkpoint("QUOTIENT"),evidence_batching("QUOTIENT"),
 parameter_recode("QUOTIENT"),obligation_partition("QUOTIENT"),path_loop("QUOTIENT").
noncommuting_preserved:-path_order(P),P\="UNKNOWN".
local_geometry:-local_structure(S),S\="NONE".
atlas_admissible:-quotient_complete,noncommuting_preserved,local_geometry,
 continuation_value("SEPARATE"),reopening("ACTIVE").
yn(G,"YES"):-call(G),!. yn(_,"NO").

emit:-chart(C),inert_checkpoint(I),evidence_batching(E),parameter_recode(P),
 obligation_partition(O),path_loop(L),path_order(PO),local_structure(S),
 magnitude_transport(M),continuation_value(V),reopening(R),
 yn(quotient_complete,QC),yn(noncommuting_preserved,NP),yn(local_geometry,LG),yn(atlas_admissible,AA),
 (M="LICENSED"->MD="LICENSED_LOCAL";MD="NO"),
 (V="SEPARATE"->SS="REJECT";SS="INVALID_COLLAPSE"),
 format("progress.chart=~w~n",[C]),format("progress.inert_checkpoint=~w~n",[I]),
 format("progress.evidence_batching=~w~n",[E]),format("progress.parameter_recode=~w~n",[P]),
 format("progress.obligation_partition=~w~n",[O]),format("progress.path_loop=~w~n",[L]),
 format("progress.path_order=~w~n",[PO]),format("progress.local_structure=~w~n",[S]),
 format("progress.magnitude_transport=~w~n",[M]),format("progress.continuation_value=~w~n",[V]),
 format("progress.reopening=~w~n",[R]),format("progress.inert_quotient_complete=~w~n",[QC]),
 format("progress.noncommuting_path_preserved=~w~n",[NP]),
 format("progress.local_geometry_admitted=~w~n",[LG]),format("progress.atlas_admissible=~w~n",[AA]),
 writeln("progress.global_scalar=REJECT"),format("progress.cross_domain_magnitude_default=~w~n",[MD]),
 writeln("progress.progress_equals_promotion=NO"),format("progress.scalar_threshold_stop=~w~n",[SS]),
 writeln("progress.truth_distance_inferred=NO"),writeln("progress.final_geometry_complete=NO"),
 writeln("progress.guidance_mode=GLOBAL_META_LOCAL_GEOMETRY").
