from datetime import datetime as dt

from dateutil.relativedelta import relativedelta as rdelta
from typer.testing import CliRunner

from travel_pricing_scraper.cli import app

runner = CliRunner()


def test_cli_app():
    flight_date = (dt.today() + rdelta(days=1)).strftime('%Y-%m-%d')
    print(flight_date)
    result = runner.invoke(
        app, ['--origin', 'CWB', '--destination', 'POA', '--date', flight_date]
    )
    assert result.exit_code == 0
    assert 'Flights' in result.output
