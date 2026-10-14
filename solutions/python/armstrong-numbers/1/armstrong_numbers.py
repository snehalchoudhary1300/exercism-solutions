
"""Check whether a number is an Armstrong number."""


def is_armstrong_number(number):
    """Return True if the number is an Armstrong number."""
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number
