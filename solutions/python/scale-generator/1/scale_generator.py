
"""Generate chromatic and interval-based musical scales."""


SHARP_NOTES = [
    "A", "A#", "B", "C", "C#", "D",
    "D#", "E", "F", "F#", "G", "G#"
]

FLAT_NOTES = [
    "A", "Bb", "B", "C", "Db", "D",
    "Eb", "E", "F", "Gb", "G", "Ab"
]

FLAT_KEYS = {
    "F", "Bb", "Eb", "Ab", "Db", "Gb",
    "d", "g", "c", "f", "bb", "eb"
}


class Scale:
    """Represent a musical scale."""

    def __init__(self, tonic):
        """Initialize a scale with its tonic."""
        self.tonic = tonic[0].upper() + tonic[1:].lower()

        if tonic in FLAT_KEYS:
            self.notes = FLAT_NOTES
        else:
            self.notes = SHARP_NOTES

    def chromatic(self):
        """Return the twelve notes of the chromatic scale."""
        start = self.notes.index(self.tonic)
        return self.notes[start:] + self.notes[:start]

    def interval(self, intervals):
        """Return a scale generated from a sequence of intervals."""
        notes = self.chromatic()
        result = [notes[0]]
        position = 0

        for step in intervals:
            if step == "m":
                position += 1
            elif step == "M":
                position += 2
            elif step == "A":
                position += 3
            else:
                raise ValueError("Invalid interval")

            result.append(notes[position % 12])

        return result
