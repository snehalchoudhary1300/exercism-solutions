
"""Check whether a number is valid using the Luhn algorithm."""


class Luhn:
    """Validate a number using the Luhn checksum."""

    def __init__(self, card_num):
        """Store the number to validate."""
        self.card_num = card_num

    def valid(self):
        """Return True if the number passes the Luhn check."""
        number = self.card_num.replace(" ", "")

        if len(number) <= 1:
            return False

        if not number.isascii() or not number.isdigit():
            return False

        total = 0

        for index, digit in enumerate(reversed(number)):
            value = int(digit)

            if index % 2 == 1:
                value *= 2

                if value > 9:
                    value -= 9

            total += value

        return total % 10 == 0
