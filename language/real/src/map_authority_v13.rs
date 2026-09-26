use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

const RELATIONS: [&str; 6] = ["DISJOINT", "EXACT", "MERGE", "OVERLAP", "REFINE", "UNMAPPED"];

#[derive(Clone, Debug)]
struct Adjudicator {
    id: String,
    ancestry: String,
    provenance: String,
}

#[derive(Clone, Debug)]
struct Standard {
    id: String,
    ancestry: String,
    timing: String,
}

#[derive(Clone, Debug)]
struct Witness {
    id: String,
    standard: String,
    adjudicator: String,
    layer: String,
    supports: BTreeSet<String>,
}

#[derive(Clone, Debug)]
struct Challenge {
    id: String,
    mode: String,
    supports: BTreeSet<String>,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    source_ontology: String,
    target_ontology: String,
    candidate_relation: String,
    proposer_id: String,
    proposer_ancestry: String,
    adjudicators: BTreeMap<String, Adjudicator>,
    standards: BTreeMap<String, Standard>,
    witnesses: Vec<Witness>,
    challenges: Vec<Challenge>,
    meta_deps: Vec<(String, String)>,
    meta_anchors: BTreeSet<String>,
    force_singleton: bool,
    expected_authority: Option<String>,
    expected_singleton: Option<String>,
    expected_self: Option<String>,
    expected_capture: Option<String>,
    expected_meta_cycle: Option<String>,
    expected_world_separator: Option<String>,
}

fn toks(s: &str) -> Vec<String> {
    s.split_whitespace().map(|x| x.trim_matches('"').to_string()).collect()
}

fn split_plus(s: &str) -> Result<BTreeSet<String>, String> {
    let xs: BTreeSet<String> = s.split('+').filter(|x| !x.is_empty()).map(|x| x.to_uppercase()).collect();
    if xs.is_empty() {
        return Err("empty relation support set".into());
    }
    for x in &xs {
        if !RELATIONS.contains(&x.as_str()) {
            return Err(format!("invalid relation in support set: {x}"));
        }
    }
    Ok(xs)
}

fn all_relations() -> BTreeSet<String> {
    RELATIONS.iter().map(|x| x.to_string()).collect()
}

fn yes(x: bool) -> &'static str { if x { "YES" } else { "NO" } }

fn join(xs: &BTreeSet<String>) -> String {
    if xs.is_empty() { "NONE".into() } else { xs.iter().cloned().collect::<Vec<_>>().join("+") }
}

