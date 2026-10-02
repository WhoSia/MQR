use std::{env,fs};

fn put(slot:&mut Option<String>,v:&str,name:&str)->Result<(),String>{
    if slot.is_some(){return Err(format!("duplicate {name}"));}
    *slot=Some(v.to_string()); Ok(())
}
fn yn(b:bool)->&'static str{if b{"YES"}else{"NO"}}

fn main(){
    if let Err(e)=run(){eprintln!("REALCONSEQUENCE_ERROR {e}");std::process::exit(2);}
}

fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v22-consequence <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut header=false; let mut ended=false;
    let mut id=None; let mut target=None; let mut typed=None; let mut ancestry=None;
    let mut common=None; let mut grammar=None; let mut off=None; let mut expansion=None;
    let mut serialization=None; let mut tacit=None; let mut heuristic=None;
    let mut holdout=None; let mut reopening=None; let mut world_complete=None;

    for(ln,raw) in src.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        if ended{return Err(format!("content after END at line {}",ln+1));}
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header{
            if t.as_slice()==["REALCONSEQUENCE","0.22"]{header=true;continue;}
            return Err(format!("expected REALCONSEQUENCE 0.22 at line {}",ln+1));
        }
        match t[0]{
            "END" if t.len()==1=>ended=true,
            "id" if t.len()==2=>put(&mut id,t[1],"id")?,
            "target" if t.len()==2=>{
                if !matches!(t[1],"PROGRESS"|"MEASUREMENT"|"CAUSAL"|"REPRESENTATION"|"OTHER"){return Err("bad target".into());}
                put(&mut target,t[1],"target")?;
            }
            "typed_channels" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"){return Err("bad typed_channels".into());}
                put(&mut typed,t[1],"typed_channels")?;
            }
            "ancestry_audit" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad ancestry_audit".into());}
                put(&mut ancestry,t[1],"ancestry_audit")?;
            }
            "common_mode" if t.len()==2=>{
                if !matches!(t[1],"YES"|"NO"|"UNKNOWN"){return Err("bad common_mode".into());}
                put(&mut common,t[1],"common_mode")?;
            }
            "generator_grammar" if t.len()==2=>{
                if !matches!(t[1],"DECLARED"|"HOLD"){return Err("bad generator_grammar".into());}
                put(&mut grammar,t[1],"generator_grammar")?;
            }
            "off_grammar_route" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"ABSENT"){return Err("bad off_grammar_route".into());}
                put(&mut off,t[1],"off_grammar_route")?;
            }
            "adversarial_expansion" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"HOLD"|"FAIL"){return Err("bad adversarial_expansion".into());}
                put(&mut expansion,t[1],"adversarial_expansion")?;
            }
            "serialization_quotient" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"){return Err("bad serialization_quotient".into());}
                put(&mut serialization,t[1],"serialization_quotient")?;
            }
            "tacit_competence" if t.len()==2=>{
                if !matches!(t[1],"VERIFIED"|"RECONSTRUCTIBLE"|"MISSING"|"NA"){return Err("bad tacit_competence".into());}
                put(&mut tacit,t[1],"tacit_competence")?;
            }
            "heuristic_role" if t.len()==2=>{
                if !matches!(t[1],"GENERATE_ONLY"|"SELF_AUTHORIZING"|"NONE"){return Err("bad heuristic_role".into());}
                put(&mut heuristic,t[1],"heuristic_role")?;
            }
            "holdout" if t.len()==2=>{
                if !matches!(t[1],"AVAILABLE"|"UNAVAILABLE_JUSTIFIED"|"ABSENT"){return Err("bad holdout".into());}
                put(&mut holdout,t[1],"holdout")?;
            }
            "reopening" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"INACTIVE"){return Err("bad reopening".into());}
                put(&mut reopening,t[1],"reopening")?;
            }
            "world_complete" if t.len()==2=>{
                if !matches!(t[1],"NO_CLAIM"|"CLAIMED"){return Err("bad world_complete".into());}
                put(&mut world_complete,t[1],"world_complete")?;
            }
            _=>return Err(format!("unknown or malformed line {}: {}",ln+1,line)),
        }
    }
    if !header||!ended{return Err("missing header or END".into());}
    let _id=id.ok_or("missing id")?;
    let target=target.ok_or("missing target")?;
    let typed=typed.ok_or("missing typed_channels")?;
    let ancestry=ancestry.ok_or("missing ancestry_audit")?;
    let common=common.ok_or("missing common_mode")?;
    let grammar=grammar.ok_or("missing generator_grammar")?;
    let off=off.ok_or("missing off_grammar_route")?;
    let expansion=expansion.ok_or("missing adversarial_expansion")?;
    let serialization=serialization.ok_or("missing serialization_quotient")?;
    let tacit=tacit.ok_or("missing tacit_competence")?;
    let heuristic=heuristic.ok_or("missing heuristic_role")?;
    let holdout=holdout.ok_or("missing holdout")?;
    let reopening=reopening.ok_or("missing reopening")?;
    let world_complete=world_complete.ok_or("missing world_complete")?;

    let local=typed=="PASS"&&ancestry=="PASS"&&common=="NO"&&grammar=="DECLARED"
        &&off=="ACTIVE"&&expansion=="PASS"&&serialization=="PASS"
        &&tacit!="MISSING"&&heuristic!="SELF_AUTHORIZING"
        &&holdout!="ABSENT"&&reopening=="ACTIVE"&&world_complete=="NO_CLAIM";

    let diagnosis=
        if typed=="FAIL"{"CHANNEL_COLLAPSE"}
        else if ancestry!="PASS"{"ANCESTRY_AUDIT_GAP"}
        else if common=="YES"{"COMMON_MODE_CAPTURE"}
        else if grammar!="DECLARED"{"GENERATOR_GRAMMAR_HOLD"}
        else if off!="ACTIVE"{"GENERATOR_CLOSURE_MIRAGE"}
        else if expansion!="PASS"{"ADVERSARIAL_EXPANSION_GAP"}
        else if serialization!="PASS"{"SERIALIZATION_INFLATION"}
        else if tacit=="MISSING"{"COMPETENCE_GAP"}
        else if heuristic=="SELF_AUTHORIZING"{"HEURISTIC_SELF_AUTHORITY"}
        else if holdout=="ABSENT"{"HOLDOUT_GAP"}
        else if reopening!="ACTIVE"{"REOPENING_FAILURE"}
        else if world_complete=="CLAIMED"{"WORLD_COMPLETENESS_OVERCLAIM"}
        else{"OPEN_LOCAL_ADMISSIBLE"};

    println!("consequence.target={target}");
    println!("consequence.typed_channels={typed}");
    println!("consequence.ancestry_audit={ancestry}");
    println!("consequence.common_mode={common}");
    println!("consequence.generator_grammar={grammar}");
    println!("consequence.off_grammar_route={off}");
    println!("consequence.adversarial_expansion={expansion}");
    println!("consequence.serialization_quotient={serialization}");
    println!("consequence.tacit_competence={tacit}");
    println!("consequence.heuristic_role={heuristic}");
    println!("consequence.holdout={holdout}");
    println!("consequence.reopening={reopening}");
    println!("consequence.world_complete={world_complete}");
    println!("consequence.local_adequacy={}",yn(local));
    println!("consequence.diagnosis={diagnosis}");
    println!("consequence.self_certifying_family=REJECT");
    println!("consequence.formal_rigor_implies_family_completeness=REJECT");
    println!("consequence.intuition_self_authorizes=REJECT");
    println!("consequence.more_tests_implies_more_authority=REJECT");
    println!("consequence.world_family_complete=NO");
    println!("consequence.wccfr={}",if local{"EARNED_LOCAL_CANDIDATE"}else{"HOLD"});
    Ok(())
}
