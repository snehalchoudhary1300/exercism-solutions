
"""Implement a doubly linked list."""

from dataclasses import dataclass


@dataclass
class Node:
    """Represent a node in a doubly linked list."""

    value: object
    next: object = None
    prev: object = None


class LinkedList:
    """Represent a doubly linked list of nodes."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        """Add a value to the end of the list."""
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return new_node

    def pop(self):
        """Remove and return the last value."""
        if self.tail is None:
            raise IndexError("List is empty")

        removed_node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = removed_node.prev
            self.tail.next = None

        self.length -= 1
        return removed_node.value

    def shift(self):
        """Remove and return the first value."""
        if self.head is None:
            raise IndexError("List is empty")

        removed_node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = removed_node.next
            self.head.prev = None

        self.length -= 1
        return removed_node.value

    def unshift(self, value):
        """Add a value to the beginning of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return new_node

    def delete(self, value):
        """Remove the first node containing the specified value."""
        current = self.head

        while current is not None:
            if current.value == value:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev

                self.length -= 1
                return

            current = current.next

        raise ValueError("Value not found")

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.length

    def __iter__(self):
        """Iterate over the values in the list."""
        current = self.head

        while current is not None:
            yield current.value
            current = current.next
