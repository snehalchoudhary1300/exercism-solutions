
"""Represent a clock without a date."""


class Clock:
    """Represent a 24-hour clock."""

    def __init__(self, hour, minute):
        """Initialize the clock."""
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __str__(self):
        """Return the clock time as HH:MM."""
        return f"{self.hour:02d}:{self.minute:02d}"

    def __repr__(self):
        """Return a representation that recreates the clock."""
        return f"Clock({self.hour}, {self.minute})"

    def __eq__(self, other):
        """Check whether two clocks represent the same time."""
        if not isinstance(other, Clock):
            return NotImplemented

        return (
            self.hour == other.hour
            and self.minute == other.minute
        )

    def __add__(self, minutes):
        """Return a new clock after adding minutes."""
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        """Return a new clock after subtracting minutes."""
        return Clock(self.hour, self.minute - minutes)
