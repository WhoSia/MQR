//! MQR-4.100 P2: approximate observation morphisms and coupling provenance.
//! Elementary finite-TV calculations and constructed negative controls.
//! No scientific novelty, finite-sample guarantee or field validation is claimed.
use mqr4100_observation_refinement::{old_marginal,Experiment};
const TOL:f64=1e-10;
fn approx(a:f64,b:f64)->bool{(a-b).abs()<TOL}
fn tv(p:&[f64],q:&[f64])->f64{
    assert_eq!(p.len(),q.len());
    0.5*p.iter().zip(q).map(|(x,y)|(x-y).abs()).sum::<f64>()
}
fn errors(old:&Experiment,joint:&Experiment,outs_y:usize,outs_z:usize)->Vec<f64>{
    let projected=old_marginal(joint,outs_y,outs_z);
    assert_eq!(old.rows.len(),joint.rows.len());
    assert_eq!(old.rows[0].len(),outs_y);
    (0..old.rows.len()).map(|i|tv(&old.rows[i],&projected.rows[i])).collect()
}
fn triangle_bound(old:&Experiment,joint:&Experiment,y:usize,z:usize,i:usize,j:usize)->(f64,f64){
    let e=errors(old,joint,y,z);
    let lhs=tv(&old.rows[i],&old.rows[j]);
    let rhs=tv(&joint.rows[i],&joint.rows[j])+e[i]+e[j];
    assert!(lhs<=rhs+TOL,"TV inequality violated: {} > {}",lhs,rhs);
    (lhs,rhs)
}
fn frechet_11(p_y:f64,p_z:f64)->(f64,f64){
    for x in [p_y,p_z]{assert!(x.is_finite()&&(0.0..=1.0).contains(&x));}
    ((p_y+p_z-1.0).max(0.0),p_y.min(p_z))
}
fn binary_classification_risk_uniform(e:&Experiment)->f64{
    assert_eq!(e.rows.len(),2);
    let acc=(0..e.rows[0].len()).map(|y|e.rows[0][y].max(e.rows[1][y])).sum::<f64>()/2.0;
    1.0-acc
}
/// For finite theta and specified target labels, minimum TV separating distinct targets.
fn target_separation_margin(e:&Experiment,g:&[usize])->Option<f64>{
    assert_eq!(e.rows.len(),g.len());
    let mut minimum=f64::INFINITY;
    for i in 0..g.len(){for j in i+1..g.len(){
        if g[i]!=g[j]{minimum=minimum.min(tv(&e.rows[i],&e.rows[j]));}
    }}
    if minimum.is_finite(){Some(minimum)}else{None}
}
fn main(){
    let old=Experiment::new(vec![vec![0.6,0.4],vec![0.4,0.6]]);
    let joint=Experiment::new(vec![vec![0.5,0.0,0.5,0.0],vec![0.5,0.0,0.5,0.0]]);
    let (lhs,rhs)=triangle_bound(&old,&joint,2,2,0,1);
    assert!(approx(lhs,0.2)&&approx(rhs,0.2));
    let fr=frechet_11(0.5,0.5);
    assert!(approx(fr.0,0.0)&&approx(fr.1,0.5));
    println!("P2_TV_BOUND_SHARP old_pair_tv={lhs:.6} bound={rhs:.6}");
    println!("P2_UNPAIRED_BERNOULLI_MARGINALS p11_range=[{:.3},{:.3}]",fr.0,fr.1);
    println!("P2_SCOPE=constructed_finite_laws; pairing/source_transport/field_truth=HOLD");
}
#[cfg(test)]
mod tests{
    use super::*;
    fn eq(a:f64,b:f64){assert!(approx(a,b),"{a} != {b}");}
    #[test]fn error_triangle_constant_two_is_attainable(){
        let old=Experiment::new(vec![vec![0.6,0.4],vec![0.4,0.6]]);
        // Complete new observation has EXACTLY the same law for both theta.
        let joint=Experiment::new(vec![vec![0.5,0.0,0.5,0.0],vec![0.5,0.0,0.5,0.0]]);
        let es=errors(&old,&joint,2,2);
        eq(es[0],0.1);eq(es[1],0.1);
        let (lhs,rhs)=triangle_bound(&old,&joint,2,2,0,1);
        eq(lhs,0.2);eq(rhs,0.2);eq(tv(&joint.rows[0],&joint.rows[1]),0.0);
    }
    #[test]fn gap_greater_than_error_sum_cannot_be_erased(){
        let old=Experiment::new(vec![vec![0.8,0.2],vec![0.2,0.8]]);
        let joint=Experiment::new(vec![vec![0.75,0.0,0.25,0.0],vec![0.25,0.0,0.75,0.0]]);
        let es=errors(&old,&joint,2,2);
        eq(es[0],0.05);eq(es[1],0.05);
        let tv_old=tv(&old.rows[0],&old.rows[1]);let tv_joint=tv(&joint.rows[0],&joint.rows[1]);
        eq(tv_old,0.6);eq(tv_joint,0.5);
        assert!(tv_joint+TOL>=tv_old-es[0]-es[1]);
    }
    #[test]fn marginal_data_do_not_identify_joint_pairing(){
        let corr=Experiment::new(vec![vec![0.5,0.0,0.0,0.5]]);
        let anti=Experiment::new(vec![vec![0.0,0.5,0.5,0.0]]);
        let (y1,z1)=(old_marginal(&corr,2,2),mqr4100_observation_refinement::new_marginal(&corr,2,2));
        let (y2,z2)=(old_marginal(&anti,2,2),mqr4100_observation_refinement::new_marginal(&anti,2,2));
        assert_eq!(y1.rows,y2.rows);assert_eq!(z1.rows,z2.rows);
        eq(tv(&corr.rows[0],&anti.rows[0]),1.0);
        let (lo,hi)=frechet_11(0.5,0.5);
        eq(corr.rows[0][3],hi);eq(anti.rows[0][3],lo);
    }
    #[test]fn selected_pairs_change_old_marginal_and_invalidate_bridge(){
        let old=Experiment::new(vec![vec![0.5,0.5],vec![0.5,0.5]]);
        // A sample retained only for Y=theta (selection varies with latent theta).
        // These are CONDITIONAL selected-sample laws, not an unconditional original protocol.
        let selected=Experiment::new(vec![vec![1.0,0.0,0.0,0.0],vec![0.0,0.0,1.0,0.0]]);
        let es=errors(&old,&selected,2,2);
        eq(es[0],0.5);eq(es[1],0.5);
        assert!(!approx(es[0],0.0));
        eq(tv(&selected.rows[0],&selected.rows[1]),1.0);
    }
    #[test]fn bounded_loss_regret_can_equal_projection_error(){
        // Uniform theta prior; original Y is perfect; new measured Y misses with probability e=0.1.
        let old=Experiment::new(vec![vec![1.0,0.0],vec![0.0,1.0]]);
        let measured=Experiment::new(vec![vec![0.9,0.0,0.1,0.0],vec![0.1,0.0,0.9,0.0]]);
        let e=errors(&old,&measured,2,2);
        eq(e[0],0.1);eq(e[1],0.1);
        let delta_r=binary_classification_risk_uniform(&measured)-binary_classification_risk_uniform(&old);
        eq(delta_r,0.1);assert!(delta_r<=e[0].max(e[1])+TOL);
        // This is a one-sided epsilon degradation receipt, not global Blackwell equivalence.
    }
    #[test]fn fixed_target_margin_is_separate_from_full_parameter_identification(){
        let e=Experiment::new(vec![vec![0.8,0.2],vec![0.8,0.2],vec![0.2,0.8]]);
        eq(target_separation_margin(&e,&[0,0,1]).unwrap(),0.6);
        eq(target_separation_margin(&e,&[0,1,2]).unwrap(),0.0);
        // Under uniform per-parameter error <=0.1, the g=[0,0,1] pairs remain separated.
        let j=Experiment::new(vec![vec![0.7,0.0,0.3,0.0],vec![0.7,0.0,0.3,0.0],vec![0.3,0.0,0.7,0.0]]);
        let es=errors(&e,&j,2,2);
        assert!(es.iter().all(|x|*x<=0.1+TOL));
        assert!(tv(&j.rows[0],&j.rows[2])>=0.6-0.2-TOL);
    }
    #[test]fn identical_symbols_across_target_protocols_do_not_prove_transfer(){
        let source=Experiment::new(vec![vec![1.0,0.0],vec![0.0,1.0]]);
        let target=Experiment::new(vec![vec![0.5,0.5],vec![0.5,0.5]]);
        eq(target_separation_margin(&source,&[0,1]).unwrap(),1.0);
        eq(target_separation_margin(&target,&[0,1]).unwrap(),0.0);
        // Source-to-target Markov kernel and population correspondence not supplied.
    }
    #[test]fn nonuniform_projection_errors_require_pairwise_not_average_budget(){
        let e=Experiment::new(vec![vec![0.7,0.3],vec![0.3,0.7]]);
        let j=Experiment::new(vec![vec![0.5,0.0,0.5,0.0],vec![0.5,0.0,0.5,0.0]]);
        let es=errors(&e,&j,2,2);
        eq(es[0],0.2);eq(es[1],0.2);
        let (a,b)=triangle_bound(&e,&j,2,2,0,1);
        eq(a,0.4);eq(b,0.4);
    }
}
