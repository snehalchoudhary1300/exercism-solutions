
"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location and health."""

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize an alien."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrease alien health by one."""
        self.health -= 1

    def is_alive(self):
        """Return True if the alien is alive."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move the alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Handle collision detection."""
        pass


def new_aliens_collection(positions):
    """Create a list of aliens from coordinate pairs."""
    aliens = []

    for x_coordinate, y_coordinate in positions:
        aliens.append(Alien(x_coordinate, y_coordinate))

    return aliens
