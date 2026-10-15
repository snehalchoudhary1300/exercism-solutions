
"""Calculate the largest product of a series of adjacent digits."""


def largest_product(series, size):
    """Return the largest product of adjacent digits of the given size."""
    if size < 0:
        raise ValueError("span must not be negative")

    if not series.isdigit() and series != "":
        raise ValueError("digits input must only contain digits")

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if size == 0:
        return 1

    largest = 0

    for start in range(len(series) - size + 1):
        product = 1

        for digit in series[start:start + size]:
            product *= int(digit)

        largest = max(largest, product)

    return largest
