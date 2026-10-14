
"""Create a diamond shape using letters."""


def rows(letter):
    """Return the rows of a diamond ending with the given letter."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = alphabet.index(letter)
    diamond_rows = []
    width = letter_index * 2 + 1

    for index in range(letter_index + 1):
        character = alphabet[index]
        outside_spaces = letter_index - index

        if index == 0:
            row = " " * outside_spaces + character + " " * outside_spaces
        else:
            inside_spaces = index * 2 - 1
            row = (
                " " * outside_spaces
                + character
                + " " * inside_spaces
                + character
                + " " * outside_spaces
            )

        diamond_rows.append(row)

    diamond_rows.extend(diamond_rows[-2::-1])

    return diamond_rows
