
"""Convert numbers into English words."""


ONES = [
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]

TENS = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]


def convert_hundreds(number):
    """Convert a number below 1000 into words."""
    words = []

    if number >= 100:
        words.append(ONES[number // 100])
        words.append("hundred")
        number %= 100

    if number >= 20:
        words.append(TENS[number // 10])
        number %= 10

        if number:
            words[-1] += "-" + ONES[number]

    elif number > 0:
        words.append(ONES[number])

    return " ".join(words)


def say(number):
    """Return the English words for a number."""
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    scales = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
        (1, "")
    ]

    words = []

    for value, scale in scales:
        if number >= value:
            group = number // value
            number %= value

            if group:
                words.append(convert_hundreds(group))

                if scale:
                    words.append(scale)

    return " ".join(words)
