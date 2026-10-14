
"""Simulate a robot moving on a grid."""

NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"

DIRECTIONS = (NORTH, EAST, SOUTH, WEST)


class Robot:  # pylint: disable=too-few-public-methods
    """Represent a robot with a position and direction."""

    def __init__(self, direction, x_coordinate, y_coordinate):
        """Initialize the robot."""
        if direction not in DIRECTIONS:
            raise ValueError("Invalid direction")

        self.direction = direction
        self.coordinates = (x_coordinate, y_coordinate)

    def move(self, instructions):
        """Execute the robot's movement instructions."""
        x_coordinate, y_coordinate = self.coordinates
        direction_index = DIRECTIONS.index(self.direction)

        for instruction in instructions:
            if instruction == "R":
                direction_index = (direction_index + 1) % 4
            elif instruction == "L":
                direction_index = (direction_index - 1) % 4
            elif instruction == "A":
                if direction_index == 0:
                    y_coordinate += 1
                elif direction_index == 1:
                    x_coordinate += 1
                elif direction_index == 2:
                    y_coordinate -= 1
                else:
                    x_coordinate -= 1
            else:
                raise ValueError("Invalid instruction")

        self.direction = DIRECTIONS[direction_index]
        self.coordinates = (x_coordinate, y_coordinate)
