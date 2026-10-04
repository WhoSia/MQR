:- use_module(library(readutil)).
yn("YES",true). yn("NO",false).
verdict([_Id,_Domain,_A,_B,SA0,SI0,WC0,P0,N0,R0,B0,F0,_Expected],V):-
 yn(SA0,SA),yn(SI0,SI),yn(WC0,WC),yn(P0,P),yn(N0,N),yn(R0,R),yn(B0,B),yn(F0,F),
 ( P=true,R=true -> V="NO_PROSPECTIVE_AUTHORITY"
 ; N=true,R=false -> V="NOVEL_BUT_IRRELEVANT"
 ; B=true,F=false -> V="NO_CLOSURE_FROM_SEARCH_FAILURE"
 ; SA=true -> V="COMMON_MODE_HOLD"
 ; WC=true,F=true -> V="AUTHORITY_UPGRADED"
 ; SI=true,SA=false,WC=false,N=false,R=true -> V="BENIGN_SHARED_INFRASTRUCTURE"
 ; SA=false,R=true,F=true,WC=false -> V="ROUTE_DIVERSE_LOCAL"
 ; V="HOLD").
check([],0,0,[]).
check([R|Rs],N,B,[Id-V|Pairs]):-
 R=[Id|_],last(R,E),verdict(R,V),check(Rs,N0,B0,Pairs),N is N0+1,(V=E->B=B0;B is B0+1).
lookup(I,P,V):-member(I-V,P).
run(File):-
 read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls0),exclude(=(""),Ls0,[_|Ls]),
 findall(V,(member(L,Ls),split_string(L,"\t","",V)),Rows),check(Rows,N,B,P),
 lookup("N1",P,CM),lookup("C1",P,BI),lookup("M1",P,BC),lookup("N5",P,UP),lookup("N6",P,PO),lookup("N7",P,NI),
 (N=13,B=0,CM="COMMON_MODE_HOLD",BI="BENIGN_SHARED_INFRASTRUCTURE",BC="NO_CLOSURE_FROM_SEARCH_FAILURE",UP="AUTHORITY_UPGRADED",PO="NO_PROSPECTIVE_AUTHORITY",NI="NOVEL_BUT_IRRELEVANT"->OK="PASS";OK="FAIL"),
 format("MQR475_PROLOG_CHALLENGE_COURT=~w~n",[OK]),format("MQR475_PROLOG_CASES=~w~n",[N]),(OK="PASS"->true;halt(1)).
:- initialization(main,main).
main(Argv):- (Argv=[F|_]->run(F);halt(2)).
