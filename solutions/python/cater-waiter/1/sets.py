
"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicate ingredients from a dish."""
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    """Identify a drink as a cocktail or mocktail."""
    if set(drink_ingredients) & ALCOHOLS:
        return drink_name + " Cocktail"
    return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize a dish based on its ingredients."""
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Find special ingredients in a dish."""
    dish_name, dish_ingredients = dish
    special = set(dish_ingredients) & SPECIAL_INGREDIENTS
    return dish_name, special


def compile_ingredients(dishes):
    """Compile all ingredients from a group of dishes."""
    ingredients = set()

    for dish in dishes:
        ingredients.update(dish)

    return ingredients


def separate_appetizers(dishes, appetizers):
    """Remove appetizers and duplicate dish names."""
    appetizer_set = set(appetizers)
    result = []

    for dish in dishes:
        if dish not in appetizer_set and dish not in result:
            result.append(dish)

    return result


def singleton_ingredients(dishes, intersection):
    """Find ingredients that appear in only one dish."""
    ingredient_counts = {}

    for dish in dishes:
        for ingredient in dish:
            ingredient_counts[ingredient] = (
                ingredient_counts.get(ingredient, 0) + 1
            )

    return {
        ingredient
        for ingredient, count in ingredient_counts.items()
        if count == 1 and ingredient not in intersection
    }
