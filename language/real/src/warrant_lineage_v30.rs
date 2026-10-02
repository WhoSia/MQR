use std::{collections::HashMap, env, fs, process};

fn get<'a>(m:&'a HashMap<String,String>, k:&str)->&'a str{
    m.get(k).map(String::as_str).unwrap_or_else(||{
        eprintln!("missing required field: {k}");
        process::exit(2)
    })
}
fn allowed_evidence(x:&str)->bool{
    matches!(x,"OBSERVED"|"PROVED"|"ENUMERATED"|"SIMULATED"|"INFERRED"|"OPEN")
}
fn main(){
    let path=env::args().nth(1).unwrap_or_else(||{
        eprintln!("usage: real-v30-warrant-lineage <packet>");
        process::exit(2)
    });
    let src=fs::read_to_string(path).unwrap_or_else(|e|{
        eprintln!("read failed: {e}");
        process::exit(2)
    });
    let mut header=false;
    let mut m=HashMap::<String,String>::new();
    for raw in src.lines(){
        let line=raw.trim();
        if line.is_empty() || line.starts_with('#'){continue}
        if line=="REALWARRANT 0.30-CANDIDATE"{header=true;continue}
        if line=="END"{break}
        let mut it=line.split_whitespace();
        match (it.next(),it.next(),it.next()){
            (Some(k),Some(v),None)=>{m.insert(k.to_string(),v.to_string());}
            _=>{eprintln!("invalid packet line: {line}");process::exit(2)}
        }
    }
    if !header{eprintln!("expected REALWARRANT 0.30-CANDIDATE");process::exit(2)}
    for k in ["sealed","lineage","audit","intervention_frozen"]{
        if get(&m,k)!="PASS"{eprintln!("governance gate failed: {k}");process::exit(2)}
    }
    let evidence=get(&m,"evidence_kind");
    if !allowed_evidence(evidence){eprintln!("invalid evidence kind");process::exit(2)}
    if get(&m,"current_rule_hash")=="OPEN" || get(&m,"current_surface_hash")=="OPEN"{
        eprintln!("present surface hashes must be closed");
        process::exit(2)
    }
    let pair=get(&m,"extensional_pair_id");
    if pair=="OPEN"{eprintln!("extensional_pair_id must be explicit");process::exit(2)}
    let lineage=get(&m,"full_lineage_ref");
    let intervention=get(&m,"intervention_family_hash");
    let pclass=get(&m,"predictive_class");
    let cert=get(&m,"lineage_certificate");
    if lineage=="OPEN" || intervention=="OPEN" || pclass=="OPEN" || cert=="OPEN"{
        eprintln!("lineage/predictive certificate fields must be explicit");
        process::exit(2)
    }
    if get(&m,"predictive_class_authority")!="DERIVED"{
        eprintln!("predictive_class_authority must be DERIVED");
        process::exit(2)
    }
    if get(&m,"primitive_ancestry_ontology")!="OFF"{
        eprintln!("primitive_ancestry_ontology must be OFF");
        process::exit(2)
    }
    if get(&m,"minimality_claim")!="INTERVENTION_RELATIVE"{
        eprintln!("minimality_claim must be INTERVENTION_RELATIVE");
        process::exit(2)
    }
    let world=if evidence=="SIMULATED"{"NOT_ESTABLISHED"}
        else if evidence=="OPEN"{"OPEN"}
        else {"LIMITED_BY_EVIDENCE_KIND"};

    println!("warrant.current_rule_hash={}",get(&m,"current_rule_hash"));
    println!("warrant.current_surface_hash={}",get(&m,"current_surface_hash"));
    println!("warrant.scope={}",get(&m,"scope"));
    println!("warrant.extensional_pair_id={pair}");
    println!("warrant.full_lineage_ref={lineage}");
    println!("warrant.intervention_family_hash={intervention}");
    println!("warrant.predictive_class={pclass}");
    println!("warrant.lineage_certificate={cert}");
    println!("warrant.predictive_class_authority=DERIVED");
    println!("warrant.minimality_claim=INTERVENTION_RELATIVE");
    println!("warrant.full_lineage_equals_minimal_state=NO");
    println!("warrant.typed_ancestry_axes_primitive=NO");
    println!("warrant.behavioral_sufficiency_world_validity=NOT_ESTABLISHED");
    println!("warrant.evidence_kind={evidence}");
    println!("warrant.world_validity={world}");
    println!("warrant.status=CANDIDATE_UNPROMOTED");
}
