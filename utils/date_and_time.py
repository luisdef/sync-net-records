import datetime
from datetime import datetime as datett


def format_datetime_to_pt_br_standard(timestamp: str) -> str:
    """
    Formats a timestamp string into the standard Brazilian date-time format.

    This function takes a timestamp string and returns a formatted string
    representing the date and time in the Brazilian standard format 
    (DD/MM/YYYY HH:MM:SS).

    Args:
        timestamp (str): A timestamp string to be formatted. This should be 
                         a string representation of a datetime object.

    Returns:
        str: A string representing the formatted date and time in the 
             'DD/MM/YYYY HH:MM:SS' format.

    Raises:
        AttributeError: If the input is not a valid datetime object or does 
                        not have the required attributes like year, month, day, 
                        hour, minute, or second.

    Example:
        >>> from datetime import datetime
        >>> ts = datetime(2024, 8, 27, 14, 30, 45)
        >>> format_datetime_pt_br_standard(ts)
        '27/08/2024 14:30:45'
    """
    return datetime.datetime(
        year=timestamp.year,
        month=timestamp.month,
        day=timestamp.day,
        hour=timestamp.hour,
        minute=timestamp.minute,
        second=timestamp.second
    ).strftime('%d/%m/%Y %H:%M:%S')


def parse_datetime_from_pt_br_standard(date_string: str) -> datett:
    """
    Parses a date-time string in the Brazilian standard format into a datetime object.

    This function takes a date-time string formatted in the Brazilian standard format
    (DD/MM/YYYY HH:MM:SS) and returns a corresponding datetime object.

    Args:
        date_string (str): A date-time string in the 'DD/MM/YYYY HH:MM:SS' format.

    Returns:
        datetime.datetime: A datetime object representing the parsed date and time.

    Example:
        >>> date_str = '27/08/2024 14:30:45'
        >>> parse_datetime_from_pt_br_standard(date_str)
        datetime.datetime(2024, 8, 27, 14, 30, 45)
    """
    return datett.strptime(date_string, '%d/%m/%Y %H:%M:%S')


def seconds_between_dates(d1, d2):
    d1 = parse_datetime_from_pt_br_standard(d1)
    d2 = parse_datetime_from_pt_br_standard(d2)
    return (d1 - d2).seconds


def newer_record(r1, r2) -> list:
    diff = seconds_between_dates(r1["updated_at"], r2["updated_at"])
    if diff >= 0:
        return [r1, diff]
    else:
        return [r2, abs(diff)]

    