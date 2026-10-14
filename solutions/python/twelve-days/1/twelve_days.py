
"""Generate the lyrics of The Twelve Days of Christmas."""

ORDINALS = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

GIFTS = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]


def recite(start_verse, end_verse):
    """Return the requested verses of the song."""
    verses = []

    for verse_number in range(start_verse, end_verse + 1):
        gifts = GIFTS[:verse_number][::-1]

        if verse_number == 1:
            gift_text = gifts[0] + "."
        else:
            gift_text = ", ".join(gifts[:-1])
            gift_text += ", and " + gifts[-1] + "."

        verse = (
            f"On the {ORDINALS[verse_number - 1]} day of Christmas "
            f"my true love gave to me: {gift_text}"
        )
        verses.append(verse)

    return verses
