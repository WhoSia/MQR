:- use_module(library(readutil)).
yn("YES",true). yn("NO",false).
verdict(R,V):-
  get_dict(coherent,R,C0),yn(C0,C),get_dict(claim_relevant,R,R0),yn(R0,Rel),
  get_dict(independent_motivation,R,I0),yn(I0,Ind),get_dict(scope_preserved,R,S0),yn(S0,Scope),
  get_dict(action,R,A),
  ( A="ADMIT_NEW_FAILURE" -> (C=true,Rel=true,Ind=true,Scope=true->V="REOPEN_SUCCESSOR_AUTHORITY";V="HOLD_UNEARNED")
  ; A="ADMIT_SCIENTIFIC_DEBT" -> get_dict(realizability,R,Real),get_dict(execution_permission,R,Perm),
      (C=true,Rel=true,Ind=true,Scope=true,Real="CURRENTLY_UNREALIZABLE",Perm="BLOCKED"->V="KEEP_EXECUTION_HOLD";V="HOLD_UNEARNED")
  ; A="REJECT_INCOHERENT" -> (C=false->V="KEEP_CERTIFICATE";V="HOLD_UNEARNED")
  ; A="REJECT_IRRELEVANT" -> (Rel=false->V="KEEP_CERTIFICATE";V="HOLD_UNEARNED")
  ; A="HOLD_POSTOUTCOME" -> (Ind=false->V="NO_RETROACTIVE_USE";V="HOLD_UNEARNED")
  ; A="HOLD_SCOPE_DRIFT" -> get_dict(domain,R,D),(Scope=false->(D="MATH"->V="SEMANTIC_TRANSPORT_REQUIRED";V="TRANSPORT_REQUIRED");V="HOLD_UNEARNED")
  ; A="SPLIT_PARENT" -> V="SPLIT_RECEIPT_REQUIRED"
  ; A="MERGE_CHILDREN" -> V="MERGE_LOSS_AUDIT_REQUIRED"
  ; A="HOLD_UNEARNED" -> V="KEEP_CERTIFICATE"
  ; A="NO_NEW_FAILURE" -> V="KEEP_SCOPED_HISTORICAL_CERTIFICATE"
  ; V="HOLD_UNEARNED"
  ).

row_dict(H,V,D):- pairs_keys_values(P,H,V),dict_pairs(D,row,P).
check_rows([],0,0,[]).
check_rows([D|Ds],N,B,[Id-V|Rest]):-
  verdict(D,V),get_dict(expected,D,E),get_dict(case_id,D,Id),
  check_rows(Ds,N0,B0,Rest),N is N0+1,(V=E->B=B0;B is B0+1).

lookup(Id,Pairs,V):-member(Id-V,Pairs).

run(File):-
  read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls0),exclude(=(""),Ls0,[Head|Lines]),
  split_string(Head,"\t","",H),findall(D,(member(L,Lines),split_string(L,"\t","",V),row_dict(H,V,D)),Rows),
  check_rows(Rows,N,B,Pairs),
  lookup("E1",Pairs,U),lookup("E3",Pairs,O),lookup("E2",Pairs,X),lookup("E6",Pairs,P),lookup("M2",Pairs,M),lookup("H1",Pairs,Hs),
  (N=15,B=0,U="REOPEN_SUCCESSOR_AUTHORITY",O="KEEP_CERTIFICATE",X="KEEP_EXECUTION_HOLD",P="NO_RETROACTIVE_USE",M="SEMANTIC_TRANSPORT_REQUIRED",Hs="KEEP_SCOPED_HISTORICAL_CERTIFICATE"->OK="PASS";OK="FAIL"),
  format("MQR474_PROLOG_ENVELOPE_COURT=~w~n",[OK]),format("MQR474_PROLOG_CASES=~w~n",[N]),
  format("MQR474_PROLOG_UNDERINCLUSION_REOPENS=~w~n",[(U="REOPEN_SUCCESSOR_AUTHORITY"->"YES";"NO")]),
  (OK="PASS"->true;halt(1)).
:- initialization(main,main).
main(Argv):- (Argv=[F|_]->run(F);halt(2)).
