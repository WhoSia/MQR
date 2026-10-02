use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

const RELATIONS: [&str; 6] = ["DISJOINT","EXACT","MERGE","OVERLAP","REFINE","UNMAPPED"];

#[derive(Clone, Debug)]
struct Probe {
    id: String,
    ancestry: String,
    selected: bool,
    mode: String,
    supports: BTreeSet<String>,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    candidate_relations: BTreeSet<String>,
    selector_id: String,
    selector_ancestry: String,
    selection_timing: String,
    rule_id: String,
    rule_ancestry: String,
    rule_mode: String,
    routes: BTreeSet<String>,
    probes: BTreeMap<String, Probe>,
    covers: Vec<(String,String)>,
    score_source: BTreeMap<String,String>,
    relevance_source: BTreeMap<String,String>,
    expansions: Vec<(String,BTreeSet<String>)>,
    expected_authority: Option<String>,
    expected_narrowed: Option<String>,
    expected_coverage: Option<String>,
    expected_common: Option<String>,
    expected_capture: Option<String>,
    expected_expansion_reopen: Option<String>,
}

fn toks(s:&str)->Vec<String>{
    s.split_whitespace().map(|x|x.trim_matches('"').to_string()).collect()
}

fn split_plus(s:&str)->Result<BTreeSet<String>,String>{
    let xs:BTreeSet<String>=s.split('+').filter(|x|!x.is_empty()).map(|x|x.to_uppercase()).collect();
    if xs.is_empty(){return Err("empty relation set".into());}
    for x in &xs{
        if !RELATIONS.contains(&x.as_str()){return Err(format!("invalid relation: {x}"));}
    }
    Ok(xs)
}

fn yes(x:bool)->&'static str{if x{"YES"}else{"NO"}}

fn join(xs:&BTreeSet<String>)->String{
    if xs.is_empty(){"NONE".into()}else{xs.iter().cloned().collect::<Vec<_>>().join("+")}
}

