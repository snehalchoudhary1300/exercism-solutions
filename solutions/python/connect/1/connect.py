
"""Determine the winner of a Connect game."""


class ConnectGame:
    """Represent a Connect game board."""

    def __init__(self, board):
        """Initialize the board."""
        self.board = [
            line.split()
            for line in board.splitlines()
            if line.strip()
        ]

    def get_winner(self):
        """Return the winner or an empty string."""
        if not self.board:
            return ""

        rows = len(self.board)
        directions = [
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
        ]

        def has_connection(player, starts, target):
            """Check whether a player connects their target edges."""
            visited = set()
            stack = list(starts)

            while stack:
                row, col = stack.pop()

                if (row, col) in visited:
                    continue

                visited.add((row, col))

                if target(row, col):
                    return True

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < len(self.board[nr])
                        and self.board[nr][nc] == player
                        and (nr, nc) not in visited
                    ):
                        stack.append((nr, nc))

            return False

        # X connects the left edge to the right edge.
        x_starts = [
            (row, 0)
            for row in range(rows)
            if self.board[row][0] == "X"
        ]

        if has_connection(
            "X",
            x_starts,
            lambda row, col: col == len(self.board[row]) - 1,
        ):
            return "X"

        # O connects the top edge to the bottom edge.
        o_starts = [
            (0, col)
            for col, cell in enumerate(self.board[0])
            if cell == "O"
        ]

        if has_connection(
            "O",
            o_starts,
            lambda row, col: row == rows - 1,
        ):
            return "O"

        return ""
