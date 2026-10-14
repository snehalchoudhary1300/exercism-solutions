
"""Convert delivery date descriptions into actual delivery dates."""

from datetime import datetime, timedelta


def _now(start):
    """Return the date two hours after the meeting."""
    return start + timedelta(hours=2)


def _asap(start):
    """Return the ASAP delivery date."""
    if start.hour < 13:
        return start.replace(
            hour=17, minute=0, second=0, microsecond=0
        )

    return (start + timedelta(days=1)).replace(
        hour=13, minute=0, second=0, microsecond=0
    )


def _eow(start):
    """Return the end-of-week delivery date."""
    if start.weekday() <= 2:
        days = 4 - start.weekday()
        hour = 17
    else:
        days = 6 - start.weekday()
        hour = 20

    return (start + timedelta(days=days)).replace(
        hour=hour, minute=0, second=0, microsecond=0
    )


def _month_delivery(start, description):
    """Return the first workday of the requested month."""
    month = int(description[:-1])
    year = start.year + (month <= start.month)
    result = datetime(year, month, 1, 8, 0)

    while result.weekday() >= 5:
        result += timedelta(days=1)

    return result


def _quarter_delivery(start, description):
    """Return the last workday of the requested quarter."""
    quarter = int(description[1:])
    month = quarter * 3
    year = start.year + (month < start.month)

    if month == 12:
        result = datetime(year + 1, 1, 1, 8, 0)
    else:
        result = datetime(year, month + 1, 1, 8, 0)

    result -= timedelta(days=1)

    while result.weekday() >= 5:
        result -= timedelta(days=1)

    return result


def delivery_date(start, description):
    """Calculate the delivery date from the meeting start and description."""
    start = datetime.fromisoformat(start)

    handlers = {
        "NOW": _now,
        "ASAP": _asap,
        "EOW": _eow,
    }

    if description in handlers:
        result = handlers[description](start)
    elif description.endswith("M"):
        result = _month_delivery(start, description)
    elif description.startswith("Q"):
        result = _quarter_delivery(start, description)
    else:
        raise ValueError("Invalid delivery date description.")

    return result.isoformat()
