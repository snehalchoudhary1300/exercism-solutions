

"""Store Scrabble letters and their point values."""


def transform(legacy_data):
    """Convert grouped letter scores into individual letter scores."""
    result = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = score

    return result
