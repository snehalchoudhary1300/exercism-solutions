"""Calculate scores for a ten-frame bowling game."""


class BowlingGame:
    """Track rolls and calculate a bowling game's score."""

    def __init__(self):
        """Initialize a new bowling game."""
        self.rolls = []
        self.finished = False

    def _tenth_frame_start(self):
        """Find the index where the tenth frame begins."""
        roll_index = 0
        frames = 0

        while frames < 9:
            if roll_index >= len(self.rolls):
                return None

            if self.rolls[roll_index] == 10:
                roll_index += 1
            else:
                if roll_index + 1 >= len(self.rolls):
                    return None
                roll_index += 2

            frames += 1

        return roll_index

    def roll(self, pins):
        """Record a roll after validating the rules."""
        if self.finished:
            raise IndexError("cannot roll after game is over")

        if not isinstance(pins, int) or isinstance(pins, bool):
            raise ValueError("invalid number of pins")

        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")

        tenth_start = self._tenth_frame_start()

        if tenth_start is None:
            if self.rolls:
                previous_roll = self.rolls[-1]

                if previous_roll != 10:
                    frame_start = len(self.rolls) - 1
                    if frame_start >= 0:
                        frame_index = 0
                        index = 0

                        while index < frame_start:
                            if self.rolls[index] == 10:
                                index += 1
                            else:
                                index += 2
                            frame_index += 1

                        if (
                            index == frame_start
                            and frame_index < 9
                            and previous_roll + pins > 10
                        ):
                            raise ValueError(
                                "pin count exceeds pins on the lane"
                            )

            self.rolls.append(pins)
            return

        tenth_rolls = self.rolls[tenth_start:]

        if len(tenth_rolls) == 0:
            self.rolls.append(pins)
            return

        if len(tenth_rolls) == 1:
            first_roll = tenth_rolls[0]

            if first_roll != 10 and first_roll + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")

            self.rolls.append(pins)

            if first_roll != 10 and first_roll + pins < 10:
                self.finished = True

            return

        first_roll, second_roll = tenth_rolls[:2]

        if first_roll == 10:
            if second_roll < 10 and second_roll + pins > 10:
                raise ValueError("invalid fill balls")
        elif first_roll + second_roll == 10:
            pass
        else:
            raise IndexError("cannot throw bonus with an open tenth frame")

        self.rolls.append(pins)
        self.finished = True

    def score(self):
        """Return the total score for a completed game."""
        if not self.finished:
            raise IndexError("cannot score before the game is over")

        total_score = 0
        roll_index = 0
        frames_scored = 0

        while frames_scored < 10:
            first_roll = self.rolls[roll_index]

            if first_roll == 10:
                total_score += (
                    10
                    + self.rolls[roll_index + 1]
                    + self.rolls[roll_index + 2]
                )
                roll_index += 1
            elif first_roll + self.rolls[roll_index + 1] == 10:
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                total_score += (
                    first_roll + self.rolls[roll_index + 1]
                )
                roll_index += 2

            frames_scored += 1

        return total_score
