"""Implement rational number arithmetic."""

from math import gcd


class Rational:
    """Represent a rational number in reduced form."""

    def __init__(self, numer, denom):
        """Initialize a rational number."""
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        common = gcd(numer, denom)
        numer //= common
        denom //= common

        if denom < 0:
            numer = -numer
            denom = -denom

        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        """Check whether two rational numbers are equal."""
        if not isinstance(other, Rational):
            return NotImplemented

        return (
            self.numer == other.numer
            and self.denom == other.denom
        )

    def __hash__(self):
        """Return a hash based on the numerator and denominator."""
        return hash((self.numer, self.denom))

    def __add__(self, other):
        """Add two rational numbers."""
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        """Subtract two rational numbers."""
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        """Multiply two rational numbers."""
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        """Divide two rational numbers."""
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
        )

    def __abs__(self):
        """Return the absolute value."""
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        """Raise the rational number to a power."""
        if isinstance(power, int):
            if power < 0:
                if self.numer == 0:
                    raise ZeroDivisionError(
                        "Zero cannot have a negative power"
                    )

                return Rational(
                    self.denom ** (-power),
                    self.numer ** (-power)
                )

            return Rational(
                self.numer ** power,
                self.denom ** power
            )

        return (self.numer / self.denom) ** power

    def __rpow__(self, base):
        """Raise a real number to this rational power."""
        return base ** (self.numer / self.denom)
