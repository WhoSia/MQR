use std::{env,fs,process,collections::BTreeMap};

const ORIGINS:[&str;4]=["INTERNAL","EXTERNAL","MIXED","UNKNOWN"];
const CORR:[&str;5]=["EXACT","REFINE","MERGE","OVERLAP","DISJOINT"];
const CONTACT:[&str;7]=["MEASUREMENT","RAW_DATA","ANALYSIS","SEMANTIC","PROOF","MODEL","NONE"];
const SM:[&str;3]=["NONE","SPLIT","MERGE"];
const STATES:[&str;7]=["NO_UPGRADE","DIAGNOSTIC_REPLICATION_ONLY","LOCAL_AUTHORITY_UPGRADE","CROSS_ROUTE_INDEPENDENCE_UPGRADE","SPLIT_REQUIRED","MERGE_COLLAPSE","REOPEN"];
const EFFECTS:[&str;5]=["BREAK","PRESERVE","REPLACE","UNRESOLVED","NEW"];
const FIELDS:[&str;16]=[
"id","sealed","origin","source_challenge_hash","claim_scope_hash","source_dependency_graph_hash",
"witness_route","witness_provenance_hash","correspondence","postoutcome_tuned","contact_kind",
"split_merge","residual_common_mode","authority_state","certificate_version",
"reopen_on_ancestry_revision"
];

#[derive(Debug)]
struct Dep{name:String,effect:String,prov:String}
fn die(m:impl AsRef<str>)->!{eprintln!("{}",m.as_ref());process::exit(2)}
fn req<'a>(m:&'a BTreeMap<String,String>,k:&str)->&'a str{m.get(k).map(String::as_str).unwrap_or_else(||die(format!("missing required field: {k}")))}
fn explicit(x:&str)->bool{!x.is_empty()&&x!="OPEN"&&x!="NA"}
fn yn(x:&str)->bool{match x{"YES"=>true,"NO"=>false,_=>die(format!("expected YES/NO, got {x}"))}}

fn main(){
 let p=env::args().nth(1).unwrap_or_else(||die("usage: real-v33-upgrade <packet>"));
 let src=fs::read_to_string(&p).unwrap_or_else(|e|die(format!("read failed: {e}")));
 let mut header=false;let mut ended=false;let mut f=BTreeMap::new();let mut deps=Vec::new();
 for (ln,raw) in src.lines().enumerate(){
   let line=raw.trim(); if line.is_empty()||line.starts_with('#'){continue}
   if line=="REALUPGRADE 0.33-CANDIDATE"{header=true;continue}
   if line=="END"{ended=true;break}
   let t:Vec<&str>=line.split_whitespace().collect();
   if t.first()==Some(&"dependency"){
     if t.len()!=4||!EFFECTS.contains(&t[2]){die(format!("{}:{} invalid dependency",p,ln+1))}
     if matches!(t[2],"BREAK"|"REPLACE"|"NEW")&&!explicit(t[3]){die("authority-changing dependency edge requires explicit provenance")}
     deps.push(Dep{name:t[1].into(),effect:t[2].into(),prov:t[3].into()});
     continue
   }
   if t.len()!=2{die(format!("{}:{} invalid field",p,ln+1))}
   if !FIELDS.contains(&t[0]){die(format!("{}:{} unknown field: {}",p,ln+1,t[0]))}
   if f.insert(t[0].into(),t[1].into()).is_some(){die(format!("duplicate field: {}",t[0]))}
 }
 if !header||!ended{die("packet must contain REALUPGRADE 0.33-CANDIDATE ... END")}
 if req(&f,"sealed")!="PASS"{die("sealed must be PASS")}
 for k in ["id","source_challenge_hash","claim_scope_hash","source_dependency_graph_hash","witness_route","witness_provenance_hash","certificate_version"]{
   if !explicit(req(&f,k)){die(format!("{k} must be explicit"))}
 }
 let origin=req(&f,"origin"); if !ORIGINS.contains(&origin){die("invalid origin")}
 let corr=req(&f,"correspondence"); if !CORR.contains(&corr){die("invalid correspondence")}
 let post=yn(req(&f,"postoutcome_tuned"));
 let contact=req(&f,"contact_kind"); if !CONTACT.contains(&contact){die("invalid contact_kind")}
 let sm=req(&f,"split_merge"); if !SM.contains(&sm){die("invalid split_merge")}
 let residual=yn(req(&f,"residual_common_mode"));
 let state=req(&f,"authority_state"); if !STATES.contains(&state){die("invalid authority_state")}
 if req(&f,"reopen_on_ancestry_revision")!="YES"{die("upgrade certificate must be defeasible and reopen on ancestry revision")}
 let breaks=deps.iter().filter(|d|d.effect=="BREAK").count();
 let upgrade=matches!(state,"LOCAL_AUTHORITY_UPGRADE"|"CROSS_ROUTE_INDEPENDENCE_UPGRADE");
 if upgrade {
   if corr=="DISJOINT"{die("noncorresponding witness cannot earn authority upgrade")}
   if post{die("post-outcome tuned route cannot earn prospective authority upgrade")}
   if breaks==0{die("authority upgrade requires at least one relevant dependency BREAK")}
 }
 if state=="CROSS_ROUTE_INDEPENDENCE_UPGRADE" && (residual||contact=="NONE"){
   die("cross-route upgrade requires no declared residual common mode and non-NONE contact")}
 if state=="SPLIT_REQUIRED" && !(sm=="SPLIT"||matches!(corr,"REFINE"|"OVERLAP")){
   die("SPLIT_REQUIRED needs split state or partial correspondence")}
 if state=="MERGE_COLLAPSE" && sm!="MERGE"{die("MERGE_COLLAPSE requires split_merge MERGE")}
 println!("upgrade.id={}",req(&f,"id"));
 println!("upgrade.origin={origin}");
 println!("upgrade.correspondence={corr}");
 println!("upgrade.contact_kind={contact}");
 println!("upgrade.split_merge={sm}");
 println!("upgrade.residual_common_mode={}",if residual{"YES"}else{"NO"});
 println!("upgrade.postoutcome_tuned={}",if post{"YES"}else{"NO"});
 println!("upgrade.authority_state={state}");
 println!("upgrade.break_count={breaks}");
 println!("upgrade.dependency_count={}",deps.len());
 println!("upgrade.original_independence_rewritten=NO");
 println!("upgrade.independence_scalar=OFF");
 println!("upgrade.reopen_on_ancestry_revision=YES");
 println!("upgrade.status=CANDIDATE_UNPROMOTED");
 for (i,d) in deps.iter().enumerate(){println!("upgrade.dependency.{i}={}:{}:{}",d.name,d.effect,d.prov)}
}
