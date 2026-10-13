
"""Convert numbers into raindrop sounds."""


def convert(number):
    """Return the raindrop sound corresponding to a number."""
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if result == "":
        return str(number)

    return result
