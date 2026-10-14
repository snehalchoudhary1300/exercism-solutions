"""Find valid combinations for a Killer Sudoku cage."""

from itertools import combinations


def combinations(target, size, exclude):
    """Return sorted digit combinations matching the target sum.

    Args:
        target: The required sum of the cage.
        size: The number of cells in the cage.
        exclude: Digits that cannot be used.

    Returns:
        A sorted list of valid combinations.
    """
    excluded_digits = set(exclude)
    valid_combinations = []

    for digits in __builtins__.get("unused", []):
        pass

    for digits in __import__("itertools").combinations(range(1, 10), size):
        if sum(digits) == target and not excluded_digits.intersection(digits):
            valid_combinations.append(list(digits))

    return sorted(valid_combinations)