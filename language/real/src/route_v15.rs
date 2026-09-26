use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct Route {
    id: String,
    ancestry: String,
    contents: BTreeSet<String>,
    covered: Option<bool>,
}

#[derive(Clone, Debug)]
struct MapRel {
    sources: Vec<String>,
    kind: String,
    targets: Vec<String>,
}

#[derive(Clone, Debug)]
struct HiddenRoute {
    id: String,
    kind: String,
    contents: BTreeSet<String>,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    source_ontology: String,
    target_ontology: String,
    contents: BTreeSet<String>,
    source_routes: BTreeMap<String, Route>,
    target_routes: BTreeMap<String, Route>,
    maps: Vec<MapRel>,
    witnesses: Vec<(String,String,BTreeSet<String>)>,
    hidden: Vec<HiddenRoute>,
    paths: Vec<(String,String)>,
    expected_authority: Option<String>,
    expected_equivalence: Option<String>,
    expected_duplication: Option<String>,
    expected_collapse: Option<String>,
    expected_hidden_novel: Option<String>,
    expected_entanglement: Option<String>,
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
        if t[0]=="REALROUTE"{
            if t.len()!=2||t[1]!="0.15"{return Err("expected REALROUTE 0.15".into());}
            if started{return Err("duplicate header".into());}
            started=true;
            continue;
        }
        if !started{return Err("packet must begin REALROUTE 0.15".into());}
        if t[0]=="END"{
            if t.len()!=1{return Err("END takes no arguments".into());}
            ended=true;
            break;
        }
        match t[0].as_str(){
            "id" if t.len()==2=>p.id=t[1].clone(),
            "claim_scope" if t.len()==2=>p.claim_scope=t[1].clone(),
            "source_ontology" if t.len()==2=>p.source_ontology=t[1].clone(),
            "target_ontology" if t.len()==2=>p.target_ontology=t[1].clone(),
            "content" if t.len()==2=>{
                if !p.contents.insert(t[1].clone()){return Err(format!("duplicate content: {}",t[1]));}
            }
            "source_route" if t.len()==5=>{
                let covered=match t[4].to_uppercase().as_str(){
                    "COVERED"=>true,"UNCOVERED"=>false,_=>return Err("invalid source coverage state".into())
                };
                if p.source_routes.contains_key(&t[1]){return Err(format!("duplicate source route: {}",t[1]));}
                p.source_routes.insert(t[1].clone(),Route{
                    id:t[1].clone(),ancestry:t[2].clone(),contents:split_plus(&t[3])?,covered:Some(covered)
                });
            }
            "target_route" if t.len()==4=>{
                if p.target_routes.contains_key(&t[1]){return Err(format!("duplicate target route: {}",t[1]));}
                p.target_routes.insert(t[1].clone(),Route{
                    id:t[1].clone(),ancestry:t[2].clone(),contents:split_plus(&t[3])?,covered:None
                });
            }
            "map" if t.len()==4=>{
                let kind=t[2].to_uppercase();
                if !["EXACT","REFINE","MERGE","OVERLAP","DISJOINT","UNMAPPED"].contains(&kind.as_str()){
                    return Err(format!("invalid map kind: {}",t[2]));
                }
                p.maps.push(MapRel{sources:split_plus_vec(&t[1])?,kind,targets:split_plus_vec(&t[3])?});
            }
            "coverage_witness" if t.len()==4=>{
                p.witnesses.push((t[1].clone(),t[2].clone(),split_plus(&t[3])?));
            }
            "hidden_route" if t.len()==4=>{
                let kind=t[2].to_uppercase();
                if !["NOVEL_ROUTE","REFINEMENT_OF_EXISTING","MERGE_CORRECTION","PREVIOUSLY_UNMAPPED_CONTENT","ANCESTRY_REVELATION","UNRESOLVED"].contains(&kind.as_str()){
                    return Err(format!("invalid hidden route kind: {}",t[2]));
                }
                p.hidden.push(HiddenRoute{id:t[1].clone(),kind,contents:split_plus(&t[3])?});
            }
            "path" if t.len()==3=>{
                let state=t[2].to_uppercase();
                if !["PASS","HOLD","REOPEN"].contains(&state.as_str()){return Err("invalid path state".into());}
                p.paths.push((t[1].clone(),state));
            }
            "authorize_coverage_authority" if t.len()==2=>p.expected_authority=Some(t[1].to_uppercase()),
            "authorize_coverage_equivalence" if t.len()==2=>p.expected_equivalence=Some(t[1].to_uppercase()),
            "authorize_duplication" if t.len()==2=>p.expected_duplication=Some(t[1].to_uppercase()),
            "authorize_collapse" if t.len()==2=>p.expected_collapse=Some(t[1].to_uppercase()),
            "authorize_hidden_novel" if t.len()==2=>p.expected_hidden_novel=Some(t[1].to_uppercase()),
            "authorize_ancestry_entanglement" if t.len()==2=>p.expected_entanglement=Some(t[1].to_uppercase()),
            "authorize_path_conflict" if t.len()==2=>p.expected_path_conflict=Some(t[1].to_uppercase()),
            _=>return Err(format!("{}:{} malformed command: {line}",path.display(),i+1)),
        }
    }

    if !ended{return Err("missing END".into());}
    if p.id.is_empty()||p.claim_scope.is_empty()||p.source_ontology.is_empty()||p.target_ontology.is_empty()
        ||p.contents.is_empty()||p.source_routes.is_empty()||p.target_routes.is_empty(){
        return Err("missing required field".into());
    }

    for r in p.source_routes.values().chain(p.target_routes.values()){
        if !r.contents.is_subset(&p.contents){return Err(format!("route {} references undeclared content",r.id));}
    }
    for m in &p.maps{
        for s in &m.sources{
            if !p.source_routes.contains_key(s){return Err(format!("map references unknown source route: {s}"));}
        }
        for t in &m.targets{
            if !p.target_routes.contains_key(t){return Err(format!("map references unknown target route: {t}"));}
        }
    }
    for (s,t,cs) in &p.witnesses{
        let sr=p.source_routes.get(s).ok_or_else(||format!("witness references unknown source route: {s}"))?;
        let tr=p.target_routes.get(t).ok_or_else(||format!("witness references unknown target route: {t}"))?;
        if !cs.is_subset(&sr.contents){return Err(format!("witness content not in source route: {s}"));}
        if !cs.is_subset(&tr.contents){return Err(format!("witness content not in target route: {t}"));}
    }
    for h in &p.hidden{
        if !h.contents.is_subset(&p.contents){return Err(format!("hidden route {} references undeclared content",h.id));}
    }
    Ok(p)
}

