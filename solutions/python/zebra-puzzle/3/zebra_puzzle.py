
"""Solve the Zebra Puzzle."""

from itertools import permutations


HOUSES = (1, 2, 3, 4, 5)
NATIONALITIES = (
    "Englishman",
    "Spaniard",
    "Ukrainian",
    "Norwegian",
    "Japanese",
)


def drinks_water():
    """Return the nationality of the person who drinks water."""
    return solve_puzzle()["water"]


def owns_zebra():
    """Return the nationality of the person who owns the zebra."""
    return solve_puzzle()["zebra"]


def solve_puzzle():
    """Find the arrangement satisfying all puzzle clues."""
    for colors in permutations(HOUSES):
        red, green, ivory, yellow, blue = colors

        if green != ivory + 1:
            continue

        for nationalities in permutations(HOUSES):
            englishman, spaniard, ukrainian, norwegian, japanese = nationalities

            if englishman != red or norwegian != 1:
                continue

            if abs(norwegian - blue) != 1:
                continue

            result = _find_solution(colors, nationalities)
            if result is not None:
                return result

    return None


def _find_solution(colors, nationalities):
    """Check beverage, hobby, and pet arrangements."""
    _, green, _, yellow, _ = colors
    _, spaniard, ukrainian, _, japanese = nationalities

    for beverages in permutations(HOUSES):
        coffee, tea, milk, orange_juice, water = beverages

        if coffee != green or tea != ukrainian or milk != 3:
            continue

        for hobbies in permutations(HOUSES):
            dancing, painter, reading, football, chess = hobbies

            if painter != yellow or football != orange_juice:
                continue

            if chess != japanese:
                continue

            result = _check_pets(nationalities, hobbies, water, spaniard)
            if result is not None:
                return result

    return None


def _check_pets(nationalities, hobbies, water, spaniard):
    """Check pet positions and return the answers if valid."""
    dancing, painter, reading, _, _ = hobbies

    for pets in permutations(HOUSES):
        dog, snail, fox, horse, zebra = pets

        if dog != spaniard or snail != dancing:
            continue

        if abs(reading - fox) != 1:
            continue

        if abs(painter - horse) != 1:
            continue

        return {
            "water": _nationality_at(nationalities, water),
            "zebra": _nationality_at(nationalities, zebra),
        }

    return None


def _nationality_at(nationalities, position):
    """Return the nationality associated with a house position."""
    return NATIONALITIES[nationalities.index(position)]
