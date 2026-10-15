
"""Parse Smart Game Format (SGF) strings."""


class SgfTree:
    """Represent a node in an SGF tree."""

    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        return (
            self.properties == other.properties
            and self.children == other.children
        )

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    """Parse an SGF string into an SgfTree."""
    if not input_string or not input_string.startswith("("):
        raise ValueError("tree missing")

    index = 0
    length = len(input_string)

    def parse_value():
        nonlocal index
        index += 1
        value = []

        while index < length:
            char = input_string[index]

            if char == "]":
                index += 1
                return "".join(value)

            if char == "\\":
                index += 1
                if index >= length:
                    raise ValueError("properties without delimiter")

                escaped = input_string[index]
                if escaped == "\n":
                    index += 1
                    continue

                value.append(" " if escaped.isspace() else escaped)
                index += 1
                continue

            value.append(" " if char.isspace() and char != "\n" else char)
            index += 1

        raise ValueError("properties without delimiter")

    def parse_node():
        nonlocal index

        if index >= length or input_string[index] != ";":
            raise ValueError("tree with no nodes")

        index += 1
        properties = {}

        while index < length and input_string[index] not in ";()":
            start = index

            while index < length and input_string[index].isalpha():
                index += 1

            key = input_string[start:index]

            if not key or not key.isupper():
                raise ValueError("property must be in uppercase")

            if index >= length or input_string[index] != "[":
                raise ValueError("properties without delimiter")

            values = []
            while index < length and input_string[index] == "[":
                values.append(parse_value())

            properties[key] = values

        return SgfTree(properties, [])

    def parse_sequence():
        nonlocal index
        root = parse_node()
        current = root

        while index < length and input_string[index] == ";":
            child = parse_node()
            current.children.append(child)
            current = child

        return root

    def parse_tree():
        nonlocal index

        if index >= length or input_string[index] != "(":
            raise ValueError("tree missing")

        index += 1

        if index >= length or input_string[index] != ";":
            raise ValueError("tree with no nodes")

        root = parse_sequence()

        while index < length and input_string[index] == "(":
            root.children.append(parse_tree())

        if index >= length or input_string[index] != ")":
            raise ValueError("tree missing")

        index += 1
        return root

    tree = parse_tree()

    if index != length:
        raise ValueError("tree missing")

    return tree
