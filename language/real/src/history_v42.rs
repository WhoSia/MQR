//! REALHISTORY 0.42-CANDIDATE
//! Finite observational quotient vs history-dependent target factorization.
//! This is a model-relative counterexample tool, NOT a world truth oracle.
//! No change to promoted REALPACKET / REALACQUIRE or v0.41 candidate.
#![forbid(unsafe_code)]
use std::collections::{BTreeMap,BTreeSet};
use std::{env,fs};

#[derive(Clone,Debug,PartialEq,Eq)]
enum ProbeStatus {Available,Destroyed,Unknown}
#[derive(Clone,Debug)]
struct World { name:String, fields:BTreeMap<String,String> }
#[derive(Clone,Debug)]
struct Court {
    id:String, basis:String, source_sha256:Option<String>, target:String,
    visible:Vec<String>, probes:BTreeMap<String,ProbeStatus>,
    worlds:Vec<World>,
}
fn identifier(s:&str)->bool{
    !s.is_empty() && s.len()<=80 &&
    s.bytes().all(|b|b.is_ascii_alphanumeric()||b==b'_'||b==b'-'||b==b'.')
}
fn parse(text:&str)->Result<Court,String>{
    let mut lines=text.lines().map(str::trim).filter(|s|!s.is_empty()&&!s.starts_with('#'));
    if lines.next()!=Some("REALHISTORY 0.42-CANDIDATE"){
        return Err("expected REALHISTORY 0.42-CANDIDATE".into());
    }
    let mut id=None;let mut basis=None;let mut source=None;let mut target=None;
    let mut visible=Vec::new();let mut probes=BTreeMap::new();
    let mut worlds=Vec::new();let mut names=BTreeSet::new();let mut ended=false;
    while let Some(line)=lines.next(){
        if line=="END" {ended=true;break;}
        let t:Vec<_>=line.split_whitespace().collect();
        match t.as_slice(){
            ["id",v] if identifier(v)=>{
                if id.replace((*v).to_string()).is_some(){return Err("duplicate id".into());}
            }
            ["basis",v] if ["FINITE_COUNTERMODEL","SOURCE_REPORTED"].contains(v)=>{
                if basis.replace((*v).to_string()).is_some(){return Err("duplicate basis".into());}
            }
            ["source_sha256",v]=>{
                if v.len()!=64||!v.bytes().all(|b|b.is_ascii_hexdigit())
                    ||source.replace((*v).to_string()).is_some(){return Err("invalid/duplicate SHA256".into());}
            }
            ["target",v] if identifier(v)=>{
                if target.replace((*v).to_string()).is_some(){return Err("duplicate target".into());}
            }
            ["observe",v] if identifier(v)=>{
                if visible.contains(&(*v).to_string()){return Err("duplicate observable".into());}
                visible.push((*v).to_string());
            }
            ["probe",v,status] if identifier(v)=>{
                let s=match *status {
                    "AVAILABLE"=>ProbeStatus::Available,
                    "DESTROYED"=>ProbeStatus::Destroyed,
                    "UNKNOWN"=>ProbeStatus::Unknown,
                    _=>return Err(format!("unknown probe status {status}")),
                };
                if probes.insert((*v).to_string(),s).is_some(){return Err("duplicate probe".into());}
            }
            ["world",w,rest @ ..] if identifier(w) && !rest.is_empty()=>{
                if !names.insert((*w).to_string()){return Err("duplicate possible world".into());}
                let mut fields=BTreeMap::new();
                for pair in rest {
                    let (k,v)=pair.split_once('=').ok_or("world fields require key=value")?;
                    if !identifier(k)||!identifier(v)||fields.insert(k.to_string(),v.to_string()).is_some(){
                        return Err("invalid or duplicate world field".into());
                    }
                }
                worlds.push(World{name:(*w).to_string(),fields});
                if worlds.len()>64 {return Err("maximum 64 finite model histories".into());}
            }
            _=>return Err(format!("unknown/malformed REALHISTORY statement: {line}")),
        }
    }
    if !ended || lines.next().is_some(){return Err("exactly one END with no trailing statements required".into());}
    let c=Court{
        id:id.ok_or("missing id")?,basis:basis.ok_or("missing basis")?,
        source_sha256:source,target:target.ok_or("missing target")?,
        visible,probes,worlds,
    };
    if c.basis=="SOURCE_REPORTED" && c.source_sha256.is_none(){
        return Err("source-reported model requires an externally checkable SHA256 pointer".into());
    }
    if c.basis=="FINITE_COUNTERMODEL" && c.source_sha256.is_some(){
        return Err("synthetic countermodel cannot masquerade as source-pinned observations".into());
    }
    if c.worlds.len()<2||c.visible.is_empty()||c.probes.len()>8{
        return Err(">=2 possible worlds, >=1 visible field and <=8 proposed probes required".into());
    }
    if c.visible.contains(&c.target)||c.probes.contains_key(&c.target){
        return Err("target must not be declared already observed/probed".into());
    }
    for k in &c.visible{
        if c.probes.contains_key(k){return Err("probe cannot duplicate existing observation".into());}
    }
    let fieldset:BTreeSet<_>=c.worlds[0].fields.keys().cloned().collect();
    let required:Vec<_>=c.visible.iter().chain(c.probes.keys()).chain(std::iter::once(&c.target)).collect();
    if required.iter().any(|key|!fieldset.contains(*key)){return Err("declared field absent in model".into());}
    if c.worlds.iter().any(|w|w.fields.keys().cloned().collect::<BTreeSet<_>>()!=fieldset){
        return Err("all worlds must share exact typed attribute schema".into());
    }
    Ok(c)
}
fn equiv(w1:&World,w2:&World,keys:&[String])->bool{
    keys.iter().all(|key|w1.fields[key]==w2.fields[key])
}
fn ambiguous(c:&Court,observables:&[String])->Vec<(String,String)>{
    let mut out=Vec::new();
    for i in 0..c.worlds.len(){
        for j in i+1..c.worlds.len(){
            if equiv(&c.worlds[i],&c.worlds[j],observables)
                && c.worlds[i].fields[&c.target]!=c.worlds[j].fields[&c.target]{
                out.push((c.worlds[i].name.clone(),c.worlds[j].name.clone()));
            }
        }
    }
    out
}
#[derive(Debug)]
struct Verdict {
    base:Vec<(String,String)>,all_available:Vec<(String,String)>,
    minimal_sets:Vec<Vec<String>>,
    missing:Vec<String>,
}
fn assess(c:&Court)->Verdict{
    let base=ambiguous(c,&c.visible);
    let available:Vec<String>=c.probes.iter().filter(|(_,s)|**s==ProbeStatus::Available)
        .map(|(k,_)|k.clone()).collect();
    let mut combined=c.visible.clone();combined.extend(available.clone());
    let all_available=ambiguous(c,&combined);
    let missing=c.probes.iter().filter(|(_,s)|**s!=ProbeStatus::Available)
        .map(|(k,_)|k.clone()).collect();
    let mut minimal_sets:Vec<Vec<String>>=Vec::new();
    for mask in 0..(1usize<<available.len()){
        let mut keys=c.visible.clone();let mut set=Vec::new();
        for (i,k) in available.iter().enumerate(){
            if mask&(1<<i)!=0{keys.push(k.clone());set.push(k.clone());}
        }
        if ambiguous(c,&keys).is_empty(){
            let n=set.len();
            if minimal_sets.is_empty()||n<minimal_sets[0].len(){
                minimal_sets.clear();minimal_sets.push(set);
            }else if n==minimal_sets[0].len(){minimal_sets.push(set);}
        }
    }
    Verdict{base,all_available,minimal_sets,missing}
}
fn render(c:&Court)->String{
    let v=assess(c);
    let example=v.base.first().map(|(a,b)|format!("{a},{b}"))
        .unwrap_or_else(||"NONE".into());
    let sets=if v.minimal_sets.is_empty(){"NONE".into()}else{
        v.minimal_sets.iter().map(|p|if p.is_empty(){"EMPTY".into()}else{p.join("+")})
            .collect::<Vec<_>>().join(";")
    };
    format!("history.version=0.42-CANDIDATE\nhistory.id={}\nhistory.basis={}\n\
             history.finite_worlds={}\nhistory.visible_fields={}\nhistory.target={}\n\
             history.base_ambiguous_pairs={}\nhistory.base_counterexample={}\n\
             history.base_finite_factorization={}\nhistory.all_available_probe_ambiguous_pairs={}\n\
             history.probe_minimal_resolving_sets={}\nhistory.nonavailable_probe_fields={}\n\
             history.finite_probe_status=CONDITIONAL_ONLY\nhistory.world_authority=HOLD\n\
             history.extrapolation_to_unmodeled_histories=FORBIDDEN\n\
             history.source_truth_from_sha256=NOT_INFERRED\nhistory.real_language_promotion=UNPROMOTED_CANDIDATE\n",
            c.id,c.basis,c.worlds.len(),c.visible.join("+"),c.target,
            v.base.len(),example,
            if v.base.is_empty(){"PASS_WITHIN_DECLARED_FINITE_MODEL"}else{"FAIL_TWIN_HISTORIES"},
            v.all_available.len(),sets,v.missing.join("+"))
}
fn main(){
    let path=env::args().nth(1).unwrap_or_else(||{eprintln!("usage: real-v42-history <packet.real>");std::process::exit(2)});
    let input=fs::read_to_string(path).unwrap_or_else(|e|{eprintln!("READ_FAILED: {e}");std::process::exit(2)});
    match parse(&input){Ok(c)=>print!("{}",render(&c)),Err(e)=>{
        eprintln!("REJECTED: {e}");std::process::exit(2);
    }}
}
#[cfg(test)]
mod tests {
    use super::*;
    const TWO:&str="REALHISTORY 0.42-CANDIDATE\nid selection\nbasis FINITE_COUNTERMODEL\ntarget published_full\nobserve tutorial\nprobe roster AVAILABLE\nworld h1 tutorial=PUB49 roster=R_A published_full=A\nworld h2 tutorial=PUB49 roster=R_B published_full=B\nEND\n";
    #[test]fn identifies_twin_histories(){let c=parse(TWO).unwrap();let a=assess(&c);assert_eq!(a.base.len(),1);assert!(a.all_available.is_empty());assert_eq!(a.minimal_sets,vec![vec!["roster".to_string()]]);}
    #[test]fn destructive_evidence_cannot_be_restored(){let c=parse(&TWO.replace("roster AVAILABLE","roster DESTROYED")).unwrap();let a=assess(&c);assert_eq!(a.all_available.len(),1);assert!(a.minimal_sets.is_empty());}
    #[test]fn possible_is_not_acquired(){let c=parse(&TWO.replace("roster AVAILABLE","roster UNKNOWN")).unwrap();assert!(render(&c).contains("history.all_available_probe_ambiguous_pairs=1"));}
    #[test]fn independent_nonseparating_channel_does_not_help(){let s=TWO.replace("probe roster AVAILABLE","probe roster AVAILABLE\nprobe duplicate AVAILABLE").replace("roster=R_A","roster=R_A duplicate=PUB49").replace("roster=R_B","roster=R_B duplicate=PUB49");let c=parse(&s).unwrap();let v=assess(&c);assert_eq!(v.minimal_sets,vec![vec!["roster".to_string()]]);}
    #[test]fn adding_observation_refines_not_coarsens(){let c=parse(TWO).unwrap();let b=ambiguous(&c,&c.visible).len();let mut obs=c.visible.clone();obs.push("roster".into());assert!(ambiguous(&c,&obs).len()<=b);}
    #[test]fn target_constant_on_fibers_suffices_locally(){let s=TWO.replace("published_full=B","published_full=A");let c=parse(&s).unwrap();let a=assess(&c);assert!(a.base.is_empty());assert_eq!(a.minimal_sets,vec![Vec::<String>::new()]);assert!(render(&c).contains("history.world_authority=HOLD"));}
    #[test]fn no_self_certificate_without_source(){let s=TWO.replace("basis FINITE_COUNTERMODEL","basis SOURCE_REPORTED");assert!(parse(&s).is_err());}
    #[test]fn synthetic_must_not_use_empirical_sha(){let s=TWO.replace("basis FINITE_COUNTERMODEL","basis FINITE_COUNTERMODEL\nsource_sha256 0000000000000000000000000000000000000000000000000000000000000000");assert!(parse(&s).is_err());}
    #[test]fn reject_bad_duplicate_and_trailing(){assert!(parse(&TWO.replace("id selection","id selection\nid duplicate")).is_err());assert!(parse(&(TWO.to_string()+"world illegal x=y\n")).is_err());}
    #[test]fn reject_target_laundering_as_observable(){assert!(parse(&TWO.replace("observe tutorial","observe tutorial\nobserve published_full")).is_err());}
    #[test]fn refusal_to_infer_world_completeness(){let c=parse(TWO).unwrap();assert!(render(&c).contains("extrapolation_to_unmodeled_histories=FORBIDDEN"));}
}
