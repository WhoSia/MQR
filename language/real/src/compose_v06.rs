use std::{collections::{BTreeMap,BTreeSet},env,fs,path::Path};

#[derive(Clone,Copy,Debug,PartialEq,Eq,PartialOrd,Ord)]
enum Status{Fail,Hold,Pass}
impl Status{
 fn parse(s:&str)->Result<Self,String>{match s{"FAIL"=>Ok(Self::Fail),"HOLD"=>Ok(Self::Hold),"PASS"=>Ok(Self::Pass),_=>Err(format!("invalid status {s}"))}}
 fn text(self)->&'static str{match self{Self::Fail=>"FAIL",Self::Hold=>"HOLD",Self::Pass=>"PASS"}}
}
fn meet(a:Status,b:Status)->Status{if a<b{a}else{b}}

#[derive(Clone,Debug)]
struct Bridge{id:String,src:String,dst:String,local:Status,custody:Status}
#[derive(Clone,Debug)]
struct Semantic{id:String,status:Status,warrant:String}
#[derive(Clone,Debug)]
struct Ancestor{id:String,status:Status}
#[derive(Clone,Debug)]
struct Assumption{bridge:String,key:String,value:String,status:Status}
#[derive(Clone,Debug)]
struct Defeat{bridge:String,src:String,dst:String,state:String}

#[derive(Default)]
struct Packet{
 id:String,
 source_authority:Option<Status>,
 final_authority:Option<Status>,
 bridges:Vec<Bridge>,
 semantics:BTreeMap<String,Semantic>,
 semantic_comp:Option<(Status,String)>,
 scope_source:BTreeSet<String>,
 scope_maps:BTreeMap<String,Vec<(String,String)>>,
 final_claim:BTreeSet<String>,
 ancestors:Vec<Ancestor>,
 preserves:BTreeSet<(String,String)>,
 assumptions:Vec<Assumption>,
 defeats:Vec<Defeat>,
 direct:Option<Status>,
 requested:Option<Status>,
}

fn tokens(s:&str)->Vec<String>{s.split_whitespace().map(|x|x.trim_matches('"').to_string()).collect()}

fn parse(path:&Path)->Result<Packet,String>{
 let txt=fs::read_to_string(path).map_err(|e|e.to_string())?;
 let mut p=Packet::default(); let mut started=false; let mut ended=false;
 for (i,raw) in txt.lines().enumerate(){
  let line=raw.trim(); if line.is_empty()||line.starts_with('#'){continue}
  let t=tokens(line); if t.is_empty(){continue}
  if t[0]=="REALCOMPOSE"{if t.len()!=2||t[1]!="0.6"{return Err("expected REALCOMPOSE 0.6".into())}started=true;continue}
  if !started{return Err("packet must begin REALCOMPOSE 0.6".into())}
  if t[0]=="END"{ended=true;break}
  match t[0].as_str(){
   "id" if t.len()==2=>p.id=t[1].clone(),
   "source_authority" if t.len()==2=>p.source_authority=Some(Status::parse(&t[1].to_uppercase())?),
   "final_authority" if t.len()==2=>p.final_authority=Some(Status::parse(&t[1].to_uppercase())?),
   "bridge" if t.len()==6=>{
    p.bridges.push(Bridge{id:t[1].clone(),src:t[2].clone(),dst:t[3].clone(),local:Status::parse(&t[4].to_uppercase())?,custody:Status::parse(&t[5].to_uppercase())?});
   }
   "semantic" if t.len()==4=>{
    p.semantics.insert(t[1].clone(),Semantic{id:t[1].clone(),status:Status::parse(&t[2].to_uppercase())?,warrant:t[3].to_uppercase()});
   }
   "semantic_comp" if t.len()==3=>p.semantic_comp=Some((Status::parse(&t[1].to_uppercase())?,t[2].to_uppercase())),
   "scope_source" if t.len()>=2=>for x in &t[1..]{p.scope_source.insert(x.clone());},
   "scope_map" if t.len()==4=>p.scope_maps.entry(t[1].clone()).or_default().push((t[2].clone(),t[3].clone())),
   "final_claim" if t.len()>=2=>for x in &t[1..]{p.final_claim.insert(x.clone());},
   "ancestor" if t.len()==3=>p.ancestors.push(Ancestor{id:t[1].clone(),status:Status::parse(&t[2].to_uppercase())?}),
   "preserve" if t.len()==3=>{p.preserves.insert((t[1].clone(),t[2].clone()));},
   "assumption" if t.len()==5=>p.assumptions.push(Assumption{bridge:t[1].clone(),key:t[2].clone(),value:t[3].to_uppercase(),status:Status::parse(&t[4].to_uppercase())?}),
   "defeat" if t.len()==5=>{
    let st=t[4].to_uppercase(); if !["REACHABLE","DEAD","FORBIDDEN"].contains(&st.as_str()){return Err(format!("invalid defeat state {st}"))}
    p.defeats.push(Defeat{bridge:t[1].clone(),src:t[2].clone(),dst:t[3].clone(),state:st});
   }
   "direct_receipt" if t.len()==2=>p.direct=Some(Status::parse(&t[1].to_uppercase())?),
   "authorize" if t.len()==2=>p.requested=Some(Status::parse(&t[1].to_uppercase())?),
   _=>return Err(format!("{}:{} malformed command {line}",path.display(),i+1))
  }
 }
 if !ended{return Err("missing END".into())}
 if p.id.is_empty()||p.source_authority.is_none()||p.final_authority.is_none()||p.bridges.len()<2||p.requested.is_none(){return Err("missing required composition field".into())}
 Ok(p)
}

