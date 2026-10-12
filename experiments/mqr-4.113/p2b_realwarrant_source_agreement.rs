//! MQR-4.113 P2-B — bounded original-publication agreement semantics for Real Lang.
//! Copyright-respecting numeric summary (Bland & Altman 1986), not raw PEFR data.
//! This is an epistemic/ontological separation, not a calibration certificate.
//! No external crates. Standalone rustc entry point; v0.44 remains unpromoted.

use std::{collections::BTreeMap, env, fs};

#[derive(Debug, PartialEq, Eq, Clone, Copy)]
enum Basis { PublishedAggregate, Constructed }
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
enum Calibration { Unverified, DeclaredShared }
#[derive(Debug)]
struct Packet {
    id: String,
    basis: Basis,
    source_doi: String,
    source_drive_id: String,
    quantity: String,
    unit: String,
    source_operation: String,
    target_operation: String,
    calibration: Calibration,
    mean_difference: f64,
    sd_difference: f64,
    correlation: f64,
}
#[derive(Debug)]
struct Verdict {
    limits_95: (f64, f64),
    correlation_is_agreement: bool,
    original_pairwise_data: &'static str,
    sampling_transport: &'static str,
    independent_reference: &'static str,
    physical_measurand_identity: &'static str,
    instrument_substitution: &'static str,
    language_promotion: &'static str,
}

const HEADER: &str = "REALWARRANT 0.44-P2-CANDIDATE";
const FIELDS: &[&str] = &[
    "id", "basis", "source_doi", "source_drive_id", "quantity", "unit",
    "source_operation", "target_operation", "calibration",
    "mean_difference", "sd_difference", "correlation"
];

