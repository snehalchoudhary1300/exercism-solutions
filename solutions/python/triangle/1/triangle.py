
"""Determine the types of triangles."""


def equilateral(sides):
    """Return True if the triangle is equilateral."""
    return (
        all(side > 0 for side in sides)
        and len(set(sides)) == 1
        and sum(sides) >= 2 * max(sides)
    )


def isosceles(sides):
    """Return True if the triangle is isosceles."""
    return (
        all(side > 0 for side in sides)
        and sum(sides) >= 2 * max(sides)
        and len(set(sides)) <= 2
    )


def scalene(sides):
    """Return True if the triangle is scalene."""
    return (
        all(side > 0 for side in sides)
        and sum(sides) >= 2 * max(sides)
        and len(set(sides)) == 3
    )
