# MQR 5.4 · MQR 44 · Record 18 — A new capability can invalidate an old translation without changing passive evidence

**Date:** 2026-11-22 KST. Research version **MQR 5.4 OPEN**. Claim level: logically exact proposition (known quotient-action theory), 1821 primary case comparison (NOT proof of the proposition's actual historical instantiation), and falsifiable research program. Source provenance preserved in R13–R17.

## 1. One mathematically sharp synthesis, not another generic taxonomy
Let two scientific interfaces be connected by a fixed surjective but non-injective output map f:A->B. An experiment repertoire at time t is a set I_t of operations T:A->A. The map f is **operationally adequate** for repertoire I_t when for each T in I_t there exists a B-level operation G_T satisfying
  f∘T = G_T∘f.

**Proposition (immediate from definition):** operational bridge adequacy is *antitone in the available intervention repertoire*. When I_t ⊆ I_u, a fixed f that is adequate for the larger repertoire I_u must be adequate for I_t; the converse is false. In particular, a new physically executable action can *invalidate an earlier sufficient bridge* even though f, source state space and passive measurement distribution are unchanged.

Constructive witness (R17 code): A={0,1,2}, B={L,R}; f(0)=f(1)=L, f(2)=R.
- At t0 only identity and swap(0,1) are admissible; both induce well-defined operations on B. Bridge status: ADEQUATE at declared repertoire.
- At t1 an additional action T=swap(1,2) becomes admissible. For two A states 0 and 1 that both read L, the outputs after T are L and R respectively; no single B-level G can reproduce that operation. Bridge status: INADEQUATE for extended repertoire.
- No passive observation or category names changed. It is the *newly possible question* (what happens under T?) that exposed previously hidden structural differences.

The proposition is not a novel theorem; it is an accessible corollary of quotient congruence. The MQR research challenge is to find a historically dated real experiment satisfying or contradicting the analogue with *materially available operations*.

## 2. The inverse possibility
If an instrument or shared method instead refines B's output distinctions and the new categories separate old fibers, a previously impossible operation bridge may become representable. E.g. replace B={L,R} by B'={L0,L1,R} and refine f' to a bijection, then every T lifts as G=f'∘T∘(f')^-1. This is a mathematical construction, not a claim that all translations can be made invertible or that actual sciences can build such instruments.

Thus science-bridge adequacy is jointly determined by the declared tasks, instrument repertoire and resolution, not just a once-for-all semantic dictionary. An intellectual revolution might render old translations insufficient by expanding what scientists can ask, even when older observations still agree perfectly.

## 3. Independently documented history: carefully bounded analogy
- **Faraday0148** (12 Sep 1821): he reinterprets apparent attractions/repulsions in rotary terms while rejecting certainty that unseen electrical currents exist within ordinary magnets.
- **Faraday0153** (18 Oct): compact apparatus and stated inability to follow German scientific material; no proof this language barrier caused a particular discovery.
- **Faraday0158** (16 Nov): apparatus + operational letter sent to **De La Rive**.
- **Faraday0160** (Hachette → Faraday, 12 Dec): reports that Faraday's effect was introduced to the Paris Academy **19 Nov** and repeated before Société Philomatique **24 Nov**, with an apparatus sent to **Hachette** and related explanations; the two recipient routes are distinct.
- **Faraday0165** (editorial date 2 Feb 1822, but transcribed date line 1821): Faraday repeats Ampère's experiment yet disputes its capacity to establish microscopic-current location and continues to withhold broad theoretical assent.

These witnesses establish *practical replication together with inferential disagreement*; they do NOT establish that the physically available rotation operations literally instantiate our three-state quotient transformation. Source-specific formal encoding remains a prospective task.

## 4. Falsification and measurement protocol
A defensible historical test must identify:
1. A genuinely **earlier** bridge map (or documented common predictions/procedures) and the actual operation set available then.
2. An independently dated **new operation**, available at later time, with reproducible world contact.
3. Explicit empirical response or proof that distinguishes states previously identified by the bridge.
4. A rival explanation: instrument error, differing object preparation, previously known relevant distinctions, or deliberate coarse-grained task objective.
5. A documented response: did a party refine the bridge, abandon it, or retain it for narrower purposes?

If a putative example has no evidence of earlier operational adequacy, it is **NO TEST** rather than a bridge failure; if the new operation was available earlier, there is no demonstrated capability-induced transition.

## 5. Prior art and claimed contribution
The pure mathematical fact is standard algebra of quotients, congruences and Markov lumpability analogies; the idea of experimental skill altering conceptual translation has deep prior art in Gooding, Steinle, Nersessian and Galison. The prospective contribution is the **joint, claim-scope-aware explanation of how new instruments can change the validity domain of a historical scientific translation**, demonstrated under independent sources and dated practices. No priority claim until such a case is actually adjudicated against strong rivals.

## 6. Gates and outcomes
- Finite exact proof and exhaustive enumeration: PASS. See `mqr_dynamic_quotient_bridge_v54.py`; 27 source actions, 15 compatible, 12 incompatible.
- Nonbijective candidate mapping and conditional entropy: PASS. See `mqr_nonbijective_bridges_v54.py`.
- Locally executed independent unittest: six cases PASS in `test_mqr_bridges_v54.py`.
- Historically documented effect reproduction and mixed interpretation: PASS at dated contemporaneous letter-transcription level, meeting-minute independent audit HOLD.
- Formal premise that original Faraday/Ampère experiments instantiate any particular f,T: HOLD.
- Metaparadigm or novel physical law: HOLD. **MQR 5.4 remains OPEN**.
