
"""Find Pythagorean triplets."""


def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals number."""
    triplets = []

    for first_side in range(1, number // 3):
        numerator = number * (number - 2 * first_side)
        denominator = 2 * (number - first_side)

        if numerator % denominator != 0:
            continue

        second_side = numerator // denominator
        third_side = number - first_side - second_side

        if (
            first_side < second_side < third_side
            and first_side ** 2 + second_side ** 2 == third_side ** 2
        ):
            triplets.append([first_side, second_side, third_side])

    return triplets
