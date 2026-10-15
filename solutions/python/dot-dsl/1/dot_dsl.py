
"""Create graph structures using a domain-specific language."""

NODE, EDGE, ATTR = range(3)


class Node:
    """Represent a graph node."""

    def __init__(self, name, attrs):
        """Initialize a node with its name and attributes."""
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        """Compare nodes by name and attributes."""
        if not isinstance(other, Node):
            return NotImplemented
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    """Represent an edge between two nodes."""

    def __init__(self, src, dst, attrs):
        """Initialize an edge with its source, destination, and attributes."""
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        """Compare edges by endpoints and attributes."""
        if not isinstance(other, Edge):
            return NotImplemented
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    """Represent a graph containing nodes, edges, and attributes."""

    def __init__(self, data=None):
        """Build a graph from DSL tuples."""
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is None:
            return

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for item in data:
            if not isinstance(item, tuple) or len(item) < 2:
                raise TypeError("Graph item incomplete")

            kind = item[0]

            if kind == ATTR:
                self._add_attribute(item)
            elif kind == NODE:
                self._add_node(item)
            elif kind == EDGE:
                self._add_edge(item)
            else:
                raise ValueError("Unknown item")

    def _add_attribute(self, item):
        """Add a graph attribute."""
        if (
            len(item) != 3
            or not isinstance(item[1], str)
            or not isinstance(item[2], str)
        ):
            raise ValueError("Attribute is malformed")

        self.attrs[item[1]] = item[2]

    def _add_node(self, item):
        """Add a node to the graph."""
        if (
            len(item) != 3
            or not isinstance(item[1], str)
            or not isinstance(item[2], dict)
        ):
            raise ValueError("Node is malformed")

        self.nodes.append(Node(item[1], item[2]))

    def _add_edge(self, item):
        """Add an edge to the graph."""
        if (
            len(item) != 4
            or not isinstance(item[1], str)
            or not isinstance(item[2], str)
            or not isinstance(item[3], dict)
        ):
            raise ValueError("Edge is malformed")

        self.edges.append(Edge(item[1], item[2], item[3]))
