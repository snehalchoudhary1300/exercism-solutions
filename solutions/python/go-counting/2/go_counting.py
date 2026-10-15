"""Count territory on a Go board."""

BLACK = "B"
WHITE = "W"
NONE = " "


class Board:
    """Represent a Go board and calculate territory."""

    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0]) if board else 0

    def _valid_coordinate(self, x, y):
        """Check whether a coordinate is on the board."""
        return (
            isinstance(x, int)
            and not isinstance(x, bool)
            and isinstance(y, int)
            and not isinstance(y, bool)
            and 0 <= x < self.width
            and 0 <= y < self.height
        )

    def territory(self, x=None, y=None):
        """Return the owner and coordinates of a territory."""
        if isinstance(x, tuple) and y is None:
            x, y = x

        if not self._valid_coordinate(x, y):
            raise ValueError("Invalid coordinate")

        if self.board[y][x] != NONE:
            return NONE, set()

        territory_coordinates = set()
        visited = set()
        stack = [(x, y)]
        bordering_colors = set()

        while stack:
            column, row = stack.pop()
            coordinate = (column, row)

            if coordinate in visited:
                continue

            visited.add(coordinate)

            if self.board[row][column] == NONE:
                territory_coordinates.add(coordinate)

                neighbors = [
                    (column - 1, row),
                    (column + 1, row),
                    (column, row - 1),
                    (column, row + 1),
                ]

                for next_column, next_row in neighbors:
                    if (
                        self._valid_coordinate(next_column, next_row)
                        and (next_column, next_row) not in visited
                    ):
                        stack.append((next_column, next_row))
            else:
                bordering_colors.add(self.board[row][column])

        if len(bordering_colors) == 1:
            owner = bordering_colors.pop()
        else:
            owner = NONE

        return owner, territory_coordinates

    def territories(self):
        """Return all territories for black, white, and neutral."""
        result = {
            BLACK: set(),
            WHITE: set(),
            NONE: set(),
        }
        visited = set()

        for row in range(self.height):
            for column in range(self.width):
                if (
                    self.board[row][column] != NONE
                    or (column, row) in visited
                ):
                    continue

                owner, territory_coordinates = self.territory(
                    x=column, y=row
                )
                visited.update(territory_coordinates)
                result[owner].update(territory_coordinates)

        return result