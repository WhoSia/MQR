use std::{env,fs};

fn put(slot:&mut Option<String>,v:&str,name:&str)->Result<(),String>{
    if slot.is_some(){return Err(format!("duplicate {name}"));}
    *slot=Some(v.to_string()); Ok(())
}
fn yn(b:bool)->&'static str{if b{"YES"}else{"NO"}}

fn main(){ if let Err(e)=run(){eprintln!("REALVALUE_ERROR {e}"); std::process::exit(2);} }

fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v23-value <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut header=false; let mut ended=false;
    let mut id=None; let mut target=None; let mut typed=None; let mut provenance=None;
    let mut proxy=None; let mut drift=None; let mut decoy=None; let mut opportunity=None;
    let mut unit=None; let mut horizon=None; let mut optionv=None; let mut exterior=None;
    let mut reopening=None; let mut optimizer=None; let mut scalar=None; let mut world=None;

    for (ln,raw) in src.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        if ended{return Err(format!("content after END at line {}",ln+1));}
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header{
            if t.as_slice()==["REALVALUE","0.23"]{header=true;continue;}
            return Err(format!("expected REALVALUE 0.23 at line {}",ln+1));
        }
        match t[0]{
            "END" if t.len()==1=>ended=true,
            "id" if t.len()==2=>put(&mut id,t[1],"id")?,
            "target_contract" if t.len()==2=>{
                if !matches!(t[1],"DECLARED"|"HOLD"){return Err("bad target_contract".into());}
                put(&mut target,t[1],"target_contract")?;
            }
            "typed_value_profile" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"){return Err("bad typed_value_profile".into());}
                put(&mut typed,t[1],"typed_value_profile")?;
            }
            "value_provenance" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"|"UNKNOWN"){return Err("bad value_provenance".into());}
                put(&mut provenance,t[1],"value_provenance")?;
            }
            "proxy_dependence" if t.len()==2=>{
                if !matches!(t[1],"DECLARED"|"HIDDEN"){return Err("bad proxy_dependence".into());}
                put(&mut proxy,t[1],"proxy_dependence")?;
            }
            "target_drift_sentinel" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"ABSENT"){return Err("bad target_drift_sentinel".into());}
                put(&mut drift,t[1],"target_drift_sentinel")?;
            }
            "adversarial_decoy_test" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"HOLD"|"FAIL"){return Err("bad adversarial_decoy_test".into());}
                put(&mut decoy,t[1],"adversarial_decoy_test")?;
            }
            "opportunity_cost" if t.len()==2=>{
                if !matches!(t[1],"DECLARED"|"HOLD"){return Err("bad opportunity_cost".into());}
                put(&mut opportunity,t[1],"opportunity_cost")?;
            }
            "unit_audit" if t.len()==2=>{
                if !matches!(t[1],"PASS"|"FAIL"){return Err("bad unit_audit".into());}
                put(&mut unit,t[1],"unit_audit")?;
            }
            "horizon" if t.len()==2=>{
                if !matches!(t[1],"DECLARED"|"HOLD"){return Err("bad horizon".into());}
                put(&mut horizon,t[1],"horizon")?;
            }
            "option_value" if t.len()==2=>{
                if !matches!(t[1],"TRACKED"|"UNTRACKED"){return Err("bad option_value".into());}
                put(&mut optionv,t[1],"option_value")?;
            }
            "exterior_value_challenge" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"ABSENT"){return Err("bad exterior_value_challenge".into());}
                put(&mut exterior,t[1],"exterior_value_challenge")?;
            }
            "reopening" if t.len()==2=>{
                if !matches!(t[1],"ACTIVE"|"INACTIVE"){return Err("bad reopening".into());}
                put(&mut reopening,t[1],"reopening")?;
            }
            "optimizer_scope" if t.len()==2=>{
                if !matches!(t[1],"DECLARED_MODEL"|"NONE"|"WORLD"){return Err("bad optimizer_scope".into());}
                put(&mut optimizer,t[1],"optimizer_scope")?;
            }
            "scalar_default" if t.len()==2=>{
                if !matches!(t[1],"OFF"|"ON"){return Err("bad scalar_default".into());}
                put(&mut scalar,t[1],"scalar_default")?;
            }
            "world_optimum" if t.len()==2=>{
                if !matches!(t[1],"NO_CLAIM"|"CLAIMED"){return Err("bad world_optimum".into());}
                put(&mut world,t[1],"world_optimum")?;
            }
            _=>return Err(format!("unknown or malformed line {}: {}",ln+1,line)),
        }
    }
    if !header||!ended{return Err("missing header or END".into());}
    let _id=id.ok_or("missing id")?;
    let target=target.ok_or("missing target_contract")?;
    let typed=typed.ok_or("missing typed_value_profile")?;
    let provenance=provenance.ok_or("missing value_provenance")?;
    let proxy=proxy.ok_or("missing proxy_dependence")?;
    let drift=drift.ok_or("missing target_drift_sentinel")?;
    let decoy=decoy.ok_or("missing adversarial_decoy_test")?;
    let opportunity=opportunity.ok_or("missing opportunity_cost")?;
    let unit=unit.ok_or("missing unit_audit")?;
    let horizon=horizon.ok_or("missing horizon")?;
    let optionv=optionv.ok_or("missing option_value")?;
    let exterior=exterior.ok_or("missing exterior_value_challenge")?;
    let reopening=reopening.ok_or("missing reopening")?;
    let optimizer=optimizer.ok_or("missing optimizer_scope")?;
    let scalar=scalar.ok_or("missing scalar_default")?;
    let world=world.ok_or("missing world_optimum")?;

    let local=target=="DECLARED"&&typed=="PASS"&&provenance=="PASS"&&proxy=="DECLARED"
        &&drift=="ACTIVE"&&decoy=="PASS"&&opportunity=="DECLARED"&&unit=="PASS"
        &&horizon=="DECLARED"&&optionv=="TRACKED"&&exterior=="ACTIVE"&&reopening=="ACTIVE"
        &&optimizer!="WORLD"&&scalar=="OFF"&&world=="NO_CLAIM";

    let diagnosis=
        if target!="DECLARED"{"TARGET_CONTRACT_HOLD"}
        else if typed!="PASS"{"VALUE_PROFILE_COLLAPSE"}
        else if provenance!="PASS"{"VALUE_PROVENANCE_GAP"}
        else if proxy!="DECLARED"{"HIDDEN_PROXY_DEPENDENCE"}
        else if drift!="ACTIVE"{"TARGET_DRIFT_BLIND"}
        else if decoy!="PASS"{"DECOY_RESISTANCE_GAP"}
        else if opportunity!="DECLARED"{"OPPORTUNITY_COST_HOLD"}
        else if unit!="PASS"{"UNIT_RANK_REVERSAL"}
        else if horizon!="DECLARED"{"HORIZON_HOLD"}
        else if optionv!="TRACKED"{"OPTION_VALUE_BLIND"}
        else if exterior!="ACTIVE"{"VALUE_MODEL_SELF_INSULATION"}
        else if reopening!="ACTIVE"{"VALUE_REOPENING_FAILURE"}
        else if optimizer=="WORLD"{"WORLD_OPTIMIZER_OVERCLAIM"}
        else if scalar!="OFF"{"SCALAR_DEFAULT_ON"}
        else if world=="CLAIMED"{"WORLD_OPTIMUM_OVERCLAIM"}
        else{"LOCAL_EXPANSION_GUIDANCE_ADMISSIBLE"};

    println!("value.target_contract={target}");
    println!("value.typed_value_profile={typed}");
    println!("value.value_provenance={provenance}");
    println!("value.proxy_dependence={proxy}");
    println!("value.target_drift_sentinel={drift}");
    println!("value.adversarial_decoy_test={decoy}");
    println!("value.opportunity_cost={opportunity}");
    println!("value.unit_audit={unit}");
    println!("value.horizon={horizon}");
    println!("value.option_value={optionv}");
    println!("value.exterior_value_challenge={exterior}");
    println!("value.reopening={reopening}");
    println!("value.optimizer_scope={optimizer}");
    println!("value.scalar_default={scalar}");
    println!("value.world_optimum={world}");
    println!("value.local_guidance={}",yn(local));
    println!("value.diagnosis={diagnosis}");
    println!("value.universal_scientific_utility=REJECT");
    println!("value.value_constitution_self_authorizes=REJECT");
    println!("value.world_optimal_policy=NOT_EARNED");
    println!("value.wcepr={}",if local{"EARNED_LOCAL_CANDIDATE"}else{"HOLD"});
    Ok(())
}
