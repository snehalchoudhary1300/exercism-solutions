
"""Recite the lyrics to Ten Green Bottles."""


NUMBERS = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}


def recite(start, take=1):
    """Return the requested verses as a list of lines."""
    lyrics = []

    for number in range(start, start - take, -1):
        current_number = NUMBERS[number].capitalize()
        next_number = NUMBERS[number - 1]

        current_bottle = "bottle" if number == 1 else "bottles"
        next_bottle = "bottle" if number - 1 == 1 else "bottles"

        lyrics.extend([
            f"{current_number} green {current_bottle} hanging on the wall,",
            f"{current_number} green {current_bottle} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_number} green {next_bottle} hanging on the wall.",
        ])

        if number > start - take + 1:
            lyrics.append("")

    return lyrics
