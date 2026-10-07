use std::{
    collections::BTreeSet,
    env,
    fs,
};

type Pair = (char, char);
type Rel = BTreeSet<Pair>;

fn bit(s: &str) -> bool {
    s == "1"
}

fn parse_edges(s: &str) -> Rel {
    let mut out = Rel::new();
    if s == "-" || s.trim().is_empty() {
        return out;
    }
    for raw in s.split(';') {
        let (a, b) = raw
            .split_once('>')
            .unwrap_or_else(|| panic!("bad edge token: {raw}"));
        let mut ac = a.chars();
        let mut bc = b.chars();
        let x = ac.next().expect("missing lhs");
        let y = bc.next().expect("missing rhs");
        assert!(ac.next().is_none() && bc.next().is_none(), "nodes must be single chars");
        out.insert((x, y));
    }
    out
}

fn relation_from_ranks(nodes: &[char], ranks: &[usize]) -> Rel {
    let mut r = Rel::new();
    for (i, &x) in nodes.iter().enumerate() {
        for (j, &y) in nodes.iter().enumerate() {
            if ranks[i] <= ranks[j] {
                r.insert((x, y));
            }
        }
    }
    r
}

fn is_extension(base: &Rel, nodes: &[char], ext: &Rel) -> bool {
    let mut weak = base.clone();
    for &x in nodes {
        weak.insert((x, x));
    }
    if !weak.is_subset(ext) {
        return false;
    }
    for &(x, y) in base {
        if x != y && !base.contains(&(y, x)) && ext.contains(&(y, x)) {
            return false;
        }
    }
    true
}

fn enumerate_ranks(
    idx: usize,
    nodes: &[char],
    ranks: &mut [usize],
    base: &Rel,
    seen: &mut BTreeSet<Vec<Pair>>,
) {
    if idx == nodes.len() {
        let r = relation_from_ranks(nodes, ranks);
        if is_extension(base, nodes, &r) {
            seen.insert(r.iter().copied().collect());
        }
        return;
    }
    for k in 0..nodes.len() {
        ranks[idx] = k;
        enumerate_ranks(idx + 1, nodes, ranks, base, seen);
    }
}

fn ordering_extensions(base: &Rel, nodes: &[char]) -> Vec<Rel> {
    let mut seen: BTreeSet<Vec<Pair>> = BTreeSet::new();
    let mut ranks = vec![0usize; nodes.len()];
    enumerate_ranks(0, nodes, &mut ranks, base, &mut seen);
    seen.into_iter()
        .map(|v| v.into_iter().collect::<Rel>())
        .collect()
}

fn choice_set(r: &Rel, nodes: &[char]) -> String {
    let mut s = String::new();
    for &x in nodes {
        if nodes.iter().all(|&y| r.contains(&(x, y))) {
            s.push(x);
        }
    }
    s
}

fn added_edges(ext: &Rel, repaired: &Rel) -> Rel {
    ext.iter()
        .copied()
        .filter(|(x, y)| x != y && !repaired.contains(&(*x, *y)))
        .collect()
}

fn common_added_count(exts: &[Rel], repaired: &Rel) -> usize {
    if exts.is_empty() {
        return 0;
    }
    let mut common = added_edges(&exts[0], repaired);
    for r in &exts[1..] {
        let a = added_edges(r, repaired);
        common = common.intersection(&a).copied().collect();
    }
    common.len()
}

fn p_u(s: &str) -> usize {
    s.parse::<usize>()
        .unwrap_or_else(|_| panic!("bad integer: {s}"))
}

