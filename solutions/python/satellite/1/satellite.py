
"""Rebuild a binary tree from preorder and inorder traversals."""


def tree_from_traversals(preorder, inorder):
    """Build a nested dictionary representing the binary tree."""
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    def build(pre, ino):
        if not pre:
            return {}

        root_value = pre[0]
        root_index = ino.index(root_value)

        left_inorder = ino[:root_index]
        right_inorder = ino[root_index + 1:]
        left_size = len(left_inorder)

        left_tree = build(pre[1:left_size + 1], left_inorder)
        right_tree = build(pre[left_size + 1:], right_inorder)

        return {
            "v": root_value,
            "l": left_tree,
            "r": right_tree,
        }

    return build(list(preorder), list(inorder))
