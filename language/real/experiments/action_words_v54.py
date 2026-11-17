"""Compile declared action words into boundary-only Real-Lang experiments."""

from collections.abc import Mapping

from protocol_frontier_v54 import Machine


def compile_words(machine: Machine, words: Mapping[str, tuple[str, ...]]) -> Machine:
    """Expose only each word's initial and final state, using native transitions."""
    compiled = {}
    for alias, word in words.items():
        if not word:
            raise ValueError(f"empty native action word for {alias!r}")
        states = tuple(range(len(machine.observations)))
        for action in word:
            if action not in machine.transitions:
                raise ValueError(f"unknown native action {action!r} for {alias!r}")
            transition = machine.transitions[action]
            states = tuple(transition[state] for state in states)
        compiled[alias] = states
    return Machine(machine.observations, compiled, machine.initial)
