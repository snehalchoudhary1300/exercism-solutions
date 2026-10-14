
"""Calculate the score of a dart thrown at a target."""


def score(x, y):
    """Return the score based on the dart's distance from the center."""
    distance_squared = x ** 2 + y ** 2

    if distance_squared <= 1 ** 2:
        return 10
    elif distance_squared <= 5 ** 2:
        return 5
    elif distance_squared <= 10 ** 2:
        return 1
    else:
        return 0