fn endpoint(p:&Packet)->Status{
 for w in p.bridges.windows(2){if w[0].dst!=w[1].src{return Status::Fail}}
 Status::Pass
}
fn semantic(p:&Packet)->Status{
 let mut s=Status::Pass;
 for b in &p.bridges{
  let Some(w)=p.semantics.get(&b.id) else{return Status::Hold};
  if w.warrant=="SELF"{return Status::Fail}
  s=meet(s,w.status);
 }
 match &p.semantic_comp{
  None=>Status::Hold,
  Some((st,w))=>{if w=="SELF"{Status::Fail}else{meet(s,*st)}}
 }
}
fn scope(p:&Packet)->Status{
 if p.final_claim.is_empty()||p.scope_source.is_empty(){return Status::Hold}
 let mut frontier=p.scope_source.clone();
 for b in &p.bridges{
  let Some(maps)=p.scope_maps.get(&b.id) else{return Status::Hold};
  let mut next=BTreeSet::new();
  for (a,z) in maps{if frontier.contains(a){next.insert(z.clone());}}
  frontier=next;
  if frontier.is_empty(){return Status::Fail}
 }
 if p.final_claim.iter().all(|x|frontier.contains(x)){Status::Pass}else{Status::Fail}
}
fn ancestry(p:&Packet)->Status{
 if p.ancestors.is_empty(){return Status::Hold}
 for a in &p.ancestors{
  for b in &p.bridges{
   if !p.preserves.contains(&(b.id.clone(),a.id.clone())){return Status::Fail}
  }
 }
 Status::Pass
}
fn defeat(p:&Packet)->Status{
 for b in &p.bridges{
  let xs:Vec<_>=p.defeats.iter().filter(|d|d.bridge==b.id).collect();
  if xs.is_empty(){return Status::Hold}
  if !xs.iter().any(|d|d.state=="REACHABLE"&&d.src==b.src&&d.dst==b.dst){return Status::Fail}
 }
 Status::Pass
}
fn assumptions(p:&Packet)->Status{
 let mut s=Status::Pass; let mut values:BTreeMap<&str,&str>=BTreeMap::new();
 for a in &p.assumptions{
  s=meet(s,a.status);
  if let Some(v)=values.get(a.key.as_str()){if *v!=a.value.as_str(){return Status::Fail}}
  else{values.insert(a.key.as_str(),a.value.as_str());}
 }
 s
}
fn local(p:&Packet)->Status{p.bridges.iter().fold(Status::Pass,|a,b|meet(a,meet(b.local,b.custody)))}
fn global_nonamp(p:&Packet)->Status{
 let mut ceiling=p.source_authority.unwrap();
 for a in &p.ancestors{ceiling=meet(ceiling,a.status)}
 for a in &p.assumptions{ceiling=meet(ceiling,a.status)}
 if p.final_authority.unwrap()>ceiling{Status::Fail}else if p.final_authority.unwrap()<ceiling{Status::Pass}else{Status::Pass}
}
fn direct(p:&Packet)->Status{p.direct.unwrap_or(Status::Hold)}

fn derive(p:&Packet)->BTreeMap<&'static str,Status>{
 let mut d=BTreeMap::new();
 d.insert("endpoint",endpoint(p)); d.insert("semantic",semantic(p)); d.insert("scope",scope(p));
 d.insert("ancestry",ancestry(p)); d.insert("defeat",defeat(p)); d.insert("assumption",assumptions(p));
 d.insert("local",local(p)); d.insert("global_nonamplification",global_nonamp(p)); d.insert("direct",direct(p));
 let mut c=Status::Pass;
 for k in ["endpoint","semantic","scope","ancestry","defeat","assumption","local","global_nonamplification","direct"]{c=meet(c,d[k]);}
 d.insert("composition",c); d
}

fn canonical(p:&Packet,d:&BTreeMap<&'static str,Status>)->String{
 let mut o=vec!["REAL-COMPOSITION=0.6".into(),format!("id={}",p.id),format!("source_authority={}",p.source_authority.unwrap().text()),format!("final_authority={}",p.final_authority.unwrap().text())];
 for k in ["endpoint","semantic","scope","ancestry","defeat","assumption","local","global_nonamplification","direct","composition"]{o.push(format!("coordinate.{k}={}",d[k].text()));}
 o.push("composition.meaning=CONDITIONAL_PATHWISE_NONAMPLIFICATION".into());
 o.push("local_pass_does_not_imply_composite_pass=true".into());
 o.push("adjacent_pass_does_not_imply_direct_pass=true".into());
 o.push("algebraic_composability_is_not_epistemic_composability=true".into());
 o.push("final_truth_distance=UNIDENTIFIED".into());
 o.join("\n")+"\n"
}

fn main(){
 let args:Vec<String>=env::args().skip(1).collect(); if args.is_empty(){eprintln!("usage: real-v06-compose PACKET...");std::process::exit(2)}
 for a in args{
  match parse(Path::new(&a)){
   Ok(p)=>{let d=derive(&p);let req=p.requested.unwrap();if req>d["composition"]{eprintln!("COMPOSITION_LAUNDERING: requested {} above derived {}",req.text(),d["composition"].text());std::process::exit(1)}print!("{}",canonical(&p,&d));}
   Err(e)=>{eprintln!("{e}");std::process::exit(1)}
  }
 }
}
