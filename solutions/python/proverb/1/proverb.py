
"""Generate a proverb from a list of words."""


def proverb(*items, qualifier=None):
    """Return the proverb based on the given items."""
    lines = []

    for index in range(len(items) - 1):
        lines.append(
            f"For want of a {items[index]} the {items[index + 1]} was lost."
        )

    if items:
        last_item = items[0]

        if qualifier:
            last_item = f"{qualifier} {last_item}"

        lines.append(f"And all for the want of a {last_item}.")

    return lines
