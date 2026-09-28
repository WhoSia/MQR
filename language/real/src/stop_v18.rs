use std::{env, fs};

fn yes(b: bool) -> &'static str { if b { "YES" } else { "NO" } }

fn parse_bool(s: &str) -> Result<bool, String> {
    match s {
        "YES" => Ok(true),
        "NO" => Ok(false),
        _ => Err(format!("expected YES/NO, got {s}")),
    }
}

fn main() {
    if let Err(e) = run() {
        eprintln!("REALSTOP_ERROR {e}");
        std::process::exit(2);
    }
}

fn run() -> Result<(), String> {
    let path = env::args().nth(1).ok_or("usage: real-v18-stop <file>")?;
    let src = fs::read_to_string(path).map_err(|e| e.to_string())?;

    let mut header = false;
    let mut ended = false;
    let mut id: Option<String> = None;
    let mut upstream: Option<String> = None;
    let mut oqsc: Option<bool> = None;
    let mut live_debt: Option<bool> = None;
    let mut criterion_invariant: Option<bool> = None;
    let mut break_kind: Option<String> = None;
    let mut confirmation_required: Option<u32> = None;
    let mut eligible_streak: Option<u32> = None;

    for (ln, raw) in src.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if ended { return Err(format!("content after END at line {}", ln + 1)); }
        let t: Vec<&str> = line.split_whitespace().collect();

        if !header {
            if t.as_slice() == ["REALSTOP", "0.18"] {
                header = true;
                continue;
            }
            return Err(format!("expected REALSTOP 0.18 at line {}", ln + 1));
        }

        match t[0] {
            "END" if t.len() == 1 => ended = true,
            "id" if t.len() == 2 => {
                if id.is_some() { return Err("duplicate id".into()); }
                id = Some(t[1].into());
            }
            "upstream" if t.len() == 2 => {
                if upstream.is_some() { return Err("duplicate upstream".into()); }
                if !matches!(t[1], "PASS" | "HOLD" | "REOPEN") {
                    return Err("bad upstream state".into());
                }
                upstream = Some(t[1].into());
            }
            "oqsc" if t.len() == 2 => {
                if oqsc.is_some() { return Err("duplicate oqsc".into()); }
                oqsc = Some(parse_bool(t[1])?);
            }
            "live_debt" if t.len() == 2 => {
                if live_debt.is_some() { return Err("duplicate live_debt".into()); }
                live_debt = Some(parse_bool(t[1])?);
            }
            "criterion_invariant" if t.len() == 2 => {
                if criterion_invariant.is_some() {
                    return Err("duplicate criterion_invariant".into());
                }
                criterion_invariant = Some(parse_bool(t[1])?);
            }
            "break" if t.len() == 2 => {
                if break_kind.is_some() { return Err("duplicate break".into()); }
                if !matches!(t[1], "NONE" | "WORLD_CONTACT" | "DECISION_CONTRACT" | "PATH_CONFLICT") {
                    return Err("bad break kind".into());
                }
                break_kind = Some(t[1].into());
            }
            "confirmation_required" if t.len() == 2 => {
                if confirmation_required.is_some() {
                    return Err("duplicate confirmation_required".into());
                }
                confirmation_required = Some(
                    t[1].parse().map_err(|_| "bad confirmation_required")?
                );
            }
            "eligible_streak" if t.len() == 2 => {
                if eligible_streak.is_some() {
                    return Err("duplicate eligible_streak".into());
                }
                eligible_streak = Some(t[1].parse().map_err(|_| "bad eligible_streak")?);
            }
            _ => return Err(format!("unknown or malformed line {}: {}", ln + 1, line)),
        }
    }

    if !header || !ended { return Err("missing header or END".into()); }
    let _id = id.ok_or("missing id")?;
    let upstream = upstream.ok_or("missing upstream")?;
    let oqsc = oqsc.ok_or("missing oqsc")?;
    let live_debt = live_debt.ok_or("missing live_debt")?;
    let criterion_invariant = criterion_invariant.ok_or("missing criterion_invariant")?;
    let break_kind = break_kind.ok_or("missing break")?;
    let confirmation_required = confirmation_required.ok_or("missing confirmation_required")?;
    let eligible_streak = eligible_streak.ok_or("missing eligible_streak")?;

    if confirmation_required > 3 {
        return Err("confirmation_required outside frozen calibration family".into());
    }

    let eligible =
        upstream == "PASS" &&
        oqsc &&
        !live_debt &&
        criterion_invariant &&
        break_kind == "NONE";

    let action =
        if upstream == "REOPEN" || break_kind != "NONE" {
            "REOPEN"
        } else if eligible && eligible_streak >= confirmation_required + 1 {
            "STOP"
        } else {
            "CONTINUE"
        };

    println!("stop.eligible={}", yes(eligible));
    println!("stop.confirmation_required={confirmation_required}");
    println!("stop.eligible_streak={eligible_streak}");
    println!("stop.action={action}");
    println!("stop.hidden_gold_access=NO");
    println!("stop.future_oracle=NO");
    println!("stop.post_holdout_policy_repair=FORBIDDEN");
    println!("stop.primary_scalar_score=OFF");
    println!("stop.external_calibration=HOLD");
    println!("stop.universal_optimality=FORBIDDEN");
    println!("stop.guidance_mode=CALIBRATED_REOPENABLE_STOP");
    Ok(())
}
