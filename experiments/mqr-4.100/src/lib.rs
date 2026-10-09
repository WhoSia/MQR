//! MQR-4.100-P1: finite stochastic-experiment regression witnesses.
//! These are elementary known structures, not a new statistical theorem or field estimate.
#[derive(Clone, Debug)]
pub struct Experiment {
    /// One probability mass function per *fixed*, shared parameter value.
    pub rows: Vec<Vec<f64>>,
}
fn close(a:f64,b:f64)->bool { (a-b).abs()<1e-10 }
impl Experiment {
    pub fn new(rows:Vec<Vec<f64>>)->Self {
        assert!(!rows.is_empty());
        let width=rows[0].len();
        assert!(width>0 && rows.iter().all(|r| r.len()==width));
        assert!(rows.iter().all(|r| {
            r.iter().all(|v|v.is_finite() && *v>=0.0 && *v<=1.0)
            && close(r.iter().sum(),1.0)
        }),"Each row must be a proper probability mass function");
        Self{rows}
    }
    pub fn equiv(&self, a:usize, b:usize)->bool {
        self.rows[a].iter().zip(&self.rows[b]).all(|(x,y)|close(*x,*y))
    }
    pub fn classes(&self)->Vec<Vec<usize>> {
        let mut c:Vec<Vec<usize>>=Vec::new();
        for i in 0..self.rows.len() {
            if let Some(cl)=c.iter_mut().find(|cl|self.equiv(i,cl[0])) { cl.push(i) }
            else { c.push(vec![i]); }
        }
        c
    }
    pub fn identifies(&self,target:&[usize])->bool {
        assert_eq!(self.rows.len(),target.len());
        (0..self.rows.len()).all(|i|(0..self.rows.len()).all(|j|
            !self.equiv(i,j) || target[i]==target[j]))
    }
}
/// Joint arrays are indexed y*new_outcomes+z, requiring actual PAIR-MATCHED observation.
pub fn old_marginal(joint:&Experiment, old_outcomes:usize, new_outcomes:usize)->Experiment{
    assert!(old_outcomes>0&&new_outcomes>0);
    assert_eq!(joint.rows[0].len(),old_outcomes*new_outcomes);
    Experiment::new(joint.rows.iter().map(|row|{
        (0..old_outcomes).map(|y|(0..new_outcomes).map(|z|
            row[y*new_outcomes+z]).sum()).collect()
    }).collect())
}
pub fn new_marginal(joint:&Experiment, old_outcomes:usize, new_outcomes:usize)->Experiment{
    assert!(old_outcomes>0&&new_outcomes>0);
    assert_eq!(joint.rows[0].len(),old_outcomes*new_outcomes);
    Experiment::new(joint.rows.iter().map(|row|{
        (0..new_outcomes).map(|z|(0..old_outcomes).map(|y|
            row[y*new_outcomes+z]).sum()).collect()
    }).collect())
}
/// Compares equivalence on EXACTLY the same parameter domain and marginal-compatible kernels.
pub fn same_domain_refinement(old:&Experiment,joint:&Experiment,new_outcomes:usize)->(bool,bool){
    assert_eq!(old.rows.len(),joint.rows.len());
    let p=old_marginal(joint,old.rows[0].len(),new_outcomes);
    assert!(old.rows.iter().zip(p.rows.iter()).all(|(a,b)|
        a.iter().zip(b).all(|(x,y)|close(*x,*y))),"Old kernel not the projection of joint");
    let mut strict=false;
    for i in 0..old.rows.len() {for j in 0..old.rows.len(){
        if joint.equiv(i,j)&&!old.equiv(i,j){return (false,false);}
        if old.equiv(i,j)&&!joint.equiv(i,j){strict=true;}
    }}
    (true,strict)
}
/// Bayes optimal 0-1 state-classification accuracy for a UNIFORM prior over theta.
pub fn classification_accuracy_uniform(e:&Experiment)->f64{
    let n=e.rows.len();
    (0..e.rows[0].len()).map(|z|
        e.rows.iter().map(|row|row[z]).fold(0.0_f64,f64::max)
    ).sum::<f64>()/n as f64
}
#[cfg(test)]
mod tests{
    use super::*;
    fn verify(a:f64,b:f64){assert!(close(a,b),"{a} != {b}");}
    #[test]fn zero_information_auxiliary_can_be_exact_duplicate(){
        let old=Experiment::new(vec![vec![0.6,0.4],vec![0.4,0.6]]);
        let joint=Experiment::new(vec![vec![0.6,0.0,0.0,0.4],vec![0.4,0.0,0.0,0.6]]);
        assert_eq!(same_domain_refinement(&old,&joint,2),(true,false));
        verify(classification_accuracy_uniform(&old),0.6);
        verify(classification_accuracy_uniform(&joint),0.6);
    }
    #[test]fn joint_pairing_refines_when_each_separate_marginal_does_not(){
        // Theta 0: perfectly correlated; theta 1: perfectly anticorrelated.
        let joint=Experiment::new(vec![vec![0.5,0.0,0.0,0.5],vec![0.0,0.5,0.5,0.0]]);
        let old=old_marginal(&joint,2,2);
        let auxiliary=new_marginal(&joint,2,2);
        assert!(old.equiv(0,1)&&auxiliary.equiv(0,1)&&!joint.equiv(0,1));
        assert_eq!(same_domain_refinement(&old,&joint,2),(true,true));
        assert_eq!(old.classes(),vec![vec![0,1]]);
        assert_eq!(joint.classes(),vec![vec![0],vec![1]]);
        verify(classification_accuracy_uniform(&old),0.5);
        verify(classification_accuracy_uniform(&joint),1.0);
    }
    #[test]fn quotient_equality_does_not_entail_equal_blackwell_decision_value(){
        // Both old and joint already separate theta, thus quotient does NOT strictly refine.
        let old=Experiment::new(vec![vec![0.6,0.4],vec![0.4,0.6]]);
        let joint=Experiment::new(vec![vec![0.6,0.0,0.4,0.0],vec![0.0,0.4,0.0,0.6]]);
        assert_eq!(same_domain_refinement(&old,&joint,2),(true,false));
        assert_eq!(old.classes(),joint.classes());
        verify(classification_accuracy_uniform(&old),0.6);
        verify(classification_accuracy_uniform(&joint),1.0);
    }
    #[test]fn different_model_class_not_a_valid_auxiliary_refinement(){
        // Old E: y=theta. New model enlarges parameter space theta x eta and y=theta XOR eta.
        // These are different marginal models; missing projection/parameter bridge is a real failure.
        let old=Experiment::new(vec![vec![1.0,0.0],vec![0.0,1.0]]);
        let relaxed=Experiment::new(vec![
            vec![1.0,0.0], // theta0 eta0
            vec![0.0,1.0], // theta0 eta1
            vec![0.0,1.0], // theta1 eta0
            vec![1.0,0.0], // theta1 eta1
        ]);
        assert!(old.identifies(&[0,1]));
        assert!(!relaxed.identifies(&[0,0,1,1]));
        assert!(relaxed.equiv(0,3));
        assert_ne!(old.rows.len(),relaxed.rows.len()); // thus no naive joint-refinement comparison
    }
    #[test]fn assumption_only_submodel_shrinks_feasible_parameter_family_without_new_data(){
        let old=Experiment::new(vec![vec![0.5,0.5],vec![0.5,0.5]]);
        assert!(!old.identifies(&[0,1]));
        let restricted=Experiment::new(vec![old.rows[0].clone()]);
        assert!(restricted.identifies(&[0])); // domain was restricted, no new signal
    }
    #[test]fn parameter_separation_can_improve_without_target_function_gain(){
        let joint=Experiment::new(vec![vec![1.0,0.0,0.0,0.0],
            vec![0.0,1.0,0.0,0.0],vec![0.0,0.0,1.0,0.0]]);
        let old=old_marginal(&joint,2,2);
        assert_eq!(same_domain_refinement(&old,&joint,2),(true,true));
        assert!(old.identifies(&[0,0,1]));
        assert!(joint.identifies(&[0,0,1]));
        assert!(!old.identifies(&[0,1,2]));
        assert!(joint.identifies(&[0,1,2]));
    }
    #[test]fn external_protocol_transport_is_not_licensed_by_source_identification(){
        let source=Experiment::new(vec![vec![1.0,0.0],vec![0.0,1.0]]);
        let target=Experiment::new(vec![vec![0.5,0.5],vec![0.5,0.5]]);
        assert!(source.identifies(&[0,1])&&!target.identifies(&[0,1]));
        // No relation between these kernels is asserted; same labels do not establish a bridge.
    }
}
