//! MQR-4.113 P2-A: exact constructed calibration-path countermodels.
//! Not measured instrument channels and not a novel statistical theorem.
//! No external crates, no repository writeback.
#[derive(Clone, Copy, Debug)]
struct Kernel {
    num: [[u64; 2]; 2],
    den: u64,
}

impl Kernel {
    fn new(num: [[u64; 2]; 2], den: u64) -> Self {
        assert!(den > 0);
        for row in num {
            assert_eq!(row[0].checked_add(row[1]).expect("overflow"), den);
        }
        Self { num, den }
    }

    fn identity() -> Self {
        Self::new([[1, 0], [0, 1]], 1)
    }

    fn then(&self, next: &Self) -> Self {
        let mut out = [[0u64; 2]; 2];
        for i in 0..2 {
            for j in 0..2 {
                for k in 0..2 {
                    let product = self.num[i][k]
                        .checked_mul(next.num[k][j]).expect("product overflow");
                    out[i][j] = out[i][j]
                        .checked_add(product).expect("sum overflow");
                }
            }
        }
        Self::new(out, self.den.checked_mul(next.den).expect("den overflow"))
    }

    fn statistical_eq(&self, other: &Self) -> bool {
        (0..2).all(|i| (0..2).all(|j| {
            (self.num[i][j] as u128) * (other.den as u128) ==
            (other.num[i][j] as u128) * (self.den as u128)
        }))
    }

    /// Maximum over states of binary-output total-variation distance.
    /// Returns an exact numerator and denominator (not necessarily reduced).
    fn worst_state_tv(&self, other: &Self) -> (u128, u128) {
        let den = (self.den as u128) * (other.den as u128);
        let max_num = (0..2).map(|i| {
            let left = (self.num[i][0] as u128) * (other.den as u128);
            let right = (other.num[i][0] as u128) * (self.den as u128);
            left.abs_diff(right)
        }).max().unwrap();
        (max_num, den)
    }
}

fn noisy_quarter() -> Kernel {
    Kernel::new([[3, 1], [1, 3]], 4)
}

fn one_sided_half() -> Kernel {
    Kernel::new([[2, 0], [1, 1]], 2)
}

fn main() {
    let calibration = noisy_quarter();
    let drift = one_sided_half();
    let forward = calibration.then(&drift);
    let reverse = drift.then(&calibration);
    let (num, den) = forward.worst_state_tv(&reverse);
    println!("scope=FINITE_CONSTRUCTED_CHANNELS_ONLY");
    println!("calibration_then_drift={:?}/{}", forward.num, forward.den);
    println!("drift_then_calibration={:?}/{}", reverse.num, reverse.den);
    println!("worst_state_TV={}/{}", num, den);
    println!("physical_calibration_ancestry=HOLD");
    println!("empirical_measurand_equivalence=HOLD");
    println!("real_language_v044_promotion=UNPROMOTED");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn each_kernel_is_stochastic() {
        let _ = noisy_quarter().then(&one_sided_half());
        let _ = one_sided_half().then(&noisy_quarter());
    }

    #[test]
    fn compositional_identity_is_exact() {
        let c = noisy_quarter();
        assert!(c.then(&Kernel::identity()).statistical_eq(&c));
        assert!(Kernel::identity().then(&c).statistical_eq(&c));
    }

    #[test]
    fn calibration_order_noncommutes_exactly() {
        let c = noisy_quarter();
        let d = one_sided_half();
        let cd = c.then(&d);
        let dc = d.then(&c);
        assert_eq!(cd.num, [[7, 1], [5, 3]]);
        assert_eq!(dc.num, [[6, 2], [4, 4]]);
        assert_eq!(cd.den, 8);
        assert_eq!(dc.den, 8);
        assert!(!cd.statistical_eq(&dc));
        assert_eq!(cd.worst_state_tv(&dc), (8, 64));
    }

    #[test]
    fn different_histories_can_have_exactly_equal_channels() {
        let c = noisy_quarter();
        let two_stages = c.then(&c);
        let one_stage = Kernel::new([[5, 3], [3, 5]], 8);
        assert!(two_stages.statistical_eq(&one_stage));
        assert_eq!(two_stages.worst_state_tv(&one_stage).0, 0);
        assert_ne!(two_stages.den, one_stage.den);
    }

    #[test]
    fn statistical_equality_is_not_ancestry_identity() {
        let a = noisy_quarter().then(&noisy_quarter());
        let b = Kernel::identity().then(&Kernel::new([[5, 3], [3, 5]], 8));
        assert!(a.statistical_eq(&b));
        // These are two different DECLARED paths; no historical source is supplied.
        // This test deliberately makes NO empirical equality assertion.
    }

    #[test]
    #[should_panic]
    fn non_stochastic_row_is_rejected() {
        let _ = Kernel::new([[2, 0], [1, 0]], 2);
    }
}
