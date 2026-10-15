
"""Implement a custom set containing unique elements."""


class CustomSet:
    """Represent a set of unique elements."""

    __hash__ = None

    def __init__(self, elements=None):
        """Initialize the set without duplicate elements."""
        if elements is None:
            elements = []

        self.elements = []
        for element in elements:
            self.add(element)

    def isempty(self):
        """Return True if the set is empty."""
        return len(self.elements) == 0

    def __contains__(self, element):
        """Check whether an element belongs to the set."""
        return element in self.elements

    def issubset(self, other):
        """Check whether every element belongs to the other set."""
        return all(element in other for element in self.elements)

    def isdisjoint(self, other):
        """Check whether the sets have no common elements."""
        return not any(element in other for element in self.elements)

    def __eq__(self, other):
        """Compare sets without considering element order."""
        if not isinstance(other, CustomSet):
            return NotImplemented

        return (
            len(self.elements) == len(other.elements)
            and self.issubset(other)
        )

    def add(self, element):
        """Add an element if it is not already present."""
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        """Return the elements common to both sets."""
        return CustomSet(
            element for element in self.elements if element in other
        )

    def __sub__(self, other):
        """Return elements present only in this set."""
        return CustomSet(
            element for element in self.elements if element not in other
        )

    def __add__(self, other):
        """Return the union of both sets."""
        return CustomSet(
            self.elements + other.elements
        )
