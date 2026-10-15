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
                previous_roll = self.rolls[-1]

                if previous_roll + pins > 10:
                    raise ValueError("pin count exceeds pins on the lane")

                self.rolls.append(pins)
                self.frame += 1
                self.first_roll = True

            return

        self._roll_tenth_frame(pins)

    def _roll_tenth_frame(self, pins):
        """Validate and record rolls in the tenth frame."""
        tenth_frame_rolls = self.rolls[self._tenth_frame_start():]

        if len(tenth_frame_rolls) == 0:
            self.rolls.append(pins)
            return

        if len(tenth_frame_rolls) == 1:
            first_roll = tenth_frame_rolls[0]

            if first_roll == 10:
                self.rolls.append(pins)
                return

            if first_roll + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")

            self.rolls.append(pins)

            if first_roll + pins < 10:
                self.finished = True

            return

        first_roll, second_roll = tenth_frame_rolls[0], tenth_frame_rolls[1]

        if first_roll == 10 and second_roll < 10:
            if second_roll + pins > 10:
                raise ValueError("invalid fill balls")
        elif first_roll == 10 and second_roll == 10:
            pass
        elif first_roll + second_roll == 10:
            pass
        else:
            raise IndexError("cannot throw bonus with an open tenth frame")

        self.rolls.append(pins)
        self.finished = True

    def _tenth_frame_start(self):
        """Return the index where the tenth frame begins."""
        roll_index = 0
        frame_number = 1

        while frame_number < 10 and roll_index < len(self.rolls):
            if self.rolls[roll_index] == 10:
                roll_index += 1
            else:
                roll_index += 2

            frame_number += 1

        return roll_index

    def score(self):
        """Return the final score if the game is complete."""
        if not self.finished:
            raise IndexError("cannot score before the game is over")

        total_score = 0
        roll_index = 0

        for frame_number in range(10):
            if self.rolls[roll_index] == 10:
                total_score += (
                    10 + self.rolls[roll_index + 1]
                    + self.rolls[roll_index + 2]
                )
                roll_index += 1

            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2

            else:
                total_score += (
                    self.rolls[roll_index] + self.rolls[roll_index + 1]
                )
                roll_index += 2

        return total_score
