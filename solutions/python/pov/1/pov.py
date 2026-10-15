
"""Reparent a tree from a selected node."""


class Tree:
    """Represent a tree with a name and child nodes."""

    def __init__(self, name, children=None):
        """Initialize a tree node."""
        self.name = name
        self.children = children if children is not None else []

    def __eq__(self, other):
        """Compare trees by their names and children."""
        return (
            isinstance(other, Tree)
            and self.name == other.name
            and self.children == other.children
        )

    def _get_nodes(self):
        """Collect nodes and their original parents."""
        nodes = {}
        parents = {}

        def visit(node, parent=None):
            nodes[node.name] = node
            parents[node.name] = parent

            for child in node.children:
                visit(child, node.name)

        visit(self)
        return nodes, parents

    def path_to(self, start, end):
        """Return the path between two nodes."""
        nodes, parents = self._get_nodes()

        if start not in nodes:
            raise ValueError("Tree could not be reoriented")

        if end not in nodes:
            raise ValueError("No path found")

        def ancestors(name):
            result = []

            while name is not None:
                result.append(name)
                name = parents[name]

            return result

        start_path = ancestors(start)
        end_path = ancestors(end)

        common = next(
            (name for name in start_path if name in end_path),
            None,
        )

        if common is None:
            raise ValueError("No path found")

        return (
            start_path[:start_path.index(common) + 1]
            + list(reversed(end_path[:end_path.index(common)]))
        )

    def from_pov(self, from_node):
        """Return a new tree rooted at the selected node."""
        nodes, parents = self._get_nodes()

        if from_node not in nodes:
            raise ValueError("Tree could not be reoriented")

        path = self.path_to(from_node, self.name)

        def rebuild(name, previous=None):
            original = nodes[name]
            children = []

            for child in original.children:
                if child.name != previous:
                    children.append(rebuild(child.name, name))

            parent = parents[name]

            if parent is not None and parent != previous:
                children.append(rebuild(parent, name))

            if name == from_node and len(path) > 2:
                original_child_count = len(original.children)
                children[:original_child_count] = reversed(
                    children[:original_child_count]
                )

            return Tree(name, children)

        return rebuild(from_node)
