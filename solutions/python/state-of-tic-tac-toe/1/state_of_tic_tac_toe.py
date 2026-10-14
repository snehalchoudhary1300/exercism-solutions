
"""Determine the state of a Tic-Tac-Toe game."""


def gamestate(board):
    """Return the game state or raise ValueError for an invalid board."""
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    lines = list(board)

    for column in range(3):
        lines.append(
            "".join(board[row][column] for row in range(3))
        )

    lines.append("".join(board[index][index] for index in range(3)))
    lines.append("".join(board[index][2 - index] for index in range(3)))

    x_wins = "XXX" in lines
    o_wins = "OOO" in lines

    if x_wins and o_wins:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins and x_count != o_count + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_wins and x_count != o_count:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins or o_wins:
        return "win"

    if x_count + o_count == 9:
        return "draw"

    return "ongoing"
