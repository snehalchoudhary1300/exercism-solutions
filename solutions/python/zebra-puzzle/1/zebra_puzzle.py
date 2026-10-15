
"""Solve the Zebra Puzzle."""

from itertools import permutations


def drinks_water():
    """Return the nationality of the person who drinks water."""
    return solve_puzzle()["water"]


def owns_zebra():
    """Return the nationality of the person who owns the zebra."""
    return solve_puzzle()["zebra"]


def solve_puzzle():
    """Find the solution satisfying all the puzzle clues."""
    houses = (1, 2, 3, 4, 5)

    for colors in permutations(houses):
        red, green, ivory, yellow, blue = colors

        if green != ivory + 1:
            continue

        for nationalities in permutations(houses):
            englishman, spaniard, ukrainian, norwegian, japanese = nationalities

            if englishman != red or norwegian != 1:
                continue

            if abs(norwegian - blue) != 1:
                continue

            for beverages in permutations(houses):
                coffee, tea, milk, orange_juice, water = beverages

                if coffee != green or tea != ukrainian or milk != 3:
                    continue

                for hobbies in permutations(houses):
                    dancing, painter, reading, football, chess = hobbies

                    if painter != yellow or football != orange_juice:
                        continue

                    if chess != japanese:
                        continue

                    for pets in permutations(houses):
                        dog, snail, fox, horse, zebra = pets

                        if dog != spaniard or snail != dancing:
                            continue

                        if abs(reading - fox) != 1:
                            continue

                        if abs(painter - horse) != 1:
                            continue

                        return {
                            "water": next(
                                nationality
                                for nationality in (
                                    "Englishman",
                                    "Spaniard",
                                    "Ukrainian",
                                    "Norwegian",
                                    "Japanese",
                                )
                                if nationalities[
                                    (
                                        "Englishman",
                                        "Spaniard",
                                        "Ukrainian",
                                        "Norwegian",
                                        "Japanese",
                                    ).index(nationality)
                                ] == water
                            ),
                            "zebra": next(
                                nationality
                                for nationality in (
                                    "Englishman",
                                    "Spaniard",
                                    "Ukrainian",
                                    "Norwegian",
                                    "Japanese",
                                )
                                if nationalities[
                                    (
                                        "Englishman",
                                        "Spaniard",
                                        "Ukrainian",
                                        "Norwegian",
                                        "Japanese",
                                    ).index(nationality)
                                ] == zebra
                            ),
                        }


def main():
    """Print the answers to the puzzle."""
    print("Water:", drinks_water())
    print("Zebra:", owns_zebra())


if __name__ == "__main__":
    main()
