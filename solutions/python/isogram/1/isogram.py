"""Check whether a word or phrase is an isogram."""


def is_isogram(phrase):
    """Return True if no letter is repeated in the phrase."""
    letters = [
        character.lower()
        for character in phrase
        if character.isalpha()
    ]

    return len(letters) == len(set(letters))
