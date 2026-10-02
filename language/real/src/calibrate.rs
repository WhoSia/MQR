use std::{env, fs};

fn ratio(a: &str, b: &str) -> Result<f64, String> {
    let x: f64 = a.parse().map_err(|_| format!("bad number: {a}"))?;
    let y: f64 = b.parse().map_err(|_| format!("bad number: {b}"))?;
    if y <= 0.0 {
        return Err("nonpositive denominator".into());
    }
    Ok(x / y)
}

fn main() {
    let path = env::args().nth(1).unwrap_or_else(|| {
        eprintln!("usage: real-calibrate PUBLIC.tsv");
        std::process::exit(2)
    });
    let text = fs::read_to_string(&path).unwrap_or_else(|e| {
        eprintln!("{path}: {e}");
        std::process::exit(1)
    });
    let mut it = text.lines();
    let head = it.next().unwrap_or("");
    let expected = "lane	id	w_success	w_total	w_repeat_decoy	n_lineages	n_replicate_decoy	i_invariant	i_total	i_rival_count_decoy	t_success	t_total	t_train_decoy	d_covered	d_total	d_challenge_decoy";
    if head != expected {
        eprintln!("unexpected header");
        std::process::exit(1)
    }
    println!("id	W	N	I	T	D");
    for (ln, line) in it.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let f: Vec<&str> = line.split('\t').collect();
        if f.len() != 16 {
            eprintln!("line {}: expected 16 fields", ln + 2);
            std::process::exit(1)
        }
        let lane = f[0];
        let id = f[1];
        let w = ratio(f[2], f[3]).unwrap_or_else(|e| {
            eprintln!("{id}: {e}");
            std::process::exit(1)
        });
        let nden = if lane == "exact" {
            4.0
        } else if lane == "noisy" {
            64.0
        } else {
            eprintln!("{id}: bad lane");
            std::process::exit(1)
        };
        let n: f64 = f[5].parse::<f64>().unwrap_or_else(|_| {
            eprintln!("{id}: bad n_lineages");
            std::process::exit(1)
        }) / nden;
        let i = ratio(f[7], f[8]).unwrap_or_else(|e| {
            eprintln!("{id}: {e}");
            std::process::exit(1)
        });
        let t = ratio(f[10], f[11]).unwrap_or_else(|e| {
            eprintln!("{id}: {e}");
            std::process::exit(1)
        });
        let d = ratio(f[13], f[14]).unwrap_or_else(|e| {
            eprintln!("{id}: {e}");
            std::process::exit(1)
        });
        println!("{id}	{w:.6}	{n:.6}	{i:.6}	{t:.6}	{d:.6}");
    }
}
