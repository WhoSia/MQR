use std::{env,fs};

fn one(slot:&mut Option<String>,v:&str,name:&str)->Result<(),String>{
    if slot.is_some(){return Err(format!("duplicate {name}"));}
    *slot=Some(v.to_string()); Ok(())
}
fn yn(b:bool)->&'static str{if b{"YES"}else{"NO"}}
fn main(){if let Err(e)=run(){eprintln!("REALINVARIANCE_ERROR {e}");std::process::exit(2);}}
fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v21-invariance <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut header=false; let mut ended=false;
    let mut id=None; let mut target=None; let mut grammar=None; let mut scope=None;
    let mut probe=None; let mut intervention=None; let mut composition=None;
    let mut defeat=None; let mut embedding=None; let mut morphism=None;
    let mut provenance=None; let mut reopening=None;

    for(ln,raw) in src.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        if ended{return Err(format!("content after END at line {}",ln+1));}
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header{
            if t.as_slice()==["REALINVARIANCE","0.21"]{header=true;continue;}
            return Err(format!("expected REALINVARIANCE 0.21 at line {}",ln+1));
        }
        match t[0]{
            "END" if t.len()==1=>ended=true,
            "id" if t.len()==2=>one(&mut id,t[1],"id")?,
            "target" if t.len()==2=>{
                if !matches!(t[1],"PROGRESS"|"MEASUREMENT"|"CAUSAL"|"REPRESENTATION"|"OTHER"){return Err("bad target".into());}
                one(&mut target,t[1],"target")?;
            }
            "grammar" if t.len()==2=>{
                if !matches!(t[1],"GROUP"|"GROUPOID"|"PSEUDOGROUP"|"MONOID"|"PARTIAL_FAMILY"){return Err("bad grammar".into());}
                one(&mut grammar,t[1],"grammar")?;
            }
            "scope" if t.len()==2=>{
                if !matches!(t[1],"SUBSYSTEM"|"COMPOSITE"|"GLOBAL"){return Err("bad scope".into());}
                one(&mut scope,t[1],"scope")?;
            }
            "probe_preservation" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad probe_preservation".into());}
                one(&mut probe,t[1],"probe_preservation")?;
            }
            "intervention_preservation" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad intervention_preservation".into());}
                one(&mut intervention,t[1],"intervention_preservation")?;
            }
            "composition_status" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"PARTIAL_VERIFIED"|"UNKNOWN"){return Err("bad composition_status".into());}
                one(&mut composition,t[1],"composition_status")?;
            }
            "defeat_preservation" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad defeat_preservation".into());}
                one(&mut defeat,t[1],"defeat_preservation")?;
            }
            "embedding_status" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"LOCAL_ONLY"|"FAIL"|"UNKNOWN"){return Err("bad embedding_status".into());}
                one(&mut embedding,t[1],"embedding_status")?;
            }
            "morphism_integrity" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad morphism_integrity".into());}
                one(&mut morphism,t[1],"morphism_integrity")?;
            }
            "preseal_provenance" if t.len()==2=>{
                if !matches!(t[1],"SEALED"|"POSTHOC"){return Err("bad preseal_provenance".into());}
                one(&mut provenance,t[1],"preseal_provenance")?;
            }
            "reopening" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"INACTIVE"){return Err("bad reopening".into());}
                one(&mut reopening,t[1],"reopening")?;
            }
            _=>return Err(format!("unknown or malformed line {}: {}",ln+1,line)),
        }
    }
    if !header||!ended{return Err("missing header or END".into());}
    let _id=id.ok_or("missing id")?;
    let target=target.ok_or("missing target")?;
    let grammar=grammar.ok_or("missing grammar")?;
    let scope=scope.ok_or("missing scope")?;
    let probe=probe.ok_or("missing probe_preservation")?;
    let intervention=intervention.ok_or("missing intervention_preservation")?;
    let composition=composition.ok_or("missing composition_status")?;
    let defeat=defeat.ok_or("missing defeat_preservation")?;
    let embedding=embedding.ok_or("missing embedding_status")?;
    let morphism=morphism.ok_or("missing morphism_integrity")?;
    let provenance=provenance.ok_or("missing preseal_provenance")?;
    let reopening=reopening.ok_or("missing reopening")?;

    let closure_ok=if grammar=="PARTIAL_FAMILY"{
        composition=="PASS"||composition=="PARTIAL_VERIFIED"
    }else{
        composition=="PASS"
    };
    let embedding_ok=embedding=="PASS"||(embedding=="LOCAL_ONLY"&&scope!="GLOBAL");
    let preservation_ok=probe=="PASS"&&intervention=="PASS"&&defeat=="PASS";
    let constitution_admissible=preservation_ok&&closure_ok&&embedding_ok
        &&morphism=="PASS"&&provenance=="SEALED"&&reopening=="ACTIVE";
    let global_transport=constitution_admissible&&scope=="GLOBAL"&&embedding=="PASS";
    let diagnosis=
        if intervention=="FAIL"{"OVER_QUOTIENT"}
        else if probe=="FAIL"{"PROBE_FAILURE"}
        else if composition=="FAIL"||composition=="UNKNOWN"{"CLOSURE_FAILURE"}
        else if defeat=="FAIL"{"DEFEAT_ERASURE"}
        else if embedding=="FAIL"||(scope=="GLOBAL"&&embedding=="LOCAL_ONLY"){"SCOPE_EXPORT_FAILURE"}
        else if morphism=="FAIL"{"MORPHISM_CAPTURE"}
        else if provenance=="POSTHOC"{"CONSTITUTION_CAPTURE"}
        else if reopening=="INACTIVE"{"REOPENING_FAILURE"}
        else{"ADMISSIBLE_LOCAL"};

    println!("invariance.target={target}");
    println!("invariance.grammar={grammar}");
    println!("invariance.scope={scope}");
    println!("invariance.probe_preservation={probe}");
    println!("invariance.intervention_preservation={intervention}");
    println!("invariance.composition_status={composition}");
    println!("invariance.defeat_preservation={defeat}");
    println!("invariance.embedding_status={embedding}");
    println!("invariance.morphism_integrity={morphism}");
    println!("invariance.preseal_provenance={provenance}");
    println!("invariance.reopening={reopening}");
    println!("invariance.grammar_closure_adequate={}",yn(closure_ok));
    println!("invariance.embedding_claim_adequate={}",yn(embedding_ok));
    println!("invariance.constitution_admissible={}",yn(constitution_admissible));
    println!("invariance.global_transport={}",if global_transport{"YES_WITHIN_DECLARED_SCOPE"}else{"NO"});
    println!("invariance.diagnosis={diagnosis}");
    println!("invariance.self_authorizing=REJECT");
    println!("invariance.unique_global_constitution=NOT_EARNED");
    println!("invariance.actual_symmetry_equals_certified_inert=NO");
    println!("invariance.relation=CONTRACT_INDEXED");
    println!("invariance.wcicr={}",if constitution_admissible{"EARNED_LOCAL_CANDIDATE"}else{"HOLD"});
    Ok(())
}
