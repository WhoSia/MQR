use std::{env,fs};

fn yes(b:bool)->&'static str{if b{"YES"}else{"NO"}}

fn main(){if let Err(e)=run(){eprintln!("REALTRACE_ERROR {e}");std::process::exit(2);}}

fn one<'a>(slot:&mut Option<String>,v:&str,name:&str)->Result<(),String>{
    if slot.is_some(){return Err(format!("duplicate {name}"));}
    *slot=Some(v.to_string()); Ok(())
}

fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v19-trace <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut header=false; let mut ended=false;
    let mut id=None; let mut source_cutoff=None; let mut mapping=None;
    let mut claim=None; let mut probe=None; let mut use_mode=None;
    let mut live=None; let mut criterion=None; let mut break_kind=None;
    let mut projection=None; let mut granularity=None; let mut window=None;
    let mut historical_action=None;

    for(ln,raw) in src.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        if ended{return Err(format!("content after END at line {}",ln+1));}
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header{
            if t.as_slice()==["REALTRACE","0.19"]{header=true;continue;}
            return Err(format!("expected REALTRACE 0.19 at line {}",ln+1));
        }
        match t[0]{
            "END" if t.len()==1=>ended=true,
            "id" if t.len()==2=>one(&mut id,t[1],"id")?,
            "source_cutoff" if t.len()==2=>one(&mut source_cutoff,t[1],"source_cutoff")?,
            "mapping" if t.len()==2=>{
                if !matches!(t[1],"EXACT"|"BOUNDED"|"PROXY"|"UNKNOWN"){return Err("bad mapping".into());}
                one(&mut mapping,t[1],"mapping")?;
            }
            "claim" if t.len()==2=>{
                if !matches!(t[1],"OPEN"|"RESTRICTED"|"FROZEN"){return Err("bad claim".into());}
                one(&mut claim,t[1],"claim")?;
            }
            "probe" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"PAUSED"|"HANDOFF"|"ARCHIVED"){return Err("bad probe".into());}
                one(&mut probe,t[1],"probe")?;
            }
            "use" if t.len()==2=>{
                if !matches!(t[1],"NONE"|"PROVISIONAL"|"AUTHORIZED"){return Err("bad use".into());}
                one(&mut use_mode,t[1],"use")?;
            }
            "live_obligation" if t.len()==2=>{
                if !matches!(t[1],"CLEAR"|"LIVE"|"BOUNDED"|"UNKNOWN"){return Err("bad live_obligation".into());}
                one(&mut live,t[1],"live_obligation")?;
            }
            "criterion" if t.len()==2=>{
                if !matches!(t[1],"AGREE"|"DISAGREE"|"UNKNOWN"){return Err("bad criterion".into());}
                one(&mut criterion,t[1],"criterion")?;
            }
            "break" if t.len()==2=>{
                if !matches!(t[1],"NONE"|"WORLD_CONTACT"|"DECISION_CONTRACT"|"PATH_CONFLICT"){return Err("bad break".into());}
                one(&mut break_kind,t[1],"break")?;
            }
            "projection" if t.len()==2=>{
                if !matches!(t[1],"UNIQUE"|"MULTI_MODE"|"NONE"){return Err("bad projection".into());}
                one(&mut projection,t[1],"projection")?;
            }
            "granularity" if t.len()==2=>{
                if !matches!(t[1],"REGULAR"|"IRREGULAR"|"UNKNOWN"){return Err("bad granularity".into());}
                one(&mut granularity,t[1],"granularity")?;
            }
            "stop_window" if t.len()==2=>{
                if !matches!(t[1],"IDENTIFIED"|"INTERVAL"|"LEFT_CENSORED"|"RIGHT_CENSORED"|"NONIDENTIFIABLE"){return Err("bad stop_window".into());}
                one(&mut window,t[1],"stop_window")?;
            }
            "historical_action" if t.len()==2=>{
                if !matches!(t[1],"CONTINUE_PROBING"|"CLAIM_FREEZE"|"PROVISIONAL_USE"|"ARCHIVE"|"HANDOFF"|"REOPEN"){return Err("bad historical_action".into());}
                one(&mut historical_action,t[1],"historical_action")?;
            }
            _=>return Err(format!("unknown or malformed line {}: {}",ln+1,line)),
        }
    }
    if !header||!ended{return Err("missing header or END".into());}
    let _id=id.ok_or("missing id")?;
    let source_cutoff=source_cutoff.ok_or("missing source_cutoff")?;
    let mapping=mapping.ok_or("missing mapping")?;
    let claim=claim.ok_or("missing claim")?;
    let probe=probe.ok_or("missing probe")?;
    let use_mode=use_mode.ok_or("missing use")?;
    let live=live.ok_or("missing live_obligation")?;
    let criterion=criterion.ok_or("missing criterion")?;
    let break_kind=break_kind.ok_or("missing break")?;
    let projection=projection.ok_or("missing projection")?;
    let granularity=granularity.ok_or("missing granularity")?;
    let window=window.ok_or("missing stop_window")?;
    let historical_action=historical_action.ok_or("missing historical_action")?;

    let admission=matches!(mapping.as_str(),"EXACT"|"BOUNDED") && live!="UNKNOWN" && criterion!="UNKNOWN";
    let projection_loss=projection!="UNIQUE";
    let reopen=break_kind!="NONE";
    let lag_transport=if granularity=="IRREGULAR"{"REJECT"}else{"NOT_ESTABLISHED"};
    let window_point=window=="IDENTIFIED";

    println!("trace.source_cutoff={source_cutoff}");
    println!("trace.mapping={mapping}");
    println!("trace.claim_mode={claim}");
    println!("trace.probe_mode={probe}");
    println!("trace.use_mode={use_mode}");
    println!("trace.live_obligation={live}");
    println!("trace.criterion={criterion}");
    println!("trace.break={break_kind}");
    println!("trace.projection={projection}");
    println!("trace.granularity={granularity}");
    println!("trace.stop_window={window}");
    println!("trace.historical_action={historical_action}");
    println!("trace.naturalistic_admission={}",yes(admission));
    println!("trace.binary_projection_loss={}",yes(projection_loss));
    println!("trace.reopen_required={}",yes(reopen));
    println!("trace.fixed_event_lag_transport={lag_transport}");
    println!("trace.point_window_identified={}",yes(window_point));
    println!("trace.unique_stop_time_inferred=NO");
    println!("trace.historical_action_truth_oracle=NO");
    println!("trace.naturalistic_retuning_lambda=NO");
    println!("trace.prospective_external_validation=NO");
    println!("trace.popperian_master_semantics=REJECT");
    println!("trace.world_contact_negative_only=NO");
    println!("trace.guidance_mode=MODE_RELATIVE_REOPENABLE_AUTHORITY");
    Ok(())
}
