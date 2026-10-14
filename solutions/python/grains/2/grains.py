
"""Calculate the number of grains on a chessboard."""


def square(number):
    """Return the number of grains on a given square."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on all 64 squares."""
    return 2 ** 64 - 1
