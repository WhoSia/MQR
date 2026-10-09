//! MQR-4.99 P1: mathematical scope checks only; not a field-data estimator.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct ThreePositive {
    pub only_first: f64,
    pub only_second: f64,
    pub both: f64,
}

fn valid_probability(x: f64) -> bool { x.is_finite() && (0.0..=1.0).contains(&x) }

/// Shared availability, two conditionally independent observers, no false positives.
/// Returns probabilities of each positive pattern *conditional on at least one detection*.
pub fn zero_truncated_two_observers(
    availability: f64, first: f64, second: f64
) -> Option<ThreePositive> {
    if ![availability, first, second].iter().copied().all(valid_probability) {
        return None;
    }
    let admit = first + second - first * second;
    if availability == 0.0 || admit <= 0.0 { return None; }
    // Availability cancels algebraically; conditioning on a positive pair excludes 00.
    Some(ThreePositive {
        only_first: first * (1.0 - second) / admit,
        only_second: (1.0 - first) * second / admit,
        both: first * second / admit,
    })
}

/// Ideal-population observer detection rates from the positive-only pattern mix.
/// This does NOT identify shared availability.
pub fn positive_overlap_detection(mix: ThreePositive) -> Option<(f64, f64)> {
    let v = [mix.only_first, mix.only_second, mix.both];
    if !v.iter().copied().all(valid_probability) || (v.iter().sum::<f64>() - 1.0).abs() > 1e-9 {
        return None;
    }
    let d1 = mix.only_second + mix.both;
    let d2 = mix.only_first + mix.both;
    if d1 == 0.0 || d2 == 0.0 { return None; }
    Some((mix.both / d1, mix.both / d2))
}

/// Sharp partial-identification interval for p when q=a*p is unconditionally observed
/// against a known common denominator, and independent a lies in [lower, upper].
pub fn sharp_detection_bounds(q: f64, lower: f64, upper: f64) -> Option<(f64, f64)> {
    if ![q, lower, upper].iter().copied().all(valid_probability) || lower > upper {
        return None;
    }
    let amin = lower.max(q);
    if upper < amin { return None; }
    if q == 0.0 {
        // If a=0 could be admitted, p is unconstrained; otherwise p=0.
        return if amin == 0.0 { Some((0.0, 1.0)) } else { Some((0.0, 0.0)) };
    }
    Some((q / upper, q / amin))
}

#[cfg(test)]
mod tests {
    use super::*;
    fn close(a: f64, b: f64) { assert!((a - b).abs() < 1e-12, "{a} != {b}"); }

    #[test]
    fn positivity_only_erases_shared_availability() {
        let x = zero_truncated_two_observers(0.5, 0.6, 0.4).unwrap();
        let y = zero_truncated_two_observers(0.9, 0.6, 0.4).unwrap();
        close(x.only_first, 9.0 / 19.0);
        close(x.only_second, 4.0 / 19.0);
        close(x.both, 6.0 / 19.0);
        assert_eq!(x, y);
    }
    #[test]
    fn overlap_recovers_conditional_observer_rates_only() {
        let mix = zero_truncated_two_observers(0.7, 0.6, 0.4).unwrap();
        let (p1, p2) = positive_overlap_detection(mix).unwrap();
        close(p1, 0.6);
        close(p2, 0.4);
    }
    #[test]
    fn external_availability_interval_yields_sharp_bounds() {
        let (lo, hi) = sharp_detection_bounds(0.35, 0.5, 0.8).unwrap();
        close(lo, 7.0 / 16.0);
        close(hi, 7.0 / 10.0);
    }
    #[test]
    fn invalid_or_nonpositive_denominators_are_not_silently_divided() {
        assert_eq!(zero_truncated_two_observers(0.0, 0.6, 0.4), None);
        assert_eq!(zero_truncated_two_observers(0.5, 0.0, 0.0), None);
        assert_eq!(sharp_detection_bounds(0.7, 0.1, 0.6), None);
        assert_eq!(sharp_detection_bounds(0.0, 0.0, 0.8), Some((0.0, 1.0)));
        assert_eq!(sharp_detection_bounds(0.0, 0.2, 0.8), Some((0.0, 0.0)));
    }
}
