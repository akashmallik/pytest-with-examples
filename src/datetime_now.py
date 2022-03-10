"""Python datetime module explore"""
import logging
import datetime

LOGGER = logging.getLogger(__file__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logging.StreamHandler())


def get_now() -> str:
    """
    Get current datetime in ISO format
    :return: Current Datetime
    :rtype: str
    """
    now = datetime.datetime.now()
    return now.isoformat()


def get_now_with_timezone(timezone: datetime.tzinfo) -> str:
    """
    Get current datetime in ISO format with timezone
    :param timezone: timezone of the datetime for
    :type timezone: tzinfo
    :return: Current Datetime
    :rtype: str
    """
    now = datetime.datetime.now(tz=timezone)
    return now.isoformat()


if __name__ == "__main__":
    LOGGER.info("Now: %s", get_now())
    LOGGER.info("Now with timezone utc: %s", get_now_with_timezone(datetime.timezone.utc))
