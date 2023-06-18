from datetime import date, datetime


def date_plus_hours(date_var: date, hours: str) -> datetime:
    """Returns a datetime object from a date string and a time string.

    Args:
        date_var (date): Date in date format.
        hours (str): Time in HH:MM format.

    Returns:
        datetime: Datetime object.

    Examples:
        >>> date_plus_hours(date(2021, 1, 1), '12:00')
        datetime.datetime(2021, 1, 1, 12, 0)
    """
    hours = hours + ':00'
    return datetime.fromisoformat(f'{date_var}T{hours}')
