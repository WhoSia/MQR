#!/usr/bin/env bash
set -euo pipefail
f="$1"
V=./language/real/target/release/real-v14-challenge
P=language/real/prolog/challenge_v14.pl
CORE='^challenge\.(registered_probe_count|selected_probe_count|selected_world_probe_count|selected_ancestry_count|route_count|covered_route_count|uncovered_route_count|declared_route_coverage_complete|probe_route_multiplicity|common_ancestry|post_outcome_selection|incumbent_relevance|discriminator_capture|omitted_counterprobe|correspondence_before|correspondence_after|narrowed|expansion_count|expansion_instability|expansion_reopen_required|expansion_state|current_family_complete|future_challenge_space_closed|probe_count_truth_oracle|externality_truth_oracle|cost_truth_oracle|selection_rule_truth_oracle|selection_authority|guidance_mode)='
"$V" "$f" > /tmp/rust
swipl -q -s "$P" -g "run('$f'),halt" -t "halt(1)" > /tmp/prolog
grep -E "$CORE" /tmp/rust > /tmp/rust.core
grep -E "$CORE" /tmp/prolog > /tmp/prolog.core
diff -u /tmp/rust.core /tmp/prolog.core
