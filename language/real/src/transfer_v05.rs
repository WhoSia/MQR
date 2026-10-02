use std::{collections::{BTreeMap, BTreeSet}, env, fs, path::Path};

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Status { Fail, Hold, Pass }

impl Status {
    fn parse(s: &str) -> Result<Self,String> {
        match s {
            "FAIL" => Ok(Self::Fail),
            "HOLD" => Ok(Self::Hold),
            "PASS" => Ok(Self::Pass),
            _ => Err(format!("invalid status {s}")),
        }
    }
    fn as_str(self) -> &'static str {
        match self { Self::Fail=>"FAIL", Self::Hold=>"HOLD", Self::Pass=>"PASS" }
    }
}

#[derive(Clone, Debug)]
struct SemanticWitness {
    id: String,
    status: Status,
    warrant: String,
    world_predicate: String,
    formal_predicate: String,
    criterion: String,
}

#[derive(Clone, Debug)]
struct Ancestor {
    id: String,
    role: String,
    status: Status,
}

#[derive(Clone, Debug)]
struct DefeatPath {
    id: String,
    state: String,
    receipt: String,
}

#[derive(Default)]
struct Packet {
    id: String,
    mode: String,
    claim_scope: String,
    world_scope: String,
    statement_scope: String,
    world_authority: Option<Status>,
    scope_edges: Vec<(String,String)>,
    witnesses: Vec<SemanticWitness>,
    ancestors: Vec<Ancestor>,
    preserved: BTreeSet<String>,
    defeat_paths: Vec<DefeatPath>,
    formal_custody: String,
    formal_receipt: String,
    requested: String,
}

fn tokens(s: &str) -> Result<Vec<String>,String> {
    let mut out=Vec::new();
    let mut cur=String::new();
    let mut q=false;
    let mut esc=false;
    for ch in s.chars() {
        if esc { cur.push(ch); esc=false; continue; }
        if ch=='\\' { esc=true; continue; }
        if ch=='"' { q=!q; continue; }
        if ch.is_whitespace() && !q {
            if !cur.is_empty() { out.push(std::mem::take(&mut cur)); }
        } else { cur.push(ch); }
    }
    if esc || q { return Err("unterminated quote/escape".into()); }
    if !cur.is_empty() { out.push(cur); }
    Ok(out)
}

fn reachable(edges:&[(String,String)], sup:&str, sub:&str) -> bool {
    if sup==sub { return true; }
    let mut seen=BTreeSet::new();
    let mut stack=vec![sup.to_string()];
    while let Some(x)=stack.pop() {
        if !seen.insert(x.clone()) { continue; }
        for (a,b) in edges {
            if a==&x {
                if b==sub { return true; }
                stack.push(b.clone());
            }
        }
    }
    false
}

fn parse(path:&Path)->Result<Packet,String>{
    let text=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut p=Packet::default();
    let mut started=false;
    let mut ended=false;
    for (i,raw) in text.lines().enumerate() {
        let line=raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        let t=tokens(line).map_err(|e|format!("{}:{}: {e}",path.display(),i+1))?;
        if t.is_empty(){continue;}
        if t[0]=="REALTRANSFER" {
            if t.len()!=2 || t[1]!="0.5" { return Err("expected REALTRANSFER 0.5".into()); }
            started=true; continue;
        }
        if !started { return Err("packet must begin REALTRANSFER 0.5".into()); }
        if t[0]=="END" { ended=true; break; }
        match t[0].as_str() {
            "id" if t.len()==2 => p.id=t[1].clone(),
            "mode" if t.len()==2 => {
                let m=t[1].to_uppercase();
                if !["FORMAL_MEDIATED","NONFORMAL"].contains(&m.as_str()) { return Err(format!("invalid mode {m}")); }
                p.mode=m;
            }
            "claim_scope" if t.len()==2 => p.claim_scope=t[1].clone(),
            "world_scope" if t.len()==2 => p.world_scope=t[1].clone(),
            "statement_scope" if t.len()==2 => p.statement_scope=t[1].clone(),
            "world_authority" if t.len()==2 => p.world_authority=Some(Status::parse(&t[1].to_uppercase())?),
            "scope_contains" if t.len()==3 => p.scope_edges.push((t[1].clone(),t[2].clone())),
            "semantic_witness" if t.len()>=7 => {
                let status=Status::parse(&t[2].to_uppercase())?;
                let warrant=t[3].to_uppercase();
                if !["EXTERNAL","SELF","UNTESTED"].contains(&warrant.as_str()) { return Err(format!("invalid witness warrant {warrant}")); }
                p.witnesses.push(SemanticWitness{
                    id:t[1].clone(),status,warrant,
                    world_predicate:t[4].clone(),
                    formal_predicate:t[5].clone(),
                    criterion:t[6..].join(" "),
                });
            }
            "ancestor" if t.len()==4 => {
                let role=t[2].to_uppercase();
                if !["LOAD_BEARING","AUXILIARY"].contains(&role.as_str()) { return Err(format!("invalid ancestor role {role}")); }
                p.ancestors.push(Ancestor{id:t[1].clone(),role,status:Status::parse(&t[3].to_uppercase())?});
            }
            "preserve" if t.len()==2 => { p.preserved.insert(t[1].clone()); },
            "defeat_path" if t.len()>=4 => {
                let state=t[2].to_uppercase();
                if !["REACHABLE","DEAD","FORBIDDEN"].contains(&state.as_str()) { return Err(format!("invalid defeat state {state}")); }
                p.defeat_paths.push(DefeatPath{id:t[1].clone(),state,receipt:t[3..].join(" ")});
            }
            "formal_custody" if t.len()>=3 => {
                let state=t[1].to_uppercase();
                if !["PASS","HOLD","FAIL","NOT_APPLICABLE"].contains(&state.as_str()) { return Err(format!("invalid formal custody {state}")); }
                p.formal_custody=state;
                p.formal_receipt=t[2..].join(" ");
            }
            "authorize" if t.len()==2 => {
                let a=t[1].to_uppercase();
                if !["PASS","HOLD","FAIL","NOT_APPLICABLE"].contains(&a.as_str()) { return Err(format!("invalid authorization {a}")); }
                p.requested=a;
            }
            _ => return Err(format!("{}:{}: malformed command {line}",path.display(),i+1)),
        }
    }
    if !ended { return Err("missing END".into()); }
    if p.id.is_empty() || p.mode.is_empty() || p.claim_scope.is_empty() || p.world_scope.is_empty() || p.world_authority.is_none() || p.formal_custody.is_empty() || p.requested.is_empty() {
        return Err("missing required transfer field".into());
    }
    if p.mode=="FORMAL_MEDIATED" && p.statement_scope.is_empty() { return Err("FORMAL_MEDIATED requires statement_scope".into()); }
    Ok(p)
}

