
"""Determine a person's allergies from their score."""


ALLERGENS = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]


class Allergies:
    """Represent a person's allergies."""

    def __init__(self, score):
        """Initialize the allergy score."""
        self.score = score

    def allergic_to(self, item):
        """Return whether the person is allergic to an item."""
        if item not in ALLERGENS:
            return False

        allergen_score = 2 ** ALLERGENS.index(item)
        return bool(self.score & allergen_score)

    @property
    def lst(self):
        """Return the list of allergens present in the score."""
        return [
            allergen
            for index, allergen in enumerate(ALLERGENS)
            if self.score & (2 ** index)
        ]
