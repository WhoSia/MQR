use std::{env, fmt, fs, str::FromStr};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EdgeState {
    Pass,
    Fail,
    SplitRequired,
    Hold,
}

impl FromStr for EdgeState {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "TRANSPORT_PASS" => Ok(Self::Pass),
            "TRANSPORT_FAIL" => Ok(Self::Fail),
            "SPLIT_REQUIRED" => Ok(Self::SplitRequired),
            "HOLD" => Ok(Self::Hold),
            _ => Err(format!("invalid edge state: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum PathClass {
    Commutes,
    Diverges,
    Untested,
}

impl FromStr for PathClass {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "COMMUTES" => Ok(Self::Commutes),
            "DIVERGES" => Ok(Self::Diverges),
            "UNTESTED" => Ok(Self::Untested),
            _ => Err(format!("invalid path class: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SupportClass {
    StrictSupport,
    GeneralizationRisk,
    PathRisk,
    Unresolved,
}

impl FromStr for SupportClass {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "S0_STRICT_SUPPORT" => Ok(Self::StrictSupport),
            "S1_GENERALIZATION_RISK" => Ok(Self::GeneralizationRisk),
            "S2_PATH_RISK" => Ok(Self::PathRisk),
            "S3_UNRESOLVED" => Ok(Self::Unresolved),
            _ => Err(format!("invalid support class: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum CompositionState {
    NoCandidate,
    CompositionPass,
    NontransitivityWitness,
    PathDivergentPass,
    CompositionSplitRequired,
    Hold,
}

impl fmt::Display for CompositionState {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let s = match self {
            Self::NoCandidate => "NO_CANDIDATE",
            Self::CompositionPass => "COMPOSITION_PASS",
            Self::NontransitivityWitness => "NONTRANSITIVITY_WITNESS",
            Self::PathDivergentPass => "PATH_DIVERGENT_PASS",
            Self::CompositionSplitRequired => "COMPOSITION_SPLIT_REQUIRED",
            Self::Hold => "HOLD",
        };
        write!(f, "{s}")
    }
}

#[derive(Debug)]
struct Row {
    id: String,
    lineage: String,
    support: SupportClass,
    ab: EdgeState,
    bc: EdgeState,
    direct: EdgeState,
    path: PathClass,
    component_identity: bool,
    direct_independent: bool,
    domain_covered: bool,
    information_preserved: bool,
    state_reset: bool,
    adapter_commutative: bool,
    confirmatory: bool,
}

impl Row {
    fn candidate(&self) -> bool {
        self.ab == EdgeState::Pass
            && self.bc == EdgeState::Pass
            && self.component_identity
            && self.direct_independent
    }

    fn adjudicate(&self) -> CompositionState {
        if !self.candidate() {
            return CompositionState::NoCandidate;
        }
        match (self.direct, self.path) {
            (EdgeState::Pass, PathClass::Commutes) => CompositionState::CompositionPass,
            (EdgeState::Pass, PathClass::Diverges) => CompositionState::PathDivergentPass,
            (EdgeState::Fail, _) => CompositionState::NontransitivityWitness,
            (EdgeState::SplitRequired, _) => CompositionState::CompositionSplitRequired,
            (EdgeState::Hold, _) | (EdgeState::Pass, PathClass::Untested) => CompositionState::Hold,
        }
    }

    fn structural_class_valid(&self) -> bool {
        match self.support {
            SupportClass::StrictSupport => {
                self.domain_covered
                    && self.information_preserved
                    && self.state_reset
                    && self.adapter_commutative
                    && self.component_identity
                    && self.direct_independent
            }
            SupportClass::GeneralizationRisk => {
                !self.domain_covered && self.component_identity && self.direct_independent
            }
            SupportClass::PathRisk => {
                (!self.information_preserved || !self.state_reset || !self.adapter_commutative)
                    && self.component_identity
                    && self.direct_independent
            }
            SupportClass::Unresolved => true,
        }
    }

    fn prediction_matches(&self, state: CompositionState) -> bool {
        match self.support {
            SupportClass::StrictSupport => state == CompositionState::CompositionPass,
            SupportClass::GeneralizationRisk => state == CompositionState::NontransitivityWitness,
            SupportClass::PathRisk => matches!(
                state,
                CompositionState::PathDivergentPass | CompositionState::CompositionSplitRequired
            ),
            SupportClass::Unresolved => true,
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
    let mut lines = s.lines();
    let header = lines.next().ok_or("missing header")?;
    let expected = "id\tlineage\tsupport\tab\tbc\tdirect\tpath\tcomponent_identity\tdirect_independent\tdomain_covered\tinformation_preserved\tstate_reset\tadapter_commutative\tconfirmatory";
    if header != expected {
        return Err(format!("unexpected header: {header}"));
    }

    let mut rows = Vec::new();
    for (i, line) in lines.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 14 {
            return Err(format!("line {} has {} columns", i + 2, p.len()));
        }
        rows.push(Row {
            id: p[0].to_owned(),
            lineage: p[1].to_owned(),
            support: p[2].parse()?,
            ab: p[3].parse()?,
            bc: p[4].parse()?,
            direct: p[5].parse()?,
            path: p[6].parse()?,
            component_identity: parse_bool(p[7], "component_identity")?,
            direct_independent: parse_bool(p[8], "direct_independent")?,
            domain_covered: parse_bool(p[9], "domain_covered")?,
            information_preserved: parse_bool(p[10], "information_preserved")?,
            state_reset: parse_bool(p[11], "state_reset")?,
            adapter_commutative: parse_bool(p[12], "adapter_commutative")?,
            confirmatory: parse_bool(p[13], "confirmatory")?,
        });
    }
    Ok(rows)
}

fn main() {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "experiments/mqr-4.33/forcing-worlds.tsv".to_owned());
    let rows = parse(&path).unwrap_or_else(|e| {
        eprintln!("{e}");
        std::process::exit(2)
    });

    let mut forcing_mismatches = 0usize;
    let mut structural_mismatches = 0usize;
    let mut confirmatory = 0usize;
    let mut strict_support = 0usize;
    let mut strict_false_safe = 0usize;
    let mut nontrans = 0usize;
    let mut path_risk_hits = 0usize;
    let mut engineering_confirmatory = 0usize;
    let mut research_lab_confirmatory = 0usize;

    for row in &rows {
        let state = row.adjudicate();
        let structural_valid = row.structural_class_valid();
        let prediction_match = row.prediction_matches(state);

        structural_mismatches += usize::from(!structural_valid);
        forcing_mismatches += usize::from(!prediction_match);

        if row.confirmatory {
            confirmatory += 1;
            engineering_confirmatory += usize::from(row.lineage == "ENGINEERING_DEVELOPMENT");
            research_lab_confirmatory += usize::from(row.lineage == "RESEARCH_LAB");
        }
        if row.support == SupportClass::StrictSupport && row.confirmatory {
            strict_support += 1;
            strict_false_safe += usize::from(state != CompositionState::CompositionPass);
        }
        nontrans +=
            usize::from(row.confirmatory && state == CompositionState::NontransitivityWitness);
        path_risk_hits += usize::from(
            row.confirmatory
                && matches!(
                    state,
                    CompositionState::PathDivergentPass
                        | CompositionState::CompositionSplitRequired
                ),
        );

        println!(
            "TRIANGLE={} lineage={} support={:?} candidate={} structural_valid={} direct={:?} path={:?} composition={} prediction_match={}",
            row.id,
            row.lineage,
            row.support,
            row.candidate(),
            structural_valid,
            row.direct,
            row.path,
            state,
            prediction_match
        );
    }

    let support_discovered = confirmatory >= 6
        && engineering_confirmatory >= 2
        && research_lab_confirmatory >= 2
        && strict_support >= 2
        && strict_false_safe == 0
        && nontrans >= 1
        && path_risk_hits >= 1
        && structural_mismatches == 0
        && forcing_mismatches == 0;

    println!("TRIANGLES={}", rows.len());
    println!("FORCING_EXPECTATION_MISMATCHES={forcing_mismatches}");
    println!("STRUCTURAL_CLASS_MISMATCHES={structural_mismatches}");
    println!("CONFIRMATORY_TRIANGLES={confirmatory}");
    println!("ENGINEERING_CONFIRMATORY={engineering_confirmatory}");
    println!("RESEARCH_LAB_CONFIRMATORY={research_lab_confirmatory}");
    println!("STRICT_SUPPORT_CONFIRMATORY={strict_support}");
    println!("STRICT_SUPPORT_FALSE_SAFE={strict_false_safe}");
    println!("NONTRANSITIVITY_WITNESS_COUNT={nontrans}");
    println!("PATH_RISK_HIT_COUNT={path_risk_hits}");
    println!(
        "SUPPORT_DOMAIN_DISCOVERY={}",
        if support_discovered { "PASS" } else { "HOLD" }
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    fn base() -> Row {
        Row {
            id: "T".into(),
            lineage: "SYNTHETIC".into(),
            support: SupportClass::StrictSupport,
            ab: EdgeState::Pass,
            bc: EdgeState::Pass,
            direct: EdgeState::Pass,
            path: PathClass::Commutes,
            component_identity: true,
            direct_independent: true,
            domain_covered: true,
            information_preserved: true,
            state_reset: true,
            adapter_commutative: true,
            confirmatory: false,
        }
    }

    #[test]
    fn strict_support_requires_all_structural_guards() {
        let mut r = base();
        assert!(r.structural_class_valid());
        r.domain_covered = false;
        assert!(!r.structural_class_valid());
    }

    #[test]
    fn coverage_failure_is_nontransitivity_witness() {
        let mut r = base();
        r.support = SupportClass::GeneralizationRisk;
        r.domain_covered = false;
        r.direct = EdgeState::Fail;
        r.path = PathClass::Untested;
        assert_eq!(r.adjudicate(), CompositionState::NontransitivityWitness);
        assert!(r.prediction_matches(r.adjudicate()));
    }

    #[test]
    fn direct_pass_can_still_be_path_divergent() {
        let mut r = base();
        r.support = SupportClass::PathRisk;
        r.adapter_commutative = false;
        r.path = PathClass::Diverges;
        assert_eq!(r.adjudicate(), CompositionState::PathDivergentPass);
        assert!(r.prediction_matches(r.adjudicate()));
    }

    #[test]
    fn lossy_path_can_require_split() {
        let mut r = base();
        r.support = SupportClass::PathRisk;
        r.information_preserved = false;
        r.direct = EdgeState::SplitRequired;
        r.path = PathClass::Diverges;
        assert_eq!(r.adjudicate(), CompositionState::CompositionSplitRequired);
        assert!(r.prediction_matches(r.adjudicate()));
    }
}
