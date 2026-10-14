
"""Functions for resistor color codes."""

COLOR_LIST = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color):
    """Return the numerical code for a given color."""
    return COLOR_LIST.index(color)


def colors():
    """Return the list of resistor colors."""
    return COLOR_LIST
