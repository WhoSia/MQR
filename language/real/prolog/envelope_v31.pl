:- use_module(library(readutil)).
:- use_module(library(lists)).

generator('THEORY'). generator('RIVAL'). generator('ANOMALY'). generator('INSTRUMENT').
generator('DOMAIN_GRAMMAR'). generator('EXTERNAL'). generator('COUNTERMODEL').
generator('FRAMEWORK_EXTENSION'). generator('PROOF_OBLIGATION'). generator('POSTOUTCOME'). generator('LABEL_ONLY').
realizability('AVAILABLE'). realizability('CURRENTLY_UNREALIZABLE'). realizability('IMPOSSIBLE_IN_PRINCIPLE'). realizability('NOT_APPLICABLE').
permission('PERMITTED'). permission('BLOCKED'). permission('NOT_APPLICABLE').
evidence('OBSERVED'). evidence('PROVED'). evidence('ENUMERATED'). evidence('SIMULATED'). evidence('INFERRED'). evidence('OPEN').
transition_kind('EXPAND'). transition_kind('SPLIT'). transition_kind('MERGE'). transition_kind('TRANSPORT').

die(M):- writeln(user_error,M),halt(2).
field(Lines,K,V):- member(L,Lines), split_string(L," "," ",[K,V]), !.
need(L,K,V):- (field(L,K,V)->true;format(string(M),"missing required field: ~w",[K]),die(M)).
explicit(V):- V\="", V\="OPEN".
yn("YES",true). yn("NO",false).

parse_pert(Line,p(Id,G,C,R,I,Real,Perm,S,A)):-
  split_string(Line," "," ",["perturbation",Id,G,C0,R0,I0,Real,Perm,S0,A]),
  generator(G), realizability(Real), permission(Perm),
  yn(C0,C),yn(R0,R),yn(I0,I),yn(S0,S).

parse_trans(Line,t(K,S,T,R)):-
  split_string(Line," "," ",["transition",K,S,T,R]),
  transition_kind(K), explicit(R).

has_transition(Ts,K):- member(t(K,_,_,_),Ts).

audit(Ps,Ts,Reopen,Debt,Rejected,Holds,Stable):-
  audit_(Ps,Ts,false,0,0,0,0,Reopen,Debt,Rejected,Holds,Stable).

audit_([],_,R,D,X,H,S,R,D,X,H,S).
audit_([p(Id,G,C,Rel,Ind,Real,Perm,Scope,A)|Rest],Ts,R0,D0,X0,H0,S0,R,D,X,H,S):-
  (
   A="ADMIT_NEW_FAILURE" ->
     (C=true,Rel=true,Ind=true,Scope=true,G\="POSTOUTCOME",Real\="IMPOSSIBLE_IN_PRINCIPLE" -> R1=true,D1=D0,X1=X0,H1=H0,S1=S0 ; format(string(M),"~w cannot be admitted as same-scope new failure",[Id]),die(M))
  ; A="ADMIT_SCIENTIFIC_DEBT" ->
     (C=true,Rel=true,Ind=true,Scope=true,Real="CURRENTLY_UNREALIZABLE",Perm="BLOCKED" -> R1=R0,D1 is D0+1,X1=X0,H1=H0,S1=S0 ; format(string(M),"~w invalid scientific debt",[Id]),die(M))
  ; A="REJECT_INCOHERENT" ->
     (C=false -> R1=R0,D1=D0,X1 is X0+1,H1=H0,S1=S0 ; format(string(M),"~w marked incoherent but coherence=YES",[Id]),die(M))
  ; A="REJECT_IRRELEVANT" ->
     (Rel=false, Perm\="BLOCKED" -> R1=R0,D1=D0,X1 is X0+1,H1=H0,S1=S0 ; format(string(M),"~w invalid irrelevant rejection",[Id]),die(M))
  ; A="HOLD_POSTOUTCOME" ->
     (G="POSTOUTCOME",Ind=false -> R1=R0,D1=D0,X1=X0,H1 is H0+1,S1=S0 ; format(string(M),"~w invalid post-outcome hold",[Id]),die(M))
  ; A="HOLD_SCOPE_DRIFT" ->
     (Scope=false -> R1=R0,D1=D0,X1=X0,H1 is H0+1,S1=S0 ; format(string(M),"~w scope drift requires scope_preserved=NO",[Id]),die(M))
  ; A="SPLIT_PARENT" ->
     (has_transition(Ts,"SPLIT") -> R1=R0,D1=D0,X1=X0,H1 is H0+1,S1=S0 ; format(string(M),"~w split requires SPLIT transition receipt",[Id]),die(M))
  ; A="MERGE_CHILDREN" ->
     (has_transition(Ts,"MERGE") -> R1=R0,D1=D0,X1=X0,H1 is H0+1,S1=S0 ; format(string(M),"~w merge requires MERGE transition receipt",[Id]),die(M))
  ; A="HOLD_UNEARNED" ->
     (Ind=false -> R1=R0,D1=D0,X1=X0,H1 is H0+1,S1=S0 ; format(string(M),"~w HOLD_UNEARNED expects independent=NO",[Id]),die(M))
  ; A="NO_NEW_FAILURE" ->
     R1=R0,D1=D0,X1=X0,H1=H0,S1 is S0+1
  ; format(string(M),"invalid action for ~w",[Id]),die(M)
  ),
  audit_(Rest,Ts,R1,D1,X1,H1,S1,R,D,X,H,S).