fn parse(contents: &str) -> Result<Packet, String> {
    let lines: Vec<&str> = contents.lines()
        .map(str::trim).filter(|l| !l.is_empty() && !l.starts_with('#')).collect();
    if lines.first().copied() != Some(HEADER) || lines.last().copied() != Some("END") {
        return Err("INVALID_PACKET_BOUNDARY".into());
    }
    let mut fields = BTreeMap::<String, String>::new();
    for line in &lines[1..lines.len() - 1] {
        let mut iter = line.split_whitespace();
        let key = iter.next().ok_or("EMPTY_FIELD")?;
        let value = iter.next().ok_or("MISSING_FIELD_VALUE")?;
        if iter.next().is_some() || !FIELDS.contains(&key) || value.len() > 256 {
            return Err("UNKNOWN_FIELD_OR_ARITY".into());
        }
        if fields.insert(key.to_owned(), value.to_owned()).is_some() {
            return Err("DUPLICATE_FIELD".into());
        }
    }
    if fields.len() != FIELDS.len() { return Err("REQUIRED_FIELDS_MISSING".into()); }
    let get = |k: &str| -> Result<String, String> {
        fields.get(k).cloned().ok_or_else(|| format!("MISSING_{k}"))
    };
    let basis = match get("basis")?.as_str() {
        "PUBLISHED_AGGREGATE" => Basis::PublishedAggregate,
        "FINITE_CONSTRUCTED" => Basis::Constructed,
        _ => return Err("INVALID_EVIDENCE_BASIS".into()),
    };
    let calibration = match get("calibration")?.as_str() {
        "UNVERIFIED" => Calibration::Unverified,
        "DECLARED_SHARED" => Calibration::DeclaredShared,
        _ => return Err("INVALID_CALIBRATION_STATUS".into()),
    };
    let numeric = |k: &str| -> Result<f64, String> {
        let x = get(k)?.parse::<f64>().map_err(|_| format!("INVALID_{k}"))?;
        if !x.is_finite() { return Err(format!("NONFINITE_{k}")); }
        Ok(x)
    };
    let correlation = numeric("correlation")?;
    let sd_difference = numeric("sd_difference")?;
    if !(-1.0..=1.0).contains(&correlation) || sd_difference <= 0.0 {
        return Err("INVALID_REPORTED_MOMENTS".into());
    }
    let source_doi = get("source_doi")?;
    let source_drive_id = get("source_drive_id")?;
    if basis == Basis::PublishedAggregate &&
       (!source_doi.starts_with("10.") || source_drive_id == "NONE") {
        return Err("PUBLISHED_SUMMARY_REQUIRES_TRACE_POINTER".into());
    }
    if basis == Basis::Constructed &&
       (source_doi != "NONE" || source_drive_id != "NONE") {
        return Err("CONSTRUCTED_SAMPLE_CANNOT_CLAIM_PUBLISHED_SOURCE".into());
    }
    Ok(Packet {
        id: get("id")?, basis, source_doi, source_drive_id,
        quantity: get("quantity")?, unit: get("unit")?,
        source_operation: get("source_operation")?,
        target_operation: get("target_operation")?,
        calibration, mean_difference: numeric("mean_difference")?,
        sd_difference, correlation
    })
}
fn evaluate(p: &Packet) -> Verdict {
    let width = 1.96 * p.sd_difference;
    Verdict {
        limits_95: (p.mean_difference - width, p.mean_difference + width),
        correlation_is_agreement: false,
        original_pairwise_data: "NOT_IN_PACKET",
        sampling_transport: "HOLD_NONPROBABILITY_ILLUSTRATIVE_SAMPLE",
        independent_reference: "HOLD_UNVERIFIED",
        physical_measurand_identity: "HOLD_DECLARATION_ONLY",
        instrument_substitution: "HOLD_NO_PROSPECTIVE_TOLERANCE_OR_EXTERNAL_VALIDATION",
        language_promotion: "UNPROMOTED_CANDIDATE"
    }
}
fn run(contents: &str) -> Result<String, String> {
    let p = parse(contents)?;
    let v = evaluate(&p);
    Ok(format!(
        "packet_id={}\nevidence_basis={:?}\nsource_doi={}\nsource_file_id={}\nquantity={}\nunit={}\noperations={}::{}\ncalibration_claim={:?}\ncorrelation={:.5}\nreported_bias={:.3}\nreported_sd_diff={:.3}\nparametric_loa_95={:.3},{:.3}\ncorrelation_certifies_agreement={}\nraw_paired_values={}\nsampling_transport={}\nindependent_reference={}\nphysical_measurand_identity={}\ninstrument_substitution={}\nreal_language_promotion={}\n",
        p.id, p.basis, p.source_doi, p.source_drive_id, p.quantity,
        p.unit, p.source_operation, p.target_operation, p.calibration,
        p.correlation, p.mean_difference, p.sd_difference,
        v.limits_95.0, v.limits_95.1, v.correlation_is_agreement,
        v.original_pairwise_data, v.sampling_transport, v.independent_reference,
        v.physical_measurand_identity, v.instrument_substitution, v.language_promotion
    ))
}
fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("usage: realwarrant-p2 <packet-file>");
        std::process::exit(2);
    }
    let output = fs::read_to_string(&args[1])
        .map_err(|e| format!("PACKET_IO_{e}"))
        .and_then(|s| run(&s));
    match output { Ok(o) => print!("{o}"), Err(e) => {
        eprintln!("REALWARRANT_REJECTED={e}");
        std::process::exit(2);
    }}
}
#[cfg(test)]
mod tests {
    use super::*;
    fn synthetic() -> String {
        [
            HEADER, "id CASE1", "basis FINITE_CONSTRUCTED",
            "source_doi NONE", "source_drive_id NONE",
            "quantity PEFR", "unit L_per_min",
            "source_operation Wright", "target_operation MiniWright",
            "calibration DECLARED_SHARED", "mean_difference 0",
            "sd_difference 38.8", "correlation 1.0", "END",
        ].join("\n")
    }
    #[test]
    fn finite_summary_has_no_physical_authority() {
        let p = parse(&synthetic()).unwrap();
        let v = evaluate(&p);
        assert!(!v.correlation_is_agreement);
        assert_eq!(v.physical_measurand_identity, "HOLD_DECLARATION_ONLY");
        assert_eq!(v.independent_reference, "HOLD_UNVERIFIED");
    }
    #[test]
    fn exact_source_document_aggregate_recomputes_published_values() {
        let mut txt = synthetic()
            .replace("basis FINITE_CONSTRUCTED", "basis PUBLISHED_AGGREGATE")
            .replace("source_doi NONE", "source_doi 10.1016/S0140-6736(86)90837-8")
            .replace("source_drive_id NONE", "source_drive_id 1HyV_DwLEOoNSHWPah_NUHh9_NKHBxzEe")
            .replace("mean_difference 0", "mean_difference -2.1")
            .replace("correlation 1.0", "correlation 0.94");
        // Textual source pointers are *not* raw-measurement validation.
        let p = parse(&txt).unwrap();
        let v = evaluate(&p);
        assert!((v.limits_95.0 + 78.148).abs() < 1e-9);
        assert!((v.limits_95.1 - 73.948).abs() < 1e-9);
        assert_eq!(v.original_pairwise_data, "NOT_IN_PACKET");
        assert_eq!(v.instrument_substitution, "HOLD_NO_PROSPECTIVE_TOLERANCE_OR_EXTERNAL_VALIDATION");
        txt.push('\n');
    }
    #[test]
    fn perfect_correlation_with_nonzero_disagreement_is_not_agreement() {
        let mut txt = synthetic().replace("mean_difference 0", "mean_difference 100.0");
        let p = parse(&txt).unwrap();
        let v = evaluate(&p);
        assert_eq!(p.correlation, 1.0);
        assert_ne!(v.limits_95.0, 0.0);
        txt.push('\n');
    }
    #[test]
    fn shared_label_is_not_independent_reference() {
        let p = parse(&synthetic()).unwrap();
        assert_eq!(p.calibration, Calibration::DeclaredShared);
        assert_eq!(evaluate(&p).independent_reference, "HOLD_UNVERIFIED");
    }
    #[test]
    fn duplicate_field_rejected() {
        assert_eq!(parse(&synthetic().replace("END","id DUPLICATED\nEND"))
            .unwrap_err(), "DUPLICATE_FIELD");
    }
    #[test]
    fn forged_published_source_without_pointer_rejected() {
        let txt = synthetic().replace("basis FINITE_CONSTRUCTED", "basis PUBLISHED_AGGREGATE");
        assert_eq!(parse(&txt).unwrap_err(), "PUBLISHED_SUMMARY_REQUIRES_TRACE_POINTER");
    }
    #[test]
    fn forbidden_empirical_laundering_rejected() {
        let txt = synthetic().replace("source_doi NONE", "source_doi 10.false/test");
        assert_eq!(parse(&txt).unwrap_err(), "CONSTRUCTED_SAMPLE_CANNOT_CLAIM_PUBLISHED_SOURCE");
    }
    #[test]
    fn nonfinite_values_rejected() {
        assert!(parse(&synthetic().replace("sd_difference 38.8","sd_difference NaN")).is_err());
    }
    #[test]
    fn missing_field_rejected() {
        assert_eq!(parse(&synthetic().replace("unit L_per_min\n","")).unwrap_err(), "REQUIRED_FIELDS_MISSING");
    }
    #[test]
    fn claimed_calibration_certification_not_accepted() {
        assert_eq!(parse(&synthetic().replace("DECLARED_SHARED", "INDEPENDENT_VERIFIED")).unwrap_err(), "INVALID_CALIBRATION_STATUS");
    }
}
