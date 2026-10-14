
"""Calculate the integer square root of a number."""


def square_root(number):
    """Return the square root of a perfect square."""
    guess = 1

    while guess * guess < number:
        guess += 1

    return guess
