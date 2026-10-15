
"""Implement the logic for a Hangman game."""

STATUS_ONGOING = "ongoing"
STATUS_WIN = "win"
STATUS_LOSE = "lose"

STATUS_WON = STATUS_WIN
STATUS_LOST = STATUS_LOSE


class Hangman:
    """Manage a game of Hangman."""

    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.remaining_guesses = 9
        self.game_over = False

    def guess(self, letter):
        """Process a guessed letter."""
        if self.game_over:
            raise ValueError("The game has already ended.")

        letter = letter.lower()

        if letter in self.guessed_letters or letter not in self.word:
            self.remaining_guesses -= 1

        self.guessed_letters.add(letter)

        if all(
            character in self.guessed_letters
            for character in self.word
        ):
            self.game_over = True
        elif self.remaining_guesses < 0:
            self.game_over = True

    def get_masked_word(self):
        """Return the word with unguessed letters masked."""
        return "".join(
            character if character in self.guessed_letters else "_"
            for character in self.word
        )

    def get_status(self):
        """Return the current game status."""
        if all(
            character in self.guessed_letters
            for character in self.word
        ):
            return STATUS_WIN

        if self.remaining_guesses <= 0:
            return STATUS_LOSE

        return STATUS_ONGOING
