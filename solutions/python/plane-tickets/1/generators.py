
"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate seat letters from A to D."""
    letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate seat numbers, skipping row 13."""
    row = 1

    for letter in generate_seat_letters(number):
        if row == 13:
            row += 1

        yield f"{row}{letter}"

        if letter == "D":
            row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""
    assignments = {}

    for passenger, seat in zip(passengers, generate_seats(len(passengers))):
        assignments[passenger] = seat

    return assignments


def generate_codes(seat_numbers, flight_id):
    """Generate 12-character ticket codes."""
    for seat in seat_numbers:
        code = seat + flight_id
        yield code.ljust(12, "0")
