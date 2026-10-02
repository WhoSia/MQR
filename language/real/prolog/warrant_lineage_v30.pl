:- use_module(library(readutil)).
field(Lines,K,V) :-
    member(Line,Lines),
    split_string(Line," "," ",[K0,V0]),
    K0=K,!,atom_string(V,V0).
need(Lines,K,V) :-
    (field(Lines,K,V)->true;format(user_error,"missing required field: ~w~n",[K]),halt(2)).
need_pass(Lines,K) :-
    need(Lines,K,V),(V='PASS'->true;format(user_error,"governance gate failed: ~w~n",[K]),halt(2)).
evidence('OBSERVED'). evidence('PROVED'). evidence('ENUMERATED').
evidence('SIMULATED'). evidence('INFERRED'). evidence('OPEN').
run(File):-
    read_file_to_string(File,S,[]), split_string(S,"\n","\r",Lines),
    (member("REALWARRANT 0.30-CANDIDATE",Lines)->true;
      writeln(user_error,'expected REALWARRANT 0.30-CANDIDATE'),halt(2)),
    need_pass(Lines,"sealed"),need_pass(Lines,"lineage"),need_pass(Lines,"audit"),
    need_pass(Lines,"intervention_frozen"),
    need(Lines,"evidence_kind",E),(evidence(E)->true;writeln(user_error,'invalid evidence kind'),halt(2)),
    need(Lines,"current_rule_hash",RH),need(Lines,"current_surface_hash",SH),
    (RH\='OPEN',SH\='OPEN'->true;writeln(user_error,'present surface hashes must be closed'),halt(2)),
    need(Lines,"extensional_pair_id",Pair),(Pair\='OPEN'->true;writeln(user_error,'extensional_pair_id must be explicit'),halt(2)),
    need(Lines,"full_lineage_ref",Lineage),need(Lines,"intervention_family_hash",IFH),
    need(Lines,"predictive_class",PC),need(Lines,"lineage_certificate",Cert),
    (Lineage\='OPEN',IFH\='OPEN',PC\='OPEN',Cert\='OPEN'->true;
      writeln(user_error,'lineage/predictive certificate fields must be explicit'),halt(2)),
    need(Lines,"predictive_class_authority",PCA),
    (PCA='DERIVED'->true;writeln(user_error,'predictive_class_authority must be DERIVED'),halt(2)),
    need(Lines,"primitive_ancestry_ontology",PAO),
    (PAO='OFF'->true;writeln(user_error,'primitive_ancestry_ontology must be OFF'),halt(2)),
    need(Lines,"minimality_claim",MC),
    (MC='INTERVENTION_RELATIVE'->true;writeln(user_error,'minimality_claim must be INTERVENTION_RELATIVE'),halt(2)),
    need(Lines,"scope",Scope),
    (E='SIMULATED'->WV='NOT_ESTABLISHED';E='OPEN'->WV='OPEN';WV='LIMITED_BY_EVIDENCE_KIND'),
    format("warrant.current_rule_hash=~w~n",[RH]),
    format("warrant.current_surface_hash=~w~n",[SH]),
    format("warrant.scope=~w~n",[Scope]),
    format("warrant.extensional_pair_id=~w~n",[Pair]),
    format("warrant.full_lineage_ref=~w~n",[Lineage]),
    format("warrant.intervention_family_hash=~w~n",[IFH]),
    format("warrant.predictive_class=~w~n",[PC]),
    format("warrant.lineage_certificate=~w~n",[Cert]),
    writeln("warrant.predictive_class_authority=DERIVED"),
    writeln("warrant.minimality_claim=INTERVENTION_RELATIVE"),
    writeln("warrant.full_lineage_equals_minimal_state=NO"),
    writeln("warrant.typed_ancestry_axes_primitive=NO"),
    writeln("warrant.behavioral_sufficiency_world_validity=NOT_ESTABLISHED"),
    format("warrant.evidence_kind=~w~n",[E]),
    format("warrant.world_validity=~w~n",[WV]),
    writeln("warrant.status=CANDIDATE_UNPROMOTED").
:- initialization(main,main).
main(Argv):- (Argv=[File|_]->run(File);writeln(user_error,'usage: swipl -q -f warrant_lineage_v30.pl -- <packet>'),halt(2)).
