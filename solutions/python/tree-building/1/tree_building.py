
"""Build a tree from unordered records."""


class Record:
    """Represent a record with an ID and parent ID."""

    def __init__(self, record_id, parent_id):
        """Initialize a record."""
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Represent a node in the tree."""

    def __init__(self, node_id):
        """Initialize a node."""
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """Build and return a tree from the records."""
    if not records:
        return None

    records = sorted(records, key=lambda record: record.record_id)

    for index, record in enumerate(records):
        if record.record_id != index:
            raise ValueError("Record id is invalid or out of order.")

    for record in records:
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError(
                    "Only root should have equal record and parent id."
                )
        elif record.parent_id >= record.record_id:
            raise ValueError(
                "Node parent_id should be smaller than its record_id."
            )

    nodes = [Node(record.record_id) for record in records]

    for record in records[1:]:
        nodes[record.parent_id].children.append(nodes[record.record_id])

    return nodes[0]
