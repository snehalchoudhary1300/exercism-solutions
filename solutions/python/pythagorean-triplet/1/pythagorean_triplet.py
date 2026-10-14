
"""Find Pythagorean triplets."""


def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals number."""
    triplets = []

    for a in range(1, number // 3):
        numerator = number * (number - 2 * a)
        denominator = 2 * (number - a)

        if numerator % denominator != 0:
            continue

        b = numerator // denominator
        c = number - a - b

        if a < b < c and a * a + b * b == c * c:
            triplets.append([a, b, c])

    return triplets
