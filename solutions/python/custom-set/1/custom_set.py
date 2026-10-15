
class CustomSet:
    """Represent a set of unique elements."""

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
        """Return True if every element belongs to the other set."""
        for element in self.elements:
            if element not in other:
                return False
        return True

    def isdisjoint(self, other):
        """Return True if the sets have no common elements."""
        for element in self.elements:
            if element in other:
                return False
        return True

    def __eq__(self, other):
        """Compare two sets without considering element order."""
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
        result = CustomSet()

        for element in self.elements:
            if element in other:
                result.add(element)

        return result

    def __sub__(self, other):
        """Return elements that are in this set but not the other."""
        result = CustomSet()

        for element in self.elements:
            if element not in other:
                result.add(element)

        return result

    def __add__(self, other):
        """Return the union of both sets."""
        result = CustomSet(self.elements)

        for element in other.elements:
            result.add(element)

        return result
