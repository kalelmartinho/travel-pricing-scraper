from pytest import raises

from travel_pricing_scraper.flights import flights


def test_invalid_date_format():
    """Test if invalid date format raises ValueError."""
    origin = 'CWB'
    destination = 'POA'
    flight_date = '2021/01/01'

    error_msg = 'Date must be in YYYY-MM-DD format (iso format).'

    with raises(ValueError) as excinfo:
        flights(origin, destination, flight_date)

    assert excinfo.value.args[0] == error_msg
