# MQR-5.3 R46-AC — An unpublished 1780 precursor and path-dependent pyrometric evidence

Date: 2026-11-05 KST. Status: archival source discovery and analytical reconstruction; NOVELTY HOLD.

## 1. Corrected archival genealogy
The three *published* Wedgwood pyrometer papers of 1782, 1784 and 1786 are not an exhaustive documentary chronology. The Royal Society identifies Wedgwood's earlier unpublished manuscript **“A method of ascertaining very great degrees of heat”**, read **14 December 1780**, **L&P/7/178**, 7-page manuscript:
https://makingscience.royalsociety.org/items/l-and-p_7_178/paper-a-method-of-ascertaining-very-great-degrees-of-heat-by-josiah-wedgwood

1782 published experimental instrument proposal: DOI https://doi.org/10.1098/rstl.1782.0021 (full image scan held, transcription incomplete).
1784 independent scale-connection paper: DOI https://doi.org/10.1098/rstl.1784.0028 ; Royal Society L&P/8/79, contains three plates (Drive original missing).
1786 additional instrument investigations: DOI https://doi.org/10.1098/rstl.1786.0022 ; Royal Society L&P/9/1 (Drive original missing).

The *existence/date/title* of the 1780 manuscript are verified from institutional metadata; its substantive propositions and numerical experiments were **not** transcribed. The 1780 item is a new **primary-source collation target**, not a claim that the idea was independently invented for the first time in that year.

## 2. Why instantaneous temperature and thermal history are separate

Consider a class of analytical models with a readout after thermal exposure:
  r(t_f) = F_b(T(t_f), z(t_f)) + epsilon,
  dz/dt = k_b(T(t))(1-z), z(0)=0.
Then z(t_f)=1-exp(-integral_0^{t_f} k_b(T(t))dt). Here b labels production batch and preparation. k_b is a hypothetical temperature-dependent rate (1/time) and z a dimensionless material-state variable; F_b maps endpoint T and internal state to instrument contraction. **This is a constructed model, not an empirically validated historical clay law.**

Two histories h1 and h2 can have identical endpoint T(t_f)=T* but different integrated rate K_h = integral k_b(T(t))dt and hence different r. Conversely under fixed heating protocols r may be stable across repeated trials even though r is not a single-valued function of instantaneous T. Thus repeatability of a controlled *process* does not identify a context-free temperature scale.

The model has a stringent discriminating experiment: compare (i) equal endpoint temperatures reached with differing durations and (ii) equal integrated exposure histories ending at differing temperatures, with endpoint temperature independently assessed. If the readings track K more than T, a simple instantaneous temperature calibration loses validity in that domain. An independent reference is essential: using the same clay response to define 'equal temperature' would be circular.

Important: without a separate thermometer and experimentally varied histories, observing r alone does not identify temperature, rate, batch, and history terms jointly. The formal claim is a conditional identifiability warning, not an original universal impossibility theorem.

## 3. Historical discrimination against Chang (2004), rather than easy novelty
Chang, _Inventing Temperature_ (2004), chapter 3, pp.103-158, already addresses extrapolation and the Wedgwood case, including the necessity of transporting a concept beyond its original measurement domain: https://doi.org/10.1093/0195171276.003.0003.
The Science Museum describes surviving 1786 equipment and test pieces: https://collection.sciencemuseumgroup.org.uk/objects/co1684/wedgwood-pyrometer-1786
What is NOT yet shown is that Chang neglected history dependence or that the 1780 manuscript makes a substantially different philosophical judgment. Do not infer this from the constructed model.

## 4. Next evidence gates
A. Collate the seven original manuscript pages of L&P/7/178, identify any explicitly stated relationship between duration, material preparation, heating profile, and scale.
B. Compare exact passages and plates of the 1784 31-page archival entry (manuscript and plates combined) and 1786 20-page manuscript before ascribing intentions to Wedgwood.
C. Separate three propositions: 'repeatable firing protocol', 'invariant under different heating histories', and 'independent calibration to temperature'. Record contemporaneous feasible experiments and available measurement standards.
D. Explicitly adjudicate whether Chang (2004), Tal (2019), and Ohnesorge (2022) already account for the case. A difference in vocabulary is not philosophical novelty.
E. Keep missing registry separately current, including 1780 manuscript as unheld (although digitized online); do not treat archive catalog access as original-byte acquisition.

Outcome: revised archival genealogy **1780 → 1782 → 1784 → 1786**, mechanistic alternative with falsifiable requirements, and no unearned claim of historical source transcription or new theory.
