from math import gcd


class Rational:
    def __init__(self, numer, denom):
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
        return (
            self.numer == other.numer
            and self.denom == other.denom
        )

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
        )

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
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
        return base ** (self.numer / self.denom)
