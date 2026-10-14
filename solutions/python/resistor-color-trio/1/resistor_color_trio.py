
"""Calculate resistor resistance from three color bands."""


def label(colors):
    """Return the resistance value with the appropriate unit."""
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

    first_digit = color_codes[colors[0]]
    second_digit = color_codes[colors[1]]
    zeros = color_codes[colors[2]]

    value = (first_digit * 10 + second_digit) * (10 ** zeros)

    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    if value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    if value >= 1_000:
        return f"{value // 1_000} kiloohms"

    return f"{value} ohms"
