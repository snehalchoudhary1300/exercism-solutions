
"""Convert delivery date descriptions into actual delivery dates."""

from datetime import datetime, timedelta


def delivery_date(start, description):
    """Calculate the delivery date from the meeting start and description."""
    start = datetime.fromisoformat(start)

    if description == "NOW":
        result = start + timedelta(hours=2)
        return result.isoformat()

    if description == "ASAP":
        if start.hour < 13:
            result = start.replace(
                hour=17, minute=0, second=0, microsecond=0
            )
        else:
            result = (start + timedelta(days=1)).replace(
                hour=13, minute=0, second=0, microsecond=0
            )
        return result.isoformat()

    if description == "EOW":
        if start.weekday() <= 2:
            days = 4 - start.weekday()
            result = start + timedelta(days=days)
            result = result.replace(
                hour=17, minute=0, second=0, microsecond=0
            )
        else:
            days = 6 - start.weekday()
            result = start + timedelta(days=days)
            result = result.replace(
                hour=20, minute=0, second=0, microsecond=0
            )
        return result.isoformat()

    if description.endswith("M"):
        month = int(description[:-1])
        year = start.year + (month <= start.month)

        result = datetime(year, month, 1, 8, 0)

        while result.weekday() >= 5:
            result += timedelta(days=1)

        return result.isoformat()

    if description.startswith("Q"):
        quarter = int(description[1:])
        quarter_end_month = quarter * 3

        year = start.year + (quarter_end_month < start.month)

        result = datetime(year, quarter_end_month, 1, 8, 0)

        # Move to the final day of the quarter.
        if quarter_end_month == 12:
            result = datetime(year + 1, 1, 1, 8, 0)
        else:
            result = datetime(year, quarter_end_month + 1, 1, 8, 0)

        result -= timedelta(days=1)

        while result.weekday() >= 5:
            result -= timedelta(days=1)

        return result.isoformat()

    raise ValueError("Invalid delivery date description.")
