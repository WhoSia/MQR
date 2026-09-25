use std::{env, fs, str::FromStr};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum GeneratorRelation {
    SameGenerator,
    BridgeSubsetDirect,
    OverlapNonnested,
    Unknown,
}

impl FromStr for GeneratorRelation {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "SAME_GENERATOR" => Ok(Self::SameGenerator),
            "BRIDGE_SUBSET_DIRECT" => Ok(Self::BridgeSubsetDirect),
            "OVERLAP_NONNESTED" => Ok(Self::OverlapNonnested),
            "UNKNOWN" => Ok(Self::Unknown),
            _ => Err(format!("invalid generator relation: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SemanticMap {
    IdentityOnScope,
    Inclusion,
    ForgetfulSurjection,
    ExplicitPartialMap,
    NoAdmissibleMap,
    Unknown,
}

impl FromStr for SemanticMap {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "IDENTITY_ON_SCOPE" => Ok(Self::IdentityOnScope),
            "INCLUSION" => Ok(Self::Inclusion),
            "FORGETFUL_SURJECTION" => Ok(Self::ForgetfulSurjection),
            "EXPLICIT_PARTIAL_MAP" => Ok(Self::ExplicitPartialMap),
            "NO_ADMISSIBLE_MAP" => Ok(Self::NoAdmissibleMap),
            "UNKNOWN" => Ok(Self::Unknown),
            _ => Err(format!("invalid semantic map: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ComponentRelation {
    SameComponent,
    SameQuotient,
    RefinedComponent,
    ShiftedComponent,
    Unresolved,
}

impl FromStr for ComponentRelation {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "SAME_COMPONENT" => Ok(Self::SameComponent),
            "SAME_QUOTIENT" => Ok(Self::SameQuotient),
            "REFINED_COMPONENT" => Ok(Self::RefinedComponent),
            "SHIFTED_COMPONENT" => Ok(Self::ShiftedComponent),
            "UNRESOLVED_COMPONENT" => Ok(Self::Unresolved),
            _ => Err(format!("invalid component relation: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum QuotientRelation {
    SameQuotient,
    DirectRefinesBridge,
    BridgeRefinesDirect,
    Incommensurable,
    Unknown,
}

impl FromStr for QuotientRelation {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "SAME_QUOTIENT" => Ok(Self::SameQuotient),
            "DIRECT_REFINES_BRIDGE" => Ok(Self::DirectRefinesBridge),
            "BRIDGE_REFINES_DIRECT" => Ok(Self::BridgeRefinesDirect),
            "INCOMMENSURABLE" => Ok(Self::Incommensurable),
            "UNKNOWN_QUOTIENT_RELATION" => Ok(Self::Unknown),
            _ => Err(format!("invalid quotient relation: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum StateRelation {
    ResetEquivalent,
    StateCarried,
    StateTransformed,
    StateIrrelevant,
    Unresolved,
}

impl FromStr for StateRelation {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "RESET_EQUIVALENT" => Ok(Self::ResetEquivalent),
            "STATE_CARRIED" => Ok(Self::StateCarried),
            "STATE_TRANSFORMED" => Ok(Self::StateTransformed),
            "STATE_IRRELEVANT_BY_CONSTRUCTION" => Ok(Self::StateIrrelevant),
            "STATE_UNRESOLVED" => Ok(Self::Unresolved),
            _ => Err(format!("invalid state relation: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EndpointContract {
    Same,
    CoarsePreserved,
    Extended,
    Changed,
    Unresolved,
}

impl FromStr for EndpointContract {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "SAME_ENDPOINT_CONTRACT" => Ok(Self::Same),
            "COARSE_ENDPOINT_PRESERVED" => Ok(Self::CoarsePreserved),
            "ENDPOINT_CONTRACT_EXTENDED" => Ok(Self::Extended),
            "ENDPOINT_CONTRACT_CHANGED" => Ok(Self::Changed),
            "ENDPOINT_CONTRACT_UNRESOLVED" => Ok(Self::Unresolved),
            _ => Err(format!("invalid endpoint contract: {s}")),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Relation {
    R0,
    R1,
    R2,
    R3,
    R4,
    R5,
}

impl Relation {
    fn label(self) -> &'static str {
        match self {
            Self::R0 => "R0_SAME_GENERATOR_HOLDOUT",
            Self::R1 => "R1_STRICT_DOMAIN_EXTENSION",
            Self::R2 => "R2_SUCCESSOR_REFINEMENT",
            Self::R3 => "R3_CONSTITUTIVE_COMPONENT_SHIFT",
            Self::R4 => "R4_OVERLAP_NONNESTED",
            Self::R5 => "R5_UNRESOLVED",
        }
    }

    fn authority(self) -> &'static str {
        match self {
            Self::R0 => "A0_HOLDOUT_SUPPORT_ADMISSIBLE",
            Self::R1 => "A1_EXTENSION_REQUIRES_FRESH_CONTACT",
            Self::R2 => "A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED",
            Self::R3 => "A3_CONSTITUTIVE_BREAK_NO_CANDIDATE",
            Self::R4 => "A4_OVERLAP_HOLD",
            Self::R5 => "A5_RELATION_UNRESOLVED_HOLD",
        }
    }
}

#[derive(Debug)]
struct Row {
    id: String,
    lineage: String,
    generator: GeneratorRelation,
    semantic: SemanticMap,
    component: ComponentRelation,
    quotient: QuotientRelation,
    state: StateRelation,
    endpoint: EndpointContract,
    _decoy: String,
    expected_relation: String,
    expected_authority: String,
    confirmatory: bool,
}

impl Row {
    fn classify(&self) -> Relation {
        if self.component == ComponentRelation::ShiftedComponent
            || self.semantic == SemanticMap::NoAdmissibleMap
            || self.quotient == QuotientRelation::Incommensurable
            || self.endpoint == EndpointContract::Changed
        {
            return Relation::R3;
        }

        if self.generator == GeneratorRelation::OverlapNonnested {
            return Relation::R4;
        }

        if self.generator == GeneratorRelation::Unknown
            || self.semantic == SemanticMap::Unknown
            || self.component == ComponentRelation::Unresolved
            || self.quotient == QuotientRelation::Unknown
            || self.state == StateRelation::Unresolved
            || self.endpoint == EndpointContract::Unresolved
        {
            return Relation::R5;
        }

        if self.generator == GeneratorRelation::BridgeSubsetDirect
            && self.semantic == SemanticMap::ForgetfulSurjection
            && self.component == ComponentRelation::RefinedComponent
            && self.quotient == QuotientRelation::DirectRefinesBridge
            && matches!(
                self.endpoint,
                EndpointContract::CoarsePreserved | EndpointContract::Extended
            )
        {
            return Relation::R2;
        }

        if self.generator == GeneratorRelation::BridgeSubsetDirect {
            return Relation::R1;
        }

        if self.generator == GeneratorRelation::SameGenerator
            && self.semantic == SemanticMap::IdentityOnScope
            && matches!(
                self.component,
                ComponentRelation::SameComponent | ComponentRelation::SameQuotient
            )
            && self.quotient == QuotientRelation::SameQuotient
            && matches!(
                self.state,
                StateRelation::ResetEquivalent | StateRelation::StateIrrelevant
            )
            && self.endpoint == EndpointContract::Same
        {
            return Relation::R0;
        }

        Relation::R5
    }
}

fn parse_bool(s: &str) -> Result<bool, String> {
    match s {
        "1" => Ok(true),
        "0" => Ok(false),
        _ => Err(format!("invalid boolean: {s}")),
    }
}

fn parse(path: &str) -> Result<Vec<Row>, String> {
    let input = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut lines = input.lines();
    let header = lines.next().ok_or("missing header")?;
    let expected = "id\tlineage\tgenerator_relation\tsemantic_map\tcomponent_relation\tquotient_relation\tstate_relation\tendpoint_contract\tdecoy\texpected_relation\texpected_authority\tconfirmatory";
    if header != expected {
        return Err(format!("unexpected header: {header}"));
    }

    let mut rows = Vec::new();
    for (idx, line) in lines.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 12 {
            return Err(format!("line {} has {} columns", idx + 2, p.len()));
        }
        rows.push(Row {
            id: p[0].to_owned(),
            lineage: p[1].to_owned(),
            generator: p[2].parse()?,
            semantic: p[3].parse()?,
            component: p[4].parse()?,
            quotient: p[5].parse()?,
            state: p[6].parse()?,
            endpoint: p[7].parse()?,
            _decoy: p[8].to_owned(),
            expected_relation: p[9].to_owned(),
            expected_authority: p[10].to_owned(),
            confirmatory: parse_bool(p[11])?,
        });
    }
    Ok(rows)
}

fn main() {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "experiments/mqr-4.34/forcing-worlds.tsv".to_owned());

    let rows = parse(&path).unwrap_or_else(|e| {
        eprintln!("{e}");
        std::process::exit(2)
    });

    let mut mismatches = 0usize;
    let mut confirmatory = 0usize;

    for row in &rows {
        let relation = row.classify();
        let authority = relation.authority();
        let matched =
            relation.label() == row.expected_relation && authority == row.expected_authority;
        mismatches += usize::from(!matched);
        confirmatory += usize::from(row.confirmatory);

        println!(
            "RELATION={} lineage={} relation={} authority={} expected_match={}",
            row.id,
            row.lineage,
            relation.label(),
            authority,
            matched
        );
    }

    println!("ROWS={}", rows.len());
    println!("CONFIRMATORY_ROWS={confirmatory}");
    println!("RELATION_EXPECTATION_MISMATCHES={mismatches}");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn row() -> Row {
        Row {
            id: "T".to_owned(),
            lineage: "SYNTHETIC".to_owned(),
            generator: GeneratorRelation::SameGenerator,
            semantic: SemanticMap::IdentityOnScope,
            component: ComponentRelation::SameComponent,
            quotient: QuotientRelation::SameQuotient,
            state: StateRelation::ResetEquivalent,
            endpoint: EndpointContract::Same,
            _decoy: "x".to_owned(),
            expected_relation: "R0_SAME_GENERATOR_HOLDOUT".to_owned(),
            expected_authority: "A0_HOLDOUT_SUPPORT_ADMISSIBLE".to_owned(),
            confirmatory: false,
        }
    }

    #[test]
    fn same_generator_is_r0() {
        assert_eq!(row().classify(), Relation::R0);
    }

    #[test]
    fn strict_extension_is_r1() {
        let mut r = row();
        r.generator = GeneratorRelation::BridgeSubsetDirect;
        r.semantic = SemanticMap::Inclusion;
        r.endpoint = EndpointContract::Extended;
        assert_eq!(r.classify(), Relation::R1);
    }

    #[test]
    fn refinement_is_r2_before_extension() {
        let mut r = row();
        r.generator = GeneratorRelation::BridgeSubsetDirect;
        r.semantic = SemanticMap::ForgetfulSurjection;
        r.component = ComponentRelation::RefinedComponent;
        r.quotient = QuotientRelation::DirectRefinesBridge;
        r.endpoint = EndpointContract::CoarsePreserved;
        assert_eq!(r.classify(), Relation::R2);
    }

    #[test]
    fn component_shift_is_r3() {
        let mut r = row();
        r.component = ComponentRelation::ShiftedComponent;
        r.semantic = SemanticMap::NoAdmissibleMap;
        r.quotient = QuotientRelation::Incommensurable;
        r.endpoint = EndpointContract::Changed;
        assert_eq!(r.classify(), Relation::R3);
    }
}
