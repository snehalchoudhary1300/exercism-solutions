
"""Manage the plants in a kindergarten garden."""


class Garden:
    """Represent a kindergarten garden."""

    PLANT_NAMES = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }

    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry",
    ]

    def __init__(self, diagram, students=None):
        """Initialize the garden."""
        self.rows = diagram.splitlines()
        self.students = sorted(
            students if students is not None else self.DEFAULT_STUDENTS
        )

    def plants(self, student):
        """Return the four plants belonging to a student."""
        student_index = self.students.index(student)
        start = student_index * 2

        return [
            self.PLANT_NAMES[plant]
            for row in self.rows
            for plant in row[start:start + 2]
        ]
