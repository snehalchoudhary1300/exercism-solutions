
"""Encode and decode strings using run-length encoding."""


def encode(s):
    """Return the run-length encoded string."""
    if not s:
        return ""

    result = []
    count = 1

    for index in range(1, len(s)):
        if s[index] == s[index - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(s[index - 1])
            count = 1

    if count > 1:
        result.append(str(count))

    result.append(s[-1])

    return "".join(result)


def decode(s):
    """Return the original string from its run-length encoding."""
    result = []
    count = ""

    for character in s:
        if character.isdigit():
            count += character
        else:
            repetitions = int(count) if count else 1
            result.append(character * repetitions)
            count = ""

    return "".join(result)