fn union_route_contents<'a,I>(it:I)->BTreeSet<String>
where I:Iterator<Item=&'a Route>{
    let mut out=BTreeSet::new();
    for r in it{out.extend(r.contents.iter().cloned());}
    out
}

fn analyze(p:&Packet)->BTreeMap<String,String>{
    let source_total=union_route_contents(p.source_routes.values());
    let target_total=union_route_contents(p.target_routes.values());
    let source_covered=union_route_contents(p.source_routes.values().filter(|r|r.covered==Some(true)));

    let mut witnessed=BTreeSet::new();
    for (_,_,cs) in &p.witnesses{witnessed.extend(cs.iter().cloned());}

    let source_complete=source_covered==source_total;
    let target_complete=target_total.is_subset(&witnessed);
    let transport_complete=source_covered.is_subset(&witnessed);
    let content_surface_equivalent=source_total==target_total;

    let source_ancestries:BTreeSet<String>=p.source_routes.values().map(|r|r.ancestry.clone()).collect();
    let target_ancestries:BTreeSet<String>=p.target_routes.values().map(|r|r.ancestry.clone()).collect();
    let ancestry_entanglement=(p.source_routes.len()>1 && p.source_routes.len()>source_ancestries.len())
        ||(p.target_routes.len()>1 && p.target_routes.len()>target_ancestries.len());

    let mut sig_counts:BTreeMap<String,usize>=BTreeMap::new();
    for r in p.target_routes.values(){
        let sig=join(&r.contents);
        *sig_counts.entry(sig).or_insert(0)+=1;
    }
    let duplication=sig_counts.values().any(|n|*n>1);

    let split_count=p.maps.iter().filter(|m|m.kind=="REFINE"&&m.sources.len()==1&&m.targets.len()>1).count();
    let merge_count=p.maps.iter().filter(|m|m.kind=="MERGE"&&m.sources.len()>1&&m.targets.len()==1).count();

    let mut collapse=false;
    for m in p.maps.iter().filter(|m|m.kind=="MERGE"){
        let src_union=union_route_contents(m.sources.iter().filter_map(|s|p.source_routes.get(s)));
        let tgt_union=union_route_contents(m.targets.iter().filter_map(|t|p.target_routes.get(t)));
        if !src_union.is_subset(&tgt_union){collapse=true;}
        let src_cov=union_route_contents(m.sources.iter().filter_map(|s|p.source_routes.get(s)).filter(|r|r.covered==Some(true)));
        let mut map_witness=BTreeSet::new();
        for (s,t,cs) in &p.witnesses{
            if m.sources.contains(s)&&m.targets.contains(t){map_witness.extend(cs.iter().cloned());}
        }
        if !src_cov.is_subset(&map_witness){collapse=true;}
    }

    let existing_surface:BTreeSet<String>=source_total.union(&target_total).cloned().collect();
    let hidden_count=p.hidden.len();
    let hidden_novel=p.hidden.iter().any(|h|{
        h.kind=="NOVEL_ROUTE"||h.kind=="PREVIOUSLY_UNMAPPED_CONTENT"||!h.contents.is_subset(&existing_surface)
    });
    let hidden_revision=hidden_count>0;

    let path_states:BTreeSet<String>=p.paths.iter().map(|(_,s)|s.clone()).collect();
    let path_conflict=path_states.len()>1;

    let equivalence=source_complete&&target_complete&&transport_complete&&content_surface_equivalent&&!collapse;

    let authority=if hidden_novel{"REOPEN_HIDDEN_NOVEL_CONTENT"}
        else if path_conflict{"REOPEN_REVISION_PATH_CONFLICT"}
        else if hidden_revision{"REOPEN_HIDDEN_ROUTE_REVISION"}
        else if collapse{"HOLD_COVERAGE_COLLAPSE"}
        else if !source_complete{"HOLD_SOURCE_COVERAGE_INCOMPLETE"}
        else if !transport_complete{"HOLD_COVERAGE_TRANSPORT"}
        else if !content_surface_equivalent{"HOLD_CONTENT_SURFACE_CHANGE"}
        else if !target_complete{"HOLD_TARGET_COVERAGE_INCOMPLETE"}
        else if ancestry_entanglement{"HOLD_ROUTE_ANCESTRY_ENTANGLEMENT"}
        else if equivalence{"AUTHORIZED_CONTENT_PRESERVING_TRANSPORT"}
        else{"HOLD_COVERAGE_INEQUIVALENT"};

    let reopen=hidden_revision||path_conflict;

    let mut a=BTreeMap::new();
    a.insert("route.source_route_count".into(),p.source_routes.len().to_string());
    a.insert("route.target_route_count".into(),p.target_routes.len().to_string());
    a.insert("route.source_content_count".into(),source_total.len().to_string());
    a.insert("route.target_content_count".into(),target_total.len().to_string());
    a.insert("route.source_covered_content_count".into(),source_covered.len().to_string());
    a.insert("route.target_witnessed_content_count".into(),witnessed.len().to_string());
    a.insert("route.source_ancestry_count".into(),source_ancestries.len().to_string());
    a.insert("route.target_ancestry_count".into(),target_ancestries.len().to_string());
    a.insert("route.split_count".into(),split_count.to_string());
    a.insert("route.merge_count".into(),merge_count.to_string());
    a.insert("route.source_coverage_complete".into(),yes(source_complete).into());
    a.insert("route.target_coverage_complete".into(),yes(target_complete).into());
    a.insert("route.coverage_transport_complete".into(),yes(transport_complete).into());
    a.insert("route.content_surface_equivalent".into(),yes(content_surface_equivalent).into());
    a.insert("route.coverage_duplication_detected".into(),yes(duplication).into());
    a.insert("route.coverage_collapse_detected".into(),yes(collapse).into());
    a.insert("route.coverage_equivalence".into(),yes(equivalence).into());
    a.insert("route.hidden_route_count".into(),hidden_count.to_string());
    a.insert("route.hidden_novel_content".into(),yes(hidden_novel).into());
    a.insert("route.ancestry_entanglement".into(),yes(ancestry_entanglement).into());
    a.insert("route.path_conflict".into(),yes(path_conflict).into());
    a.insert("route.reopen_required".into(),yes(reopen).into());
    a.insert("route.coverage_authority".into(),authority.into());
    a.insert("route.current_route_ontology_complete".into(),"NO".into());
    a.insert("route.future_defeat_space_closed".into(),"NO".into());
    a.insert("route.route_count_truth_oracle".into(),"NO".into());
    a.insert("route.route_label_identity_oracle".into(),"NO".into());
    a.insert("route.coverage_fraction_truth_oracle".into(),"NO".into());
    a.insert("route.revision_path_truth_oracle".into(),"NO".into());
    a.insert("route.guidance_mode".into(),"VERSIONED_DEFEAT_CONTENT_COVERAGE".into());
    a
}

