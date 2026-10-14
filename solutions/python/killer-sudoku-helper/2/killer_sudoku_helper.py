"""Find valid combinations for a Killer Sudoku cage."""

from itertools import combinations as get_combinations


def combinations(target, size, exclude):
    """Return sorted valid digit combinations."""
    excluded_digits = set(exclude)
    result = []

    for digits in get_combinations(range(1, 10), size):
        if sum(digits) == target and not excluded_digits.intersection(digits):
            result.append(list(digits))

    return result