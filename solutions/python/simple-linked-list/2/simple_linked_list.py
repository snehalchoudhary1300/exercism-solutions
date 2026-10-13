
"""Functions for implementing a singly linked list."""


class EmptyListException(Exception):
    """Exception raised when an operation is performed on an empty list."""


class Node:
    """Represent a node containing a value and a link to the next node."""

    def __init__(self, value):
        """Initialize a node with a value."""
        self._value = value
        self._next = None

    def value(self):
        """Return the value stored in the node."""
        return self._value

    def next(self):
        """Return the next node."""
        return self._next

    def set_next(self, node):
        """Set the next node."""
        self._next = node


class LinkedList:
    """Represent a singly linked list."""

    def __init__(self, values=None):
        """Initialize the list with optional values."""
        self._head = None

        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self):
        """Iterate over the values in the list."""
        current = self._head

        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        """Return the number of values in the list."""
        count = 0
        current = self._head

        while current is not None:
            count += 1
            current = current.next()

        return count

    def head(self):
        """Return the first node or raise an exception if empty."""
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        """Add a value to the beginning of the list."""
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node

    def pop(self):
        """Remove and return the first value in the list."""
        if self._head is None:
            raise EmptyListException("The list is empty.")

        value = self._head.value()
        self._head = self._head.next()
        return value

    def reversed(self):
        """Return a new linked list with values in reverse order."""
        new_list = LinkedList()

        for value in self:
            new_list.push(value)

        return new_list
