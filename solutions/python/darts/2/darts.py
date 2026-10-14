
"""Calculate the score of a dart thrown at a target."""


def score(coordinate_x, coordinate_y):
    """Return the score based on the dart's distance from the center."""
    distance_squared = coordinate_x ** 2 + coordinate_y ** 2

    if distance_squared <= 1:
        return 10

    if distance_squared <= 25:
        return 5

    if distance_squared <= 100:
        return 1

    return 0
