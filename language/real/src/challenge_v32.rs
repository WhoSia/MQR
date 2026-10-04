use std::{collections::{BTreeMap,BTreeSet},env,fs,process};

const EVIDENCE:[&str;6]=["OBSERVED","PROVED","ENUMERATED","SIMULATED","INFERRED","OPEN"];
const RELATIONS:[&str;6]=[
 "COMMON_MODE_HOLD","INDEPENDENT_CHALLENGE","ROUTE_DIVERSE_LOCAL",
 "AUTHORITY_UPGRADED","BENIGN_SHARED_INFRASTRUCTURE","NO_CLOSURE_FROM_SEARCH_FAILURE"
];

#[derive(Clone,Debug)]
struct Gen{
 id:String,family:String,ancestry:String,target_dep:bool,world_contact:bool,
 post:bool,novel:bool,relevant:bool,bounded:bool
}
#[derive(Clone,Debug)]
struct Pair{
 a:String,b:String,shared_ancestry:bool,shared_infra:bool,route_diverse:bool,relation:String
}

fn die(m:impl AsRef<str>)->!{eprintln!("{}",m.as_ref());process::exit(2)}
fn yn(x:&str)->bool{match x{"YES"=>true,"NO"=>false,_=>die(format!("expected YES/NO, got {x}"))}}
fn req<'a>(m:&'a BTreeMap<String,String>,k:&str)->&'a str{m.get(k).map(String::as_str).unwrap_or_else(||die(format!("missing required field: {k}")))}
fn explicit(x:&str)->bool{!x.is_empty()&&x!="OPEN"}

