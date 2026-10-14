
"""Encode and decode strings using run-length encoding."""


def encode(text):
    """Return the run-length encoded string."""
    if not text:
        return ""

    result = []
    count = 1

    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(text[index - 1])
            count = 1

    if count > 1:
        result.append(str(count))

    result.append(text[-1])

    return "".join(result)


def decode(text):
    """Return the original string from its run-length encoding."""
    result = []
    count = ""

    for character in text:
        if character.isdigit():
            count += character
        else:
            repetitions = int(count) if count else 1
            result.append(character * repetitions)
            count = ""

    return "".join(result)
