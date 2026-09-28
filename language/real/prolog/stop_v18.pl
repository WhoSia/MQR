:- dynamic seen_header/0, seen_end/0, rid/1, upstream/1, oqsc/1,
  live_debt/1, criterion_invariant/1, break_kind/1,
  confirmation_required/1, eligible_streak/1.

reset_all :-
  retractall(seen_header), retractall(seen_end), retractall(rid(_)),
  retractall(upstream(_)), retractall(oqsc(_)), retractall(live_debt(_)),
  retractall(criterion_invariant(_)), retractall(break_kind(_)),
  retractall(confirmation_required(_)), retractall(eligible_streak(_)).

run(File) :-
  reset_all,
  setup_call_cleanup(open(File, read, S), read_string(S, _, Text), close(S)),
  split_string(Text, "\n", "\r", Lines),
  maplist(parse_line, Lines),
  validate,
  emit.

parse_line(Line) :-
  normalize_space(string(N), Line),
  ( N = "" -> true
  ; sub_string(N, 0, 1, _, "#") -> true
  ; seen_end -> fail
  ; split_string(N, " \t", " \t", T),
    ( \+ seen_header ->
        (T = ["REALSTOP", "0.18"] -> assertz(seen_header) ; fail)
    ; parse_tokens(T)
    )
  ).

parse_tokens(["END"]) :- assertz(seen_end), !.
parse_tokens(["id", X]) :- \+ rid(_), assertz(rid(X)), !.
parse_tokens(["upstream", X]) :-
  \+ upstream(_), member(X, ["PASS","HOLD","REOPEN"]),
  assertz(upstream(X)), !.
parse_tokens(["oqsc", X]) :- \+ oqsc(_), yn(X), assertz(oqsc(X)), !.
parse_tokens(["live_debt", X]) :-
  \+ live_debt(_), yn(X), assertz(live_debt(X)), !.
parse_tokens(["criterion_invariant", X]) :-
  \+ criterion_invariant(_), yn(X), assertz(criterion_invariant(X)), !.
parse_tokens(["break", X]) :-
  \+ break_kind(_),
  member(X, ["NONE","WORLD_CONTACT","DECISION_CONTRACT","PATH_CONFLICT"]),
  assertz(break_kind(X)), !.
parse_tokens(["confirmation_required", X]) :-
  \+ confirmation_required(_), number_string(N, X), integer(N), N >= 0, N =< 3,
  assertz(confirmation_required(N)), !.
parse_tokens(["eligible_streak", X]) :-
  \+ eligible_streak(_), number_string(N, X), integer(N), N >= 0,
  assertz(eligible_streak(N)), !.
parse_tokens(_) :- fail.

yn("YES"). yn("NO").

validate :-
  seen_header, seen_end, rid(_), upstream(_), oqsc(_), live_debt(_),
  criterion_invariant(_), break_kind(_), confirmation_required(_),
  eligible_streak(_).

eligible :-
  upstream("PASS"), oqsc("YES"), live_debt("NO"),
  criterion_invariant("YES"), break_kind("NONE").

action("REOPEN") :-
  ( upstream("REOPEN") ; break_kind(B), B \= "NONE" ), !.
action("STOP") :-
  eligible,
  confirmation_required(L),
  eligible_streak(S),
  S >= L + 1, !.
action("CONTINUE").

bool(P, "YES") :- call(P), !.
bool(_, "NO").

emit :-
  bool(eligible, E),
  confirmation_required(L),
  eligible_streak(S),
  action(A),
  format("stop.eligible=~w~n", [E]),
  format("stop.confirmation_required=~w~n", [L]),
  format("stop.eligible_streak=~w~n", [S]),
  format("stop.action=~w~n", [A]),
  writeln("stop.hidden_gold_access=NO"),
  writeln("stop.future_oracle=NO"),
  writeln("stop.post_holdout_policy_repair=FORBIDDEN"),
  writeln("stop.primary_scalar_score=OFF"),
  writeln("stop.external_calibration=HOLD"),
  writeln("stop.universal_optimality=FORBIDDEN"),
  writeln("stop.guidance_mode=CALIBRATED_REOPENABLE_STOP").
