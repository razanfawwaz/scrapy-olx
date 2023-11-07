# Scraping OLX data using Scrapy

## Installation

First of all, we should initialize the Scrapy project. We started it from create a directory and create an virtual environment.

```bash
mkdir olxbot
cd olxbot
```

Creating the virtual environment:

```bash
python3 -m venv .venv
```

Activating the virtual environment:

```bash
source .venv/bin/activate
```

Installing Scrapy:

```bash
pip install scrapy
```

Creating the Scrapy project:

```bash
scrapy startproject olxbot
```

## Creating the spider

```bash
cd olxbot
```

Code of the spider in [olxbot/spiders/olx.py](olxbot/spiders/olx.py)

## Running the spider

```bash
scrapy crawl olx
```

## Result

The result will be on JSON if you set the config to JSON [Check Result](olxbot.json)