fn main() {
    let path = env::args().nth(1).expect("usage: mqr485 COURT-FREEZE.tsv");
    let text = fs::read_to_string(path).expect("read freeze");
    let mut cases = 0usize;
    let mut passed = 0usize;

    let mut nonlift = 0usize;
    let mut positive_lift = 0usize;
    let mut choice_invariance_nonlift = 0usize;
    let mut core_nonlift = 0usize;
    let mut unauthorized_selector = 0usize;
    let mut reopen_cases = 0usize;

    for (line_no, line) in text.lines().enumerate() {
        if line_no == 0 || line.trim().is_empty() {
            continue;
        }
        let c: Vec<&str> = line.split('\t').collect();
        assert_eq!(c.len(), 22, "{}: expected 22 columns, got {}", c[0], c.len());

        let id = c[0];
        let nodes: Vec<char> = c[1].chars().collect();
        assert!((3..=4).contains(&nodes.len()), "{id}: only 3–4 node frozen cases allowed");

        let base = parse_edges(c[2]);
        let add_warrant = parse_edges(c[3]);
        let delete = parse_edges(c[4]);
        let delete_warrant = parse_edges(c[5]);
        let debt_ok = bit(c[6]);
        let scope_ok = bit(c[7]);
        let provenance_ok = bit(c[8]);
        let select_one = bit(c[9]);
        let selector_warrant = bit(c[10]);
        let reopen = c[11];

        assert!(delete.is_subset(&base), "{id}: deletion must target base edge");

        let repaired: Rel = base.difference(&delete).copied().collect();
        let math = ordering_extensions(&repaired, &nodes);

        let math_choices: BTreeSet<String> =
            math.iter().map(|r| choice_set(r, &nodes)).collect();

        let repair_auth =
            delete.is_subset(&delete_warrant) && debt_ok && scope_ok && provenance_ok;

        let wpee: Vec<Rel> = if repair_auth {
            math.iter()
                .filter(|r| added_edges(r, &repaired).is_subset(&add_warrant))
                .cloned()
                .collect()
        } else {
            Vec::new()
        };

        let wpee_choices: BTreeSet<String> =
            wpee.iter().map(|r| choice_set(r, &nodes)).collect();

        let math_core = common_added_count(&math, &repaired);
        let warrant_core = common_added_count(&wpee, &repaired);

        let selection_auth = !select_one || (selector_warrant && !wpee.is_empty());
        let fallback_mwcs = !math.is_empty() && wpee.is_empty();
        let reopen_required = reopen != "none";

        let got = [
            math.len(),
            wpee.len(),
            math_choices.len(),
            wpee_choices.len(),
            math_core,
            warrant_core,
            repair_auth as usize,
            selection_auth as usize,
            fallback_mwcs as usize,
            reopen_required as usize,
        ];

        let expected = [
            p_u(c[12]),
            p_u(c[13]),
            p_u(c[14]),
            p_u(c[15]),
            p_u(c[16]),
            p_u(c[17]),
            p_u(c[18]),
            p_u(c[19]),
            p_u(c[20]),
            p_u(c[21]),
        ];

        let ok = got == expected;
        cases += 1;
        if ok {
            passed += 1;
        } else {
            eprintln!("{id}: expected={expected:?} got={got:?}");
        }

        if !math.is_empty() && wpee.is_empty() {
            nonlift += 1;
        }
        if !wpee.is_empty() {
            positive_lift += 1;
        }
        if math_choices.len() == 1 && !math.is_empty() && wpee.is_empty() {
            choice_invariance_nonlift += 1;
        }
        if math_core > 0 && warrant_core == 0 {
            core_nonlift += 1;
        }
        if select_one && !selection_auth {
            unauthorized_selector += 1;
        }
        if reopen_required {
            reopen_cases += 1;
        }

        println!(
            "{id} math={} wpee={} math_choice_variants={} wpee_choice_variants={} math_core={} warrant_core={} repair_auth={} selection_auth={} fallback_mwcs={} reopen={} {}",
            got[0], got[1], got[2], got[3], got[4], got[5], got[6], got[7], got[8], got[9],
            if ok { "PASS" } else { "FAIL" }
        );
    }

    println!("MQR485_CASES={cases}");
    println!("MQR485_PASS={passed}");
    println!("MQR485_NONLIFT_WITNESSES={nonlift}");
    println!("MQR485_POSITIVE_LIFT_WITNESSES={positive_lift}");
    println!("MQR485_CHOICE_INVARIANCE_NONLIFT_WITNESSES={choice_invariance_nonlift}");
    println!("MQR485_CORE_NONLIFT_WITNESSES={core_nonlift}");
    println!("MQR485_UNAUTHORIZED_SELECTOR_WITNESSES={unauthorized_selector}");
    println!("MQR485_REOPEN_CASES={reopen_cases}");

    let witness_guards =
        nonlift > 0
        && positive_lift > 0
        && choice_invariance_nonlift > 0
        && core_nonlift > 0
        && unauthorized_selector > 0
        && reopen_cases > 0;

    let pass = cases == 20 && passed == cases && witness_guards;
    println!("MQR485_COURT={}", if pass { "PASS" } else { "FAIL" });
    if !pass {
        std::process::exit(1);
    }
}
