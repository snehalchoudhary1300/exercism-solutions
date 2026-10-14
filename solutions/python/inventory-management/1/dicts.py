
"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount of each element."""
    inventory = {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """Remove an item from inventory."""
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """List items that have a count greater than zero."""
    available_items = []

    for item, count in inventory.items():
        if count > 0:
            available_items.append((item, count))

    return available_items