fn derived(p:&Packet)->Result<BTreeMap<&'static str,String>,String>{
    let mut out=BTreeMap::new();
    let world=p.world_authority.unwrap();

    let load:Vec<_>=p.ancestors.iter().filter(|a|a.role=="LOAD_BEARING").collect();
    if load.is_empty() { return Err("no LOAD_BEARING ancestry".into()); }
    let ancestry_ceiling=load.iter().map(|a|a.status).min().unwrap();
    if world>ancestry_ceiling {
        return Err(format!("WORLD_AUTHORITY_LAUNDERING: {} exceeds load-bearing ancestry ceiling {}",world.as_str(),ancestry_ceiling.as_str()));
    }

    if p.mode=="NONFORMAL" {
        if p.formal_custody!="NOT_APPLICABLE" { return Err("NONFORMAL requires formal_custody NOT_APPLICABLE".into()); }
        if p.requested!="NOT_APPLICABLE" { return Err("NONFORMAL transfer authorization must be NOT_APPLICABLE".into()); }
        out.insert("semantic","NOT_APPLICABLE".into());
        out.insert("scope", if reachable(&p.scope_edges,&p.world_scope,&p.claim_scope){"PASS"}else{"FAIL"}.into());
        out.insert("ancestry","NOT_APPLICABLE".into());
        out.insert("defeat","NOT_APPLICABLE".into());
        out.insert("noncircular","NOT_APPLICABLE".into());
        out.insert("formal_custody","NOT_APPLICABLE".into());
        out.insert("transfer","NOT_APPLICABLE".into());
        return Ok(out);
    }

    let semantic = if p.witnesses.is_empty() {
        "HOLD"
    } else if p.witnesses.iter().any(|w| w.status == Status::Fail) {
        "FAIL"
    } else if p.witnesses.iter().any(|w| w.status == Status::Hold) {
        "HOLD"
    } else {
        "PASS"
    };
    out.insert("semantic",semantic.into());

    let scope = if reachable(&p.scope_edges,&p.world_scope,&p.claim_scope)
        && reachable(&p.scope_edges,&p.statement_scope,&p.claim_scope) {"PASS"} else {"FAIL"};
    out.insert("scope",scope.into());

    let ancestry = if load.iter().all(|a|p.preserved.contains(&a.id)) {"PASS"} else {"FAIL"};
    out.insert("ancestry",ancestry.into());

    let defeat = if p.defeat_paths.iter().any(|d| d.state == "REACHABLE") {
        "PASS"
    } else if p.defeat_paths.iter().any(|d| d.state == "DEAD" || d.state == "FORBIDDEN") {
        "FAIL"
    } else {
        "HOLD"
    };
    out.insert("defeat",defeat.into());

    let noncircular = if p.witnesses.iter().any(|w| w.warrant == "SELF") {
        "FAIL"
    } else if p.witnesses.is_empty() || p.witnesses.iter().any(|w| w.warrant == "UNTESTED") {
        "HOLD"
    } else {
        "PASS"
    };
    out.insert("noncircular",noncircular.into());

    let custody = match p.formal_custody.as_str() {
        "PASS"=>"PASS",
        "HOLD"=>"HOLD",
        "FAIL"=>"FAIL",
        _=>"FAIL",
    };
    out.insert("formal_custody",custody.into());

    let coords=[semantic,scope,ancestry,defeat,noncircular,custody];
    let contract = if coords.iter().all(|x|*x=="PASS") && world==Status::Pass {
        "PASS"
    } else if coords.iter().any(|x|*x=="FAIL") || world==Status::Fail {
        "FAIL"
    } else {
        "HOLD"
    };
    out.insert("transfer",contract.into());

    let req_rank=match p.requested.as_str(){"FAIL"=>0,"HOLD"=>1,"PASS"=>2,_=>return Err("FORMAL_MEDIATED authorization may not be NOT_APPLICABLE".into())};
    let got_rank=match contract{"FAIL"=>0,"HOLD"=>1,"PASS"=>2,_=>0};
    if req_rank>got_rank { return Err(format!("TRANSFER_LAUNDERING: requested {} above derived {contract}",p.requested)); }

    Ok(out)
}

