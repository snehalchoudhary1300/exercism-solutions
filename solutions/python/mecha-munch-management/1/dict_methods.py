
"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    cart = {}

    for item in notes:
        cart[item] = 1

    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe, ingredients in recipe_updates:
        ideas[recipe] = ingredients

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart alphabetically."""
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order with aisle and refrigeration information."""
    fulfillment_cart = {}

    for item in sorted(cart, reverse=True):
        fulfillment_cart[item] = [cart[item]] + aisle_mapping[item]

    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, details in fulfillment_cart.items():
        store_inventory[item][0] -= details[0]

        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = "Out of Stock"

    return store_inventory