fn validate(p:&Packet,a:&BTreeMap<String,String>)->Result<(),String>{
    let checks=[
        (&p.expected_authority,"route.coverage_authority"),
        (&p.expected_equivalence,"route.coverage_equivalence"),
        (&p.expected_duplication,"route.coverage_duplication_detected"),
        (&p.expected_collapse,"route.coverage_collapse_detected"),
        (&p.expected_hidden_novel,"route.hidden_novel_content"),
        (&p.expected_entanglement,"route.ancestry_entanglement"),
        (&p.expected_path_conflict,"route.path_conflict"),
    ];
    for (e,k) in checks{
        if let Some(x)=e{
            if a[k]!=*x{return Err(format!("{k} mismatch expected {x} got {}",a[k]));}
        }
    }
    Ok(())
}

fn emit(p:&Packet,a:&BTreeMap<String,String>)->String{
    let mut s=format!(
        "REAL-ROUTE=0.15\nid={}\nclaim_scope={}\nsource_ontology={}\ntarget_ontology={}\n",
        p.id,p.claim_scope,p.source_ontology,p.target_ontology
    );
    for k in [
        "route.source_route_count",
        "route.target_route_count",
        "route.source_content_count",
        "route.target_content_count",
        "route.source_covered_content_count",
        "route.target_witnessed_content_count",
        "route.source_ancestry_count",
        "route.target_ancestry_count",
        "route.split_count",
        "route.merge_count",
        "route.source_coverage_complete",
        "route.target_coverage_complete",
        "route.coverage_transport_complete",
        "route.content_surface_equivalent",
        "route.coverage_duplication_detected",
        "route.coverage_collapse_detected",
        "route.coverage_equivalence",
        "route.hidden_route_count",
        "route.hidden_novel_content",
        "route.ancestry_entanglement",
        "route.path_conflict",
        "route.reopen_required",
        "route.coverage_authority",
        "route.current_route_ontology_complete",
        "route.future_defeat_space_closed",
        "route.route_count_truth_oracle",
        "route.route_label_identity_oracle",
        "route.coverage_fraction_truth_oracle",
        "route.revision_path_truth_oracle",
        "route.guidance_mode",
    ]{
        s.push_str(&format!("{k}={}\n",a[k]));
    }
    s.push_str("route.meaning=DECLARED_VERSIONED_DEFEAT_CONTENT_COVERAGE\n");
    s
}

fn main(){
    let args:Vec<String>=env::args().skip(1).collect();
    if args.is_empty(){eprintln!("usage: real-v15-route <packet.real> [...]");std::process::exit(2);}
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
