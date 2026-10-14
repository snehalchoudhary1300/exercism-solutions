
"""Find anagrams of a target word."""

def find_anagrams(word, candidates):
    """Return candidates that are anagrams of the target word."""
    anagrams = []
    target = word.lower()

    for candidate in candidates:
        if candidate.lower() != target:
            if sorted(candidate.lower()) == sorted(target):
                anagrams.append(candidate)

    return anagrams
