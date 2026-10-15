
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
        if colors[1] != colors[2] + 1:
            continue

        for nationalities in permutations(HOUSES):
            if nationalities[0] != colors[0]:
                continue

            if nationalities[3] != 1:
                continue

            if abs(nationalities[3] - colors[4]) != 1:
                continue

            result = _find_solution(colors, nationalities)

            if result is not None:
                return result

    return None


def _find_solution(colors, nationalities):
    """Find matching beverages, hobbies, and pets."""
    green_house = colors[1]
    yellow_house = colors[3]
    ukrainian_house = nationalities[2]
    spaniard_house = nationalities[1]
    japanese_house = nationalities[4]

    for beverages in permutations(HOUSES):
        coffee, tea, milk, orange_juice, water = beverages

        if coffee != green_house:
            continue

        if tea != ukrainian_house or milk != 3:
            continue

        for hobbies in permutations(HOUSES):
            painter = hobbies[1]
            football = hobbies[3]
            chess = hobbies[4]

            if painter != yellow_house:
                continue

            if football != orange_juice or chess != japanese_house:
                continue

            result = _check_pets(
                nationalities,
                hobbies,
                water,
                spaniard_house,
            )

            if result is not None:
                return result

    return None


def _check_pets(nationalities, hobbies, water, spaniard_house):
    """Check pet positions and return the answers."""
    dancing = hobbies[0]
    painter = hobbies[1]
    reading = hobbies[2]

    for pets in permutations(HOUSES):
        dog, snail, fox, horse, zebra = pets

        if dog != spaniard_house or snail != dancing:
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
    """Return the nationality living at a given house position."""
    nationality_index = nationalities.index(position)
    return NATIONALITIES[nationality_index]
