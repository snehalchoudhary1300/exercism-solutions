
"""Manage a school's student roster."""


class School:
    """Represent a school and its student roster."""

    def __init__(self):
        """Initialize the school."""
        self.students = {}
        self.added_students = []

    def add_student(self, name, grade):
        """Add a student to a grade if not already enrolled."""
        if any(
            name in student_list
            for student_list in self.students.values()
        ):
            self.added_students.append(False)
            return

        if grade not in self.students:
            self.students[grade] = []

        self.students[grade].append(name)
        self.added_students.append(True)

    def added(self):
        """Return the results of all addition attempts."""
        return self.added_students

    def roster(self):
        """Return all students sorted by grade and name."""
        return [
            name
            for grade in sorted(self.students)
            for name in sorted(self.students[grade])
        ]

    def grade(self, grade_number):
        """Return students in the specified grade."""
        return sorted(self.students.get(grade_number, []))
