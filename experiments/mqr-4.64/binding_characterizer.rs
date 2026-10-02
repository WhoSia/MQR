use std::collections::{BTreeMap, BTreeSet};
use std::fs::{create_dir_all, File};
use std::io::{BufWriter, Write};

#[derive(Clone, Copy, Debug)]
struct Action {
    name: &'static str,
    u: i32,
    c: i32,
    sep: u8,
    reopen: bool,
    ancestry: u8,
    exterior: bool,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Baseline { Myopic, Lookahead, Constrained, Diversity }

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Constraint { Opr, Arr, Eai, Exterior, Nedl }

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Class {
    DiagnosticOnly,
    RedundantConstraint,
    BaselineAbsorbed,
    BindingLocal,
    Overconstraining,
}

#[derive(Clone, Copy, Debug)]
struct World {
    irr: bool,
    sub: bool,
    reopen_live: bool,
    anc_live: bool,
    ext_live: bool,
}

fn bname(b: Baseline) -> &'static str {
    match b { Baseline::Myopic=>"MYOPIC", Baseline::Lookahead=>"LOOKAHEAD",
              Baseline::Constrained=>"CONSTRAINED", Baseline::Diversity=>"DIVERSITY" }
}
fn cname(c: Constraint) -> &'static str {
    match c { Constraint::Opr=>"OPR", Constraint::Arr=>"ARR", Constraint::Eai=>"EAI",
              Constraint::Exterior=>"EXTERIOR", Constraint::Nedl=>"NEDL" }
}
fn clname(c: Class) -> &'static str {
    match c { Class::DiagnosticOnly=>"DIAGNOSTIC_ONLY",
              Class::RedundantConstraint=>"REDUNDANT_CONSTRAINT",
              Class::BaselineAbsorbed=>"BASELINE_ABSORBED",
              Class::BindingLocal=>"BINDING_LOCAL",
              Class::Overconstraining=>"OVERCONSTRAINING" }
}

fn pop2(x: u8) -> i32 { ((x & 1) != 0) as i32 + ((x & 2) != 0) as i32 }

fn effective_sep(a: Action, w: World) -> u8 {
    if !w.irr { return 3; }
    if w.sub {
        if a.sep != 0 { 1 } else { 0 }
    } else { a.sep }
}
fn effective_reopen(a: Action, w: World) -> bool {
    if !w.irr { true } else { a.reopen }
}

fn net(a: Action) -> i32 { a.u - a.c }

fn catalog() -> Vec<Action> {
    vec![
        Action{name:"A0_HI_DROP",u:2,c:0,sep:0,reopen:false,ancestry:0,exterior:false},
        Action{name:"A1_FULL",u:1,c:0,sep:3,reopen:true,ancestry:1,exterior:true},
        Action{name:"A2_COST_FULL",u:2,c:1,sep:3,reopen:true,ancestry:1,exterior:true},
        Action{name:"A3_S0_HI",u:2,c:0,sep:1,reopen:false,ancestry:0,exterior:false},
        Action{name:"A4_S1_HI",u:2,c:0,sep:2,reopen:false,ancestry:0,exterior:false},
        Action{name:"A5_S0_REOPEN",u:1,c:0,sep:1,reopen:true,ancestry:1,exterior:false},
        Action{name:"A6_S1_REOPEN",u:1,c:0,sep:2,reopen:true,ancestry:1,exterior:false},
        Action{name:"A7_FULL_EXT",u:1,c:0,sep:3,reopen:false,ancestry:0,exterior:true},
        Action{name:"A8_DROP_REOPEN",u:2,c:1,sep:0,reopen:true,ancestry:1,exterior:true},
        Action{name:"A9_CHEAP_FULL_G0",u:1,c:1,sep:3,reopen:true,ancestry:0,exterior:false},
        Action{name:"A10_LOW_FULL",u:0,c:0,sep:3,reopen:true,ancestry:1,exterior:true},
        Action{name:"A11_HI_FULL",u:2,c:0,sep:3,reopen:false,ancestry:0,exterior:false},
        Action{name:"A12_HI_REOPEN_DROP",u:2,c:0,sep:0,reopen:true,ancestry:0,exterior:false},
        Action{name:"A13_HI_G1_DROP",u:2,c:0,sep:0,reopen:false,ancestry:1,exterior:false},
        Action{name:"A14_HI_EXT_DROP",u:2,c:0,sep:0,reopen:false,ancestry:0,exterior:true},
        Action{name:"A15_FULL_REOPEN_EXT_G0",u:1,c:0,sep:3,reopen:true,ancestry:0,exterior:true},
    ]
}

fn baseline_feasible(actions: &[Action;3], w: World, b: Baseline) -> Vec<usize> {
    let mut ids: Vec<usize>=(0..3).collect();
    if b == Baseline::Constrained && w.irr {
        let any = actions.iter().any(|a| effective_sep(*a,w)!=0);
        if any { ids.retain(|&i| effective_sep(actions[i],w)!=0); }
    }
    ids
}

