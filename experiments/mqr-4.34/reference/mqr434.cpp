#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

struct Row {
  std::string id, lineage, generator, semantic, component, quotient, state, endpoint;
  std::string decoy, expected_relation, expected_authority;
  bool confirmatory{};
};

static std::vector<std::string> split(const std::string& s, char sep) {
  std::vector<std::string> out;
  std::stringstream ss(s);
  std::string x;
  while (std::getline(ss, x, sep)) out.push_back(x);
  return out;
}

static std::string classify(const Row& r) {
  if (r.component == "SHIFTED_COMPONENT" || r.semantic == "NO_ADMISSIBLE_MAP" ||
      r.quotient == "INCOMMENSURABLE" || r.endpoint == "ENDPOINT_CONTRACT_CHANGED")
    return "R3_CONSTITUTIVE_COMPONENT_SHIFT";

  if (r.generator == "OVERLAP_NONNESTED")
    return "R4_OVERLAP_NONNESTED";

  if (r.generator == "UNKNOWN" || r.semantic == "UNKNOWN" ||
      r.component == "UNRESOLVED_COMPONENT" ||
      r.quotient == "UNKNOWN_QUOTIENT_RELATION" ||
      r.state == "STATE_UNRESOLVED" ||
      r.endpoint == "ENDPOINT_CONTRACT_UNRESOLVED")
    return "R5_UNRESOLVED";

  if (r.generator == "BRIDGE_SUBSET_DIRECT" &&
      r.semantic == "FORGETFUL_SURJECTION" &&
      r.component == "REFINED_COMPONENT" &&
      r.quotient == "DIRECT_REFINES_BRIDGE" &&
      (r.endpoint == "COARSE_ENDPOINT_PRESERVED" ||
       r.endpoint == "ENDPOINT_CONTRACT_EXTENDED"))
    return "R2_SUCCESSOR_REFINEMENT";

  if (r.generator == "BRIDGE_SUBSET_DIRECT")
    return "R1_STRICT_DOMAIN_EXTENSION";

  if (r.generator == "SAME_GENERATOR" &&
      r.semantic == "IDENTITY_ON_SCOPE" &&
      (r.component == "SAME_COMPONENT" || r.component == "SAME_QUOTIENT") &&
      r.quotient == "SAME_QUOTIENT" &&
      (r.state == "RESET_EQUIVALENT" ||
       r.state == "STATE_IRRELEVANT_BY_CONSTRUCTION") &&
      r.endpoint == "SAME_ENDPOINT_CONTRACT")
    return "R0_SAME_GENERATOR_HOLDOUT";

  return "R5_UNRESOLVED";
}

static std::string authority(const std::string& r) {
  if (r == "R0_SAME_GENERATOR_HOLDOUT")
    return "A0_HOLDOUT_SUPPORT_ADMISSIBLE";
  if (r == "R1_STRICT_DOMAIN_EXTENSION")
    return "A1_EXTENSION_REQUIRES_FRESH_CONTACT";
  if (r == "R2_SUCCESSOR_REFINEMENT")
    return "A2_REFINEMENT_SUPPORT_IS_QUOTIENT_INDEXED";
  if (r == "R3_CONSTITUTIVE_COMPONENT_SHIFT")
    return "A3_CONSTITUTIVE_BREAK_NO_CANDIDATE";
  if (r == "R4_OVERLAP_NONNESTED")
    return "A4_OVERLAP_HOLD";
  return "A5_RELATION_UNRESOLVED_HOLD";
}

int main(int argc, char** argv) {
  const std::string path = argc > 1 ? argv[1] : "experiments/mqr-4.34/forcing-worlds.tsv";
  std::ifstream in(path);
  if (!in) return 2;

  std::string line;
  if (!std::getline(in, line)) return 2;
  const std::string expected_header =
      "id\tlineage\tgenerator_relation\tsemantic_map\tcomponent_relation\tquotient_relation\tstate_relation\tendpoint_contract\tdecoy\texpected_relation\texpected_authority\tconfirmatory";
  if (line != expected_header) return 2;

  std::size_t rows = 0, confirmatory = 0, mismatches = 0;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    auto p = split(line, '\t');
    if (p.size() != 12) return 2;

    Row r{p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11] == "1"};
    const auto rel = classify(r);
    const auto auth = authority(rel);
    const bool matched = rel == r.expected_relation && auth == r.expected_authority;

    ++rows;
    if (r.confirmatory) ++confirmatory;
    if (!matched) ++mismatches;

    std::cout << "RELATION=" << r.id
              << " lineage=" << r.lineage
              << " relation=" << rel
              << " authority=" << auth
              << " expected_match=" << (matched ? "true" : "false")
              << "\n";
  }

  std::cout << "ROWS=" << rows << "\n";
  std::cout << "CONFIRMATORY_ROWS=" << confirmatory << "\n";
  std::cout << "RELATION_EXPECTATION_MISMATCHES=" << mismatches << "\n";
}
