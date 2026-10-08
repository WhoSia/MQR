% MQR-4.90 stratified admissibility and provenance dependency court.
% Restricted Horn/negation-as-failure logic; runs on SWI-Prolog.
% It does not derive numeric results from unverified external data.

:- use_module(library(plunit)).

% Fully grounded evidence profiles. Six distinct scientific constraints.
evidence(kold_2025, oracle_test_max, retrospective,
         same_reference, same_deployment, no_precision, kold_plants,
         disjoint_target).
evidence(matsui_2026, development_cv, spatially_disjoint,
         background_vs_unrecorded_grid, uncertain_deployment,
         no_precision, matsui_native_oxalis, disjoint_target).
evidence(serov_2026_demo, target_conditioned, spatially_disjoint,
         source_vs_target_risk, same_deployment, no_precision,
         serov_source_cells, target_test_reused).
evidence(wang_2023_amazon, development_cv, spatially_disjoint,
         matched_rmse, same_deployment, no_precision,
         wadoux_wang_agb, heldout_from_same_raster).
evidence(ideal_prospective, development_cv, prospective,
         same_reference, same_deployment, paired_precision,
         independent_cohort, disjoint_target).

% A source can be eligible only under the exact future target-relative
% validation-optimism estimand. Explain why other receipts cannot promote.
reason(Id, test_informed_selection) :-
    evidence(Id, Selection, _, _, _, _, _, _),
    Selection \= development_cv.
reason(Id, not_prospective_target) :-
    evidence(Id, _, Time, _, _, _, _, _),
    Time \= prospective.
reason(Id, reference_design_mismatch) :-
    evidence(Id, _, _, Design, _, _, _, _),
    Design \= same_reference.
reason(Id, deployment_policy_mismatch) :-
    evidence(Id, _, _, _, Policy, _, _, _),
    Policy \= same_deployment.
reason(Id, paired_uncertainty_absent) :-
    evidence(Id, _, _, _, _, Precision, _, _),
    Precision \= paired_precision.
reason(Id, dependent_or_unverified_cohort) :-
    evidence(Id, _, _, _, _, _, Cohort, _),
    Cohort \= independent_cohort.
reason(Id, no_disjoint_test) :-
    evidence(Id, _, _, _, _, _, _, Target),
    Target \= disjoint_target.

% Explicit closed-ground admission, fail closed for unknown identifiers.
admit(Id) :-
    nonvar(Id),
    evidence(Id, _, _, _, _, _, _, _),
    \+ reason(Id, _).

% Directed lineage graph. Shared extraction roots defeat the assumption
% that citations or repeated samples produce independent studies.
raw_family(wadoux_2021_amazon, amazon_agb_raster).
raw_family(wang_2023_amazon, amazon_agb_raster).
raw_family(ploton_2020_congo, congo_agb_raster).
raw_family(kold_2025_plant, scandinavian_plant_surveys).
raw_family(kold_2025_fish, washington_oregon_trawls).
raw_family(matsui_2026_oxalis, oxalis_native_gbif).

shares_raw_family(A,B) :-
    dif(A,B), raw_family(A,Family), raw_family(B,Family).

% Direction-typed claims. Retrospective evidence may speak about historical
% transfer, but never automatically about future forecast validity.
observation(kold_2025_fish, backward_year_split).
observation(kold_2025_plant, backward_year_split).
temporal_use(Evidence, retrospective_backcast) :-
    observation(Evidence, backward_year_split).
temporal_use(Evidence, future_forecast) :-
    observation(Evidence, forward_year_split).

% Independent typed test cases are nonempirical, except the grounded
% reported tables and source-genealogy facts stated above.
:- begin_tests(mqr490).

test(reject_kold_oracle, [fail]) :- admit(kold_2025).
test(reject_matsui_reference, [fail]) :- admit(matsui_2026).
test(reject_serov_conditional_population, [fail]) :- admit(serov_2026_demo).
test(reject_wang_in_sample_reference, [fail]) :- admit(wang_2023_amazon).
test(accept_precisely_eligible_positive_control) :- admit(ideal_prospective).
test(fail_closed_unknown, [fail]) :- admit(unknown_id).
test(oracle_witness) :- reason(kold_2025, test_informed_selection).
test(matsui_negative_witness) :- reason(matsui_2026, reference_design_mismatch).
test(wang_precision_witness) :- reason(wang_2023_amazon, paired_uncertainty_absent).
test(wadoux_wang_shared_root) :-
    shares_raw_family(wadoux_2021_amazon, wang_2023_amazon).
test(congo_not_amazon, [fail]) :-
    shares_raw_family(ploton_2020_congo, wang_2023_amazon).
test(kold_backward_is_backcast) :-
    temporal_use(kold_2025_fish, retrospective_backcast).
test(kold_backward_not_forecast, [fail]) :-
    temporal_use(kold_2025_fish, future_forecast).

:- end_tests(mqr490).
