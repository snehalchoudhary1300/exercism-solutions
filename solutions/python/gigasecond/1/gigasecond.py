
"""Calculate the date and time one gigasecond after a given moment."""

from datetime import timedelta


def add(moment):
    """Return the moment one gigasecond later."""
    return moment + timedelta(seconds=1_000_000_000)
