:- dynamic seen_header/0, seen_end/0, rid/1, scope/1, scope_timing/1,
  scope_nonvacuous/1, challenge/1, world_contact/1, decision_contract/1,
  action_invariant/1, decision_contract_change/1, stability_rounds/1,
  refinement/3, criterion/3, criterion_verdict/3, debt/3, path_state/2,
  new_contact/2, new_criterion/2.

reset_all :-
  retractall(seen_header), retractall(seen_end), retractall(rid(_)), retractall(scope(_)),
  retractall(scope_timing(_)), retractall(scope_nonvacuous(_)), retractall(challenge(_)),
  retractall(world_contact(_)), retractall(decision_contract(_)), retractall(action_invariant(_)),
  retractall(decision_contract_change(_)), retractall(stability_rounds(_)),
  retractall(refinement(_,_,_)), retractall(criterion(_,_,_)), retractall(criterion_verdict(_,_,_)),
  retractall(debt(_,_,_)), retractall(path_state(_,_)), retractall(new_contact(_,_)),
  retractall(new_criterion(_,_)).

run(File) :-
  reset_all,
  setup_call_cleanup(open(File,read,S), read_string(S,_,Text), close(S)),
  split_string(Text,"\n","\r",Lines),
  maplist(parse_line,Lines),
  validate,
  emit.

parse_line(Line) :-
  normalize_space(string(N),Line),
  ( N="" -> true
  ; sub_string(N,0,1,_,"#") -> true
  ; seen_end -> fail
  ; split_string(N," \t"," \t",T),
    ( \+ seen_header ->
        (T=["REALREGRESS","0.17"] -> assertz(seen_header) ; fail)
    ; parse_tokens(T)
    )
  ).

parse_tokens(["END"]) :- assertz(seen_end), !.
parse_tokens(["id",X]) :- \+ rid(_), assertz(rid(X)), !.
parse_tokens(["claim_scope",X]) :- \+ scope(_), assertz(scope(X)), !.
parse_tokens(["scope_timing",X]) :- \+ scope_timing(_), member(X,["FROZEN","PROSPECTIVE_REVISION","POST_OUTCOME_REVISION"]), assertz(scope_timing(X)), !.
parse_tokens(["scope_nonvacuous",X]) :- \+ scope_nonvacuous(_), yn(X), assertz(scope_nonvacuous(X)), !.
parse_tokens(["challenge",X]) :- assertz(challenge(X)), !.
parse_tokens(["world_contact",X]) :- assertz(world_contact(X)), !.
parse_tokens(["decision_contract",X]) :- \+ decision_contract(_), assertz(decision_contract(X)), !.
parse_tokens(["action_invariant",X]) :- \+ action_invariant(_), yn(X), assertz(action_invariant(X)), !.
parse_tokens(["decision_contract_change",X]) :- yn(X), retractall(decision_contract_change(_)), assertz(decision_contract_change(X)), !.
parse_tokens(["stability_rounds",X]) :- number_string(_,X), retractall(stability_rounds(_)), assertz(stability_rounds(X)), !.
parse_tokens(["refinement",I,S,E]) :-
  \+ refinement(I,_,_), member(S,["REPLAYED","DEFERRED","UNEXECUTED"]),
  member(E,["INERT","CHANGES_DEFEAT","CHANGES_DISCRIMINATION","CHANGES_DECISION","UNKNOWN"]),
  assertz(refinement(I,S,E)), !.
parse_tokens(["criterion",I,T,A]) :-
  \+ criterion(I,_,_), member(T,["PROSPECTIVE","INHERITED","POST_OUTCOME"]),
  member(A,["INDEPENDENT","DEPENDENT","CYCLIC"]), assertz(criterion(I,T,A)), !.
parse_tokens(["criterion_verdict",C,R,V]) :-
  member(V,["INERT","MATERIAL","UNKNOWN"]), \+ criterion_verdict(C,R,_),
  assertz(criterion_verdict(C,R,V)), !.
parse_tokens(["debt",I,M,S]) :-
  member(M,["MATERIAL","NONMATERIAL","UNKNOWN"]), member(S,["LIVE","RESOLVED"]),
  assertz(debt(I,M,S)), !.
parse_tokens(["path",I,S]) :- member(S,["PASS","HOLD","REOPEN"]), assertz(path_state(I,S)), !.
parse_tokens(["new_contact",I,S]) :- member(S,["INERT","DISTINGUISHES"]), assertz(new_contact(I,S)), !.
parse_tokens(["new_criterion",I,S]) :- member(S,["AGREES","BREAKS"]), assertz(new_criterion(I,S)), !.
parse_tokens(_) :- fail.

yn("YES"). yn("NO").

validate :-
  seen_header, seen_end, rid(_), scope(_), scope_timing(_), scope_nonvacuous(_),
  decision_contract(_), action_invariant(_),
  forall(criterion_verdict(C,R,_),(criterion(C,_,_),refinement(R,_,_))).

count(P,N) :- findall(X,call(P,X),Xs),length(Xs,N).

vacuous :-
  scope_nonvacuous("NO"), !.
vacuous :- \+ challenge(_), !.
vacuous :- \+ world_contact(_), !.
vacuous :- \+ refinement(_,_,_), !.
vacuous :- \+ criterion(_,_,_), !.

