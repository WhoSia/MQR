"""Exact finite example of a three-action constraint hidden by pairwise views."""

from itertools import combinations, permutations

ALPHABET = "abc"


def traces(max_length):
    return {
        "".join(word)
        for length in range(max_length + 1)
        for word in permutations(ALPHABET, length)
    }


def project(language, component):
    return {"".join(action for action in word if action in component) for word in language}


def main():
    pairwise = tuple(combinations(ALPHABET, 2))
    restricted = traces(2)
    permissive = traces(3)
    local_languages = tuple(project(restricted, component) for component in pairwise)
    assert local_languages == tuple(project(permissive, component) for component in pairwise)

    # The pair projections forbid repetition, so every accepted word has length <= 3.
    reconstructed = {
        word
        for word in permissive
        if all(
            "".join(action for action in word if action in component) in local
            for component, local in zip(pairwise, local_languages)
        )
    }
    assert reconstructed == permissive
    assert reconstructed - restricted == {"abc", "acb", "bac", "bca", "cab", "cba"}
    assert "abc" not in restricted and "abc" in permissive
    print(f"Restricted={len(restricted)}, pairwise product={len(reconstructed)}")
    print("Spurious traces:", ", ".join(sorted(reconstructed - restricted)))


if __name__ == "__main__":
    main()