emit_trans([], _).
emit_trans([t(K,S,T,R)|Xs],I):- format("envelope.transition.~w=~w:~w->~w:~w~n",[I,K,S,T,R]), J is I+1, emit_trans(Xs,J).
emit_ps([], _).
emit_ps([p(Id,G,C,R,I,Real,Perm,S,A)|Xs],N):-
  (C=true->CS="YES";CS="NO"),(R=true->RS="YES";RS="NO"),(I=true->IS="YES";IS="NO"),(S=true->SS="YES";SS="NO"),
  format("envelope.perturbation.~w=~w:~w:~w:~w:~w:~w:~w:~w:~w~n",[N,Id,G,CS,RS,IS,Real,Perm,SS,A]),
  M is N+1, emit_ps(Xs,M).

run(File):-
  read_file_to_string(File,Src,[]), split_string(Src,"\n","\r",Raw),
  exclude(=(""),Raw,Lines),
  (member("REALENVELOPE 0.31-CANDIDATE",Lines)->true;die("expected REALENVELOPE 0.31-CANDIDATE")),
  (member("END",Lines)->true;die("missing END")),
  need(Lines,"sealed",Seal),(Seal="PASS"->true;die("sealed must be PASS")),
  forall(member(K,["claim_scope_hash","obligation_family_hash","envelope_id","envelope_version","admissibility_rule_hash","revision_rule_hash"]),
    (need(Lines,K,V),(explicit(V)->true;format(string(M),"~w must be explicit",[K]),die(M)))),
  need(Lines,"evidence_kind",E),(evidence(E)->true;die("invalid evidence_kind")),
  need(Lines,"completeness_claim",CC),(CC="RELATIVE_ONLY"->true;die("completeness_claim must be RELATIVE_ONLY")),
  need(Lines,"open_world_complete",OW),(OW="OFF"->true;die("open_world_complete must be OFF")),
  findall(P,(member(L,Lines),sub_string(L,0,13,_,"perturbation "),parse_pert(L,P)),Ps),
  findall(T,(member(L,Lines),sub_string(L,0,11,_,"transition "),parse_trans(L,T)),Ts),
  audit(Ps,Ts,Reopen,Debt,Rejected,Holds,Stable),
  need(Lines,"envelope_id",Env),need(Lines,"envelope_version",Ver),need(Lines,"claim_scope_hash",CSH),need(Lines,"obligation_family_hash",OFH),
  format("envelope.id=~w~n",[Env]),format("envelope.version=~w~n",[Ver]),
  format("envelope.claim_scope_hash=~w~n",[CSH]),format("envelope.obligation_family_hash=~w~n",[OFH]),
  length(Ps,NP),length(Ts,NT),format("envelope.perturbation_count=~w~n",[NP]),format("envelope.transition_count=~w~n",[NT]),
  format("envelope.scientific_debt_count=~w~n",[Debt]),format("envelope.rejected_count=~w~n",[Rejected]),
  format("envelope.hold_count=~w~n",[Holds]),format("envelope.stable_control_count=~w~n",[Stable]),
  (Reopen=true->RA="REOPEN";RA="UNCHANGED_AT_DECLARED_ENVELOPE"),
  format("envelope.successor_authority=~w~n",[RA]),
  writeln("envelope.prior_scoped_certificate=HISTORICALLY_VALID_AT_PRIOR_DECLARED_ENVELOPE"),
  writeln("envelope.completeness_claim=RELATIVE_ONLY"),writeln("envelope.open_world_complete=OFF"),
  writeln("envelope.size_is_authority=NO"),writeln("envelope.stress_extremity_is_relevance=NO"),
  writeln("envelope.later_defeat_implies_retroactive_falsehood=NO"),
  format("envelope.evidence_kind=~w~n",[E]),writeln("envelope.status=CANDIDATE_UNPROMOTED"),
  emit_trans(Ts,0),emit_ps(Ps,0).

:- initialization(main,main).
main(Argv):- (Argv=[File|_]->run(File);die("usage: envelope_v31.pl <packet>")).