scope_capture :- scope_timing("POST_OUTCOME_REVISION").
criterion_capture :- criterion(_,"POST_OUTCOME",_).
meta_cycle :- criterion(_,_, "CYCLIC").
live_debt :- debt(_,M,"LIVE"), M \= "NONMATERIAL", !.
live_debt :- refinement(_,S,_), S \= "REPLAYED", !.
material_refinement :- refinement(_,"REPLAYED",E), E \= "INERT".
path_conflict :- path_state(_,S), S \= "PASS".
new_contact_break :- new_contact(_,"DISTINGUISHES").
criterion_break :- new_criterion(_,"BREAKS").
decision_changed :- decision_contract_change("YES").

criterion_stop_support :-
  criterion(_,_,_), refinement(_,_,_),
  forall((criterion(C,_,_),refinement(R,_,_)),criterion_verdict(C,R,"INERT")).

criterion_noninvariance :-
  criterion(C,_,_), refinement(R,_,_), \+ criterion_verdict(C,R,_), !.
criterion_noninvariance :-
  criterion_verdict(_,_, "UNKNOWN"), !.
criterion_noninvariance :-
  criterion_verdict(C1,R,V1), criterion_verdict(C2,R,V2), C1 \= C2, V1 \= V2, !.

base_stop :-
  \+ vacuous, \+ scope_capture, \+ criterion_capture, \+ meta_cycle,
  \+ live_debt, \+ material_refinement, \+ criterion_noninvariance,
  criterion_stop_support, \+ path_conflict, \+ new_contact_break,
  \+ criterion_break, \+ decision_changed.

authority("REOPEN_NEW_WORLD_CONTACT") :- new_contact_break, !.
authority("REOPEN_CRITERION_ENVELOPE") :- criterion_break, !.
authority("REOPEN_DECISION_CONTRACT_CHANGE") :- decision_changed, !.
authority("REOPEN_REGRESS_PATH_CONFLICT") :- path_conflict, !.
authority("HOLD_SCOPE_CAPTURE") :- scope_capture, !.
authority("HOLD_META_CRITERION_CAPTURE") :- criterion_capture, !.
authority("HOLD_META_CYCLE") :- meta_cycle, !.
authority("HOLD_VACUOUS_TERMINATION") :- vacuous, !.
authority("HOLD_LIVE_REFINEMENT_DEBT") :- live_debt, !.
authority("HOLD_META_CRITERION_NONINVARIANCE") :- criterion_noninvariance, !.
authority("HOLD_PREMATURE_TERMINATION") :- material_refinement, !.
authority("AUTHORIZED_CRITERION_ROBUST_OPERATIONAL_STOP") :- base_stop, !.
authority("HOLD_PREMATURE_TERMINATION").

action_authority("REOPEN_DECISION_CONTRACT_CHANGE") :- decision_changed, !.
action_authority("AUTHORIZED_ACTION_UNDER_DECLARED_CONTRACT") :-
  decision_contract(D), D \= "NONE", action_invariant("YES"), base_stop, !.
action_authority("NOT_AUTHORIZED").

bool(P,"YES") :- call(P), !.
bool(_,"NO").

emit :-
  count(challenge,NC), count(world_contact,NW),
  findall(I,refinement(I,_,_),Rs),length(Rs,NR),
  findall(I,criterion(I,_,_),Cs),length(Cs,NK),
  bool(live_debt,LD), bool(material_refinement,MR), bool(scope_capture,SC),
  bool(criterion_capture,CC), bool(meta_cycle,MC), bool(criterion_noninvariance,CN),
  bool(criterion_stop_support,CS), bool(path_conflict,PC), bool(new_contact_break,NB),
  bool(criterion_break,CB), bool(decision_changed,DC), bool(base_stop,BS),
  action_authority(AA), authority(A),
  (stability_rounds(SR)->true;SR="0"),
  format("regress.challenge_count=~w~n",[NC]),
  format("regress.world_contact_count=~w~n",[NW]),
  format("regress.refinement_count=~w~n",[NR]),
  format("regress.criterion_count=~w~n",[NK]),
  format("regress.live_material_debt=~w~n",[LD]),
  format("regress.material_refinement=~w~n",[MR]),
  format("regress.scope_capture=~w~n",[SC]),
  format("regress.criterion_capture=~w~n",[CC]),
  format("regress.meta_cycle=~w~n",[MC]),
  format("regress.criterion_noninvariance=~w~n",[CN]),
  format("regress.criterion_stop_support=~w~n",[CS]),
  format("regress.path_conflict=~w~n",[PC]),
  format("regress.new_world_contact_break=~w~n",[NB]),
  format("regress.criterion_envelope_break=~w~n",[CB]),
  format("regress.decision_contract_change=~w~n",[DC]),
  format("regress.operational_stop_authorized=~w~n",[BS]),
  format("regress.action_authority=~w~n",[AA]),
  format("regress.authority_state=~w~n",[A]),
  format("regress.stability_rounds=~w~n",[SR]),
  writeln("regress.metaphysical_termination=NO"),
  writeln("regress.final_ontology_inferred=NO"),
  writeln("regress.future_refinement_space_closed=NO"),
  writeln("regress.stop_rule_truth_oracle=NO"),
  writeln("regress.claim_scope_truth_oracle=NO"),
  writeln("regress.meta_criterion_truth_oracle=NO"),
  writeln("regress.operational_stop_permanent=NO"),
  writeln("regress.reopening_reserve=ACTIVE"),
  writeln("regress.guidance_mode=REOPENABLE_OPERATIONAL_FIXED_POINT").
