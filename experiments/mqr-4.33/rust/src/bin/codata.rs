use std::{env, fs};

#[derive(Clone, Debug)]
struct Record {
    constant: String,
    year: u32,
    value: f64,
    uncertainty: f64,
}

fn z(a: &Record, b: &Record) -> f64 {
    let denom = (a.uncertainty * a.uncertainty + b.uncertainty * b.uncertainty).sqrt();
    if denom > 0.0 {
        (a.value - b.value).abs() / denom
    } else if a.value == b.value {
        0.0
    } else {
        f64::INFINITY
    }
}

fn state(v: f64) -> &'static str {
    if v <= 1.0 { "PASS" } else { "FAIL" }
}

fn fmt_z(v: f64) -> String {
    if v.is_infinite() {
        "inf".to_owned()
    } else {
        format!("{v:.6}")
    }
}

fn main() {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "experiments/mqr-4.33/codata/codata-values.tsv".to_owned());

    let input = fs::read_to_string(path).unwrap_or_else(|e| {
        eprintln!("{e}");
        std::process::exit(2)
    });

    let mut lines = input.lines();
    let header = lines.next().unwrap_or("");
    if header != "constant\tyear\tvalue\tuncertainty\tunit" {
        eprintln!("unexpected header: {header}");
        std::process::exit(2);
    }

    let mut records = Vec::new();
    let mut constants = Vec::<String>::new();

    for (idx, line) in lines.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 5 {
            eprintln!("line {} has {} columns", idx + 2, p.len());
            std::process::exit(2);
        }
        let constant = p[0].to_owned();
        if !constants.iter().any(|x| x == &constant) {
            constants.push(constant.clone());
        }
        records.push(Record {
            constant,
            year: p[1].parse().unwrap_or_else(|_| {
                eprintln!("invalid year on line {}", idx + 2);
                std::process::exit(2)
            }),
            value: p[2].parse().unwrap_or_else(|_| {
                eprintln!("invalid value on line {}", idx + 2);
                std::process::exit(2)
            }),
            uncertainty: p[3].parse().unwrap_or_else(|_| {
                eprintln!("invalid uncertainty on line {}", idx + 2);
                std::process::exit(2)
            }),
        });
    }

    let triangles = [(2010_u32, 2014_u32, 2018_u32), (2014, 2018, 2022)];

    println!("constant\ttriangle\tz_ab\tz_bc\tz_ac\tab\tbc\tac\tcomposition_candidate");

    let mut candidate_count = 0usize;
    let mut candidate_direct_pass = 0usize;
    let mut candidate_direct_fail = 0usize;

    for constant in constants {
        for (a_year, b_year, c_year) in triangles {
            let get = |year| {
                records
                    .iter()
                    .find(|r| r.constant == constant && r.year == year)
                    .unwrap_or_else(|| {
                        eprintln!("missing {constant} {year}");
                        std::process::exit(2)
                    })
            };
            let a = get(a_year);
            let b = get(b_year);
            let c = get(c_year);

            let z_ab = z(a, b);
            let z_bc = z(b, c);
            let z_ac = z(a, c);
            let ab = state(z_ab);
            let bc = state(z_bc);
            let ac = state(z_ac);
            let candidate = ab == "PASS" && bc == "PASS";

            if candidate {
                candidate_count += 1;
                if ac == "PASS" {
                    candidate_direct_pass += 1;
                } else {
                    candidate_direct_fail += 1;
                }
            }

            println!(
                "{}\t{}-{}-{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                constant,
                a_year,
                b_year,
                c_year,
                fmt_z(z_ab),
                fmt_z(z_bc),
                fmt_z(z_ac),
                ab,
                bc,
                ac,
                if candidate { "YES" } else { "NO" }
            );
        }
    }

    eprintln!("CODATA_TRIANGLES={}", records.len() / 2);
    eprintln!("COMPOSITION_CANDIDATES={candidate_count}");
    eprintln!("CANDIDATE_DIRECT_PASS={candidate_direct_pass}");
    eprintln!("CANDIDATE_DIRECT_FAIL={candidate_direct_fail}");
}
