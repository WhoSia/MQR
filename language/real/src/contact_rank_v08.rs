use std::{collections::{BTreeMap,BTreeSet},env,fs,path::Path};

#[derive(Clone,Debug)]
struct Root{id:String,kind:String,fresh:String,cost:u64}
#[derive(Default,Debug)]
struct Packet{
    id:String,claim_scope:String,frontier:String,query_class:String,
    roots:BTreeMap<String,Root>,obligations:BTreeSet<String>,
    separates:BTreeSet<(String,String)>,
    expect_rank:Option<String>,expect_unique:Option<String>,expect_exchange:Option<String>,
}
fn toks(s:&str)->Vec<String>{s.split_whitespace().map(|x|x.trim_matches('"').to_string()).collect()}
fn parse(path:&Path)->Result<Packet,String>{
    let text=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut p=Packet::default(); let mut started=false; let mut ended=false;
    for (i,raw) in text.lines().enumerate(){
        let line=raw.trim(); if line.is_empty()||line.starts_with('#'){continue}
        let t=toks(line); if t.is_empty(){continue}
        if t[0]=="REALCONTACTRANK"{
            if t.len()!=2||t[1]!="0.8"{return Err("expected REALCONTACTRANK 0.8".into())}
            started=true;continue
        }
        if !started{return Err("packet must begin REALCONTACTRANK 0.8".into())}
        if t[0]=="END"{ended=true;break}
        match t[0].as_str(){
            "id" if t.len()==2=>p.id=t[1].clone(),
            "claim_scope" if t.len()==2=>p.claim_scope=t[1].clone(),
            "frontier" if t.len()==2=>p.frontier=t[1].clone(),
            "query_class" if t.len()==2=>p.query_class=t[1].clone(),
            "root" if t.len()==4=>{
                let kind=t[2].to_uppercase(); let fresh=t[3].to_uppercase();
                if !["EXTERNAL","INTERNAL"].contains(&kind.as_str()){return Err(format!("invalid root kind {kind}"))}
                if !["LIVE","STALE","EXPIRED"].contains(&fresh.as_str()){return Err(format!("invalid freshness {fresh}"))}
                p.roots.insert(t[1].clone(),Root{id:t[1].clone(),kind,fresh,cost:1});
            }
            "cost" if t.len()==3=>{
                let c=t[2].parse::<u64>().map_err(|_|format!("invalid cost {}",t[2]))?;
                let Some(r)=p.roots.get_mut(&t[1]) else{return Err(format!("unknown root {}",t[1]))};
                r.cost=c;
            }
            "obligation" if t.len()==2=>{p.obligations.insert(t[1].clone());},
            "separates" if t.len()==3=>{p.separates.insert((t[1].clone(),t[2].clone()));},
            "authorize_rank" if t.len()==2=>p.expect_rank=Some(t[1].to_uppercase()),
            "authorize_unique" if t.len()==2=>p.expect_unique=Some(t[1].to_uppercase()),
            "authorize_exchange" if t.len()==2=>p.expect_exchange=Some(t[1].to_uppercase()),
            _=>return Err(format!("{}:{} malformed command: {line}",path.display(),i+1)),
        }
    }
    if !ended{return Err("missing END".into())}
    if p.id.is_empty()||p.claim_scope.is_empty()||p.frontier.is_empty()||p.query_class.is_empty()||p.roots.is_empty()||p.obligations.is_empty(){return Err("missing required field".into())}
    for (r,o) in &p.separates{
        if !p.roots.contains_key(r){return Err(format!("unknown root in separates: {r}"))}
        if !p.obligations.contains(o){return Err(format!("unknown obligation in separates: {o}"))}
    }
    Ok(p)
}
fn eligible(p:&Packet)->Vec<String>{
    let mut v:Vec<_>=p.roots.values().filter(|r|r.kind=="EXTERNAL"&&r.fresh=="LIVE").map(|r|r.id.clone()).collect();
    v.sort();v
}
fn covers(p:&Packet,b:&[String])->bool{
    p.obligations.iter().all(|o|b.iter().any(|r|p.separates.contains(&(r.clone(),o.clone()))))
}
fn combinations(items:&[String],k:usize)->Vec<Vec<String>>{
    fn rec(items:&[String],k:usize,start:usize,cur:&mut Vec<String>,out:&mut Vec<Vec<String>>){
        if cur.len()==k{out.push(cur.clone());return}
        let need=k-cur.len(); if items.len().saturating_sub(start)<need{return}
        for i in start..items.len(){cur.push(items[i].clone());rec(items,k,i+1,cur,out);cur.pop();}
    }
    let mut out=Vec::new(); rec(items,k,0,&mut Vec::new(),&mut out); out
}
fn minimum_bases(p:&Packet)->Vec<Vec<String>>{
    let roots=eligible(p); if roots.len()>24{return Vec::new()}
    for k in 0..=roots.len(){
        let good:Vec<_>=combinations(&roots,k).into_iter().filter(|b|covers(p,b)).collect();
        if !good.is_empty(){return good}
    }
    Vec::new()
}
fn replacement(mut b:Vec<String>,remove:&str,add:&str)->Vec<String>{
    b.retain(|x|x!=remove);b.push(add.to_string());b.sort();b.dedup();b
}
fn exchange_property(bases:&[Vec<String>])->&'static str{
    if bases.is_empty(){return "UNAVAILABLE"} if bases.len()==1{return "VACUOUS"}
    let set:BTreeSet<Vec<String>>=bases.iter().cloned().collect();
    for b1 in bases{for b2 in bases{
        if b1==b2{continue}
        for a in b1.iter().filter(|x|!b2.contains(x)){
            let mut found=false;
            for x in b2.iter().filter(|x|!b1.contains(x)){
                if set.contains(&replacement(b1.clone(),a,x)){found=true;break}
            }
            if !found{return "FAIL"}
        }
    }}
    "PASS"
}
fn basis_cost(p:&Packet,b:&[String])->u64{b.iter().map(|r|p.roots[r].cost).sum()}
fn analyze(p:&Packet)->BTreeMap<String,String>{
    let bases=minimum_bases(p);let mut a=BTreeMap::new();
    a.insert("rank.coverage_complete".into(),if bases.is_empty(){"FAIL"}else{"PASS"}.into());
    if bases.is_empty(){
        for (k,v) in [("rank.minimum","UNCOVERED"),("rank.basis_count","0"),("rank.unique","NO"),("rank.exchange_property","UNAVAILABLE"),("rank.minimum_basis_cost_min","UNAVAILABLE"),("rank.minimum_basis_cost_max","UNAVAILABLE"),("rank.minimum_bases","")]{a.insert(k.into(),v.into());}
    }else{
        let costs:Vec<_>=bases.iter().map(|b|basis_cost(p,b)).collect();
        a.insert("rank.minimum".into(),bases[0].len().to_string());
        a.insert("rank.basis_count".into(),bases.len().to_string());
        a.insert("rank.unique".into(),if bases.len()==1{"YES"}else{"NO"}.into());
        a.insert("rank.exchange_property".into(),exchange_property(&bases).into());
        a.insert("rank.minimum_basis_cost_min".into(),costs.iter().min().unwrap().to_string());
        a.insert("rank.minimum_basis_cost_max".into(),costs.iter().max().unwrap().to_string());
        a.insert("rank.minimum_bases".into(),bases.iter().map(|b|b.join("+")).collect::<Vec<_>>().join(";"));
    }
    a.insert("rank.obligation_count".into(),p.obligations.len().to_string());
    a.insert("rank.eligible_root_count".into(),eligible(p).len().to_string());
    for (k,v) in [("rank.frontier_relative","true"),("rank.instrument_relative","true"),("rank.ontic_dimension","false"),("rank.degree_ontology_primitive","false"),("rank.cost_objective","SEPARATE"),("rank.open_world_final","false"),("rank.common_cause_independence_inferred","false"),("rank.calibration_authority_inferred","false"),("rank.selection_history_sufficiency_inferred","false"),("rank.decision_warrant_inferred","false"),("rank.evaluation_contract_authority_inferred","false")]{a.insert(k.into(),v.into());}
    a
}
fn validate(p:&Packet,a:&BTreeMap<String,String>)->Result<(),String>{
    if let Some(x)=&p.expect_rank{if a["rank.minimum"]!=*x{return Err(format!("RANK_MISMATCH expected {x} got {}",a["rank.minimum"]))}}
    if let Some(x)=&p.expect_unique{if a["rank.unique"]!=*x{return Err(format!("UNIQUE_MISMATCH expected {x} got {}",a["rank.unique"]))}}
    if let Some(x)=&p.expect_exchange{if a["rank.exchange_property"]!=*x{return Err(format!("EXCHANGE_MISMATCH expected {x} got {}",a["rank.exchange_property"]))}}
    Ok(())
}
fn emit(p:&Packet,a:&BTreeMap<String,String>)->String{
    let mut s=format!("REAL-CONTACT-RANK=0.8\nid={}\nclaim_scope={}\nfrontier={}\nquery_class={}\n",p.id,p.claim_scope,p.frontier,p.query_class);
    for k in ["rank.coverage_complete","rank.minimum","rank.basis_count","rank.unique","rank.exchange_property","rank.minimum_basis_cost_min","rank.minimum_basis_cost_max","rank.minimum_bases","rank.obligation_count","rank.eligible_root_count","rank.frontier_relative","rank.instrument_relative","rank.ontic_dimension","rank.degree_ontology_primitive","rank.cost_objective","rank.open_world_final","rank.common_cause_independence_inferred","rank.calibration_authority_inferred","rank.selection_history_sufficiency_inferred","rank.decision_warrant_inferred","rank.evaluation_contract_authority_inferred"]{s.push_str(&format!("{k}={}\n",a[k]));}
    s.push_str("rank.meaning=FROZEN_FRONTIER_MINIMUM_EXTERNAL_DISCRIMINATION_COVER\nminimum_rank_does_not_identify_obligation_ontology=true\nminimum_rank_does_not_select_best_cost_or_robustness_basis=true\nfinal_truth_distance=UNIDENTIFIED\n");s
}
fn main(){
    let args:Vec<String>=env::args().skip(1).collect();if args.is_empty(){std::process::exit(2)}
    for f in args{match parse(Path::new(&f)){Ok(p)=>{let a=analyze(&p);if let Err(e)=validate(&p,&a){eprintln!("{e}");std::process::exit(1)}print!("{}",emit(&p,&a));},Err(e)=>{eprintln!("{e}");std::process::exit(1)}}}
}
