import locale
from typing import List

import typer
from rich.console import Console
from rich.table import Table
from typer import Option

from .flights import flights as get_flights
from .models import Flight

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
app = typer.Typer()


@app.command()
def flights(
    origin: str = Option(
        ..., help='Origin airport code', prompt='Origin airport code'
    ),
    destination: str = Option(
        ..., help='Destination airport code', prompt='Destination airport code'
    ),
    date: str = Option(
        ...,
        prompt='Date in YYYY-MM-DD format (iso format)',
        help='Date in YYYY-MM-DD format (iso format) e.g. 2021-01-01',
    ),
    passengers: int = Option(1, help='Number of passengers'),
):
    table = Table(title='Flights')
    console = Console()

    table.add_column('Origem')
    table.add_column('Destino')
    table.add_column('Embarque')
    table.add_column('Chegada')
    table.add_column('Preço')
    table.add_column('Companhia')
    flights_list: List[Flight] = get_flights(
        origin, destination, date, passengers
    )

    for flight in flights_list:
        table.add_row(
            flight.origin,
            flight.destination,
            flight.departure_date.strftime('%d/%m/%Y às %H:%M'),
            flight.arrive_date.strftime('%d/%m/%Y às %H:%M'),
            locale.currency(flight.price, grouping=True),
            flight.carrier,
        )

    console.print(table)


if __name__ == '__main__':
    app()
