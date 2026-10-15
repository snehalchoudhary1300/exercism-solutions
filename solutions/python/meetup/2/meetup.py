
"""Calculate meetup dates."""

from datetime import date
import calendar


class MeetupDayException(ValueError):
    """Exception raised when the requested meetup date does not exist."""

    def __init__(self, message):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    """Return the date of the requested meetup."""

    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    if day_of_week not in weekdays:
        raise MeetupDayException("That day does not exist.")

    first_weekday, days_in_month = calendar.monthrange(year, month)
    weekday = weekdays[day_of_week]

    if week == "teenth":
        start_day, end_day = 13, 19
    elif week == "first":
        start_day, end_day = 1, 7
    elif week == "second":
        start_day, end_day = 8, 14
    elif week == "third":
        start_day, end_day = 15, 21
    elif week == "fourth":
        start_day, end_day = 22, 28
    elif week == "fifth":
        start_day, end_day = 29, days_in_month
    elif week == "last":
        start_day = max(1, days_in_month - 6)
        end_day = days_in_month
    else:
        raise MeetupDayException("That day does not exist.")

    for day in range(start_day, end_day + 1):
        if day <= days_in_month:
            if date(year, month, day).weekday() == weekday:
                return date(year, month, day)

    raise MeetupDayException("That day does not exist.")
