"""Calculate the degree of separation between family members."""

from collections import deque


# pylint: disable=too-few-public-methods
class RelativeDistance:
    """Find the shortest relationship distance in a family tree."""

    def __init__(self, family_tree):
        """Store the family tree and build a relationship graph."""
        self.family_tree = family_tree
        self.graph = {}

        for parent, children in family_tree.items():
            self.graph.setdefault(parent, set())

            for child in children:
                self.graph.setdefault(child, set())
                self.graph[parent].add(child)
                self.graph[child].add(parent)

            for child in children:
                for sibling in children:
                    if child != sibling:
                        self.graph[child].add(sibling)

    def degree_of_separation(self, person_a, person_b):
        """Return the shortest number of connections between two people."""
        if person_a not in self.graph:
            raise ValueError("Person A not in family tree.")

        if person_b not in self.graph:
            raise ValueError("Person B not in family tree.")

        queue = deque([(person_a, 0)])
        visited = {person_a}

        while queue:
            person, distance = queue.popleft()

            if person == person_b:
                return distance

            for relative in self.graph[person]:
                if relative not in visited:
                    visited.add(relative)
                    queue.append((relative, distance + 1))

        raise ValueError("No connection between person A and person B.")
