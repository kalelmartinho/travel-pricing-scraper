from datetime import date

from playwright.async_api import async_playwright

from ...utils import date_plus_hours


async def decolar_flights(origin, destination, flight_date, passengers=1):
    flight_date = date.fromisoformat(flight_date)

    cluster_css = '.COMMON'
    rows_locator = 'li[class="itinerary-container"]'
    carr_locator = 'span[class="airline-container airline-logo-name-container -have-name"]'

    flights = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=0.5)
        page = await browser.new_page()
        await page.goto(
            'https://www.decolar.com/passagens-aereas/',
            wait_until='load',
            timeout=60000,
        )
        await page.get_by_role('emphasis').filter(
            has_text='Não quero benefícios'
        ).click()
        await page.click('text="Só ida"')
        date_text_locator = 'div[class="sbox5-monthgrid"]'
        origin_input = page.get_by_role(
            'textbox', name='Insira sua cidade de origem'
        )
        dest_input = page.get_by_role(
            'textbox', name='Insira sua cidade de destino'
        )
        date_input = page.get_by_role('textbox', name='Ida', exact=True)
        submit = page.get_by_role('button', name='Buscar')
        await origin_input.click()
        await origin_input.clear()
        await origin_input.type(origin)
        await page.wait_for_timeout(1500)
        await origin_input.press('Enter')
        await page.wait_for_timeout(500)
        await dest_input.click()
        await dest_input.type(destination, delay=100)
        await page.wait_for_timeout(1500)
        await dest_input.press('Enter')
        await date_input.click()
        standard_date = await page.locator(
            date_text_locator
        ).first.get_attribute('data-month')
        standard_date = date(
            int(standard_date[0:4]), int(standard_date[5:7]), 1
        )
        while (
            standard_date.month != flight_date.month
            or standard_date.year != flight_date.year
        ):
            await page.locator('a[class="calendar-arrow-right"]').first.click()
            standard_date = await page.locator(
                date_text_locator
            ).first.get_attribute('data-month')
            standard_date = date(
                int(standard_date[0:4]), int(standard_date[5:7]), 1
            )

        await page.get_by_text(str(flight_date.day), exact=True).first.click()
        await page.wait_for_timeout(500)
        await submit.click()
        await page.wait_for_load_state()
        await page.get_by_role('emphasis').filter(
            has_text='Não quero benefícios'
        ).click()

        # await page.wait_for_timeout(3000)
        await page.wait_for_selector(cluster_css)
        clusters = await page.locator(cluster_css).all()
        for cluster in clusters:
            rows = await cluster.locator(rows_locator).all()
            price = cluster.locator('p[class="item-fare fare-price"]')
            price = await price.locator(
                'span[class="amount price-amount"]'
            ).text_content()
            for row in rows:
                departs = date_plus_hours(
                    flight_date, await row.locator('.leave').text_content()
                )
                arrives = date_plus_hours(
                    flight_date, await row.locator('.arrive').text_content()
                )

                carrier = await (row.locator(carr_locator).text_content())

                flight = {}
                flight['origin'] = origin
                flight['destination'] = destination
                flight['date'] = flight_date.isoformat()
                flight['carrier'] = carrier.strip()
                flight['departure_date'] = departs
                flight['arrive_date'] = arrives
                flight['price'] = price
                flights.append(flight)

    return flights


if __name__ == '__main__':
    print(decolar_flights('CWB', 'POA', '2023-07-08', 1))
