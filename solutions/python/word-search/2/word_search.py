
"""Find words in a word search puzzle."""


class Point:
    """Represent a point in the puzzle."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class WordSearch:
    """Search for words in a letter grid."""

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.columns = len(puzzle[0]) if puzzle else 0

    def search(self, word):
        """Find a word and return its start and end points."""
        if not word:
            return None

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        for row in range(self.rows):
            for column in range(self.columns):
                for row_step, column_step in directions:
                    end_row = row + (len(word) - 1) * row_step
                    end_column = column + (len(word) - 1) * column_step

                    if not (
                        0 <= end_row < self.rows
                        and 0 <= end_column < self.columns
                    ):
                        continue

                    found = True

                    for index, letter in enumerate(word):
                        current_row = row + index * row_step
                        current_column = column + index * column_step

                        if (
                            self.puzzle[current_row][current_column]
                            != letter
                        ):
                            found = False
                            break

                    if found:
                        return (
                            Point(column, row),
                            Point(end_column, end_row),
                        )

        return None
