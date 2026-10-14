
"""Validate ISBN-10 numbers."""


def is_valid(isbn):
    """Return True if the ISBN-10 number is valid."""
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    total = 0

    for position in range(10):
        if isbn[position] == "X":
            digit = 10
        else:
            digit = int(isbn[position])

        total += digit * (10 - position)

    return total % 11 == 0
