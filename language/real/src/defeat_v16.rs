use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct Content {
    id: String,
    mechanism: String,
    manifestation: String,
    ancestry: String,
    profile: BTreeSet<String>,
}

#[derive(Clone, Debug)]
struct MapRel {
    sources: Vec<String>,
    kind: String,
    targets: Vec<String>,
}

#[derive(Clone, Debug)]
struct Hidden {
    id: String,
    kind: String,
    profile: BTreeSet<String>,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    source_representation: String,
    target_representation: String,
    challenges: BTreeSet<String>,
    source: BTreeMap<String,Content>,
    target: BTreeMap<String,Content>,
    maps: Vec<MapRel>,
    witnesses: Vec<(String,String,BTreeSet<String>)>,
    hidden: Vec<Hidden>,
    expansions: Vec<(String,String,String,String)>,
    paths: Vec<(String,String)>,
    expected_authority: Option<String>,
    expected_local_equivalence: Option<String>,
    expected_split_duplication: Option<String>,
    expected_manifestation_multiplication: Option<String>,
    expected_mechanism_aliasing: Option<String>,
    expected_common_cause: Option<String>,
    expected_expansion_break: Option<String>,
    expected_hidden_novel: Option<String>,
    expected_path_conflict: Option<String>,
}

fn toks(s:&str)->Vec<String>{
    s.split_whitespace().map(|x|x.trim_matches('"').to_string()).collect()
}
fn split_plus(s:&str)->Result<BTreeSet<String>,String>{
    let xs:BTreeSet<String>=s.split('+').filter(|x|!x.is_empty()).map(|x|x.to_string()).collect();
    if xs.is_empty(){return Err("empty set".into());}
    Ok(xs)
}
fn split_plus_vec(s:&str)->Result<Vec<String>,String>{
    let xs:Vec<String>=s.split('+').filter(|x|!x.is_empty()).map(|x|x.to_string()).collect();
    if xs.is_empty(){return Err("empty list".into());}
    Ok(xs)
}
fn yes(x:bool)->&'static str{if x{"YES"}else{"NO"}}
fn signature(xs:&BTreeSet<String>)->String{
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
        if t[0]=="REALDEFEAT"{
            if t.len()!=2||t[1]!="0.16"{return Err("expected REALDEFEAT 0.16".into());}
            if started{return Err("duplicate header".into());}
            started=true; continue;
        }
        if !started{return Err("packet must begin REALDEFEAT 0.16".into());}
        if t[0]=="END"{if t.len()!=1{return Err("END takes no arguments".into());} ended=true; break;}
        match t[0].as_str(){
            "id" if t.len()==2=>p.id=t[1].clone(),
            "claim_scope" if t.len()==2=>p.claim_scope=t[1].clone(),
            "source_representation" if t.len()==2=>p.source_representation=t[1].clone(),
            "target_representation" if t.len()==2=>p.target_representation=t[1].clone(),
            "challenge" if t.len()==2=>{if !p.challenges.insert(t[1].clone()){return Err(format!("duplicate challenge: {}",t[1]));}},
            "source_content" if t.len()==6=>{
                if p.source.contains_key(&t[1]){return Err(format!("duplicate source content: {}",t[1]));}
                p.source.insert(t[1].clone(),Content{id:t[1].clone(),mechanism:t[2].clone(),manifestation:t[3].clone(),ancestry:t[4].clone(),profile:split_plus(&t[5])?});
            }
            "target_content" if t.len()==6=>{
                if p.target.contains_key(&t[1]){return Err(format!("duplicate target content: {}",t[1]));}
                p.target.insert(t[1].clone(),Content{id:t[1].clone(),mechanism:t[2].clone(),manifestation:t[3].clone(),ancestry:t[4].clone(),profile:split_plus(&t[5])?});
            }
            "map" if t.len()==4=>{
                let kind=t[2].to_uppercase();
                if !["EXACT","REFINE","MERGE","OVERLAP","DISJOINT","UNMAPPED"].contains(&kind.as_str()){return Err(format!("invalid map kind: {}",t[2]));}
                p.maps.push(MapRel{sources:split_plus_vec(&t[1])?,kind,targets:split_plus_vec(&t[3])?});
            }
            "role_witness" if t.len()==4=>p.witnesses.push((t[1].clone(),t[2].clone(),split_plus(&t[3])?)),
            "hidden_content" if t.len()==4=>{
                let kind=t[2].to_uppercase();
                if !["NOVEL_COUNTERFACTUAL_DISTINCTION","REFINEMENT_OF_EXISTING","MECHANISM_REASSIGNMENT","MANIFESTATION_REASSIGNMENT","COMMON_CAUSE_REVEAL","REPRESENTATION_ESCAPE","PREVIOUSLY_UNMAPPED","UNRESOLVED"].contains(&kind.as_str()){return Err(format!("invalid hidden content kind: {}",t[2]));}
                p.hidden.push(Hidden{id:t[1].clone(),kind,profile:split_plus(&t[3])?});
            }
            "expansion" if t.len()==5=>{
                let s=t[4].to_uppercase();
                if !["SAME","DISTINGUISHES"].contains(&s.as_str()){return Err("invalid expansion state".into());}
                p.expansions.push((t[1].clone(),t[2].clone(),t[3].clone(),s));
            }
            "path" if t.len()==3=>{
                let s=t[2].to_uppercase();
                if !["PASS","HOLD","REOPEN"].contains(&s.as_str()){return Err("invalid path state".into());}
                p.paths.push((t[1].clone(),s));
            }
            "authorize_identity_authority" if t.len()==2=>p.expected_authority=Some(t[1].to_uppercase()),
            "authorize_local_equivalence" if t.len()==2=>p.expected_local_equivalence=Some(t[1].to_uppercase()),
            "authorize_split_duplication" if t.len()==2=>p.expected_split_duplication=Some(t[1].to_uppercase()),
            "authorize_manifestation_multiplication" if t.len()==2=>p.expected_manifestation_multiplication=Some(t[1].to_uppercase()),
            "authorize_mechanism_aliasing" if t.len()==2=>p.expected_mechanism_aliasing=Some(t[1].to_uppercase()),
            "authorize_common_cause" if t.len()==2=>p.expected_common_cause=Some(t[1].to_uppercase()),
            "authorize_expansion_break" if t.len()==2=>p.expected_expansion_break=Some(t[1].to_uppercase()),
            "authorize_hidden_novel" if t.len()==2=>p.expected_hidden_novel=Some(t[1].to_uppercase()),
            "authorize_path_conflict" if t.len()==2=>p.expected_path_conflict=Some(t[1].to_uppercase()),
            _=>return Err(format!("{}:{} malformed command: {line}",path.display(),i+1)),
        }
    }
    if !ended{return Err("missing END".into());}
    if p.id.is_empty()||p.claim_scope.is_empty()||p.source_representation.is_empty()||p.target_representation.is_empty()||p.challenges.is_empty()||p.source.is_empty()||p.target.is_empty(){return Err("missing required field".into());}
    for c in p.source.values().chain(p.target.values()){
        if !c.profile.is_subset(&p.challenges){return Err(format!("content {} references undeclared challenge",c.id));}
    }
    for m in &p.maps{
        for s in &m.sources{if !p.source.contains_key(s){return Err(format!("map references unknown source content: {s}"));}}
        for t in &m.targets{if !p.target.contains_key(t){return Err(format!("map references unknown target content: {t}"));}}
    }
    for (s,t,qs) in &p.witnesses{
        let sc=p.source.get(s).ok_or_else(||format!("witness references unknown source content: {s}"))?;
        let tc=p.target.get(t).ok_or_else(||format!("witness references unknown target content: {t}"))?;
        if !qs.is_subset(&sc.profile)||!qs.is_subset(&tc.profile){return Err(format!("role witness incompatible with mapped profiles: {s}->{t}"));}
    }
    for h in &p.hidden{if !h.profile.is_subset(&p.challenges){return Err(format!("hidden content {} references undeclared challenge",h.id));}}
    for (_,s,t,_) in &p.expansions{
        if !p.source.contains_key(s){return Err(format!("expansion references unknown source content: {s}"));}
        if !p.target.contains_key(t){return Err(format!("expansion references unknown target content: {t}"));}
    }
    Ok(p)
}

