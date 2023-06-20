from datetime import date as dt

from dateutil.relativedelta import relativedelta as rdelta
from pytest import mark, raises

from travel_pricing_scraper.flights import flights
from travel_pricing_scraper.models import Flight


def test_invalid_date_format():
    """Test if invalid date format raises ValueError."""
    origin = 'CWB'
    destination = 'POA'
    flight_date = '2021/01/01'

    error_msg = 'Date must be in YYYY-MM-DD format (iso format).'

    with raises(ValueError) as excinfo:
        flights(origin, destination, flight_date)

    assert excinfo.value.args[0] == error_msg


@mark.parametrize(
    'origin, destination, flight_date',
    [('CWB', 'POA', (dt.today() + rdelta(days=1)).isoformat())],
)
def test_flights(origin, destination, flight_date):
    """Test if flights returns a list of Flight objects."""
    result = flights(origin, destination, flight_date)

    assert isinstance(result, list)
    assert all(isinstance(flight, Flight) for flight in result)
