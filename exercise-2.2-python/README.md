# Exercise 2.2 — Python API Client

Weather report fetcher using Open-Meteo public API.

## What it does

Fetches current weather for Sarajevo, Beograd, Zagreb and prints a formatted table.

## Stack

- Python 3.10
- `requests` library
- Open-Meteo REST API (no API key required)

## Run

```bash
python3 weather.py
```

## Concepts learned

- HTTP GET with query parameters
- JSON parsing
- Error handling with `try/except` for specific exception types
- Timeout handling
- Pretty-printing with f-strings and alignment specifiers
