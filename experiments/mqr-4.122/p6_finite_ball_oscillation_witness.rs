//! MQR-4.122 P6: uniform finite-volume emitter, radially occupied toy target.
//! SI lengths in metres. No real BEST geometry, nuclear rates, or empirical fit.
use std::f64::consts::PI;
const A: f64 = 0.05; // uniform source ball radius, metres
const BINS: [(f64, f64); 3] = [(0.20,0.34),(0.34,0.49),(0.49,0.65)];
const AMP: f64 = 0.55;
const KAPPA: f64 = 8.0; // radians/metre; synthetic witness, NOT fitted BEST

fn shell_volume((lo, hi):(f64,f64)) -> f64 {
    (4.0*PI/3.0)*(hi.powi(3)-lo.powi(3))
}
// Average over source radius s and relative polar angle u of r²/|r-s|².
// Valid for r>A; the finite ball's radial density is 3s²/A³.
fn kernel_zero_analytic(r:f64)->f64 {
    assert!(r>A);
    (3.0*r/(2.0*A.powi(3)))*
    (r*A + 0.5*(A*A-r*r)*((r+A)/(r-A)).ln())
}
fn integrate_1d(f:impl Fn(f64)->f64,lo:f64,hi:f64,n:usize)->f64 {
    assert!(n>0);
    let step=(hi-lo)/(n as f64);
    (0..n).map(|i|f(lo+(i as f64+0.5)*step)).sum::<f64>()*step
}
fn kernel_numeric(r:f64,amp:f64,kappa:f64,ns:usize,nu:usize)->f64 {
    assert!(r>A && (0.0..=1.0).contains(&amp));
    let ds=A/(ns as f64);
    let du=2.0/(nu as f64);
    let mut result=0.0;
    for j in 0..ns {
        let s=(j as f64+0.5)*ds;
        let ws=3.0*s*s/(A*A*A)*ds;
        for k in 0..nu {
            let u=-1.0+(k as f64+0.5)*du;
            let d2=r*r+s*s-2.0*r*s*u;
            let d=d2.sqrt();
            let survival=1.0-amp*(kappa*d).sin().powi(2);
            result+=ws*(du/2.0)*(r*r/d2)*survival;
        }
    }
    result
}
fn dot(a:[f64;3],b:[f64;3])->f64 {
    a.iter().zip(b.iter()).map(|(x,y)|x*y).sum()
}
fn cross(a:[f64;3],b:[f64;3])->[f64;3] {
    [a[1]*b[2]-a[2]*b[1],
     a[2]*b[0]-a[0]*b[2],
     a[0]*b[1]-a[1]*b[0]]
}
struct Audit {
    volume:[f64;3], baseline:[f64;3], oscillation:[f64;3],
    plus:[f64;3], minus:[f64;3],
}
fn audit(nr:usize,ns:usize,nu:usize)->Audit {
    let mut volume=[0.0;3];
    let mut baseline=[0.0;3];
    let mut oscillation=[0.0;3];
    for i in 0..3 {
        let (lo,hi)=BINS[i];
        volume[i]=shell_volume((lo,hi));
        baseline[i]=integrate_1d(kernel_zero_analytic,lo,hi,nr);
        oscillation[i]=integrate_1d(
            |r|kernel_numeric(r,AMP,KAPPA,ns,nu),lo,hi,nr);
    }
    let mut h=cross(volume,baseline);
    let maxabs=h.iter().map(|x|x.abs()).fold(0.0_f64,f64::max);
    assert!(maxabs>1.0e-8);
    for value in &mut h {*value/=maxabs;}
    let mut plus=[0.0;3];
    let mut minus=[0.0;3];
    for i in 0..3 {
        plus[i]=0.5+0.3*h[i];
        minus[i]=0.5-0.3*h[i];
        assert!((0.0..=1.0).contains(&plus[i]));
        assert!((0.0..=1.0).contains(&minus[i]));
    }
    Audit{volume,baseline,oscillation,plus,minus}
}
fn difference(a:[f64;3],q:[f64;3],p:[f64;3])->f64 {
    dot(a,q)-dot(a,p)
}
fn print_receipt(a:&Audit) {
    let dv=difference(a.volume,a.plus,a.minus);
    let dl=difference(a.baseline,a.plus,a.minus);
    let dr=difference(a.oscillation,a.plus,a.minus);
    println!("volume={:?}, baseline={:?}, oscillation={:?}",a.volume,a.baseline,a.oscillation);
    println!("q_plus={:?}, q_minus={:?}",a.plus,a.minus);
    println!("delta_volume_m3={dv:.12e}, delta_baseline_m={dl:.12e}, delta_oscillation_m={dr:.12e}");
    assert!(dv.abs()<1e-12);
    assert!(dl.abs()<1e-12);
    assert!(dr.abs()>0.02 && dr.abs()<0.04);
    println!("MQR_4122_P6_FINITE_SOURCE_TOY_SEPARATION=PASS");
    println!("MQR_4122_P6_ACTUAL_BEST_GEOMETRY_REPRODUCTION=HOLD");
}
fn main() {
    let a=audit(160,48,64);
    print_receipt(&a);
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn finite_ball_radial_kernel_exceeds_point_source() {
        for r in [0.20,0.34,0.49,0.65] {
            assert!(kernel_zero_analytic(r)>1.0);
        }
    }
    #[test]
    fn source_normalization_and_analytic_kernel_match() {
        for r in [0.22,0.42,0.62] {
            let n=kernel_numeric(r,0.0,8.0,128,128);
            let exact=kernel_zero_analytic(r);
            assert!((n-exact).abs()<2.0e-5, "{r}: {n} != {exact}");
        }
    }
    #[test]
    fn two_geometries_same_volume_and_baseline() {
        let a=audit(100,40,48);
        assert!(difference(a.volume,a.plus,a.minus).abs()<1e-12);
        assert!(difference(a.baseline,a.plus,a.minus).abs()<1e-12);
    }
    #[test]
    fn oscillation_weight_separates_and_occupancy_is_legal() {
        let a=audit(100,40,48);
        assert!(difference(a.oscillation,a.plus,a.minus).abs()>0.02);
        for q in a.plus.into_iter().chain(a.minus) {
            assert!((0.0..=1.0).contains(&q));
        }
    }
    #[test]
    fn quadrature_refinement_stable() {
        let a=audit(80,32,40);
        let b=audit(160,48,64);
        let x=difference(a.oscillation,a.plus,a.minus);
        let y=difference(b.oscillation,b.plus,b.minus);
        assert!((x-y).abs()<1e-4,"{x} vs {y}");
    }
}
