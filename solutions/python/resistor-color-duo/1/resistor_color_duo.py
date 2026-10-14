
"""Convert resistor colors into a two-digit value."""


def value(colors):
    """Return the value of the first two resistor colors."""
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    return color_codes[colors[0]] * 10 + color_codes[colors[1]]
