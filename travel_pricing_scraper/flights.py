import asyncio
from datetime import date
from typing import List

from dateutil.relativedelta import relativedelta

from .models import Flight
from .scrapers.flights import scrape_flights

now_isoformat = (date.today() + relativedelta(days=1)).isoformat()


def flights(
    origin: str, destination: str, date: str, passengers: int = 1
) -> List[Flight]:
    """Returns a list of flight prices from origin to destination on date.

    Args:
        origin (str): Origin airport code.
        destination (str): Destination airport code.
        date (str): Date in YYYY-MM-DD format (iso format).
        passengers (int, optional): Number of passengers. Defaults to 1.

    Returns:
        list: List of flight prices.

    Raises:
        ValueError: If origin, destination, or date is invalid.

    Examples:
        >>> flights('CWB', 'POA', '{}'.format(now_isoformat))
        [...]
    """   # doctest: +ELLIPSIS
    if not asyncio.get_event_loop().is_running():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    flights = loop.run_until_complete(
        scrape_flights(origin, destination, date)
    )
    return flights