fn esc(s:&str)->String{
    s.replace('\\',"\\\\").replace('\n',"\\n").replace('=',"\\=")
}

fn canonical(p:&Packet,d:&BTreeMap<&'static str,String>)->String{
    let mut o=Vec::new();
    o.push("REAL-TRANSFER=0.5".into());
    o.push(format!("id={}",esc(&p.id)));
    o.push(format!("mode={}",p.mode));
    o.push(format!("world_authority={}",p.world_authority.unwrap().as_str()));
    o.push(format!("scope.claim={}",esc(&p.claim_scope)));
    o.push(format!("scope.world={}",esc(&p.world_scope)));
    o.push(format!("scope.statement={}",if p.statement_scope.is_empty(){"NOT_APPLICABLE".into()}else{esc(&p.statement_scope)}));
    for k in ["semantic","scope","ancestry","defeat","noncircular","formal_custody","transfer"] {
        o.push(format!("coordinate.{k}={}",d[k]));
    }
    o.push(format!("requested.authorization={}",p.requested));
    o.push(format!("witness.count={}",p.witnesses.len()));
    for (i,w) in p.witnesses.iter().enumerate() {
        o.push(format!("witness.{i}.id={}",esc(&w.id)));
        o.push(format!("witness.{i}.status={}",w.status.as_str()));
        o.push(format!("witness.{i}.warrant={}",w.warrant));
        o.push(format!("witness.{i}.world={}",esc(&w.world_predicate)));
        o.push(format!("witness.{i}.formal={}",esc(&w.formal_predicate)));
        o.push(format!("witness.{i}.criterion={}",esc(&w.criterion)));
    }
    o.push(format!("ancestor.count={}",p.ancestors.len()));
    for (i,a) in p.ancestors.iter().enumerate() {
        o.push(format!("ancestor.{i}.id={}",esc(&a.id)));
        o.push(format!("ancestor.{i}.role={}",a.role));
        o.push(format!("ancestor.{i}.status={}",a.status.as_str()));
        o.push(format!("ancestor.{i}.preserved={}",p.preserved.contains(&a.id)));
    }
    o.push(format!("defeat_path.count={}",p.defeat_paths.len()));
    for (i,x) in p.defeat_paths.iter().enumerate() {
        o.push(format!("defeat_path.{i}.id={}",esc(&x.id)));
        o.push(format!("defeat_path.{i}.state={}",x.state));
        o.push(format!("defeat_path.{i}.receipt={}",esc(&x.receipt)));
    }
    o.push(format!("formal_custody.receipt={}",esc(&p.formal_receipt)));
    o.push("transfer.meaning=STRUCTURAL_ADMISSIBILITY_NONAMPLIFYING".into());
    o.push("transfer.does_not_raise_world_authority=true".into());
    o.push("cross_language_agreement_is_not_world_correspondence=true".into());
    o.push("final_truth_distance=UNIDENTIFIED".into());
    o.join("\n")+"\n"
}

fn main(){
    let args:Vec<String>=env::args().skip(1).collect();
    if args.is_empty(){eprintln!("usage: real-v05-transfer PACKET...");std::process::exit(2);}
    let mut first=true;
    for a in args {
        match parse(Path::new(&a)).and_then(|p|derived(&p).map(|d|(p,d))) {
            Ok((p,d))=>{
                if !first{println!("---");}
                print!("{}",canonical(&p,&d));
                first=false;
            }
            Err(e)=>{eprintln!("{e}");std::process::exit(1);}
        }
    }
}
