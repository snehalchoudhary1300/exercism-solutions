
"""Calculate resistor values and tolerance."""


def resistor_label(colors):
    """Return the resistance label with tolerance."""
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

    tolerances = {
        "grey": "0.05",
        "violet": "0.1",
        "blue": "0.25",
        "green": "0.5",
        "brown": "1",
        "red": "2",
        "gold": "5",
        "silver": "10",
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        first = color_codes[colors[0]]
        second = color_codes[colors[1]]
        multiplier = color_codes[colors[2]]
        tolerance = tolerances[colors[3]]
        value = (first * 10 + second) * (10 ** multiplier)
    else:
        first = color_codes[colors[0]]
        second = color_codes[colors[1]]
        third = color_codes[colors[2]]
        multiplier = color_codes[colors[3]]
        tolerance = tolerances[colors[4]]
        value = (first * 100 + second * 10 + third) * (10 ** multiplier)

    if value >= 1_000_000:
        value = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value = value / 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    if value == int(value):
        value = int(value)

    return f"{value} {unit} ±{tolerance}%"