fn distinct_values<'a,I>(it:I)->usize where I:Iterator<Item=&'a str>{
    it.map(|x|x.to_string()).collect::<BTreeSet<_>>().len()
}
fn profile_count<'a,I>(it:I)->usize where I:Iterator<Item=&'a Content>{
    it.map(|c|signature(&c.profile)).collect::<BTreeSet<_>>().len()
}
fn role_transport_complete(p:&Packet)->bool{
    for s in p.source.values(){
        let mapped_targets:BTreeSet<String>=p.maps.iter().filter(|m|m.sources.contains(&s.id)).flat_map(|m|m.targets.iter().cloned()).collect();
        if mapped_targets.is_empty(){return false;}
        let mut witnessed=BTreeSet::new();
        for (ws,wt,qs) in &p.witnesses{
            if ws==&s.id && mapped_targets.contains(wt){witnessed.extend(qs.iter().cloned());}
        }
        if !s.profile.is_subset(&witnessed){return false;}
    }
    true
}
fn local_equivalence(p:&Packet)->bool{
    p.maps.iter().any(|m|{
        m.sources.len()==1&&m.targets.len()==1&&
        p.source.get(&m.sources[0]).zip(p.target.get(&m.targets[0])).map(|(s,t)|s.profile==t.profile).unwrap_or(false)
    })
}
fn manifestation_multiplication(p:&Packet)->bool{
    let mut map:BTreeMap<String,BTreeSet<String>>=BTreeMap::new();
    for c in p.source.values().chain(p.target.values()){
        map.entry(c.mechanism.clone()).or_default().insert(c.manifestation.clone());
    }
    map.values().any(|x|x.len()>1)
}
fn mechanism_aliasing(p:&Packet)->bool{
    let mut map:BTreeMap<String,BTreeSet<String>>=BTreeMap::new();
    for c in p.source.values().chain(p.target.values()){
        map.entry(c.manifestation.clone()).or_default().insert(c.mechanism.clone());
    }
    map.values().any(|x|x.len()>1)
}
fn source_union(p:&Packet)->BTreeSet<String>{
    p.source.values().flat_map(|c|c.profile.iter().cloned()).collect()
}
fn target_union(p:&Packet)->BTreeSet<String>{
    p.target.values().flat_map(|c|c.profile.iter().cloned()).collect()
}
fn analyze(p:&Packet)->BTreeMap<String,String>{
    let source_profiles=profile_count(p.source.values());
    let target_profiles=profile_count(p.target.values());
    let source_mechs=distinct_values(p.source.values().map(|c|c.mechanism.as_str()));
    let target_mechs=distinct_values(p.target.values().map(|c|c.mechanism.as_str()));
    let source_mans=distinct_values(p.source.values().map(|c|c.manifestation.as_str()));
    let target_mans=distinct_values(p.target.values().map(|c|c.manifestation.as_str()));
    let source_anc=distinct_values(p.source.values().map(|c|c.ancestry.as_str()));
    let target_anc=distinct_values(p.target.values().map(|c|c.ancestry.as_str()));
    let split_count=p.maps.iter().filter(|m|m.kind=="REFINE"&&m.sources.len()==1&&m.targets.len()>1).count();
    let merge_count=p.maps.iter().filter(|m|m.kind=="MERGE"&&m.sources.len()>1&&m.targets.len()==1).count();
    let split_duplication=split_count>0&&p.target.len()>p.source.len()&&target_profiles<=source_profiles;
    let man_mult=manifestation_multiplication(p);
    let mech_alias=mechanism_aliasing(p);
    let common_cause=(p.source.len()>1&&source_anc<p.source.len())||(p.target.len()>1&&target_anc<p.target.len());
    let transport=role_transport_complete(p);
    let local_eq=local_equivalence(p);
    let role_drift=p.maps.iter().any(|m|{
        m.kind=="EXACT"&&m.sources.len()==1&&m.targets.len()==1&&
        p.source.get(&m.sources[0]).zip(p.target.get(&m.targets[0])).map(|(s,t)|s.profile!=t.profile).unwrap_or(false)
    });
    let expansion_break=p.expansions.iter().any(|(_,_,_,s)|s=="DISTINGUISHES");
    let hidden_count=p.hidden.len();
    let hidden_novel=p.hidden.iter().any(|h|h.kind=="NOVEL_COUNTERFACTUAL_DISTINCTION"||h.kind=="PREVIOUSLY_UNMAPPED");
    let hidden_revision=hidden_count>0;
    let path_states:BTreeSet<String>=p.paths.iter().map(|(_,s)|s.clone()).collect();
    let path_conflict=path_states.len()>1;
    let representation_collapse=!source_union(p).is_subset(&target_union(p));
    let merge_launder=merge_count>0&&!transport;
    let refine_authorized=split_count>0&&transport&&target_profiles>source_profiles;
    let merge_authorized=merge_count>0&&transport&&!representation_collapse;
    let reopen=expansion_break||hidden_revision||path_conflict;

    let authority=if hidden_novel{"REOPEN_HIDDEN_NOVEL_DISTINCTION"}
        else if expansion_break{"REOPEN_EXPANSION_BREAK"}
        else if path_conflict{"REOPEN_REVISION_PATH_CONFLICT"}
        else if hidden_revision{"REOPEN_HIDDEN_CONTENT_REVISION"}
        else if role_drift{"HOLD_ROLE_DRIFT"}
        else if split_duplication{"HOLD_SPLIT_WITHOUT_NEW_DISTINCTION"}
        else if merge_launder{"HOLD_MERGE_DISTINCTION_LAUNDERING"}
        else if representation_collapse{"HOLD_REPRESENTATION_COLLAPSE"}
        else if !transport{"HOLD_ROLE_TRANSPORT"}
        else if refine_authorized{"AUTHORIZED_COUNTERFACTUAL_REFINEMENT"}
        else if merge_authorized{"AUTHORIZED_SCOPE_QUOTIENT_MERGE"}
        else if local_eq{"AUTHORIZED_LOCAL_COUNTERFACTUAL_QUOTIENT"}
        else{"AUTHORIZED_LOCAL_DEFEAT_ROLE_TRANSPORT"};

    let mut a=BTreeMap::new();
    a.insert("defeat.source_content_count".into(),p.source.len().to_string());
    a.insert("defeat.target_content_count".into(),p.target.len().to_string());
    a.insert("defeat.source_mechanism_count".into(),source_mechs.to_string());
    a.insert("defeat.target_mechanism_count".into(),target_mechs.to_string());
    a.insert("defeat.source_manifestation_count".into(),source_mans.to_string());
    a.insert("defeat.target_manifestation_count".into(),target_mans.to_string());
    a.insert("defeat.source_ancestry_count".into(),source_anc.to_string());
    a.insert("defeat.target_ancestry_count".into(),target_anc.to_string());
    a.insert("defeat.counterfactual_profile_count_source".into(),source_profiles.to_string());
    a.insert("defeat.counterfactual_profile_count_target".into(),target_profiles.to_string());
    a.insert("defeat.split_count".into(),split_count.to_string());
    a.insert("defeat.merge_count".into(),merge_count.to_string());
    a.insert("defeat.manifestation_multiplication".into(),yes(man_mult).into());
    a.insert("defeat.mechanism_aliasing".into(),yes(mech_alias).into());
    a.insert("defeat.common_cause_compression".into(),yes(common_cause).into());
    a.insert("defeat.role_transport_complete".into(),yes(transport).into());
    a.insert("defeat.local_counterfactual_equivalence".into(),yes(local_eq).into());
    a.insert("defeat.role_drift".into(),yes(role_drift).into());
    a.insert("defeat.split_without_new_distinction".into(),yes(split_duplication).into());
    a.insert("defeat.representation_collapse".into(),yes(representation_collapse).into());
    a.insert("defeat.expansion_breaks_equivalence".into(),yes(expansion_break).into());
    a.insert("defeat.hidden_content_count".into(),hidden_count.to_string());
    a.insert("defeat.hidden_novel_distinction".into(),yes(hidden_novel).into());
    a.insert("defeat.path_conflict".into(),yes(path_conflict).into());
    a.insert("defeat.reopen_required".into(),yes(reopen).into());
    a.insert("defeat.identity_authority".into(),authority.into());
    a.insert("defeat.current_defeat_atoms_complete".into(),"NO".into());
    a.insert("defeat.future_defeat_space_closed".into(),"NO".into());
    a.insert("defeat.label_identity_oracle".into(),"NO".into());
    a.insert("defeat.mechanism_identity_oracle".into(),"NO".into());
    a.insert("defeat.manifestation_identity_oracle".into(),"NO".into());
    a.insert("defeat.counterfactual_equivalence_truth_oracle".into(),"NO".into());
    a.insert("defeat.representation_truth_oracle".into(),"NO".into());
    a.insert("defeat.guidance_mode".into(),"REOPENABLE_COUNTERFACTUAL_DEFEAT_QUOTIENT".into());
    a
}
fn validate(p:&Packet,a:&BTreeMap<String,String>)->Result<(),String>{
    let checks=[
        (&p.expected_authority,"defeat.identity_authority"),
        (&p.expected_local_equivalence,"defeat.local_counterfactual_equivalence"),
        (&p.expected_split_duplication,"defeat.split_without_new_distinction"),
        (&p.expected_manifestation_multiplication,"defeat.manifestation_multiplication"),
        (&p.expected_mechanism_aliasing,"defeat.mechanism_aliasing"),
        (&p.expected_common_cause,"defeat.common_cause_compression"),
        (&p.expected_expansion_break,"defeat.expansion_breaks_equivalence"),
        (&p.expected_hidden_novel,"defeat.hidden_novel_distinction"),
        (&p.expected_path_conflict,"defeat.path_conflict"),
    ];
    for (e,k) in checks{
        if let Some(x)=e{if a[k]!=*x{return Err(format!("{k} mismatch expected {x} got {}",a[k]));}}
    }
    Ok(())
}
fn emit(p:&Packet,a:&BTreeMap<String,String>)->String{
    let mut s=format!("REAL-DEFEAT=0.16\nid={}\nclaim_scope={}\nsource_representation={}\ntarget_representation={}\n",p.id,p.claim_scope,p.source_representation,p.target_representation);
    for k in [
        "defeat.source_content_count","defeat.target_content_count",
        "defeat.source_mechanism_count","defeat.target_mechanism_count",
        "defeat.source_manifestation_count","defeat.target_manifestation_count",
        "defeat.source_ancestry_count","defeat.target_ancestry_count",
        "defeat.counterfactual_profile_count_source","defeat.counterfactual_profile_count_target",
        "defeat.split_count","defeat.merge_count",
        "defeat.manifestation_multiplication","defeat.mechanism_aliasing","defeat.common_cause_compression",
        "defeat.role_transport_complete","defeat.local_counterfactual_equivalence","defeat.role_drift",
        "defeat.split_without_new_distinction","defeat.representation_collapse",
        "defeat.expansion_breaks_equivalence","defeat.hidden_content_count","defeat.hidden_novel_distinction",
        "defeat.path_conflict","defeat.reopen_required","defeat.identity_authority",
        "defeat.current_defeat_atoms_complete","defeat.future_defeat_space_closed",
        "defeat.label_identity_oracle","defeat.mechanism_identity_oracle","defeat.manifestation_identity_oracle",
        "defeat.counterfactual_equivalence_truth_oracle","defeat.representation_truth_oracle","defeat.guidance_mode"
    ]{s.push_str(&format!("{k}={}\n",a[k]));}
    s.push_str("defeat.meaning=DECLARED_CLAIM_RELATIVE_DEFEAT_ROLE\n");
    s
}
fn main(){
    let args:Vec<String>=env::args().skip(1).collect();
    if args.is_empty(){eprintln!("usage: real-v16-defeat <packet.real> [...]");std::process::exit(2);}
    for f in args{
        match parse(Path::new(&f)){
            Ok(p)=>{let a=analyze(&p);if let Err(e)=validate(&p,&a){eprintln!("{e}");std::process::exit(1);}print!("{}",emit(&p,&a));}
            Err(e)=>{eprintln!("{e}");std::process::exit(1);}
        }
    }
}
