
"""Check whether brackets are correctly balanced."""


def is_paired(input_string):
    """Return True if all brackets are correctly matched and nested."""
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for character in input_string:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0
