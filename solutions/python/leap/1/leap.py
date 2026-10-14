
"""Determine whether a year is a leap year."""


def leap_year(year):
    """Return True if the given year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
