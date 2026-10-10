//! MQR-4.111 P1: finite synthetic indistinguishability fixtures.
//! No model here is a fitted mineral/thermometer experiment or a new theorem.
//! Rust standard library only. Passing unit tests is not a scientific discovery.
#![forbid(unsafe_code)]

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
enum World { Preexisting, ProbeCreated }

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
struct Record {
    prior_q: usize,
    probe_y: usize,
    marker_m: usize,
    after_visible_reset: usize,
}

/// Eight equiprobable atoms. Marker error probability is true_slots / 4.
/// Assumes a pre-probe, non-perturbing, independently calibrated marker.
fn eight_atoms(world: World, true_slots: usize) -> Vec<Record> {
    assert!(true_slots <= 4);
    let mut out = Vec::with_capacity(8);
    for seed in 0..=1_usize {
        for slot in 0..4 {
            let q = match world {
                World::Preexisting => seed,
                World::ProbeCreated => 0,
            };
            let y = seed;
            let measurement_error = usize::from(slot < true_slots);
            let marker = q ^ measurement_error;
            out.push(Record {
                prior_q: q,
                probe_y: y,
                marker_m: marker,
                after_visible_reset: 0,
            });
        }
    }
    out
}
fn probe_counts(atoms: &[Record]) -> [usize; 2] {
    let mut ans = [0; 2];
    for a in atoms { ans[a.probe_y] += 1; }
    ans
}
fn marker_probe_counts(atoms: &[Record]) -> [[usize; 2]; 2] {
    let mut ans = [[0; 2]; 2];
    for a in atoms { ans[a.marker_m][a.probe_y] += 1; }
    ans
}
fn repeated_probe_reset_counts(atoms: &[Record]) -> [[usize; 2]; 2] {
    let mut ans = [[0; 2]; 2];
    for a in atoms { ans[a.probe_y][a.after_visible_reset] += 1; }
    ans
}
fn prior_counts(atoms: &[Record]) -> [usize; 2] {
    let mut ans = [0; 2];
    for a in atoms { ans[a.prior_q] += 1; }
    ans
}

fn main() {
    let a = eight_atoms(World::Preexisting, 1);
    let b = eight_atoms(World::ProbeCreated, 1);
    println!("MQR-4.111-P1 SYNTHETIC / NOT EMPIRICAL");
    println!("probe A={:?}; B={:?}", probe_counts(&a), probe_counts(&b));
    println!("prior A={:?}; B={:?}", prior_counts(&a), prior_counts(&b));
    println!("pre-marker/probe A={:?}; B={:?}",
        marker_probe_counts(&a), marker_probe_counts(&b));
    println!("visible-reset/probe A={:?}; B={:?}",
        repeated_probe_reset_counts(&a), repeated_probe_reset_counts(&b));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn identical_post_probe_law_with_different_prior_truth() {
        let a = eight_atoms(World::Preexisting, 1);
        let b = eight_atoms(World::ProbeCreated, 1);
        assert_eq!(a.len(), 8);
        assert_eq!(b.len(), 8);
        assert_eq!(probe_counts(&a), [4, 4]);
        assert_eq!(probe_counts(&a), probe_counts(&b));
        assert_eq!(prior_counts(&a), [4, 4]);
        assert_eq!(prior_counts(&b), [8, 0]);
    }

    #[test]
    fn identical_operational_reset_does_not_reconstruct_past() {
        let a = eight_atoms(World::Preexisting, 1);
        let b = eight_atoms(World::ProbeCreated, 1);
        assert_eq!(repeated_probe_reset_counts(&a), [[4, 0], [4, 0]]);
        assert_eq!(repeated_probe_reset_counts(&a), repeated_probe_reset_counts(&b));
        assert_ne!(prior_counts(&a), prior_counts(&b));
    }

    #[test]
    fn independently_calibrated_weak_pre_probe_marker_separates() {
        // Known marker error 1/4, conditionally independent of future probe.
        let a = eight_atoms(World::Preexisting, 1);
        let b = eight_atoms(World::ProbeCreated, 1);
        assert_eq!(marker_probe_counts(&a), [[3, 1], [1, 3]]);
        assert_eq!(marker_probe_counts(&b), [[3, 3], [1, 1]]);
        assert_ne!(marker_probe_counts(&a), marker_probe_counts(&b));
    }

    #[test]
    fn wholly_uninformative_marker_does_not_separate() {
        let a = eight_atoms(World::Preexisting, 2);
        let b = eight_atoms(World::ProbeCreated, 2);
        assert_eq!(marker_probe_counts(&a), [[2, 2], [2, 2]]);
        assert_eq!(marker_probe_counts(&a), marker_probe_counts(&b));
    }
}