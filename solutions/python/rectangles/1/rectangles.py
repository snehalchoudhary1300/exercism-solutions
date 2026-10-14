
def rectangles(strings):
    if not strings:
        return 0

    count = 0
    rows = len(strings)
    cols = len(strings[0])

    for top in range(rows):
        for bottom in range(top + 1, rows):
            for left in range(cols):
                if strings[top][left] != "+" or strings[bottom][left] != "+":
                    continue

                for right in range(left + 1, cols):
                    if strings[top][right] != "+" or strings[bottom][right] != "+":
                        continue

                    # Check the top and bottom edges.
                    if not all(
                        strings[top][col] in "-+"
                        and strings[bottom][col] in "-+"
                        for col in range(left, right + 1)
                    ):
                        continue

                    # Check the left and right edges.
                    if not all(
                        strings[row][left] in "|+"
                        and strings[row][right] in "|+"
                        for row in range(top, bottom + 1)
                    ):
                        continue

                    count += 1

    return count