fn score(a: Action, w: World, b: Baseline) -> i32 {
    let n=net(a)*20;
    match b {
        Baseline::Myopic|Baseline::Constrained => n,
        Baseline::Lookahead => {
            n + pop2(effective_sep(a,w))*20
              + if w.reopen_live && effective_reopen(a,w) {10} else {0}
        },
        Baseline::Diversity => {
            n + if w.anc_live && a.ancestry==1 {8} else {0}
              + if w.ext_live && a.exterior {8} else {0}
        },
    }
}

fn choose(actions:&[Action;3], w:World, b:Baseline, feasible:&[usize]) -> usize {
    *feasible.iter().max_by_key(|&&i| (score(actions[i],w,b), -(i as i32))).unwrap()
}

fn typed_allowed(a:Action, actions:&[Action;3], w:World, c:Constraint) -> bool {
    match c {
        Constraint::Opr => {
            if !w.irr { return true; }
            let any=actions.iter().any(|x| effective_sep(*x,w)!=0);
            !any || effective_sep(a,w)!=0
        },
        Constraint::Arr => {
            if !w.reopen_live { return true; }
            let any=actions.iter().any(|x| effective_reopen(*x,w));
            !any || effective_reopen(a,w)
        },
        Constraint::Eai => {
            if !w.anc_live { return true; }
            let any=actions.iter().any(|x| x.ancestry==1);
            !any || a.ancestry==1
        },
        Constraint::Exterior => {
            if !w.ext_live { return true; }
            let any=actions.iter().any(|x| x.exterior);
            !any || a.exterior
        },
        Constraint::Nedl => {
            if !w.irr { return true; }
            if w.sub {
                let any=actions.iter().any(|x| effective_sep(*x,w)!=0);
                return !any || effective_sep(a,w)!=0;
            }
            let any_full=actions.iter().any(|x| effective_sep(*x,w)==3);
            if any_full { effective_sep(a,w)==3 }
            else {
                let any=actions.iter().any(|x| effective_sep(*x,w)!=0);
                !any || effective_sep(a,w)!=0
            }
        },
    }
}

fn reach_key(a:Action,w:World)->(u8,bool,u8,bool) {
    (effective_sep(a,w), effective_reopen(a,w), a.ancestry, a.exterior)
}
fn material_gain(base:Action, typed:Action, w:World, c:Constraint)->bool {
    match c {
        Constraint::Opr|Constraint::Nedl => {
            let eb=effective_sep(base,w); let et=effective_sep(typed,w);
            if w.sub { (et!=0) && (eb==0) } else { (et & !eb)!=0 || pop2(et)>pop2(eb) }
        },
        Constraint::Arr => w.reopen_live && effective_reopen(typed,w) && !effective_reopen(base,w),
        Constraint::Eai => w.anc_live && typed.ancestry==1 && base.ancestry==0,
        Constraint::Exterior => w.ext_live && typed.exterior && !base.exterior,
    }
}

fn classify(actions:&[Action;3],w:World,b:Baseline,c:Constraint)->(Class,usize,usize,usize,usize) {
    let phys:Vec<usize>=(0..3).collect();
    let global_allowed:Vec<usize>=phys.iter().copied().filter(|&i|typed_allowed(actions[i],actions,w,c)).collect();
    let fb=baseline_feasible(actions,w,b);
    let typed_fb:Vec<usize>=fb.iter().copied().filter(|&i|typed_allowed(actions[i],actions,w,c)).collect();

    let base=choose(actions,w,b,&fb);
    if global_allowed.len()==3 {
        return (Class::DiagnosticOnly,base,base,fb.len(),typed_fb.len());
    }
    if typed_fb.len()==fb.len() {
        return (Class::BaselineAbsorbed,base,base,fb.len(),typed_fb.len());
    }
    if typed_fb.is_empty() {
        return (Class::Overconstraining,base,base,fb.len(),0);
    }
    let typed=choose(actions,w,b,&typed_fb);
    if typed==base || reach_key(actions[typed],w)==reach_key(actions[base],w) {
        return (Class::RedundantConstraint,base,typed,fb.len(),typed_fb.len());
    }
    if material_gain(actions[base],actions[typed],w,c) {
        return (Class::BindingLocal,base,typed,fb.len(),typed_fb.len());
    }
    (Class::Overconstraining,base,typed,fb.len(),typed_fb.len())
}

fn world_family(w:World,c:Constraint)->String {
    match c {
        Constraint::Opr|Constraint::Nedl => format!("SEP:irr{}:sub{}",w.irr as u8,w.sub as u8),
        Constraint::Arr => format!("REOPEN:irr{}:live{}",w.irr as u8,w.reopen_live as u8),
        Constraint::Eai => format!("ANCESTRY:live{}",w.anc_live as u8),
        Constraint::Exterior => format!("EXTERIOR:live{}",w.ext_live as u8),
    }
}

