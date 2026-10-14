
"""Calculate a person's age on different planets."""


class SpaceAge:
    """Convert age in seconds to planetary years."""

    SECONDS_PER_EARTH_YEAR = 31557600

    def __init__(self, seconds):
        """Initialize with age in seconds."""
        self.seconds = seconds

    def age_on_planet(self, orbital_period):
        """Calculate age in years for a given orbital period."""
        return round(
            self.seconds / (self.SECONDS_PER_EARTH_YEAR * orbital_period),
            2,
        )

    def on_earth(self):
        """Return age in Earth years."""
        return self.age_on_planet(1.0)

    def on_mercury(self):
        """Return age in Mercury years."""
        return self.age_on_planet(0.2408467)

    def on_venus(self):
        """Return age in Venus years."""
        return self.age_on_planet(0.61519726)

    def on_mars(self):
        """Return age in Mars years."""
        return self.age_on_planet(1.8808158)

    def on_jupiter(self):
        """Return age in Jupiter years."""
        return self.age_on_planet(11.862615)

    def on_saturn(self):
        """Return age in Saturn years."""
        return self.age_on_planet(29.447498)

    def on_uranus(self):
        """Return age in Uranus years."""
        return self.age_on_planet(84.016846)

    def on_neptune(self):
        """Return age in Neptune years."""
        return self.age_on_planet(164.79132)
