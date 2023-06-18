import uuid
from datetime import datetime as dt

from pydantic import BaseModel, validator


class Flight(BaseModel):
    """Flight model.
    >>> Flight(id=uuid.UUID('50b5e710-db51-424c-b052-8383635ad39d'), origin='CWB', destination='POA', departure_date=dt(2021, 7, 8, 0, 0), arrive_date=dt(2021, 7, 10, 0, 0), price=100.0)
    Flight(id=UUID('50b5e710-db51-424c-b052-8383635ad39d'), origin='CWB', destination='POA', departure_date=datetime.datetime(2021, 7, 8, 0, 0), arrive_date=datetime.datetime(2021, 7, 10, 0, 0), price=100.0)
    """

    id: uuid.UUID = uuid.uuid4()
    origin: str
    destination: str
    departure_date: dt | str
    arrive_date: dt | str
    price: float

    @validator('price')
    def price_must_be_positive(cls, v):
        """Validates that price is positive.
        >>> Flight(id=uuid.UUID('50b5e710-db51-424c-b052-8383635ad39d'), origin='CWB', destination='POA', departure_date=dt(2021, 7, 8, 0, 0), arrive_date=dt(2021, 7, 10, 0, 0), price=-100.0)
        Traceback (most recent call last):
          File "/usr/lib/python3.10/doctest.py", line 1350, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest travel_pricing_scraper.models.Flight.price_must_be_positive[0]>", line 1, in <module>
            Flight(id=uuid.UUID('50b5e710-db51-424c-b052-8383635ad39d'), origin='CWB', destination='POA', departure_date=dt(2021, 7, 8, 0, 0), arrive_date=dt(2021, 7, 10, 0, 0), price=-100.0)
          File "pydantic/main.py", line 341, in pydantic.main.BaseModel.__init__
        pydantic.error_wrappers.ValidationError: 1 validation error for Flight
        price
          price == -100.0 must be positive (type=assertion_error)"""   # doctest: +ELLIPSIS
        assert v > 0, f'price == {v} must be positive'
        return v

    @validator('departure_date', 'arrive_date')
    def datestring_to_datetime(cls, v):
        """Converts date string to datetime.
        >>> Flight(id=uuid.UUID('50b5e710-db51-424c-b052-8383635ad39d'), origin='CWB', destination='POA', departure_date='2021-07-08', arrive_date='2021-07-10', price=100.0)
        Flight(id=UUID('...'), origin='CWB', destination='POA', departure_date=datetime.datetime(2021, 7, 8, 0, 0), arrive_date=datetime.datetime(2021, 7, 10, 0, 0), price=100.0)"""
        if isinstance(v, str):
            return dt.fromisoformat(v)
        return v
