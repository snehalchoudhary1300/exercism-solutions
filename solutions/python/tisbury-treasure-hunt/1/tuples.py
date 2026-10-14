
"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return the coordinate from a treasure record."""
    return record[1]


def convert_coordinate(coordinate):
    """Split a coordinate string into individual components."""
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Check whether the coordinates in both records match."""
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine matching records into a single record."""
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean records and return them as a multi-line string."""
    result = ""

    for record in combined_record_group:
        cleaned_record = (record[0], record[2], record[3], record[4])
        result += str(cleaned_record) + "\n"

    return result
