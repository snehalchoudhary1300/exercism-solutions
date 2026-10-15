"""Binary Search Tree implementation."""


class TreeNode:
    """Represent a node in a binary search tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """Insert a value into the tree."""
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        elif self.right is None:
            self.right = TreeNode(data)
        else:
            self.right.insert(data)

    def sorted_data(self):
        """Return values in ascending order."""
        result = []

        if self.left is not None:
            result.extend(self.left.sorted_data())

        result.append(self.data)

        if self.right is not None:
            result.extend(self.right.sorted_data())

        return result


# Alias for compatibility.
Node = TreeNode


class BinarySearchTree:
    """Represent a binary search tree."""

    def __init__(self, tree_data):
        self.root = None

        for value in tree_data:
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self.root.insert(value)

    def data(self):
        """Return the root node."""
        return self.root

    def sorted_data(self):
        """Return all values in ascending order."""
        if self.root is None:
            return []

        return self.root.sorted_data()