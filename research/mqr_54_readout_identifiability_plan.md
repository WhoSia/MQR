# MQR 5.4 — Readout alignment and a held-out order test

2026-11-17 KST · design recorded before replay of the constructed fixtures and before extracting the published Malus table.

## Exact checks

A candidate predicts an input intensity for each recorded output. A detector is shared within the run and may have an arbitrary nondecreasing response, or the narrower strictly increasing response. Every reading and anchor constrains the noiseless response to a closed interval. Feasibility is tested separately under each proposed operation translation; this allows equally data-compatible nuisance responses to differ between hypotheses. Combine anchors and readings for equal predicted intensities before testing their order. No linear normalization is assumed.

1. With exact observations 1,1,0 and distinct blocked/full reference readings 0 and 1, only the dark-ending candidate (1,1,0) can fit; the constant candidate (1,1,1) must reuse the same detector value. If the recorded trace instead reads 1,1,1 and no anchors are available, a strictly increasing detector selects the constant candidate while a saturating detector can fit both. With distinct blocked/full references the saturating explanation on these intensities must fail.
2. A single interior readout of 1/2 can fit either a predicted intensity of 1/4 or 3/4 with an unknown strictly increasing detector anchored at 0 and 1. Add an independent interior reference whose true intensity and exact detector response both equal 1/2, and the prediction 1/4 requires a detector response strictly below 1/2, while 3/4 requires one strictly above it. Both candidates now fail. Use a second constructed recording below the interior response to test a single surviving candidate.
3. If two noisy readings of the same intensity have disjoint closed response intervals, the equal-intensity candidate must fail. Touching intervals count as consistent for repeated intensity. Strict order has a separate boundary: distinct latent intensities cannot have equal noiseless response.

## Published-source inspection

Inspect the empirical rows listed by the Malus teaching paper (DOI 10.3390/opt7040067, verify at publisher) before claiming a physical check. A fixed order and a single detector can stress-test endpoint normalization or an order constraint but cannot adjudicate swapped element order across instruments. Record whether readings are rounded table summaries, whether device linearity was separately established, and whether dark/reference and both component orders are archived. A scan of the literature alone provides no physical validation of the translation model.
