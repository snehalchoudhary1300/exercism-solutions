
"""Generate unique random robot names."""

import random
import string


used_names = set()


class Robot:
    """Represent a robot with a unique random name."""

    def __init__(self):
        """Initialize a robot without a name."""
        self._name = None

    @property
    def name(self):
        """Return the robot's name, generating one if needed."""
        if self._name is None:
            while True:
                letters = ''.join(
                    random.choices(string.ascii_uppercase, k=2)
                )
                digits = ''.join(
                    random.choices(string.digits, k=3)
                )
                new_name = letters + digits

                if new_name not in used_names:
                    used_names.add(new_name)
                    self._name = new_name
                    break

        return self._name

    def reset(self):
        """Reset the robot's name."""
        self._name = None
