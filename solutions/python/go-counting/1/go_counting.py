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

    def territory(self, x=None, y=None):
        """Return the owner and coordinates of a territory."""
        if isinstance(x, tuple) and y is None:
            x, y = x

        if (
            not isinstance(x, int)
            or isinstance(x, bool)
            or not isinstance(y, int)
            or isinstance(y, bool)
            or x < 0
            or x >= self.width
            or y < 0
            or y >= self.height
        ):
            raise ValueError("Invalid coordinate")

        # Occupied positions do not count as territory.
        if self.board[y][x] != NONE:
            return NONE, set()

        territory = set()
        visited = set()
        stack = [(x, y)]
        bordering_colors = set()

        while stack:
            current_x, current_y = stack.pop()
            coordinate = (current_x, current_y)

            if coordinate in visited:
                continue

            visited.add(coordinate)

            if self.board[current_y][current_x] == NONE:
                territory.add(coordinate)

                neighbors = [
                    (current_x - 1, current_y),
                    (current_x + 1, current_y),
                    (current_x, current_y - 1),
                    (current_x, current_y + 1),
                ]

                for next_x, next_y in neighbors:
                    if (
                        0 <= next_x < self.width
                        and 0 <= next_y < self.height
                        and (next_x, next_y) not in visited
                    ):
                        stack.append((next_x, next_y))
            else:
                bordering_colors.add(
                    self.board[current_y][current_x]
                )

        if len(bordering_colors) == 1:
            owner = bordering_colors.pop()
        else:
            owner = NONE

        return owner, territory

    def territories(self):
        """Return all territories for black, white, and neutral."""
        result = {
            BLACK: set(),
            WHITE: set(),
            NONE: set(),
        }
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != NONE or (x, y) in visited:
                    continue

                owner, territory = self.territory(x=x, y=y)
                visited.update(territory)
                result[owner].update(territory)

        return result