fn parse(path:&Path)->Result<Packet,String>{
    let text=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut p=Packet::default();
    let mut started=false;
    let mut ended=false;

    for (i,raw) in text.lines().enumerate(){
        let line=raw.trim();
        if line.is_empty()||line.starts_with('#'){continue;}
        let t=toks(line);
        if t.is_empty(){continue;}
        if t[0]=="REALCHALLENGE"{
            if t.len()!=2||t[1]!="0.14"{return Err("expected REALCHALLENGE 0.14".into());}
            if started{return Err("duplicate header".into());}
            started=true;
            continue;
        }
        if !started{return Err("packet must begin REALCHALLENGE 0.14".into());}
        if t[0]=="END"{
            if t.len()!=1{return Err("END takes no arguments".into());}
            ended=true;
            break;
        }
        match t[0].as_str(){
            "id" if t.len()==2=>p.id=t[1].clone(),
            "claim_scope" if t.len()==2=>p.claim_scope=t[1].clone(),
            "candidate_relations" if t.len()==2=>p.candidate_relations=split_plus(&t[1])?,
            "selector" if t.len()==3=>{
                p.selector_id=t[1].clone(); p.selector_ancestry=t[2].clone();
            }
            "selection_timing" if t.len()==2=>{
                let x=t[1].to_uppercase();
                if !["PRESEALED","POST_OUTCOME"].contains(&x.as_str()){return Err("invalid selection timing".into());}
                p.selection_timing=x;
            }
            "selection_rule" if t.len()==4=>{
                let x=t[3].to_uppercase();
                if !["INDEPENDENT","INCUMBENT_DEFINED","UNRESOLVED"].contains(&x.as_str()){return Err("invalid selection rule mode".into());}
                p.rule_id=t[1].clone(); p.rule_ancestry=t[2].clone(); p.rule_mode=x;
            }
            "route" if t.len()==2=>{
                if !p.routes.insert(t[1].clone()){return Err(format!("duplicate route: {}",t[1]));}
            }
            "probe" if t.len()==6=>{
                let selected=match t[3].to_uppercase().as_str(){
                    "SELECTED"=>true,"UNSELECTED"=>false,_=>return Err("invalid probe selection state".into())
                };
                let mode=t[4].to_uppercase();
                if !["WORLD_FACING","INTERNAL"].contains(&mode.as_str()){return Err("invalid probe mode".into());}
                if p.probes.contains_key(&t[1]){return Err(format!("duplicate probe: {}",t[1]));}
                p.probes.insert(t[1].clone(),Probe{
                    id:t[1].clone(), ancestry:t[2].clone(), selected, mode, supports:split_plus(&t[5])?
                });
            }
            "covers" if t.len()==3=>p.covers.push((t[1].clone(),t[2].clone())),
            "score_source" if t.len()==3=>{
                let x=t[2].to_uppercase();
                if !["INDEPENDENT","CANDIDATE_DERIVED","STANDARD_DERIVED"].contains(&x.as_str()){return Err("invalid score source".into());}
                p.score_source.insert(t[1].clone(),x);
            }
            "relevance_source" if t.len()==3=>{
                let x=t[2].to_uppercase();
                if !["INDEPENDENT","CANDIDATE_DERIVED","STANDARD_DERIVED"].contains(&x.as_str()){return Err("invalid relevance source".into());}
                p.relevance_source.insert(t[1].clone(),x);
            }
            "expansion" if t.len()==3=>p.expansions.push((t[1].clone(),split_plus(&t[2])?)),
            "authorize_selection_authority" if t.len()==2=>p.expected_authority=Some(t[1].to_uppercase()),
            "authorize_narrowed" if t.len()==2=>p.expected_narrowed=Some(t[1].to_uppercase()),
            "authorize_declared_route_coverage_complete" if t.len()==2=>p.expected_coverage=Some(t[1].to_uppercase()),
            "authorize_common_ancestry" if t.len()==2=>p.expected_common=Some(t[1].to_uppercase()),
            "authorize_discriminator_capture" if t.len()==2=>p.expected_capture=Some(t[1].to_uppercase()),
            "authorize_expansion_reopen" if t.len()==2=>p.expected_expansion_reopen=Some(t[1].to_uppercase()),
            _=>return Err(format!("{}:{} malformed command: {line}",path.display(),i+1)),
        }
    }

    if !ended{return Err("missing END".into());}
    if p.id.is_empty()||p.claim_scope.is_empty()||p.candidate_relations.is_empty()
        ||p.selector_id.is_empty()||p.selector_ancestry.is_empty()||p.selection_timing.is_empty()
        ||p.rule_id.is_empty()||p.rule_ancestry.is_empty()||p.rule_mode.is_empty()
        ||p.routes.is_empty()||p.probes.is_empty(){
        return Err("missing required field".into());
    }
    for (probe,route) in &p.covers{
        if !p.probes.contains_key(probe){return Err(format!("coverage references unknown probe: {probe}"));}
        if !p.routes.contains(route){return Err(format!("coverage references unknown route: {route}"));}
    }
    for id in p.probes.keys(){
        if !p.score_source.contains_key(id){return Err(format!("missing score_source for probe: {id}"));}
        if !p.relevance_source.contains_key(id){return Err(format!("missing relevance_source for probe: {id}"));}
    }
    Ok(p)
}

fn intersect(a:&BTreeSet<String>,b:&BTreeSet<String>)->BTreeSet<String>{
    a.intersection(b).cloned().collect()
}

