
"""Generate a D&D character with random ability scores."""

import random


def modifier(constitution):
    """Calculate the constitution modifier."""
    return (constitution - 10) // 2


class Character:
    """Represent a D&D character."""

    def __init__(self):
        """Generate ability scores and calculate hitpoints."""
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        """Roll four dice and sum the highest three."""
        dice_rolls = [
            random.randint(1, 6) for dice_number in range(4)
        ]
        dice_rolls.remove(min(dice_rolls))
        return sum(dice_rolls)