fn parse(path: &Path) -> Result<Packet, String> {
    let text = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut p = Packet::default();
    let mut started = false;
    let mut ended = false;

    for (i, raw) in text.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        let t = toks(line);
        if t.is_empty() { continue; }

        if t[0] == "REALMAPAUTH" {
            if t.len() != 2 || t[1] != "0.13" { return Err("expected REALMAPAUTH 0.13".into()); }
            if started { return Err("duplicate REALMAPAUTH header".into()); }
            started = true;
            continue;
        }
        if !started { return Err("packet must begin REALMAPAUTH 0.13".into()); }
        if t[0] == "END" {
            if t.len() != 1 { return Err("END takes no arguments".into()); }
            ended = true;
            break;
        }

        match t[0].as_str() {
            "id" if t.len()==2 => p.id=t[1].clone(),
            "claim_scope" if t.len()==2 => p.claim_scope=t[1].clone(),
            "source_ontology" if t.len()==2 => p.source_ontology=t[1].clone(),
            "target_ontology" if t.len()==2 => p.target_ontology=t[1].clone(),
            "candidate_relation" if t.len()==2 => {
                let r=t[1].to_uppercase();
                if !RELATIONS.contains(&r.as_str()) { return Err(format!("invalid candidate relation: {}",t[1])); }
                p.candidate_relation=r;
            }
            "proposer" if t.len()==3 => {
                p.proposer_id=t[1].clone();
                p.proposer_ancestry=t[2].clone();
            }
            "adjudicator" if t.len()==4 => {
                let prov=t[3].to_uppercase();
                if !["INTERNAL","EXTERNAL","MIXED"].contains(&prov.as_str()) { return Err(format!("invalid adjudicator provenance: {}",t[3])); }
                if p.adjudicators.contains_key(&t[1]) { return Err(format!("duplicate adjudicator: {}",t[1])); }
                p.adjudicators.insert(t[1].clone(),Adjudicator{id:t[1].clone(),ancestry:t[2].clone(),provenance:prov});
            }
            "standard" if t.len()==4 => {
                let timing=t[3].to_uppercase();
                if !["PRESEALED","POST_OUTCOME","INHERITED"].contains(&timing.as_str()) { return Err(format!("invalid standard timing: {}",t[3])); }
                if p.standards.contains_key(&t[1]) { return Err(format!("duplicate standard: {}",t[1])); }
                p.standards.insert(t[1].clone(),Standard{id:t[1].clone(),ancestry:t[2].clone(),timing});
            }
            "witness" if t.len()==6 => {
                let layer=t[4].to_uppercase();
                if !["DIRECT","META"].contains(&layer.as_str()) { return Err(format!("invalid witness layer: {}",t[4])); }
                p.witnesses.push(Witness{id:t[1].clone(),standard:t[2].clone(),adjudicator:t[3].clone(),layer,supports:split_plus(&t[5])?});
            }
            "challenge" if t.len()==4 => {
                let mode=t[2].to_uppercase();
                if !["INTERNAL","WORLD_FACING"].contains(&mode.as_str()) { return Err(format!("invalid challenge mode: {}",t[2])); }
                p.challenges.push(Challenge{id:t[1].clone(),mode,supports:split_plus(&t[3])?});
            }
            "meta_dep" if t.len()==3 => p.meta_deps.push((t[1].clone(),t[2].clone())),
            "meta_anchor" if t.len()==3 => {
                let kind=t[2].to_uppercase();
                if !["WORLD_FACING","DECLARED"].contains(&kind.as_str()) { return Err(format!("invalid meta anchor: {}",t[2])); }
                p.meta_anchors.insert(t[1].clone());
            }
            "force_singleton" if t.len()==2 => {
                p.force_singleton=match t[1].to_uppercase().as_str(){"YES"=>true,"NO"=>false,_=>return Err("force_singleton must be YES or NO".into())};
            }
            "authorize_mapping_authority" if t.len()==2 => p.expected_authority=Some(t[1].to_uppercase()),
            "authorize_correspondence_singleton" if t.len()==2 => p.expected_singleton=Some(t[1].to_uppercase()),
            "authorize_self_certified" if t.len()==2 => p.expected_self=Some(t[1].to_uppercase()),
            "authorize_capture_risk" if t.len()==2 => p.expected_capture=Some(t[1].to_uppercase()),
            "authorize_meta_cycle" if t.len()==2 => p.expected_meta_cycle=Some(t[1].to_uppercase()),
            "authorize_world_separator" if t.len()==2 => p.expected_world_separator=Some(t[1].to_uppercase()),
            _ => return Err(format!("{}:{} malformed command: {line}",path.display(),i+1)),
        }
    }

    if !ended { return Err("missing END".into()); }
    if p.id.is_empty() || p.claim_scope.is_empty() || p.source_ontology.is_empty() || p.target_ontology.is_empty()
        || p.candidate_relation.is_empty() || p.proposer_id.is_empty() || p.proposer_ancestry.is_empty()
        || p.adjudicators.is_empty() || p.standards.is_empty() || p.witnesses.is_empty() {
        return Err("missing required field".into());
    }
    for w in &p.witnesses {
        if !p.standards.contains_key(&w.standard) { return Err(format!("witness references unknown standard: {}",w.standard)); }
        if !p.adjudicators.contains_key(&w.adjudicator) { return Err(format!("witness references unknown adjudicator: {}",w.adjudicator)); }
    }
    Ok(p)
}

fn intersect_sets(sets: &[BTreeSet<String>]) -> BTreeSet<String> {
    if sets.is_empty() { return all_relations(); }
    let mut out=sets[0].clone();
    for s in &sets[1..] { out=out.intersection(s).cloned().collect(); }
    out
}

fn evidence_sets(p:&Packet, include_world:bool) -> Vec<BTreeSet<String>> {
    let mut v:Vec<BTreeSet<String>>=p.witnesses.iter().map(|w|w.supports.clone()).collect();
    for c in &p.challenges {
        if include_world || c.mode!="WORLD_FACING" { v.push(c.supports.clone()); }
    }
    v
}

fn layer_intersection(p:&Packet, layer:&str) -> Option<BTreeSet<String>> {
    let xs:Vec<_>=p.witnesses.iter().filter(|w|w.layer==layer).map(|w|w.supports.clone()).collect();
    if xs.is_empty(){None}else{Some(intersect_sets(&xs))}
}