fn analyze(p:&Packet)->BTreeMap<String,String>{
    let selected_world:Vec<&Probe>=p.probes.values().filter(|q|q.selected&&q.mode=="WORLD_FACING").collect();
    let selected_count=p.probes.values().filter(|q|q.selected).count();
    let selected_world_count=selected_world.len();
    let selected_ancestries:BTreeSet<String>=selected_world.iter().map(|q|q.ancestry.clone()).collect();
    let selected_ancestry_count=selected_ancestries.len();
    let common_ancestry=selected_world_count>selected_ancestry_count && selected_world_count>1;

    let mut covered_routes=BTreeSet::new();
    for (probe,route) in &p.covers{
        if let Some(q)=p.probes.get(probe){
            if q.selected && q.mode=="WORLD_FACING"{covered_routes.insert(route.clone());}
        }
    }
    let route_count=p.routes.len();
    let covered_route_count=covered_routes.len();
    let uncovered_route_count=route_count.saturating_sub(covered_route_count);
    let coverage_complete=uncovered_route_count==0;
    let probe_route_multiplicity=selected_world_count>covered_route_count && selected_world_count>1;

    let post_outcome=p.selection_timing=="POST_OUTCOME";
    let incumbent_relevance=p.rule_mode=="INCUMBENT_DEFINED" || selected_world.iter().any(|q|p.relevance_source.get(&q.id).map(|x|x=="CANDIDATE_DERIVED").unwrap_or(false));
    let candidate_score=selected_world.iter().any(|q|p.score_source.get(&q.id).map(|x|x=="CANDIDATE_DERIVED").unwrap_or(false));
    let discriminator_capture=incumbent_relevance||candidate_score;

    let before=p.candidate_relations.clone();
    let mut after=before.clone();
    for q in &selected_world{after=intersect(&after,&q.supports);}
    let narrowed=!after.is_empty()&&after.len()<before.len();

    let omitted_counterprobe=p.probes.values().any(|q|{
        if q.selected||q.mode!="WORLD_FACING"||after.is_empty(){return false;}
        intersect(&after,&q.supports).is_empty() && !intersect(&before,&q.supports).is_empty()
    });

    let mut expansion_instability=false;
    let mut expansion_reopen=false;
    let mut expansion_narrow=false;
    for (_,support) in &p.expansions{
        let x=intersect(&after,support);
        if x!=after{expansion_instability=true;}
        if !after.is_empty()&&x.is_empty(){expansion_reopen=true;}
        if !x.is_empty()&&x.len()<after.len(){expansion_narrow=true;}
    }
    let expansion_state=if p.expansions.is_empty(){"NONE"}
        else if expansion_reopen{"REOPENED"}
        else if expansion_narrow{"NARROWED"}
        else if expansion_instability{"CHANGED"}
        else{"STABLE"};

    let authority=if post_outcome{"HOLD_POST_OUTCOME_SELECTION"}
        else if discriminator_capture{"HOLD_DISCRIMINATOR_CAPTURE"}
        else if omitted_counterprobe{"REOPEN_OMITTED_COUNTERPROBE"}
        else if selected_world_count==0{"HOLD_NO_WORLD_FACING"}
        else if !coverage_complete{"HOLD_ROUTE_COVERAGE"}
        else if common_ancestry{"HOLD_COMMON_ANCESTRY"}
        else if expansion_reopen{"REOPEN_EXPANSION_CONFLICT"}
        else if after.is_empty(){"REOPEN_SELECTED_CONFLICT"}
        else if narrowed{"AUTHORIZED_PROVISIONAL_NARROWING"}
        else{"ADMISSIBLE_NO_NARROWING"};

    let mut a=BTreeMap::new();
    a.insert("challenge.registered_probe_count".into(),p.probes.len().to_string());
    a.insert("challenge.selected_probe_count".into(),selected_count.to_string());
    a.insert("challenge.selected_world_probe_count".into(),selected_world_count.to_string());
    a.insert("challenge.selected_ancestry_count".into(),selected_ancestry_count.to_string());
    a.insert("challenge.route_count".into(),route_count.to_string());
    a.insert("challenge.covered_route_count".into(),covered_route_count.to_string());
    a.insert("challenge.uncovered_route_count".into(),uncovered_route_count.to_string());
    a.insert("challenge.declared_route_coverage_complete".into(),yes(coverage_complete).into());
    a.insert("challenge.probe_route_multiplicity".into(),yes(probe_route_multiplicity).into());
    a.insert("challenge.common_ancestry".into(),yes(common_ancestry).into());
    a.insert("challenge.post_outcome_selection".into(),yes(post_outcome).into());
    a.insert("challenge.incumbent_relevance".into(),yes(incumbent_relevance).into());
    a.insert("challenge.discriminator_capture".into(),yes(discriminator_capture).into());
    a.insert("challenge.omitted_counterprobe".into(),yes(omitted_counterprobe).into());
    a.insert("challenge.correspondence_before".into(),join(&before));
    a.insert("challenge.correspondence_after".into(),join(&after));
    a.insert("challenge.narrowed".into(),yes(narrowed).into());
    a.insert("challenge.expansion_count".into(),p.expansions.len().to_string());
    a.insert("challenge.expansion_instability".into(),yes(expansion_instability).into());
    a.insert("challenge.expansion_reopen_required".into(),yes(expansion_reopen).into());
    a.insert("challenge.expansion_state".into(),expansion_state.into());
    a.insert("challenge.current_family_complete".into(),"NO".into());
    a.insert("challenge.future_challenge_space_closed".into(),"NO".into());
    a.insert("challenge.probe_count_truth_oracle".into(),"NO".into());
    a.insert("challenge.externality_truth_oracle".into(),"NO".into());
    a.insert("challenge.cost_truth_oracle".into(),"NO".into());
    a.insert("challenge.selection_rule_truth_oracle".into(),"NO".into());
    a.insert("challenge.selection_authority".into(),authority.into());
    a.insert("challenge.guidance_mode".into(),"CONSTITUTED_REOPENABLE_SEPARATOR_AUTHORITY".into());
    a
}

