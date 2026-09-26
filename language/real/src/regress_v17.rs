use std::{collections::{HashMap,HashSet}, env, fs};

#[derive(Clone)]
struct Refinement { id:String, status:String, effect:String }
#[derive(Clone)]
struct Criterion { id:String, timing:String, ancestry:String }
#[derive(Clone)]
struct Debt { materiality:String, status:String }

fn yes(b:bool)->&'static str { if b {"YES"} else {"NO"} }

fn main() {
    if let Err(e)=run() {
        eprintln!("REALREGRESS_ERROR {e}");
        std::process::exit(2);
    }
}

fn run()->Result<(),String>{
    let path=env::args().nth(1).ok_or("usage: real-v17-regress <file>")?;
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;

    let mut header=false;
    let mut ended=false;
    let mut id:Option<String>=None;
    let mut scope:Option<String>=None;
    let mut scope_timing:Option<String>=None;
    let mut scope_nonvacuous:Option<bool>=None;
    let mut challenges:Vec<String>=vec![];
    let mut contacts:Vec<String>=vec![];
    let mut decision:Option<String>=None;
    let mut action_invariant:Option<bool>=None;
    let mut decision_change=false;
    let mut stability_rounds:u32=0;
    let mut refinements:Vec<Refinement>=vec![];
    let mut criteria:Vec<Criterion>=vec![];
    let mut verdicts:Vec<(String,String,String)>=vec![];
    let mut debts:Vec<Debt>=vec![];
    let mut paths:Vec<(String,String)>=vec![];
    let mut new_contacts:Vec<(String,String)>=vec![];
    let mut new_criteria:Vec<(String,String)>=vec![];

    for (ln,raw) in src.lines().enumerate() {
        let line=raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if ended { return Err(format!("content after END at line {}",ln+1)); }
        let t:Vec<&str>=line.split_whitespace().collect();
        if !header {
            if t.as_slice()==["REALREGRESS","0.17"] { header=true; continue; }
            return Err(format!("expected REALREGRESS 0.17 at line {}",ln+1));
        }
        match t[0] {
            "END" if t.len()==1 => { ended=true; }
            "id" if t.len()==2 => {
                if id.is_some(){return Err("duplicate id".into());}
                id=Some(t[1].into());
            }
            "claim_scope" if t.len()==2 => {
                if scope.is_some(){return Err("duplicate claim_scope".into());}
                scope=Some(t[1].into());
            }
            "scope_timing" if t.len()==2 => {
                if scope_timing.is_some(){return Err("duplicate scope_timing".into());}
                if !matches!(t[1],"FROZEN"|"PROSPECTIVE_REVISION"|"POST_OUTCOME_REVISION"){return Err("bad scope_timing".into());}
                scope_timing=Some(t[1].into());
            }
            "scope_nonvacuous" if t.len()==2 => {
                if scope_nonvacuous.is_some(){return Err("duplicate scope_nonvacuous".into());}
                scope_nonvacuous=Some(parse_bool(t[1])?);
            }
            "challenge" if t.len()==2 => challenges.push(t[1].into()),
            "world_contact" if t.len()==2 => contacts.push(t[1].into()),
            "decision_contract" if t.len()==2 => {
                if decision.is_some(){return Err("duplicate decision_contract".into());}
                decision=Some(t[1].into());
            }
            "action_invariant" if t.len()==2 => {
                if action_invariant.is_some(){return Err("duplicate action_invariant".into());}
                action_invariant=Some(parse_bool(t[1])?);
            }
            "decision_contract_change" if t.len()==2 => { decision_change=parse_bool(t[1])?; }
            "stability_rounds" if t.len()==2 => { stability_rounds=t[1].parse().map_err(|_|"bad stability_rounds")?; }
            "refinement" if t.len()==4 => {
                if refinements.iter().any(|x|x.id==t[1]){return Err(format!("duplicate refinement {}",t[1]));}
                if !matches!(t[2],"REPLAYED"|"DEFERRED"|"UNEXECUTED"){return Err("bad refinement status".into());}
                if !matches!(t[3],"INERT"|"CHANGES_DEFEAT"|"CHANGES_DISCRIMINATION"|"CHANGES_DECISION"|"UNKNOWN"){return Err("bad refinement effect".into());}
                refinements.push(Refinement{id:t[1].into(),status:t[2].into(),effect:t[3].into()});
            }
            "criterion" if t.len()==4 => {
                if criteria.iter().any(|x|x.id==t[1]){return Err(format!("duplicate criterion {}",t[1]));}
                if !matches!(t[2],"PROSPECTIVE"|"INHERITED"|"POST_OUTCOME"){return Err("bad criterion timing".into());}
                if !matches!(t[3],"INDEPENDENT"|"DEPENDENT"|"CYCLIC"){return Err("bad criterion ancestry".into());}
                criteria.push(Criterion{id:t[1].into(),timing:t[2].into(),ancestry:t[3].into()});
            }
            "criterion_verdict" if t.len()==4 => {
                if !matches!(t[3],"INERT"|"MATERIAL"|"UNKNOWN"){return Err("bad criterion verdict".into());}
                verdicts.push((t[1].into(),t[2].into(),t[3].into()));
            }
            "debt" if t.len()==4 => {
                if !matches!(t[2],"MATERIAL"|"NONMATERIAL"|"UNKNOWN"){return Err("bad debt materiality".into());}
                if !matches!(t[3],"LIVE"|"RESOLVED"){return Err("bad debt status".into());}
                debts.push(Debt{materiality:t[2].into(),status:t[3].into()});
            }
            "path" if t.len()==3 => {
                if !matches!(t[2],"PASS"|"HOLD"|"REOPEN"){return Err("bad path state".into());}
                paths.push((t[1].into(),t[2].into()));
            }
            "new_contact" if t.len()==3 => {
                if !matches!(t[2],"INERT"|"DISTINGUISHES"){return Err("bad new_contact state".into());}
                new_contacts.push((t[1].into(),t[2].into()));
            }
            "new_criterion" if t.len()==3 => {
                if !matches!(t[2],"AGREES"|"BREAKS"){return Err("bad new_criterion state".into());}
                new_criteria.push((t[1].into(),t[2].into()));
            }
            _ => return Err(format!("unknown or malformed line {}: {}",ln+1,line)),
        }
    }

    if !header || !ended { return Err("missing header or END".into()); }
    let _id=id.ok_or("missing id")?;
    let _scope=scope.ok_or("missing claim_scope")?;
    let timing=scope_timing.ok_or("missing scope_timing")?;
    let scope_nonvacuous=scope_nonvacuous.ok_or("missing scope_nonvacuous")?;
    let decision=decision.ok_or("missing decision_contract")?;
    let action_invariant=action_invariant.ok_or("missing action_invariant")?;

    let rids:HashSet<_>=refinements.iter().map(|r|r.id.as_str()).collect();
    let cids:HashSet<_>=criteria.iter().map(|c|c.id.as_str()).collect();
    let mut seen=HashSet::new();
    for (c,r,_) in &verdicts {
        if !cids.contains(c.as_str()) {return Err(format!("criterion_verdict unknown criterion {c}"));}
        if !rids.contains(r.as_str()) {return Err(format!("criterion_verdict unknown refinement {r}"));}
        if !seen.insert((c.clone(),r.clone())) {return Err(format!("duplicate criterion_verdict {c}/{r}"));}
    }

    let vacuous=!scope_nonvacuous || challenges.is_empty() || contacts.is_empty() || refinements.is_empty() || criteria.is_empty();
    let scope_capture=timing=="POST_OUTCOME_REVISION";
    let criterion_capture=criteria.iter().any(|c|c.timing=="POST_OUTCOME");
    let meta_cycle=criteria.iter().any(|c|c.ancestry=="CYCLIC");
    let live_debt=debts.iter().any(|d|d.status=="LIVE" && d.materiality!="NONMATERIAL")
        || refinements.iter().any(|r|r.status!="REPLAYED");
    let material_refinement=refinements.iter().any(|r|r.status=="REPLAYED" && r.effect!="INERT");
    let path_conflict=paths.iter().any(|(_,s)|s!="PASS");
    let new_contact_break=new_contacts.iter().any(|(_,s)|s=="DISTINGUISHES");
    let criterion_break=new_criteria.iter().any(|(_,s)|s=="BREAKS");

    let vmap:HashMap<(String,String),String>=verdicts.into_iter().map(|(c,r,v)|((c,r),v)).collect();
    let mut criterion_stop_support=!criteria.is_empty() && !refinements.is_empty();
    let mut criterion_noninvariance=false;
    for r in &refinements {
        let mut vals:HashSet<String>=HashSet::new();
        for c in &criteria {
            match vmap.get(&(c.id.clone(),r.id.clone())) {
                Some(v) => { vals.insert(v.clone()); if v!="INERT" {criterion_stop_support=false;} }
                None => { criterion_stop_support=false; criterion_noninvariance=true; }
            }
        }
        if vals.len()>1 || vals.contains("UNKNOWN") { criterion_noninvariance=true; }
    }

    let base_stop = !vacuous && !scope_capture && !criterion_capture && !meta_cycle &&
        !live_debt && !material_refinement && !criterion_noninvariance && criterion_stop_support &&
        !path_conflict && !new_contact_break && !criterion_break && !decision_change;

    let authority =
        if new_contact_break {"REOPEN_NEW_WORLD_CONTACT"}
        else if criterion_break {"REOPEN_CRITERION_ENVELOPE"}
        else if decision_change {"REOPEN_DECISION_CONTRACT_CHANGE"}
        else if path_conflict {"REOPEN_REGRESS_PATH_CONFLICT"}
        else if scope_capture {"HOLD_SCOPE_CAPTURE"}
        else if criterion_capture {"HOLD_META_CRITERION_CAPTURE"}
        else if meta_cycle {"HOLD_META_CYCLE"}
        else if vacuous {"HOLD_VACUOUS_TERMINATION"}
        else if live_debt {"HOLD_LIVE_REFINEMENT_DEBT"}
        else if criterion_noninvariance {"HOLD_META_CRITERION_NONINVARIANCE"}
        else if material_refinement {"HOLD_PREMATURE_TERMINATION"}
        else if base_stop {"AUTHORIZED_CRITERION_ROBUST_OPERATIONAL_STOP"}
        else {"HOLD_PREMATURE_TERMINATION"};

    let action_authority =
        if decision_change {"REOPEN_DECISION_CONTRACT_CHANGE"}
        else if decision!="NONE" && action_invariant && base_stop {"AUTHORIZED_ACTION_UNDER_DECLARED_CONTRACT"}
        else {"NOT_AUTHORIZED"};

    println!("regress.challenge_count={}",challenges.len());
    println!("regress.world_contact_count={}",contacts.len());
    println!("regress.refinement_count={}",refinements.len());
    println!("regress.criterion_count={}",criteria.len());
    println!("regress.live_material_debt={}",yes(live_debt));
    println!("regress.material_refinement={}",yes(material_refinement));
    println!("regress.scope_capture={}",yes(scope_capture));
    println!("regress.criterion_capture={}",yes(criterion_capture));
    println!("regress.meta_cycle={}",yes(meta_cycle));
    println!("regress.criterion_noninvariance={}",yes(criterion_noninvariance));
    println!("regress.criterion_stop_support={}",yes(criterion_stop_support));
    println!("regress.path_conflict={}",yes(path_conflict));
    println!("regress.new_world_contact_break={}",yes(new_contact_break));
    println!("regress.criterion_envelope_break={}",yes(criterion_break));
    println!("regress.decision_contract_change={}",yes(decision_change));
    println!("regress.operational_stop_authorized={}",yes(base_stop));
    println!("regress.action_authority={action_authority}");
    println!("regress.authority_state={authority}");
    println!("regress.stability_rounds={stability_rounds}");
    println!("regress.metaphysical_termination=NO");
    println!("regress.final_ontology_inferred=NO");
    println!("regress.future_refinement_space_closed=NO");
    println!("regress.stop_rule_truth_oracle=NO");
    println!("regress.claim_scope_truth_oracle=NO");
    println!("regress.meta_criterion_truth_oracle=NO");
    println!("regress.operational_stop_permanent=NO");
    println!("regress.reopening_reserve=ACTIVE");
    println!("regress.guidance_mode=REOPENABLE_OPERATIONAL_FIXED_POINT");
    Ok(())
}

fn parse_bool(s:&str)->Result<bool,String>{
    match s {"YES"=>Ok(true),"NO"=>Ok(false),_=>Err(format!("expected YES/NO, got {s}"))}
}