fn support_disagreement(p:&Packet)->bool{
    let xs=evidence_sets(p,true);
    if xs.len()<2{return false;}
    xs.iter().skip(1).any(|x| *x!=xs[0])
}

fn graph_cycle(edges:&[(String,String)])->bool{
    let mut g:BTreeMap<String,Vec<String>>=BTreeMap::new();
    for (a,b) in edges { g.entry(a.clone()).or_default().push(b.clone()); g.entry(b.clone()).or_default(); }
    fn dfs(n:&str,g:&BTreeMap<String,Vec<String>>,visiting:&mut BTreeSet<String>,done:&mut BTreeSet<String>)->bool{
        if visiting.contains(n){return true;}
        if done.contains(n){return false;}
        visiting.insert(n.to_string());
        if let Some(ns)=g.get(n){
            for x in ns { if dfs(x,g,visiting,done){return true;} }
        }
        visiting.remove(n);
        done.insert(n.to_string());
        false
    }
    let mut visiting=BTreeSet::new();
    let mut done=BTreeSet::new();
    for n in g.keys(){ if dfs(n,&g,&mut visiting,&mut done){return true;} }
    false
}

fn meta_debt_count(p:&Packet)->usize{
    if p.meta_deps.is_empty(){return 0;}
    let mut nodes=BTreeSet::new();
    let mut sources=BTreeSet::new();
    for (a,b) in &p.meta_deps { nodes.insert(a.clone()); nodes.insert(b.clone()); sources.insert(a.clone()); }
    nodes.into_iter().filter(|n|!sources.contains(n) && !p.meta_anchors.contains(n)).count()
}

fn analyze(p:&Packet)->BTreeMap<String,String>{
    let mut a=BTreeMap::new();
    let adj_count=p.adjudicators.len();
    let adj_ancestries:BTreeSet<_>=p.adjudicators.values().map(|x|x.ancestry.clone()).collect();
    let adjudicator_ancestry_count=adj_ancestries.len();
    let self_certified=p.adjudicators.values().any(|x|x.id==p.proposer_id || x.ancestry==p.proposer_ancestry);
    let common_ancestry=adj_count>adjudicator_ancestry_count;
    let capture_risk=p.standards.values().any(|s|s.timing=="POST_OUTCOME" || s.ancestry==p.proposer_ancestry);
    let pre_world=intersect_sets(&evidence_sets(p,false));
    let cas=intersect_sets(&evidence_sets(p,true));
    let world_present=p.challenges.iter().any(|c|c.mode=="WORLD_FACING");
    let world_separator=world_present && !cas.is_empty() && cas.len()<pre_world.len();
    let singleton=cas.len()==1;
    let forced_overclaim=p.force_singleton && !singleton;
    let direct_meta_conflict=match (layer_intersection(p,"DIRECT"),layer_intersection(p,"META")){
        (Some(d),Some(m))=>d.intersection(&m).next().is_none(),
        _=>false,
    };
    let meta_cycle=graph_cycle(&p.meta_deps);
    let meta_debt=meta_debt_count(p);
    let conflict_count=if support_disagreement(p) || direct_meta_conflict {1}else{0};
    let candidate_supported=cas.contains(&p.candidate_relation);

    let independence_state=if self_certified{"SELF_CERTIFIED"}
        else if common_ancestry{"COMMON_ANCESTRY"}
        else if adjudicator_ancestry_count>=2{"ANCESTRY_SEPARATED"}
        else{"UNRESOLVED"};

    let authority=if cas.is_empty(){"CONTESTED_NO_COMMON_RELATION"}
        else if forced_overclaim{"REOPEN_FORCED_SINGLETON"}
        else if meta_cycle{"REOPEN_META_CYCLE"}
        else if direct_meta_conflict{"REOPEN_DIRECT_META_CONFLICT"}
        else if capture_risk{"HOLD_STANDARD_CAPTURE"}
        else if self_certified{"HOLD_SELF_CERTIFIED"}
        else if common_ancestry && adj_count>1{"HOLD_COMMON_ANCESTRY"}
        else if meta_debt>0{"HOLD_META_DEBT"}
        else if !candidate_supported{"HOLD_CANDIDATE_UNSUPPORTED"}
        else if cas.len()>1{"SET_VALUED_PROVISIONAL"}
        else{"EARNED_PROVISIONAL"};

    a.insert("authority.candidate_relation".into(),p.candidate_relation.clone());
    a.insert("authority.adjudicator_count".into(),adj_count.to_string());
    a.insert("authority.adjudicator_ancestry_count".into(),adjudicator_ancestry_count.to_string());
    a.insert("authority.independence_state".into(),independence_state.into());
    a.insert("authority.self_certified".into(),yes(self_certified).into());
    a.insert("authority.common_ancestry".into(),yes(common_ancestry).into());
    a.insert("authority.standard_count".into(),p.standards.len().to_string());
    a.insert("authority.capture_risk".into(),yes(capture_risk).into());
    a.insert("authority.correspondence_set".into(),join(&cas));
    a.insert("authority.correspondence_set_size".into(),cas.len().to_string());
    a.insert("authority.correspondence_singleton".into(),yes(singleton).into());
    a.insert("authority.forced_singleton_overclaim".into(),yes(forced_overclaim).into());
    a.insert("authority.conflict_count".into(),conflict_count.to_string());
    a.insert("authority.direct_meta_conflict".into(),yes(direct_meta_conflict).into());
    a.insert("authority.world_facing_separator_present".into(),yes(world_separator).into());
    a.insert("authority.meta_cycle".into(),yes(meta_cycle).into());
    a.insert("authority.meta_debt_count".into(),meta_debt.to_string());
    a.insert("authority.mapping_authority".into(),authority.into());
    a.insert("authority.unique_world_correspondence_inferred".into(),"NO".into());
    a.insert("authority.future_translation_closed".into(),"NO".into());
    a.insert("authority.consensus_truth_oracle".into(),"NO".into());
    a.insert("authority.standard_truth_oracle".into(),"NO".into());
    a.insert("authority.externality_truth_oracle".into(),"NO".into());
    a.insert("authority.meta_cycle_authority".into(),"NO".into());
    a.insert("authority.guidance_mode".into(),"CONTESTABLE_SET_VALUED_TRANSLATION_AUTHORITY".into());
    a
}

