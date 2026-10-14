
"""Translate English words into Pig Latin."""


def translate(text):
    """Return the Pig Latin translation of the given text."""
    words = text.split()
    result = []

    for word in words:
        if word[0] in "aeiou" or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        index = 0

        while index < len(word):
            if word[index] in "aeiou":
                break

            if word[index:index + 2] == "qu":
                index += 2
                break

            if word[index] == "y" and index > 0:
                break

            index += 1

        result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
