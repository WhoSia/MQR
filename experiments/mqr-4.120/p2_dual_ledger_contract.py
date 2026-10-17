"""MQR-4.120 P2 finite dual-ledger contract checker. No scientific certification."""
STATUSES = {"PASS", "FAIL", "HOLD", "OUT_OF_SCOPE"}
def validate(c):
    errors = []
    required = ("id", "origin", "claim_scope", "j1", "j2", "dissent", "alternative_question", "reopening_trigger")
    errors += ["missing:" + k for k in required if k not in c]
    if errors: return sorted(errors)
    if c["origin"] != "CONSTRUCTED": errors.append("origin:not_constructed")
    for side in ("j1", "j2"):
        d = c[side]
        errors += [side + ":missing_" + k for k in ("status", "reasons", "scope", "basis") if not d.get(k)]
        if d.get("status") not in STATUSES: errors.append(side + ":bad_status")
    a, b = c["j1"], c["j2"]
    if a.get("physical_traceability_claim") and a.get("status") == "PASS" and not a.get("independent_custody_verified"):
        errors.append("j1:traceability_without_custody")
    if a.get("unresolved_discriminator") and a.get("status") == "PASS":
        errors.append("j1:unresolved_alternative")
    if b.get("status") == "PASS" and b.get("self_authorized") and not b.get("external_mandate_verified"):
        errors.append("j2:self_certification")
    if b.get("status") == "PASS" and not b.get("challenge_route"):
        errors.append("j2:missing_challenge_route")
    if c.get("agreement_count", 0) and b.get("basis") == "vote_count_only":
        errors.append("j2:majority_as_authority")
    if c["dissent"] and not c["alternative_question"]:
        errors.append("dissent:question_elided")
    return sorted(errors)

def case(id, j1, j2, **kw):
    return dict(id=id, origin="CONSTRUCTED", claim_scope="hypothetical", j1=j1,
                j2=j2, dissent=kw.pop("dissent", ""), alternative_question=kw.pop("alternative_question", "n/a"),
                reopening_trigger="new material evidence", **kw)
def judgment(status, **extra):
    return dict(status=status, reasons="stipulated hypothetical reasons", scope="bounded", basis="constructed assumption", **extra)
def check():
    cases = [
        (case("DC1", judgment("PASS"), judgment("HOLD")), False),
        (case("DC2", judgment("HOLD", unresolved_discriminator=True), judgment("PASS", challenge_route="appeal")), False),
        (case("DC3", judgment("PASS"), judgment("FAIL"), dissent="excluded query", alternative_question="who sets scope?"), False),
        (case("DC4", judgment("PASS"), judgment("PASS", challenge_route="external appeal")), False),
        (case("BAD_TRACE", judgment("PASS", physical_traceability_claim=True), judgment("HOLD")), True),
        (case("BAD_UNCERTAINTY", judgment("PASS", unresolved_discriminator=True), judgment("HOLD")), True),
        (case("BAD_SELF", judgment("PASS"), judgment("PASS", self_authorized=True, basis="vote_count_only"),
              agreement_count=3), True),
        (case("BAD_DISSENT", judgment("PASS"), judgment("HOLD"), dissent="excluded", alternative_question=""), True),
    ]
    assert len(cases) == 8
    for obj, reject in cases:
        flags = validate(obj)
        assert bool(flags) == reject, (obj["id"], flags)
        print(obj["id"], "REJECT" if flags else "ACCEPT", flags)
    print("PASS: 8 constructed contract examples; not scientific validation")
if __name__ == "__main__": check()
