use std::{env, fmt, fs, str::FromStr};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EdgeState {
    Pass,
    Fail,
    SplitRequired,
    HoldUntested,
    HoldTargetUnavailable,
    OutOfScope,
}

impl FromStr for EdgeState {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "TRANSPORT_PASS" => Ok(Self::Pass),
            "TRANSPORT_FAIL" => Ok(Self::Fail),
            "SPLIT_REQUIRED" => Ok(Self::SplitRequired),
            "HOLD_UNTESTED" => Ok(Self::HoldUntested),
            "HOLD_TARGET_UNAVAILABLE" => Ok(Self::HoldTargetUnavailable),
            "OUT_OF_SCOPE" => Ok(Self::OutOfScope),
            _ => Err(format!("invalid edge state: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum BridgeClass {
    Exact,
    QuotientCompatible,
    SuccessorRefinement,
    Lossy,
    Noncommensurable,
    Unresolved,
}

impl BridgeClass {
    fn admissible(self) -> bool {
        matches!(
            self,
            Self::Exact | Self::QuotientCompatible | Self::SuccessorRefinement
        )
    }
}

impl FromStr for BridgeClass {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "EXACT" => Ok(Self::Exact),
            "QUOTIENT_COMPATIBLE" => Ok(Self::QuotientCompatible),
            "SUCCESSOR_REFINEMENT" => Ok(Self::SuccessorRefinement),
            "LOSSY" => Ok(Self::Lossy),
            "NONCOMMENSURABLE" => Ok(Self::Noncommensurable),
            "UNRESOLVED" => Ok(Self::Unresolved),
            _ => Err(format!("invalid bridge class: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum PathClass {
    CommutesExact,
    CommutesAtClaimQuotient,
    NoncommutesRefinement,
    NoncommutesLoss,
    NoncommutesOther,
    Untested,
}

impl PathClass {
    fn congruent(self) -> bool {
        matches!(self, Self::CommutesExact | Self::CommutesAtClaimQuotient)
    }
}

impl FromStr for PathClass {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "COMMUTES_EXACT" => Ok(Self::CommutesExact),
            "COMMUTES_AT_CLAIM_QUOTIENT" => Ok(Self::CommutesAtClaimQuotient),
            "NONCOMMUTES_REFINEMENT" => Ok(Self::NoncommutesRefinement),
            "NONCOMMUTES_LOSS" => Ok(Self::NoncommutesLoss),
            "NONCOMMUTES_OTHER" => Ok(Self::NoncommutesOther),
            "UNTESTED" => Ok(Self::Untested),
            _ => Err(format!("invalid path class: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum CompositionState {
    NoCandidate,
    CompositionPass,
    PathDivergentPass,
    NontransitivityWitness,
    CompositionSplitRequired,
    CompositionHoldUntested,
    CompositionHoldTargetUnavailable,
    CompositionOutOfScope,
}

impl fmt::Display for CompositionState {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let s = match self {
            Self::NoCandidate => "NO_CANDIDATE",
            Self::CompositionPass => "COMPOSITION_PASS",
            Self::PathDivergentPass => "PATH_DIVERGENT_PASS",
            Self::NontransitivityWitness => "NONTRANSITIVITY_WITNESS",
            Self::CompositionSplitRequired => "COMPOSITION_SPLIT_REQUIRED",
            Self::CompositionHoldUntested => "COMPOSITION_HOLD_UNTESTED",
            Self::CompositionHoldTargetUnavailable => "COMPOSITION_HOLD_TARGET_UNAVAILABLE",
            Self::CompositionOutOfScope => "COMPOSITION_OUT_OF_SCOPE",
        };
        write!(f, "{s}")
    }
}

#[derive(Debug)]
struct Row {
    id: String,
    lineage: String,
    ab: EdgeState,
    bc: EdgeState,
    bridge_ab: BridgeClass,
    bridge_bc: BridgeClass,
    mid_compatible: bool,
    downstream_distinctions_preserved: bool,
    direct: EdgeState,
    path: PathClass,
    confirmatory: bool,
}

impl Row {
    fn candidate(&self) -> bool {
        self.ab == EdgeState::Pass
            && self.bc == EdgeState::Pass
            && self.bridge_ab.admissible()
            && self.bridge_bc.admissible()
            && self.mid_compatible
            && self.downstream_distinctions_preserved
    }

    fn adjudicate(&self) -> CompositionState {
        if !self.candidate() {
            return CompositionState::NoCandidate;
        }
        match self.direct {
            EdgeState::Pass if self.path.congruent() => CompositionState::CompositionPass,
            EdgeState::Pass => CompositionState::PathDivergentPass,
            EdgeState::Fail => CompositionState::NontransitivityWitness,
            EdgeState::SplitRequired => CompositionState::CompositionSplitRequired,
            EdgeState::HoldUntested => CompositionState::CompositionHoldUntested,
            EdgeState::HoldTargetUnavailable => CompositionState::CompositionHoldTargetUnavailable,
            EdgeState::OutOfScope => CompositionState::CompositionOutOfScope,
        }
    }
}

fn parse_bool(s: &str, name: &str) -> Result<bool, String> {
    match s {
        "1" => Ok(true),
        "0" => Ok(false),
        _ => Err(format!("invalid {name}: {s}; expected 0/1")),
    }
}

fn parse(path: &str) -> Result<Vec<Row>, String> {
    let s = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut it = s.lines();
    let header = it.next().ok_or("missing header")?;
    let expected = "id\tlineage\tab\tbc\tbridge_ab\tbridge_bc\tmid_compatible\tdownstream_distinctions_preserved\tdirect\tpath\tconfirmatory";
    if header != expected {
        return Err(format!("unexpected header: {header}"));
    }

    let mut rows = Vec::new();
    for (i, line) in it.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 11 {
            return Err(format!("line {} has {} columns", i + 2, p.len()));
        }
        rows.push(Row {
            id: p[0].to_owned(),
            lineage: p[1].to_owned(),
            ab: p[2].parse()?,
            bc: p[3].parse()?,
            bridge_ab: p[4].parse()?,
            bridge_bc: p[5].parse()?,
            mid_compatible: parse_bool(p[6], "mid_compatible")?,
            downstream_distinctions_preserved: parse_bool(
                p[7],
                "downstream_distinctions_preserved",
            )?,
            direct: p[8].parse()?,
            path: p[9].parse()?,
            confirmatory: parse_bool(p[10], "confirmatory")?,
        });
    }
    Ok(rows)
}

fn main() {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "experiments/mqr-4.32/synthetic-triangles.tsv".to_owned());

    let rows = parse(&path).unwrap_or_else(|e| {
        eprintln!("{e}");
        std::process::exit(2)
    });

    let mut candidates = 0usize;
    let mut passes = 0usize;
    let mut nontrans = 0usize;
    let mut path_divergent = 0usize;
    let mut holds = 0usize;
    let mut no_candidate = 0usize;
    let mut confirmatory = 0usize;
    let mut research = false;
    let mut engineering = false;

    for row in &rows {
        let candidate = row.candidate();
        let state = row.adjudicate();
        candidates += usize::from(candidate);
        confirmatory += usize::from(row.confirmatory);
        research |= row.confirmatory && row.lineage == "RESEARCH_LAB";
        engineering |= row.confirmatory && row.lineage == "ENGINEERING_DEVELOPMENT";

        match state {
            CompositionState::CompositionPass => passes += 1,
            CompositionState::NontransitivityWitness => nontrans += 1,
            CompositionState::PathDivergentPass => path_divergent += 1,
            CompositionState::CompositionHoldUntested
            | CompositionState::CompositionHoldTargetUnavailable
            | CompositionState::CompositionOutOfScope
            | CompositionState::CompositionSplitRequired => holds += 1,
            CompositionState::NoCandidate => no_candidate += 1,
        }

        println!(
            "TRIANGLE={} lineage={} candidate={} direct={:?} path={:?} composition={}",
            row.id, row.lineage, candidate, row.direct, row.path, state
        );
    }

    println!("TRIANGLES={}", rows.len());
    println!("COMPOSITION_CANDIDATES={candidates}");
    println!("COMPOSITION_PASS_COUNT={passes}");
    println!("NONTRANSITIVITY_WITNESS_COUNT={nontrans}");
    println!("PATH_DIVERGENT_PASS_COUNT={path_divergent}");
    println!("COMPOSITION_HOLD_OR_SPLIT_COUNT={holds}");
    println!("NO_CANDIDATE_COUNT={no_candidate}");
    println!("CONFIRMATORY_TRIANGLES={confirmatory}");
    println!(
        "CROSS_LINEAGE_CONFIRMATORY={}",
        if research && engineering {
            "PASS"
        } else {
            "HOLD"
        }
    );

    let external_ready = confirmatory >= 6
        && research
        && engineering
        && passes >= 1
        && nontrans >= 1
        && path_divergent >= 1;

    println!(
        "MQR432_EXTERNAL_PROMOTION={}",
        if external_ready { "PASS" } else { "HOLD" }
    );
    println!("TRANSPORT_COMPOSITION=PARTIAL_RECEIPT_CONDITIONED");
    println!("GLOBAL_TRANSITIVITY=REJECTED_AS_DEFAULT");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn row(
        ab: EdgeState,
        bc: EdgeState,
        bridge_ab: BridgeClass,
        bridge_bc: BridgeClass,
        mid: bool,
        preserved: bool,
        direct: EdgeState,
        path: PathClass,
    ) -> Row {
        Row {
            id: "T".to_owned(),
            lineage: "OTHER".to_owned(),
            ab,
            bc,
            bridge_ab,
            bridge_bc,
            mid_compatible: mid,
            downstream_distinctions_preserved: preserved,
            direct,
            path,
            confirmatory: false,
        }
    }

    #[test]
    fn pass_plus_pass_does_not_create_pass_without_direct_test() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::Exact,
            BridgeClass::Exact,
            true,
            true,
            EdgeState::HoldUntested,
            PathClass::Untested,
        );
        assert!(r.candidate());
        assert_eq!(r.adjudicate(), CompositionState::CompositionHoldUntested);
    }

    #[test]
    fn lossy_bridge_blocks_candidate() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::Lossy,
            BridgeClass::Exact,
            true,
            true,
            EdgeState::Pass,
            PathClass::CommutesExact,
        );
        assert!(!r.candidate());
        assert_eq!(r.adjudicate(), CompositionState::NoCandidate);
    }

    #[test]
    fn missing_successor_distinction_blocks_candidate() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::SuccessorRefinement,
            BridgeClass::Exact,
            true,
            false,
            EdgeState::Pass,
            PathClass::CommutesExact,
        );
        assert!(!r.candidate());
    }

    #[test]
    fn adjacent_pass_with_direct_fail_is_nontransitivity_witness() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::Exact,
            BridgeClass::QuotientCompatible,
            true,
            true,
            EdgeState::Fail,
            PathClass::NoncommutesOther,
        );
        assert_eq!(r.adjudicate(), CompositionState::NontransitivityWitness);
    }

    #[test]
    fn direct_pass_does_not_imply_path_equivalence() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::Exact,
            BridgeClass::SuccessorRefinement,
            true,
            true,
            EdgeState::Pass,
            PathClass::NoncommutesRefinement,
        );
        assert_eq!(r.adjudicate(), CompositionState::PathDivergentPass);
    }

    #[test]
    fn quotient_commutation_can_support_scoped_composition() {
        let r = row(
            EdgeState::Pass,
            EdgeState::Pass,
            BridgeClass::QuotientCompatible,
            BridgeClass::QuotientCompatible,
            true,
            true,
            EdgeState::Pass,
            PathClass::CommutesAtClaimQuotient,
        );
        assert_eq!(r.adjudicate(), CompositionState::CompositionPass);
    }
}
