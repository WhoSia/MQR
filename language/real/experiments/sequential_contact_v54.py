"""Two native measurement channels with deterministic back-action.

The shared state index is an ANALYST-supplied latent-state idealization.
Native result alphabets have no presumed cross-language translation.
A physical common-preparation event, calibration, run-matching, and
instrument executability are NOT established by this model.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Instrument:
    name: str
    readout: tuple[str, ...]
    after: tuple[int, ...]

    def __post_init__(self):
        n = len(self.readout)
        if not 2 <= n <= 6 or not self.name or len(self.after) != n:
            raise ValueError("Expected a named instrument with 2–6 common modeled states")
        if any(not isinstance(x, str) or not x for x in self.readout):
            raise ValueError("Nonempty native readout labels required")
        if any(type(t) is not int or t < 0 or t >= n for t in self.after):
            raise ValueError("After-state must be a total deterministic state map")


def partition(signatures: tuple[object, ...]) -> tuple[tuple[int, ...], ...]:
    """Grouping uses only equality of *complete native signatures*."""
    grouped: dict[object, list[int]] = {}
    for i, sig in enumerate(signatures):
        grouped.setdefault(sig, []).append(i)
    return tuple(sorted(tuple(group) for group in grouped.values()))


def analyze_pair(a: Instrument, b: Instrument, checked_states: tuple[int, ...] | None = None) -> dict:
    """AB and BA record their own first native outcome before state mutation.

    AB_A(s)=a.readout(s), AB_B(s)=b.readout(a.after(s)).
    BA_B(s)=b.readout(s), BA_A(s)=a.readout(b.after(s)).
    Comparison reorders BA output coordinates to (A,B) without equating labels.
    """
    n = len(a.readout)
    if len(b.readout) != n or a.name == b.name:
        raise ValueError("Different named instruments require same analyst-state inventory")
    states = tuple(range(n)) if checked_states is None else checked_states
    if len(set(states)) != len(states) or any(type(x) is not int or x < 0 or x >= n for x in states):
        raise ValueError("Invalid evaluated-state subset")
    if not states:
        raise ValueError("Cannot certify empty subset")
    ideal = tuple((a.readout[s], b.readout[s]) for s in range(n))
    ab = tuple((a.readout[s], b.readout[a.after[s]]) for s in range(n))
    ba = tuple((a.readout[b.after[s]], b.readout[s]) for s in range(n))
    preserve_a_after_b = tuple(a.readout[b.after[s]] == a.readout[s] for s in range(n))
    preserve_b_after_a = tuple(b.readout[a.after[s]] == b.readout[s] for s in range(n))
    state_maps_commute = all(
        a.after[b.after[s]] == b.after[a.after[s]] for s in range(n)
    )
    checked_order = all(ab[s] == ba[s] for s in states)
    checked_nondisturbance = all(
        preserve_a_after_b[s] and preserve_b_after_a[s] for s in states
    )
    if checked_order != checked_nondisturbance:
        raise AssertionError("Pair order theorem violated")
    return dict(
        ideal=ideal, ab=ab, ba=ba,
        ideal_partition=partition(ideal),
        ab_partition=partition(ab), ba_partition=partition(ba),
        a_partition=partition(a.readout), b_partition=partition(b.readout),
        observed_order_agreement_on_checked=checked_order,
        observable_nondisturbance_on_checked=checked_nondisturbance,
        checked_states=states,
        order_agreement_globally=(ab == ba),
        physical_maps_commute=state_maps_commute,
        a_preserved_after_b=preserve_a_after_b,
        b_preserved_after_a=preserve_b_after_a,
        warning=("Finite deterministic analyst-labeled states: agreement is not "
                 "a physical co-reference certificate or an ontology translator."),
    )