fn main(){
 let path=env::args().nth(1).unwrap_or_else(||die("usage: real-v32-challenge <packet>"));
 let src=fs::read_to_string(&path).unwrap_or_else(|e|die(format!("read failed: {e}")));
 let mut header=false;let mut ended=false;let mut fields=BTreeMap::new();let mut gs=Vec::new();let mut ps=Vec::new();
 for (ln,raw) in src.lines().enumerate(){
   let line=raw.trim(); if line.is_empty()||line.starts_with('#'){continue}
   if line=="REALCHALLENGE 0.32-CANDIDATE"{header=true;continue}
   if line=="END"{ended=true;break}
   let t:Vec<&str>=line.split_whitespace().collect();
   if t.first()==Some(&"generator"){
     if t.len()!=10{die(format!("{}:{} generator expects 9 args",path,ln+1))}
     gs.push(Gen{id:t[1].into(),family:t[2].into(),ancestry:t[3].into(),
       target_dep:yn(t[4]),world_contact:yn(t[5]),post:yn(t[6]),novel:yn(t[7]),relevant:yn(t[8]),bounded:yn(t[9])});
     continue
   }
   if t.first()==Some(&"pair"){
     if t.len()!=7||!RELATIONS.contains(&t[6]){die(format!("{}:{} invalid pair",path,ln+1))}
     ps.push(Pair{a:t[1].into(),b:t[2].into(),shared_ancestry:yn(t[3]),shared_infra:yn(t[4]),route_diverse:yn(t[5]),relation:t[6].into()});
     continue
   }
   if t.len()!=2{die(format!("{}:{} invalid field",path,ln+1))}
   fields.insert(t[0].into(),t[1].into());
 }
 if !header||!ended{die("packet must contain REALCHALLENGE 0.32-CANDIDATE ... END")}
 if req(&fields,"sealed")!="PASS"{die("sealed must be PASS")}
 for k in ["claim_scope_hash","challenge_family_hash","portfolio_id","admissibility_rule_hash","dependency_rule_hash"]{
   if !explicit(req(&fields,k)){die(format!("{k} must be explicit"))}
 }
 let ev=req(&fields,"evidence_kind"); if !EVIDENCE.contains(&ev){die("invalid evidence_kind")}
 if req(&fields,"completeness_claim")!="RELATIVE_ONLY"{die("completeness_claim must be RELATIVE_ONLY")}
 if req(&fields,"open_world_complete")!="OFF"{die("open_world_complete must be OFF")}

 let ids:BTreeSet<String>=gs.iter().map(|g|g.id.clone()).collect();
 for p in &ps{
   if !ids.contains(&p.a)||!ids.contains(&p.b){die("pair references undeclared generator")}
   let a=gs.iter().find(|g|g.id==p.a).unwrap();
   let b=gs.iter().find(|g|g.id==p.b).unwrap();
   match p.relation.as_str(){
     "COMMON_MODE_HOLD"=>{
       if !p.shared_ancestry{die("COMMON_MODE_HOLD requires shared authority ancestry")}
     }
     "INDEPENDENT_CHALLENGE"=>{
       if p.shared_ancestry||!p.route_diverse||!(a.world_contact||b.world_contact){die("independent challenge not earned")}
       if a.post||b.post{die("post-outcome generator cannot earn prospective independent authority")}
       if !a.relevant||!b.relevant{die("claim-irrelevant generator cannot earn independent challenge authority")}
     }
     "ROUTE_DIVERSE_LOCAL"=>{
       if p.shared_ancestry||!p.route_diverse{die("route-diverse local relation not earned")}
       if !a.relevant||!b.relevant{die("route-diverse local requires claim relevance")}
     }
     "AUTHORITY_UPGRADED"=>{
       if p.shared_ancestry||!(a.world_contact||b.world_contact)||!p.route_diverse{die("authority upgrade requires external/contact route break")}
       if a.post||b.post{die("post-outcome tuning blocks prospective upgrade")}
     }
     "BENIGN_SHARED_INFRASTRUCTURE"=>{
       if p.shared_ancestry||!p.shared_infra{die("benign shared infrastructure requires shared infrastructure without shared authority ancestry")}
     }
     "NO_CLOSURE_FROM_SEARCH_FAILURE"=>{
       if !(a.bounded||b.bounded){die("search-failure ceiling requires bounded search")}
     }
     _=>unreachable!()
   }
 }
 let common=ps.iter().filter(|p|p.relation=="COMMON_MODE_HOLD").count();
 let independent=ps.iter().filter(|p|p.relation=="INDEPENDENT_CHALLENGE").count();
 let upgraded=ps.iter().filter(|p|p.relation=="AUTHORITY_UPGRADED").count();
 let no_closure=ps.iter().filter(|p|p.relation=="NO_CLOSURE_FROM_SEARCH_FAILURE").count();
 let post=gs.iter().filter(|g|g.post).count();
 let novel_irrelevant=gs.iter().filter(|g|g.novel&&!g.relevant).count();

 println!("challenge.portfolio_id={}",req(&fields,"portfolio_id"));
 println!("challenge.generator_count={}",gs.len());
 println!("challenge.pair_count={}",ps.len());
 println!("challenge.common_mode_count={common}");
 println!("challenge.independent_count={independent}");
 println!("challenge.authority_upgrade_count={upgraded}");
 println!("challenge.no_closure_count={no_closure}");
 println!("challenge.postoutcome_generator_count={post}");
 println!("challenge.novel_irrelevant_count={novel_irrelevant}");
 println!("challenge.novelty_is_independence=NO");
 println!("challenge.algorithm_diversity_is_assumption_diversity=NO");
 println!("challenge.shared_infrastructure_is_automatic_dependence=NO");
 println!("challenge.bounded_search_failure_is_counterexample_absence=NO");
 println!("challenge.portfolio_diversity_is_generator_completeness=NO");
 println!("challenge.postoutcome_tuning_is_prospective_authority=NO");
 println!("challenge.completeness_claim=RELATIVE_ONLY");
 println!("challenge.open_world_complete=OFF");
 println!("challenge.evidence_kind={ev}");
 println!("challenge.status=CANDIDATE_UNPROMOTED");

 for (i,g) in gs.iter().enumerate(){
   println!("challenge.generator.{i}={}:{}:{}:{}:{}:{}:{}:{}:{}",
     g.id,g.family,g.ancestry,if g.target_dep{"YES"}else{"NO"},if g.world_contact{"YES"}else{"NO"},
     if g.post{"YES"}else{"NO"},if g.novel{"YES"}else{"NO"},if g.relevant{"YES"}else{"NO"},if g.bounded{"YES"}else{"NO"});
 }
 for (i,p) in ps.iter().enumerate(){
   println!("challenge.pair.{i}={}:{}:{}:{}:{}:{}",
     p.a,p.b,if p.shared_ancestry{"YES"}else{"NO"},if p.shared_infra{"YES"}else{"NO"},
     if p.route_diverse{"YES"}else{"NO"},p.relation);
 }
}
