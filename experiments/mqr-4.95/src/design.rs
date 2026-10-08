//! Classical finite-population sampling design capability checks.
//! These are tiny **mathematical fixtures**, not independent Serov witnesses.
#[derive(Debug, Clone, Copy, PartialEq)]
pub enum Design {
    DeterministicTopK { n: usize, k: usize },
    EqualStrataSrs { units_per_stratum: usize, selected_per_stratum: usize, strata: usize },
}
impl Design {
    fn frame_size(&self)->usize {
        match *self {
            Self::DeterministicTopK{n,..}=>n,
            Self::EqualStrataSrs{units_per_stratum,strata,..}=>units_per_stratum*strata
        }
    }
    pub fn first_order(&self, i:usize)->f64 {
        assert!(i<self.frame_size());
        match *self {
            Self::DeterministicTopK{n,k} => {
                assert!(k<=n);
                if i<k {1.0}else{0.0}
            }
            Self::EqualStrataSrs{units_per_stratum:n,selected_per_stratum:k,..}=>{
                assert!(k<=n && n>0);
                k as f64/n as f64
            }
        }
    }
    pub fn second_order(&self, i:usize,j:usize)->f64 {
        let p1=self.first_order(i);
        if i==j {return p1;}
        let p2=self.first_order(j);
        match *self {
            Self::DeterministicTopK{..}=>p1*p2,
            Self::EqualStrataSrs{units_per_stratum:n,selected_per_stratum:k,..}=>{
                if i/n!=j/n {p1*p2}
                else if n<2 || k<2 {0.0}
                else {(k as f64)*((k-1) as f64)/((n as f64)*((n-1) as f64))}
            }
        }
    }
    pub fn all_first_order_positive(&self)->bool {
        (0..self.frame_size()).all(|i|self.first_order(i)>0.0)
    }
    pub fn all_second_order_positive(&self)->bool {
        (0..self.frame_size()).all(|i| {
            (0..self.frame_size()).all(|j|i==j || self.second_order(i,j)>0.0)
        })
    }
}
pub fn theoretical_design_gate()->(bool,bool,bool) {
    let targeted=Design::DeterministicTopK{n:64,k:4};
    let one=Design::EqualStrataSrs{units_per_stratum:16,selected_per_stratum:1,strata:4};
    let two=Design::EqualStrataSrs{units_per_stratum:16,selected_per_stratum:2,strata:4};
    (!targeted.all_first_order_positive(),
     one.all_first_order_positive()&&!one.all_second_order_positive(),
     two.all_first_order_positive()&&two.all_second_order_positive())
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn first_and_second_order_inclusion_gate() {
        let s=Design::EqualStrataSrs{units_per_stratum:16,selected_per_stratum:1,strata:4};
        assert!((s.first_order(2)-1.0/16.0).abs()<1e-12);
        assert_eq!(s.second_order(2,7),0.0);
        assert!((s.second_order(2,21)-1.0/256.0).abs()<1e-12);
        let two=Design::EqualStrataSrs{units_per_stratum:16,selected_per_stratum:2,strata:4};
        assert!((two.second_order(2,7)-2.0/(16.0*15.0)).abs()<1e-12);
        assert_eq!(theoretical_design_gate(),(true,true,true));
    }
    #[test] fn exact_stratified_ht_design_mean_unbiased_over_all_draws() {
        let losses=[0.2,0.8,1.3,0.5];
        let real_mean=losses.iter().sum::<f64>()/4.0;
        let mut estimates=Vec::new();
        for a in 0..2 {
            for b in 2..4 {
                let ht=((losses[a]/0.5)+(losses[b]/0.5))/4.0;
                estimates.push(ht);
            }
        }
        assert_eq!(estimates.len(),4);
        assert!((estimates.iter().sum::<f64>()/4.0-real_mean).abs()<1e-12);
    }
    #[test] fn identical_sampled_values_different_hidden_population() {
        let a=[0.2,0.8,1.3,0.5];
        let b=[0.2,200.0,1.3,200.0];
        // One-per-stratum sample {0,2} cannot distinguish these worlds.
        assert_eq!((a[0],a[2]),(b[0],b[2]));
        assert!((a.iter().sum::<f64>()-b.iter().sum::<f64>()).abs()>100.0);
    }
}
