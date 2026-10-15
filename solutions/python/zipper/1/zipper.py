
"""Create and navigate a zipper for a binary tree."""


class Zipper:
    """Represent a focus within a binary tree."""

    def __init__(self, tree, parent=None, direction=None):
        self.tree = tree
        self.parent = parent
        self.direction = direction

    @staticmethod
    def from_tree(tree):
        """Create a zipper focused on the root."""
        if tree is None:
            return None
        return Zipper(tree)

    def value(self):
        """Return the value of the focused node."""
        return self.tree["value"]

    def set_value(self, value):
        """Return a zipper with the focused value changed."""
        new_tree = self._copy_tree(self.tree)
        new_tree["value"] = value
        return self._replace_tree(new_tree)

    def left(self):
        """Move focus to the left child."""
        if self.tree.get("left") is None:
            return None
        return Zipper(self.tree["left"], self, "left")

    def set_left(self, tree):
        """Replace the left child."""
        new_tree = self._copy_tree(self.tree)
        new_tree["left"] = tree
        return self._replace_tree(new_tree)

    def right(self):
        """Move focus to the right child."""
        if self.tree.get("right") is None:
            return None
        return Zipper(self.tree["right"], self, "right")

    def set_right(self, tree):
        """Replace the right child."""
        new_tree = self._copy_tree(self.tree)
        new_tree["right"] = tree
        return self._replace_tree(new_tree)

    def up(self):
        """Move focus to the parent node."""
        return self.parent

    def to_tree(self):
        """Return the complete tree with all changes."""
        zipper = self
        while zipper.parent is not None:
            zipper = zipper.parent
        return zipper.tree

    def _copy_tree(self, tree):
        """Make a copy of a tree node."""
        if tree is None:
            return None

        return {
            "value": tree["value"],
            "left": self._copy_tree(tree.get("left")),
            "right": self._copy_tree(tree.get("right")),
        }

    def _replace_tree(self, new_tree):
        """Return a zipper with the updated tree."""
        if self.parent is None:
            return Zipper(new_tree)

        parent_tree = self.parent._copy_tree(self.parent.tree)
        parent_tree[self.direction] = new_tree
        return self.parent._replace_tree(parent_tree)
