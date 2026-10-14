
"""Recite verses from 'This is the House that Jack Built'."""

def recite(start_verse, end_verse):
    """Return the requested verses."""
    phrases = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to"),
    ]

    verses = []

    for verse_number in range(start_verse, end_verse + 1):
        parts = ["This is " + phrases[verse_number - 1][0]]

        for phrase_number in range(verse_number - 1, 0, -1):
            parts.append(phrases[phrase_number][1] + " " + phrases[phrase_number - 1][0])

        verses.append(" ".join(parts) if verse_number == 1 else " ".join(parts))

    return verses
