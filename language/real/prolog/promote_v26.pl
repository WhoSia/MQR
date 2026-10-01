:- use_module(library(readutil)).

run(File) :-
    read_file_to_string(File, S, []),
    split_string(S, "\n", "\r", Lines0),
    exclude(blank, Lines0, Lines),
    phrase(packet(M), Lines),
    decide(M, D),
    format("promote.decision=~w~n", [D]),
    writeln("promote.prior_rule_necessary=REJECT"),
    writeln("promote.execution_universal_gate=REJECT"),
    writeln("promote.universal_meta_objective=NOT_EARNED"),
    writeln("promote.rpar=CANDIDATE"),
    writeln("promote.mcl=CANDIDATE"),
    writeln("promote.cdr=CANDIDATE").

blank(S) :- string_codes(S, Cs), forall(member(C,Cs), char_type(C, space)).

packet(M) --> ["REALPROMOTE 0.26"], body([], M).

body(A, M) --> ["END"], {dict_create(M, p, A)}.
body(A0, M) --> [Line], {
    split_string(Line, " ", " ", [K,V]),
    atom_string(KA,K), atom_string(VA,V)
  },
  body([KA-VA|A0], M).

v(M,K,D,V) :- (get_dict(K,M,V0) -> V=V0 ; V=D).

decide(M, D) :-
    v(M,sealed,'PASS',Sealed),
    v(M,lineage,'PASS',Lineage),
    v(M,live,'YES',Live),
    v(M,archive,'NO',Archive),
    v(M,add,'NONE',Add),
    v(M,contact,'NONE',Contact),
    v(M,repair,'NONE',Repair),
    v(M,simplify,'NO',Simplify),
    v(M,narrow,'NO',Narrow),
    v(M,localize,'NO',Localize),
    v(M,scope,'NO',Scope),
    (Sealed \= 'PASS' ; Lineage \= 'PASS') -> D='HOLD' ;
    (
      (Add='MATERIAL';Contact='INDEPENDENT';Repair='SCIENTIFIC';Simplify='YES';Narrow='YES';Localize='YES';Scope='YES')
      -> (Live='YES' -> D='PROMOTE' ; (Archive='YES' -> D='ARCHIVE' ; D='REJECT'))
      ; (Live='NO',Archive='YES' -> D='ARCHIVE'
        ; (Add='FORMAL';Contact='DUPLICATE';Repair='ENGINEERING') -> D='COMPRESS'
        ; D='REJECT')
    ).
