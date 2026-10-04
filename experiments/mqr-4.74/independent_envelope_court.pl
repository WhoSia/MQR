:- use_module(library(readutil)).

yn("YES",true). yn("NO",false).

verdict([Id,Domain,_Current,_Generator,Coherent,Relevant,Independent,Realizability,Permission,Scope,Action,_Expected],V):-
  yn(Coherent,C),yn(Relevant,R),yn(Independent,I),yn(Scope,S),
  ( Action="ADMIT_NEW_FAILURE" ->
      (C=true,R=true,I=true,S=true -> V="REOPEN_SUCCESSOR_AUTHORITY"; V="HOLD_UNEARNED")
  ; Action="ADMIT_SCIENTIFIC_DEBT" ->
      (C=true,R=true,I=true,S=true,Realizability="CURRENTLY_UNREALIZABLE",Permission="BLOCKED" -> V="KEEP_EXECUTION_HOLD"; V="HOLD_UNEARNED")
  ; Action="REJECT_INCOHERENT" -> (C=false -> V="KEEP_CERTIFICATE"; V="HOLD_UNEARNED")
  ; Action="REJECT_IRRELEVANT" -> (R=false -> V="KEEP_CERTIFICATE"; V="HOLD_UNEARNED")
  ; Action="HOLD_POSTOUTCOME" -> (I=false -> V="NO_RETROACTIVE_USE"; V="HOLD_UNEARNED")
  ; Action="HOLD_SCOPE_DRIFT" ->
      (S=false -> (Domain="MATH" -> V="SEMANTIC_TRANSPORT_REQUIRED"; V="TRANSPORT_REQUIRED"); V="HOLD_UNEARNED")
  ; Action="SPLIT_PARENT" -> V="SPLIT_RECEIPT_REQUIRED"
  ; Action="MERGE_CHILDREN" -> V="MERGE_LOSS_AUDIT_REQUIRED"
  ; Action="HOLD_UNEARNED" -> V="KEEP_CERTIFICATE"
  ; Action="NO_NEW_FAILURE" -> V="KEEP_SCOPED_HISTORICAL_CERTIFICATE"
  ; V="HOLD_UNEARNED"
  ),
  Id=Id.

check([],0,0,[]).
check([R|Rs],N,B,[Id-V|Pairs]):-
  R=[Id|_], last(R,Expected), verdict(R,V),
  check(Rs,N0,B0,Pairs), N is N0+1, (V=Expected -> B=B0 ; B is B0+1).

lookup(Id,Pairs,V):-member(Id-V,Pairs).

run(File):-
  read_file_to_string(File,S,[]),
  split_string(S,"\n","\r",Ls0), exclude(=(""),Ls0,[_Header|Lines]),
  findall(Cols,(member(L,Lines),split_string(L,"\t","",Cols)),Rows),
  check(Rows,N,B,Pairs),
  lookup("E1",Pairs,U), lookup("E3",Pairs,O), lookup("E2",Pairs,X),
  lookup("E6",Pairs,P), lookup("M2",Pairs,M), lookup("H1",Pairs,H),
  ( N=15, B=0,
    U="REOPEN_SUCCESSOR_AUTHORITY",
    O="KEEP_CERTIFICATE",
    X="KEEP_EXECUTION_HOLD",
    P="NO_RETROACTIVE_USE",
    M="SEMANTIC_TRANSPORT_REQUIRED",
    H="KEEP_SCOPED_HISTORICAL_CERTIFICATE"
    -> OK="PASS"; OK="FAIL"),
  format("MQR474_PROLOG_ENVELOPE_COURT=~w~n",[OK]),
  format("MQR474_PROLOG_CASES=~w~n",[N]),
  (U="REOPEN_SUCCESSOR_AUTHORITY"->UY="YES";UY="NO"),
  format("MQR474_PROLOG_UNDERINCLUSION_REOPENS=~w~n",[UY]),
  (OK="PASS"->true;halt(1)).

:- initialization(main,main).
main(Argv):- (Argv=[F|_]->run(F);halt(2)).