fn validate(p:&Packet,a:&BTreeMap<String,String>)->Result<(),String>{
    let checks=[
        (&p.expected_authority,"challenge.selection_authority"),
        (&p.expected_narrowed,"challenge.narrowed"),
        (&p.expected_coverage,"challenge.declared_route_coverage_complete"),
        (&p.expected_common,"challenge.common_ancestry"),
        (&p.expected_capture,"challenge.discriminator_capture"),
        (&p.expected_expansion_reopen,"challenge.expansion_reopen_required"),
    ];
    for (e,k) in checks{
        if let Some(x)=e{
            if a[k]!=*x{return Err(format!("{k} mismatch expected {x} got {}",a[k]));}
        }
    }
    Ok(())
}

fn emit(p:&Packet,a:&BTreeMap<String,String>)->String{
    let mut s=format!("REAL-CHALLENGE=0.14\nid={}\nclaim_scope={}\n",p.id,p.claim_scope);
    for k in [
        "challenge.registered_probe_count",
        "challenge.selected_probe_count",
        "challenge.selected_world_probe_count",
        "challenge.selected_ancestry_count",
        "challenge.route_count",
        "challenge.covered_route_count",
        "challenge.uncovered_route_count",
        "challenge.declared_route_coverage_complete",
        "challenge.probe_route_multiplicity",
        "challenge.common_ancestry",
        "challenge.post_outcome_selection",
        "challenge.incumbent_relevance",
        "challenge.discriminator_capture",
        "challenge.omitted_counterprobe",
        "challenge.correspondence_before",
        "challenge.correspondence_after",
        "challenge.narrowed",
        "challenge.expansion_count",
        "challenge.expansion_instability",
        "challenge.expansion_reopen_required",
        "challenge.expansion_state",
        "challenge.current_family_complete",
        "challenge.future_challenge_space_closed",
        "challenge.probe_count_truth_oracle",
        "challenge.externality_truth_oracle",
        "challenge.cost_truth_oracle",
        "challenge.selection_rule_truth_oracle",
        "challenge.selection_authority",
        "challenge.guidance_mode",
    ]{s.push_str(&format!("{k}={}\n",a[k]));}
    s
}

fn main(){
    let args:Vec<String>=env::args().skip(1).collect();
    if args.is_empty(){eprintln!("usage: real-v14-challenge <packet.real> [...]");std::process::exit(2);}
    for f in args{
        match parse(Path::new(&f)){
            Ok(p)=>{
                let a=analyze(&p);
                if let Err(e)=validate(&p,&a){eprintln!("{e}");std::process::exit(1);}
                print!("{}",emit(&p,&a));
            }
            Err(e)=>{eprintln!("{e}");std::process::exit(1);}
        }
    }
}
