import asyncio

from ...models import Flight
from .decolar import decolar_flights


async def scrape_flights(origin, destination, flight_date):
    results = []
    tasks = []
    flights = []
    tasks.append(
        asyncio.create_task(decolar_flights(origin, destination, flight_date))
    )
    await asyncio.wait(tasks)
    results = [task.result() for task in tasks]
    for result in results:
        for flight in result:
            flights.append(flight)

    return [Flight(**flight) for flight in flights]
