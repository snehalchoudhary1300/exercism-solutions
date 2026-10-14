
"""Determine the winner of a Connect game."""


class ConnectGame:  # pylint: disable=too-few-public-methods
    """Represent a Connect game board."""

    def __init__(self, board):
        """Initialize the game board."""
        self.board = [
            line.split()
            for line in board.splitlines()
            if line.strip()
        ]

    def get_winner(self):
        """Return X, O, or an empty string if there is no winner."""
        if not self.board:
            return ""

        row_count = len(self.board)
        directions = [
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
        ]

        def has_connection(player, starting_positions, target):
            """Check whether a player connects their two edges."""
            visited = set()
            stack = list(starting_positions)

            while stack:
                current_row, current_col = stack.pop()

                if (current_row, current_col) in visited:
                    continue

                visited.add((current_row, current_col))

                if target(current_row, current_col):
                    return True

                for row_change, col_change in directions:
                    next_row = current_row + row_change
                    next_col = current_col + col_change

                    if (
                        0 <= next_row < row_count
                        and 0 <= next_col < len(self.board[next_row])
                        and self.board[next_row][next_col] == player
                        and (next_row, next_col) not in visited
                    ):
                        stack.append((next_row, next_col))

            return False

        # X connects the left edge to the right edge.
        x_starts = [
            (row_index, 0)
            for row_index in range(row_count)
            if self.board[row_index][0] == "X"
        ]

        if has_connection(
            "X",
            x_starts,
            lambda row_index, col_index: (
                col_index == len(self.board[row_index]) - 1
            ),
        ):
            return "X"

        # O connects the top edge to the bottom edge.
        o_starts = [
            (0, col_index)
            for col_index, cell in enumerate(self.board[0])
            if cell == "O"
        ]

        if has_connection(
            "O",
            o_starts,
            lambda row_index, col_index: row_index == row_count - 1,
        ):
            return "O"

        return ""
