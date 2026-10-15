
"""Generate the lyrics of the song about an old lady."""

ANIMALS = [
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse",
]

COMMENTS = [
    "",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]


def verse(number):
    """Return one verse of the song."""
    animal = ANIMALS[number - 1]
    lines = [f"I know an old lady who swallowed a {animal}."]

    if number == 8:
        lines.append(COMMENTS[number - 1])
        return lines

    if number > 1:
        lines.append(COMMENTS[number - 1])

    for index in range(number - 1, 0, -1):
        current = ANIMALS[index]
        previous = ANIMALS[index - 1]

        if current == "spider":
            lines.append(
                "She swallowed the spider to catch the fly."
            )
        elif current == "bird":
            lines.append(
                "She swallowed the bird to catch the spider "
                "that wriggled and jiggled and tickled inside her."
            )
        else:
            lines.append(
                f"She swallowed the {current} to catch the {previous}."
            )

    lines.append(
        "I don't know why she swallowed the fly. Perhaps she'll die."
    )

    return lines


def recite(start, end):
    """Return the song verses from start to end."""
    result = []

    for number in range(start, end + 1):
        result.extend(verse(number))
        if number != end:
            result.append("")

    return result
