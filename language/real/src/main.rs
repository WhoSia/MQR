use std::{collections::BTreeMap,env,fs,path::Path};

const VERSION:&str="0.2";
const GATES:[&str;4]=["C","E","P","R"];
const AXES:[&str;5]=["W","N","I","T","D"];

#[derive(Default)]
struct Packet{
    id:String, epoch:String, claim_type:String, claim_text:String, scope:String,
    gates:BTreeMap<String,String>,
    axes:BTreeMap<String,(f64,String)>,
    generators:Vec<(String,String)>,
    rivals:Vec<(String,String)>,
    residue:Vec<(String,String)>,
    mystery:Vec<(String,String)>,
    ontic:Vec<(String,String)>,
    successor:String,
    shocks:Vec<(String,String,String)>,
    sources:Vec<String>,
}

fn tokens(s:&str)->Result<Vec<String>,String>{
    let mut out=Vec::new(); let mut cur=String::new();
    let mut q=false; let mut esc=false;
    for ch in s.chars(){
        if esc { cur.push(ch); esc=false; continue; }
        if ch=='\\' { esc=true; continue; }
        if ch=='"' { q=!q; continue; }
        if ch.is_whitespace() && !q {
            if !cur.is_empty(){ out.push(std::mem::take(&mut cur)); }
        } else { cur.push(ch); }
    }
    if esc || q { return Err("unterminated quote/escape".into()); }
    if !cur.is_empty(){ out.push(cur); }
    Ok(out)
}

fn parse(path:&Path)->Result<Packet,String>{
    let text=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut p=Packet::default(); p.successor="VULNERABLE".into();
    let mut started=false; let mut ended=false;

    for (i,raw) in text.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty() || line.starts_with('#'){continue}
        let t=tokens(line).map_err(|e|format!("{}:{}: {}",path.display(),i+1,e))?;
        if t.is_empty(){continue}
        let cmd=t[0].as_str();

        if cmd.eq_ignore_ascii_case("REALPACKET"){
            if t.len()!=2 || t[1]!=VERSION {return Err(format!("{}:{}: expected REALPACKET {}",path.display(),i+1,VERSION))}
            started=true; continue
        }
        if !started{return Err(format!("{}:{}: packet must begin with REALPACKET {}",path.display(),i+1,VERSION))}
        if cmd.eq_ignore_ascii_case("END"){ended=true;break}

        match cmd {
            "id" if t.len()==2 => p.id=t[1].clone(),
            "epoch" if t.len()==2 => p.epoch=t[1].clone(),
            "claim" if t.len()>=3 => {p.claim_type=t[1].to_uppercase();p.claim_text=t[2..].join(" ");},
            "scope" if t.len()>=2 => p.scope=t[1..].join(" "),
            "gate" if t.len()==3 => {
                let g=t[1].to_uppercase(); let s=t[2].to_uppercase();
                if !GATES.contains(&g.as_str()) || !["PASS","HOLD","FAIL"].contains(&s.as_str()){return Err(format!("{}:{}: invalid gate",path.display(),i+1))}
                p.gates.insert(g,s);
            },
            "axis" if t.len()>=3 => {
                let a=t[1].to_uppercase();
                if !AXES.contains(&a.as_str()){return Err(format!("{}:{}: invalid axis",path.display(),i+1))}
                let v:f64=t[2].parse().map_err(|_|format!("{}:{}: axis must be numeric",path.display(),i+1))?;
                if !(0.0..=1.0).contains(&v){return Err(format!("{}:{}: axis outside [0,1]",path.display(),i+1))}
                p.axes.insert(a,(v,t[3..].join(" ")));
            },
            "generator" if t.len()>=3 => p.generators.push((t[1].to_uppercase(),t[2..].join(" "))),
            "rival" if t.len()>=3 => p.rivals.push((t[1].to_uppercase(),t[2..].join(" "))),
            "residue" if t.len()>=3 => p.residue.push((t[1].to_uppercase(),t[2..].join(" "))),
            "mystery" if t.len()>=3 => p.mystery.push((t[1].to_uppercase(),t[2..].join(" "))),
            "ontic" if t.len()>=3 => p.ontic.push((t[1].to_uppercase(),t[2..].join(" "))),
            "successor" if t.len()==2 => p.successor=t[1].to_uppercase(),
            "shock" if t.len()>=4 => p.shocks.push((t[1].clone(),t[2].to_uppercase(),t[3..].join(" "))),
            "source" if t.len()>=2 => p.sources.push(t[1..].join(" ")),
            _ => return Err(format!("{}:{}: malformed command: {}",path.display(),i+1,line)),
        }
    }
    if !ended{return Err(format!("{}: missing END",path.display()))}
    if p.id.is_empty()||p.epoch.is_empty()||p.claim_type.is_empty()||p.claim_text.is_empty()||p.scope.is_empty(){return Err(format!("{}: missing required field",path.display()))}
    for g in GATES{if !p.gates.contains_key(g){return Err(format!("{}: missing gate {}",path.display(),g))}}
    for a in AXES{if !p.axes.contains_key(a){return Err(format!("{}: missing axis {}",path.display(),a))}}
    Ok(p)
}