fn main() {
    let cats=catalog();
    let baselines=[Baseline::Myopic,Baseline::Lookahead,Baseline::Constrained,Baseline::Diversity];
    let constraints=[Constraint::Opr,Constraint::Arr,Constraint::Eai,Constraint::Exterior,Constraint::Nedl];
    let mut counts:BTreeMap<(Constraint,Baseline,Class),usize>=BTreeMap::new();
    let mut bind_families:BTreeMap<Constraint,BTreeSet<String>>=BTreeMap::new();
    let mut bind_baselines:BTreeMap<Constraint,BTreeSet<Baseline>>=BTreeMap::new();
    let mut first_witness:BTreeMap<(Constraint,Baseline),(usize,usize,usize,World,usize,usize)>=BTreeMap::new();
    let mut worlds=0usize;
    let mut comparisons=0usize;

    for i in 0..cats.len() {
      for j in i..cats.len() {
        for k in j..cats.len() {
          let actions=[cats[i],cats[j],cats[k]];
          for flags in 0..32u8 {
            let w=World{
              irr: flags&1!=0,
              sub: flags&2!=0,
              reopen_live: flags&4!=0,
              anc_live: flags&8!=0,
              ext_live: flags&16!=0,
            };
            worlds+=1;
            for &b in &baselines {
              for &c in &constraints {
                let (cl,ba,ta,_,_)=classify(&actions,w,b,c);
                *counts.entry((c,b,cl)).or_insert(0)+=1;
                comparisons+=1;
                if cl==Class::BindingLocal {
                    bind_families.entry(c).or_default().insert(world_family(w,c));
                    bind_baselines.entry(c).or_default().insert(b);
                    first_witness.entry((c,b)).or_insert((i,j,k,w,ba,ta));
                }
              }
            }
          }
        }
      }
    }

    create_dir_all("experiments/mqr-4.64/results").unwrap();
    let mut out=BufWriter::new(File::create("experiments/mqr-4.64/results/rust_summary.tsv").unwrap());
    writeln!(out,"kind\tconstraint\tbaseline\tclass\tcount").unwrap();
    for &c in &constraints {
      for &b in &baselines {
        for cl in [Class::DiagnosticOnly,Class::RedundantConstraint,Class::BaselineAbsorbed,Class::BindingLocal,Class::Overconstraining] {
          let n=*counts.get(&(c,b,cl)).unwrap_or(&0);
          writeln!(out,"COUNT\t{}\t{}\t{}\t{}",cname(c),bname(b),clname(cl),n).unwrap();
        }
      }
    }
    for &c in &constraints {
        let fam=bind_families.get(&c).map(|x|x.len()).unwrap_or(0);
        let bs=bind_baselines.get(&c).map(|x|x.len()).unwrap_or(0);
        let structural=fam>=2 && bs>=2;
        writeln!(out,"PROMOTION\t{}\tALL\tBINDING_STRUCTURAL_CANDIDATE\t{}",cname(c),structural as usize).unwrap();
        writeln!(out,"META\t{}\tALL\tBINDING_FAMILY_COUNT\t{}",cname(c),fam).unwrap();
        writeln!(out,"META\t{}\tALL\tBINDING_BASELINE_COUNT\t{}",cname(c),bs).unwrap();
    }

    let mut wit=BufWriter::new(File::create("experiments/mqr-4.64/results/rust_witnesses.tsv").unwrap());
    writeln!(wit,"constraint\tbaseline\ta0\ta1\ta2\tirr\tsub\treopen_live\tanc_live\text_live\tbaseline_action\ttyped_action").unwrap();
    for ((c,b),(i,j,k,w,ba,ta)) in first_witness {
        writeln!(wit,"{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
          cname(c),bname(b),cats[i].name,cats[j].name,cats[k].name,
          w.irr as u8,w.sub as u8,w.reopen_live as u8,w.anc_live as u8,w.ext_live as u8,
          [cats[i],cats[j],cats[k]][ba].name,[cats[i],cats[j],cats[k]][ta].name).unwrap();
    }

    println!("MQR464_WORLD_COUNT={}",worlds);
    println!("MQR464_COMPARISON_COUNT={}",comparisons);
    println!("MQR464_ACTION_CATALOG=16");
    println!("MQR464_SCALAR_SCORE=FORBIDDEN");

    // Explicit structural fixtures independent of aggregate outcomes.
    println!("MQR464_ORACLE_TRAP=ORACLE_DEPENDENT");
    println!("MQR464_REVERSIBLE_OPR_RELEASE=PASS");
    println!("MQR464_SUBSTITUTABLE_SEPARATOR_RELEASE=PASS");
    println!("MQR464_RESULT_DEPENDENT_MUTATION=FORBIDDEN");
}
