from datetime import datetime


def str_to_date(date: str) -> datetime:
    """
    Convert a string to datetime object

    :param date: string to convert
    :return: datetime object

    """
    
    return datetime.strptime(
        date,
        "%Y-%m-%dT%H:%M:%SZ"
    )


def date_to_str(date: datetime) -> str:
    """
    Convert a datetime object to string

    :param date: datetime object to convert
    :return: string
    
    """

    return "{}-{}-{}T{}:{}:{}Z".format(
        date.year, date.month,
        date.day, date.hour,
        date.minute, date.second
    )

