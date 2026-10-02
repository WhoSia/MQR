use std::{env,fs};

fn yn(b:bool)->&'static str{if b{"YES"}else{"NO"}}
fn one(slot:&mut Option<String>,v:&str,name:&str)->Result<(),String>{
    if slot.is_some(){return Err(format!("duplicate {name}"));}
    *slot=Some(v.to_string()); Ok(())
}
fn main(){if let Err(e)=run(){eprintln!("REALPROGRESS_ERROR {e}");std::process::exit(2);}}
fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v20-progress <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut header=false; let mut ended=false;
    let mut id=None; let mut chart=None; let mut checkpoint=None; let mut batching=None;
    let mut parameter=None; let mut obligation=None; let mut loop_mode=None;
    let mut path_order=None; let mut local_structure=None; let mut magnitude=None;
    let mut continuation=None; let mut reopening=None;

    for(ln,raw) in src.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        if ended{return Err(format!("content after END at line {}",ln+1));}
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header{
            if t.as_slice()==["REALPROGRESS","0.20"]{header=true;continue;}
            return Err(format!("expected REALPROGRESS 0.20 at line {}",ln+1));
        }
        match t[0]{
            "END" if t.len()==1=>ended=true,
            "id" if t.len()==2=>one(&mut id,t[1],"id")?,
            "chart" if t.len()==2=>{
                if !matches!(t[1],"STATISTICAL"|"EXPERIMENT"|"OBLIGATION"|"CAUSAL"|"MODE"|"OTHER"){return Err("bad chart".into());}
                one(&mut chart,t[1],"chart")?;
            }
            "inert_checkpoint" if t.len()==2=>{
                if !matches!(t[1],"QUOTIENT"|"MATERIAL"){return Err("bad inert_checkpoint".into());}
                one(&mut checkpoint,t[1],"inert_checkpoint")?;
            }
            "evidence_batching" if t.len()==2=>{
                if !matches!(t[1],"QUOTIENT"|"MATERIAL"){return Err("bad evidence_batching".into());}
                one(&mut batching,t[1],"evidence_batching")?;
            }
            "parameter_recode" if t.len()==2=>{
                if !matches!(t[1],"QUOTIENT"|"MATERIAL"){return Err("bad parameter_recode".into());}
                one(&mut parameter,t[1],"parameter_recode")?;
            }
            "obligation_partition" if t.len()==2=>{
                if !matches!(t[1],"QUOTIENT"|"MATERIAL"){return Err("bad obligation_partition".into());}
                one(&mut obligation,t[1],"obligation_partition")?;
            }
            "path_loop" if t.len()==2=>{
                if !matches!(t[1],"QUOTIENT"|"MATERIAL"){return Err("bad path_loop".into());}
                one(&mut loop_mode,t[1],"path_loop")?;
            }
            "path_order" if t.len()==2=>{
                if !matches!(t[1],"COMMUTATIVE"|"NONCOMMUTATIVE"|"UNKNOWN"){return Err("bad path_order".into());}
                one(&mut path_order,t[1],"path_order")?;
            }
            "local_structure" if t.len()==2=>{
                if !matches!(t[1],"METRIC"|"PARTIAL_ORDER"|"PREORDER"|"ADMISSIBLE_REGION"|"NONE"){return Err("bad local_structure".into());}
                one(&mut local_structure,t[1],"local_structure")?;
            }
            "magnitude_transport" if t.len()==2=>{
                if !matches!(t[1],"LICENSED"|"UNLICENSED"){return Err("bad magnitude_transport".into());}
                one(&mut magnitude,t[1],"magnitude_transport")?;
            }
            "continuation_value" if t.len()==2=>{
                if !matches!(t[1],"SEPARATE"|"COLLAPSED"){return Err("bad continuation_value".into());}
                one(&mut continuation,t[1],"continuation_value")?;
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
    let chart=chart.ok_or("missing chart")?;
    let checkpoint=checkpoint.ok_or("missing inert_checkpoint")?;
    let batching=batching.ok_or("missing evidence_batching")?;
    let parameter=parameter.ok_or("missing parameter_recode")?;
    let obligation=obligation.ok_or("missing obligation_partition")?;
    let loop_mode=loop_mode.ok_or("missing path_loop")?;
    let path_order=path_order.ok_or("missing path_order")?;
    let local_structure=local_structure.ok_or("missing local_structure")?;
    let magnitude=magnitude.ok_or("missing magnitude_transport")?;
    let continuation=continuation.ok_or("missing continuation_value")?;
    let reopening=reopening.ok_or("missing reopening")?;

    let quotient_complete=[&checkpoint,&batching,&parameter,&obligation,&loop_mode]
        .iter().all(|x| x.as_str()=="QUOTIENT");
    let noncommuting_preserved=path_order!="UNKNOWN";
    let local_geometry=local_structure!="NONE";
    let atlas_admissible=quotient_complete && noncommuting_preserved && local_geometry
        && continuation=="SEPARATE" && reopening=="ACTIVE";
    let magnitude_default=if magnitude=="LICENSED"{"LICENSED_LOCAL"}else{"NO"};
    let scalar_stop=if continuation=="SEPARATE"{"REJECT"}else{"INVALID_COLLAPSE"};

    println!("progress.chart={chart}");
    println!("progress.inert_checkpoint={checkpoint}");
    println!("progress.evidence_batching={batching}");
    println!("progress.parameter_recode={parameter}");
    println!("progress.obligation_partition={obligation}");
    println!("progress.path_loop={loop_mode}");
    println!("progress.path_order={path_order}");
    println!("progress.local_structure={local_structure}");
    println!("progress.magnitude_transport={magnitude}");
    println!("progress.continuation_value={continuation}");
    println!("progress.reopening={reopening}");
    println!("progress.inert_quotient_complete={}",yn(quotient_complete));
    println!("progress.noncommuting_path_preserved={}",yn(noncommuting_preserved));
    println!("progress.local_geometry_admitted={}",yn(local_geometry));
    println!("progress.atlas_admissible={}",yn(atlas_admissible));
    println!("progress.global_scalar=REJECT");
    println!("progress.cross_domain_magnitude_default={magnitude_default}");
    println!("progress.progress_equals_promotion=NO");
    println!("progress.scalar_threshold_stop={scalar_stop}");
    println!("progress.truth_distance_inferred=NO");
    println!("progress.final_geometry_complete=NO");
    println!("progress.guidance_mode=GLOBAL_META_LOCAL_GEOMETRY");
    Ok(())
}