fn validate(p:&Packet,a:&BTreeMap<String,String>)->Result<(),String>{
    let checks=[
        (&p.expected_authority,"authority.mapping_authority"),
        (&p.expected_singleton,"authority.correspondence_singleton"),
        (&p.expected_self,"authority.self_certified"),
        (&p.expected_capture,"authority.capture_risk"),
        (&p.expected_meta_cycle,"authority.meta_cycle"),
        (&p.expected_world_separator,"authority.world_facing_separator_present"),
    ];
    for (e,k) in checks {
        if let Some(x)=e { if a[k]!=*x { return Err(format!("{k} mismatch expected {x} got {}",a[k])); } }
    }
    Ok(())
}

fn emit(p:&Packet,a:&BTreeMap<String,String>)->String{
    let mut s=format!(
        "REAL-MAP-AUTHORITY=0.13\nid={}\nclaim_scope={}\nsource_ontology={}\ntarget_ontology={}\n",
        p.id,p.claim_scope,p.source_ontology,p.target_ontology
    );
    for k in [
        "authority.candidate_relation",
        "authority.adjudicator_count",
        "authority.adjudicator_ancestry_count",
        "authority.independence_state",
        "authority.self_certified",
        "authority.common_ancestry",
        "authority.standard_count",
        "authority.capture_risk",
        "authority.correspondence_set",
        "authority.correspondence_set_size",
        "authority.correspondence_singleton",
        "authority.forced_singleton_overclaim",
        "authority.conflict_count",
        "authority.direct_meta_conflict",
        "authority.world_facing_separator_present",
        "authority.meta_cycle",
        "authority.meta_debt_count",
        "authority.mapping_authority",
        "authority.unique_world_correspondence_inferred",
        "authority.future_translation_closed",
        "authority.consensus_truth_oracle",
        "authority.standard_truth_oracle",
        "authority.externality_truth_oracle",
        "authority.meta_cycle_authority",
        "authority.guidance_mode",
    ]{s.push_str(&format!("{k}={}\n",a[k]));}
    s.push_str("authority.meaning=DECLARED_CONTESTABLE_MAPPING_AUTHORITY\n");
    s.push_str("mapping_validity_does_not_mean_world_identity=true\n");
    s.push_str("adjudicator_plurality_does_not_mean_independence=true\n");
    s.push_str("meta_validation_does_not_mean_regress_closure=true\n");
    s
}

fn main(){
    let args:Vec<String>=env::args().skip(1).collect();
    if args.is_empty(){eprintln!("usage: real-v13-map-authority <packet.real> [...]");std::process::exit(2);}
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
