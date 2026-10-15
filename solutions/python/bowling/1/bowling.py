"""Keep track of a bowling game's score."""


class BowlingGame:
    """Calculate the score of a ten-frame bowling game."""

    def __init__(self):
        """Initialize an empty game."""
        self.rolls = []
        self.frame = 1
        self.first_roll = True
        self.finished = False

    def roll(self, pins):
        """Record a roll and validate the game rules."""
        if self.finished:
            raise IndexError("cannot roll after game is over")

        if not isinstance(pins, int) or isinstance(pins, bool):
            raise ValueError("invalid number of pins")

        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")

        if self.frame < 10:
            if self.first_roll:
                self.rolls.append(pins)

                if pins == 10:
                    self.frame += 1
                    self.first_roll = True
                else:
                    self.first_roll = False
            else:
                previous = self.rolls[-1]

                if previous + pins > 10:
                    raise ValueError("pin count exceeds pins on the lane")

                self.rolls.append(pins)
                self.frame += 1
                self.first_roll = True

            return

        self._roll_tenth_frame(pins)

    def _roll_tenth_frame(self, pins):
        """Validate and record rolls in the tenth frame."""
        tenth_rolls = self.rolls[self._tenth_frame_start():]

        if len(tenth_rolls) == 0:
            self.rolls.append(pins)

            if pins == 10:
                return

            return

        if len(tenth_rolls) == 1:
            first = tenth_rolls[0]

            if first == 10:
                self.rolls.append(pins)
                return

            if first + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")

            self.rolls.append(pins)

            if first + pins < 10:
                self.finished = True

            return

        first, second = tenth_rolls[0], tenth_rolls[1]

        if first == 10 and second < 10:
            if second + pins > 10:
                raise ValueError("invalid fill balls")
        elif first == 10 and second == 10:
            pass
        elif first + second == 10:
            pass
        else:
            raise IndexError("cannot throw bonus with an open tenth frame")

        self.rolls.append(pins)
        self.finished = True

    def _tenth_frame_start(self):
        """Return the index where the tenth frame begins."""
        index = 0
        frame = 1

        while frame < 10 and index < len(self.rolls):
            if self.rolls[index] == 10:
                index += 1
            else:
                index += 2
            frame += 1

        return index

    def score(self):
        """Return the final score if the game is complete."""
        if not self.finished:
            raise IndexError("cannot score before the game is over")

        total = 0
        index = 0

        for _ in range(10):
            if self.rolls[index] == 10:
                total += 10 + self.rolls[index + 1] + self.rolls[index + 2]
                index += 1
            elif self.rolls[index] + self.rolls[index + 1] == 10:
                total += 10 + self.rolls[index + 2]
                index += 2
            else:
                total += self.rolls[index] + self.rolls[index + 1]
                index += 2

        return total
