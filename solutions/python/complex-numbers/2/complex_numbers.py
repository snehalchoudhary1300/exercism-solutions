
"""Implement complex number operations without built-in complex numbers."""

import math


class ComplexNumber:
    """Represent a complex number."""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        """Compare two complex numbers."""
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        return (
            math.isclose(self.real, other.real, rel_tol=1e-9, abs_tol=1e-9)
            and math.isclose(
                self.imaginary,
                other.imaginary,
                rel_tol=1e-9,
                abs_tol=1e-9,
            )
        )

    def __hash__(self):
        """Return a hash based on the real and imaginary parts."""
        return hash((self.real, self.imaginary))

    def __add__(self, other):
        """Add two complex numbers or a real number."""
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)

        if not isinstance(other, ComplexNumber):
            return NotImplemented

        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def __radd__(self, other):
        """Support addition with a real number on the left."""
        return self + other

    def __sub__(self, other):
        """Subtract two complex numbers or a real number."""
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)

        if not isinstance(other, ComplexNumber):
            return NotImplemented

        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary,
        )

    def __rsub__(self, other):
        """Support subtraction with a real number on the left."""
        if isinstance(other, (int, float)):
            return ComplexNumber(other, 0) - self

        return NotImplemented

    def __mul__(self, other):
        """Multiply two complex numbers or a real number."""
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)

        if not isinstance(other, ComplexNumber):
            return NotImplemented

        real = (
            self.real * other.real
            - self.imaginary * other.imaginary
        )
        imaginary = (
            self.real * other.imaginary
            + self.imaginary * other.real
        )

        return ComplexNumber(real, imaginary)

    def __rmul__(self, other):
        """Support multiplication with a real number on the left."""
        return self * other

    def __truediv__(self, other):
        """Divide two complex numbers or a real number."""
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)

        if not isinstance(other, ComplexNumber):
            return NotImplemented

        denominator = other.real ** 2 + other.imaginary ** 2

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        real = (
            self.real * other.real
            + self.imaginary * other.imaginary
        ) / denominator

        imaginary = (
            self.imaginary * other.real
            - self.real * other.imaginary
        ) / denominator

        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other):
        """Support division with a real number on the left."""
        if isinstance(other, (int, float)):
            return ComplexNumber(other, 0) / self

        return NotImplemented

    def __abs__(self):
        """Return the absolute value of the complex number."""
        return math.sqrt(
            self.real ** 2 + self.imaginary ** 2
        )

    def conjugate(self):
        """Return the complex conjugate."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """Return e raised to this complex number."""
        magnitude = math.exp(self.real)

        return ComplexNumber(
            magnitude * math.cos(self.imaginary),
            magnitude * math.sin(self.imaginary),
        )
