# Travel Pricing Scraper

[![Documentation Status](https://readthedocs.org/projects/travel-pricing-scraper/badge/?version=latest)](https://travel-pricing-scraper.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/kalelmartinho/travel-pricing-scraper/actions/workflows/pipeline.yml/badge.svg)](https://github.com/kalelmartinho/travel-pricing-scraper/actions/workflows/pipeline.yml)

## Introduction

The objective of this project is to demonstrate my skills in writing scalable, well-documented, and tested code. For this purpose, i've used Playwright as a web scraping tool to fetch airfare prices. While there are more specialized approaches to extract data of this kind, the main emphasis here is to showcase the ability to develop high-quality code using Playwright. 

In this project, Playwright is used to navigate through different airline websites, fill in search forms, click buttons, and extract price information. It is important to note that in a real production environment, specific solutions would need to be considered for scraping airfare data. However, this project serves as a basic example of my skills in developing scalable, well-documented, and tested code, using Playwright as a widely documented and tested web scraping tool.

## Installation

## How to install

To install the project, we recommend to use `pipx` to install the project in a virtual environment.

```bash
pipx install travel-pricing-scraper
```

This is the recommended way to install the project, but you can also install it using `pip`:

```bash
pip install travel-pricing-scraper
```

Then install playwright dependencies:

```bash
playwright install
```

## How to use

## How to use?
You can use scraper via command line. For example:

```bash
travel-pricing-scraper travels
```
Options
```
Origin airport code: CWB
Destination airport code: POA
Date in YYYY-MM-DD format (iso format): 2023-08-01
```

OR with arguments:
```bash
travel-pricing-scraper  --origin CWB --destination POA --date "2023-08-01"
```

Returns:
                                       

| Origem | Destino | Embarque            | Chegada             | Preço     | Companhia |
| ------ | ------- | ------------------- | ------------------- | --------- | --------- |
| CWB    | POA     | 01/08/2023 às 06:00 | 01/08/2023 às 07:15 | R$ 198,00 | Gol       |
| CWB    | POA     | 01/08/2023 às 16:55 | 01/08/2023 às 18:05 | R$ 198,00 | LATAM     |
| CWB    | POA     | 01/08/2023 às 09:55 | 01/08/2023 às 11:10 | R$ 369,00 | Azul      |
| CWB    | POA     | 01/08/2023 às 09:55 | 01/08/2023 às 11:10 | R$ 369,00 | Azul      |
| CWB    | POA     | 01/08/2023 às 09:55 | 01/08/2023 às 11:10 | R$ 474,00 | Azul      |
| CWB    | POA     | 01/08/2023 às 09:55 | 01/08/2023 às 11:10 | R$ 474,00 | Azul      |
| CWB    | POA     | 01/08/2023 às 11:10 | 01/08/2023 às 15:25 | R$ 278,00 | Gol       |
| CWB    | POA     | 01/08/2023 às 11:50 | 01/08/2023 às 16:15 | R$ 278,00 | Gol       |
