#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

static vector<string> split(const string& s, char d) {
    vector<string> out; string x; stringstream ss(s);
    while (getline(ss, x, d)) out.push_back(x);
    return out;
}

int main() {
    ifstream f("experiments/mqr-4.73/COURT-FREEZE.tsv");
    string line; getline(f, line);
    auto headers = split(line, '\t');
    int cases = 0, bad = 0;
    bool hidden=false, strict=false, trace=false, mathloss=false, kernel=false;
    while (getline(f, line)) {
        auto vals = split(line, '\t');
        unordered_map<string,string> r;
        for (size_t i=0;i<headers.size();++i) r[headers[i]]=vals[i];
        bool recover = r["old_distinction_recoverable"]=="YES";
        bool adds = r["new_distinction"]=="YES";
        bool indep = r["independent_support"]=="YES";
        string bridge = r["bridge"], got = "HOLD";
        if (bridge=="TRACEABLE_ONLY" && !indep) got="HOLD_TRACEABILITY_NOT_ENOUGH";
        else if (bridge=="LABEL_ONLY" && !indep) got="HOLD_BRIDGE_UNEARNED";
        else if (bridge=="NONCONSERVATIVE_UNKNOWN" && !indep) got="HOLD_STRENGTH_UNEARNED";
        else if (bridge=="MERGE_LOSSY" && !recover) got="HOLD_MERGE_LOSS";
        else if (!recover && adds) got=(r["domain"]=="NATSCI" ? "INCOMPARABLE_HIDDEN_LOSS" : "INCOMPARABLE_SEMANTIC_LOSS");
        else if (!recover) got="INCOMPARABLE";
        else if ((bridge=="REFINEMENT_UNION" || bridge=="OBLIGATION_REFINEMENT") && adds && indep)
            got=(r["domain"]=="NATSCI" ? "REFINEMENT_DOMINANCE_LOCAL" : "REFINEMENT_DOMINANCE_RELATIVE");
        else if (adds && indep)
            got=(r["domain"]=="NATSCI" ? "STRICT_DOMINANCE_LOCAL" : "STRICT_DOMINANCE_RELATIVE");
        else if (recover && !adds && indep)
            got=(r["domain"]=="NATSCI" ? "EQUIVALENT_LOCAL" : "EQUIVALENT_RELATIVE");

        ++cases;
        if (got != r["expected"]) { ++bad; cerr << r["case_id"] << " " << got << " != " << r["expected"] << "\n"; }
        if (r["case_id"]=="N3") hidden = got=="INCOMPARABLE_HIDDEN_LOSS";
        if (r["case_id"]=="N4") strict = got=="STRICT_DOMINANCE_LOCAL";
        if (r["case_id"]=="N8") trace = got=="HOLD_TRACEABILITY_NOT_ENOUGH";
        if (r["case_id"]=="M2") mathloss = got=="INCOMPARABLE_SEMANTIC_LOSS";
        if (r["case_id"]=="M1") kernel = got=="EQUIVALENT_RELATIVE";
    }
    bool ok = bad==0 && hidden && strict && trace && mathloss && kernel;
    cout << "MQR473_CPP_CAPABILITY_COURT=" << (ok?"PASS":"FAIL") << "\n";
    cout << "MQR473_CPP_CASES=" << cases << "\n";
    cout << "MQR473_CPP_HIDDEN_LOSS_BLOCKS_DOMINANCE=" << (hidden?"YES":"NO") << "\n";
    cout << "MQR473_CPP_TRACEABILITY_ALONE_NOT_ENOUGH=" << (trace?"YES":"NO") << "\n";
    cout << "MQR473_CPP_MATH_SEMANTIC_LOSS_BLOCKS_DOMINANCE=" << (mathloss?"YES":"NO") << "\n";
    return ok ? 0 : 1;
}
