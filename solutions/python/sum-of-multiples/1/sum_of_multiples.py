
"""Calculate the sum of unique multiples."""


def sum_of_multiples(limit, multiples):
    """Return the sum of unique multiples below the limit."""
    numbers = set()

    for multiple in multiples:
        if multiple == 0:
            continue

        for number in range(multiple, limit, multiple):
            numbers.add(number)

    return sum(numbers)