fn esc(s:&str)->String{s.replace('\\',"\\\\").replace('\n',"\\n").replace('=',"\\=")}

fn canonical(p:&Packet,scalar:bool)->String{
    let mut o=Vec::new();
    o.push("REAL-LANGUAGE=0.2".into());
    o.push(format!("id={}",esc(&p.id)));
    o.push(format!("epoch={}",esc(&p.epoch)));
    o.push(format!("claim.type={}",esc(&p.claim_type)));
    o.push(format!("claim.text={}",esc(&p.claim_text)));
    o.push(format!("scope={}",esc(&p.scope)));
    for g in GATES{o.push(format!("gate.{}={}",g,p.gates[g]));}
    for a in AXES{
        let (v,n)=&p.axes[a];
        o.push(format!("profile.{}={:.6}",a,v));
        o.push(format!("profile.{}.note={}",a,esc(n)));
    }
    let pass=GATES.iter().all(|g|p.gates[*g]=="PASS");
    o.push(format!("authority={}",if pass{"SCOPED_REALIST_AUTHORITY"}else{"HOLD"}));
    o.push("profile.order=PARETO_PARTIAL".into());
    o.push("profile.scalar.default=OFF".into());
    if scalar{
        let prod: f64=AXES.iter().map(|a|p.axes[*a].0).product();
        let gm=prod.powf(1.0/5.0);
        o.push(format!("display.scalar.geometric_mean={:.6}",gm));
        o.push("display.scalar.status=UNCALIBRATED_DISPLAY_ONLY".into());
    }
    o.push("open_world_residue=true".into());
    o.push("final_truth_distance=UNIDENTIFIED".into());
    o.push(format!("successor={}",p.successor));
    for (i,(k,d)) in p.generators.iter().enumerate(){o.push(format!("generator.{}.kind={}",i,k));o.push(format!("generator.{}.text={}",i,esc(d)));}
    for (i,(k,d)) in p.rivals.iter().enumerate(){o.push(format!("rival.{}.state={}",i,k));o.push(format!("rival.{}.text={}",i,esc(d)));}
    for (i,(k,d)) in p.residue.iter().enumerate(){o.push(format!("residue.{}.level={}",i,k));o.push(format!("residue.{}.text={}",i,esc(d)));}
    for (i,(k,d)) in p.mystery.iter().enumerate(){o.push(format!("mystery.{}.level={}",i,k));o.push(format!("mystery.{}.text={}",i,esc(d)));}
    for (i,(k,d)) in p.ontic.iter().enumerate(){o.push(format!("ontic.{}.state={}",i,k));o.push(format!("ontic.{}.text={}",i,esc(d)));}
    for (i,(e,k,d)) in p.shocks.iter().enumerate(){o.push(format!("shock.{}.epoch={}",i,esc(e)));o.push(format!("shock.{}.type={}",i,k));o.push(format!("shock.{}.text={}",i,esc(d)));}
    for (i,s) in p.sources.iter().enumerate(){o.push(format!("source.{}={}",i,esc(s)));}
    o.join("\n")+"\n"
}

fn main(){
    let mut args:Vec<String>=env::args().skip(1).collect();
    let scalar=if let Some(i)=args.iter().position(|x|x=="--diagnostic-scalar"){args.remove(i);true}else{false};
    if args.is_empty(){eprintln!("usage: real [--diagnostic-scalar] PACKET [PACKET ...]");std::process::exit(2)}
    let mut first=true;
    for a in args{
        match parse(Path::new(&a)){
            Ok(p)=>{
                if !first{print!("---\n")}
                print!("{}",canonical(&p,scalar)); first=false;
            },
            Err(e)=>{eprintln!("{e}");std::process::exit(1)}
        }
    }
}
